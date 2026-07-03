# Project 03: Your First Skills

Status: Complete

Completed: 2026-07-03

Course page: <https://aidbagentos.ai/projects>

## Goal

Create reusable skill files for repeated workflows, preserve native skill formats,
and translate selected skills into Codex's repo skill format.

## Inputs

- Course instructions: Build 2-3 reusable skill files for workflows I repeat.
- Existing skills:
  - Claude Code Measurabl skills.
  - Cursor Excelsior skills.
- Tools used:
  - Codex repo skills under `.agents/skills/`
  - Native skill archives under `os/skills/native/`

## Local Artifacts

- `.agents/skills/`
- `os/skills/README.md`
- `os/skills/catalog.md`
- `os/skills/native/`

## Build Notes

### Decisions

- Use `.agents/skills/` for Codex-executable repo skills.
- Use `os/skills/` as the AgentOS catalog and archive layer.
- Preserve imported skills in their native source format before translating them.

### Output

- Migrated `/complete` to `.agents/skills/complete/`.
- Imported and translated Measurabl Claude skills:
  - `/ticket-to-pr`
  - `/resolve-pr-comments`
- Imported and translated Excelsior Cursor skills:
  - `/add-card`
  - `/add-community-deck`
  - `/pdf-to-png`
  - `/ship`
  - `/start`
  - `/start-aws-db-tunnel`

## Evidence

- Files:
  - `.agents/skills/`
  - `os/skills/catalog.md`
  - `os/skills/native/`
  - `os/skills/README.md`

## Reflection

What worked:

- Preserving native skill files first made the Codex translations easier to trust.

What I would improve:

- Forward-test the translated skills inside their target repositories.

What should be added to the playbook:

- Track skills by native format, scope, Codex translation, and maturity.
