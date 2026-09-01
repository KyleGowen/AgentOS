# Project History

Compact history of meaningful outcomes and milestones. This is not a full changelog.

### 2026-09-01 - AgentOS-Wide Experiential Learning Contract Added

- Extended the existing skill-local learning loop to every AgentOS agent and
  executable skill through root governance.
- Kept deterministic policy-approved state automatic while making agent,
  skill, code, permission, and safety changes evidence-gated and review-only.
- Audited the executable skills and active agent definitions, then added
  explicit learning destinations and privacy boundaries where they were
  missing.

### 2026-08-17 - Project 10 Started

- Began Project 10, Your Playbook, using the existing `PLAYBOOK.md` as the
  canonical operating-manual artifact rather than creating a duplicate.
- Added a source-grounded requirement review and corrected the manual's stale
  Project 09 status and next-step reference.
- Kyle's concise operating reflection, a source-grounded final review, and a
  manual monthly `os-map` review cadence are recorded.

### 2026-08-17 - Playbook Project-Surface Sync Added

- Added a generated inherited-project-surface section to the Project 10
  playbook, driven only by the AgentOS inheritance registry.
- Added a checked-in sync script and stale-state check so new prompted external
  projects receive a playbook row without duplicating their local procedures.
- Added a standalone browser-ready nested map of the AgentOS foundation, native
  agents and skills, and currently inherited project surfaces.
- Promoted that map into the `os-map` skill so it can be opened and refreshed
  on demand without treating the visual as the source of truth.

### 2026-08-16 - Project 08 Started

- Began Project 08, Test & Verify, using ThraxOS as the verification target.
- Added a verification plan, four-item checklist, scenario set, and sanitized
  evaluation-record template.
- The next gate is an executed representative read-only health snapshot with
  checklist results and Kyle's reflection.

### 2026-08-13 - AgentOS Project Tracker Audit

- Reconciled `PROJECT_TRACKER.md`, `README.md`, project notes, AgentOS artifacts,
  and live Codex automation configuration.
- Confirmed Projects 00–06 complete; recorded Project 07 as in progress, Project
  08 as not started, and Projects 09–11 as in progress.
- Recorded the missing completion evidence instead of inferring completion from
  agent definitions or automation policies alone.

## AgentOS

### 2026-08-16 - Project 07 Re-scoped To ThraxOS

- Kyle selected the working ThraxOS specialist as the Project 07 build instead
  of the AI Office Hours Prep Agent.
- Verified that `KyleGowen/ThraxOS` contains a custom Codex agent, operating
  contract, context, skills, guarded scripts, memory, safety boundaries, and
  real operations evidence.
- Kept Project 07 in progress pending a compact representative invocation,
  verified result, and reflection in the AgentOS completion packet.

### 2026-07-30 - SDGE Energy Alert Skill Created

- Added `.agents/skills/catalog-sdge-energy-alerts/` to process unread SDGE Energy Use Alert emails through the Gmail connector.
- The skill stores parsed utility facts in `os/data/sdge-energy-alerts/records.jsonl`, regenerates `os/reports/sdge-energy-alerts/index.html`, and marks only successfully processed SDGE message IDs read.
- Added `os/automations/sdge-energy-alerts.md` and scheduled Codex automation `sdge-energy-alerts` to run the skill weekly Monday at 7:00 AM Pacific.
- Expanded parser and dashboard coverage for SDGE usage-report meter data: electric usage to date, on/off/super-off-peak kWh, gas therms, and meter endings.

### 2026-07-29 - Project 07 AI Coaching Context Interview

- Interviewed Kyle on what would make the AI Office Hours Prep Agent complete enough for Project 07.
- Updated `os/context/ai-coaching.md` with the sub-five-minute prep-brief target, current-event discussion starter requirement, source authority suggestions, Business Operations Engineer role context, during-session guidance, and sharper coaching safety boundaries.

### 2026-07-19 - Automation Efficiency Review Added

- Added `os/automations/automation-efficiency-review.md` as a daily 6:30 AM Pacific review-only optimization digest.
- Replaced the daily automation-efficiency review with skill-local post-run learning loops and removed the scheduled review policy.
- The retired automation reviewed recent scheduled runs and future automation candidates, then recommended token and efficiency improvements by skill without applying changes until Kyle approved them.

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

### 2026-08-16 - Project 07 - The Build Completed

- Marked AgentOS Project 07 - The Build complete.
- Evidence: `projects/07-working-agent/notes.md`.

### 2026-08-16 - Project 08 - Test & Verify Completed

- Verified selective, durable, policy-level AgentOS inheritance in ThraxOS
  during the Arcade Console rebuild. Global governance and UI preferences were
  inherited, while unrelated Project 08 context remained isolated.
- The cached AgentOS SHA matched local committed `main`; upstream freshness was
  explicitly unverified because a live fetch check was unavailable.
- Evidence: `projects/08-test-and-verify/notes.md` and
  `projects/08-test-and-verify/runs/2026-08-16-thraxos-selective-inheritance.md`.

### 2026-08-17 - Project 09 - The Second Agent Completed

- Marked AgentOS Project 09 - The Second Agent complete with the SDGE Energy
  Agent, a policy-scoped home-utility data steward distinct from ThraxOS.
- Evidence: `projects/09-agent-team/notes.md` and
  `projects/09-agent-team/runs/2026-08-17-sdge-energy-agent.md`.

### 2026-08-17 - Project 10 - Your Playbook Completed

- Marked AgentOS Project 10 - Your Playbook complete.
- Evidence: `projects/10-playbook/notes.md`.

### 2026-08-17 - Project 11 - Automations Completed

- Marked AgentOS Project 11 - Automations complete.
- Evidence: `projects/11-automations/notes.md`.

### 2026-07-01 - Project 00 - Your OS Thought Partner Completed

- Marked AgentOS Project 00 - Your OS Thought Partner complete.
- Evidence: `projects/00-os-thought-partner/notes.md`.

### 2026-07-01 - Project 01 - Your Identity Completed

- Marked AgentOS Project 01 - Your Identity complete.
- Evidence: `projects/01-context/notes.md`.

### 2026-07-02 - Project 02 - Your Context Completed

- Marked AgentOS Project 02 - Your Context complete.
- Evidence: `projects/02-your-context/notes.md`.

### 2026-07-03 - Project 03 - Your First Skills Completed

- Marked AgentOS Project 03 - Your First Skills complete.
- Evidence: `projects/03-your-first-skills/notes.md`.

## Work

- Keep detailed work source material in Jira, GitHub, Confluence, Slack, or other source systems.
- Store only sanitized milestones here when they matter for future agent behavior.

## Home

- Store meaningful personal project milestones when they affect future priorities, risks, or workflow.

### 2026-08-16 - Excelsior Added Permanent AgentOS Inheritance

- Added a compact, provenance-tracked global AgentOS rules cache and read-only
  freshness check to Excelsior.
- Established Excelsior as authority for its product and technical state while
  limiting AgentOS to global governance and summary-level Excelsior context.
- Corrected local routing so `/Users/kyle/cursored` is used after confirming its
  remote, without selecting the older checkout merely because it exists.

### 2026-08-13 - Personal Project Status Audit

- Audited personal-project context against available local source repositories.
- Confirmed Excelsior active development in `/Users/kyle/cursored`; identified
  `/Users/kyle/Projects/excelsior` as an older divergent checkout.
- Confirmed Korlash documentation still describes an unverified pre-boot
  rebuild state.
- Marked DDR/ITG current status as unverified because its source repositories
  were unavailable locally and remote refresh failed.
- Kept Vimanas paused and Planted background based on their documented routing.

### 2026-07-05 - Home Media Server Added To AgentOS

- Added Kyle's Plex server ecosystem to AgentOS as the active Home Media Server project.
- Source: <https://github.com/KyleGowen/plex-server-hardware>.
- AgentOS now stores summary context, remote/mobile Codex workflow, live-server safety boundaries, memory entries, and non-executable Plex skill archives while the Plex repo remains source of truth for detailed operations.

### 2026-07-05 - DDR/ITG Machine Added To AgentOS

- Added Kyle's StepMania, DDR, and ITGMania setup to AgentOS as the active DDR/ITG Machine hobby-log project.
- Sources: <https://github.com/KyleGowen/itgmania-backup> and <https://github.com/KyleGowen/Thraximundar-Backup>.
- AgentOS now stores summary context, fitness-progress framing, digest-coach routing, backup safety boundaries, and catalog-only workflow notes while the tooling and backup repos remain source of truth.
