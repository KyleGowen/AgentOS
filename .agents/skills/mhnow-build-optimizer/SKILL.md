---
name: mhnow-build-optimizer
description: "Optimize Monster Hunter Now builds for a specific weapon and target monster. Use when Kyle names a MHNow weapon and monster, asks for the highest practical DPS build, requests exact armor and all five driftsmelts, compares variants, or wants to persist a build he is interested in."
---

# Monster Hunter Now Build Optimizer

## Overview

Use this skill to produce a current, hunt-specific Monster Hunter Now build rather than a generic weapon build. Optimize for the named weapon, target monster, current game mechanics, obtainable armor and driftsmelts, and Kyle's stated constraints.

The durable AgentOS state for builds Kyle wants to revisit is `os/context/mhnow-builds.md`. Read it before researching so previously selected builds can be reused or updated instead of rebuilt from scratch.

## Trigger

Invoke when Kyle provides a Monster Hunter Now weapon and target monster, or asks to refine, compare, persist, or revisit an existing MHNow build.

## Required Inputs

- Weapon name and weapon type.
- Target monster.
- Any explicit constraints such as obtainable driftstones only, no event-exclusive or unavailable stones, preferred playstyle, survivability tolerance, or owned gear limitations.
- `os/context/mhnow-builds.md` for previously persisted recommendations.

If the weapon or monster name is ambiguous, resolve the likely in-game entity from current sources before optimizing.

## Research Rules

1. Treat current MHNow data as time-sensitive. Verify current weapon stats/mechanics, armor skills, driftsmelt availability, target weaknesses, hitzones, status susceptibility, event-exclusive availability, and relevant balance changes from current public sources before finalizing a build.
2. Prefer primary or high-quality current sources when available. Do not rely on stale remembered values when current verification is possible.
3. Distinguish theoretical ceiling from practical hunt DPS. Prefer the highest practical DPS build for the named matchup unless Kyle explicitly asks for a paper-DPS or comfort variant.
4. Honor obtainable-only constraints literally. Do not recommend unavailable, impossible, or mutually incompatible driftsmelts.
5. Consider weapon-specific mechanics such as ammo, shelling, phials, coatings, aerial/ground loops, guard/counter windows, status application, affinity, elemental scaling, and style customization where applicable.
6. Consider the target monster's actual elemental weakness, breakable parts, accessible hitzones, enraged/riftcharged behavior, and status susceptibility rather than optimizing from element alone.

## Workflow

1. Check persisted state.
   - Read `os/context/mhnow-builds.md`.
   - If an exact weapon + monster build already exists, use it as the starting point and verify whether current game data has changed before recomputing everything.
   - Preserve Kyle's previously selected or favored variant unless new evidence materially changes the recommendation; explain the change when it does.

2. Establish current context.
   - Identify the target monster's current weaknesses and important hunt modifiers.
   - When current events materially affect the recommendation, include a compact current-context section listing highlighted monsters and their weaknesses.
   - Prefer an at-a-glance table. Use familiar elemental/status symbols or emoji only when they are unambiguous; always include the weakness name in text so the table remains readable without icons.

3. Evaluate the weapon.
   - Verify the named weapon's damage type, element/status, weapon-specific mechanics, and style customization options when applicable.
   - Determine which damage skills actually scale the weapon's important attacks.

4. Generate candidate builds.
   - Evaluate relevant head, chest, arms, waist, and legs combinations.
   - Account for native armor skills plus five driftsmelt slots.
   - Reject combinations that require unavailable skills, impossible slot assumptions, or driftsmelts excluded by Kyle's constraints.
   - Compare candidates on practical DPS, uptime, matchup fit, and execution burden.

5. Rank recommendations.
   - Lead with one clear best recommendation.
   - When useful, add compact alternate variants such as maximum DPS, safer/comfort, easier-to-build, or part-break focused.
   - If using medal-style ranking, Gold is the default recommendation, Silver is the strongest meaningful alternative, and Bronze is a situational or lower-cost option.

6. Specify the exact loadout.
   - Weapon and style customization where applicable.
   - Exact head, chest, arms, waist, and legs.
   - Exactly one driftsmelt recommendation for each armor slot, for five total.
   - Resulting key skill totals after driftsmelts.
   - Note any substitution that materially changes the resulting totals or rotation.

7. Explain how to play it.
   - Give a concise hunt rotation or tactical plan tied to the weapon and monster.
   - Call out target parts, openings, positioning, counters/guards, burst windows, and when the build's key skills are expected to be active.

8. Persist builds Kyle becomes interested in.
   - When Kyle explicitly says he likes, wants to explore, wants to save, or wants to revisit a recommendation, update `os/context/mhnow-builds.md` with a compact build record.
   - Store the weapon, target or intended use, armor, five driftsmelts, key skill totals, why it was selected, date verified, and source notes sufficient to know when it may need refresh.
   - Do not persist every generated candidate automatically.

## Output Shape

Lead with the recommendation and keep the core build readable on a phone.

Use a compact table with columns equivalent to:

| Slot | Equipment | Driftsmelt | Important skills |
|---|---|---|---|
| Weapon | ... | n/a | ... |
| Head | ... | ... | ... |
| Chest | ... | ... | ... |
| Arms | ... | ... | ... |
| Waist | ... | ... | ... |
| Legs | ... | ... | ... |

Then include:

- Key skill totals.
- Why this wins for the named matchup.
- Concise play rotation/strategy.
- Any material availability or verification caveat.

For event context, prefer a small weakness table before the build rather than a long prose section.

## Verification

Before finalizing:

- Confirm all five armor pieces exist and provide the claimed native skills.
- Confirm all five driftsmelts are obtainable under the stated constraints.
- Recalculate key skill totals from armor plus driftsmelts.
- Confirm the target weakness/status assumptions are current.
- Confirm the recommended skills affect the weapon's important damage sources as expected.
- If a persisted build changed, identify the data or balance change that caused the update.

## Post-Run Learning

After a meaningful run:

- Reuse verified current facts and persisted selected builds to avoid repeating research.
- Capture recurring source-quality issues, ambiguous skill interactions, unavailable driftsmelt assumptions, or calculation mistakes as proposed improvements.
- Persist only builds Kyle expresses interest in or asks to save.
- Do not silently rewrite this `SKILL.md` after each run. Promote stable, source-grounded improvements through normal AgentOS review.
