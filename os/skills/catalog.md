# Skill Catalog

This catalog tracks reusable skills in their natural state and the project-local
translations that make them usable in Codex.

| Skill | Natural Format | Scope | Natural Source | Archived Natural Copy | Codex Translation | Status |
|---|---|---|---|---|---|---|
| `os-map` | Codex skill | AgentOS maintenance | `projects/10-playbook/agentos-system-map.html` and AgentOS source files | None | `.agents/skills/os-map/SKILL.md` | Created |
| `/ticket-to-pr` | Claude Code skill | Measurabl work | `/Users/kyle/.claude/skills/ticket-to-pr/SKILL.md` | `os/skills/native/claude/ticket-to-pr/SKILL.md` | `.agents/skills/ticket-to-pr/SKILL.md` | Translated |
| `/resolve-pr-comments` | Claude Code skill | Measurabl work | `/Users/kyle/.claude/skills/resolve-pr-comments/SKILL.md` | `os/skills/native/claude/resolve-pr-comments/SKILL.md` | `.agents/skills/resolve-pr-comments/SKILL.md` | Translated |
| `/add-card` | Cursor skill | Excelsior | attachment paste | `os/skills/native/cursor/add-card/SKILL.md` | `.agents/skills/add-card/SKILL.md` | Translated |
| `/add-community-deck` | Cursor skill | Excelsior | inline paste | `os/skills/native/cursor/add-community-deck/SKILL.md` | `.agents/skills/add-community-deck/SKILL.md` | Translated |
| `/add-tournament-deck` | Cursor skill | Excelsior | `/Users/kyle/cursored/.cursor/skills/add-tournament-deck/SKILL.md` | `os/skills/native/cursor/add-tournament-deck/SKILL.md` | `.agents/skills/add-tournament-deck/SKILL.md` | Translated |
| `/api-layer-migration` | Cursor skill | Excelsior | `/Users/kyle/Projects/excelsior/.cursor/skills/api-layer-migration/SKILL.md` | `os/skills/native/cursor/api-layer-migration/SKILL.md` | `.agents/skills/api-layer-migration/SKILL.md` | Translated |
| `/pdf-to-png` | Cursor skill | Excelsior | inline paste | `os/skills/native/cursor/pdf-to-png/SKILL.md` | `.agents/skills/pdf-to-png/SKILL.md` | Translated |
| `/ship` | Cursor skill | Excelsior | attachment paste | `os/skills/native/cursor/ship/SKILL.md` | `.agents/skills/ship/SKILL.md` | Translated |
| `/start` | Cursor skill | Excelsior | attachment paste | `os/skills/native/cursor/start/SKILL.md` | `.agents/skills/start/SKILL.md` | Translated |
| `/start-aws-db-tunnel` | Cursor skill | Excelsior | attachment paste | `os/skills/native/cursor/start-aws-db-tunnel/SKILL.md` | `.agents/skills/start-aws-db-tunnel/SKILL.md` | Translated |
| `fix-trivy` | Codex skill | Excelsior | `/Users/kyle/cursored/.agents/skills/fix-trivy/SKILL.md` | `os/skills/native/codex/excelsior/fix-trivy/SKILL.md` | Excelsior repo-local skill | Archived |
| `start-local-dev` | Codex skill | Excelsior | `/Users/kyle/cursored/.agents/skills/start-local-dev/SKILL.md` | `os/skills/native/codex/excelsior/start-local-dev/SKILL.md` | Excelsior repo-local skill | Archived |
| `accept-sender-appointments` | Codex skill | Personal productivity | live Gmail/Calendar workflow | None | `.agents/skills/accept-sender-appointments/SKILL.md` | Created |
| `find-card-listings` | Codex skill | Personal collecting | AgentOS automation spec | None | `.agents/skills/find-card-listings/SKILL.md` | Created |
| `catalog-sdge-energy-alerts` | Codex skill | Personal utilities | live Gmail SDGE alerts | None | `.agents/skills/catalog-sdge-energy-alerts/SKILL.md` | Created |
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
- `/add-tournament-deck`: import exported deck JSON into the internal tournament decks account for the Home Tournament Winning Decks rail.
- `/api-layer-migration`: migrate legacy Express routes to the `/api/v1` layer with services, DTOs, docs, tests, local restart, and browser proof.
- `/pdf-to-png`: convert image PDFs to PNG at native resolution through the existing Docker Poppler helper.
- `/ship`: run the Excelsior release gate, remove debug noise, commit, and push.
- `/start`: start the v2 local dev stack and report health.
- `/start-aws-db-tunnel`: prepare or start production RDS access through AWS SSM port forwarding.

Each is preserved verbatim under `os/skills/native/cursor/<skill-name>/` and translated into a Codex repo skill under `.agents/skills/<skill-name>/`.

Repo-local Codex skills discovered in Excelsior:

- `fix-trivy`: debug and fix Excelsior GitHub Actions Trivy dependency-vulnerability failures, with a helper script in `/Users/kyle/cursored/.agents/skills/fix-trivy/scripts/run_trivy_ci_scan.py`.
- `start-local-dev`: start or verify the Excelsior root API on 8085 and Vite frontend on 5173, with final `/health` verification via `/Users/kyle/cursored/.agents/skills/start-local-dev/scripts/start_local_dev.py`.

These are archived under `os/skills/native/codex/excelsior/` for AgentOS context. Their executable helper scripts remain owned by the Excelsior repo.

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
- Output: active listing report grouped by game, with one price-sorted table per active card, days remaining, links, and compact notes for bulk lots or companion cards. Adding or activating one card triggers a full-list refresh, not a single-card-only report.
- Verification: Codex skill validation plus report spot-checks for logged-out eBay access, omitted ended auctions, and ascending total price sort.

## `catalog-sdge-energy-alerts`

- Trigger: Kyle asks to process SDGE Energy Use Alert emails, catalog SDGE utility metrics, backfill read or unread SDGE mail, or regenerate the SDGE usage dashboard.
- Inputs: Gmail access to `notices@sdge.com` messages in the `SDGE` label, plus `os/data/sdge-energy-alerts/processed-emails.jsonl` when present.
- Natural state: live Gmail workflow over Kyle's filtered SDGE notices.
- Codex state: repo skill under `.agents/skills/catalog-sdge-energy-alerts/`.
- Output: JSONL utility records, a processed-email ledger, and `os/reports/sdge-energy-alerts/index.html` with charges, projections, kWh, therms, solar export, and other tracked metrics.
- Verification: helper-script sample ingest/report check, all-status Gmail ID comparison against the local ledger, and final Gmail unread re-query after any read-state cleanup.

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
