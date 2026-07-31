# AgentOS Memory

Memory about this AgentOS system, the course, and how the pieces should fit together.

## Current System Shape

- Codex is the home base for AgentOS.
- `os/context/` stores durable background context.
- `.agents/skills/` stores Codex-executable repo skills.
- `os/skills/` stores the AgentOS skill catalog and native skill archives.
- `os/memory/` stores intentional memory that should survive sessions.
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

- Project 04, Your Memory, is focused on separating working memory from persistent memory and documenting how agents should maintain both.
- The memory framework should adapt Codex built-in memory rather than pretending Codex lacks memory.
- The canonical Project 04 folder is `projects/04-your-memory/`.
- The old memory scaffold at `projects/03-memory/` was removed to avoid drift.
- `AGENTS.md` exists at the repo root to point future agents toward memory and context rules.
- Project 06, The Job, created the AI Office Hours Prep Agent as a single-responsibility pre-session prep agent for weekly AI office hours.
- The AI Office Hours Follow-Up Agent was added as a separate single-responsibility post-session agent instead of expanding the prep agent.
- The PR Review Prep Agent was added as a separate read-only engineering review agent with minimal local state for merged PR digest suppression.
- Project 07 is using the AI Office Hours Prep Agent as the working-agent assignment. `os/context/ai-coaching.md` now defines the Project 7 readiness target: a sub-five-minute agenda brief from meeting transcription notes, prior-session context, colleague open projects, and one verified current-event discussion starter.

## Open System Questions

- Which memory items should eventually become skills?
- Which repeated memory updates should become automations?
- How often should project history be reviewed for stale or overly detailed entries?
- After several real tasks, should the memory update checklist become a skill or stay as README guidance?
