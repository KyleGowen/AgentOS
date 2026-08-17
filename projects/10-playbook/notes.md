# Project 10: Your Playbook

Status: In progress

Started: 2026-08-17

Last audited: 2026-08-17

Course page: <https://aidbagentos.ai/projects>

## Goal

Create and maintain one honest, useful operating manual for the AgentOS: what
exists, how its layers and agents relate, what works, what remains incomplete,
and what should be built next.

## Local Artifacts

- `PLAYBOOK.md`
- `playbook-review.md`
- `agentos-system-map.html` — standalone nested AgentOS map for Chrome or
  another modern browser.
- `.agents/skills/os-map/` — on-demand map refresh and opening workflow.

## Source Template

The course app's Project 10 playbook template is represented locally in
`PLAYBOOK.md`. The initial local review maps each requested playbook section to
current AgentOS evidence and distinguishes verified state from open inputs.

## Current State

`PLAYBOOK.md` is a substantial operating-manual draft. The 2026-08-17 baseline
corrected its stale Project 09 status and creates a concrete review list for
the remaining narrative sections. Its inherited-project-surface map is
generated from `os/context/agentos-inheritance-registry.md` by
`scripts/sync-playbook-project-surfaces.py`.

## Completion Gate

- Review the playbook against its current source files and keep unsupported
  claims marked as open or unverified.
- [x] Add Kyle's concise reflection on what changed, what works, and what he
  would tell another person building an AgentOS.
- Confirm the current next steps, automation status, and a lightweight monthly
  review cadence are accurate, then record the completed-project evidence in
  this folder and the tracker.
