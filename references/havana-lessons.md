# Havana-syndrome pass: reusable plwiki lessons

Add only lessons likely to recur in future article conversions.

## Citation templates

### Multi-author fields can break plwiki preview
- Pattern: imported citation uses `imię1`, `nazwisko1`, `imię2`, `nazwisko2`, etc. inside `{{Cytuj stronę}}` or `{{Cytuj pismo}}`
- Preferred action: simplify to a single verified author field unless plwiki docs for that exact template clearly support the numbered form
- Notes: in preview-driven drafting, a working single-author citation is better than a broken perfect-author citation

### Deduplicate repeated full refs after stabilization
- Pattern: article reaches clean preview, but identical `<ref>...</ref>` bodies repeat many times
- Preferred action: convert one instance into a named ref and replace later copies with `<ref name="..." />`
- Notes: do this after parser/template stability, not before

## Infoboxes

### `Choroba infobox` should be added cautiously
- Pattern: medical/health article on plwiki may tempt direct early infobox insertion
- Preferred action:
  1. read the plwiki template doc first
  2. add only high-confidence fields
  3. explicitly leave unsupported/unknown fields empty or omitted according to the doc
  4. preview immediately
- Failure mode: if preview shows raw `{{{param}}}` placeholders, remove the infobox and retry later with stricter field selection

## Media

### Prefer plain captions over red links in image labels
- Pattern: imported/enriched article gets section images whose depicted building/place has no plwiki article
- Preferred action: keep the image, but use plain Polish caption text instead of forcing a red wikilink
- Example:
  - `[[Plik:...|thumb|Ambasada Stanów Zjednoczonych w Wiedniu]]`
  - not `[[Plik:...|thumb|[[Ambasada Stanów Zjednoczonych w Wiedniu]]]]`

## See also

### Keep `Zobacz też` internal and existing
- Pattern: enwiki `See also` contains topics without plwiki articles
- Preferred action: keep only real plwiki pages in `== Zobacz też ==`; remove plain-text items and non-existent targets instead of leaving them there
- Notes: foreign/sister-project links belong in `== Linki zewnętrzne ==`, not `Zobacz też`
