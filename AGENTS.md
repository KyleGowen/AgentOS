# AgentOS Repo Guidance

This repository is Kyle's AgentOS coursework and durable operating system for agent-assisted work.

## Memory

- When a task involves project continuity, decisions, patterns, lessons, or AgentOS maintenance, read `os/memory/README.md` before updating memory files.
- Treat `os/memory/` as the intentional memory layer. Codex generated memories are helpful recall, but they are not the source of truth for required rules or durable decisions.
- Keep work and home project context separated. Do not let personal project context influence work reasoning.
- Never store secrets, private customer details, raw Slack excerpts, or unnecessary personal data in memory files.

## Context

- Use `os/context/identity.md` for Kyle's durable preferences and working style.
- Use `os/context/design-system.md` for Kyle's global UI, frontend, and
  component-design preference. Subprojects that inherit AgentOS global rules
  should carry this preference with source provenance.
- Use `os/context/current-projects.md` for project context, but warn Kyle if it is more than 30 days old.
- Use `PLAYBOOK.md` for the current operating manual and project status.
