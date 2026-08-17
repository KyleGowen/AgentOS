# Project 10 Playbook Review

Status: Complete

Reviewed: 2026-08-17

Source: Project 10 course prompt and `PLAYBOOK.md`.

## Purpose

Project 10 asks for one operating manual that explains the AgentOS as it runs
today: its layers, agents and their relationships, working practices, gaps,
and next build priorities. This review keeps that manual grounded in local,
reviewable sources instead of treating a polished narrative as proof.

## Requirement Map

| Playbook need | Current location | Baseline result |
|---|---|---|
| Identity | `PLAYBOOK.md` → My OS Foundation; `os/context/identity.md` | Documented |
| Context | `PLAYBOOK.md` → My OS Foundation; `os/context/` | Documented |
| Skills | `PLAYBOOK.md` → My OS Foundation; `.agents/skills/` | Documented |
| Memory | `PLAYBOOK.md` → My OS Foundation; `os/memory/` | Documented |
| Connections | `PLAYBOOK.md` → My OS Foundation | Documented with active, desired, and deferred states |
| Verification | `PLAYBOOK.md` → Verification; `projects/08-test-and-verify/` | Documented with a reusable checklist and completed Project 08 evidence |
| Agents and relationships | `PLAYBOOK.md` → My Agents | Documented for six agents, including the separate ThraxOS source of truth |
| Automations | `PLAYBOOK.md` → Automations; `os/automations/` | Documented; Project 11 remains the completion owner |
| What works, gaps, and next steps | `PLAYBOOK.md` → What's Working Best and Gaps & Next Steps | Gaps and next steps are present; Kyle's ThraxOS working assessment is recorded |
| Personal reflection | `PLAYBOOK.md` → Reflection | Kyle's reflection is recorded |

## Baseline Corrections

- The playbook now records Projects 00–10 as complete and Project 11 as in
  progress, matching `PROJECT_TRACKER.md`.
- The stale Project 09 evaluation task was removed from the current next steps.
- The inheritance registry now records the completed ThraxOS verification with
  its local-cache/upstream-freshness limitation, matching the Project 08 run
  record.
- The tracker no longer presents the already-completed Project 08 run as a
  Project 07 next gate or says that Project 11 notes are missing.
- The playbook's inherited-project-surface map is generated from the
  inheritance registry. New prompted external projects gain a row when the
  checked-in sync script runs; check mode exposes drift before review.
- `agentos-system-map.html` is a standalone nested visual index of the current
  foundation, native agents and skills, and inherited project surfaces.

## Final Review

- Kyle reports that ThraxOS's automated tasks are working well and make
  managing his ITG machine easier than doing it manually.
- The map now shows known recurring-task status at the AgentOS and inherited
  project layers. ThraxOS task names and schedules remain explicitly
  unverified because no local ThraxOS source is available in this repository.
- Kyle's reflection covers the pre-AgentOS repetition, the benefit of shared
  preferences and skills, the surprise of self-management, and the advice to
  separate high-level projects from small tasks.
- A manual monthly `os-map` review is the maintenance cadence. Proposed skill
  removal or task changes must be confirmed against their owning source.
