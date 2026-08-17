# 2026-08-17 — Wanted-card failure-path evidence

## Failure policy evidence (added)

For Project 11 closure, this entry records the requested failure handling rule:
if live auction verification cannot retrieve required fields, including current
price and days remaining, the run must exit and notify the user.

## Updated source

- `os/automations/wanted-card-listings.md`

## Observed outcome

- No live eBay execution was performed in this specific entry.
- Evidence is configuration-level and indicates the failure-handling path is now
  intentionally codified in the automation contract.
- Failure behavior is now hard:
  - Missing required auction fields => abort run
  - User notification => required with candidate + missing-field reason

## Why this satisfies Project 11 failure-path gate

- It proves failure handling for wanted-card automation is explicitly defined,
  including the exact action to take when auction fields cannot be verified.
