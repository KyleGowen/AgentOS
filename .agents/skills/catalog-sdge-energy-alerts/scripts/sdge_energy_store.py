#!/usr/bin/env python3
"""Store SDGE energy alert records and generate a local dashboard."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


DEFAULT_DB_FILE = Path("os/data/sdge-energy-alerts/records.jsonl")
DEFAULT_PROCESSED_FILE = Path("os/data/sdge-energy-alerts/processed-emails.jsonl")
DEFAULT_REPORT_FILE = Path("os/reports/sdge-energy-alerts/index.html")


def coerce_money(value: Any) -> Any:
    if value is None or isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        cleaned = value.strip().replace("$", "").replace(",", "")
        if not cleaned:
            return None
        try:
            return float(cleaned) if "." in cleaned else int(cleaned)
        except ValueError:
            return value
    return value


def coerce_number(value: Any) -> Any:
    if value is None or isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        cleaned = value.strip().replace(",", "")
        if not cleaned:
            return None
        try:
            return float(cleaned) if "." in cleaned else int(cleaned)
        except ValueError:
            return value
    return value


def get_path(record: dict[str, Any], path: str) -> Any:
    current: Any = record
    for part in path.split("."):
        if not isinstance(current, dict):
            return None
        current = current.get(part)
    return current


def set_path(record: dict[str, Any], path: str, value: Any) -> None:
    current = record
    parts = path.split(".")
    for part in parts[:-1]:
        current = current.setdefault(part, {})
    current[parts[-1]] = value


def normalize_iso_date(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return None
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
            return text
        for fmt in ("%b %d, %Y", "%B %d, %Y", "%m/%d/%Y", "%Y-%m-%dT%H:%M:%S%z"):
            try:
                return dt.datetime.strptime(text, fmt).date().isoformat()
            except ValueError:
                pass
        try:
            return dt.datetime.fromisoformat(text.replace("Z", "+00:00")).date().isoformat()
        except ValueError:
            return text
    return value


def infer_from_source_text(record: dict[str, Any]) -> None:
    text = record.get("source_text")
    if not isinstance(text, str) or not text.strip():
        return

    compact = re.sub(r"[ \t]+", " ", text)
    compact = re.sub(r"\s*\n\s*", "\n", compact)

    money_pattern = r"(-?\$?[\d,.]+|\$-?[\d,.]+)"

    account = re.search(
        r"Account Ending:\s*(\d+)\s+(.+?)(?=\s+(?:Account Ending:|Hi\b|Energy Use Alert|Statement Date:|How (?:you are|you're)|$))",
        compact,
        re.I,
    )
    if account:
        set_path(record, "account.ending", record.get("account", {}).get("ending") or account.group(1))
        if account.group(2):
            set_path(
                record,
                "account.service_address",
                record.get("account", {}).get("service_address") or account.group(2).strip(),
            )

    status = re.search(
        rf"How (?:you are|you're) doing so far:?\s*{money_pattern}\s+as of\s+([A-Za-z]{{3,9}}\s+\d{{1,2}},\s+\d{{4}})",
        compact,
        re.I,
    )
    if not status:
        status = re.search(
            rf"As of\s+([A-Za-z]{{3,9}}\s+\d{{1,2}},\s+\d{{4}}).*?(?:(?:Est\.\s*)?Bill|SDG&E Charges)\s+to date\s+{money_pattern}",
            compact,
            re.I,
        )
        if status:
            status = (status.group(2), status.group(1))
    if status:
        if isinstance(status, tuple):
            to_date_value, date_text = status
        else:
            to_date_value, date_text = status.group(1), status.group(2)
        set_path(record, "charges.total.to_date", coerce_money(to_date_value))
        alert_date = normalize_iso_date(date_text)
        set_path(record, "alert_date", record.get("alert_date") or alert_date)
        set_path(record, "billing.as_of_date", record.get("billing", {}).get("as_of_date") or alert_date)

    days_left = re.search(r"(?:You have\s+)?(\d+)\s+days?\s+left\s+in\s+(?:the\s+)?bill\s+period", compact, re.I)
    if days_left:
        set_path(record, "billing.days_left_in_bill_period", coerce_number(days_left.group(1)))

    projected = re.search(rf"PROJECTED BILL\s+{money_pattern}\s*(?:TO|-)\s*{money_pattern}", compact, re.I)
    if projected:
        set_path(record, "charges.total.projected_min", coerce_money(projected.group(1)))
        set_path(record, "charges.total.projected_max", coerce_money(projected.group(2)))

    statement_date = re.search(r"Statement Date:\s*([A-Za-z]{3,9}\s+\d{1,2},\s+\d{4})", compact, re.I)
    if statement_date:
        date_value = normalize_iso_date(statement_date.group(1))
        set_path(record, "billing.statement_date", record.get("billing", {}).get("statement_date") or date_value)
        set_path(record, "alert_date", record.get("alert_date") or date_value)

    amount_due = re.search(rf"Amount Due\s+{money_pattern}", compact, re.I)
    if not amount_due:
        amount_due = re.search(
            rf"Statement Date:\s*[A-Za-z]{{3,9}}\s+\d{{1,2}},\s+\d{{4}}\s+{money_pattern}",
            compact,
            re.I,
        )
    if amount_due:
        set_path(record, "charges.bill.amount_due", coerce_money(amount_due.group(1)))

    line_items: list[dict[str, Any]] = []
    for line in compact.splitlines():
        item_match = re.search(rf"^(.+?)\s+{money_pattern}\s+{money_pattern}\s+to\s+{money_pattern}\s*$", line, re.I)
        if not item_match:
            continue
        name = item_match.group(1).strip()
        item = {
            "name": name,
            "to_date": coerce_money(item_match.group(2)),
            "projected_min": coerce_money(item_match.group(3)),
            "projected_max": coerce_money(item_match.group(4)),
        }
        if name.lower() == "total":
            set_path(record, "charges.total.to_date", item["to_date"])
            set_path(record, "charges.total.projected_min", item["projected_min"])
            set_path(record, "charges.total.projected_max", item["projected_max"])
        else:
            line_items.append(item)
    if line_items and not get_path(record, "charges.line_items"):
        set_path(record, "charges.line_items", line_items)

    kwh = re.search(r"([\d,.]+)\s*kWh", compact, re.I)
    if kwh:
        set_path(record, "usage.electricity.kwh_to_date", coerce_number(kwh.group(1)))

    therms = re.search(r"([\d,.]+)\s*therms?", compact, re.I)
    if therms:
        set_path(record, "usage.gas.therms_to_date", coerce_number(therms.group(1)))

    solar = re.search(r"(?:returned|sent|exported)\s+[^.\n]*?grid[^.\n]*?([\d,.]+)\s*kWh", compact, re.I)
    if solar:
        set_path(record, "usage.solar.returned_to_grid_kwh_to_date", coerce_number(solar.group(1)))


def normalize_record(record: dict[str, Any]) -> dict[str, Any]:
    if "message_id" not in record or not str(record["message_id"]).strip():
        raise ValueError("record is missing required message_id")

    normalized = dict(record)
    infer_from_source_text(normalized)

    normalized["message_id"] = str(normalized["message_id"])
    if normalized.get("thread_id") is not None:
        normalized["thread_id"] = str(normalized["thread_id"])

    for path in (
        "alert_date",
        "billing.as_of_date",
        "billing.bill_period_start",
        "billing.bill_period_end",
    ):
        value = get_path(normalized, path)
        if value is not None:
            set_path(normalized, path, normalize_iso_date(value))

    for path in (
        "charges.total.to_date",
        "charges.total.projected_min",
        "charges.total.projected_max",
        "charges.bill.amount_due",
    ):
        value = get_path(normalized, path)
        if value is not None:
            set_path(normalized, path, coerce_money(value))

    for path in (
        "billing.days_left_in_bill_period",
        "usage.electricity.kwh_to_date",
        "usage.electricity.kwh_projected_min",
        "usage.electricity.kwh_projected_max",
        "usage.gas.therms_to_date",
        "usage.gas.therms_projected_min",
        "usage.gas.therms_projected_max",
        "usage.solar.returned_to_grid_kwh_to_date",
        "usage.solar.returned_to_grid_kwh_projected_min",
        "usage.solar.returned_to_grid_kwh_projected_max",
    ):
        value = get_path(normalized, path)
        if value is not None:
            set_path(normalized, path, coerce_number(value))

    line_items = get_path(normalized, "charges.line_items")
    if isinstance(line_items, list):
        for item in line_items:
            if isinstance(item, dict):
                for key in ("to_date", "projected_min", "projected_max"):
                    if key in item:
                        item[key] = coerce_money(item[key])

    normalized.pop("source_text", None)
    normalized.setdefault("observations", {})
    normalized["processed_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
    return normalized


def load_records(db_file: Path) -> list[dict[str, Any]]:
    if not db_file.exists():
        return []
    records: list[dict[str, Any]] = []
    with db_file.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                record = json.loads(text)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{db_file}:{line_number}: invalid JSONL record: {exc}") from exc
            if isinstance(record, dict):
                records.append(record)
    return records


def load_processed_entries(processed_file: Path) -> list[dict[str, Any]]:
    if not processed_file.exists():
        return []
    entries: list[dict[str, Any]] = []
    with processed_file.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                entry = json.loads(text)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{processed_file}:{line_number}: invalid JSONL entry: {exc}") from exc
            if isinstance(entry, dict) and entry.get("message_id"):
                entries.append(entry)
    return entries


def processed_sort_key(entry: dict[str, Any]) -> tuple[str, str]:
    date_value = entry.get("email_date") or entry.get("alert_date") or entry.get("processed_at") or ""
    return (str(date_value), str(entry.get("message_id", "")))


def processed_entry_from_record(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "message_id": str(record.get("message_id")),
        "thread_id": record.get("thread_id"),
        "email_date": record.get("email_date"),
        "subject": record.get("subject"),
        "from": record.get("from"),
        "alert_date": record.get("alert_date"),
        "processed_at": record.get("processed_at") or dt.datetime.now(dt.timezone.utc).isoformat(),
        "status": "processed",
    }


def write_processed_entries(processed_file: Path, entries: list[dict[str, Any]]) -> None:
    processed_file.parent.mkdir(parents=True, exist_ok=True)
    by_id = {str(entry.get("message_id")): entry for entry in entries if entry.get("message_id")}
    with processed_file.open("w", encoding="utf-8") as handle:
        for entry in sorted(by_id.values(), key=processed_sort_key):
            handle.write(json.dumps(entry, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
            handle.write("\n")


def sync_processed_ledger(processed_file: Path, records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    entries = {str(entry.get("message_id")): entry for entry in load_processed_entries(processed_file)}
    for record in records:
        message_id = record.get("message_id")
        if not message_id:
            continue
        entries[str(message_id)] = {**entries.get(str(message_id), {}), **processed_entry_from_record(record)}
    merged = list(entries.values())
    write_processed_entries(processed_file, merged)
    return sorted(merged, key=processed_sort_key)


def record_sort_key(record: dict[str, Any]) -> tuple[str, str]:
    date_value = record.get("alert_date") or record.get("email_date") or ""
    return (str(date_value), str(record.get("message_id", "")))


def write_records(db_file: Path, records: list[dict[str, Any]]) -> None:
    db_file.parent.mkdir(parents=True, exist_ok=True)
    records = sorted(records, key=record_sort_key)
    with db_file.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
            handle.write("\n")


def upsert_records(db_file: Path, processed_file: Path, incoming: list[dict[str, Any]]) -> list[dict[str, Any]]:
    existing = {str(record.get("message_id")): record for record in load_records(db_file)}
    for raw in incoming:
        record = normalize_record(raw)
        existing[record["message_id"]] = {**existing.get(record["message_id"], {}), **record}
    records = list(existing.values())
    write_records(db_file, records)
    records = sorted(records, key=record_sort_key)
    sync_processed_ledger(processed_file, records)
    return records


def chart_points(records: list[dict[str, Any]], path: str) -> list[dict[str, Any]]:
    points: list[dict[str, Any]] = []
    for record in records:
        value = get_path(record, path)
        if isinstance(value, (int, float)):
            points.append(
                {
                    "date": record.get("alert_date") or str(record.get("email_date", ""))[:10],
                    "value": value,
                    "message_id": record.get("message_id"),
                }
            )
    return points


def parse_point_date(point: dict[str, Any]) -> dt.date | None:
    date_value = point.get("date")
    if not isinstance(date_value, str) or not date_value:
        return None
    try:
        return dt.date.fromisoformat(date_value[:10])
    except ValueError:
        return None


def subtract_one_year(value: dt.date) -> dt.date:
    try:
        return value.replace(year=value.year - 1)
    except ValueError:
        return value - dt.timedelta(days=365)


def build_dashboard_html(records: list[dict[str, Any]], db_file: Path) -> str:
    generated_at = dt.datetime.now(dt.timezone.utc).isoformat()
    chart_specs = [
        {
            "id": "charge-to-date",
            "title": "Charge To Date",
            "description": "Estimated charges at the time each usage alert was sent.",
            "series": [
                {"label": "To date", "unit": "$", "points": chart_points(records, "charges.total.to_date")},
            ],
        },
        {
            "id": "projected-low",
            "title": "Projected Bill Low",
            "description": "Lower end of the projected bill range.",
            "series": [
                {"label": "Projected low", "unit": "$", "points": chart_points(records, "charges.total.projected_min")},
            ],
        },
        {
            "id": "projected-high",
            "title": "Projected Bill High",
            "description": "Upper end of the projected bill range.",
            "series": [
                {"label": "Projected high", "unit": "$", "points": chart_points(records, "charges.total.projected_max")},
            ],
        },
        {
            "id": "bill-amount-due",
            "title": "Bill Amount Due",
            "description": "Final bill amount captured from bill-summary emails.",
            "series": [
                {"label": "Bill amount due", "unit": "$", "points": chart_points(records, "charges.bill.amount_due")},
            ],
        },
        {
            "id": "electricity",
            "title": "Electricity",
            "description": "Electric usage tracked from SDGE alerts.",
            "series": [
                {"label": "kWh to date", "unit": " kWh", "points": chart_points(records, "usage.electricity.kwh_to_date")},
                {
                    "label": "Projected low",
                    "unit": " kWh",
                    "points": chart_points(records, "usage.electricity.kwh_projected_min"),
                },
                {
                    "label": "Projected high",
                    "unit": " kWh",
                    "points": chart_points(records, "usage.electricity.kwh_projected_max"),
                },
            ],
        },
        {
            "id": "gas",
            "title": "Gas",
            "description": "Gas therms tracked from SDGE alerts.",
            "series": [
                {"label": "Therms to date", "unit": " therms", "points": chart_points(records, "usage.gas.therms_to_date")},
                {
                    "label": "Projected low",
                    "unit": " therms",
                    "points": chart_points(records, "usage.gas.therms_projected_min"),
                },
                {
                    "label": "Projected high",
                    "unit": " therms",
                    "points": chart_points(records, "usage.gas.therms_projected_max"),
                },
            ],
        },
        {
            "id": "solar",
            "title": "Solar Export",
            "description": "Energy returned or exported to the grid.",
            "series": [
                {
                    "label": "Returned to grid",
                    "unit": " kWh",
                    "points": chart_points(records, "usage.solar.returned_to_grid_kwh_to_date"),
                },
                {
                    "label": "Projected low",
                    "unit": " kWh",
                    "points": chart_points(records, "usage.solar.returned_to_grid_kwh_projected_min"),
                },
                {
                    "label": "Projected high",
                    "unit": " kWh",
                    "points": chart_points(records, "usage.solar.returned_to_grid_kwh_projected_max"),
                },
            ],
        },
        {
            "id": "bill-period",
            "title": "Bill Period",
            "description": "Days remaining when each alert was sent.",
            "series": [
                {
                    "label": "Days left",
                    "unit": " days",
                    "points": chart_points(records, "billing.days_left_in_bill_period"),
                }
            ],
        },
    ]
    all_chart_points = [
        point
        for chart in chart_specs
        for series in chart["series"]
        for point in series["points"]
    ]
    dated_points = [date_value for point in all_chart_points if (date_value := parse_point_date(point))]
    chart_window_end = max(dated_points) if dated_points else dt.datetime.now(dt.timezone.utc).date()
    chart_window_start = subtract_one_year(chart_window_end)

    charts = []
    for chart in chart_specs:
        series = []
        for entry in chart["series"]:
            points = [
                point
                for point in entry["points"]
                if (date_value := parse_point_date(point)) and chart_window_start <= date_value <= chart_window_end
            ]
            if points:
                series.append({**entry, "points": points})
        if series:
            charts.append({**chart, "series": series})

    dashboard_data = {
        "generated_at": generated_at,
        "db_file": str(db_file),
        "records": records,
        "chart_window": {
            "start": chart_window_start.isoformat(),
            "end": chart_window_end.isoformat(),
        },
        "charts": charts,
    }

    data_json = json.dumps(dashboard_data, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e")
    escaped_db_file = html.escape(str(db_file))
    record_count = len(records)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>SDGE Energy Alerts</title>
  <style>
    :root {{
      color-scheme: dark;
      --background: 220 3% 17%;
      --foreground: 211 23% 72%;
      --muted: 210 4% 24%;
      --muted-foreground: 214 12% 58%;
      --border: 210 4% 30%;
      --input: 210 4% 30%;
      --card: 210 4% 22%;
      --card-foreground: 211 23% 76%;
      --popover: 210 4% 22%;
      --popover-foreground: 211 23% 76%;
      --primary: 204 37% 57%;
      --primary-foreground: 220 3% 14%;
      --secondary: 210 4% 26%;
      --secondary-foreground: 211 23% 76%;
      --accent: 210 4% 28%;
      --accent-foreground: 211 23% 76%;
      --radius: 0.5rem;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: hsl(var(--background));
      color: hsl(var(--foreground));
    }}
    .page {{
      max-width: 1380px;
      margin: 0 auto;
      padding: 40px 24px 64px;
    }}
    header {{
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 24px;
    }}
    h1, h2, h3, p {{ margin: 0; }}
    h1 {{ font-size: 32px; line-height: 1.2; letter-spacing: 0; font-weight: 650; }}
    h2 {{ font-size: 18px; line-height: 1.4; font-weight: 650; }}
    .muted {{ color: hsl(var(--muted-foreground)); }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 16px;
      margin-bottom: 20px;
    }}
    .card {{
      border: 1px solid hsl(var(--border));
      border-radius: var(--radius);
      background: hsl(var(--card));
      color: hsl(var(--card-foreground));
      padding: 20px;
      box-shadow: 0 1px 2px rgb(0 0 0 / 0.18);
    }}
    .metric {{
      font-size: 24px;
      font-weight: 650;
      margin-top: 6px;
    }}
    .charts {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 18px;
    }}
    .chart-card {{
      min-height: 500px;
    }}
    .chart-head {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 18px;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      border-radius: 999px;
      border: 1px solid hsl(var(--border));
      background: hsl(var(--secondary));
      padding: 3px 10px;
      color: hsl(var(--muted-foreground));
      font-size: 12px;
      white-space: nowrap;
    }}
    .chart {{
      width: 100%;
      height: 410px;
      border: 1px solid hsl(var(--border));
      border-radius: var(--radius);
      background: hsl(220 3% 18%);
    }}
    .legend {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 12px;
      color: hsl(var(--muted-foreground));
      font-size: 12px;
    }}
    .legend-item {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .swatch {{
      width: 10px;
      height: 10px;
      border-radius: 999px;
      display: inline-block;
    }}
    .table-card {{
      margin-top: 18px;
      overflow-x: auto;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
    }}
    th, td {{
      border-bottom: 1px solid hsl(var(--border));
      padding: 12px 10px;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      color: hsl(var(--muted-foreground));
      font-weight: 600;
      background: hsl(var(--muted));
    }}
    code {{
      border-radius: 4px;
      background: hsl(220 3% 17%);
      color: hsl(38 100% 72%);
      padding: 2px 4px;
      font-size: 12px;
    }}
    @media (max-width: 860px) {{
      header {{ align-items: flex-start; flex-direction: column; }}
      .grid, .charts {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <header>
      <div>
        <p class="muted">SDGE Energy Use Alerts</p>
        <h1>Energy Time Series</h1>
      </div>
      <p class="muted">Generated <span id="generated"></span></p>
    </header>

    <section class="grid" aria-label="summary metrics">
      <div class="card"><p class="muted">Records</p><p class="metric">{record_count}</p></div>
      <div class="card"><p class="muted">Latest alert</p><p class="metric" id="latest-alert">--</p></div>
      <div class="card"><p class="muted">Database</p><p><code>{escaped_db_file}</code></p></div>
    </section>

    <main class="charts" id="charts"></main>

    <section class="card table-card">
      <div class="chart-head">
        <div>
          <h2>Records</h2>
          <p class="muted">Compact normalized values from each processed SDGE email.</p>
        </div>
      </div>
      <table>
        <thead>
          <tr id="records-head"></tr>
        </thead>
        <tbody id="records-body"></tbody>
      </table>
    </section>
  </div>
  <script id="dashboard-data" type="application/json">{data_json}</script>
  <script>
    const data = JSON.parse(document.getElementById("dashboard-data").textContent);
    const colors = ["#6897bb", "#6a8759", "#cc7832", "#9876aa", "#ffc66d", "#bc3f3c"];
    const chartColors = {{
      "charge-to-date": "#6897bb",
      "projected-low": "#6a8759",
      "projected-high": "#cc7832",
      "bill-amount-due": "#9876aa",
      "bill-period": "#ffc66d",
    }};
    document.getElementById("generated").textContent = new Date(data.generated_at).toLocaleString();

    const latest = [...data.records].reverse().find((record) => record.alert_date || record.email_date);
    document.getElementById("latest-alert").textContent = latest ? (latest.alert_date || String(latest.email_date).slice(0, 10)) : "--";

    function valueAt(record, path) {{
      return path.split(".").reduce((current, part) => current && current[part], record);
    }}

    function formatValue(value, unit) {{
      if (value === null || value === undefined || value === "") return "--";
      const number = Number(value);
      const digits = Number.isInteger(number) ? 0 : 2;
      const formatted = number.toLocaleString(undefined, {{ maximumFractionDigits: digits }});
      if (unit === "$") return "$" + formatted;
      return formatted + (unit || "");
    }}

    function formatAxisValue(value, unit) {{
      const formatted = Number(value).toLocaleString(undefined, {{ maximumFractionDigits: 0 }});
      if (unit === "$") return "$" + formatted;
      return formatted + (unit || "");
    }}

    function formatAxisDate(value) {{
      return new Date(value).toLocaleDateString(undefined, {{ month: "short", year: "2-digit" }});
    }}

    function dateTicks(min, max, count) {{
      if (min === max) return [min];
      return Array.from({{ length: count }}, (_, index) => min + ((max - min) * index) / (count - 1));
    }}

    function yearTicks(min, max) {{
      if (min === max) return [min];
      return dateTicks(min, max, 5);
    }}

    function valueTicks(min, max, count) {{
      if (min === max) return [min];
      return Array.from({{ length: count }}, (_, index) => min + ((max - min) * index) / (count - 1));
    }}

    function niceDomain(min, max) {{
      if (min === max) {{
        const pad = Math.max(Math.abs(min) * 0.2, 1);
        return [min - pad, max + pad];
      }}
      const span = max - min;
      const paddedMin = min - span * 0.12;
      const paddedMax = max + span * 0.12;
      const niceStep = Math.pow(10, Math.floor(Math.log10(Math.max(paddedMax - paddedMin, 1))));
      const step = niceStep / 2;
      return [Math.floor(paddedMin / step) * step, Math.ceil(paddedMax / step) * step];
    }}

    function smoothPath(points, xScale, yScale) {{
      if (points.length === 1) {{
        const x = xScale(points[0].dateValue).toFixed(2);
        const y = yScale(points[0].value).toFixed(2);
        return `M ${{x}} ${{y}}`;
      }}
      const mapped = points.map((point) => ({{ x: xScale(point.dateValue), y: yScale(point.value) }}));
      const commands = [`M ${{mapped[0].x.toFixed(2)}} ${{mapped[0].y.toFixed(2)}}`];
      for (let index = 0; index < mapped.length - 1; index += 1) {{
        const p0 = mapped[Math.max(0, index - 1)];
        const p1 = mapped[index];
        const p2 = mapped[index + 1];
        const p3 = mapped[Math.min(mapped.length - 1, index + 2)];
        const tension = 0.18;
        const cp1x = p1.x + (p2.x - p0.x) * tension;
        const cp1y = p1.y + (p2.y - p0.y) * tension;
        const cp2x = p2.x - (p3.x - p1.x) * tension;
        const cp2y = p2.y - (p3.y - p1.y) * tension;
        commands.push(`C ${{cp1x.toFixed(2)}} ${{cp1y.toFixed(2)}}, ${{cp2x.toFixed(2)}} ${{cp2y.toFixed(2)}}, ${{p2.x.toFixed(2)}} ${{p2.y.toFixed(2)}}`);
      }}
      return commands.join(" ");
    }}

    function makeChart(chart) {{
      const series = chart.series.filter((entry) => entry.points.length > 0);
      if (series.length === 0) return null;
      const allPoints = series.flatMap((entry) => entry.points.map((point) => ({{ ...point, dateValue: Date.parse(point.date) || 0 }})));
      const minX = Date.parse(data.chart_window.start);
      const maxX = Date.parse(data.chart_window.end);
      const rawMinY = Math.min(...allPoints.map((point) => point.value));
      const rawMaxY = Math.max(...allPoints.map((point) => point.value));
      const [minY, maxY] = niceDomain(rawMinY, rawMaxY);
      const dateRange = minX === maxX ? formatAxisDate(minX) : `${{formatAxisDate(minX)}} - ${{formatAxisDate(maxX)}}`;
      const card = document.createElement("section");
      card.className = "card chart-card";
      const count = series.reduce((total, entry) => total + entry.points.length, 0);
      card.innerHTML = `
        <div class="chart-head">
          <div>
            <h2>${{chart.title}}</h2>
            <p class="muted">${{chart.description}}</p>
          </div>
          <span class="badge">Past year / ${{count}} points</span>
        </div>
        <svg class="chart" viewBox="0 0 960 390" role="img" aria-label="${{chart.title}} chart"></svg>
        <div class="legend"></div>
      `;

      const svg = card.querySelector("svg");
      const legend = card.querySelector(".legend");
      const left = 78, top = 34, width = 830, height = 270;
      const bottom = top + height;
      const xScale = (dateValue) => left + ((dateValue - minX) / Math.max(maxX - minX, 1)) * width;
      const yScale = (value) => top + height - ((value - minY) / Math.max(maxY - minY, 1)) * height;

      const yTicks = valueTicks(minY, maxY, 5);
      const xTicks = yearTicks(minX, maxX);
      const zeroLine = minY < 0 && maxY > 0 ? `<line x1="${{left}}" y1="${{yScale(0)}}" x2="${{left + width}}" y2="${{yScale(0)}}" stroke="#808a96" stroke-dasharray="4 4" />` : "";
      svg.innerHTML = `
        <rect x="0" y="0" width="960" height="390" rx="8" fill="#2b2b2b" />
        <text x="${{left}}" y="20" fill="#808a96" font-size="12">${{dateRange}}</text>
        ${{yTicks.map((tick) => `<g><line x1="${{left}}" y1="${{yScale(tick)}}" x2="${{left + width}}" y2="${{yScale(tick)}}" stroke="#45494a" /><text x="${{left - 14}}" y="${{yScale(tick) + 4}}" text-anchor="end" fill="#a9b7c6" font-size="12">${{formatAxisValue(tick, series[0].unit)}}</text></g>`).join("")}}
        ${{xTicks.map((tick) => `<g><line x1="${{xScale(tick)}}" y1="${{top}}" x2="${{xScale(tick)}}" y2="${{bottom}}" stroke="#3c3f41" /><text x="${{xScale(tick)}}" y="${{bottom + 34}}" text-anchor="middle" fill="#a9b7c6" font-size="12">${{formatAxisDate(tick)}}</text></g>`).join("")}}
        ${{zeroLine}}
        <line x1="${{left}}" y1="${{top}}" x2="${{left}}" y2="${{bottom}}" stroke="#5e6366" />
        <line x1="${{left}}" y1="${{bottom}}" x2="${{left + width}}" y2="${{bottom}}" stroke="#5e6366" />
      `;

      series.forEach((entry, index) => {{
        const color = chartColors[chart.id] || colors[index % colors.length];
        const points = entry.points
          .map((point) => ({{ ...point, dateValue: Date.parse(point.date) || 0 }}))
          .sort((a, b) => a.dateValue - b.dateValue);
        const path = smoothPath(points, xScale, yScale);
        const areaPath = points.length > 1
          ? `${{path}} L ${{xScale(points[points.length - 1].dateValue).toFixed(2)}} ${{bottom}} L ${{xScale(points[0].dateValue).toFixed(2)}} ${{bottom}} Z`
          : "";
        if (areaPath) {{
          const areaNode = document.createElementNS("http://www.w3.org/2000/svg", "path");
          areaNode.setAttribute("d", areaPath);
          areaNode.setAttribute("fill", color);
          areaNode.setAttribute("opacity", "0.16");
          svg.appendChild(areaNode);
        }}
        const pathNode = document.createElementNS("http://www.w3.org/2000/svg", "path");
        pathNode.setAttribute("d", path);
        pathNode.setAttribute("fill", "none");
        pathNode.setAttribute("stroke", color);
        pathNode.setAttribute("stroke-width", "3");
        pathNode.setAttribute("stroke-linecap", "round");
        pathNode.setAttribute("stroke-linejoin", "round");
        svg.appendChild(pathNode);

        const markedPoints = points.length <= 18 ? points : [points[0], points[points.length - 1]];
        markedPoints.forEach((point) => {{
          const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          dot.setAttribute("cx", xScale(point.dateValue));
          dot.setAttribute("cy", yScale(point.value));
          dot.setAttribute("r", points.length <= 18 ? "3.5" : "4.5");
          dot.setAttribute("fill", color);
          dot.setAttribute("stroke", "#2b2b2b");
          dot.setAttribute("stroke-width", "2");
          dot.innerHTML = `<title>${{point.date}}: ${{formatValue(point.value, entry.unit)}}</title>`;
          svg.appendChild(dot);
        }});

        const item = document.createElement("span");
        item.className = "legend-item";
        item.innerHTML = `<span class="swatch" style="background:${{color}}"></span>${{entry.label}}`;
        legend.appendChild(item);
      }});

      return card;
    }}

    const charts = document.getElementById("charts");
    data.charts.forEach((chart) => {{
      const card = makeChart(chart);
      if (card) charts.appendChild(card);
    }});

    const tableColumns = [
      {{
        label: "Date",
        always: true,
        render: (record) => record.alert_date || String(record.email_date || "").slice(0, 10) || "--",
      }},
      {{
        label: "Charge to date",
        path: "charges.total.to_date",
        unit: "$",
        render: (record) => formatValue(valueAt(record, "charges.total.to_date"), "$"),
      }},
      {{
        label: "Projected low",
        path: "charges.total.projected_min",
        unit: "$",
        render: (record) => formatValue(valueAt(record, "charges.total.projected_min"), "$"),
      }},
      {{
        label: "Projected high",
        path: "charges.total.projected_max",
        unit: "$",
        render: (record) => formatValue(valueAt(record, "charges.total.projected_max"), "$"),
      }},
      {{
        label: "Bill amount due",
        path: "charges.bill.amount_due",
        unit: "$",
        render: (record) => formatValue(valueAt(record, "charges.bill.amount_due"), "$"),
      }},
      {{
        label: "kWh",
        path: "usage.electricity.kwh_to_date",
        unit: " kWh",
        render: (record) => formatValue(valueAt(record, "usage.electricity.kwh_to_date"), " kWh"),
      }},
      {{
        label: "Therms",
        path: "usage.gas.therms_to_date",
        unit: " therms",
        render: (record) => formatValue(valueAt(record, "usage.gas.therms_to_date"), " therms"),
      }},
      {{
        label: "Solar returned",
        path: "usage.solar.returned_to_grid_kwh_to_date",
        unit: " kWh",
        render: (record) => formatValue(valueAt(record, "usage.solar.returned_to_grid_kwh_to_date"), " kWh"),
      }},
      {{
        label: "Days left",
        path: "billing.days_left_in_bill_period",
        unit: " days",
        render: (record) => formatValue(valueAt(record, "billing.days_left_in_bill_period"), " days"),
      }},
    ];
    const activeColumns = tableColumns.filter((column) => (
      column.always || data.records.some((record) => typeof valueAt(record, column.path) === "number")
    ));
    document.getElementById("records-head").innerHTML = activeColumns.map((column) => `<th>${{column.label}}</th>`).join("");
    const tbody = document.getElementById("records-body");
    data.records.forEach((record) => {{
      const row = document.createElement("tr");
      row.innerHTML = activeColumns.map((column) => `<td>${{column.render(record)}}</td>`).join("");
      tbody.appendChild(row);
    }});
  </script>
</body>
</html>
"""


def write_report(report_file: Path, db_file: Path, records: list[dict[str, Any]]) -> None:
    report_file.parent.mkdir(parents=True, exist_ok=True)
    report_file.write_text(build_dashboard_html(records, db_file), encoding="utf-8")


def parse_record_json(record_json: str) -> list[dict[str, Any]]:
    payload = parse_json_value(record_json)
    if isinstance(payload, dict):
        return [payload]
    if isinstance(payload, list) and all(isinstance(item, dict) for item in payload):
        return payload
    raise ValueError("--record-json must be a JSON object or an array of objects")


def parse_json_value(value: str) -> Any:
    if value == "-":
        return json.load(sys.stdin)
    if value.startswith("@"):
        return json.loads(Path(value[1:]).read_text(encoding="utf-8"))
    return json.loads(value)


def parse_message_ids_json(value: str) -> list[str]:
    payload = parse_json_value(value)
    if isinstance(payload, dict) and isinstance(payload.get("message_ids"), list):
        payload = payload["message_ids"]
    if not isinstance(payload, list) or not all(isinstance(item, str) for item in payload):
        raise ValueError("message IDs must be a JSON array of strings or an object with message_ids")
    return payload


def processed_id_set(processed_entries: list[dict[str, Any]]) -> set[str]:
    return {str(entry["message_id"]) for entry in processed_entries if entry.get("message_id")}


def diff_message_ids(message_ids: list[str], processed_entries: list[dict[str, Any]]) -> dict[str, Any]:
    processed_ids = processed_id_set(processed_entries)
    seen: set[str] = set()
    unique_ids: list[str] = []
    duplicate_ids: list[str] = []
    for message_id in message_ids:
        if message_id in seen:
            duplicate_ids.append(message_id)
            continue
        seen.add(message_id)
        unique_ids.append(message_id)

    already_processed = [message_id for message_id in unique_ids if message_id in processed_ids]
    unprocessed = [message_id for message_id in unique_ids if message_id not in processed_ids]
    return {
        "status": "ok",
        "message_ids_seen": len(message_ids),
        "unique_message_ids": len(unique_ids),
        "duplicate_message_ids": duplicate_ids,
        "already_processed_count": len(already_processed),
        "unprocessed_count": len(unprocessed),
        "unprocessed_ids": unprocessed,
        "already_processed_ids": already_processed,
    }


def build_run_plan(
    records: list[dict[str, Any]],
    processed_entries: list[dict[str, Any]],
    gmail_total: int | None,
    unread_ids: list[str],
    report_file: Path,
) -> dict[str, Any]:
    processed_ids = processed_id_set(processed_entries)
    unique_unread_ids = list(dict.fromkeys(unread_ids))
    processed_unread_ids = [message_id for message_id in unique_unread_ids if message_id in processed_ids]
    unknown_unread_ids = [message_id for message_id in unique_unread_ids if message_id not in processed_ids]
    counts_match = gmail_total is not None and gmail_total == len(processed_ids)
    report_exists = report_file.exists()

    if counts_match and not unknown_unread_ids:
        if processed_unread_ids:
            action = "batch_mark_processed_unread_read_then_verify"
        elif report_exists:
            action = "fast_path_noop"
        else:
            action = "regenerate_report_only"
        can_skip_all_id_paging = True
    else:
        action = "page_all_message_ids_then_diff"
        can_skip_all_id_paging = False

    return {
        "status": "ok",
        "recommended_action": action,
        "can_skip_all_id_paging": can_skip_all_id_paging,
        "counts_match": counts_match,
        "gmail_total": gmail_total,
        "records": len(records),
        "processed_entries": len(processed_entries),
        "processed_ids": len(processed_ids),
        "report_exists": report_exists,
        "unread_ids_seen": len(unique_unread_ids),
        "processed_unread_ids": processed_unread_ids,
        "unknown_unread_ids": unknown_unread_ids,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db-file", type=Path, default=Path(os.environ.get("SDGE_ENERGY_DB_FILE", DEFAULT_DB_FILE)))
    parser.add_argument(
        "--processed-file",
        type=Path,
        default=Path(os.environ.get("SDGE_ENERGY_PROCESSED_FILE", DEFAULT_PROCESSED_FILE)),
    )
    parser.add_argument(
        "--report-file",
        type=Path,
        default=Path(os.environ.get("SDGE_ENERGY_REPORT_FILE", DEFAULT_REPORT_FILE)),
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    upsert_parser = subparsers.add_parser("upsert", help="Upsert one record or a list of records and optionally regenerate the report.")
    upsert_parser.add_argument("--record-json", required=True, help="JSON object or array of objects to upsert.")
    upsert_parser.add_argument("--no-report", action="store_true", help="Only update JSONL data and ledger; regenerate report later.")

    subparsers.add_parser("report", help="Regenerate the report from the existing database.")
    subparsers.add_parser("summary", help="Print a compact JSON summary of the existing database.")
    subparsers.add_parser("processed-ids", help="Print processed Gmail message IDs as JSON.")
    subparsers.add_parser("sync-ledger", help="Backfill the processed-email ledger from existing records.")

    diff_parser = subparsers.add_parser("diff-ids", help="Compare Gmail message IDs with the processed-email ledger.")
    diff_parser.add_argument("--message-ids-json", required=True, help="JSON array, {'message_ids': [...]}, @file, or - for stdin.")

    plan_parser = subparsers.add_parser("run-plan", help="Plan the efficient Gmail workflow from local state and cheap Gmail counts.")
    plan_parser.add_argument("--gmail-total", type=int, help="Gmail SDGE label total from list_labels.")
    plan_parser.add_argument(
        "--unread-ids-json",
        default="[]",
        help="Unread matching Gmail message IDs as JSON array, {'message_ids': [...]}, @file, or - for stdin.",
    )

    args = parser.parse_args()

    if args.command == "upsert":
        incoming = parse_record_json(args.record_json)
        records = upsert_records(args.db_file, args.processed_file, incoming)
        if not args.no_report:
            write_report(args.report_file, args.db_file, records)
        print(
            json.dumps(
                {
                    "status": "ok",
                    "records_written": len(records),
                    "upserted": len(incoming),
                    "report_written": not args.no_report,
                    "db_file": str(args.db_file),
                    "processed_file": str(args.processed_file),
                    "report_file": str(args.report_file),
                },
                indent=2,
            )
        )
        return 0

    records = sorted(load_records(args.db_file), key=record_sort_key)
    processed_entries = sorted(load_processed_entries(args.processed_file), key=processed_sort_key)

    if args.command == "diff-ids":
        message_ids = parse_message_ids_json(args.message_ids_json)
        print(json.dumps(diff_message_ids(message_ids, processed_entries), indent=2))
        return 0

    if args.command == "run-plan":
        unread_ids = parse_message_ids_json(args.unread_ids_json)
        print(json.dumps(build_run_plan(records, processed_entries, args.gmail_total, unread_ids, args.report_file), indent=2))
        return 0

    if args.command == "report":
        write_report(args.report_file, args.db_file, records)
        print(
            json.dumps(
                {
                    "status": "ok",
                    "records_written": len(records),
                    "processed_entries": len(processed_entries),
                    "report_file": str(args.report_file),
                },
                indent=2,
            )
        )
        return 0

    if args.command == "processed-ids":
        ids = [entry["message_id"] for entry in processed_entries if entry.get("message_id")]
        print(json.dumps({"status": "ok", "message_ids": ids, "processed_file": str(args.processed_file)}, indent=2))
        return 0

    if args.command == "sync-ledger":
        processed_entries = sync_processed_ledger(args.processed_file, records)
        print(
            json.dumps(
                {
                    "status": "ok",
                    "records": len(records),
                    "processed_entries": len(processed_entries),
                    "processed_file": str(args.processed_file),
                },
                indent=2,
            )
        )
        return 0

    latest = records[-1] if records else None
    print(
        json.dumps(
            {
                "status": "ok",
                "records": len(records),
                "processed_entries": len(processed_entries),
                "latest_alert_date": latest.get("alert_date") if latest else None,
                "db_file": str(args.db_file),
                "processed_file": str(args.processed_file),
                "report_file": str(args.report_file),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
