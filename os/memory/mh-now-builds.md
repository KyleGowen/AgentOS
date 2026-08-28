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

### Tobi-Kadachi Gunlance — Blast Dash — Gold Thunder recommendation

- **Status:** Current adopted/explored recommendation
- **Persisted:** 2026-08-28
- **Evidence date:** 2026-08-28
- **Scope:** General-purpose practical-DPS Blast Dash build for Tobi-Kadachi Gunlance against monsters weak to Thunder; hybridizes aerial Burst Fire shelling with the weapon's large Thunder component rather than treating Long shelling as pure shelling.
- **Weapon:** Tobi-Kadachi Gunlance (`Pulsar Gunlance` / `Kadachi Striker` line), Blast Dash style. Verified Long shelling; at G10.5 current data lists 1549 attack + 1131 Thunder and Evade Extender 1 from G8+.
- **Style/customization:** Blast Dash. Prioritize the weapon's physical/elemental style upgrades after unlocking the style; Ground Splitter is part of the shelling-buff setup. Exact per-node style-custom allocation was not independently enumerated in the 2026-08-28 web evidence and should be rechecked before spending rare style resources.
- **Armor snapshot:**
  - Head: Quematrice Helm
  - Chest: Basarios Mail
  - Arms: Kaiser Vambraces
  - Waist: Astalos Coil
  - Legs: Astalos Greaves
- **Owned baseline:** All five pieces were present in the 2026-08-27 inventory sweep (Quematrice Head 132; Basarios Chest 197; Kaiser Arms 193; Astalos Waist 142; Astalos Legs 142).
- **Driftsmelt snapshot:**
  - Quematrice Helm: Thunder Attack — Amber Driftstone / Thunder Attack Driftgem
  - Basarios Mail: Thunder Attack — Amber Driftstone / Thunder Attack Driftgem
  - Kaiser Vambraces: Thunder Attack — Amber Driftstone / Thunder Attack Driftgem
  - Astalos Coil: Weakness Exploit — Cyan Driftstone / Weakness Exploit Driftgem
  - Astalos Greaves: Weakness Exploit — Cyan Driftstone / Weakness Exploit Driftgem
- **Key resulting skill totals/breakpoints:** Artillery is supplied at 6 native levels but caps at Artillery 5 effect (40% shelling/Wyvern's Fire damage and +1 Gunlance ammo); Thunder Attack 5 after three smelts (+500 Thunder); Advanced Thunder Attack 2 from Astalos Coil + Greaves (+400 Thunder while Thunder Attack 5+ is active); Critical Element 1 and Critical Eye 1 from Astalos Coil; Weakness Exploit 2 after two smelts (25% affinity on weak points); Lock On 1 from Quematrice Helm; Guard 1 from Kaiser Vambraces; Evade Extender 1 from the weapon at G8+.
- **Core rotation:** Lock onto an accessible weak point for the physical/Thunder portions. Use Ground Splitter when practical to establish/refresh its shelling buff, then Blast Dash → Aerial Smash → Aerial Burst Fire. Reload and repeat around openings; exploit the Long gunlance's reach/charged-shell option when an aerial loop is unsafe rather than forcing a bad commitment.
- **Why selected:** This keeps capped Artillery for Blast Dash aerial Burst Fire while reaching Thunder Attack 5 and Advanced Thunder Attack 2 for the large elemental component. Astalos Coil adds Critical Element/Critical Eye, and Quematrice Helm preserves Lock On for general weak-point consistency. It is designed as a reusable Thunder-weak-target loadout, not a single-monster scripted matchup.
- **Confidence:** High on the verified armor skills, weapon stats/shelling type, Artillery/Thunder/Advanced Thunder breakpoints, and Driftsmelt availability; medium on exact mathematical supremacy because no independent full-combo DPS calculator comparison was available in the evidence set.
- **Freshness trigger:** Revalidate if Blast Dash/Ground Splitter behavior, Artillery cap or shelling scaling, Tobi-Kadachi style customization, Astalos Advanced Thunder Attack/Critical Element skills, July-2026 Kaiser balance changes, Driftsmelt pools, or a target-specific Thunder hitzone changes materially.
