# Listing Matching Reference

Use this reference when deciding whether an eBay listing is relevant to a wanted OverPower or Magic: The Gathering card.

## Wanted-Card Fields

Read these fields from `os/context/wanted-trading-cards.md` when available:

- Game: `OverPower` or `Magic: The Gathering`.
- Card name.
- Set, edition, year, printing, language, foil/non-foil, border, rarity, character/team, or other variant constraints.
- Description of the exact card Kyle wants.
- Image path or URL for visual confirmation.
- Ended auction links for similar items.
- Search terms and negative terms.
- Maximum price guidance, if Kyle later adds it.
- Cached retail baseline price, checked date, and source URL.

## Image Matching

When the wanted-card context includes an image, inspect it before searching and record concrete visual cues. For trading cards, useful cues include:

- Exact art or character pose.
- Border, background, and layout.
- Stat boxes, values, colors, icons, and orientation.
- Set, promo, collector, language, foil, or copyright markers visible in the image.
- Differences from similarly named cards.

Use image cues as hard requirements when Kyle says the image distinguishes the target. Do not call a listing an `exact match` unless the listing photo or listing text confirms those cues. If a public search result has a promising title but no listing photo/detail page can be inspected, classify it as skipped/uncertain instead of reporting it as a row.

## Search Strategy

For each active card, run a small set of searches:

- Exact quoted card name plus game name.
- Card name plus set/edition or character/team.
- Broader name without punctuation or subtitle.
- Bulk-lot search terms, such as `lot`, `collection`, `set`, `binder`, `bulk`, `overpower cards`, `mtg lot`, or the set name.
- Negative terms from the context, such as unrelated games, digital-only products, proxies, custom cards, or wrong editions.

Use ended auction links only to extract comparable words, photos, variant cues, and seller/category patterns. Do not report ended listings as opportunities.

## Listing URL Requirements

Report rows must link to individual eBay item pages, normally URLs shaped like `https://www.ebay.com/itm/<item-id>` or an international eBay equivalent with an item id.

Use these only for discovery and never as main table links:

- Seller pages.
- Store pages.
- Category pages.
- Search result pages.
- Saved-search URLs.
- Image-only result links.

If a candidate can only be found on a seller page or search/category result and the individual item page cannot be opened while logged out, omit it from the main table and mention it under skipped/uncertain with the exact limitation.

## Days Remaining

Open each individual item page while logged out and extract the listing format and end timing:

- Auction: convert the visible time remaining or end timestamp to days remaining with one decimal when possible.
- Buy It Now with no visible countdown: use `n/a`.
- Buy It Now with a visible sale/countdown: include days remaining.
- Ended, completed, or sold listing: omit from the report.

Do not leave `Days Left` blank in a main table row. If days remaining cannot be verified, move the candidate to skipped/uncertain.

## Retail Baselines

Use cached baseline fields from `os/context/wanted-trading-cards.md` when present:

- `Retail baseline price`
- `Retail baseline checked`
- `Retail baseline URL`

Do not re-query The Orange King or Brute Force MTG on every run for a card with cached baseline values. Search the retail baseline once when the wanted-card entry is missing those values, then update the wanted-card entry so future scheduled runs can reuse it. For OverPower, only use The Orange King retail site at `theorangeking.com`; do not use The Orange King's eBay account, any seller page, or any eBay listing as the retail baseline. Refresh a cached baseline only when Kyle asks for a refresh or the cached value is clearly invalid.

## Match Classes

Use these classes in notes when helpful:

- `exact match`: title and visible details match the wanted card and required variant.
- `likely match`: title matches but a variant, condition, or image detail is not fully confirmed.
- `bulk deal`: target appears to be included in a lot, binder, set, or collection.
- `comes with other cards`: listing includes the target plus named companion cards.
- `variant uncertain`: printing, foil, language, border, edition, or image does not prove the exact target.
- `weak match`: search hit looks related but lacks enough evidence; omit unless the report has an uncertainty section.

## OverPower Matching

- Verify character/team, special/artifact/aspect/type, expansion, and card text cues when available.
- Treat sealed packs, full sets, starter decks, and bulk lots as relevant only when they plausibly contain the wanted card or include visible/photo evidence.
- Compare retail against The Orange King.

## Magic Matching

- Verify set, collector number, foil treatment, border, language, edition, and condition when these matter.
- Treat foreign-language, proxy, custom, digital, altered, gold-bordered, art-card, oversized, or token listings as separate variants unless Kyle explicitly wants them.
- Compare retail against Brute Force MTG.

## Price Handling

- Total price is item price plus shipping.
- For auctions, use current bid plus shipping as the current total and include days remaining.
- For buy-it-now listings, use BIN price plus shipping and set days remaining to `n/a` unless an end date is visible.
- Prefer US/domestic shipping for Kyle's report. If both domestic and international shipping appear, use domestic shipping. If only international shipping appears, note `international shipping shown`.
- If shipping is not available, leave total as `unknown` and note `shipping variable`.
- Sort known totals ascending, then unknown totals.
