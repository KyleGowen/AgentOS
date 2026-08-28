---
name: mhnow-build-optimizer
description: "Optimize Monster Hunter Now builds for a specific weapon and target monster. Use when Kyle names a MHNow weapon and monster, asks for the highest practical DPS build, requests exact armor and all five driftsmelts, compares variants, or wants to persist or recall a build he is interested in."
---

# Monster Hunter Now Build Optimizer

## Overview

Use this skill to produce a current, hunt-specific Monster Hunter Now build rather than a generic weapon build. Optimize for the named weapon, target monster, current game mechanics, obtainable armor and driftsmelts, and Kyle's stated constraints.

The **single durable AgentOS source of truth** for builds Kyle wants to revisit is `os/memory/mh-now-builds.md`. Read that file directly before researching or answering any question about saved, favored, adopted, historical, or previously explored builds. Do not treat GitHub code-search misses, chat history, model memory, `os/context/mhnow-builds.md`, or `os/skills/mhnow-build-optimizer/saved-builds.md` as competing authorities; the latter two are compatibility pointers only.

## Trigger

Invoke when Kyle provides a Monster Hunter Now weapon and target monster, or asks to refine, compare, persist, recall, or revisit an existing MHNow build.

## Required Inputs

- Weapon name and weapon type.
- Target monster.
- Any explicit constraints such as obtainable driftstones only, no event-exclusive or unavailable stones, preferred playstyle, survivability tolerance, or owned gear limitations.
- `os/memory/mh-now-builds.md` for previously persisted recommendations.

If the weapon or monster name is ambiguous, resolve the likely in-game entity from current sources before optimizing.

## Research Rules

1. Treat current MHNow data as time-sensitive. Verify current weapon stats/mechanics, armor skills, driftsmelt availability, target weaknesses, hitzones, status susceptibility, event-exclusive availability, and relevant balance changes from current public sources before finalizing a new or materially changed build.
2. Prefer primary or high-quality current sources when available. Do not rely on stale remembered values when current verification is possible.
3. Distinguish theoretical ceiling from practical hunt DPS. Prefer the highest practical DPS build for the named matchup unless Kyle explicitly asks for a paper-DPS or comfort variant.
4. Honor obtainable-only constraints literally. Do not recommend unavailable, impossible, or mutually incompatible driftsmelts.
5. Consider weapon-specific mechanics such as ammo, shelling, phials, coatings, aerial/ground loops, guard/counter windows, status application, affinity, elemental scaling, and style customization where applicable.
6. Consider the target monster's actual elemental weakness, breakable parts, accessible hitzones, enraged/riftcharged behavior, and status susceptibility rather than optimizing from element alone.

## Workflow

1. Check persisted state first.
   - Fetch `os/memory/mh-now-builds.md` directly.
   - If Kyle asks what was saved historically, return that stored snapshot first. Keep any current-game refresh or correction separate.
   - If an exact weapon + monster/use-case build already exists, use it as the starting point and verify only the freshness triggers that could materially change it.
   - Preserve Kyle's previously selected or favored variant unless new evidence materially changes the recommendation; explain the change when it does.
   - Never conclude that persistence is missing merely because code search did not find a keyword.

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
   - Exactly one driftsmelt recommendation for each armor slot, for five total when applicable.
   - Resulting key skill totals after driftsmelts.
   - Note any substitution that materially changes the resulting totals or rotation.

7. Explain how to play it.
   - Give a concise hunt rotation or tactical plan tied to the weapon and monster.
   - Call out target parts, openings, positioning, counters/guards, burst windows, and when the build's key skills are expected to be active.

8. Persist builds Kyle becomes interested in.
   - When Kyle selects a recommendation, asks to hone/refine it, asks for exact pieces or smelts, says he is farming/building/committing resources to it, explicitly asks to save it, or asks to revisit it later, update `os/memory/mh-now-builds.md`.
   - Persist the **complete artifact**, not a pointer to interest: build label; weapon/variant; style/customization; target or intended scope; exact head/chest/arms/waist/legs; exactly five mapped Driftsmelts and stone names/colors when applicable; key resulting skill totals and breakpoints; concise rotation assumptions; why it was selected; evidence/research date; confidence; freshness triggers; and current/superseded status.
   - A note such as “Kyle liked this build” is not valid persistence.
   - Update an existing record rather than creating a duplicate when it is the same build concept.
   - Do not persist every generated candidate automatically.

9. Verify persistence after any write.
   - Re-fetch `os/memory/mh-now-builds.md` after the update.
   - Confirm the intended build record contains the complete payload and can be located by its weapon/build label without relying on code search.
   - If the write cannot be verified, report persistence as failed rather than claiming success.

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

When recalling a persisted build, clearly label it **Saved build**, include the saved evidence date, and distinguish the stored historical snapshot from any fresh revalidation.

## Verification

Before finalizing:

- Confirm all five armor pieces exist and provide the claimed native skills.
- Confirm all five driftsmelts are obtainable under the stated constraints.
- Recalculate key skill totals from armor plus driftsmelts.
- Confirm the target weakness/status assumptions are current.
- Confirm the recommended skills affect the weapon's important damage sources as expected.
- If a persisted build changed, identify the data or balance change that caused the update.
- If persistence was requested or triggered, re-fetch `os/memory/mh-now-builds.md` and verify the complete record exists before saying it was saved.

## Post-Run Learning

After a meaningful run:

- Reuse verified current facts and persisted selected builds to avoid repeating research.
- Capture recurring source-quality issues, ambiguous skill interactions, unavailable driftsmelt assumptions, or calculation mistakes as proposed improvements.
- Persist only builds Kyle expresses clear interest in, selects, refines, farms for, or asks to save.
- Never create a second saved-build ledger outside `os/memory/mh-now-builds.md`.
- Do not silently rewrite this `SKILL.md` after each run. Promote stable, source-grounded improvements through normal AgentOS review.
