# Project 11: Automations

Status: Complete

Completed: 2026-08-17

Started: 2026-08-17

Last audited: 2026-08-17

Course page: <https://aidbagentos.ai/projects>

## Goal

Turn repeated agent workflows into scheduled or event-driven automations.

## Project 11 brief

### 11 — Automations

Make your agents work when you're not watching.

### What to Build

Set up a scheduled task, cron job, or event-driven trigger that runs your agent
without manual prompts, plus logging so you can see what happened.

### Project framing

Everything built so far runs when you ask it to. This project focuses on trustable
autonomy: repeated work should be reliable enough to run on schedule or on
events while you’re away.

### Practical tips

1. Start by automating a process you already run manually multiple times.
2. Start with automation that produces reviewable output before unsupervised
   side-effecting actions.
3. Keep logs so 3:00 AM failures are explainable.
4. This is the phase where your OS stops being helpful and becomes operational.

## Current State

Three harness-neutral automation policies exist and are paired with Codex
scheduled jobs:

- Appointment acceptance (`auto-accept-appointments` / `auto-accept-trusted-appointments`):
  active daily at 6:00 AM Pacific.
- SDGE energy alerts (`sdge-energy-alerts`): active weekly Monday at 7:00 AM
  Pacific.
- Wanted-card listings (`wanted-card-listings`): daily at 6:00 AM Pacific in policy,
  but currently paused in runner state because it requires an eBay developer account.

## Evidence

- `os/automations/auto-accept-appointments.md`
- `os/automations/sdge-energy-alerts.md`
- `os/automations/wanted-card-listings.md`
- `.agents/skills/accept-sender-appointments/`
- `.agents/skills/catalog-sdge-energy-alerts/`
- `.agents/skills/find-card-listings/`
- Live Codex automation configuration under `/Users/kyle/.codex/automations/`

## Completion Gate

### Updated status (2:24 PM)

- [x] SDGE Energy Alerts: end-to-end run evidence captured (no failures) and date-keyed in
  `runs/2026-08-17-sdge-energy-alerts.md`.
- [x] ThraxOS automation evidence: added under
  `runs/2026-08-17-thraxos-automation-evidence.md`.
- [x] Wanted-card automation: runner-state is explicitly recorded as paused due to missing
  eBay developer account requirement.
- [x] Failure-handling evidence: documented in `runs/2026-08-17-wanted-card-failure-path.md`
  for the wanted-card policy hard-stop and user-notify path when required auction
  fields cannot be retrieved.
- [x] Schedule/runner-state captured in one place for all jobs above.

## Completion evidence snapshot

### SDGE Energy Alerts run (Wednesday, 2:22 PM)

- Work time: 1m 41s
- Messages found: 248
- Newly processed: 1
- Already processed: 247
- Marked read: 1
- Left unprocessed: 0
- Database records: 248
- Ledger entries: 248
- Dashboard: [index.html](/Users/kyle/Documents/AgentOS/os/reports/sdge-energy-alerts/index.html)

## Schedule and runner-state matrix

- `auto-accept-appointments` (`auto-accept-trusted-appointments`)
  - Schedule: daily at 6:00 AM Pacific
  - Runner state: active
  - Evidence source: `os/automations/auto-accept-appointments.md`, `os/agents/os-thought-partner.md`, Playbook automation table

- `sdge-energy-alerts`
  - Schedule: weekly Monday at 7:00 AM Pacific
  - Runner state: active
  - Evidence source: `os/automations/sdge-energy-alerts.md`, `os/agents/sdge-energy-agent.md`,
    `projects/11-automations/runs/2026-08-17-sdge-energy-alerts.md`, dashboard path in `os/reports/sdge-energy-alerts/index.html`

- `wanted-card-listings`
  - Schedule policy: daily at 6:00 AM Pacific and list-change trigger
  - Runner state: paused
  - Pause reason: eBay developer account requirement not available
  - Evidence source: `os/automations/wanted-card-listings.md` and this note
