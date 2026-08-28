# Monster Hunter Now Build Memory

This file stores MH Now builds the user has explicitly adopted, continued exploring, or asked to preserve so future sessions can resume from a known recommendation without rebuilding from scratch.

## Rules

- Persist only builds with a clear user-interest signal: the user selects a recommendation, asks to hone it, asks which pieces/smelts to use, says they are building it, or explicitly asks to save it.
- Do not persist every candidate build shown in a comparison.
- Store the recommendation as a dated snapshot, not timeless truth.
- Before reusing a saved build, check whether material game facts may have changed: armor/skills, Driftsmelt pools, weapon/style mechanics, balance, caps, or event-target context.
- Reuse the saved structure when still valid; refresh only the stale parts rather than recomputing everything from zero.
- If the user asks for the exact old recommendation, show the saved snapshot and separately note any known current changes.
- When a persisted build is superseded, preserve a compact history line and mark the newest adopted version as current.

## Persisted Builds

### Mizutsune Gunlance — Blast Dash — Gold recommendation

- **Status:** Current adopted/explored recommendation
- **Persisted:** 2026-08-27
- **Evidence date:** 2026-08-27
- **Scope:** Gold practical-DPS Blast Dash build for Mizutsune Gunlance; general shelling/Water hybrid, with strong relevance to water-weak event targets.
- **Weapon:** Mizutsune Gunlance (`Mizumori` line), Blast Dash style
- **Core rotation:** Blast Dash → Aerial Smash → Burst Fire; use Ground Splitter to maintain its shelling buff when practical.
- **Armor snapshot:**
  - Head: Bazelgeuse Helm
  - Chest: Basarios Mail
  - Arms: Ceanataur Vambraces
  - Waist: Bazelgeuse Coil
  - Legs: Ceanataur Greaves
- **Driftsmelt snapshot:**
  - Bazelgeuse Helm: Water Attack — Azure Driftstone
  - Basarios Mail: Water Attack — Azure Driftstone
  - Ceanataur Vambraces: Water Attack — Azure Driftstone
  - Bazelgeuse Coil: Water Attack — Azure Driftstone
  - Ceanataur Greaves: Weakness Exploit — Cyan Driftstone
- **Key breakpoint intent:** Artillery 5; Water Attack 5; Advanced Water Attack activation; preserve Lock On; use the fifth smelt on a non-wasted multiplier rather than excess Water Attack.
- **Confidence:** Reasoned recommendation built from verified mechanics and current live data; exact mathematical DPS supremacy was not independently calculator-proven at persistence time.
- **Freshness trigger:** Revalidate if any of the following change: Gunlance Blast Dash behavior, Artillery breakpoints, Mizutsune weapon stats/style customization, Ceanataur/Bazelgeuse/Basarios skills, Advanced Water mechanics, Driftsmelt pools/colors, or the target/event context.
