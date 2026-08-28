# Monster Hunter Now Saved Builds

Durable build ledger for the Monster Hunter Now Build Optimizer skill.

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
- Context: build Kyle became interested in and refined during prior MH Now optimizer runs.
- Weapon: Mizutsune Gunlance
- Notes: Preserve this entry as a durable pointer to the favored “gold medal” recommendation. Before presenting exact armor, Driftsmelts, or skill totals from this entry, verify against the current MH Now data/source set because the exact detailed loadout was not available in the AgentOS repository at seed time.
- Persistence source: seeded from existing ChatGPT/skill context during AgentOS integration on 2026-08-27.

## Update behavior

- Prefer updating an existing saved build over creating duplicates.
- If a materially better verified variant replaces a saved build, mark the old one `superseded` and link the replacement.
- Do not silently treat stale game data as current; re-verify when patches, new armor, new Driftsmelts, or balance changes could affect the recommendation.
