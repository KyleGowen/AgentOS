---
name: ship
description: "Excelsior release gate and git workflow. Use when the user says ship, ship it, asks to commit and push after checks, or wants the Excelsior release gate: lint, conditional unit tests, optional integration tests, SOC 2 checks for HTTP paths, optional daily npm audit, debug cleanup, stage, commit, and push."
---

# Ship

When the user says "ship", commit and push the intended Excelsior changes after
the gates pass. Project rules in `.cursorrules`, especially the Ship Command
section, remain the source of truth.

## Checklist

```text
Ship progress:
- [ ] 1. ESLint clean
- [ ] 2. Unit tests pass or conditional script skips cleanly
- [ ] 2b. Integration tests when in scope
- [ ] 3. SOC 2 script when endpoint paths changed
- [ ] 4. npm audit when required
- [ ] 5. No debug statements
- [ ] 6. Stage, commit, push
```

## Checks

- Lint from repo root: `npx eslint src --ext .ts --max-warnings 0`.
- Unit tests: `bash scripts/ship-conditional-test.sh unit`. Treat skip output with exit 0 as pass.
- Force unit rerun after fixing unchanged-tree failures with `SHIP_TESTS_FORCE=1 bash scripts/ship-conditional-test.sh unit`.
- Integration tests when included: `bash scripts/ship-conditional-test.sh integration`; force with `SHIP_TESTS_FORCE=1`.
- SOC 2 is required when the ship diff touches `src/index.ts`, `src/routes/`, or `src/api/http/`; run `bash scripts/soc2-compliance-checks.sh`.
- Run `npm audit` before the first git push of each calendar day, and always when `package.json` or `package-lock.json` changed. Run `npm audit fix` for fixable vulnerabilities, then re-audit.
- Remove temporary debug output such as `console.log` and `console.debug`, while preserving legitimate production logging.

Prefer parallel execution for independent checks when tools allow it. Re-run
only failed gates after fixes.

## Git

After checks pass:

1. Review the diff and intended file list.
2. Stage intended changes only, or all changes when the user's ship intent clearly covers the full working tree.
3. Commit with a descriptive message matching project conventions.
4. Push to the configured remote.

Do not commit if any required gate fails.

## Hard Stops

- ESLint warnings or errors.
- Unit or in-scope integration test failures.
- SOC 2 script failure when endpoint paths changed.
- Required audit reports fixable vulnerabilities that remain unresolved.
- Debug noise remains in the diff.
- Unrelated working-tree changes would be swept into the commit.

## Optional Cross-Checks

If HTTP contracts changed, update the applicable API docs according to
`.cursorrules` and `AGENTS.md`. Ship does not replace integration tests for
large or risky changes.

## Post-Run Learning

After a meaningful run, capture safe efficiency lessons for future releases:

- Record repeated release-gate friction, test-selection signals, CI failures, or documentation drift in the appropriate AgentOS memory or Excelsior context.
- Note helper-script improvements and recurring verification shortcuts as proposed skill improvements.
- Do not store secrets, private work data, raw logs, or unnecessary local machine details.
- Do not rewrite this `SKILL.md` automatically. Promote a change only when the lesson is stable, source-grounded, and likely to reduce future work.
