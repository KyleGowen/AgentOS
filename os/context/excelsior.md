# Excelsior Context

Last checked: 2026-08-16 from `/Users/kyle/cursored`.

Excelsior is Kyle's main personal software project and creative outlet. It is an
OverPower web app for card browsing, deck building, collection tracking, and
community features used by a small but real player community.

## Authority and routing

- Production site: <https://excelsior.cards>.
- GitHub repository: <https://github.com/KyleGowen/excelsior>.
- Current local authority: `/Users/kyle/cursored`, confirmed on `main` at
  `33c1afe5` (`Add AgentOS inheritance guidance and status checks`) with
  `origin` pointing to `KyleGowen/excelsior` and aligned to `origin/main`.
- Do not select `/Users/kyle/Projects/excelsior` or another checkout merely
  because it exists. Confirm the current checkout's remote before using it.
- Excelsior's root `AGENTS.md`, nested instructions, source, documentation,
  skills, issues, pull requests, runtime evidence, and production evidence are
  authoritative for detailed or changing product and technical state.
- AgentOS is authoritative only for Kyle's global identity, governance,
  cross-project rules, and AgentOS course state.

## Permanent AgentOS inheritance

Excelsior checks in a compact global-rules cache and provenance manifest under
`.agentos/`, plus a read-only status script and a detailed inheritance contract
in `docs/current/AGENTOS_INHERITANCE.md`.

- Excelsior-specific instructions override inherited AgentOS rules when they
  conflict, and material conflicts are reported.
- The cache includes only global cross-project rules and excludes other AgentOS
  project context.
- Committed AgentOS `main` is the shared upstream source; uncommitted AgentOS
  work is never inherited.
- AgentOS receives only compact, durable, summary-level Excelsior updates
  through the documented write allowlist. Detailed implementation state stays
  in Excelsior.

## Stable care points

- Preserve user data and service continuity.
- Ask before production-impacting behavior, database mutation, deployments, or
  other actions that could affect real users unless a current Excelsior
  instruction expressly authorizes the action.
- Preserve Excelsior's database migration, API/architecture, security, SOC 2,
  testing, lint, release, and repo-local skill requirements.
- Keep both desktop and mobile UX in view.
- Treat the game-owner relationship delicately.
