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

## Open System Questions

- Which memory items should eventually become skills?
- Which repeated memory updates should become automations?
- How often should project history be reviewed for stale or overly detailed entries?
- After several real tasks, should the memory update checklist become a skill or stay as README guidance?
