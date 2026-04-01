# MEMORY.md — Long-Term Memory

_Last updated: 2026-04-01_

---

## 🧠 Core Identity
- Sarah, AI assistant with short, friendly, not-formal vibe.
- Prefer feminine self-reference in Polish.

## 👤 User
- User: Adam.
- Prefer replies short but not formal.
- For normal text chat, reply in the same language Adam is using.
- For voice/audio interactions, use Polish TTS by default; preferred Microsoft voice: `pl-PL-ZofiaNeural`.

## 🏗️ Projects
- Auto-Dream is now configured in this workspace with daily consolidation at 04:00 Europe/Warsaw.
- Telegram added as a primary chat surface via bot `@Sarah_MyClaw_bot`; pairing enabled for Adam.
- Gmail ingestion for `u6133809438@gmail.com` was set up via OpenClaw Gmail Pub/Sub hook + gogcli + gcloud + Tailscale Funnel.
- Ecuador & Galapagos 2026 planning: Warsaw airport hotel is set to Hampton by Hilton Warsaw Airport, and long-trip parking is arranged with Start Parking.

## 📌 Key Decisions
- For Obsidian travel notes and related calendar updates, BIGAI is the canonical GitHub destination unless Adam explicitly says otherwise.
- For travel parsing, do not use booking/reservation numbers as flight `ref` unless the document explicitly confirms they are actual carrier or ticket references.
- For family/personal scheduling, prefer the shared calendar `hp0gd751p5t7kf1uh2ub76ehv4@group.calendar.google.com` rather than the connected account's primary calendar.
- For future GitHub access across used repos, prefer `GITHUB_NEW_TOKEN`; never store token values in notes or durable memory.
- For future Git commits, use `git user.name` = Sarah and `git user.email` = sarah@openclaw.local.

## 💡 Lessons Learned
- Tailscale Funnel had to be enabled in the tailnet UI for Gmail ingestion to work.
- `sudo tailscale set --operator=ubuntu` was needed to allow non-root serve/funnel config.
- gogcli was built from source and exposed via `/usr/local/bin` plus `/usr/bin/gog` symlink so the gateway can find it after restarts.
- Headless gog keyring usage requires `GOG_KEYRING_PASSWORD` in the environment.
- Gateway restarts can stop gmail-watcher if tailscaled or gog are not running; restart tailscaled and run `openclaw webhooks gmail run`.
- Working Gmail body retrieval path in this environment: use `gog gmail messages search "<query>" --include-body --json --results-only` (and `--account u6133809438@gmail.com` when needed). Prefer this for forwarded booking emails when plain message search is not enough.
- In plwiki, footnote placement is a hard-stop QA item: refs should normally appear before closing punctuation, and article-wide ref placement should be explicitly checked before finishing a pass.
- New chat sessions do not delete git history; missing history in `travel-files` happened because it was a newer repo than the older workspace git repo.

## 🔧 Environment
- Two important directories: `/home/ubuntu/.openclaw/workspace` and `/home/ubuntu/.openclaw/travel-files`.
- There is no confirmed persistent local clone of `akumiszcza/BIGAI` at a fixed path on this host.
- Direct BIGAI access from this host is confirmed via HTTPS + environment token, not SSH.
- Plain unauthenticated `git clone https://github.com/akumiszcza/BIGAI` may fail with `could not read Username`; use environment-backed HTTPS token workflow.
- If `myclaw.ai` dashboard env editing/import is flaky, adding variables directly in `openclaw.json` may work better.
- Local calendar quick-reference file: `/home/ubuntu/.openclaw/workspace/local-calendar.md`.

## ⚡ Procedures & Preferences
- Travel confirmations are stored as machine-canonical lines in `flights.md`, `hotels.md`, and `trains.md` only.
- Each travel line must start with `lot::`, `hotel::`, or `pociąg::`.
- Datetimes use ISO 8601 with times; always include times.
- Flight lines include duration in parentheses after the time range.
- Seat notation uses compact curly-brace format like `{26C}` or `{8ABC,9A}` with no per-person mapping.
- Use commas, not em dashes, in formatted travel lines; use `⇒` for origin/destination.
- On each relevant forwarded travel email, reply with a short summary and then one formatted canonical line.
- Maintain travel files in chronological order.
- For non-classical concert notes in Obsidian/BIGAI, use a richer template with header image, official links, band Wiki links, top TODO section, practical items, event time, support acts, and a clearly marked sample/average setlist section when needed.
- Do not remove or replace an existing useful concert graphic by default; keep it or add a new image alongside it.
- For Obsidian plugin tables that sum cancellation-insurance costs, numeric PLN cells must be plain numbers only, with a dot as decimal separator, and without `PLN` / `zł` suffixes; leave cells empty when a currency value is unavailable.
- BIGAI `Brudnopis.md` is the reference scratchpad for nonstandard Markdown patterns to reuse later. It currently documents hidden comments via `[text]: #`, reference-style links, footnotes `[^1]`, strikethrough, highlight `==text==`, and Markdeep HTML trailer usage.
- When Adam asks for Markdown comments / footnotes / TODO-style hidden notes, prefer patterns already documented in `akumiszcza/BIGAI/Brudnopis.md` and treat that file plus its linked docs as the source of truth to check first.
- I can also add my own hidden Markdown comments / TODO markers to draft notes when useful, following the `Brudnopis.md` patterns.

## 🌊 Open Threads
- Consider installing the LCM plugin for working memory: `openclaw plugins install @martian-engineering/lossless-claw`.
- Auto-Dream memory structure is now initialized, but future dreams should keep refining structured sections and episode files.

## 📚 Source Notes
- FORMATS.md remains the authoritative source for detailed travel formatting rules.
- TickTick API skill local path: `/home/ubuntu/.openclaw/workspace/skills/ticktick-api`, repo: `akumiszcza/ticktick-api-skill`.
- `akumiszcza/obsidian-concerts-skill` is private and should not be published to ClawHub unless Adam explicitly changes that decision.
