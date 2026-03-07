#!/usr/bin/env python3
"""
Simple gmail post-processor for canonical travel lines.
Usage: gmail_postprocess.py INPUT_FILE
Reads INPUT_FILE, finds lines starting with lot:: / hotel:: / pociąg:: and
normalizes durations to (HhMm) form and outputs validated canonical lines to stdout.
This is a lightweight enforcer for FORMATS.md rules; integrate the script into the
webhook pipeline so that parsed output is passed through it before writing into
workspace files.

Note: This script is intentionally conservative — it will not send or delete
anything. It prints normalized canonical lines; the caller should append them to
flights.md / hotels.md / trains.md and commit as needed.
"""
import sys
import re
from datetime import datetime, timedelta

DUR_RE = re.compile(r"\((\d+)h(\d+)m\)|\\((\d+):(\d+)\\)")
LINE_RE = re.compile(r'^(lot::|hotel::|pociąg::)\s*(.*)$', re.IGNORECASE)
DT_RANGE_RE = re.compile(r'(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2})/(\d{2}:\d{2}|\d{4}-\d{2}-\d{2}T\d{2}:\d{2})')

def normalize_duration(s):
    # If already in (XhYm) leave as is; try to parse HH:MM/HH:MM ranges to duration
    m = DUR_RE.search(s)
    if m:
        return m.group(0)
    m2 = DT_RANGE_RE.search(s)
    if m2:
        start_date = m2.group(1)
        start_time = m2.group(2)
        end = m2.group(3)
        try:
            if len(end) == 5:  # HH:MM same day
                a = datetime.fromisoformat(start_date + 'T' + start_time)
                b = datetime.fromisoformat(start_date + 'T' + end)
            else:
                b = datetime.fromisoformat(end)
                a = datetime.fromisoformat(start_date + 'T' + start_time)
            if b < a:
                # assume arrival next day
                b += timedelta(days=1)
            delta = b - a
            hours = delta.seconds//3600
            minutes = (delta.seconds%3600)//60
            return f'({hours}h{minutes}m)'
        except Exception:
            return ''
    return ''


def process_text(text):
    out = []
    for line in text.splitlines():
        line=line.strip()
        if not line:
            continue
        m = LINE_RE.match(line)
        if not m:
            continue
        kind = m.group(1).lower()
        rest = m.group(2)
        # try to find/normalize duration
        dur = normalize_duration(rest)
        if dur and dur not in rest:
            # insert duration after datetime range if possible
            # naive replace: find first datetime range and append duration
            dtm = DT_RANGE_RE.search(rest)
            if dtm:
                span = dtm.group(0)
                rest = rest.replace(span, span + ' ' + dur, 1)
        out.append(f"{kind} {rest}")
    return '\n'.join(out)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: gmail_postprocess.py INPUT_FILE', file=sys.stderr)
        sys.exit(2)
    path = sys.argv[1]
    with open(path,'r',encoding='utf-8') as f:
        txt = f.read()
    print(process_text(txt))
