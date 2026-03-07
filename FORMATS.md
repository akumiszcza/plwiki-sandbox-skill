# Travel log formats (reference)

Purpose: canonical examples and rules I will use when extracting and writing travel entries.

GENERAL RULES
- Use airport IATA codes only (e.g. GDN, WAW, OTP). Do not write full airport names in formatted lines.
- Use commas, not em dashes.
- Seat notation: compact in braces, e.g. {27ABC} or {8A,8B,8C} for multiple seats.
- Put PNR/ref as `ref XYZ` immediately after airline/flight segment info.
- Times: use ISO-ish compact datetimes: YYYY-MM-DDTHH:MM/HH:MM — eg 2026-07-25T08:25/09:20, with duration in parentheses after the time block.
- Baggage: comma-separated after seats, e.g. `23kg + 8kg + przedmiot osobisty`.
- Layover line: a separate line beginning with the arrow character: `↳ Layover WAW 1h40`.

FLIGHT (single segment) - canonical:

lot:: ORG ⇒ DST 2026-07-25T08:25/09:20 (0h55m) LO3832 (LOT Polish Airlines, Embraer 175) ref XPSUNO {26C}, 23kg + 8kg + przedmiot osobisty
↳ Layover WAW 1h40   # optional, only used when next segment departs from same airport

Notes:
- Each `lot::` must represent a single flight segment (one flight number). For multi-leg journeys, use multiple `lot::` lines plus optional `↳ Layover` lines between connected legs.
- Seat lists inside braces may be a compact string (no spaces) or comma-separated.

HOTEL - canonical:

hotel:: 2026-07-08T13:00/2026-07-13T12:00 Villa Mary Elen (Milos), Apollonia, Pollonia, 84800, Grecja

Notes:
- Use check-in datetime / check-out datetime. Keep location fields as comma-separated address.

TRAIN - canonical:

pociąg:: 2026-03-21T09:48/13:09 GDN Gł. ⇒ POZ Gł. IC 5412 {Wagon 14 kl. 2 miejsca 42,48,51,53} , bilet WH47801539, 170.40 PLN

Notes:
- Use station short names when practical; main rule is keep line compact and include wagon/miejsca in braces.

If you want to change any rule, tell me the exact line to update in FORMATS.md and I will apply it. I will always consult this file when generating formatted lines and when correcting previous entries.
