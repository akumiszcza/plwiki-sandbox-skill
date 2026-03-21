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
  - when a translation is accepted as done, archive the original by moving it to `done/<same-filename>.mediawiki`
  - do not delete source files yourself unless Adam explicitly asks; Adam may still want manual edits first


## References and citation templates

### Convert enwiki citation templates to plwiki citation templates
- Source: `{{Cite web}}`, `{{cite web}}`, `{{cite news}}`, `{{cite magazine}}`
- Preferred action:
  - web pages -> `{{Cytuj stronę}}`
  - newspapers / magazines / periodicals -> `{{Cytuj pismo}}`
- Notes: do not leave English template names in the final plwiki draft

### Prefer Polish parameter names in citation templates
- Pattern: English citation params copied from enwiki
- Preferred action: convert to Polish primary parameter names used on plwiki
- Common mappings:
  - `last` -> `nazwisko`
  - `first` -> `imię`
  - `title` -> `tytuł`
  - `date` -> `data`
  - `access-date` -> `data dostępu`
  - `website` -> `opublikowany`
  - `work` -> `praca`
  - `archive-url` -> `archiwum`
  - `archive-date` -> `zarchiwizowano`
  - `author-link` -> `autor link`
- Notes: plwiki docs explicitly prefer primary Polish names, even if some aliases may work

### Normalize citation dates to ISO-like form
- Pattern: English textual dates inside citation templates
- Preferred action: use `RRRR-MM-DD` whenever full date is known
- Notes: applies especially to `data`, `data dostępu`, `zarchiwizowano`

### Remove unsupported enwiki-only citation params
- Pattern: params like `url-status=live`
- Preferred action: remove unless there is a confirmed plwiki equivalent in active use

### Paywalled article note
- Pattern: source has `url-access=subscription`
- Preferred action: replace with an explicit Polish note or template only if there is a confirmed plwiki convention; otherwise add a small manual note
- Current safe draft pattern: `|id={{Subskrypcja wymagana}}`
- Notes: verify later whether a better house style exists on plwiki


### Verify actual plwiki page titles before repointing links
- Pattern: enwiki disambiguated links often do not match plwiki titles exactly
- Preferred action: search plwiki and use the real target title
- Examples:
  - `[[Swift (programming language)|Swift]]` -> `[[Swift (język programowania LLVM)|Swift]]`
  - `[[Claude (language model)|Claude]]` -> `[[Claude (model językowy)|Claude]]`
  - `[[large language model]]` -> `[[Duży model językowy]]`

### Prefer real plwiki infobox template names
- Pattern: translated or guessed infobox names such as `Infobox oprogramowanie`
- Preferred action: replace with the actual plwiki template name after verification
- Example:
  - guessed: `{{Infobox oprogramowanie ...}}`
  - verified: `{{Oprogramowanie infobox ...}}`

### Software infobox field mapping, verified on plwiki
- Verified template: `{{Oprogramowanie infobox}}`
- High-confidence mappings:
  - `name` -> `nazwa`
  - `developer` -> `autor`
  - `released` -> `pierwsze wydanie`
  - `programming_language` -> `język programowania`
  - `operating_system` -> `system operacyjny`
  - `genre` -> `rodzaj`
  - `license` -> `licencja`
  - `website` -> `www`
- Notes: `repo` is not a standard visible field in the verified plwiki infobox template doc fetched during OpenClaw pass

### Category selection for software drafts
- Pattern: article about open-source software with AI focus and MIT license
- Preferred action: add only broad, clearly verified categories when article-specific ones are uncertain
- Safe examples used in OpenClaw draft:
  - `[[Kategoria:Wolne i otwarte oprogramowanie]]`
  - `[[Kategoria:Oprogramowanie na licencji MIT]]`
  - `[[Kategoria:Sztuczna inteligencja]]`


### Oprogramowanie infobox strictness on plwiki
- Pattern: `{{Oprogramowanie infobox}}` rejects guessed fields and expects plain file/url values in some fields
- Preferred action:
  - use only documented parameters
  - `logo` should usually be the bare filename, not embedded `[[Plik:...]]`
  - `www` should be a plain URL, not `{{URL|...}}`
  - `pierwsze wydanie` works reliably with `{{Dts|DD|MM|YYYY}}`
  - unsupported guessed fields like `inne nazwy` should be moved into article prose, not forced into the infobox
- Notes: if preview reports "Nieznane pola" or "Nieprawidłowe/puste pola", treat the template docs as authoritative and simplify


### `Cytuj pismo` uses `czasopismo`, not `praca`
- Pattern: enwiki `cite news` / `cite magazine` converted to `{{Cytuj pismo}}`
- Preferred action: map publication title to `|czasopismo=`

### Footnotes usually go before closing punctuation
- Pattern: after translation or cleanup, inline refs drift to the wrong side of a period/comma
- Preferred action: in normal prose, place the `<ref>...</ref>` or `<ref name="..." />` before the closing punctuation of the supported sentence or clause
- Notes: treat this as a preview-time quality check, not just final polish; re-check after larger rewrites because ref positions drift easily
- Do not use: `|praca=` inside `{{Cytuj pismo}}`
- Example:
  - in: `{{cite news |work=The Verge |title=...}}`
  - out: `{{Cytuj pismo |czasopismo=The Verge |tytuł=...}}`
- Notes: preview errors on plwiki explicitly flag `praca` as unknown for this template


### Polish footnote punctuation rule
- Pattern: inline references in Polish prose
- Preferred action: place `<ref>...</ref>` immediately after the referenced word/phrase and before the punctuation mark ending the sentence or clause
- Example:
  - correct: `...w autentyczny sposób<ref>...</ref>.`
  - wrong: `...w autentyczny sposób.<ref>...</ref>`
- Notes:
  - treat this as a final proofreading pass item for every article
  - treat this as a high-priority preview check, not optional polish
  - after larger cleanup passes, re-check the whole article because automated rewrites can easily push refs back to the wrong side of punctuation

### Safer external-link fallback for broken sister-project templates
- Pattern: interwiki/sister-project template renders badly or points to a dead target
- Preferred action: replace it with a normal external link until a verified local template form is known
- Example: replace a broken `{{wikisource|...}}` with `* [URL label]`


### Broken red utility templates in external links
- Pattern: imported article uses helper templates that do not exist on plwiki, e.g. GitHub / official-site templates
- Preferred action: replace them with normal external links using a clear Polish label
- Examples:
  - `{{GitHub|https://github.com/org/repo}}` -> `[https://github.com/org/repo Repozytorium projektu w serwisie GitHub]`
  - broken official-site helper -> `[https://example.com Oficjalna strona]`

### Prefer simpler Polish sentences over source-like clause stacking
- Pattern: translated sentence keeps too many English-style subordinate clauses
- Preferred action: split into two shorter Polish sentences when readability improves
- Example: describe the incident first, then explain the consent issue in a second sentence


### Cite language consistently for foreign-language sources
- Pattern: some foreign-language references display `(ang.)` while others do not because `język=` is present only on some citations
- Preferred action: add `|język=` consistently for non-Polish sources when the source language is clear
- Common values:
  - English sources: `|język=en`
  - US English sources may also appear as `|język=en-US`, but prefer one consistent style within the article when practical
  - Chinese external links in prose/link sections should be visibly labeled in Polish, e.g. `(w języku chińskim)`
- Notes: consistency improves reader expectations in generated citation output

### Footnote placement rule from plwiki help page
- Source: `Pomoc:Przypisy`
- Rule: place the footnote marker directly after the supported text and before punctuation; exception: if the sentence ends with an abbreviation already ending in a period, place the footnote after that period and do not duplicate the period
- Notes: treat `Pomoc:Przypisy` as the authoritative citation-placement reference for future conversions


### `język` is recommended for non-Polish sources in both citation templates
- Source: `Szablon:Cytuj pismo` and `Szablon:Cytuj stronę`
- Preferred action: whenever the cited source is not in Polish, fill `|język=` with the language code
- Examples:
  - English -> `|język=en`
  - Dutch -> `|język=nl`
  - US English can still be represented as `|język=en` for consistency across one article unless a more specific code is useful
- Notes: if some foreign-language refs have `język` and others do not, normalize them for consistency in rendered output


### Put foreign-language sister-project links in External links, not See also
- Pattern: a related link points outside plwiki, especially to a sister project in another language
- Preferred action: place it in `== Linki zewnętrzne ==` with a Polish description and visible language note
- Notes: `Zobacz też` should prefer internal Wikipedia navigation, not offsite or foreign-language destinations

### Prefer natural grammatical agreement in infobox values
- Pattern: imported adjective values like `cross-platform` translated mechanically
- Preferred action: match adjective form to the field label in Polish
- Examples:
  - `platforma sprzętowa = wieloplatformowa`
  - `system operacyjny = wieloplatformowy`

### Prefer explicit Polish explanations over workspace jargon in article prose
- Pattern: source-derived text mentions `workspace` or other product-internal jargon too literally
- Preferred action: rewrite into explanatory Polish, even if it becomes slightly longer
- Example:
  - instead of `skille z lokalnego workspace'u`
  - prefer `skille przechowywane w lokalnej przestrzeni roboczej`


## Iterative preview workflow

### Large-article preview cycle
- Pattern: long article conversion is too large to perfect in one pass
- Preferred action:
  1. create a first full Polish draft in `PL/`
  2. if preview is driven from GitHub, commit and push that checkpoint
  3. send it for live plwiki preview
  4. fix parser/template/link/reference problems reported by the preview in small passes
  5. repeat until preview is clean enough for manual editorial review
- Notes: for large articles, prioritize getting to a previewable full draft over polishing every citation in the first pass

### Preview-driven fixing order
- Preferred order after receiving plwiki preview feedback:
  1. red/broken templates and parser errors
  2. empty or broken references
  3. footnote placement and citation rendering rules from plwiki (`Pomoc:Przypisy`)
  4. obvious wrong or red internal links
  5. section/portal/footer cleanup
  6. style and prose refinement
- Notes: this order gives the fastest path to a usable next preview

### Lead simplification must not orphan named references
- Pattern: a cleanup pass removes or rewrites a lead sentence that previously contained the defining `<ref name="...">...</ref>` for a named citation used later in the article
- Preferred action: after removing that sentence, move the full reference definition to the first remaining in-body use before pushing
- Notes: otherwise preview may show `Brak tekstu w przypisie o nazwie ...`

### Published-article handoff
- Pattern: article has been accepted/published on plwiki and the original source file is archived to `done/`
- Preferred action:
  1. confirm the published title/link
  2. note any final lessons worth preserving in the skill
  3. treat the repo state (`PL/`, root, `done/`) as the new baseline before starting the next article
- Notes: do not keep reasoning from the previous article implicit across `/new`; write durable workflow lessons down first
