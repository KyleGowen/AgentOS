---
name: accept-sender-appointments
description: Accept calendar appointments or meeting invitations from a named sender, then optionally mark that sender's matching Gmail messages as read. Use when the user asks to accept all appointments from a sender, do the same for a sender, accept unread meeting invites from a person or company, mark those emails read, or otherwise wants Codex to coordinate Gmail invite messages with Google Calendar RSVP actions for a specific sender.
---

# Accept Sender Appointments

## Overview

Use this skill to repeat the Gmail-plus-Calendar cleanup pattern: locate unread messages from a specific sender, distinguish appointment invitations from ordinary messages, accept the matching Google Calendar events once each, and mark the requested sender messages read.

The workflow is harness-neutral. In Codex, use the Gmail and Google Calendar connectors. In another harness, use equivalent Gmail search/message-label APIs and Calendar event RSVP APIs while preserving the same inputs, safety rules, and verification steps.

## Required Inputs

- Sender name, company, or email domain. If the user gives a broad name such as "Samantha" or "Rula", search Gmail first and use the actual senders in the results.
- Optional explicit Gmail query from an automation spec, allowlist, or external harness.
- Read-state scope. Default to unread messages unless the user explicitly asks for all historical sender messages.
- Message cleanup intent. If the user says "mark all <sender> messages read", remove `UNREAD` from every matching sender message found in scope, not only invite emails. If they only ask to accept appointments, do not mark unrelated messages read unless the prompt implies the prior cleanup pattern.

## Workflow

1. Search Gmail for matching unread sender messages.
   - Use Gmail search syntax in `query`, such as `is:unread Rula -in:spam -in:trash` or `is:unread from:youngsamanth@gmail.com -in:spam -in:trash`.
   - Start with `max_results` around 50. Page if `next_page_token` appears and the prompt asks for all matching messages.
   - Keep unrelated lookalikes separate. For example, social notification emails mentioning a person are not appointment invites unless the user explicitly includes them in the read cleanup.

2. Identify appointment/invite messages.
   - Treat subjects like `Invitation:`, `Updated invitation:`, `appointment confirmed`, `appointment rescheduled`, or messages with `invite.ics` as appointment evidence.
   - Prefer accepting the underlying Calendar event, not replying by email.
   - Deduplicate updated/original invite emails that refer to the same event title and date.

3. Search Google Calendar for each event.
   - Use the concrete event title and a bounded time window derived from the email subject or snippet.
   - If the message describes a recurring appointment, search the upcoming bounded range visible in the emails before widening.
   - Read or search enough event detail to confirm the title, time, location, and sender/organizer relationship when ambiguity exists.

4. Accept each matching event exactly once.
   - Call Google Calendar's RSVP/respond action with `response_status: accepted`.
   - Use `notify: true` unless the user says not to notify.
   - Preserve event details. Do not edit title, time, attendees, reminders, location, or recurrence as part of this skill.
   - If an event description says changes must be made in an external portal, still use Calendar RSVP only; do not modify the appointment details.

5. Mark messages read if requested or clearly implied.
   - Remove the Gmail `UNREAD` label with batch modify.
   - If the request says "all <sender> messages", include receipts/confirmations from the sender in the same bounded search scope.
   - If the request only says "those emails", mark only the appointment/invite messages found for the operation.

6. Verify and report.
   - Re-run a Gmail unread search for the sender and report whether any remain.
   - If useful, re-search or read Calendar events to confirm accepted status.
   - Final response should include counts and the event dates/times, not private body details.

## Harness-Neutral Contract

Any runner implementing this skill should provide these capabilities:

- Gmail search over unread messages with sender/name/domain query support.
- Message body or metadata access sufficient to identify invitation subjects, snippets, and calendar attachments.
- Google Calendar event search or lookup over bounded date windows.
- Calendar RSVP update for the authenticated user.
- Gmail label update that can remove the unread marker from explicit message IDs.

The runner should treat the skill as a state-changing workflow. It must operate on explicit message IDs and event IDs after discovery, then verify the resulting read state and RSVP state before reporting completion.

## Safety Rules

- Do not accept invitations from multiple people or companies unless the user named each one.
- Do not mark broad mailbox categories read. Always operate on explicit message IDs returned by the sender search.
- Do not delete, archive, forward, or send mail as part of this skill.
- Do not expose sensitive appointment notes or receipt details in the final answer; summarize only what is needed to confirm completion.
- If multiple similarly named events exist and the sender/date cannot be confirmed from Gmail and Calendar evidence, stop and ask for clarification before accepting.

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
