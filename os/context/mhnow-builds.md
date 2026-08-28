# Monster Hunter Now Build State

This file is a routing pointer, not a second build ledger.

## Canonical persisted-build source

The single durable source of truth for Monster Hunter Now builds is:

`os/memory/mh-now-builds.md`

All ChatGPT, Codex, Palico, agent, and skill retrieval must read that file directly before answering questions about saved, favored, adopted, historical, or previously explored builds.

Do not store build payloads here. Do not infer that a build is missing because GitHub code search does not return it; fetch the canonical file directly.

## Persistence contract

When Kyle clearly adopts, selects, refines, farms for, asks to save, or asks to revisit a build, persist the complete snapshot in `os/memory/mh-now-builds.md`:

- build label
- weapon and exact variant
- style/customization
- target or intended scope
- exact head/chest/arms/waist/legs
- exactly five mapped Driftsmelts when applicable, including stone names/colors
- important resulting skill totals and breakpoints
- concise rotation assumptions
- evidence/research date
- confidence
- freshness triggers
- status/current-vs-superseded history

A pointer such as “Kyle liked this build” is not sufficient persistence.
