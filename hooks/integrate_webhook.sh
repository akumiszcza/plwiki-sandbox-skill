#!/usr/bin/env bash
# integrate_webhook.sh INPUT_FILE
# Reads parser output from INPUT_FILE, normalizes it with gmail_postprocess.py,
# appends canonical lines to the appropriate workspace file (flights.md/hotels.md/trains.md),
# updates Total counters, and commits changes.
set -euo pipefail
INPUT=${1:-}
if [[ -z "$INPUT" ]]; then
  echo "Usage: integrate_webhook.sh INPUT_FILE" >&2
  exit 2
fi
BASE="/home/ubuntu/.openclaw/workspace"
POST="$BASE/hooks/gmail_postprocess.py"
TMP="/tmp/gmail_post_out.$$"
python3 "$POST" "$INPUT" > "$TMP"
# append lines to the right files
while IFS= read -r line; do
  case "$line" in
    lot::*)
      # insert chronologically: append then sort
      echo "$line" >> "$BASE/flights.md.tmp"
      ;;
    hotel::*)
      echo "$line" >> "$BASE/hotels.md.tmp"
      ;;
    pociąg::*|pociag::*)
      echo "$line" >> "$BASE/trains.md.tmp"
      ;;
    *)
      # ignore
      ;;
  esac
done < "$TMP"
# Helper to merge tmp into canonical file and sort by datetime
merge_and_sort(){
  dst="$1"; tmpfile="$2"
  hdr="$(sed -n '1,/^$/p' "$dst" 2>/dev/null || true)"
  # collect existing canonical lines and new ones
  body_lines=$(grep -E '^(lot::|hotel::|pociąg::|pociag::)' "$dst" || true)
  new_lines=$(cat "$tmpfile" || true)
  # write header (if present) then merged lines sorted by date
  # simple sort: rely on ISO date at start of canonical line
  printf "%s\n" "$hdr" > "$dst".new
  printf "%s\n%s\n" "$body_lines" "$new_lines" | sed '/^$/d' | awk '{print $0}' | sort -s -k2,2 >> "$dst".new
  # update totals
  count=$(grep -cE '^(lot::|hotel::|pociąg::|pociag::)' "$dst".new || true)
  # replace Total flights/hotels/trains line if present
  if grep -q '^Total' "$dst"; then
    sed -E "s/^Total [a-zA-Z ]+:[[:space:]]+[0-9]+/Total items: $count/" "$dst".new > "$dst".final || true
    mv "$dst".final "$dst"
  else
    mv "$dst".new "$dst"
  fi
}
# Prepare tmp base files if not exist
for f in flights.md hotels.md trains.md; do
  if [[ ! -f "$BASE/$f.tmp" ]]; then
    touch "$BASE/$f.tmp"
  fi
done
merge_and_sort "$BASE/flights.md" "$BASE/flights.md.tmp" || true
merge_and_sort "$BASE/hotels.md" "$BASE/hotels.md.tmp" || true
merge_and_sort "$BASE/trains.md" "$BASE/trains.md.tmp" || true
# cleanup tmp files
rm -f "$TMP" "$BASE/flights.md.tmp" "$BASE/hotels.md.tmp" "$BASE/trains.md.tmp"
# Commit changes
cd "$BASE"
git add flights.md hotels.md trains.md || true
git commit -m "Webhook: append canonical lines from gmail watcher (automated)" || true
