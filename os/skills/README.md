# Skills

This folder tracks reusable skills created during the course.

Codex-executable repo skills live in `.agents/skills/`. This `os/skills/`
folder is the AgentOS catalog for documenting triggers, process, outputs, and
verification.

Use `catalog.md` to track reusable skills in their native tool format and their
project-local Codex translations. Preserve native skill files under
`native/<tool>/<skill-name>/` before adapting them.

For each skill, capture:

- Trigger: when to use it.
- Inputs: required context or files.
- Process: steps the agent should follow.
- Output: expected artifact or decision.
- Verification: how to check the result.
- Post-run learning: what safe facts, repeated friction, caches, or proposed skill improvements should be recorded after meaningful use.

## Post-Run Learning

Each executable skill should include a compact learning step near the end of its workflow.
Follow the global experiential-learning contract in root `AGENTS.md`; the
skill-specific section should name its approved state or proposal destination.

- Record predictable, safe state in the skill's approved context, memory, output, or runner-owned ledger.
- Capture repeated friction, ambiguity, redundant reads, cache opportunities, and verification shortcuts as proposed improvements.
- Do not store secrets, raw private content, customer details, cookies, API keys, or unnecessary personal data.
- Do not silently rewrite `SKILL.md` after every run. Promote changes into the skill only when the lesson is stable, source-grounded, and likely to reduce future work.
- When judgment is required, leave a short recommendation for Kyle or the OS Thought Partner instead of applying the skill change automatically.

## `/complete NN`

- Codex location: `.agents/skills/complete/`
- Trigger: `/complete NN`, where `NN` is a two-digit AgentOS project number.
- Inputs: Existing `PROJECT_TRACKER.md` entry and matching project notes folder.
- Process: Mark the project complete, mirror status into docs, validate the skill, then commit and push.
- Output: Updated tracker, README Project Index, project notes, and any related playbook sections.
- Verification: Run the skill validator and dry-run invalid or unknown inputs before committing.

## `/ticket-to-pr`

- Codex location: `.agents/skills/ticket-to-pr/`
- Native archive: `os/skills/native/claude/ticket-to-pr/SKILL.md`
- Trigger: a Measurabl Jira ticket id plus a request to take it through development to a draft PR.
- Inputs: Jira ticket content, related tickets, repository code, tests, GitHub access, and any user-provided constraints.
- Process: Research ticket, research code, plan for approval, implement, test, branch/commit/push, and open a draft PR.
- Output: Draft PR URL, implementation summary, test results, and review flags.
- Verification: Validate the Codex skill and forward-test on a real Measurabl ticket.

## `/resolve-pr-comments`

- Codex location: `.agents/skills/resolve-pr-comments/`
- Native archive: `os/skills/native/claude/resolve-pr-comments/SKILL.md`
- Trigger: a GitHub PR URL or `owner/repo#number` plus a request to address review comments.
- Inputs: PR metadata, linked Jira ticket, review comments across all GitHub surfaces, thread ids, repository code, tests, and user approval.
- Process: Read PR, read linked Jira ticket, collect comments, triage agree/disagree/informational, plan for approval, fix or reply, commit/push, and resolve fixed threads.
- Output: Pushed fixes, PR replies, resolved fixed threads, test results, and follow-up notes.
- Verification: Validate the Codex skill and forward-test on a real Measurabl PR.

## Excelsior Cursor Skills

- Codex locations: `.agents/skills/add-card/`, `.agents/skills/add-community-deck/`, `.agents/skills/add-tournament-deck/`, `.agents/skills/api-layer-migration/`, `.agents/skills/pdf-to-png/`, `.agents/skills/ship/`, `.agents/skills/start/`, `.agents/skills/start-aws-db-tunnel/`
- Native archives: `os/skills/native/cursor/<skill-name>/SKILL.md`
- Trigger: Excelsior-specific Cursor slash commands or natural-language equivalents.
- Inputs: Excelsior repo files, local dev services, images/PDFs/deck JSON, AWS/GitHub/npm tooling depending on the skill.
- Process: Preserve native Cursor skill text, translate to Codex `SKILL.md` frontmatter/body, validate the Codex skill, and mature through real Excelsior use.
- Output: Tool-specific Excelsior workflow results such as catalog migrations, community or tournament deck imports, API v1 route migrations, image conversions, dev stack health, release pushes, or DB tunnels.
- Verification: Validate each Codex skill and forward-test in the Excelsior repo before marking mature.

## Excelsior Repo-Local Codex Skills

- Runtime source: `/Users/kyle/cursored/.agents/skills/`
- Native archive: `os/skills/native/codex/excelsior/<skill-name>/`
- Codex locations: owned by the Excelsior repo, not by AgentOS `.agents/skills/`
- Trigger: Excelsior requests to repair Trivy CI failures or start/verify local development.
- Inputs: Excelsior repo status, CI metadata, local dev services, and skill-owned helper scripts in the Excelsior repo.
- Process: Use `os/context/excelsior.md` for routing, then defer to the Excelsior repo skill docs and helper scripts for exact operational steps.
- Output: CI fix reports, pushed fixes when requested, or local API/frontend health summaries.
- Verification: Treat AgentOS copies as context archives; verify live behavior from the Excelsior repo-local skill copies.

Archived skills:

- `fix-trivy`
- `start-local-dev`

Do not copy executable helper scripts out of the Excelsior repo into AgentOS unless the skill ownership decision changes.

## Home Media Server Codex Skills

- Native archive: `os/skills/native/codex/plex-server-hardware/<skill-name>/`
- Runtime source: <https://github.com/KyleGowen/plex-server-hardware>
- Codex locations: owned by the Plex server repo and installed on the Windows server, not by AgentOS `.agents/skills/`
- Trigger: Home Media Server requests about Plex stack health, Arr downloads, overnight activity, public media facts, media acquisition, or Plex collection curation.
- Inputs: Plex repo docs, local Windows server state, relevant installed skill helpers, and explicit user confirmation for live-server mutations.
- Process: Use `os/context/home-media-server.md` for AgentOS routing, then defer to the Plex repo skill catalog and installed skill docs for exact operational steps.
- Output: Compact readouts, confirmations, or Plex repo updates appropriate to the invoked server-specific skill.
- Verification: Treat AgentOS copies as non-executable archives; verify live behavior from the Plex repo and Windows installed skill copies.

Archived skills:

- `arr-current-downloads`
- `plex-stack-health-check`
- `media-internet-search`
- `overnight-media-audit`
- `add-media-to-plex`
- `plex-collection-curator`

Do not copy executable PowerShell helper scripts, generated logs, media ledgers, credentials, or live service configuration into AgentOS. Catalog helper script source paths instead.

## ITGMania Backup/Digest Workflow

- Runtime source: <https://github.com/KyleGowen/itgmania-backup>
- Evidence source: <https://github.com/KyleGowen/Thraximundar-Backup>
- AgentOS context: `os/context/stepmania-ddr.md`
- Trigger: DDR/ITG Machine requests about backup status, digest summaries, play cadence, difficulty trends, score progress, or restore/schedule safety.
- Inputs: tool repo README/context docs, backup repo README, `digests/`, and explicit user confirmation for mutations.
- Process: Use AgentOS context for routing, read the backup repo for current evidence, and read the tool repo for backup, install, cron, force-push, digest, and score-parsing behavior.
- Output: compact digest-coach summaries, source-aware trend readouts, or careful backup-tool plans.
- Verification: Treat this as catalog-only documentation. Do not archive PowerShell scripts, Cursor rules, backup data, raw XML uploads, or large digest mirrors in AgentOS.

Force-push, restore, schedule changes, save/config edits, backup repo mutation, or live Thraximundar machine changes require explicit confirmation.

## `accept-sender-appointments`

- Codex location: `.agents/skills/accept-sender-appointments/`
- Trigger: ask Codex to accept all appointments or meeting invitations from a named sender, optionally marking that sender's messages read.
- Inputs: sender name/email/company, Gmail search results, Google Calendar event matches.
- Process: search unread sender mail, identify appointment or invite messages, find bounded matching Calendar events, accept each event once, then remove `UNREAD` from the requested sender messages.
- Output: accepted appointments, read-state cleanup, and a compact summary with counts and dates.
- Verification: run the skill validator, verify no matching unread sender messages remain when cleanup was requested, and confirm Calendar RSVP responses are accepted.

## `catalog-sdge-energy-alerts`

- Codex location: `.agents/skills/catalog-sdge-energy-alerts/`
- Trigger: ask Codex to process SDGE Energy Use Alert emails, track SDGE electric/gas/solar usage, backfill read or unread SDGE mail, or regenerate the SDGE utility dashboard.
- Inputs: Gmail messages from `notices@sdge.com` in the `SDGE` label, plus the existing `os/data/sdge-energy-alerts/processed-emails.jsonl` ledger when present.
- Process: search ID-first across read and unread SDGE messages, skip only IDs in the local processed-email ledger, read each unprocessed SDGE alert, extract billing/usage/solar facts, upsert the JSONL flat-file database, regenerate the HTML dashboard, update the processed-email ledger, then mark successfully processed message IDs read.
- Output: structured SDGE alert records and `os/reports/sdge-energy-alerts/index.html` with shadcn-styled time-series graphs.
- Verification: run the helper against a sample record, confirm the dashboard regenerates, re-query Gmail until processed IDs are no longer unread, and confirm every matching SDGE ID is either in the local ledger or reported as blocked.

## `find-card-listings`

- Codex location: `.agents/skills/find-card-listings/`
- Trigger: ask Codex to scan eBay for wanted OverPower or Magic: The Gathering cards, add or activate a wanted card, or run the wanted-card listing automation.
- Inputs: `os/context/wanted-trading-cards.md`, public eBay listings, ended auction comparables, and retail baselines from The Orange King or Brute Force MTG.
- Process: read active wanted cards, search eBay logged out, classify exact and bulk/lot matches, remove ended auctions, compare against retail baselines, and sort active listings by price plus shipping.
- Output: game-grouped report with one table per card showing total price, price, shipping, days remaining, listing link, and notes.
- Verification: run the skill validator, confirm no logged-in eBay context was used, and spot-check that ended auctions are omitted from the report.
