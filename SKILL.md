---
name: plwiki-sandbox-skill
description: Translate and adapt MediaWiki article source files from English Wikipedia (and similar wikis) into Polish Wikipedia style and markup. Use when converting .mediawiki / wikitext files, localizing article structure, replacing templates, repointing internal links, rewriting categories, cleaning infoboxes/tables, or building/iterating a repeatable workflow for plwiki article preparation.
---

# Plwiki Sandbox Skill

Convert source wikitext into a Polish Wikipedia-ready draft, not a literal translation.

## Core workflow

Memory and continuity:

- Before continuing work on an article or a skill iteration, recall prior decisions, recurring pitfalls, and workflow preferences from memory when available.
- At the start of work on any plwiki article, first make sure the local skill matches its authoritative repo state; do not begin article work against a stale local skill copy.
- Treat durable preferences learned during plwiki work as part of the reusable workflow; if a lesson keeps recurring, save it in `references/patterns.md` or another focused reference file instead of relying on chat history.
- If access to memory is unavailable in a given runtime, fall back to the local skill references and the article/repo state, then write the newly confirmed lesson back into the skill after the pass.
- Treat `Linki.md` in the skill/repo as a living helper file for Polish Wikipedia editing rules, template docs, policy/help pages, and short local notes distilled from those sources.
- `Linki.md` is primarily for agent use: treat it as a practical "przepisy polskiej Wikipedii" notebook, not user-facing prose.
- When you find an official plwiki help/policy/template-doc page that is likely to matter again, add it to `Linki.md` with a short note about why it matters.
- Adam may append new discoveries to `Linki.md`; read and respect them in future sessions.
- Keep a local copy of `Linki.md` in sync with the authoritative skill repo copy.

GitHub-preview flow:

- This skill lives in its own GitHub repo and should be kept in sync as a first-class workflow repo, not as a workspace backup folder.
- If the human uses GitHub state to generate preview, commit and push after each meaningful pass instead of stopping on local-only changes.
- For durable skill updates Adam is expected to rely on later, default to commit + push without asking unless he explicitly requests local-only work.
- Keep passes small and checkpointed: fix one class of problems, push, inspect preview, then continue.
- After link/template cleanup, run a live plwiki parser preview against the full local wikitext with `action=parse`, not just title-existence checks. Prefer POSTing the whole draft text from the local file so preview reflects the exact unpublished state.
- For plwiki API calls from scripts/helpers, always send an explicit `User-Agent`; on this host bare/default urllib requests can get `HTTP 403`, which is a tooling artifact, not evidence that the page/query is invalid.
- If Adam saved extra fixes directly on-wiki, do not assume the local `PL.mediawiki` still matches live. Fetch the live wikitext first via `action=query&prop=revisions&rvslots=main&rvprop=content|timestamp&titles=<title>` (or `?action=raw`), confirm the exact live title, then diff local vs live.
- When checking whether a published page matches the local draft, verify the target title before comparing content. A narrow local article can publish under a different real plwiki title; in this workflow `Eternalism (philosophy of time)` mapped to live `Eternalizm (filozofia czasu)`, while `Eternalizm` was a different older page.
- For large articles, prefer this order:
  1. get a previewable full draft into `PL/`
  2. fix parser/template/reference errors
  3. expand citations section by section
  4. clean `Zobacz też`, media, and categories
  5. do final dedup/polish
- After finishing an article, also update/push the related skill repo if a reusable lesson was learned; do not leave the workflow improvement only local.

Workspace flow:

- Treat article files in the repo root as the queue of source imports awaiting translation.
- The translated Polish working drafts live in `PL/`, normally under the same filename as the root source article.
- A root-file article should be treated as still pending until its original source file is moved out of the repo root.
- Finished source originals are archived in `done/` under the same filename; if the original is in `done/`, that article is no longer in the root-queue.
- Keep the root source file untouched during translation and review unless Adam explicitly asks for restructuring.
- Do not delete source files yourself unless Adam explicitly asks for it.

Startup checklist for every article:

1. Sync the local `plwiki-sandbox-skill` with its authoritative repo state before doing article work.
2. Refresh the article repo from `origin/main` before reporting queue state or choosing the next file.
3. If Adam may have edited the draft in the visual editor or directly on GitHub, refresh the article repo from `origin/main` again before every new cleanup pass, not only at article start.
4. Pick the source article from the repo root, not from `PL/` or `done/`.
5. Then read the source `.mediawiki` file fully.
6. Identify article type, scope, and risky areas:
   - infobox/template families
   - citations and short-description/date templates
   - internal links likely needing Polish targets
   - categories, navboxes, authority control, stubs
   - tables, lists, pronunciation, names, units, dates
3. Produce a first-pass Polish draft that preserves facts and source-supported structure.
4. Normalize the draft for Polish Wikipedia conventions.
5. Run a quality pass focused on links, templates, categories, references, and natural Polish.
6. Save reusable learnings into this skill when a new recurring pattern appears.

## Non-negotiables

- Prefer correctness on Polish Wikipedia over literal faithfulness to English markup.
- Keep unsupported claims out; do not invent sources or facts.
- Preserve citations unless there is a clear formatting reason to adjust them.
- Rewrite prose into natural Polish, not machine-calque Polish.
- Replace or remove English-wiki-only maintenance templates, categories, and metadata.
- When unsure whether a template exists on plwiki, leave a visible TODO comment near the spot instead of fabricating a template name.

## Minimum output checklist

Before presenting a converted draft, verify:

- lead translated into natural Polish
- bold article title in opening sentence when appropriate
- dates, units, punctuation, and quotations adapted to Polish usage
- inline refs are placed according to plwiki help, normally before closing punctuation; re-check after cleanup passes because edits often move refs to the wrong side
- internal wikilinks repointed or deliberately left plain if target is doubtful
- live parser preview via `action=parse` shows no redlinks in the rendered draft and no obvious parser/template errors
- templates converted, removed, or flagged with TODO comments
- categories translated/replaced/removed
- references still parse sensibly after translation
- footnotes sit in normal plwiki position, usually before closing punctuation (except standard abbreviation-style exceptions)
- no obvious enwiki-only magic words, hidden categories, or cleanup templates remain

Hard stop:
- Do not call a pass "done", "polished", or even "micro-pass complete" until ref placement has been checked article-wide.
- If any refs still sit after the period/comma in normal prose, that is a real mistake, not acceptable polish debt.
- Do not use broad/global regex replacement on `<ref>` punctuation placement. Syntax-blind moves can corrupt references into broken forms like `</ref> name="..."/>`, `<ref. name="..."/>`, or strip the sentence-ending period entirely.
- When fixing ref placement, operate on the current file content and use targeted, syntax-aware edits; then re-check both sides of the sentence boundary: `...<ref/>.` not `....<ref/>` and not `...<ref/> Następne zdanie`.
- Do not replace `<references>...</references>` with `{{Przypisy}}` unless all named-ref definitions have already been inlined or otherwise preserved. A removal pass can create dozens of orphaned named refs at once.

## Template and link handling

Use `references/patterns.md` for recurring conversions.
For article-migration lessons learned from a large medical/controversial article pass, also read `references/havana-lessons.md` when working on citations, infoboxes, media captions, or `Zobacz też` cleanup.

General rules:

- Convert semantic intent, not template spelling.
- Replace enwiki metadata templates like short description / use mdy dates with plwiki-appropriate omission or local equivalent.
- For `[[link|text]]`, prefer the Polish article target when confidently known.
- If a concept almost certainly has a plwiki article but exact title is uncertain, keep visible anchor text and add a short HTML comment TODO.
- If the exact narrow-topic article does not exist but a broader real plwiki article covers the same area, prefer linking to the real broader article with a narrower display label, as long as the wording stays truthful in context.
- Example of the above pattern: prefer a real target such as `[[Filozofia przestrzeni i czasu|filozofii czasu]]` over inventing a non-existent narrow title.
- If no suitable Polish article is likely, remove the wikilink and keep plain text.
- Re-check links inside infobox parameters, hatnotes, navboxes, and table cells.

## Categories

- Remove enwiki categories.
- Replace with Polish categories only when confident.
- Do not translate category names literally unless they match real plwiki naming.
- If category mapping is uncertain, omit categories for now rather than guess.

## References and citations

- Keep citation templates/references intact when possible.
- Translate titles only when the cited work itself has an established Polish title or the surrounding prose needs an explanatory gloss.
- Preserve archive URLs, access dates, and identifiers.
- Do not change publication facts unless correcting an obvious source-side formatting issue.
- On plwiki, prefer simple single-author citation fields unless verified docs clearly support multi-author numbering for the chosen template; imported `imię1` / `nazwisko1` patterns often break preview.
- When several adjacent sentences reuse the same source, convert duplicate literal refs into named refs during cleanup instead of keeping repeated full citation bodies.
- When adding Polish-language sources to an article translated from English, prefer sources tightly about the exact concept or dispute in the article, ideally academic publications or credible university-repository records; do not pad bibliography with merely adjacent philosophy-of-time material just because it is in Polish.


- Before commit/push after citation or link cleanup, require a full `action=parse` preview on the exact local draft, `REDLINKS 0`, no technical error categories (especially `Szablon_cytuj_do_sprawdzenia`), and a clean `python3 scripts/check_ref_punctuation.py <article-file>` result.
- Documentation for `{{Cytuj}}` does not automatically apply to `{{Cytuj pismo}}` or `{{Cytuj książkę}}`; verify less-common params on the exact template variant in live preview instead of assuming inheritance.
- If explicit access status must be shown (`otwarty`, `zamknięty`, `częściowy`), prefer universal `{{Cytuj}}` after preview verification; do not force `|dostęp=` into `{{Cytuj pismo}}` or `{{Cytuj książkę}}` unless the exact variant is proven to support it.
- Do not guess open-access or full-text availability from template docs or vague repository hints; verify against the real landing page, bibliographic record, or direct PDF. If access is closed or uncertain, cite the bibliographic record rather than implying full-text access.

## Tables and infoboxes

- Preserve factual cell values.
- Localize headers, captions, unit labels, and explanatory notes.
- Replace infobox parameter names only when there is a known plwiki equivalent template/parameter set.
- If infobox conversion is incomplete, prefer a cleaned manual table or a commented TODO over broken fake syntax.
- Treat infobox work as preview-driven: verify the exact plwiki template doc first, then add only high-confidence fields, then preview again.
- If a plwiki infobox renders raw `{{{param}}}` placeholders or similar garbage, remove it temporarily rather than leaving a broken infobox in the draft.

## Style guidance

- Write concise, encyclopedic Polish.
- Avoid Anglicisms and word-for-word syntax transfer.
- Expand or reorder sentences when needed for idiomatic Polish.
- Keep proper names in original form unless a standard Polish exonym exists.
- Use Polish date and number formatting in prose.

## Iteration rule

Whenever a new repeatable transformation appears, update `references/patterns.md` with:

- source pattern
- preferred plwiki transformation
- caveats / confidence notes
- one compact example

Read `references/patterns.md` before future conversions and extend it after new learnings.
