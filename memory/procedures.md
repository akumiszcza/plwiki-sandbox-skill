# Procedures — How I Do Things

_Last updated: 2026-04-14_

---

## 🎨 Communication Preferences
- Prefer replies that are short but not formal.
- For normal text chat, reply in the same language Adam is using.
- For voice/audio interactions, default to Polish.
- When Adam asks me to send a report or link by email, default the recipient to `akumiszcza@gmail.com` unless he explicitly gives a different address.

## 🔧 Tool Workflows
- Travel email workflow: on each relevant forwarded email, reply with (1) a short summary, then (2) one canonical line starting with `lot::`, `hotel::`, or `pociąg::`.
- For forwarded Gmail booking emails in this environment, use `gog gmail messages search "<query>" --include-body --json --results-only` to get full body content; add `--account u6133809438@gmail.com` when needed.
- For headless/dashboard-only Google Calendar/Gmail re-auth on this VPS, use `gog auth add u6133809438@gmail.com --remote --step=1`, have Adam return the final localhost callback URL, then finish with `--step=2`; do not go back to the localhost browser flow.
- Keep `flights.md`, `hotels.md`, and `trains.md` sorted chronologically.
- If Telegram messages seem to disappear, check whether the gateway restarted mid-reply.
- `agent-browser` is installed globally in `~/.openclaw/skills/agent-browser`; Playwright browsers were installed and browser default preference points there.
- When I add durable memory or skill learnings Adam explicitly wants to survive `/new`, also commit and push the workspace repo so the change persists across resets.
- For plwiki work, read `/home/ubuntu/.openclaw/plwiki-sandbox/Linki.md` first, treat it as the practical citation/template notebook, and sync durable additions back into `/home/ubuntu/.openclaw/workspace/skills/plwiki-sandbox-skill/Linki.md`.
- If Adam says a plwiki page is already live, then before any later fixes or cleanup passes first refresh the local `PL.mediawiki` from the current live plwiki raw, and only then continue editing.
- For plwiki QA, trust live preview/template errors over heuristic local checks; explicitly check ref placement before punctuation, validate citation-template compatibility against `Linki.md`, and run a real wiki preview/parser check before push on larger citation/linking passes.
- For plwiki "is local identical to live?" checks, run a fresh `git pull` or `git pull --rebase` immediately before the diff and compare against the article's actual live title.
- For planned-but-missing Polish pages, use `{{link-interwiki|1=...|Q=...|tekst=...}}` only when the Wikidata anchor is solid; use `tekst=` for inflection and prefer plain text over a guessed interwiki when the item is weak.
- In plwiki work, prefer lowercase `{{link-interwiki}}` over `{{Link-interwiki}}`; both forms work, but lowercase survives human/autocorrect cleanup better.
- In plwiki citations, `{{Cytuj książkę}}` should not use `archiwum` / `zarchiwizowano`; archived links stay in `url=` with `data dostępu=`. `{{Cytuj pismo}}` uses `wolumin`, first-author `imię`/`nazwisko`, and book editors can go in `inni=... (red.)`.
- Use `{{ang.|...}}` with the dot for foreign-language glosses in plwiki, and do not use it for wikilinks.
- In plwiki refs, add `język=` for foreign-language sources by default; for Polish sources, only when it actually helps.
- If the default model falls back after an update or restart, use: `openclaw models` -> `openclaw config set agents.defaults.model.primary "openai-codex/gpt-5.4"` -> `openclaw models`; the short micro-reload from `config set` is usually sufficient.

## 📝 Format Preferences
- For Obsidian plugin tables that auto-sum cancellation-insurance costs, keep PLN values as raw numbers with `.` decimal separator, no currency suffix (`PLN`, `zł`), and leave missing values blank.
- Travel seat notation should be compact, like `{27ABC}`.
- Do not use per-person seat mapping in canonical travel lines.
- In formatted travel lines, use commas instead of em dashes.
- Do not mention `czas lokalny` in canonical travel lines.
- Airport arrow formatting `AAA ⇒ BBB` is preferred and bolded in `flights.md` for better Obsidian rendering.

## ⚡ Shortcuts & Patterns
- Model config lesson: `openai/gpt-5.4` may work at the API layer but still fail in OpenClaw model resolution; allowlist/alias config may be needed.
- Cost-control lesson: default model was moved to `openai/gpt-5-mini` with fallback `openai/gpt-5.2`.
- Git history lesson: missing history in `travel-files` was because it was a newer repo than the older workspace repo, not because new chat sessions delete git history.
- Resilio Sync lesson: Resilio 3.1.2 crashed with unsupported config keys `log_file` and `log_level`; the setup was later removed and GitHub became the chosen sharing method instead.
