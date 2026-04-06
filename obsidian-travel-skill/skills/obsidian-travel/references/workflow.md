# Private workflow notes

## Critical default

For Adam's travel-note workflow, this skill is specifically about travel + Obsidian/BIGAI work.
If you change notes or related canonical travel content that Adam is supposed to see, do not stop at local filesystem edits.
Default completion means sync the relevant repo: pull/fetch as needed, `git add -A`, commit, and push without asking.
Only skip push when Adam explicitly requests local-only changes.

## Current storage model

There are two important working areas:
- `/home/ubuntu/.openclaw/workspace`
- `/home/ubuntu/.openclaw/travel-files`

Current assumptions:
- the workspace is the main editing area,
- `travel-files` is the repo that is usually committed/pushed for the travel-files flow,
- BIGAI edits may happen through a temporary clone-on-demand workflow,
- HTTPS + environment token is the confirmed GitHub access path from this host,
- `GITHUB_NEW_TOKEN` is used for vault/BIGAI access and private skill repos.

## Privacy and publishing

- This workflow is private.
- Do not publish this skill to ClawHub unless Adam explicitly decides to change that.
- Never store token values in notes, skill files, or durable memory.

## Obsidian note conventions

For Obsidian travel notes:
- preserve frontmatter unless asked otherwise,
- keep practical note structure,
- avoid destructive cleanup,
- preserve useful attachments by default.

Fixed link block above H1 for Obsidian travel notes:

```text
[[Wyjazdy|Podróże]] | [[Spis podróży]] | [[Checklista.base]] | [[Podróże.base]]
```

## Travel parsing workflow

When handling a booking confirmation:
1. identify whether it belongs to flights, hotels, or trains,
2. extract only values explicitly supported by the source,
3. normalize into a single canonical line,
4. validate the line shape,
5. insert it chronologically into the right file,
6. keep blank-line spacing and counters consistent.

## Gmail retrieval note

When `gog gmail messages search` is not enough for parsing a forwarded booking confirmation:
- use `gog gmail get <messageId> --json --format=full`,
- read the parsed `body` field from the returned JSON,
- extract reservation details from that body text,
- ignore PINs, masked-card details, and payment-update links.

This is the reliable fallback for forwarded Booking.com confirmations when message search output is too shallow.

## Safety / privacy

- never store payment secrets,
- omit uncertain values instead of guessing.
