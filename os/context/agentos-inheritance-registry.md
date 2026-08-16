# AgentOS Inheritance Registry

Tracks which external projects have received the permanent AgentOS inheritance
prompt and whether implementation has been verified. This registry prevents a
prompt handoff from being mistaken for active inheritance.

Last updated: 2026-08-16

## Status Definitions

- `Not prompted`: No inheritance prompt has been delivered.
- `Prompt delivered`: Kyle has given the permanent inheritance prompt to the
  project, but AgentOS has not verified the implementation.
- `Implementation verified`: The project contains a durable inheritance
  mechanism with source provenance and scoped AgentOS boundaries.

## Registry

| Project | Repository | Prompt status | Implementation status | Evidence / next check |
|---|---|---|---|---|
| ThraxOS | <https://github.com/KyleGowen/ThraxOS> | Prompt delivered | Not verified | Inspect the ThraxOS inheritance contract, cache or manifest, status check, and governing instructions after implementation. |
| Excelsior | <https://github.com/KyleGowen/excelsior> | Prompt delivered | Verified 2026-08-16 | Excelsior commit `33c1afe5`; AgentOS commit `b85ae39`; `os/context/excelsior.md`. |

Any tracked project not listed above should be treated as `Not prompted`.

## Reminder Rule

When Kyle references or begins substantive work on a project that is not marked
`Prompt delivered` or `Implementation verified`, remind him that the project
does not yet inherit AgentOS and suggest applying the permanent inheritance
prompt. Do not interrupt trivial mentions, comparisons, or unrelated factual
questions with the reminder.

When a prompt is delivered, update this registry. Mark implementation verified
only after inspecting durable evidence in the target project; record its commit
or another stable evidence pointer.
