---
name: add-card
description: Excelsior card-catalog intake workflow. Use when the user says add card, invokes /add-card, or provides a path under src/resources/cards/images/ and wants a new Excelsior card added with database migration, thumbnail config, tests, docs, local migration, restart, and verification.
---

# Add Card

Use this skill in the Excelsior repository to add one card image to the catalog.
Handle one card per run. Do not write implementation files until the user
approves the proposed card summary.

## References

Read these in the Excelsior repo as needed:

- `PATH_RULES.md` for path-to-card inference.
- `CARD_TYPES.md` for type-specific columns and SQL.
- `docs/checklist-source/checklist.md` for main-line ERB cross-checks only.
- `docs/checklist-source/checklist-promos.md` for promo cross-checks only.
- `docs/current/IMAGE_PIPELINE.md` for thumbnail and image rules.
- `migrations/V257__Clear_set_numbers_and_rarity_for_all_promo_sets.sql` for promo NULL metadata.
- `frontend/src/lib/catalog/defaultCatalogCards.ts` and `frontend/src/lib/catalog/cardPrintings.ts` for printing groups.

## Workflow

Track progress:

```text
Add card:
- [ ] 1. Intake: validate image path and derive DB image_path
- [ ] 2. Parse path: type, set, and partial stats
- [ ] 3. Read image: name, text, stats, foil appearance
- [ ] 4. Cross-check checklist docs
- [ ] 5. Present summary and wait for user approval
- [ ] 6. Implement migration, thumbs, tests, docs, migrate, restart
- [ ] 7. Verify DB, thumbnails, browser, printings, deck editor, tests
```

## Intake

- Accept absolute or repo-relative paths only if they resolve under `src/resources/cards/images/`.
- Hard stop when the file is missing or outside `cards/images/`.
- Derive DB `image_path` relative to `cards/images/`, without the `src/resources/` prefix.
- Confirm the source image is committed or will be committed with the migration. Never commit generated `thumb/` files.

## Infer Metadata

Use path rules first, then image reading to confirm or fill gaps.

- `tfacp/` maps to set `TFCP`; `skyp/` to `SKYP`; `erbp/` to `ERBP`.
- `ally-universe/` or `tfacp/ally/` maps to `ally_universe_cards` with `card_type` `ally-universe`.
- `power-cards/`, `tfacp/power/`, or `skyp/power/` maps to `power_cards` with `card_type` `power`.
- Filename stat tokens include `{n}_energy`, `{n}_combat`, `{n}_brute_force`, `{n}_intelligence`, and `{n}_anypower`.
- Ally defaults follow ERB patterns: `5_*` means `stat_to_use = 5 or less`, `attack_value = 3`; `7_*` means `stat_to_use = 7 or higher`, `attack_value = 2`; `card_text = Teammate must play 1 Special card.`
- Power defaults: leading number is `value`, suffix is `power_type`, name is `{value} - {PowerType}`, promo powers are usually `one_per_deck = TRUE`.
- `_2` before extension means a distinct second printing image path.

Read the image to extract display name, text, attack lines, character stats,
special character name, and foil appearance. Normalize ally text with digit `1`,
power names as `7 - Energy`, and universe descriptions such as `{Name} ally card`.

## Cross-Check

- For main-line ERB, match `name`, `set_number`, and `rarity` in `docs/checklist-source/checklist.md`. Hard stop if no match.
- For promo sets `TFCP`, `SKYP`, and `ERBP`, cross-check promos when helpful, but keep `set_number`, `set_number_foil`, and `rarity` NULL in the database.
- Never edit checklist source files or `docs/current/COLLECTION_CHECKLIST_SOURCE.md` during add-card.
- Flag conflicts between path inference, image reading, and checklist sources.

## Approval Gate

Before editing, present a proposed-card table including:

- Source file and DB `image_path`.
- Table, `card_type`, set, name, type-specific fields, `is_foil`, `one_per_deck`, and promo NULL metadata.
- `foil_card_map` only for power/training foil-only cases, not non-foil ally promos.
- Printing group for ally/power promos.
- Thumbnail subdir and whether `PROMO_ART_SUBDIRS` needs a new entry.
- Migration name, docs to update, tests to update, and verification plan.

Ask when foil-only status, base-card link, second printing, checklist numbers, or
`one_per_deck` are ambiguous. For ally promos, confirm the ERB stat-slot base
and rely on grouping by `stat_to_use|stat_type_to_use`; do not use
`foil_card_map` for non-foil ally promos.

## Implement After Approval

- Re-glob `migrations/V*.sql` and choose max version + 1.
- Name migrations like `V{N}__{SET}_{short_description}.sql`.
- Use idempotent insert/update patterns and avoid migration version collisions.
- For ally migrations, never include `first_attack_bonus` or `second_attack_bonus`; those columns were removed.
- For foil-only power/training promos, follow existing foil-only migration patterns and remap related rows before deleting the non-foil row.
- Apply migrations with the repo's Flyway Docker script.
- Add `PROMO_ART_SUBDIRS` entries only for new set-scoped promo image subdirs and update `tests/unit/generateCardThumbnails.config.test.ts`.
- Run `npm run generate:thumbnails` when thumbnail config changes.
- Update tests for promo paths, foil semantics, thumbnail config, printings, alternate power cards, or collection captions as applicable.
- Update `docs/current/IMAGE_PIPELINE.md` only when adding a new set-scoped promo image subdir.
- Restart both dev servers after migration: repo root `npm run dev` on `:8085` and `frontend/npm run dev` on `:5173`.

## Verify

- DB row exists for `image_path`, set, and foil status.
- Thumbnail exists and serves through Vite proxy.
- Browser DBV shows the card with correct tab, set filter, foil filter, and image.
- Ally/power promos appear under the ERB base card's Printings and as their own grid tile.
- Deck editor can add the card.
- Unit tests pass.

Do not commit or ship unless the user explicitly asks to ship.

## Hard Stops

- Missing image file.
- Cannot read required metadata from image.
- Ambiguous foil/base-card link.
- Main-line ERB without checklist match.
- Migration version collision after re-glob.
- Flyway checksum error.
- Unknown `foil_card_map` base row.
- Ally insert uses removed bonus columns.
- Attempt to edit checklist source files.
