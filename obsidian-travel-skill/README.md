# obsidian-travel-skill

Private repo/folder for Adam's OpenClaw travel-note skill.

## Status

- visibility: private workflow
- distribution: internal only
- ClawHub: do not publish unless Adam explicitly decides otherwise

## Purpose

This is the main private skill area for Adam's travel workflow in Obsidian/BIGAI.

Default rule for this workflow: if a travel note or related BIGAI/Obsidian content is edited for Adam to see, do not stop at local edits. Finish with pull/fetch as needed, then commit and push without asking, unless Adam explicitly says to keep the change local.

This skill supports a private Obsidian/GitHub travel workflow built around:
- travel notes in markdown,
- canonical travel lines in `flights.md`, `hotels.md`, and `trains.md`,
- BIGAI-style vault editing,
- format stability for booking-derived records.

## Skill included here

### `skills/obsidian-travel`

Use this skill when working on:
- booking-confirmation parsing,
- canonical line creation,
- travel-note cleanup or expansion,
- travel file updates,
- format validation,
- repo/workspace travel workflow recovery.

## Repository layout

```text
skills/
  obsidian-travel/
    SKILL.md
    references/
      examples.md
      formats.md
      recovery.md
      travel-note-template.md
      workflow.md
    scripts/
      validate_canonical_line.py
```

## Auth / repo access

Current private workflow assumes one shared GitHub token env var:
- `GITHUB_NEW_TOKEN` for vault/BIGAI access and private skill repos.

Do not store token values in this repo, in skill files, or in durable memory.
