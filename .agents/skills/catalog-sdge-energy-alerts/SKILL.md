---
name: catalog-sdge-energy-alerts
description: Catalog SDGE Energy Use Alert emails from Gmail into a structured flat-file database and regenerate a local time-series dashboard. Use when Kyle asks to process SDGE notices, backfill read or unread SDGE email history, track SDGE electric/gas/solar usage emails, build utility-cost graphs, mark processed SDGE messages read, or run the SDGE energy alert Gmail workflow.
---

# Catalog SDGE Energy Alerts

## Overview

Use this skill to process Kyle's SDGE Energy Use Alert emails, whether Gmail currently marks them read or unread. Search Gmail for messages from `notices@sdge.com` in the `SDGE` label, skip only message IDs already listed in the skill-owned processed-email ledger, extract every obtainable energy, billing, account, and meter-related fact, store the facts in a structured flat-file database, mark successfully processed messages read, and regenerate a local HTML dashboard with time-series charts.

The workflow is harness-neutral. In Codex, use the Gmail connector plus `scripts/sdge_energy_store.py`. In another harness, use equivalent Gmail search/read/label APIs and the same local file contract.

## Storage Contract

Default paths, relative to `/Users/kyle/Documents/AgentOS`:

- Database: `os/data/sdge-energy-alerts/records.jsonl`
- Processed-email ledger: `os/data/sdge-energy-alerts/processed-emails.jsonl`
- Dashboard: `os/reports/sdge-energy-alerts/index.html`

Use one JSON object per SDGE email in the database. Key records by Gmail `message_id`; never duplicate an already processed message. Store all parsed facts even if the dashboard does not chart them yet.

Use `processed-emails.jsonl` as the source of truth for which individual Gmail messages are already handled. Do not infer processed state from Gmail read/unread status. A read Gmail message that is absent from `processed-emails.jsonl` is unprocessed and should be read, parsed, saved, marked in the ledger, and left/marked read. An unread Gmail message already present in `processed-emails.jsonl` should not be parsed again; remove only its `UNREAD` label and verify cleanup.

Recommended record shape:

```json
{
  "message_id": "gmail-message-id",
  "thread_id": "gmail-thread-id",
  "email_date": "2026-07-23T12:34:56-07:00",
  "subject": "Energy Use Alert",
  "from": "notices@sdge.com",
  "alert_date": "2026-07-23",
  "account": {
    "ending": "6283",
    "service_address": "1510 HACIENDA D"
  },
  "billing": {
    "days_left_in_bill_period": 21,
    "as_of_date": "2026-07-23"
  },
  "charges": {
    "total": {
      "to_date": 7,
      "projected_min": 23,
      "projected_max": 38
    },
    "line_items": [
      {
        "name": "SDG&E Gas Charges",
        "to_date": 7,
        "projected_min": 23,
        "projected_max": 38
      }
    ]
  },
  "usage": {
    "electricity": {
      "kwh_to_date": null,
      "kwh_projected_min": null,
      "kwh_projected_max": null
    },
    "gas": {
      "therms_to_date": null,
      "therms_projected_min": null,
      "therms_projected_max": null
    },
    "solar": {
      "returned_to_grid_kwh_to_date": null,
      "returned_to_grid_kwh_projected_min": null,
      "returned_to_grid_kwh_projected_max": null
    }
  },
  "observations": {
    "unparsed_metric_lines": [],
    "notes": []
  }
}
```

Keep private data minimized to SDGE alert facts Kyle explicitly asked to track. Do not store raw full email bodies, screenshots, tracking URLs, cookies, authentication details, or unrelated mailbox content. If a useful metric cannot be normalized yet, place a compact source line in `observations.unparsed_metric_lines`.

## Workflow

1. Find the SDGE label.
   - Use Gmail `list_labels` for `SDGE`.
   - Copy the returned label `id`, not the display name, for label-filtered searches.

2. Load processed message IDs.
   - Read `os/data/sdge-energy-alerts/processed-emails.jsonl` if it exists.
   - If the processed ledger is missing but `records.jsonl` exists from an older skill run, run `scripts/sdge_energy_store.py sync-ledger` once before searching Gmail.
   - Treat only `processed-emails.jsonl` entries as processed. Do not use Gmail read/unread status as the processing ledger.
   - Prefer the helper's local planning commands over ad hoc counting. Use `summary`, `run-plan`, and `diff-ids` to avoid body reads and unnecessary report writes.

3. Search SDGE alert messages, including read mail.
   - First collect cheap Gmail state:
     - `list_labels` for `SDGE`, using `messagesTotal` as `--gmail-total`.
     - `_search_email_ids` for unread matching messages only: query `from:notices@sdge.com -in:spam -in:trash`, label IDs `[SDGE_LABEL_ID, "UNREAD"]`.
   - Run `scripts/sdge_energy_store.py run-plan --gmail-total <messagesTotal> --unread-ids-json '<json-array>'`.
   - If `run-plan` returns `can_skip_all_id_paging: true`, do not page the full mailbox. The local ledger already covers every Gmail label message. Only batch-clean `processed_unread_ids` if any, verify unread search, and regenerate the report only if needed.
   - If `run-plan` returns `page_all_message_ids_then_diff`, page Gmail message IDs using `_search_email_ids` with query `from:notices@sdge.com -in:spam -in:trash` and label IDs `[SDGE_LABEL_ID]`. Do not read bodies yet.
   - After paging IDs, run `scripts/sdge_energy_store.py diff-ids --message-ids-json '<json-array>'`.
   - Read full email details only for `unprocessed_ids` from `diff-ids`. Never read bodies just to confirm already ledgered IDs.

4. Process unrecorded messages one at a time until none remain.
   - Read the first unprocessed message.
   - Confirm it is from `notices@sdge.com` and is an SDGE Energy Use Alert or equivalent SDGE usage/bill projection notice.
   - Extract all obtainable fields from the message text, HTML text, attachments, and inline images that the Gmail connector exposes.
   - Preserve the message ID, thread ID, subject, sender, and email date for traceability.
   - Normalize money as numbers without `$`; normalize projected ranges into `*_min` and `*_max`; normalize dates as ISO `YYYY-MM-DD` when possible.
   - Capture gas therms, electric kWh, solar returned/exported-to-grid kWh, projected bill ranges, line-item charges, account ending, service address, bill-period dates or days remaining, and any other metric-like fact present.
   - If the email contains an image-only table, use the connector's inline image/attachment access when available; otherwise record the limitation in `observations.notes`.

5. Upsert and regenerate the dashboard.
   - Prefer one batched upsert for all newly parsed records: `scripts/sdge_energy_store.py upsert --record-json '<json-array>'`.
   - For large backfills, use `upsert --no-report` while collecting batches, then call `scripts/sdge_energy_store.py report` once after all successful saves.
   - The script updates the JSONL database and `processed-emails.jsonl` idempotently. It regenerates the dashboard unless `--no-report` is passed.
   - Inspect script output for `records_written`, `upserted`, `report_written`, and the dashboard path.
   - Chart only metrics with at least one normalized data point. Omit empty chart groups and empty series entirely; do not render placeholder kWh, therms, solar, or other charts from missing data.
   - Keep chart cards large and readable. Split unrelated metrics into separate chart cards instead of layering several dense series together; for charge data, render separate charts for charge to date, projected low, projected high, and bill amount due.
   - Show readable date ticks on chart x-axes so the time scale is visible without inspecting individual points. Keep ticks sparse enough that adjacent labels do not overlap.
   - Render dashboard charts over a fixed rolling one-year window ending at the latest available chart point. Keep the full historical JSONL records available in the table/database, but avoid compressing multiple years into the visible charts.
   - Prefer pleasant trend-oriented charts over jagged raw plotting: use restrained gridlines, rounded/smoothed line joins through real points, subtle fills, and sparse point markers on dense series.

6. Mark processed messages read.
   - Only after the upsert succeeds, remove the Gmail `UNREAD` label from exact processed `message_id` values if they are unread.
   - Batch cleanup: collect all processed unread IDs from `run-plan` or the final unread search and call one Gmail batch modify with `remove_labels: ["UNREAD"]`.
   - If the connector does not expose a message's current labels, it is still safe to call batch modify with `remove_labels: ["UNREAD"]` for the exact processed message ID.
   - After any read-state mutation, re-run the unread sender/label search and confirm the processed ID is absent.
   - Do not archive, delete, forward, reply, label other messages, or mutate whole threads.

7. Verify completion.
   - If the fast path was valid (`messagesTotal == processed_entries` and no unknown unread IDs), skip the all-status page walk. Verification is the local `summary`, unread search, and `list_labels` unread count.
   - Otherwise, re-run the all-status sender/label ID search and confirm every matching message ID is either present in `processed-emails.jsonl` or intentionally left unprocessed due to a reported blocker.
   - Re-run the unread sender/label search and confirm no processed message IDs remain unread.
   - If messages remain unprocessed because parsing failed or a message is ambiguous, leave those messages eligible for future runs and report the blocker.

8. Report.
   - Final response should include counts only: messages found, newly processed, already-processed messages skipped, processed unread messages marked read, failed/left unprocessed, total database records, processed ledger entries, and the dashboard file path.
   - Do not include account numbers, address, full email text, or private utility details in chat unless Kyle explicitly asks.

## Helper Script

Use the helper from the repo root:

```bash
python3 .agents/skills/catalog-sdge-energy-alerts/scripts/sdge_energy_store.py upsert --record-json '{"message_id":"..."}'
python3 .agents/skills/catalog-sdge-energy-alerts/scripts/sdge_energy_store.py report
python3 .agents/skills/catalog-sdge-energy-alerts/scripts/sdge_energy_store.py summary
python3 .agents/skills/catalog-sdge-energy-alerts/scripts/sdge_energy_store.py processed-ids
python3 .agents/skills/catalog-sdge-energy-alerts/scripts/sdge_energy_store.py run-plan --gmail-total 246 --unread-ids-json '["..."]'
python3 .agents/skills/catalog-sdge-energy-alerts/scripts/sdge_energy_store.py diff-ids --message-ids-json '["..."]'
python3 .agents/skills/catalog-sdge-energy-alerts/scripts/sdge_energy_store.py sync-ledger
```

Useful options:

- `--db-file <path>`: override the JSONL database path.
- `--processed-file <path>`: override the processed-email ledger path.
- `--report-file <path>`: override the dashboard path.
- `--record-json <json>`: upsert one record object or a list of record objects.
- `--no-report`: for `upsert`, update the database and processed ledger without regenerating the dashboard.
- `--gmail-total <count>`: for `run-plan`, pass the `SDGE` Gmail label total from `list_labels`.
- `--unread-ids-json <json>`: for `run-plan`, pass unread matching message IDs from `_search_email_ids`.
- `--message-ids-json <json>`: for `diff-ids`, pass paged Gmail IDs before reading bodies.

For JSON options, pass inline JSON, `@path/to/file.json`, or `-` for stdin. `run-plan` and `diff-ids` are designed to keep normal runs cheap: decide whether a fast path is safe before paging all IDs, and read full emails only for IDs absent from the local ledger.

The dashboard is a single static HTML file styled with shadcn-style CSS variables, cards, tabs, tables, and muted borders. It uses inline JavaScript and SVG charts so it can be opened directly in Codex or Chrome without a dev server. The dashboard should only chart metrics present in the flat-file database; empty metric families are omitted instead of shown as blank or "no data" charts. Prefer a quiet shadcn-like dashboard style with a Darcula dark palette: editor-charcoal background, darker cards, muted blue-gray text, restrained borders, compact metadata, large chart surfaces, minimal legends, visible axes, one-year chart windows, and softened trend lines.

## Safety Rules

- Process only Gmail messages from `notices@sdge.com` inside the SDGE label unless Kyle explicitly widens scope.
- Process both read and unread matching messages when they are absent from `processed-emails.jsonl`.
- Mark only explicitly processed Gmail message IDs read.
- Never delete, archive, forward, send, or broadly label SDGE messages.
- Never store Gmail credentials, cookies, tracking links, unrelated body content, or raw mailbox dumps.
- Leave ambiguous or failed messages unread so a later run can retry them.

## Post-Run Learning

After a meaningful run, capture safe lessons:

- Add durable parsing improvements to this skill only when they are stable across multiple SDGE alert formats.
- Store processed-message state in `processed-emails.jsonl`, not in Gmail read/unread state or chat memory.
- Record recurring parse failures as compact `observations.notes` entries or proposed skill improvements.
- Do not store raw email bodies, full screenshots, secrets, cookies, or unrelated personal data in memory files.
