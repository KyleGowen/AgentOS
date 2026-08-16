# Project 11: Automations

Status: In progress

Last audited: 2026-08-13

## Goal

Turn repeated agent workflows into scheduled or event-driven automations.

## Current State

Three harness-neutral automation policies exist and are paired with Codex
scheduled jobs:

- Appointment acceptance: active daily at 6:00 AM Pacific.
- SDGE energy alerts: active weekly Monday at 7:00 AM Pacific.
- Wanted-card listings: configured daily at 6:00 AM Pacific but currently
  paused because the required isolated logged-out marketplace browser is not
  available.

## Evidence

- `os/automations/auto-accept-appointments.md`
- `os/automations/sdge-energy-alerts.md`
- `os/automations/wanted-card-listings.md`
- `.agents/skills/accept-sender-appointments/`
- `.agents/skills/catalog-sdge-energy-alerts/`
- `.agents/skills/find-card-listings/`
- Live Codex automation configuration under `/Users/kyle/.codex/automations/`

## Completion Gap

The automation layer is operational but the course project still needs a
completion note covering end-to-end runs, failure handling, and final schedule
and runner-state verification.
