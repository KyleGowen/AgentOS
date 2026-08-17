# SDGE Energy Alerts

## Purpose

Automatically process SDGE Energy Use Alert emails into a structured utility
database and regenerate the local dashboard.

This file is the harness-neutral source of truth. A scheduler, agent runner, or
Codex automation can implement it as long as it follows the contract below.

The SDGE Energy Agent (`os/agents/sdge-energy-agent.md`) is the designated
agent identity for this workflow. Its Codex profile is only a launcher; this
policy remains authoritative for schedule, scope, and permitted mutations.

## Schedule

Run once weekly on Monday at 7:00 AM Pacific time, observing PST/PDT
(`America/Los_Angeles`).

## Input Files

| File | Purpose | Status |
|---|---|---|
| `.agents/skills/catalog-sdge-energy-alerts/SKILL.md` | Codex skill that performs the Gmail processing, storage updates, read-state cleanup, and dashboard generation. | Active |
| `os/data/sdge-energy-alerts/records.jsonl` | Flat-file utility record database. | Active |
| `os/data/sdge-energy-alerts/processed-emails.jsonl` | Source of truth for processed Gmail message IDs. | Active |
| `os/reports/sdge-energy-alerts/index.html` | Local dashboard generated from stored records. | Active |

## Runner Contract

1. Read `.agents/skills/catalog-sdge-energy-alerts/SKILL.md` before acting.
2. Use the Gmail connector to process messages from `notices@sdge.com` in the
   `SDGE` label only.
3. Treat `os/data/sdge-energy-alerts/processed-emails.jsonl` as the only
   processed-message source of truth. Do not infer processing from Gmail read
   state.
4. Process both read and unread SDGE-label messages that are absent from the
   processed ledger.
5. Use the skill helper's `summary`, `run-plan`, and `diff-ids` commands to
   avoid unnecessary Gmail body reads.
6. Read full email bodies only for message IDs absent from the processed ledger.
7. When the skill parser has gained new usage fields, use `usage-backfill-ids`
   to find already-processed usage-report IDs missing normalized meter metrics,
   then re-read only those IDs for enrichment.
8. Save all parsed facts to the flat-file database and regenerate the dashboard
   according to the skill's storage and charting rules.
9. Mark only successfully processed unread message IDs read, then verify unread
   cleanup.
10. Leave ambiguous or failed messages eligible for a future run and report the
   blocker compactly.

## Safety Rules

- Never process messages outside the `SDGE` Gmail label and
  `notices@sdge.com` sender scope unless Kyle explicitly widens the automation.
- Never delete, archive, forward, reply to, or broadly relabel SDGE messages.
- Never store Gmail credentials, cookies, tracking links, raw full email bodies,
  screenshots, or unrelated mailbox content.
- Keep chat output to counts, blockers, and the dashboard path. Do not include
  account numbers, service address, full email text, or private utility details
  unless Kyle explicitly asks.

## Output

Each scheduled run should report:

| Count | Meaning |
|---|---|
| Messages found | Matching SDGE-label sender messages in Gmail. |
| Newly processed | Messages parsed and written during this run. |
| Already processed | Ledgered messages skipped. |
| Marked read | Successfully processed unread messages cleaned up. |
| Left unprocessed | Ambiguous or failed messages still eligible for retry. |
| Database records | Total stored utility records. |
| Processed ledger entries | Total processed message IDs. |

Include the dashboard path: `os/reports/sdge-energy-alerts/index.html`.

## Implementation Notes

- Codex implementation: use `.agents/skills/catalog-sdge-energy-alerts/`.
- Current Codex automation ID: `sdge-energy-alerts`.
- Codex cron schedule is active for Monday 7:00 AM local/Pacific time.
- Non-Codex implementation: use the same runner contract with equivalent Gmail
  search/read/label APIs.
