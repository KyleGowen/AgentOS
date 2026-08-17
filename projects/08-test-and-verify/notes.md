# Project 08: Test & Verify

Status: Complete

Completed: 2026-08-16

Started: 2026-08-16

Last audited: 2026-08-16

## Goal

Verify the first working agent before trusting it and establish a repeatable,
low-friction evaluation habit.

## Selected Agent

ThraxOS is the Project 07 working agent and the Project 08 verification target.
It is the Codex specialist for Thraximundar, Kyle's Windows ITGMania machine,
with its detailed operational source of truth in
<https://github.com/KyleGowen/ThraxOS>.

## Verification Objective

Establish that ThraxOS can complete a representative, read-only operational
task while being trustworthy in the ways Kyle cares about:

- its conclusion matches the requested scope and constraints;
- every operational claim is traceable to current, identified evidence;
- unavailable or stale live state is reported as unverified rather than guessed;
- it protects secrets and asks before any live-machine, backup, schedule, save,
  configuration, or repository mutation; and
- its answer remains compact and gives an actionable next step.

The course artifact is an executed downstream implementation, a sanitized
expected-versus-actual evaluation, the under-one-minute checklist result, and a
short retrospective.

## Start Artifacts

- `verification-plan.md` — chosen scenarios, pass criteria, checklist, and
  evaluation record.
- `../../PLAYBOOK.md` — Kyle's reusable personal verification checklist.

## Completion Evidence

The ThraxOS Arcade Console rebuild exercised a durable, selective AgentOS
inheritance implementation in a live downstream project. ThraxOS inherited the
compact global governance and UI preferences, including the shadcn/ui default
and the requirement to preserve its accessible interaction language in a
zero-build host. It did not import unrelated AgentOS project context.

Project 08 material was locally available in AgentOS, including both
`projects/08-automations/` and `projects/08-test-and-verify/`, but no Project 08
reference appeared in the ThraxOS cache. This is the intended boundary:
ThraxOS inherits only the commit-pinned compact global cache.

The verification helper confirmed that the configured AgentOS checkout exists
and that the cached AgentOS SHA matches local committed `main` at
`bd0e3bf474cacece4a65a66f866053b84bcdce26`. A live `git fetch` freshness check
was unavailable, so upstream freshness remains explicitly unverified.

The sanitized evaluation and reflection are recorded in
`runs/2026-08-16-thraxos-selective-inheritance.md`.

## Related Artifacts

- `projects/07-working-agent/notes.md`
- `projects/07-working-agent/thraxos-agentos-inheritance.md`
- `os/context/stepmania-ddr.md`
- `os/context/current-projects.md`
- `PLAYBOOK.md`
