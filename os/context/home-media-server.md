# Home Media Server

Repository-state audit: 2026-08-17. The current `main` branch records Korlash
as up and running after its replacement-platform rebuild, with Plex native to
Windows and the media-automation stack in Docker. The remaining documented
risk is intermittent system crashing; do not claim a root cause without new
evidence.

This file summarizes Kyle's Plex server project for AgentOS routing and planning. The source of truth for detailed operations is the project repo:

<https://github.com/KyleGowen/plex-server-hardware>

## Purpose

Home Media Server is Kyle's Windows-native Plex server and media automation ecosystem. It exists to operate, document, and safely evolve the Korlash Plex server without losing media, corrupting paths, leaking secrets, or making risky live-server changes casually.

Treat the project as active home operations with balanced priorities across
reliability, backups, service validation, media automation, collections, and
poster curation. The Plex repository is the authoritative documented state;
verify the host directly before making a claim about its live, moment-to-moment
health.

## Architecture Summary

Summary only. Verify current details in the Plex repo before acting.

| Area | Summary |
|---|---|
| Repository | `KyleGowen/plex-server-hardware` |
| Operating model | Windows-native server with Docker media services |
| Native Windows services | Plex Media Server and qBittorrent |
| Docker media stack | Sonarr, Radarr, Prowlarr, Bazarr, Tautulli, Uptime Kuma, Homarr, and Unpackerr |
| Optional legacy service | Jackett, only when intentionally needed |
| Storage model | Windows drive letters mounted into containers |
| AgentOS role | Routing, safety, memory, and skill catalog context |
| Plex repo role | Detailed inventories, trackers, service docs, ledgers, scripts, logs, and current operational state |

## Source Map

Use these Plex repo files instead of duplicating detailed state here:

| Need | Plex repo source |
|---|---|
| Assistant operating rules | `AGENTS.md` |
| Current status and hardening | `docs/plex_server_rebuild_wip_tracker.md` |
| Hardware inventory | `docs/plex_server_hardware_inventory.md` |
| Software inventory | `docs/plex_server_software_inventory.md` |
| Service details | `docs/services/*.md` |
| Drive/path safety | `docs/drive_reconnect_validation_checklist.md` and `docs/qbittorrent_startup_recovery.md` |
| Skills | `docs/skills_catalog.md` plus `skills/` and `tools/codex-skills/` |
| Media collections and show records | `COLLECTIONS.md`, `TV_SHOWS.md`, `collections/`, and `tv-shows/` |

## Remote Workflow

Kyle often uses Codex remotely from a mobile device because the server usually does not have a monitor attached. Parsec is the fallback remote desktop tool when a GUI session is needed.

Agent behavior:

- Prefer concise, stepwise outputs that are usable from mobile.
- Start with read-only checks and compact summaries.
- Avoid long raw command output unless Kyle asks for it or the evidence is necessary.
- Assume the session may be remote and awkward; make next actions explicit.
- For GUI-only tasks, mention Parsec as the likely access path.

## Safety Boundaries

Read-only checks are acceptable when relevant. Live-server mutations require clear user intent or confirmation.

Do not casually:

- Format, initialize, repartition, wipe, or treat any media drive as disposable.
- Change drive letters.
- Repair application paths before verifying drive letters, qBittorrent paths, and Docker bind mounts.
- Trigger Plex library refreshes.
- Start downloads, searches, imports, deletes, torrent actions, metadata edits, or service setting changes unless Kyle's request or the invoked skill authorizes that action.

Before trusting media automation after boot, crash, Docker restart, WSL restart, or storage work, confirm the relevant Windows paths and container mounts in the Plex repo's current docs and tools.

## Privacy Boundaries

Do not mirror these into AgentOS:

- Plex tokens.
- Arr API keys.
- qBittorrent credentials.
- Tracker data, private tracker URLs, cookies, passkeys, magnets, torrent hashes, and provider credentials.
- Raw logs or generated evidence that may contain secrets.
- Detailed media library, collection, or show ledgers.

AgentOS may store summary context, source pointers, safety rules, and stable workflow preferences.

## Skill Routing

The Plex repo owns executable server-specific skills. AgentOS archives non-executable skill docs under `os/skills/native/codex/plex-server-hardware/` and catalogs them in `os/skills/catalog.md`.

Use the Plex repo skill catalog to choose the workflow:

| Request shape | Skill |
|---|---|
| What is downloading now | `arr-current-downloads` |
| Stack health, service ports, folders, paths, mounts | `plex-stack-health-check` |
| Current or ambiguous public media facts | `media-internet-search` |
| Overnight downloads, imports, stuck items | `overnight-media-audit` |
| Add/search/download a clear movie or show | `add-media-to-plex` |
| Audit, create, fill, update, or posterize Plex collections | `plex-collection-curator` |

For exact live-server behavior, defer to the Plex repo's installed skill docs and current helper scripts.
