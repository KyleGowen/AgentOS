# Wanted Card Listings

## Purpose

Automatically scan public eBay listings for wanted OverPower and Magic: The Gathering cards, then produce a sorted read-only report of active opportunities.

This file is the harness-neutral source of truth. A scheduler, agent runner, shell script, or Codex automation can implement it as long as it follows the contract below.

## Schedule

- Run once daily at 6:00 AM Pacific time, observing PST/PDT (`America/Los_Angeles`).
- Run immediately after a new card is added to `os/context/wanted-trading-cards.md` or an existing card is changed from `Draft` to `Active`.
- Refresh every active card's cached retail baseline twice weekly: on the first scheduled run each Monday and each Friday, using Kyle's local timezone. On all other scheduled runs, reuse valid cached values unless a baseline is missing or invalid.
- Use Kyle's local timezone when the scheduler supports explicit timezone configuration.

The add-card trigger is a full-list refresh: process every `Active` wanted card and replace the latest report for the whole list. Do not produce a single-card-only report unless Kyle explicitly asks for one.

## Input Files

| File | Purpose | Status |
|---|---|---|
| `os/context/wanted-trading-cards.md` | Active wanted-card list, search context, ended comparable auction links, image references, and variant notes. | Active |
| `.agents/skills/find-card-listings/` | Codex skill that performs the scan and report generation. | Active |

## Efficient Runner State

Scheduled runners may keep an opaque, runner-owned ledger of **known active item URLs** and **recurring rejected candidate URLs**, keyed to the active wanted-card entry. This ledger is an optimization only; it is not policy, not a retail baseline source, and not a substitute for logged-out item-page verification.

- Start each scheduled run from cached retail baselines in `os/context/wanted-trading-cards.md`, known active item URLs from runner state, and recent rejected candidates.
- Re-open known active item URLs first. Keep them in the report only if the logged-out item page still verifies active status, price, shipping, and target match.
- Re-check recurring rejected candidates only when their rejection reason might have changed, such as a generic item-page error, missing domestic shipping, or an unbound multi-variation selection. Do not repeatedly inspect permanently irrelevant non-target items.
- Run a capped discovery pass for every active card after checking known URLs. Use exact card terms first, then broader lot/bulk terms only when the card has no verified active listing, recent evidence is stale, or the wanted-card context specifically calls for broad discovery.
- Record only durable, non-private facts needed for future efficiency: item URL, card name, last checked date/time, active/rejected status, compact rejection reason, and the verified total when reportable.
- Do not record raw eBay HTML, cookies, account data, seller messages, private data, or full page dumps.
- Do not let runner state suppress safety checks. Every reportable row still requires logged-out item-page verification during the current run.

## Runner Contract

For each active wanted card:

1. Read card name, game, variant constraints, description, optional image, search terms, negative terms, and ended auction comparables from `os/context/wanted-trading-cards.md`.
2. If an image is provided, inspect it and extract concrete visual cues before searching.
3. Re-open known active item URLs from runner state, if present, while logged out.
4. Re-check recent rejected candidates only when their rejection reason might have changed.
5. Search eBay as a logged-out user in a browser Codex launches itself. Kyle has authorized this separate browser, but never use his normal browser profile, cookies, or account session. Start every run in a new temporary private/incognito profile and confirm eBay shows its sign-in/register affordance before searching. Public pages, public APIs, and web results are supplementary discovery only; never run a raw-client-only scan or treat its `403`, CAPTCHA, or challenge as a zero-results outcome.
6. Search exact card terms first, then broader lot/bulk terms only when needed for coverage under the Efficient Runner State rules.
7. Open individual listing detail pages while logged out for every reportable candidate.
   - For auctions, retrieve the current bid through a fresh, uncached detail-page request immediately before report generation. Do not reuse cached HTML, a prior fetch, item revision time, search snippets, or runner-state totals as a current auction price. If a fresh bid cannot be verified after a logged-out retry, move the listing to skipped/uncertain.
8. Remove ended, completed, sold, and out-of-stock listings from the candidate set. Immediately before creating a summary or table row, re-open the individual item page and confirm current purchasable status: auctions need a live bid action and countdown; buy-it-now listings need a current guest checkout/purchase action and no sold, ended, unavailable, or out-of-stock status. A historical `N sold` count alone is not a sold status when availability and purchase action remain explicit.
9. Compare active candidate listings against the card's cached retail baseline in `os/context/wanted-trading-cards.md`.
10. If the wanted-card entry has no cached retail baseline, check the relevant retail baseline once, update the wanted-card context, and use that cached value for future runs.
    - On the first scheduled run each Monday and Friday in Kyle's local timezone, refresh the retail baseline for every active card and update its price, checked date, canonical URL, and stock note when available.
11. For OverPower cards missing a cached baseline, use only The Orange King retail site at <https://theorangeking.com/> as the retail baseline; do not use The Orange King's eBay account or any eBay listing as a retail baseline.
12. For OverPower cards supplied with a The Orange King product URL, use that product page as the preferred retail seed. Normalize away tracking query parameters and cache the canonical product URL, price, checked date, and any stock note.
13. For Magic: The Gathering cards missing a cached baseline, use Brute Force MTG at <https://www.bruteforcemtg.com/> as the retail baseline.
14. Update runner-owned known-active and rejected-candidate state when the runner supports it.
15. Group the report by game first, then produce one table per card under the matching game heading, sorted by price plus shipping ascending.
16. Use US/domestic shipping in totals when visible. If only international shipping is visible, say so in notes.
17. Include days remaining for every row: numeric days for auctions, `n/a` for verified buy-it-now listings with no visible countdown.
18. Link rows to individual eBay item pages only; seller pages, category pages, and search pages belong in skipped/uncertain notes.
19. If eBay returns a generic error page for a candidate item URL, keep it in skipped/uncertain unless an exact item-page screenshot or another accessible item-detail source verifies price, shipping, and active status. When a discovery source visibly shows title, price, and domestic shipping, preserve the shown values as a compact `Discovery-only` bullet with its unverified status; never include it in the summary or active tables.
20. Include notes such as `part of a bulk deal`, `comes with other cards`, `variant uncertain`, `image cues matched`, or `below retail baseline`.
21. Report search limitations, missing baseline cache, skipped ambiguity, and skipped ended/sold listings compactly.

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

Rows must be sorted by total price plus shipping ascending. Auctions/listings that have ended, completed, sold, or become out of stock must be removed from the opportunity summary and detailed output, including when that status changes during the scan.

## Implementation Notes

- Codex implementation: use `.agents/skills/find-card-listings/`.
- Current Codex automation ID: `wanted-card-listings`.
- Codex cron schedule is configured for 6:00 AM Pacific daily, but the live job
  is currently paused because the required isolated logged-out browser is
  unavailable. The list-change full refresh remains an event trigger; no
  separate startup run is scheduled.
- Non-Codex implementation: use the same runner contract with equivalent public web or marketplace APIs.
- Treat this file as policy/config, not generated output. Update wanted cards in `os/context/wanted-trading-cards.md` before changing scheduler prompts.
