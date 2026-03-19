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


## Section and article structure

### Section title translation
- Source: common enwiki section headers like `== History ==`, `== Functionality ==`, `== Security and privacy ==`, `== Reception ==`, `== References ==`, `== External links ==`, `==See also==`
- Preferred action: translate into standard plwiki section titles
- Example:
  - `== History ==` -> `== Historia ==`
  - `== References ==` -> `== Przypisy ==`
  - `== External links ==` -> `== Linki zewnętrzne ==`
  - `==See also==` -> `== Zobacz też ==`

## Files and namespace names

### File namespace
- Source: `[[File:...]]`
- Preferred action: convert to plwiki namespace `[[Plik:...]]`

## Navigation and footer templates

### Reflist
- Source: `{{reflist}}`
- Preferred action: replace with plwiki equivalent `{{Przypisy}}`

### Official website template
- Source: `{{Official website|...}}`
- Preferred action: replace with `{{Oficjalna strona|...}}` when available on plwiki

### English navbox/footer template
- Source: article footer template such as `{{Generative AI}}`
- Preferred action: replace with a confident plwiki equivalent if known, otherwise leave TODO or remove
- Example:
  - in: `{{Generative AI}}`
  - out: `{{Sztuczna inteligencja}}` or `<!-- TODO: dobrać odpowiedni szablon na plwiki -->`

## Categories and lists

### Category omission while drafting
- Pattern: source article has only enwiki categories and exact plwiki mapping is uncertain
- Preferred action: omit categories in the draft and add one TODO comment at the end
- Notes: better no category than wrong category

## Infobox localization

### Infobox field localization
- Pattern: infobox template family appears to exist on plwiki, but parameter mapping is only partly known
- Preferred action: localize only high-confidence parameter names, keep the rest omitted or TODO-marked
- Example mappings seen in software articles:
  - `name` -> `nazwa`
  - `other_names` -> `inne nazwy`
  - `developer` -> `autor`
  - `released` -> `data wydania`
  - `programming_language` -> `język programowania`
  - `operating_system` -> `system operacyjny`
  - `genre` -> `rodzaj`
  - `license` -> `licencja`
  - `repo` -> `repozytorium`
  - `website` -> `strona internetowa`
- Notes: verify against real plwiki template docs before treating as fully canonical


## Repo workflow

### Source and PL mirror layout
- Pattern: repo keeps original imported `.mediawiki` files in the root, while Polish conversions live in `PL/`
- Preferred action: save the translated/adapted version as `PL/<same-filename>.mediawiki`
- Notes:
  - do not edit the source import in place during normal conversion work
  - remove the source-root file only when the PL version is fully converted and accepted as done
