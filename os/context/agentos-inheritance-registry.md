# AgentOS Inheritance Registry

Tracks which external projects have received the permanent AgentOS inheritance
prompt and whether implementation has been verified. This registry prevents a
prompt handoff from being mistaken for active inheritance.

Last updated: 2026-08-17

## Status Definitions

- `Not prompted`: No inheritance prompt has been delivered.
- `Prompt delivered`: Kyle has given the permanent inheritance prompt to the
  project, but AgentOS has not verified the implementation.
- `Implementation verified`: The project contains a durable inheritance
  mechanism with source provenance and scoped AgentOS boundaries.

## Registry

| Project | Repository | Prompt status | Implementation status | Evidence / next check |
|---|---|---|---|---|
| ThraxOS | <https://github.com/KyleGowen/ThraxOS> | Prompt delivered | Verified 2026-08-16 | `projects/08-test-and-verify/runs/2026-08-16-thraxos-selective-inheritance.md`; the local cache matched committed AgentOS `main`, while upstream freshness was explicitly unverified. |
| Excelsior | <https://github.com/KyleGowen/excelsior> | Prompt delivered | Verified 2026-08-16 | Excelsior commit `33c1afe5`; AgentOS commit `b85ae39`; `os/context/excelsior.md`. |
| GRESB Reporting Season | Work source systems; no standalone repository recorded | Not prompted | Not implemented | Identify the authoritative project surface and applicable work-policy boundary before generating an inheritance prompt. |
| Data Locking | Work source systems; no standalone repository recorded | Not prompted | Not implemented | Identify the authoritative repository or project surface before generating an inheritance prompt. |
| AI Coaching for Non-Engineers | Claude Cowork workspace and Measurabl source systems | Not prompted | Not implemented | Decide whether inheritance belongs in the coaching workspace, a dedicated repository, or its AgentOS-native agents. |
| Legacy Core Maintenance and Incidents | Work repositories and source systems; details intentionally not recorded here | Not prompted | Not implemented | Select a specific repository or durable project surface before applying inheritance. |
| Mentoring Juniors and Contractors | No standalone project surface recorded | Not prompted | Not implemented | Determine whether this should inherit through a dedicated workspace or remain AgentOS-only context. |
| Home Media Server | <https://github.com/KyleGowen/plex-server-hardware> | Not prompted | Not implemented | Generate and deliver a project-specific inheritance prompt before substantive project work. |
| Vimanas | Repository or durable project surface not recorded | Not prompted | Not implemented | Locate or create the authoritative project surface before delivering inheritance. |
| Planted | Repository or durable project surface not recorded | Not prompted | Not implemented | Locate or create the authoritative project surface before delivering inheritance. |

This table is the complete known-project inventory derived from
`os/context/current-projects.md`. Any newly discovered project should be added
explicitly rather than relying on an implicit unlisted default.

## Reminder Rule

When Kyle references or begins substantive work on a project that is not marked
`Prompt delivered` or `Implementation verified`, remind him that the project
does not yet inherit AgentOS and suggest applying the permanent inheritance
prompt. Do not interrupt trivial mentions, comparisons, or unrelated factual
questions with the reminder.

When a prompt is delivered, update this registry. Mark implementation verified
only after inspecting durable evidence in the target project; record its commit
or another stable evidence pointer.

## Playbook Projection

`PLAYBOOK.md` contains a generated **Inherited Project Surfaces** table. The
registry is its only data source: when a project's prompt status changes from
`Not prompted` to `Prompt delivered`, run the sync in the same change so the
playbook gains its row without duplicating project-local procedures.

```sh
python3 scripts/sync-playbook-project-surfaces.py
python3 scripts/sync-playbook-project-surfaces.py --check
```

The first command updates only the marked generated section in `PLAYBOOK.md`.
The check mode exits nonzero if that section is stale. Do not edit the generated
table directly; update this registry instead.

When a project is added to `os/context/current-projects.md` or otherwise becomes
durable AgentOS project context, add it to this registry in the same change with
an initial status of `Not prompted`. Remove or archive a registry row only when
the owning project context is also removed or explicitly retired.
