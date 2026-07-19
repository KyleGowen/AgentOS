# Wanted Card Listings

## Purpose

Automatically scan public eBay listings for wanted OverPower and Magic: The Gathering cards, then produce a sorted read-only report of active opportunities.

This file is the harness-neutral source of truth. A scheduler, agent runner, shell script, or Codex automation can implement it as long as it follows the contract below.

## Schedule

- Run every 4 hours starting at midnight: 12:00 AM, 4:00 AM, 8:00 AM, 12:00 PM, 4:00 PM, and 8:00 PM.
- Run on startup.
- Run immediately after a new card is added to `os/context/wanted-trading-cards.md` or an existing card is changed from `Draft` to `Active`.
- Use Kyle's local timezone when the scheduler supports explicit timezone configuration.

The add-card trigger is a full-list refresh: process every `Active` wanted card and replace the latest report for the whole list. Do not produce a single-card-only report unless Kyle explicitly asks for one.

## Input Files

| File | Purpose | Status |
|---|---|---|
| `os/context/wanted-trading-cards.md` | Active wanted-card list, search context, ended comparable auction links, image references, and variant notes. | Active |
| `.agents/skills/find-card-listings/` | Codex skill that performs the scan and report generation. | Active |

## Runner Contract

For each active wanted card:

1. Read card name, game, variant constraints, description, optional image, search terms, negative terms, and ended auction comparables from `os/context/wanted-trading-cards.md`.
2. If an image is provided, inspect it and extract concrete visual cues before searching.
3. Search eBay as a logged-out user using public pages, public APIs, or public web results.
4. Search exact card terms and broader lot/bulk terms that could include the card.
5. Open individual listing detail pages while logged out for every reportable candidate.
6. Remove ended, completed, and sold listings from the candidate set.
7. Compare active candidate listings against the card's cached retail baseline in `os/context/wanted-trading-cards.md`.
8. If the wanted-card entry has no cached retail baseline, check the relevant retail baseline once, update the wanted-card context, and use that cached value for future runs.
9. For OverPower cards missing a cached baseline, use only The Orange King retail site at <https://theorangeking.com/> as the retail baseline; do not use The Orange King's eBay account or any eBay listing as a retail baseline.
10. For OverPower cards supplied with a The Orange King product URL, use that product page as the preferred retail seed. Normalize away tracking query parameters and cache the canonical product URL, price, checked date, and any stock note.
11. For Magic: The Gathering cards missing a cached baseline, use Brute Force MTG at <https://www.bruteforcemtg.com/> as the retail baseline.
12. Group the report by game first, then produce one table per card under the matching game heading, sorted by price plus shipping ascending.
13. Use US/domestic shipping in totals when visible. If only international shipping is visible, say so in notes.
14. Include days remaining for every row: numeric days for auctions, `n/a` for verified buy-it-now listings with no visible countdown.
15. Link rows to individual eBay item pages only; seller pages, category pages, and search pages belong in skipped/uncertain notes.
16. If eBay returns a generic error page for a candidate item URL, keep it in skipped/uncertain unless an exact item-page screenshot or another accessible item-detail source verifies price, shipping, and active status.
17. Include notes such as `part of a bulk deal`, `comes with other cards`, `variant uncertain`, `image cues matched`, or `below retail baseline`.
18. Report search limitations, missing baseline cache, skipped ambiguity, and skipped ended/sold listings compactly.

When the run is triggered by adding or activating a wanted-card entry, follow the same runner contract for every active card. The changed card is the trigger, not the scan scope.

## Safety Rules

- Never bid, buy, make offers, add items to cart, message sellers, save searches, watch listings, or sign in to eBay.
- Use a logged-out eBay context only.
- Do not use Kyle's eBay cookies, account, watch list, saved searches, seller messages, cart, or purchase history.
- Do not mutate the wanted-card context during a scheduled run.
- Do not store raw eBay HTML, account cookies, personal account data, or unnecessary seller data.
- If a listing requires logged-in access to inspect safely, skip it and note the limitation.

## Output

Primary output is a compact Markdown report. Lead every run with a one-row-per-active-card opportunity chart so Kyle can skim the result without reading the per-card evidence.

| Game | Card Name | Retail Price | Found Listing Combined Price |
|---|---|---:|---:|
| Magic: The Gathering | Example Card | $18.15 | [$17.50](https://www.ebay.com/itm/example) |

Include every active card in this chart. Use `—` when no verified active listing was found. List each verified listing separately in the final column, separated by `<br>`, and link each price to its individual eBay item page. Bold a combined price only when it is strictly lower than the retail price. The detailed, per-card tables remain the evidence layer below the chart.

Suggested scheduled-run artifact:

| Artifact | Purpose |
|---|---|
| `os/automation-output/wanted-card-listings/latest.md` | Latest active listing report. |

Each card section should include:

| Field | Required |
|---|---|
| Game group heading | Yes; group cards by the `Game` field before individual card sections |
| Card name | Yes |
| Retail baseline source and price | Best effort |
| Listing total price | Yes when available |
| Listing price | Yes when available |
| Shipping | Yes when available |
| Link | Yes; individual eBay item page only |
| Days remaining | Yes; numeric for auctions, `n/a` for verified buy-it-now listings |
| Notes | Yes when useful |

Rows must be sorted by total price plus shipping ascending. Auctions/listings that have ended, completed, or sold must be removed from the output.

## Implementation Notes

- Codex implementation: use `.agents/skills/find-card-listings/`.
- Current Codex automation ID: `wanted-card-listings`.
- Codex cron schedule is active. If the runner does not support a native startup or wanted-list-change trigger, run this automation manually on app/machine startup and immediately after adding or activating a wanted card until those hooks are available.
- Non-Codex implementation: use the same runner contract with equivalent public web or marketplace APIs.
- Treat this file as policy/config, not generated output. Update wanted cards in `os/context/wanted-trading-cards.md` before changing scheduler prompts.
