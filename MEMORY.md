# MEMORY — Canonical travel-format notes

Purpose: short, durable reference for how travel confirmations (emails) are parsed and saved to the workspace files. Keep this brief — full rules live in FORMATS.md.

Canonical summary (short):
- Store machine-canonical lines in workspace files only: flights.md, hotels.md, trains.md.
- Each line must be a single record starting with: lot:: / hotel:: / pociąg::
- Datetimes: ISO 8601 with times: YYYY-MM-DDTHH:MM/HH:MM. For same-date ranges use YYYY-MM-DDTHH:MM/HH:MM (short second part allowed: /HH:MM). Always include times.
- Include duration in parentheses after the time range for flights, e.g. (1h50m).
- Seats: compact curly-brace list, e.g. {26C} or {8ABC,9A}. Do not list per-person seat mapping in the canonical line.
- Refs: label booking refs with "ref <REF>". Include baggage summary when present (e.g. 1x23kg + 8kg + przedmiot osobisty).
- No sensitive data: never store PINs, CVV, full or partial card numbers, or full payment instrument details in canonical lines. 
- Punctuation: use commas, not em dashes. Use arrow `⇒` for origin/destination.

Files:
- FORMATS.md — full canonical formatting rules (source of truth for parsing). Path: /home/ubuntu/.openclaw/workspace/FORMATS.md
- This MEMORY.md entry is a short pointer for future reviewers and automation tests.

When anything changes here, review and update FORMATS.md as authoritative source.

(You can edit this file directly or tell me what to include.)
