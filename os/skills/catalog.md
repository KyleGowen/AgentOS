# Skill Catalog

This catalog tracks reusable skills in their natural state and the project-local
translations that make them usable in Codex.

| Skill | Natural Format | Scope | Natural Source | Archived Natural Copy | Codex Translation | Status |
|---|---|---|---|---|---|---|
| `/ticket-to-pr` | Claude Code skill | Measurabl work | `/Users/kyle/.claude/skills/ticket-to-pr/SKILL.md` | `os/skills/native/claude/ticket-to-pr/SKILL.md` | `.agents/skills/ticket-to-pr/SKILL.md` | Translated |
| `/resolve-pr-comments` | Claude Code skill | Measurabl work | `/Users/kyle/.claude/skills/resolve-pr-comments/SKILL.md` | `os/skills/native/claude/resolve-pr-comments/SKILL.md` | `.agents/skills/resolve-pr-comments/SKILL.md` | Translated |
| `/add-card` | Cursor skill | Excelsior | attachment paste | `os/skills/native/cursor/add-card/SKILL.md` | `.agents/skills/add-card/SKILL.md` | Translated |
| `/add-community-deck` | Cursor skill | Excelsior | inline paste | `os/skills/native/cursor/add-community-deck/SKILL.md` | `.agents/skills/add-community-deck/SKILL.md` | Translated |
| `/pdf-to-png` | Cursor skill | Excelsior | inline paste | `os/skills/native/cursor/pdf-to-png/SKILL.md` | `.agents/skills/pdf-to-png/SKILL.md` | Translated |
| `/ship` | Cursor skill | Excelsior | attachment paste | `os/skills/native/cursor/ship/SKILL.md` | `.agents/skills/ship/SKILL.md` | Translated |
| `/start` | Cursor skill | Excelsior | attachment paste | `os/skills/native/cursor/start/SKILL.md` | `.agents/skills/start/SKILL.md` | Translated |
| `/start-aws-db-tunnel` | Cursor skill | Excelsior | attachment paste | `os/skills/native/cursor/start-aws-db-tunnel/SKILL.md` | `.agents/skills/start-aws-db-tunnel/SKILL.md` | Translated |
| `accept-sender-appointments` | Codex skill | Personal productivity | live Gmail/Calendar workflow | None | `.agents/skills/accept-sender-appointments/SKILL.md` | Created |
| `find-card-listings` | Codex skill | Personal collecting | AgentOS automation spec | None | `.agents/skills/find-card-listings/SKILL.md` | Created |
| `arr-current-downloads` | Codex skill | Home Media Server | `KyleGowen/plex-server-hardware/skills/arr-current-downloads` | `os/skills/native/codex/plex-server-hardware/arr-current-downloads/SKILL.md` | Plex repo installed skill | Archived |
| `plex-stack-health-check` | Codex skill | Home Media Server | `KyleGowen/plex-server-hardware/skills/plex-stack-health-check` | `os/skills/native/codex/plex-server-hardware/plex-stack-health-check/SKILL.md` | Plex repo installed skill | Archived |
| `media-internet-search` | Codex skill | Home Media Server | `KyleGowen/plex-server-hardware/tools/codex-skills/media-internet-search` | `os/skills/native/codex/plex-server-hardware/media-internet-search/SKILL.md` | Plex repo installed skill | Archived |
| `overnight-media-audit` | Codex skill | Home Media Server | `KyleGowen/plex-server-hardware/tools/codex-skills/overnight-media-audit` | `os/skills/native/codex/plex-server-hardware/overnight-media-audit/SKILL.md` | Plex repo installed skill | Archived |
| `add-media-to-plex` | Codex skill | Home Media Server | `KyleGowen/plex-server-hardware/tools/codex-skills/add-media-to-plex` | `os/skills/native/codex/plex-server-hardware/add-media-to-plex/SKILL.md` | Plex repo installed skill | Archived |
| `plex-collection-curator` | Codex skill | Home Media Server | `KyleGowen/plex-server-hardware/skills/plex-collection-curator` | `os/skills/native/codex/plex-server-hardware/plex-collection-curator/SKILL.md` | Plex repo installed skill | Archived |
| `itgmania-backup-digest` | Workflow catalog | DDR/ITG Machine | `KyleGowen/itgmania-backup` and `KyleGowen/Thraximundar-Backup` | None | None | Catalog only |

## `/ticket-to-pr`

- Trigger: a Measurabl Jira ticket id such as `WILD-1234` plus a request to take it through implementation and draft PR.
- Inputs: Jira ticket id, related ticket context, user-provided constraints, repository code, tests, GitHub access, and any configured Jira/GitHub connectors.
- Natural state: Claude Code skill, preserved verbatim under `os/skills/native/claude/ticket-to-pr/SKILL.md`.
- Codex state: repo skill under `.agents/skills/ticket-to-pr/`.
- Output: draft GitHub PR, implementation summary, test results, and review flags.
- Verification: Codex skill validation plus real use on a Measurabl ticket before treating the translation as mature.

## `/resolve-pr-comments`

- Trigger: a GitHub PR URL or `owner/repo#number` plus a request to address review comments.
- Inputs: PR metadata, diff, linked Jira ticket, inline review comments, review summaries, PR conversation comments, thread ids, repository code, tests, and GitHub access.
- Natural state: Claude Code skill, preserved verbatim under `os/skills/native/claude/resolve-pr-comments/SKILL.md`.
- Codex state: repo skill under `.agents/skills/resolve-pr-comments/`.
- Output: pushed fixes for agreed comments, PR replies for disagreements, resolved fixed threads, test results, and human follow-up notes.
- Verification: Codex skill validation plus real use on a Measurabl PR before treating the translation as mature.

## Excelsior Cursor Skills

- `/add-card`: add one card image to the Excelsior catalog with approval, Flyway migration, thumbnail config, tests, docs, dev restart, and browser verification.
- `/add-community-deck`: import exported deck JSON into the internal community decks account for the Home rail.
- `/pdf-to-png`: convert image PDFs to PNG at native resolution through the existing Docker Poppler helper.
- `/ship`: run the Excelsior release gate, remove debug noise, commit, and push.
- `/start`: start the v2 local dev stack and report health.
- `/start-aws-db-tunnel`: prepare or start production RDS access through AWS SSM port forwarding.

Each is preserved verbatim under `os/skills/native/cursor/<skill-name>/` and translated into a Codex repo skill under `.agents/skills/<skill-name>/`.

## `accept-sender-appointments`

- Trigger: Kyle asks to accept all appointments, meeting invites, or calendar invitations from a named sender and optionally mark that sender's messages read.
- Inputs: sender name, company, or email/domain; Gmail access; Google Calendar access; optional read-state scope.
- Natural state: live workflow learned from accepting Samantha Young invitations and Rula appointment invites in Gmail/Google Calendar.
- Codex state: repo skill under `.agents/skills/accept-sender-appointments/`.
- Output: accepted Calendar RSVP responses, matching Gmail messages marked read when requested, compact count/date summary.
- Verification: Codex skill validation plus a post-action Gmail unread search for the sender; Calendar RSVP results should show the authenticated user as accepted.

## `find-card-listings`

- Trigger: Kyle asks to scan eBay for wanted OverPower or Magic: The Gathering cards, find active card auctions, monitor wanted cards, add a wanted card, activate a wanted-card entry, or run the wanted-card listing automation.
- Inputs: `os/context/wanted-trading-cards.md`, public eBay listings checked logged out, ended auction comparables, optional image evidence, and retail baselines from The Orange King or Brute Force MTG.
- Natural state: AgentOS automation specification under `os/automations/wanted-card-listings.md`.
- Codex state: repo skill under `.agents/skills/find-card-listings/`.
- Output: active listing report with one price-sorted table per active card, days remaining, links, and compact notes for bulk lots or companion cards. Adding or activating one card triggers a full-list refresh, not a single-card-only report.
- Verification: Codex skill validation plus report spot-checks for logged-out eBay access, omitted ended auctions, and ascending total price sort.

## Home Media Server Codex Skills

These skills belong to the Plex server repo and are archived in AgentOS for context, not installed or translated into `.agents/skills/`.

- `arr-current-downloads`: report active Arr-managed qBittorrent downloads without unrelated or manual torrents. Helper script remains in `KyleGowen/plex-server-hardware/skills/arr-current-downloads/scripts/Get-ArrCurrentDownloads.ps1`.
- `plex-stack-health-check`: validate Plex ecosystem health, Docker containers, service ports, config folders, Windows media paths, native qBittorrent paths, and container mounts. Helper script remains in `KyleGowen/plex-server-hardware/skills/plex-stack-health-check/scripts/Test-PlexStackHealth.ps1`.
- `media-internet-search`: source ambiguous, current, future, collection, chronology, remake, reboot, or public media facts before acting.
- `overnight-media-audit`: report overnight downloads, imports, completions, and blockers in compact capped form. Helper script remains in `KyleGowen/plex-server-hardware/tools/codex-skills/overnight-media-audit/scripts/Get-OvernightMedia.ps1`.
- `add-media-to-plex`: add, search, download, or monitor clear movies and shows through Arr helpers when Kyle asks for acquisition. Helper script remains in `KyleGowen/plex-server-hardware/tools/codex-skills/add-media-to-plex/scripts/Add-ArrMedia.ps1`.
- `plex-collection-curator`: audit, create, fill, update, or posterize Plex collections using the smallest mode implied by Kyle's request. Its non-executable reference docs are archived with the skill.

AgentOS archive scope:

- Copied: `SKILL.md`, `agents/openai.yaml`, and available `references/`.
- Not copied: executable PowerShell helper scripts, generated logs, media ledgers, credentials, or live service configuration.
- Runtime source of truth: the Plex server repo and the installed Windows skill copies documented there.

## ITGMania Backup/Digest Workflow

This is catalog-only AgentOS documentation, not an archived or executable skill.

- Trigger: Kyle asks about DDR/ITG backup status, score digest summaries, play cadence, difficulty trends, score progress, restore safety, or schedule behavior.
- Inputs: `KyleGowen/itgmania-backup` for backup, install, cron, force-push, digest, and score-parsing behavior; `KyleGowen/Thraximundar-Backup` for current backup and digest evidence.
- Process: Use `os/context/stepmania-ddr.md` for routing, read source repos for current facts, summarize digest trends compactly, and preserve the distinction between hobby-log insight and backup-tool mutation.
- Output: digest-coach summaries, source-aware score/progress readouts, or careful plans for backup-tool maintenance.
- Verification: Do not archive PowerShell scripts, Cursor rules, backup data directories, raw XML uploads, large digest mirrors, GitHub PATs, local config, or private credentials in AgentOS.

Force-push, restore, schedule changes, save/config edits, backup repo mutation, or live Thraximundar machine changes require explicit confirmation.
