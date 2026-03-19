---
name: plwiki-sandbox-skill
description: Translate and adapt MediaWiki article source files from English Wikipedia (and similar wikis) into Polish Wikipedia style and markup. Use when converting .mediawiki / wikitext files, localizing article structure, replacing templates, repointing internal links, rewriting categories, cleaning infoboxes/tables, or building/iterating a repeatable workflow for plwiki article preparation.
---

# Plwiki Sandbox Skill

Convert source wikitext into a Polish Wikipedia-ready draft, not a literal translation.

## Core workflow

1. Read the source `.mediawiki` file fully.
2. Identify article type, scope, and risky areas:
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
- internal wikilinks repointed or deliberately left plain if target is doubtful
- templates converted, removed, or flagged with TODO comments
- categories translated/replaced/removed
- references still parse sensibly after translation
- no obvious enwiki-only magic words, hidden categories, or cleanup templates remain

## Template and link handling

Use `references/patterns.md` for recurring conversions.

General rules:

- Convert semantic intent, not template spelling.
- Replace enwiki metadata templates like short description / use mdy dates with plwiki-appropriate omission or local equivalent.
- For `[[link|text]]`, prefer the Polish article target when confidently known.
- If a concept almost certainly has a plwiki article but exact title is uncertain, keep visible anchor text and add a short HTML comment TODO.
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

## Tables and infoboxes

- Preserve factual cell values.
- Localize headers, captions, unit labels, and explanatory notes.
- Replace infobox parameter names only when there is a known plwiki equivalent template/parameter set.
- If infobox conversion is incomplete, prefer a cleaned manual table or a commented TODO over broken fake syntax.

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
