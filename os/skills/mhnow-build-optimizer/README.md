# Palico

**Palico** is the user-facing alias for the Monster Hunter Now Build Optimizer skill.

## Alias contract

- Saying `Palico` should route to the Monster Hunter Now Build Optimizer behavior.
- Existing references to `mhnow-build-optimizer`, `Monster Hunter Now Build Optimizer`, or `@mhnowbuildoptimizer` remain valid.
- Keep the canonical repository path as `os/skills/mhnow-build-optimizer/` so existing links and persisted state remain stable.
- Palico owns the hunt-specific build workflow and the durable saved-build ledger in `saved-builds.md`.

## Expected behavior

Given a Monster Hunter Now weapon and target monster, Palico should produce the optimized hunt-specific build: weapon/style choices where applicable, exact head/chest/arms/waist/legs, all five Driftsmelt skills, important resulting skill totals, and a concise hunt strategy. It should optimize for practical DPS against the target using current weaknesses, hitzones, status susceptibility, and weapon mechanics.

When Kyle shows sustained interest in a recommendation, Palico should persist or update that build in `saved-builds.md` so future AgentOS sessions can reuse it without starting research from scratch.
