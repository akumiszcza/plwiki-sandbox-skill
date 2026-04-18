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

### Prefer lowercase `{{link-interwiki}}`
- Pattern: a future/planned plwiki target is linked through `Link-interwiki`
- Preferred action: write the template as lowercase `{{link-interwiki|...}}`
- Notes: uppercase `{{Link-interwiki}}` also works, but lowercase is the practical house style in this workflow and survives autocorrect/manual touch-ups better

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

### Published-page follow-up pass
- Pattern: Adam says the page is already live on plwiki and wants another cleanup or archive pass
- Preferred action: fetch the current live raw into the local `PL.mediawiki` before editing
- Notes:
  - even if the repo was synced earlier, live raw is the source of truth for the next pass
  - if the published page rewrites repeated refs into named definitions inside `<references>...</references>`, repoints some wikilink targets, or adds `{{Kontrola autorytatywna}}`, keep that literal live shape for the sync checkpoint instead of immediately restyling it back to the pre-publish draft
  - this also applies when live keeps or restores wording/link choices that differ from the latest local polish pass; checkpoint the exact published state first, then do any cleanup in a separate follow-up pass
  - if Adam asks only to "dociągnąć" the live page, an exact raw sync is still the goal even when the only diff is cosmetic byte-shape such as a final newline at EOF; confirm repo = live explicitly instead of skipping the checkpoint as a no-op

### After `/new` or compacted resume, verify repo state before trusting prior claims
- Pattern: the session resumes after `/new`, compaction, replay, or any context where earlier chat claims may be partial or stale
- Preferred action: check `git log`, `git status`, and the current article file before reporting what was already done or choosing the next pass
- Notes: repo state is stronger evidence than recollection or an earlier assistant summary

### Do not overwrite a fuller local draft just because live exists
- Pattern: live plwiki raw exists, but the local `PL.mediawiki` is visibly broader or more source-rich
- Preferred action: diff live vs local first and merge carefully instead of replacing local with live wholesale
- Notes: use live as the baseline for publication state, not as an excuse to discard unpublished improvements


## References and citation templates

### Core plwiki citation template references
- Keep these as the primary template docs to consult when citation preview breaks or parameter names are uncertain:
  - `Szablon:Cytuj pismo` - https://pl.wikipedia.org/wiki/Szablon:Cytuj_pismo
  - `Szablon:Cytuj książkę` - https://pl.wikipedia.org/wiki/Szablon:Cytuj_książkę
  - `Szablon:Cytuj stronę` - https://pl.wikipedia.org/wiki/Szablon:Cytuj_stronę
  - `Szablon:Cytuj` - https://pl.wikipedia.org/wiki/Szablon:Cytuj
- When fixing imported enwiki references, prefer aligning fields with these plwiki docs over guessing aliases from enwiki habits.

### Avoid `doi=` in `{{Cytuj stronę}}` unless preview proves it safe
- Pattern: a web-page citation carries a DOI and the draft uses `{{Cytuj stronę}}`
- Preferred action: omit `doi=` from `{{Cytuj stronę}}` unless the exact draft passes live preview with it
- Notes: on plwiki this can trigger hidden citation-error categories such as `Szablon_cytuj_do_sprawdzenia`; if the DOI matters, prefer a bibliographic variant better matched to the source

### Archive lookup pass: only confirmed snapshots
- Pattern: a reference-cleanup pass is adding archives to existing citations
- Preferred action: add `archiwum=` / `zarchiwizowano=` only for snapshots confirmed by Wayback/CDX
- Notes:
  - if the source URL already points to Archive.org, treat it as already archived and do not hunt a redundant Wayback snapshot
  - do not force Wayback into `{{Cytuj książkę}}`; for book citations with only an archived copy, use the full Wayback URL directly in `url=` and keep `data dostępu=`
  - prefer CDX or equally direct snapshot evidence over the weaker Wayback `available` endpoint; `available` can return no snapshot even when CDX later shows captures
  - if `available` is empty, treat that as "not yet confirmed", not as proof that no archive exists

### No `archiwum=` pass for book citations
- Pattern: an archive-cleanup pass encounters `{{Cytuj książkę}}`
- Preferred action: do not add `archiwum=` / `zarchiwizowano=` to book citations as a normal cleanup step
- Notes:
  - if the citation is to the book itself, keep it as a normal book ref without Wayback fields
  - if the only usable online witness is an archived page or scan, put that archived address directly in `url=` instead of mixing book metadata with archive parameters
  - if live plwiki removes an archive from a book ref, treat that as the correct shape and sync it back to the repo instead of restoring the archive locally

### Retry canonical OUP article URL when `article-abstract` has no snapshot
- Pattern: an Oxford Academic citation uses `/article-abstract/...` and Wayback says there is no snapshot
- Preferred action: retry the canonical `/article/...` URL before giving up on archive lookup
- Notes: snapshots may exist only for the canonical article page even when the draft currently cites the abstract form


### Verify parameter support per citation-template variant
- Pattern: a generic citation-template doc suggests a field such as `dostęp=`
- Preferred action: verify the exact target template variant in live preview; do not assume `{{Cytuj pismo}}` or `{{Cytuj książkę}}` inherit every field supported by `{{Cytuj}}`
- Notes: preview may expose `Nieznane pola: "dostęp"` and hidden error categories such as `Szablon_cytuj_do_sprawdzenia`

### Prefer `{{Cytuj}}` for explicit access-status labels
- Pattern: the draft needs to say that a source is `otwarty`, `zamknięty`, or `częściowy`
- Preferred action: convert the relevant ref to universal `{{Cytuj}}` when practical, then use `dostęp=...` there if preview confirms the exact draft renders cleanly; avoid forcing `dostęp=` into `{{Cytuj pismo}}` or `{{Cytuj książkę}}`
- Notes: rerun full parser preview afterward, keep a bibliographic-record link when full text is not openly available, treat standalone `{{Otwarty dostęp}}` / `{{Paywall}}` as fallback only, and remember that page ranges in `{{Cytuj}}` use `s=` rather than `strony=`
- Example:
  - in: `<ref>{{cytuj pismo | autor = A | tytuł = T | czasopismo = J | data = 2024 | doi = 10.1234/x}}</ref>`
  - out: `<ref>{{Cytuj | autor = A | tytuł = T | czasopismo = J | data = 2024 | s = 1–8 | doi = 10.1234/x | dostęp = otwarty}}</ref>`

### In `{{Cytuj}}` use `s=` for page ranges, not `strony=`
- Pattern: a ref is normalized from `{{Cytuj pismo}}` / `{{Cytuj książkę}}` / imported enwiki template into universal `{{Cytuj}}`
- Preferred action: rewrite page ranges to `|s=` in the final `{{Cytuj}}` call
- Notes: `|strony=` may look plausible from other template variants, but on plwiki it can trigger `Szablon_cytuj_do_sprawdzenia` in live preview; verify on the exact draft after conversion
- Example:
  - in: `{{Cytuj | autor = David W. Allan | tytuł = Statistics of atomic frequency standards | strony = 221–230 }}`
  - out: `{{Cytuj | autor = David W. Allan | tytuł = Statistics of atomic frequency standards | s = 221–230 }}`

### Verify real OA/full-text availability before encoding it
- Pattern: a repository record or helper page makes access status look ambiguous
- Preferred action: inspect the real landing page or direct PDF before marking the source as open/closed/partial in the citation
- Notes:
  - if the full text is closed or uncertain, point to the bibliographic record instead of implying open full-text access
  - keep three questions separate: archive existence, landing-page accessibility, and actual full-text openness
  - anti-bot `403` or similar blocking is not by itself proof that the source is closed to human readers

### Prefer direct paywall evidence over aggregator OA hints
- Pattern: an OA aggregator or metadata service suggests access, but the publisher page shows a purchase wall, login wall, or user-confirmed closed access
- Preferred action: treat the source as closed unless a real open full-text URL can be reached directly
- Notes: do not mark `otwarty` on the strength of `OpenAlex`, DOI metadata, or a bot-check page alone; observed paywall / purchase requirement is stronger evidence

### Commit gate after bibliography or link cleanup
- Pattern: a citation/link pass looks correct locally and is about to be committed
- Preferred action: before commit/push, run full `action=parse` preview on the local draft and `python3 scripts/check_ref_punctuation.py <file>`
- Success condition: `REDLINKS 0`, `ERROR_CATS 0`, no `Szablon_cytuj_do_sprawdzenia`, and script output like `OK: no obvious ref/punctuation issues found`

### Ignore edit-section UI links when scraping redlinks from parser HTML
- Pattern: a helper scans `action=parse` HTML for redlinks and reports fake targets such as `Edytuj kod źródłowy sekcji: ...`
- Preferred action: ignore anchors inside `mw-editsection` / edit-section UI chrome and count only redlinks coming from article content
- Notes: otherwise parser-based QA can falsely report redlinks even when the draft itself is clean

### Broader real target with narrower display label
- Pattern: a narrow concept lacks a plwiki page, but a broader verified page covers the same area
- Preferred action: link to the broader real page with a narrower display label if the statement stays truthful in context
- Example:
  - `[[Filozofia przestrzeni i czasu|filozofii czasu]]`
- Notes: remove the link entirely if the broader target would distort the meaning

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

### Pull again after visual-editor changes
- Pattern: Adam edits the article in the visual editor or directly on GitHub during an ongoing cleanup session
- Preferred action: refresh the article repo from `origin/main` again before the next pass, even if it was already synced earlier in the session
- Notes: do not keep patching against stale local content; visual-editor changes can silently invalidate line-based fixes

### Raw/broken ref opener cleanup
- Pattern: malformed raw refs such as `<ref.>`, `<ref,>`, `<ref >`, `<ref. name="..."/>`, `<ref, name="..."/>`
- Preferred action: normalize them immediately to valid `<ref>` / `<ref name="..."/>` syntax before doing any other cleanup around citations
- Notes: these often appear after visual-editor/manual edits or after unsafe automated punctuation passes

### Refs before punctuation, but keep the final period
- Pattern: a sentence-ending citation should sit before punctuation on plwiki
- Preferred action: use `...tekst<ref .../>.` or `...tekst<ref>...</ref>.`
- Notes: fixing `.<ref` is only half the job; verify that the sentence still ends with a literal period after the ref when the prose requires one

### Remove red author links inside references
- Pattern: author names inside citation/ref entries render as red links or add noisy low-value linking
- Preferred action: in references, prefer plain-text author names over redlinked author wikilinks
- Notes: keep links in refs only when they are clearly useful and high-confidence; in most citation author fields, plain text is cleaner than red author links

### Remove stray trailing punctuation from reference definitions
- Pattern: a reference definition inside `== Przypisy ==` ends with an extra literal period outside the citation template/content, e.g. `<ref name="Pessoa">{{Cytuj książkę|...}}.</ref>`
- Preferred action: remove the stray punctuation from inside the ref definition unless it is truly part of quoted source text
- Notes: this kind of extra period is easy to miss in source but produces inconsistent reference formatting

### Prefer normalized title/plain-text forms in references over raw identifier-like wikilinks
- Pattern: a cited work title appears as a raw or machine-like wikilink that is likely to render red or unnatural on plwiki, e.g. underscore-separated forms such as `[[Maggid_Mesharim]]`
- Preferred action: prefer a normal readable title in plain text (or a verified plwiki target if one clearly exists) instead of keeping the raw identifier-shaped wikilink
- Notes: titles copied from URLs, database ids, or underscore forms should be treated with suspicion during citation cleanup

### Preserve named-ref definitions when replacing reflists
- Pattern: article has `<references>...</references>` containing named ref definitions used in body text
- Preferred action: do not replace the block with bare `{{Przypisy}}` unless those definitions are preserved elsewhere; if needed, rebuild a minimal `<references>` block containing only actually-used named definitions
- Notes: otherwise preview will flood with `zdefiniowany w <references>, nie był użyty` or missing-definition errors after subsequent edits

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

### Mark foreign-language forms with plwiki language templates
- Pattern: article needs to show a foreign-language term, script form, or original wording inline
- Preferred action: prefer plwiki-style markup such as `{{ang.|...}}`, `{{W języku|kod|tekst}}`, or language-specific shortcuts like `{{chiń.|...}}` instead of raw labels like `po chińsku:`
- Example:
  - plain draft: `fuji (po chińsku: 扶乩/扶箕)`
  - better plwiki draft: `fuji ({{chiń.|扶乩}}, także {{chiń.|扶箕}})`

### Prefer real plwiki infobox template names
- Pattern: translated or guessed infobox names such as `Infobox oprogramowanie`
- Preferred action: replace with the actual plwiki template name after verification
- Example:
  - guessed: `{{Infobox oprogramowanie ...}}`
  - verified: `{{Oprogramowanie infobox ...}}`

### Film infobox strictness on plwiki
- Verified template: `{{Film infobox}}`
- Preferred action:
  - use the real template name `Film infobox`, not guessed variants like `Infobox film`
  - keep only high-confidence fields already known to render cleanly
  - if preview reports `Nieznane pola`, remove the unsupported field instead of forcing it into the infobox
- Known safe fields from the `Capturing Bigfoot` pass:
  - `tytuł`
  - `grafika`
  - `opis grafiki`
  - `gatunek`
  - `rok produkcji`
  - `data premiery`
  - `kraj produkcji`
  - `język`
  - `czas trwania`
  - `reżyseria`
  - `muzyka`
  - `zdjęcia`
  - `produkcja`
- Known failure example:
  - `producenci wykonawczy` -> preview reports `Nieznane pola`
- Notes: for film articles, recover the infobox only after preview confirms the exact plwiki template name and field set

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
  - if a user already corrected this once, treat any repeat as a process failure and update the draft before calling the pass complete
  - do not rely on memory alone; consciously scan the article for `.<ref` and `,<ref` patterns before push or handoff

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

### Expand a developed live article, do not collapse it back to a stubby summary
- Pattern: the current plwiki/live article already has substantial section structure and sourced detail
- Preferred action: preserve that structure and add verified detail where needed instead of rewriting it into a much shorter synthetic overview
- Notes: this matters especially for biography and philosophy/science articles where live already contains multiple thematic sections

### Lock preferred Polish terminology once chosen
- Pattern: during review Adam or the article context establishes a Polish preferred term for something that also has an English source-language label
- Preferred action:
  - once the Polish form is chosen, keep using it consistently in article prose
  - keep the English form only as an explanatory gloss, source-language marker, or first-mention helper when useful
  - do not drift back to the English form later as if it were a neutral synonym
- Example:
  - preferred: `[[Wielka Stopa (kryptozoologia)|Wielka Stopa]] ({{ang.|Bigfoot}})` on first mention, then `Wielka Stopa` later
  - avoid: mixing `Wielka Stopa` and `Bigfoot` interchangeably in later Polish prose
- Notes: if the article itself marks a term with `{{ang.|...}}`, treat that as evidence that the English form is source-language annotation, not the default Polish running term

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


### Remove or replace unsupported enwiki citation params (expanded list)
- Pattern: params that plwiki `Cytuj pismo` / `Cytuj książkę` / `Cytuj stronę` do not support
- **Always remove when importing from enwiki:**
  - `tom` (volume) — `Cytuj pismo` does not have a volume field; omit it
  - `hdl` (Handle identifier) — unknown in all three plwiki cite templates
  - `artykuł` — enwiki alias for article-number, not accepted on plwiki
  - `redaktor` (without number suffix) — use `redaktor1=` or omit
  - `url rozdziału` — not a valid param in `Cytuj książkę`; either omit or move the URL to `url=`
  - `url-status` — enwiki-only param, remove silently
- **Safe equivalents or workarounds:**
  - For `url rozdziału` in `Cytuj książkę`: either omit the chapter URL or move it to `url=` if needed
  - For `artykuł`: the article/chapter identifier can usually be kept as `id=CDXXXXXX` or omitted
- Notes: when preview reports "Nieznane pola", consult this list first before guessing

### Infoboks leków na plwiki — szablon „Infobox drug" nie istnieje
- Pattern: enwiki uses `{{Infobox drug}}` for pharmaceutical/vaccine articles
- Preferred action: do NOT use `{{Infobox drug}}` on plwiki — it renders as a red broken template
- Verified plwiki alternative: `{{Lek}}` or `{{Leki infobox}}` — check current plwiki docs before use
- Safe fallback when unsure: omit the infobox entirely in the draft and add a TODO comment, rather than using a broken red template
- Notes: this applies to vaccine articles and any drug/pharmaceutical article imported from enwiki

### Szablony nawigacyjne — `{{Szczepionki}}` nie istnieje na plwiki
- Pattern: enwiki uses `{{Vaccines}}` navbox; automatic translation to `{{Szczepionki}}` produces a red template
- Preferred action: check whether a plwiki navigation template for vaccines exists before using it; if uncertain, omit and add a TODO comment
- Notes: do not guess Polish navbox names from English equivalents — always verify first

### Poprawna składnia obrazków na plwiki — kolejność parametrów
- Source: `Pomoc:Ilustrowanie` na plwiki
- Preferred action: użyj kolejności `right|thumb` (lub `left|thumb`), NIE `miniatura|prawo`
- Canonical form: `[[Plik:nazwa.jpg|right|thumb|Opis podpisu]]`
- Aliases `miniatura` i `prawo` są technicznie akceptowane przez parser, ale powodują problemy z rozpoznawaniem capta i renderowaniem podpisu; angielskie `right|thumb` jest bezpieczniejsze
- Do NOT use: `miniatura|prawo|opis` — opis może nie być renderowany jako podpis
- Use: `right|thumb|opis` — opis zawsze widoczny jako podpis pod miniaturką

### `{{Legenda}}` w podpisach map — użycie wewnątrz capta
- Szablon `{{Legenda|kolor|tekst}}` istnieje na plwiki i działa
- Poprawne użycie: wewnątrz capta znacznika `[[Plik:...|right|thumb|tekst intro\n{{Legenda|...}}\n{{Legenda|...}}]]`
- Błąd poprzedni: stosowanie `miniatura|prawo` powodowało że cały caption nie był rozpoznawany — stąd legenda „wypadała" z obrazka
- Po naprawieniu kolejności na `right|thumb` szablony `{{Legenda}}` w capcie działają poprawnie
- Nie umieszczaj `{{Legenda}}` poza znacznikiem `[[Plik:...]]` jeśli chcesz legendę widoczną jako część podpisu obrazka

### Archiwa przypisów (`archiwum=` / `zarchiwizowano=`)
- Dla przypisów z `|url=` bez archiwum można półautomatycznie uzupełniać `|archiwum=` i `|zarchiwizowano=` przez Wayback Machine API, ale sam endpoint `available` traktuj tylko jako szybki sygnał, nie jako dowód braku snapshotu
- W tym środowisku preferuj prosty skrypt Python do odpytania Wayback API; bashowe tablice/expansje mogą zostać zablokowane jako obfuscation
- Gdy wynik ma znaczenie redakcyjne, preferuj twarde potwierdzenie snapshotu przez CDX albo równoważny bezpośredni zapis
- Jeśli snapshot istnieje, wpisz prawdziwy adres Wayback w formie `https://web.archive.org/web/YYYYMMDDHHMMSS/original-url`
- `zarchiwizowano=` ustawiaj jako `YYYY-MM-DD` wyciągnięte z timestampa Wayback
- Nie wpisuj jako `archiwum=` zwykłego permalinku strony, share URL ani linku z parametrami `?st=...`, `reflink=...`, `fbclid=...` itp. To nie jest archiwum
- Jeśli w artykule live jest zły `archiwum=` ale poprawka jest drobna, można po prostu odesłać poprawiony ref jako tekst do ręcznej podmiany na wiki, bez zbędnego commita do repo pomocniczego
- Przy QA przypisów sprawdzaj, czy tytuł źródła faktycznie odpowiada treści artykułu/tabeli; przykład błędu do unikania: dokument WHO o yellow fever użyty jako źródło tabeli o wymogach meningokokowych

### Mapy / grafiki w szablonie thumb — upright zbyt duże
- Pattern: an SVG map with `upright=1.9` or larger renders as an oversized image that dominates the preview, especially for complex map graphics
- Preferred action: reduce `upright` value (e.g. to `upright=1.2` or `upright=1.3`) or use `width=` in pixels to control the displayed size
- Notes: very wide SVG maps often need explicit size control; prefer smaller values initially and let Adam adjust

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
