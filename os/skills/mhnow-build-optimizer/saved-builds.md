# Monster Hunter Now Saved Builds

This file is retained for compatibility with older Palico/skill references. It is not an independent ledger.

## Canonical persisted-build source

Read and write all durable saved Monster Hunter Now builds in:

`os/memory/mh-now-builds.md`

Do not duplicate build payloads in this file. Do not treat this file, chat history, model memory, or GitHub code-search results as authoritative when recalling a saved build.

## Retrieval rule

When Kyle asks about a saved, favored, adopted, historical, or previously explored build:

1. Fetch `os/memory/mh-now-builds.md` directly.
2. Return the saved snapshot first when he asks what was persisted.
3. Run current-data freshness checks separately when needed; do not overwrite historical facts merely because current optimization may differ.
4. If a requested build is genuinely absent from the canonical memory file, say that it is not durably persisted instead of reconstructing it from a vague interest pointer.

## Persistence rule

When Kyle clearly selects, refines, farms for, commits resources to, asks to save, or asks to revisit a build, write the complete artifact to `os/memory/mh-now-builds.md`, including weapon/style, intended scope, five armor pieces, five mapped Driftsmelts and stones when applicable, key totals/breakpoints, rotation assumptions, evidence date, confidence, freshness triggers, and supersession status.

Partial interest markers are not valid persisted builds.
