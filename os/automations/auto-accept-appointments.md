# Auto-Accept Appointments

## Purpose

Automatically accept appointment or meeting invitations from a small allowlist of trusted senders, then mark matching sender messages read.

This file is the harness-neutral source of truth. A scheduler, agent runner, shell script, or Codex automation can implement it as long as it follows the contract below.

## Schedule

Run every 2 hours between 7:00 AM and 11:00 PM local time.

## Match List

Add new trusted senders by adding a row to this table.

| Name | Gmail Query | Message Cleanup | Status | Notes |
|---|---|---|---|---|
| Samantha Young | `from:youngsamanth@gmail.com` | Mark appointment/invite messages read | Active | Leave unrelated social notification emails unread unless explicitly matched by this sender query and appointment evidence. |
| Rula | `Rula` | Mark all matching Rula messages read | Active | Includes appointment confirmations, invitations, reschedules, and receipts from Rula sender domains. |

## Runner Contract

For each active row in the match list:

1. Search Gmail for unread messages matching `Gmail Query`, excluding spam and trash.
2. Identify appointment or calendar-invitation evidence.
3. Find matching Google Calendar events using concrete titles and bounded date windows from the messages.
4. Accept each matching event once.
5. Mark messages read according to `Message Cleanup`.
6. Verify the unread search after cleanup.
7. Report accepted event count, event dates/times, messages marked read, and any skipped ambiguity.

## Safety Rules

- Only process rows with `Status` set to `Active`.
- Do not accept invitations from senders outside the match list.
- Do not delete, archive, forward, or send email.
- Do not edit event title, time, attendees, location, recurrence, reminders, or notes.
- If the sender, event, date, or appointment evidence is ambiguous, skip that item and report it.
- Keep final reports compact and avoid exposing private appointment notes, receipt details, or message bodies.

## Implementation Notes

- Codex implementation: use `.agents/skills/accept-sender-appointments/`.
- Current Codex automation ID: `auto-accept-trusted-appointments`.
- Non-Codex implementation: use the same runner contract with equivalent Gmail search, Calendar RSVP, and message-label APIs.
- Treat this file as policy/config, not generated output. Update the match list here before changing a scheduler prompt.
