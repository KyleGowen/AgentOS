# Reporting Reference

Use this reference for scheduled and on-demand wanted-card reports.

## Report Header

Start with:

- Run timestamp with timezone.
- Scope: number of active wanted cards scanned.
- Access note: confirm eBay was checked logged out and whether retail baselines were verified.

## Per-Card Section

Group cards by game first, then use one section per wanted card inside each game group. Preserve the game names from the wanted-card context, normally `Magic: The Gathering` and `OverPower`.

```markdown
## Game Name

### Card Name

Baseline: $X.XX at Retail Source, checked YYYY-MM-DD. Target context: short variant summary.

| Total | Price | Shipping | Days Left | Listing | Notes |
|---:|---:|---:|---:|---|---|
| $12.34 | $9.99 | $2.35 | 3.4 | [Listing title](https://example.com) | exact match; below retail baseline |
```

Rules:

- Use `##` headings for game groups and `###` headings for individual cards.
- Keep all active cards from the same game together. Within each game group, keep the order from `os/context/wanted-trading-cards.md` unless Kyle asks for a different sort.
- Sort rows by `Total` ascending.
- Use `unknown` for unavailable total, price, shipping, or days left.
- Every main-table listing link must go to an individual eBay item page, not a seller page, shop page, category page, or search result page.
- Main-table `Price`, `Shipping`, and `Total` values must come from the opened individual item page or a user-provided screenshot of that exact item page. Do not use search-result, product-page, or web-search snippet prices as final report values.
- Put active auction days remaining in days with one decimal when possible.
- Use `n/a` for buy-it-now listings without a visible end time.
- Do not leave `Days Left` blank. If the listing detail page does not expose enough timing to decide between an auction countdown and `n/a`, move the candidate to skipped/uncertain.
- Recalculate `Total` from the reported `Price` plus `Shipping` after row edits. If the item page price differs from a discovery/source price, use the item page value and note the mismatch only when it explains a correction.
- Use US/domestic shipping in totals when visible. If only international shipping is visible, say so in notes.
- Keep links as listing title markdown links.
- Keep notes compact and evidence-oriented.
- If no active matches are found, write `No active matching listings found.`

## Skipped / Uncertain Candidates

Use this section for candidates that look promising but fail report-row requirements:

- Seller page only, no individual item URL found.
- Search result only, listing detail page unavailable.
- Candidate photo cannot be inspected for an image-sensitive target.
- Days remaining or active/ended status cannot be verified.
- Candidate is sold, completed, or ended.
- Shipping or total price cannot be verified and the item is not otherwise clearly actionable.

Include enough information for Kyle to search manually, but do not present these as active listing rows.

## Omit Ended Auctions

Ended, completed, or sold auctions/listings may be used as similarity evidence, but they must not appear in the active listing tables.

If an item ended or sold during the scan, omit it and optionally add:

```markdown
Skipped ended/sold listings: N
```

## Notes Vocabulary

Prefer these note fragments:

- `exact match`
- `likely match`
- `below retail baseline`
- `above retail baseline`
- `part of a bulk deal`
- `comes with other cards`
- `variant uncertain`
- `condition unclear`
- `shipping variable`
- `domestic shipping used`
- `international shipping shown`
- `seller photo confirms target`
- `listing URL verified`
- `image cues matched`
- `seller-page result only`

## Automation Output

For scheduled runs, write or replace a single latest-report artifact if the runner supports files:

- Suggested path: `os/automation-output/wanted-card-listings/latest.md`.
- Preserve only the current active report unless Kyle asks for historical snapshots.
- Do not store raw eBay HTML, account cookies, seller messages, or unnecessary marketplace data.
