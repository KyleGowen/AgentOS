# Monster Hunter Now Saved Builds

Durable build ledger for the Monster Hunter Now Build Optimizer skill (Palico).

## Persistence rule

When Kyle shows sustained interest in a build (for example: asks to refine it, compares variants, or explicitly says to save/keep it), persist the build here so future ChatGPT and Codex sessions can reuse it without re-researching from scratch.

Each saved build should capture:

- Weapon and exact variant
- Target monster or general use case
- Armor: head / chest / arms / waist / legs
- All 5 Driftsmelt skills
- Important resulting skill totals
- Style/customization choices where applicable
- Short hunt/rotation notes
- Source/verification note and date
- Status: draft / current favorite / superseded

## Seeded build

### Mizutsune Gunlance — “Gold medal” favored build

- Status: current favorite candidate
- Context: build Kyle became interested in and refined during prior MH Now optimizer runs; currently being reconstructed as an Artillery-focused Blast Dash build.
- Weapon: Mizutsune Gunlance
- Style: Blast Dash
- Current target context: Riftborn/Riftcharged Glavenus
- Head: Bazelgeuse Helm — explicitly persisted by Kyle on 2026-08-27.
- Chest: not yet persisted
- Arms: not yet persisted
- Waist: Bazelgeuse Coil — explicitly persisted by Kyle on 2026-08-27.
- Legs: not yet persisted
- Driftsmelts: not yet persisted
- Notes: Treat Bazelgeuse Helm and Bazelgeuse Coil as locked tracked pieces unless Kyle replaces them. Do not infer the remaining armor, Driftsmelts, or skill totals from earlier provisional recommendations; verify them before persisting.
- Persistence source: seeded from existing ChatGPT/skill context during AgentOS integration on 2026-08-27 and incrementally reconstructed from Kyle's explicit selections.

## Update behavior

- Prefer updating an existing saved build over creating duplicates.
- Explicitly persisted equipment choices are treated as locked for that tracked build until Kyle changes or replaces them.
- If a materially better verified variant replaces a saved build, mark the old one `superseded` and link the replacement.
- Do not silently treat stale game data as current; re-verify when patches, new armor, new Driftsmelts, or balance changes could affect the recommendation.
