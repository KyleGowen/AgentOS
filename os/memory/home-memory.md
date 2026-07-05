# Home Memory

Memory for personal projects and non-work context.

Keep this separate from work memory. Home project details can inform home project planning, but should not influence work recommendations.

## Excelsior

- Excelsior is Kyle's main personal software project and creative outlet.
- It serves a small OverPower community with card browsing, deck building, collection tracking, and community features.
- Care points: preserve user data, avoid service disruption, support desktop and mobile UX, and handle the game-owner relationship delicately.
- Near-term interests include adding tournament decks and the next card set.

## Home Media Server

- Home Media Server is Kyle's active Plex server and media automation project.
- Source repo: <https://github.com/KyleGowen/plex-server-hardware>.
- The rebuild is stable as of 2026-07-05.
- The server runs Plex and qBittorrent natively on Windows, with Docker media services for the Arr ecosystem and related tools.
- Kyle often uses Codex remotely from mobile because the server usually has no monitor attached; Parsec is the fallback remote desktop tool for GUI work.
- Care points: keep media drive and path safety front and center, protect all credentials and tracker/provider data, keep AgentOS summary-level, and use the Plex repo for detailed current operations.
- Agent posture: read-only checks are fine when relevant; Plex writes, downloads, deletes, path repairs, drive changes, and service setting changes require clear user intent or confirmation.

## DDR/ITG Machine

- DDR/ITG Machine is Kyle's active StepMania, DDR, and ITGMania hobby-log and exercise project.
- Physical machine identity: Thraximundar, a Windows nukbox DDR/ITG setup.
- Tooling repo: <https://github.com/KyleGowen/itgmania-backup>.
- Backup and digest repo: <https://github.com/KyleGowen/Thraximundar-Backup>.
- Kyle plays for exercise about 1-2 times per week.
- Scheduled backups and digest generation are working as of 2026-07-05.
- Future agents should default to digest-coach behavior: summarize recent play activity, consistency, difficulty range, score progress, and notable songs from source digests.
- Care points: protect GitHub PATs and local config, never casually mutate saves or backup history, avoid medical claims, and confirm before force-push, restore, schedule, save/config, backup repo, or live-machine changes.

## Other Projects

- Add Planted, Vimanas, or other home project memory when those projects become active in AgentOS.
