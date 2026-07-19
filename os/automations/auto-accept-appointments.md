# Auto-Accept Appointments

## Purpose

Automatically accept appointment or meeting invitations from a small allowlist of trusted senders, then mark matching sender messages read.

This file is the harness-neutral source of truth. A scheduler, agent runner, shell script, or Codex automation can implement it as long as it follows the contract below.

## Schedule

Run every 6 hours at 6:00 AM, noon, 6:00 PM, and midnight Pacific time, observing PST/PDT.

## Match List

Add new trusted senders by adding a row to this table.

| Name | Gmail Query | Message Cleanup | Status | Notes |
|---|---|---|---|---|
| Samantha Young | `from:youngsamanth@gmail.com` | Mark appointment/invite messages read | Active | Leave unrelated social notification emails unread unless explicitly matched by this sender query and appointment evidence. |
| Rula | `Rula` | Mark all matching Rula messages read | Active | Includes appointment confirmations, invitations, reschedules, and receipts from Rula sender domains. |

## Efficient Runner State

Scheduled runners may keep an opaque, runner-owned ledger of **reviewed non-calendar Gmail message IDs**, keyed to the active match-list row. This ledger is an optimization only; it is not policy or a source of appointment data.

- Start each row with an ID-only unread Gmail search. Read full message details only for IDs not in the ledger.
- After a newly seen message is clearly confirmed to have no appointment or calendar-invitation evidence, record only its Gmail message ID and row name in the ledger. Do not record message bodies, subjects, senders, or other personal details.
- For a ledgered message, skip Calendar lookup and invitation classification on later runs. Still apply the row's cleanup rule if it has not already been applied.
- Do not record an ambiguous message. Leave it eligible for later review and report the ambiguity.
- A broad query can return a non-allowlisted sender. Treat that as a confirmed non-calendar false positive only after checking the actual sender; do not accept an event or mark that message read.
- If a run makes no RSVP or Gmail-label changes, its initial ID-only search is the verification result. Re-run the sender search only after a state-changing action.

## Runner Contract

For each active row in the match list:

1. Search Gmail for unread message IDs matching `Gmail Query`, excluding spam and trash, then compare them with the runner ledger.
2. Identify appointment or calendar-invitation evidence only for new, non-ledgered messages.
3. Find matching Google Calendar events using concrete titles and bounded date windows from appointment candidates only.
4. Accept each matching event once.
5. Mark messages read according to `Message Cleanup`.
6. Verify the unread search after a state-changing action; otherwise use the initial ID-only result.
7. Report accepted event count, event dates/times, messages marked read, newly recorded non-calendar messages, and any skipped ambiguity.

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
