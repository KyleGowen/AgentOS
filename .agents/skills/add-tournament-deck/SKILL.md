---
name: add-tournament-deck
description: Excelsior tournament deck import workflow. Use when the user says add tournament deck, import tournament deck, wants to populate the Home Tournament Winning Decks rail, or pastes exported deck JSON in v2.0 format to publish under the internal tournament_decks account.
---

# Add Tournament Deck

Import an exported Excelsior deck JSON file into the internal tournament decks
account. Run from the Excelsior repo root.

## Workflow

```text
Add tournament deck:
- [ ] 1. Validate JSON has name and cards in v2.0 export shape
- [ ] 2. Save JSON to a temp file
- [ ] 3. Run npm run import:tournament-deck -- <temp-file>
- [ ] 4. Report deck id, name, cards added, and unresolved card names
- [ ] 5. Delete the temp file if created for this task
- [ ] 6. For production, regenerate the Flyway seed migration when adding to a deploy
```

## Account

- Username: `tournament_decks`
- Local development password for manual login/editor edits: do not store in AgentOS; read the source checkout if needed
- User id: `00000000-0000-0000-0000-000000000003`

The CLI import uses the database directly and does not need login credentials.

## Steps

1. Accept deck JSON pasted in chat or an existing `.json` path.
2. Validate it as JSON before running the import. Hard stop if `name` or `cards` is missing.
3. Save pasted JSON to `tmp/tournament-deck-import.json`, creating `tmp/` if needed.
4. Run:

```bash
npm run import:tournament-deck -- tmp/tournament-deck-import.json
```

5. Interpret script exits:
   - Exit 0: success; report deck id, deck name, and card count.
   - Exit 2: partial success; report warning list and unresolved card names.
   - Exit 1: failure; show the error and do not claim success.
6. Optionally verify `GET /api/v1/decks/tournament` as an authenticated user includes the deck near the top.
7. Click the Home Tournament Winning Decks tile when browser verification is in scope; the deck editor should load instead of "Deck not found".
8. Delete the temp file if Codex created it.

Imported decks are public automatically so users can open them from the Home rail.
For production deploys, prefer including the deck in a generated Flyway seed
migration so stable deck and card row IDs ship with the release.

## Hard Stops

- Invalid JSON: fix syntax or ask for valid JSON; do not run import.
- Missing `name` or `cards`: ask for a complete v2.0 export.
- Database not running: start local dev DB and apply migrations first.
- All cards unresolved: report failure and investigate export names versus catalog data.

## Related

- `scripts/import-tournament-deck.ts`
- `scripts/seed-tournament-decks.ts`
- `src/services/deckExportImport/`
- Home tournament deck feature documentation in the Excelsior repo

## Post-Run Learning

After a meaningful run, capture safe efficiency lessons for future tournament deck imports:

- Record repeated export-shape issues, seeding errors, validation shortcuts, or home-rail update friction in the appropriate AgentOS memory or Excelsior context.
- Note helper-script improvements and recurring ambiguity as proposed skill improvements.
- Do not store secrets, private work data, raw logs, or unnecessary local machine details.
- Do not rewrite this `SKILL.md` automatically. Promote a change only when the lesson is stable, source-grounded, and likely to reduce future work.
