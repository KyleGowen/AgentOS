# Project History

Compact history of meaningful outcomes and milestones. This is not a full changelog.

## AgentOS

### 2026-07-19 - Automation Efficiency Review Added

- Added `os/automations/automation-efficiency-review.md` as a daily 6:30 AM Pacific review-only optimization digest.
- The automation reviews recent scheduled runs and future automation candidates, then recommends token and efficiency improvements by skill without applying changes until Kyle approves them.

### 2026-07-16 - Accept Sender Appointments Skill Created

- Promoted the repeated Gmail and Google Calendar cleanup workflow into the Codex skill `.agents/skills/accept-sender-appointments/`.
- The skill accepts appointments from a named sender and can mark the sender's matching Gmail messages read when requested.

### 2026-07-16 - First AgentOS Automation Added

- Added `os/automations/auto-accept-appointments.md` as the first harness-neutral automation spec.
- Created a Codex scheduled automation to run the appointment-acceptance skill every 2 hours from 7:00 AM through 11:00 PM for active allowlisted senders.

### 2026-07-03 - Project 04 Memory Framework Drafted

- Built a memory organization plan around working memory, persistent memory, domain-separated files, and explicit maintenance rules.
- Enabled Codex built-in memories in `~/.codex/config.toml`.
- Added repo guidance so future agents know when to consult the memory manual.
- Seeded memory files from the setup chat, including Kyle's preferences for notebook-style memory, end-of-task updates, aggressive compaction, sanitized work summaries, evidence links, and roles or first names for people memory.

### 2026-07-03 - Project 04 - Your Memory Completed

- Marked AgentOS Project 04 - Your Memory complete.
- Evidence: `projects/04-your-memory/notes.md`.

### 2026-07-03 - Project 05 - Your Connections Completed

- Marked AgentOS Project 05 - Your Connections complete.
- Evidence: `projects/05-your-connections/notes.md`.

### 2026-07-05 - Project 06 - The Job Completed

- Marked AgentOS Project 06 - The Job complete.
- Evidence: `projects/06-the-job/notes.md`.

## Work

- Keep detailed work source material in Jira, GitHub, Confluence, Slack, or other source systems.
- Store only sanitized milestones here when they matter for future agent behavior.

## Home

- Store meaningful personal project milestones when they affect future priorities, risks, or workflow.

### 2026-07-05 - Home Media Server Added To AgentOS

- Added Kyle's Plex server ecosystem to AgentOS as the active Home Media Server project.
- Source: <https://github.com/KyleGowen/plex-server-hardware>.
- AgentOS now stores summary context, remote/mobile Codex workflow, live-server safety boundaries, memory entries, and non-executable Plex skill archives while the Plex repo remains source of truth for detailed operations.

### 2026-07-05 - DDR/ITG Machine Added To AgentOS

- Added Kyle's StepMania, DDR, and ITGMania setup to AgentOS as the active DDR/ITG Machine hobby-log project.
- Sources: <https://github.com/KyleGowen/itgmania-backup> and <https://github.com/KyleGowen/Thraximundar-Backup>.
- AgentOS now stores summary context, fitness-progress framing, digest-coach routing, backup safety boundaries, and catalog-only workflow notes while the tooling and backup repos remain source of truth.
