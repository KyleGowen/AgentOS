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

## Experiential Learning

Every AgentOS agent and executable skill should learn from meaningful successes
and failures without rewriting itself after every run.

- At the end of a meaningful run, check for a reusable learning delta: a
  clarified input, repeated ambiguity, source-of-truth drift, avoidable step,
  reliable shortcut, verification improvement, or failure mode. Routine success
  with no new reusable information requires no write.
- Automatically update only deterministic operational state that the owning
  policy explicitly allows, such as a ledger, cache, checkpoint, or last-seen
  identifier. Keep that state in its existing authoritative location.
- Do not automatically edit agent definitions, `SKILL.md` files, code,
  permissions, approval boundaries, or safety rules after a run. Record a
  compact improvement proposal in the agent's or skill's approved learning
  destination instead.
- Promote a proposal into the owning source only when it is source-grounded,
  generalizable, and supported by the same signal in at least two runs or by a
  retrospective after three meaningful runs. A single high-impact failure may
  be promoted sooner, but only through an explicit reviewed change with
  proportionate verification.
- Change the one authoritative agent, skill, context, policy, or state source
  that owns the behavior; do not duplicate the lesson across launchers or
  unrelated memory files.
- Keep learning records compact and within the agent's context/state allowlist.
  Never store secrets, raw private content, customer details, cookies, API
  keys, or unnecessary personal data.
- Use the monthly AgentOS review to clear unresolved improvement proposals and
  stale rules. The review supplements the per-run loop; it is not a reason to
  rewrite every agent or skill on a schedule.
- Treat this contract as inheritable global governance. External projects with
  scoped AgentOS inheritance should carry or reference it with provenance,
  while preserving project-local precedence and domain-specific learning
  allowlists.

Each specialized agent definition must name its permitted learning destination
and mutation boundary. Each executable skill must include a compact
`Post-Run Learning` section.

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
- When changing an external project's inheritance status, run
  `python3 scripts/sync-playbook-project-surfaces.py` and verify it with
  `python3 scripts/sync-playbook-project-surfaces.py --check`. The generated
  playbook table is a projection of the registry, not a second source of truth.
