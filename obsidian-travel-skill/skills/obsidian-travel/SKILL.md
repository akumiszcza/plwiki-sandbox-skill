---
name: obsidian-travel
description: Maintain private travel notes and canonical travel records for an Obsidian/GitHub workflow. Use when parsing booking confirmations, editing travel notes, updating flights.md, hotels.md, or trains.md, normalizing `lot::` / `hotel::` / `pociąg::` lines, preparing travel entries for BIGAI-style vaults, or checking whether a travel record matches the canonical format.
---

Use this skill for the private travel-note workflow built around Obsidian markdown files and canonical single-line records.

## Critical workflow rule

- This is the primary skill for Adam's travel + Obsidian/BIGAI workflow.
- If you edit travel notes or related BIGAI/Obsidian content Adam is expected to see, do not stop at local edits.
- Default behavior: pull/fetch as needed, edit, `git add -A`, commit, and push without asking.
- Only leave changes local when Adam explicitly asks for local-only work.

## Read only what you need

- Canonical line rules: read `references/formats.md`
- Full travel-note structure, headers, Dataview, and frontmatter rules: read `references/travel-note-template.md`
- Repo/workspace/note workflow rules: read `references/workflow.md`
- Concrete examples: read `references/examples.md`
- Cold start or rebuild: read `references/recovery.md`
- Fragile format validation: use `scripts/validate_canonical_line.py`

## Always follow these rules

- Keep canonical machine-readable records only in `flights.md`, `hotels.md`, and `trains.md`.
- Each canonical line must start with exactly one of: `lot::`, `hotel::`, `pociąg::`.
- Do not invent missing values.
- Do not store payment secrets, card numbers, PINs, or CVV.
- Use commas, not em dashes.
- Use `⇒` for route direction.
- Keep formatting stable and compact.

## When editing travel notes

- Preserve existing frontmatter unless explicitly asked to remove fields.
- Preserve useful existing images and attachments by default.
- Keep notes practical and concise.
- Follow the fixed note structure documented in `references/travel-note-template.md`.
