---
name: start
description: Excelsior v2 local dev stack startup workflow. Use when the user says /start, start dev server, start the dev servers, or wants local Excelsior development at http://localhost:5173 with Express API on 8085, Vite SPA on 5173, automatic API migrations, and formatted health verification.
---

# Start Excelsior

Start the Excelsior v2 dev stack: Express API at `127.0.0.1:8085` and Vite SPA
at `http://localhost:5173` with LAN enabled.

## Rules

- Start API first. Vite proxies `/api` to the API.
- Do not run `npm run migrate` separately for normal `/start`; migrations run during API boot via `DatabaseInitializationService.initializeDatabase()`.
- If API boot fails because local Flyway is missing, apply pending SQL with `bash scripts/flyway-docker.sh migrate`, then restart API with `SKIP_MIGRATIONS=true` if needed.
- On success, output the formatted health check and URLs.
- If the API never becomes healthy, do not start Vite; return the full API `npm run dev` terminal log for diagnosis.

## Workflow

```text
/start progress:
- [ ] 1. Inspect running terminals/processes
- [ ] 2. Probe API and Vite
- [ ] 3. Start or restart API in background
- [ ] 4. Wait for API health or fail with API log
- [ ] 5. Start or restart Vite after API is healthy
- [ ] 6. Wait for Vite, then print health check
```

## Commands

Probe from repo root:

```bash
curl -sf http://localhost:8085/health >/dev/null && echo API_OK || echo API_DOWN
curl -s -o /dev/null -w "%{http_code}" http://localhost:5173
```

Start API from repo root:

```bash
npm run dev
```

Start Vite from `frontend/` only after API health passes:

```bash
npm run dev
```

On success, run:

```bash
bash scripts/dev-health-check.sh
```

Fallback formatting:

```bash
curl -s http://localhost:8085/health | jq -r -f scripts/dev-health-check.jq
```

## Hard Stops

- API never healthy: output API terminal log only; do not start Vite or claim success.
- Port already in use: identify the owning process; do not stack duplicate servers.
- Vite never returns a successful dev response after API is healthy: show Vite terminal error.
- `jq` missing: use raw health JSON and note formatting skipped.

## Related

- `src/services/databaseInitialization.ts`
- `.cursor/rules/v2-dev-server.mdc`
- `.cursor/rules/local-dev-lan.mdc`
- `docs/current/FRONTEND_V2.md`

## Post-Run Learning

After a meaningful run, capture safe efficiency lessons for future dev-server starts:

- Record repeated install, port, Postgres, migration, Vite, API health, or browser-verification friction in the appropriate AgentOS memory or Excelsior context.
- Note helper-script improvements and recurring validation shortcuts as proposed skill improvements.
- Do not store secrets, private work data, raw logs, or unnecessary local machine details.
- Do not rewrite this `SKILL.md` automatically. Promote a change only when the lesson is stable, source-grounded, and likely to reduce future work.
