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

## Specialized Agent Inheritance

Every specialized agent defined inside this repository inherits AgentOS
governance when it runs from this repository. It must read this file and its
canonical definition in `os/agents/` before meaningful work.

- Inherit the applicable global rules: Kyle's durable preferences, privacy and
  approval boundaries, verification expectations, and the memory protocol.
- Load only context and durable state relevant to the assigned job. Do not
  treat inheritance as authorization to use unrelated work, home, or agent
  data.
- Give each agent definition an explicit context/state allowlist, boundaries,
  and sources of truth. Its domain policy and implementation skill remain
  canonical; do not copy them into a launcher or a second memory store.
- Keep `.codex/agents/*.toml` profiles thin: they launch the agent and point
  to this file plus the canonical definition. They must not duplicate policy,
  preferences, or operational state.
- Use `os/context/agentos-inheritance-registry.md` only for an agent in an
  external project or repository. AgentOS-native agents do not need a
  separate inheritance cache.
