# Recurring conversion patterns

Keep this file short and practical. Add only patterns that are likely to recur.

## Metadata templates

### Short description
- Source: `{{Short description|...}}`
- Preferred action: remove
- Notes: enwiki maintenance/metadata, usually not carried into plwiki article source
- Example:
  - in: `{{Short description|Open-source autonomous AI assistant software}}`
  - out: removed

### Use mdy dates
- Source: `{{Use mdy dates|date=...}}`
- Preferred action: remove
- Notes: enwiki date-style maintenance template

## Links

### Programming language article targets
- Source: `[[Swift (programming language)|Swift]]`
- Preferred action: repoint to the Polish article if known, otherwise keep plain label with TODO comment
- Example:
  - in: `[[Swift (programming language)|Swift]]`
  - out: `[[Swift|Swift]]` or `Swift <!-- TODO: sprawdzić docelowy artykuł -->`

### Disambiguated biography targets
- Source: `[[Peter Steinberger (programmer)|Peter Steinberger]]`
- Preferred action: use Polish target if it exists; otherwise keep plain linked/unlinked name only after verification
- Notes: do not assume disambiguator format matches enwiki

## Categories

### English categories
- Source: `[[Category:...]]`
- Preferred action: remove unless confident Polish equivalent is known
- Notes: never machine-translate category names blindly

## Infobox/software articles

### Infobox software
- Source: `{{Infobox software ...}}`
- Preferred action: preserve data, but convert only with verified plwiki template/parameter mapping
- Notes: if mapping is incomplete, leave commented TODOs rather than fake parameters

## Article-opening prose

### Literal lead cleanup
- Pattern: English lead translated too literally
- Preferred action: rewrite into natural Polish encyclopedic lead, keeping core facts and sourcing assumptions
- Example:
  - in: `OpenClaw jest wolnym i otwartoźródłowym autonomicznym agentem sztucznej inteligencji...`
  - out: `'''OpenClaw''' to wolne i otwarte oprogramowanie typu autonomiczny agent sztucznej inteligencji, stworzone przez Petera Steinbergera.`
