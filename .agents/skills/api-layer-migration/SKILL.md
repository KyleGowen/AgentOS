---
name: api-layer-migration
description: Excelsior API layer migration workflow. Use for route migration, v1 endpoints, thinning src/routes, moving Express handlers into src/api/http/*.http.ts, aligning services under src/api/services or src/services, updating API_DOCUMENTATION.md and API_V1.md, or following MIGRATION_ARCHITECTURE.md.
---

# API Layer Migration

Migrate Express HTTP routes to the encapsulated Excelsior backend API under
`src/api/`. Run from the Excelsior repo root.

## Source Files

Read these before changing route behavior:

1. `API_DOCUMENTATION.md` for the legacy `/api/...` contract.
2. `API_V1.md` for the `/api/v1/...` contract.
3. `API_MIGRATION_CHECKLIST.md` for the next migration target and completion columns.
4. `MIGRATION_ARCHITECTURE.md` for layers, admin namespace, testing, and JWT rules.
5. `src/api/.cursorrules` and the relevant route or HTTP module source files.
6. `references/REFERENCE.md` when templates or evolving conventions are needed.

## Core Rules

- Keep legacy `/api/...` routes thin and documented in `API_DOCUMENTATION.md`.
- Put v1 handlers only in `src/api/http/*.http.ts` and document them in `API_V1.md`.
- Use the v1 envelope `{ data, meta, errors }`; do not return legacy `{ success, data, error }` from v1 routes.
- Put shared business logic in service classes. HTTP modules should not call the database directly.
- Reuse existing authentication and password verification. Do not change hashing or password storage in this workflow.
- Put admin behavior only under `/api/v1/admin/...`; do not trust client-supplied admin flags.

## Migration Loop

```text
API migration:
- [ ] 1. Pick the next checklist row or the user-specified route group
- [ ] 2. Implement or extend HTTP-agnostic services
- [ ] 3. Add request models and public DTOs for changed contracts
- [ ] 4. Add or update the v1 HTTP module and route registration
- [ ] 5. Remove the owned legacy handler and update all callers
- [ ] 6. Run security pass for auth, authorization, logs, and status codes
- [ ] 7. Add or update unit and integration tests
- [ ] 8. Update API docs and checklist status
- [ ] 9. Restart the local dev server after completed route work
- [ ] 10. Verify the route or UI flow in a browser against local dev
```

## Testing Gate

- Unit test every touched `*.http.ts` happy path and main auth, validation, forbidden, and error paths.
- Include at least one Supertest integration test per touched HTTP module when DB/app wiring matters.
- Update fetch mocks with `ok: true` when production code checks `response.ok`.
- Run the smallest relevant tests first, then broader checks before ship.

## Browser Proof

After route work is complete, restart local dev so Express mount order, cookies,
CORS, and caches match the code. Verify the migrated route or the UI flow that
uses it against `http://127.0.0.1:<PORT>/` with the local browser tooling
available in the active environment.

## Hard Stops

- Leaving old and new URLs working indefinitely for the same owned resource.
- Changing legacy JSON without updating `API_DOCUMENTATION.md` and tests.
- Documenting v1 behavior in `API_DOCUMENTATION.md` instead of `API_V1.md`.
- Missing HTTP module unit coverage or required integration coverage.
- Skipping local browser verification after route migration work.

## Post-Run Learning

After a meaningful run, capture safe efficiency lessons for future API migrations:

- Record repeated route patterns, test gaps, integration-test triggers, or documentation drift in the appropriate AgentOS memory or Excelsior context.
- Note reusable migration templates, helper-script improvements, and recurring failure signatures as proposed skill improvements.
- Do not store secrets, private work data, raw logs, or unnecessary local machine details.
- Do not rewrite this `SKILL.md` automatically. Promote a change only when the lesson is stable, source-grounded, and likely to reduce future work.
