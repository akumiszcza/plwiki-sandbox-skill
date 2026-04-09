# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Email

- Adam direct report address: `akumiszcza@gmail.com`
- When Adam asks to send report/link emails, use `akumiszcza@gmail.com` unless he explicitly gives a different target.

## Google / gog

- Preferred Google account for calendar/Gmail CLI work here: `u6133809438@gmail.com`
- Family/shared Google Calendar to query by default: `hp0gd751p5t7kf1uh2ub76ehv4@group.calendar.google.com`
- Display name of that calendar: `Kalendarz Patrycji i Adama`
- If `gog` is missing, install `gogcli` first.
- For VPS/dashboard-only OAuth, use remote flow, not localhost browser flow:
  1. `gog auth add u6133809438@gmail.com --remote --step=1 --services calendar,gmail`
  2. send Adam the printed auth URL
  3. wait for Adam to paste back the final `http://127.0.0.1:.../oauth2/callback?...` URL
  4. run `gog auth add u6133809438@gmail.com --remote --step=2 --auth-url '<returned-url>' --services calendar,gmail`
  5. then query the shared calendar, not the primary calendar

## TTS

- Preferred TTS provider: Microsoft/Edge fallback path in OpenClaw when using `messages.tts.provider = microsoft`
- Preferred WhatsApp voice-reply mode: inbound (reply with audio after inbound voice notes)
- Preferred OpenAI voice: nova
- Preferred Microsoft voice: `pl-PL-ZofiaNeural`
- Voice-reply rule: default to Polish wording with Zofia; use English only when Polish would work noticeably worse or when Adam explicitly asks for English

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
