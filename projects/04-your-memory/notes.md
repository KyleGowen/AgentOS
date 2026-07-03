# Project 04: Your Memory

Status: Complete

Completed: 2026-07-03

Course page: <https://aidbagentos.ai/projects>

## Goal

Create a memory setup that separates working memory from persistent memory, adapts Codex built-in memory, and gives agents clear instructions for maintaining it.

## Inputs

- Course instructions: Make the tool remember what happened yesterday and last month; understand what Codex remembers automatically; separate working memory from persistent memory; document when and how memory should be updated.
- Existing context:
  - `os/agents/os-thought-partner.md`
  - `os/context/identity.md`
  - `os/context/current-projects.md`
  - `os/memory/README.md`
- Tools used:
  - Codex built-in memories.
  - AgentOS repo memory files under `os/memory/`.

## Build Notes

### Decisions

- Enable Codex memories for ambient recall.
- Use `os/memory/` as the intentional, reviewable memory layer.
- Use a lightweight notebook style rather than a large knowledge base.
- Update memory at the end of meaningful tasks.
- Compact working memory aggressively.
- Separate work, home, and AgentOS memory.
- Store sanitized work summaries, not private work source material.
- Use roles, first names, or private aliases for people memory.

### Output

- Added detailed memory operating rules to `os/memory/README.md`.
- Created working and persistent memory files.
- Added a lightweight root `AGENTS.md` so future agents know when to consult memory rules.
- Aligned this work to the canonical `projects/04-your-memory/` project folder.

## Evidence

- Files:
  - `AGENTS.md`
  - `os/memory/README.md`
  - `os/memory/working-memory.md`
  - `os/memory/decisions.md`
  - `os/memory/patterns.md`
  - `os/memory/project-history.md`
  - `os/memory/people-and-collaboration.md`
  - `os/memory/lessons-learned.md`
  - `os/memory/work-memory.md`
  - `os/memory/home-memory.md`
  - `os/memory/agentos-memory.md`

## Reflection

What worked:

- Separating Codex generated memories from intentional AgentOS memory makes the system easier to trust.
- Interviewing memory preferences first kept the structure lightweight and practical.

What I would improve:

- Test the update habit across a few real tasks before deciding whether any memory updates should become automations.

What should be added to the playbook:

- Memory is now a draft operating layer, with the detailed process in `os/memory/README.md`.
