---
name: accept-sender-appointments
description: Accept calendar appointments or meeting invitations from a named sender, then optionally mark that sender's matching Gmail messages as read. Use when the user asks to accept all appointments from a sender, do the same for a sender, accept unread meeting invites from a person or company, mark those emails read, or otherwise wants Codex to coordinate Gmail invite messages with Google Calendar RSVP actions for a specific sender.
---

# Accept Sender Appointments

## Overview

Use this skill to repeat the Gmail-plus-Calendar cleanup pattern: locate messages from a specific sender, distinguish appointment or deadline-relevant messages from ordinary messages, accept matching Google Calendar events once, create events when details are embedded in email text/attachments, and mark the requested sender messages read.

The workflow is harness-neutral. In Codex, use the Gmail and Google Calendar connectors. In another harness, use equivalent Gmail search/message-label APIs and Calendar event RSVP APIs while preserving the same inputs, safety rules, and verification steps.

## Required Inputs

- Sender name, company, or email domain. If the user gives a broad name such as "Samantha" or "Rula", search Gmail first and use the actual senders in the results.
- Optional explicit Gmail query from an automation spec, allowlist, or external harness.
- Read-state scope. Default to unread messages unless the user explicitly asks for all historical sender messages.
- Calendar target. If a sender row requires a non-primary destination (for example, `Acton`), write accepted/created events to that calendar.
- Message cleanup intent. If the user says "mark all <sender> messages read", remove `UNREAD` from every matching sender message found in scope, not only invite emails. If they only ask to accept appointments, do not mark unrelated messages read unless the prompt implies the prior cleanup pattern.

## Workflow

1. Search Gmail for matching sender messages.
   - Use Gmail search syntax in `query`, such as `is:unread Rula -in:spam -in:trash` or `is:unread from:youngsamanth@gmail.com -in:spam -in:trash`.
   - Start with `max_results` around 50. Page if `next_page_token` appears and the prompt asks for all matching messages.
   - For backfill requests, include an explicit date floor (for example `after:2026/07/01`) and process matches from that date forward even if read.
   - Keep unrelated lookalikes separate. For example, social notification emails mentioning a person are not appointment invites unless the user explicitly includes them in the read cleanup.

   For a recurring runner that has an approved, opaque reviewed-message ledger, use an ID-only search first and read full details only for IDs not already recorded as confirmed non-calendar. Record a new ID only after it is clearly non-calendar; never record ambiguous messages. The ledger must not contain message bodies or private metadata.

2. Identify appointment/deadline messages.
   - Treat subjects like `Invitation:`, `Updated invitation:`, `appointment confirmed`, `appointment rescheduled`, or messages with `invite.ics` as appointment evidence.
   - Also parse message text and supported attachments for event details when no invite exists.
   - For Acton, only process time-bounded school events labeled `All classes` or `Wonder Studio`. Ignore other class categories unless an event is explicitly for `All students`.
   - Independently process a clearly stated Acton deadline, even when the same message also describes an event for a non-allowlisted class. Create the deadline reminder on the `Acton` calendar when the date is unambiguous; leave the unrelated class-specific event unprocessed.
   - If the message is purely informational (for example side-door access guidance with no date/time), classify it as non-calendar.
   - Prefer accepting the underlying Calendar event, not replying by email.
   - If the message is deadline-only (no event time window), treat it as a reminder candidate and schedule a reminder day-before.
   - Deduplicate updated/original invite emails that refer to the same event title and date.

3. Search Google Calendar for each event.
   - Use the concrete event title and a bounded time window derived from the email subject or snippet.
   - If the message describes a recurring appointment, search the upcoming bounded range visible in the emails before widening.
   - Read or search enough event detail to confirm the title, time, location, and sender/organizer relationship when ambiguity exists.
   - If a message contains a class-category event description without an invitation link, parse the date/time and location and check for an existing matching event before creating a new one.
   - For Acton, when no invite is found, create the event directly on the `Acton` calendar instead of default primary.

4. Accept each matching event exactly once.
   - Call Google Calendar's RSVP/respond action with `response_status: accepted`.
   - Use `notify: true` unless the user says not to notify.
   - Preserve event details. Do not edit title, time, attendees, reminders, location, or recurrence as part of this skill.
   - If an event description says changes must be made in an external portal, still use Calendar RSVP only; do not modify the appointment details.
   - For Acton-only deadline messages, create a reminder with exactly one reminder offset at 1 day before the deadline and avoid duplicating if one already exists.

5. Mark messages read if requested or clearly implied.
   - Remove the Gmail `UNREAD` label with batch modify.
   - If the request says "all <sender> messages", include receipts/confirmations from the sender in the same bounded search scope.
   - If the request only says "those emails", mark only the appointment/invite messages found for the operation.
   - For Acton, keep informational/non-calendar messages unread unless explicitly requested for full-sender cleanup.

6. Verify and report.
   - Re-run a Gmail unread search for the sender after a Gmail-label or RSVP change and report whether any remain. If no state changed, the initial ID-only search is sufficient verification.
   - If useful, re-search or read Calendar events to confirm accepted status.
   - Final response should include counts and the event dates/times, plus reminder-only items when created, but not private body details.

## Harness-Neutral Contract

Any runner implementing this skill should provide these capabilities:

- Gmail search over unread messages with sender/name/domain query support.
- Message body or metadata access sufficient to identify invitation subjects, snippets, and attachment text (including PDFs) containing event details.
- Google Calendar event search or lookup over bounded date windows, plus event creation/retrieval on the target calendar when needed.
- Calendar RSVP update for the authenticated user.
- Gmail label update that can remove the unread marker from explicit message IDs.

The runner should treat the skill as a state-changing workflow. It must operate on explicit message IDs and event IDs after discovery, then verify the resulting read state and RSVP state before reporting completion.

## Safety Rules

- Do not accept invitations from multiple people or companies unless the user named each one.
- Do not mark broad mailbox categories read. Always operate on explicit message IDs returned by the sender search.
- Do not delete, archive, forward, or send mail as part of this skill.
- Do not expose sensitive appointment notes or receipt details in the final answer; summarize only what is needed to confirm completion.
- If multiple similarly named events exist and the sender/date cannot be confirmed from Gmail and Calendar evidence, stop and ask for clarification before accepting.
- Do not create duplicate events: check existing matching events on the target calendar before creating.
- Do not send Acton-sourced events to non-Acton calendars, and do not create Acton events on the primary calendar.

## Example Requests

- `Use $accept-sender-appointments for Samantha and mark those emails read.`
- `Accept all unread Rula appointments and mark all Rula messages read.`
- `Accept every meeting invite from Priya in my unread mail.`

## Output Shape

Keep the final answer compact:

- Number of accepted appointments.
- Event titles and exact dates/times.
- Number of messages marked read.
- Verification result, especially whether unread sender messages remain.

## Post-Run Learning

After a meaningful run, capture safe efficiency lessons for future runs:

- Record predictable non-calendar false positives only in the approved runner ledger, using message IDs and compact row names.
- Note repeated ambiguity, redundant searches, or cleanup wording that should become policy in `os/automations/auto-accept-appointments.md`.
- Do not store message bodies, appointment notes, receipts, secrets, or unnecessary personal details.
- Do not rewrite this `SKILL.md` automatically. Recommend a skill update only when the lesson is stable and likely to reduce future work.
## Event notices and attachment-backed dates

Some trusted sender rows describe school or organization events in ordinary email text rather than a Calendar invitation. For those rows:

- Treat email text and supported attachments as event sources. Read only attachments needed to resolve a relevant event's date, time, location, or deadline.
- Apply the row's audience filter before creating time-bounded events. For an Acton-style row, include only events explicitly for the configured studio/class and events for all students or all studios; ignore other classroom-specific items. A clearly stated standalone deadline is an exception: create its deadline reminder on the Acton calendar even if the same message also contains a disallowed class-specific event.
- Resolve the destination calendar by its configured name and always create direct events there, never on the primary calendar.
- Before creating a direct event, use a bounded search of that destination calendar for the event name and date range. Treat an existing matching event as processed instead of creating a duplicate.
- Create direct events only when the date and a usable time range are confirmed. Do not invent durations for date-only notices; leave those as ambiguities for the run report.
- For a deadline-only notice, create a clearly labeled short reminder at 9:00 AM local time when no deadline time is supplied, with one popup reminder 1,440 minutes before it. State in the description that the deadline time was not specified.
- Mark a matching message read only after its calendar event or deadline reminder has been created or deduplicated. Leave purely informational messages unread when the row requires that behavior.

## Backfills

For a requested historical backfill, replace the normal unread-only search with the row's explicit date floor and include both read and unread messages. Keep the same sender, category, attachment, destination-calendar, and deduplication rules. Return to unread-only searches on subsequent scheduled runs.
