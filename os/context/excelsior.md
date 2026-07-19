# Excelsior Context

Last checked: 2026-07-19 from local repos `/Users/kyle/Projects/excelsior`
and `/Users/kyle/cursored`.

Excelsior is Kyle's main personal software project and creative outlet. It is a
web app for OverPower with card browsing, deck building, collection tracking,
community deck surfaces, tournament deck surfaces, and card-data workflows for a
small but real user community.

## Source Of Truth

- Production site: <https://excelsior.cards>
- GitHub repository: <https://github.com/KyleGowen/excelsior>
- Verified local checkouts: `/Users/kyle/Projects/excelsior` and `/Users/kyle/cursored`.
- Preferred working surface: Codex. Kyle is trying to do Excelsior work in
  Codex now instead of Cursor.
- Cursor skill source exists in `/Users/kyle/cursored/.cursor/skills/` and
  `/Users/kyle/Projects/excelsior/.cursor/skills/`.
- Excelsior repo-local Codex skills exist in `/Users/kyle/cursored/.agents/skills/`.

When the two local checkouts disagree, prefer the checkout that matches the
current task's source files and verify with git before editing.

## Current Product Shape

- Excelsior v2 has shipped with a UI overhaul and positive community response.
- The app now has Home rails for community decks and tournament winning decks.
- The Home experience now includes a Columbus Regional breakdown/dashboard with
  stats, View All behavior, podium links, mobile layout work, and seeded Columbus
  podium decks for the tournament deck rail.
- The deck editor Add Cards desktop pane was recently improved with a stronger
  list/detail layout and local UI/UX readability guidance.
- Collection UX has recently improved with quantity controls, disabled minus
  behavior for unowned cards, hover-preview fixes around controls, layout fixes,
  and a fixed back-to-top control.
- Recent card-data work added ERB alternate-art and foil migrations, including
  Invisible Man ERB 498 / 498F alternate art, Jane Porter 102F, Tarzan 234F, and
  Zorro 289F foil rows.
- Training Any-Power deck validation was corrected and documented; preserve
  these deck-legality semantics when touching validation.

## API Layer State

Excelsior is migrating from legacy Express `/api/...` routes to `/api/v1/...`
under `src/api/`.

- `API_DOCUMENTATION.md` documents legacy routes.
- `API_V1.md` documents v1 routes and the `{ data, meta, errors }` envelope.
- `API_MIGRATION_CHECKLIST.md` tracks migration completion.
- `MIGRATION_ARCHITECTURE.md` explains service layers, admin namespace rules,
  testing expectations, and JWT/session boundaries.
- As of this check, DBV/catalog, auth, decks, collections, guest decks, admin,
  static/health non-v1 surfaces, and catalog/DBV auth are documented as migrated
  or intentionally non-v1 in the checklist.

## Skills

AgentOS tracks Excelsior skills in two forms:

- Native Cursor archives under `os/skills/native/cursor/<skill-name>/`.
- Codex-executable translations under `.agents/skills/<skill-name>/`.

Prefer improving or creating Codex-native skills when an Excelsior workflow needs
to mature. Use Cursor skill text as source material, not as the default runtime.

Current Excelsior skills include:

AgentOS-installed translations:

- `add-card`
- `add-community-deck`
- `add-tournament-deck`
- `api-layer-migration`
- `pdf-to-png`
- `ship`
- `start`
- `start-aws-db-tunnel`

Excelsior repo-local Codex skills:

- `fix-trivy`
- `start-local-dev`

## Care Points

- Preserve user data and avoid service disruption.
- Ask before production-impacting behavior, database mutation, deploys, or
  anything that could affect real users.
- Keep desktop and mobile UX in view.
- Treat the game-owner relationship delicately.
- Keep AgentOS memory summary-level; use the Excelsior repo for current
  implementation facts.
