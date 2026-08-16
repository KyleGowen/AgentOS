# Project 08: Test & Verify

Status: In progress

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

The course artifact is an executed prompt, a sanitized expected-versus-actual
evaluation, Kyle's under-one-minute checklist result, and a short retrospective.

## Start Artifacts

- `verification-plan.md` — chosen scenarios, pass criteria, checklist, and
  evaluation record.
- `../../PLAYBOOK.md` — Kyle's reusable personal verification checklist.

## Next Gate

Run Scenario 1 from `verification-plan.md` against ThraxOS with a real,
read-only host/backup-health request. Record only sanitized evidence and note
whether each checklist item passed, failed, or was not applicable. Do not mark
the project complete from the plan alone.

## Related Artifacts

- `projects/07-working-agent/notes.md`
- `projects/07-working-agent/thraxos-agentos-inheritance.md`
- `os/context/stepmania-ddr.md`
- `os/context/current-projects.md`
- `PLAYBOOK.md`
