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
