# MEMORY.md — Long-Term Memory

_Last updated: 2026-04-02_

---

## 🧠 Core Identity
- Sarah, AI assistant with short, friendly, not-formal vibe.
- Prefer feminine self-reference in Polish.

## 👤 User
- User: Adam.
- Prefer replies short but not formal.
- For normal text chat, reply in the same language Adam is using.
- For voice/audio interactions, use Polish TTS by default; preferred Microsoft voice: `pl-PL-ZofiaNeural`.
- Adam's preferred direct email address for reports/links is `akumiszcza@gmail.com`.

## 🏗️ Projects
- Auto-Dream is now configured in this workspace with daily consolidation at 04:00 Europe/Warsaw.
- Telegram added as a primary chat surface via bot `@Sarah_MyClaw_bot`; pairing enabled for Adam.
- Gmail ingestion for `u6133809438@gmail.com` was set up via OpenClaw Gmail Pub/Sub hook + gogcli + gcloud + Tailscale Funnel.
- Ecuador & Galapagos 2026 planning: Warsaw airport hotel is set to Hampton by Hilton Warsaw Airport, and long-trip parking is arranged with Start Parking.
- plwiki `Marry-your-rapist law` article work was finished in `akumiszcza/plwiki-sandbox`; the active file was `PL/Marry-your-rapist law.mediawiki`, archive coverage was substantially expanded, and the article-repo `Linki.md` plus skill copy were updated with durable workflow notes including Cite sub-referencing and `Szablon:Link-interwiki`.

## 📌 Key Decisions
- For Obsidian travel notes and related calendar updates, BIGAI is the canonical GitHub destination unless Adam explicitly says otherwise.
- For BIGAI/Obsidian work, prefer operating on the full local repo clone at `/home/ubuntu/.openclaw/BIGAI` and search across the whole vault instead of fetching or editing isolated single files when local access is sufficient.\n- Before making BIGAI changes, fetch or pull first so work starts from current remote state.
- After making changes in the local BIGAI clone that Adam should see on his side, commit and push them promptly, because Adam does not have practical access to this host's local BIGAI copy.
- Preferred BIGAI rename workflow: fetch/pull first, use `notesmd-cli move` for the rename so wikilinks update, then verify title, H1, and ordinary plain-text mentions the CLI would not rewrite, then `git add -A` so staged changes also include deletion of the old file, then commit and push if Adam needs to see the change remotely.
- For BIGAI vault operations, use `notesmd-cli` rather than the older unrelated `obsidian-cli` package exposed in this environment.
- Local BIGAI path, `notesmd-cli` usage, fetch/pull-first discipline, rename verification, `git add -A`, and git-sync expectations should be reflected not only in memory but also in the Obsidian skill repos when those skills are edited.
- For travel parsing, do not use booking/reservation numbers as flight `ref` unless the document explicitly confirms they are actual carrier or ticket references.
- For family/personal scheduling, prefer the shared calendar `hp0gd751p5t7kf1uh2ub76ehv4@group.calendar.google.com` rather than the connected account's primary calendar.
- For future GitHub access across used repos, prefer `GITHUB_NEW_TOKEN`; never store token values in notes or durable memory.
- For plwiki article work, the canonical article repo is `akumiszcza/plwiki-sandbox`, with local clone at `/home/ubuntu/.openclaw/plwiki-sandbox`; before every translation/cleanup/archive pass, pull there first, and after each meaningful change commit and push promptly because work continues from multiple machines.
- For future Git commits, use `git user.name` = Sarah and `git user.email` = sarah@openclaw.local.
- When I add durable memory/skill learnings Adam wants to survive `/new`, also commit and push the workspace repo so the update persists across resets.

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
- Local persistent clone of `akumiszcza/BIGAI` is available at `/home/ubuntu/.openclaw/BIGAI` and should be the default local working copy for Obsidian/BIGAI tasks unless Adam says otherwise.
- The npm package currently exposed as `obsidian-cli` in this environment is an unrelated Obsidian QA CLI. For vault management here, use Yakitrak `notesmd-cli` instead. It is built locally and should be preferred for search/create/move/delete/frontmatter operations in BIGAI.
- Direct BIGAI access from this host is confirmed via HTTPS + environment token, not SSH.
- Plain unauthenticated `git clone https://github.com/akumiszcza/BIGAI` may fail with `could not read Username`; use environment-backed HTTPS token workflow.
- If `myclaw.ai` dashboard env editing/import is flaky, adding variables directly in `openclaw.json` may work better.
- On this myclaw/VPS deployment, `openclaw gateway restart` from CLI is not the correct restart path because the gateway is dashboard/supervisor-managed and the CLI reports service-disabled/systemd-unavailable. For effective restarts here, use the dashboard restart flow instead.
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
- For future TickTick skill updates, treat `akumiszcza/ticktick-api-skill` as the canonical GitHub destination and commit/push there, not via the workspace repo, unless Adam explicitly says otherwise.
- TickTick skill is not just set up: real usage in Adam's account confirmed inbox review, newest-task listing, quick-add capture, deletion of test tasks, and duplicate-cleanup flows. For inbox maintenance, prefer `project-data inbox125791771` plus client-side sorting/filtering over relying on `filter-tasks` alone.
- `akumiszcza/obsidian-concerts-skill` is private and should not be published to ClawHub unless Adam explicitly changes that decision.
- Plwiki helper references now also explicitly include `Szablon:Biblia` for Bible passages and `Szablon:Odn` for shortened citations; when Adam extends `plwiki-sandbox/Linki.md`, those additions should be read and propagated into the reusable plwiki skill notes.
- New plwiki citation workflow: when native Cite sub-references are available, prefer `<ref name="..." details="..." />` over `{{Odn}}` for simple short-citation setups, especially when `{{Odn}}` would otherwise force a one-item bibliography. Define the full source only once in `<references>`, use `<ref name="ŹródłoRok" />` for unspecific reuse, and `<ref name="ŹródłoRok" details="s. ..." />` for page-specific reuse; do not duplicate the full named ref in article text.
