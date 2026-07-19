---
name: find-card-listings
description: "Find eBay listings for wanted OverPower and Magic: The Gathering cards without bidding or using a logged-in eBay account. Use when Kyle asks to scan for wanted trading cards, monitor eBay card auctions, compare listing prices to The Orange King or Brute Force MTG retail baselines, produce a per-card listing report, or run the wanted-card auction automation."
---

# Find Card Listings

## Overview

Use this skill to run the read-only wanted-card marketplace scan. The skill reads Kyle's wanted-card context, searches public eBay listings while logged out, compares candidates against the appropriate retail baseline, and reports only active listings sorted by total price.

When Kyle asks to add a wanted card, or when a wanted-card entry is changed from `Draft` to `Active`, first update `os/context/wanted-trading-cards.md`, then immediately run this scan for all active wanted cards. The newly added card triggers a full-list refresh; it does not narrow the scope to one card unless Kyle explicitly asks for a single-card run.

This skill never bids, buys, messages sellers, watches items, or uses a logged-in eBay session.

## Required Inputs

- Wanted-card context: default to `os/context/wanted-trading-cards.md`.
- Automation policy: default to `os/automations/wanted-card-listings.md` when running as a scheduled task or add-card-triggered task.
- Optional one-off card name, description, image path, retail product URL, or ended auction links from the user. Add durable targets to the wanted-card context before relying on them in scheduled runs.

## References

- Read `references/matching.md` before classifying listings, bulk lots, variants, or similar items.
- Read `references/reporting.md` before producing the final table or updating an automation output artifact.

## Workflow

1. Read the wanted-card context.
   - Process only rows or sections marked `Active`.
   - If this run follows a new wanted-card addition or a `Draft` to `Active` change, process every active card in the file, not only the changed card.
   - Preserve ended auction links as matching evidence; do not include ended auctions in the output.
   - Preserve supplied retail product URLs as seed/reference evidence, especially The Orange King product URLs for OverPower cards. Normalize tracking URLs by stripping query parameters such as `_pos`, `_sid`, and `_ss` before saving canonical baseline URLs.
   - If image evidence is available, inspect the image before searching and extract concrete visual cues such as art, border, stat bars, set marks, language, foil treatment, and distinctive layout. Use those cues as required matching evidence when the user says the image distinguishes the wanted card.

2. Search eBay publicly.
   - Use a logged-out browser context, public search pages, public APIs, or web search results.
   - Do not use Kyle's eBay account, cookies, watch list, saved searches, seller messages, cart, bidding pages, or purchase flows.
   - Search both precise names and broader terms from the wanted-card context so bulk deals and listings with companion cards can surface.
   - Promote only individual listing URLs, normally `https://www.ebay.com/itm/<item-id>...`, to report rows. Seller pages, category pages, search result pages, and generic shop pages are discovery sources only.

3. Collect active listing facts.
   - Open each candidate listing detail page while logged out before reporting it.
   - Capture title, listing URL, current bid or buy-it-now price, shipping, total price, listing format, seller-visible condition text, auction end time, and days remaining.
   - Treat search-result snippets, eBay product pages, item-card tiles, and web-search prices as discovery hints only. Do not copy those prices into the main report unless the same price and shipping are verified on the individual listing detail page or in a user-provided screenshot of that exact item page.
   - Exclude ended, completed, and sold listings from the report even when they match the card.
   - If days remaining or listing URL cannot be verified from an item detail page, omit the candidate from the main table and mention it under skipped/uncertain.
   - Use US/domestic shipping when visible. Do not use international shipping totals for Kyle's report when a US shipping price is visible or supplied by the item page/search result. If only international shipping is visible, mark the shipping basis in notes.
   - When shipping is missing or variable, mark it explicitly and sort after listings with known total price unless the listing is otherwise clearly relevant.

4. Compare against retail baselines.
   - Use cached `Retail baseline price`, `Retail baseline checked`, and `Retail baseline URL` values from the wanted-card context when present.
   - Do not re-check retail baseline sites on every run for known values.
   - If a wanted card has no cached baseline, check once and update the wanted-card context. For OverPower cards, use only The Orange King retail site at `https://theorangeking.com/`, not The Orange King's eBay account or any other eBay listing; for Magic: The Gathering cards, use Brute Force MTG at `https://www.bruteforcemtg.com/`.
   - For OverPower cards supplied with a The Orange King product URL, prefer that product page over a broad retail search. Read the canonical product URL, title, price, availability, and product image from the page or embedded Shopify product JSON, then cache the canonical URL and price.
   - For Brute Force MTG, search the public CrystalCommerce product search directly with `https://www.bruteforcemtg.com/products/search?q=<url-encoded-card-name>&c=1`. If a plain fetch returns `410 Gone`, retry with a normal browser user-agent before declaring the baseline missing.
   - Parse exact product rows only. Ignore similarly named cards. If the wanted entry accepts any official printing, use the lowest exact official printing price as the baseline and mention notable variant prices in notes. If Brute Force marks the exact product `Out of stock`, the visible product price can still be cached as the retail baseline, with the stock status noted.
   - Refresh a cached retail baseline only when Kyle asks, the cached value is clearly missing/invalid, or the wanted-card entry says to refresh it.

5. Classify matches.
   - Distinguish exact card matches, likely variants, bulk lots containing the target, and weak/ambiguous matches.
   - For visually sensitive cards, compare listing photos or explicit title/detail evidence against the wanted-card image cues before calling a match exact or likely.
   - For OverPower IQ Character cards, treat the card name, IQ Character label, stat values, art/background, and any visible card text as hard matching constraints. Exclude regular/original character cards, PowerSurge cards, specials, power cards, teamworks, and alternate named IQ variants unless Kyle explicitly asks for those variants.
   - Prefer precision over volume. Skip weak matches unless the report clearly marks why they may be relevant.
   - Add notes such as `part of a bulk deal`, `comes with other cards`, `variant uncertain`, `shipping variable`, or `below retail baseline`.

6. Report.
   - Lead with the compact cross-card opportunity chart defined in `references/reporting.md`; include every active card and bold only verified combined listing prices strictly below the cached retail baseline.
   - Group wanted cards by their `Game` field before listing individual cards. Use second-level headings for games such as `## Magic: The Gathering` and `## OverPower`, then third-level headings for each card under the matching game.
   - Produce one table per wanted card.
   - Sort rows by total price plus shipping ascending.
   - Before finalizing, re-check that every known total equals the displayed item-page price plus displayed item-page shipping. If the item page disagrees with discovery/search pricing, use the item-page values and note the correction when useful.
   - Include days remaining for every row. Use a numeric value for auctions, `n/a` for buy-it-now listings only after verifying the listing detail page has no visible end countdown, and `unknown` only in skipped/uncertain notes.
   - Keep ended, completed, and sold listings out of the tables.
   - Include a compact skipped/uncertain section only when it helps Kyle understand why a likely-looking listing was omitted.

## Safety Rules

- Never bid, buy, make offers, add to cart, message sellers, save searches, watch items, or sign in to eBay.
- Never use a logged-in eBay account or browser profile.
- Never rely on ended, completed, or sold listings as current opportunities; use them only as similarity evidence.
- Do not scrape or store more marketplace data than needed for the current report.
- If a listing might require account access to inspect safely, skip it and note the limitation.

## Output Shape

Use the table shape from `references/reporting.md`. At minimum include:

- Card name and baseline summary.
- Game-group headings, with each wanted card nested under the matching game.
- Listing rows with title, total price, price, shipping, days remaining, link, and notes.
- Run timestamp and whether eBay/retail baseline access was complete.
