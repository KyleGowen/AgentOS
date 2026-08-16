# AgentOS Memory

Memory about this AgentOS system, the course, and how the pieces should fit together.

## Current System Shape

- Codex is the home base for AgentOS.
- `os/context/` stores durable background context.
- `.agents/skills/` stores Codex-executable repo skills.
- `os/skills/` stores the AgentOS skill catalog and native skill archives.
- `os/memory/` stores intentional memory that should survive sessions.
- Cross-device memory is the committed `main` branch of
  `KyleGowen/AgentOS`: Codex and ChatGPT must read the repository files for
  durable context, while chat history and built-in model memory remain
  surface-specific.
- New durable AgentOS knowledge must be recorded in the appropriate
  `os/memory/` or `os/context/` file and pushed to GitHub before it is treated
  as shared across devices.
- `os/context/agentos-inheritance-registry.md` tracks which external projects
  have received the permanent inheritance prompt and which implementations
  have been verified. ThraxOS and Excelsior have received the prompt; only
  Excelsior is currently verified.
- `os/agents/ai-office-hours-prep-agent.md` is the first real job agent.
- `os/agents/ai-office-hours-follow-up-agent.md` is the paired post-session agent for AI office hours.
- `os/agents/pr-review-prep-agent.md` is the review-prep agent for tagged Measurabl PRs.
- `.agents/skills/accept-sender-appointments/` stores the Gmail plus Google Calendar workflow for accepting appointment invitations from a named sender and marking the related mail read.
- `.agents/skills/catalog-sdge-energy-alerts/` stores the Gmail workflow for turning SDGE Energy Use Alert emails into structured utility records and a local dashboard.
- `os/automations/auto-accept-appointments.md` stores the first harness-neutral automation spec; Codex scheduling should read this file instead of hardcoding the sender list.
- `os/automations/sdge-energy-alerts.md` stores the weekly SDGE Energy Alerts automation spec; Codex automation id `sdge-energy-alerts` runs Monday at 7:00 AM Pacific.
- AgentOS no longer uses a daily automation-efficiency review. Skills should capture efficiency lessons through post-run learning loops and promote stable improvements into their own instructions only after review.
- `PLAYBOOK.md` is the operating manual.

## Course Progress Notes

- On 2026-08-13, the project tracker was audited against the repository and
  live Codex automation configuration. That audit established the evidence
  gaps that remain recorded in `PROJECT_TRACKER.md`.
- Project 04, Your Memory, is focused on separating working memory from persistent memory and documenting how agents should maintain both.
- The memory framework should adapt Codex built-in memory rather than pretending Codex lacks memory.
- The canonical Project 04 folder is `projects/04-your-memory/`.
- The old memory scaffold at `projects/03-memory/` was removed to avoid drift.
- `AGENTS.md` exists at the repo root to point future agents toward memory and context rules.
- Project 06, The Job, created the AI Office Hours Prep Agent as a single-responsibility pre-session prep agent for weekly AI office hours.
- The AI Office Hours Follow-Up Agent was added as a separate single-responsibility post-session agent instead of expanding the prep agent.
- The PR Review Prep Agent was added as a separate read-only engineering review agent with minimal local state for merged PR digest suppression.
- On 2026-08-16, Kyle selected the ThraxOS specialist as the Project 07 working-agent assignment. `KyleGowen/ThraxOS` contains the custom Codex agent, operating contract, context, skills, guarded scripts, memory, and real operations evidence. Project 07 is complete; Project 08 owns the compact representative run, verified result, checklist evaluation, and reflection.
- On 2026-08-16, Kyle began Project 08. Its ThraxOS verification plan,
  under-one-minute checklist, scenario set, and sanitized run-record template
  are in `projects/08-test-and-verify/`; the first executed representative run
  is the next gate.

## Open System Questions

- Which memory items should eventually become skills?
- Which repeated memory updates should become automations?
- How often should project history be reviewed for stale or overly detailed entries?
- After several real tasks, should the memory update checklist become a skill or stay as README guidance?
