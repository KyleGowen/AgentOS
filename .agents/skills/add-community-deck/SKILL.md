---
name: add-community-deck
description: Excelsior community deck import workflow. Use when the user says add community deck, import community deck, wants to populate the Home Community Decks rail, or pastes exported deck JSON in v2.0 format to publish under the internal community_decks account.
---

# Add Community Deck

Import an exported Excelsior deck JSON file into the internal community decks
account. Run from the Excelsior repo root.

## Workflow

```text
Add community deck:
- [ ] 1. Validate JSON has name and cards in v2.0 export shape
- [ ] 2. Save JSON to a temp file
- [ ] 3. Run npm run import:community-deck -- <temp-file>
- [ ] 4. Report deck id, name, cards added, and unresolved card names
- [ ] 5. Delete the temp file if created for this task
```

## Steps

1. Accept deck JSON pasted in chat or an existing `.json` path.
2. Validate it as JSON before running the import. Hard stop if `name` or `cards` is missing.
3. Save pasted JSON to `tmp/community-deck-import.json`, creating `tmp/` if needed.
4. Run:

```bash
npm run import:community-deck -- tmp/community-deck-import.json
```

5. Interpret script exits:
   - Exit 0: success; report deck id, deck name, and card count.
   - Exit 2: partial success; report warning list and unresolved card names.
   - Exit 1: failure; show the error and do not claim success.
6. Optionally verify `GET /api/v1/decks/community` as an authenticated user includes the deck near the top.
7. Delete the temp file if Codex created it.

## Hard Stops

- Invalid JSON: fix syntax or ask for valid JSON; do not run import.
- Missing `name` or `cards`: ask for a complete v2.0 export.
- Database not running: start local dev DB and apply migrations first.
- All cards unresolved: report failure and investigate export names versus catalog data.

## Related

- `scripts/import-community-deck.ts`
- `src/services/deckExportImport/`
- `frontend/src/features/home/COMMUNITY_DECKS.md`

## Post-Run Learning

After a meaningful run, capture safe efficiency lessons for future community deck imports:

- Record repeated export-shape issues, importer errors, validation shortcuts, or home-rail update friction in the appropriate AgentOS memory or Excelsior context.
- Note helper-script improvements and recurring ambiguity as proposed skill improvements.
- Do not store secrets, private work data, raw logs, or unnecessary local machine details.
- Do not rewrite this `SKILL.md` automatically. Promote a change only when the lesson is stable, source-grounded, and likely to reduce future work.
