# AgentOS Memory

Memory about this AgentOS system, the course, and how the pieces should fit together.

## Current System Shape

- Codex is the home base for AgentOS.
- `os/context/` stores durable background context.
- `.agents/skills/` stores Codex-executable repo skills.
- `os/skills/` stores the AgentOS skill catalog and native skill archives.
- `os/memory/` stores intentional memory that should survive sessions.
- `PLAYBOOK.md` is the operating manual.

## Course Progress Notes

- Project 04, Your Memory, is focused on separating working memory from persistent memory and documenting how agents should maintain both.
- The memory framework should adapt Codex built-in memory rather than pretending Codex lacks memory.
- The canonical Project 04 folder is `projects/04-your-memory/`.
- The old memory scaffold at `projects/03-memory/` was removed to avoid drift.
- `AGENTS.md` exists at the repo root to point future agents toward memory and context rules.

## Open System Questions

- Which memory items should eventually become skills?
- Which repeated memory updates should become automations?
- How often should project history be reviewed for stale or overly detailed entries?
- After several real tasks, should the memory update checklist become a skill or stay as README guidance?
