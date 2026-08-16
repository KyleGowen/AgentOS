# ThraxOS AgentOS inheritance

Date: 2026-08-16

Status: Architecture milestone; Project 07 remains in progress pending its documented representative-run evidence gate.

## Outcome

ThraxOS now permanently inherits Kyle's global AgentOS identity, communication, privacy, verification, approval, memory, GitHub synchronization, and skill-learning rules through a compact checked-in cache. It deliberately excludes every unrelated AgentOS project's context.

## Evidence

- Repository: <https://github.com/KyleGowen/ThraxOS>.
- Cache: `memory/AGENTOS_INHERITANCE.md` in ThraxOS.
- Operating precedence: root `AGENTS.md` and `.codex/agents/thraxos.toml` in ThraxOS.
- Status tooling: `.agents/skills/thraxos/scripts/Get-AgentOSInheritanceStatus.ps1` in ThraxOS.
- Skill and migration documentation: `.agents/skills/thraxos/SKILL.md`, `docs/skills/thraxos.md`, and `docs/skills/README.md` in ThraxOS.

The cache records committed AgentOS `origin/main` SHA `e6389d563058e43cc871e7ecda3a632d43b8ee48` and category-level source files. A matching SHA avoids rereading AgentOS. A changed SHA restricts inspection to relevant changed sources.

## Boundaries

- ThraxOS is authoritative for every Thraximundar-specific fact, operation, context, memory, safety requirement, skill, and decision.
- AgentOS is authoritative for Kyle's global governance, identity, cross-project rules, and course state.
- ThraxOS-specific instructions win for the machine, and material conflicts are reported.
- Uncommitted AgentOS changes are never inherited.
- AgentOS writes require explicit approval, a configured local checkout, and the allowlist stored in the ThraxOS cache.
- Fetching may update Git metadata only. The workflow never pulls, merges, rebases, switches branches, resets, or changes the AgentOS worktree during refresh.
- This milestone does not satisfy the separate Project 7 representative invocation, verified result, and Kyle reflection requirement.
