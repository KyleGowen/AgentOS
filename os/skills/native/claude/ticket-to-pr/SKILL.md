---
name: ticket-to-pr
description: >-
  End-to-end ticket implementation. Given a ticket identifier (e.g. WILD-1234) and any extra
  context, research the ticket and its related/linked/parent tickets, research the relevant code,
  produce an implementation plan for approval, implement a minimal-diff fix, write full unit tests
  and the relevant integration tests (updating or disabling legacy tests that assert the old
  behavior), make the affected tests pass, then branch, commit, push, and open a DRAFT PR. Use when
  the user hands you a ticket and wants it taken from research through a draft PR.
---

# Ticket → Draft PR

A repeatable workflow for taking a ticket from research to a draft PR. The ticket id and any extra
context are provided as arguments. Work through the phases in order. Prefer accuracy over speed; do
not fabricate ticket contents, acceptance criteria, or product behavior.

## Guardrails (apply throughout)

- **Draft PR only.** Open the PR as a draft. Never merge, never mark ready-for-review, never send
  anything externally on the user's behalf.
- **Customer-facing / risky changes:** if the change affects customer-facing output, pricing,
  contracts, compliance, or commitments, call it out and note which team should verify. Do not treat
  drafted language or output as final.
- **Confidential data:** never put real customer names, account ids, contract values, or operational
  metrics into tests, fixtures, code, commit messages, or the PR body. Use synthetic values.
- **Secrets:** never write tokens/PATs into files, configs, or logs. Use already-authenticated CLIs
  (`gh`, `git`) or short-lived env vars.
- **Branch/commit only when you reach Phase 6** (or when the user asks). Branch off the default
  branch (usually `master`/`main`); name the branch with the ticket id prefix
  (e.g. `WILD-1234-short-slug`). End commit messages with the project's required `Co-Authored-By`
  trailer and PR bodies with the required generated-by line if the environment defines them.
- **Delegate find/read/test to subagents** when the user's config calls for it (this user's global
  CLAUDE.md requires a subagent for find/read operations and for running tests — honor that). Run
  independent searches/builds in parallel.

## Phase 1 — Research the ticket(s)

1. Fetch the named ticket. For Jira, use the Atlassian MCP `getJiraIssue` (cloud id is the site host,
   e.g. `measurabl.atlassian.net`). If the MCP isn't authenticated, run the authenticate tool and ask
   the user to open the returned URL, then continue once connected.
2. **Capture the acceptance criteria verbatim.** On Jira these often live in a custom field (the AC
   field), not the description. Quote the AC and the summary exactly — the fix is judged against them.
3. Follow the trail: read the **parent/epic**, **linked** tickets, any ticket referenced in the
   description, and any **background spike**. These usually hold the "why" and worked examples.
4. **Large ticket output:** if a `getJiraIssue` result is too big and gets saved to a file, hand the
   file path to a subagent with the verbatim instruction to probe it with `jq` (type/length/keys),
   extract the description/AC/comments (Atlassian Document Format → text), and return key findings
   quoted verbatim — keep the raw dump out of the main context.
5. Weave in the user's extra context (it often contains the decisive constraint, e.g. a vendor's
   written guidance or specific examples).

## Phase 2 — Research the code

- Launch **parallel `Explore` subagents** (up to ~3) to map the relevant code: where the behavior
  lives, existing utilities/patterns to reuse, and where the matching tests live. Ask for
  `file_path:line_number` references and short excerpts.
- Have a separate Explore pass find **existing tests that encode the current behavior** — including
  any that assert the *opposite* of the intended change. Note unit tests vs integration tests vs any
  declarative/scenario test suites, and how a new test/scenario is added.
- Read the few critical files yourself to confirm the mechanism before planning.

## Phase 3 — Plan and get approval

- Enter plan mode (EnterPlanMode) for non-trivial work. Write a concise plan: **Context** (problem,
  why now, intended outcome), the recommended approach only, the specific files to change (describe
  repeated patterns once), functions/utilities to reuse with paths, the test strategy, and a
  verification section.
- Use AskUserQuestion only for genuine decisions you can't resolve from the ticket/code/sensible
  defaults. Prefer minimal-diff solutions; avoid speculative refactors.
- Call ExitPlanMode to request approval. Do not start editing until approved.

## Phase 4 — Implement the fix

- Make the smallest change that satisfies the AC. Match surrounding code style, naming, and comment
  density. Reuse existing helpers found in Phase 2. Reference the ticket id in code comments/Javadoc
  where you're encoding a behavior decision (and replace stale references to a superseded ticket).
- Remove code that the change makes dead, rather than leaving it orphaned.

## Phase 5 — Tests

- **Unit tests:** cover the changed logic thoroughly. Update existing unit tests for the changed unit
  to the new expectations (this is normal, not "disabling"). If a piece is hard to test, extract it to
  its own class as a testable seam.
- **Legacy tests asserting the OLD behavior:** per the user's preference, `@Disable`/skip them with a
  note that cites the ticket and points to where the new behavior is covered — unless the user asked
  you to update them instead. Disable per-method (or per-scenario), not wholesale; leave assertions
  that are still valid (e.g. coverage-only checks) intact.
- **Integration / scenario tests:** update existing ones to the new behavior with docs pointing to the
  ticket; if none exists for this contract, add one. Determine expected values by reading the
  response-building code, not by guessing — especially null-vs-0 and any filtering. Keep fixtures
  synthetic. Update any test matrix / README the suite requires.
- **Run the affected tests** (via a subagent if required by config). Report the real summary line. If
  the relevant suite needs a running service/env that isn't up locally (check ports first), say so
  explicitly and rely on CI — don't claim ITs passed when they didn't run. Always at least
  test-compile the modules you touched.

## Phase 6 — Branch, commit, push, draft PR

1. Create the ticket-prefixed branch off the default branch (if not already on a suitable branch).
2. Stage **only** the files you changed (don't sweep in pre-existing untracked files); commit with a
   clear message and the required trailer.
3. Push and open a **draft** PR with `gh pr create --draft --base <default>`. Write the PR body as a
   real multi-line string (actual newlines, not `\n`); MCP-based PR creation renders `\n` literally,
   so prefer `gh` or pass true newlines. In the body: what & why (link the ticket), a worked example,
   the list of changes, how it was tested (note what ran locally vs CI), and any review/approval flags.
4. Report the PR URL. Stop at draft — do not advance its state.

## Done

Summarize: what changed, test results (with the caveat about anything that ran only in CI), the PR
URL, and any flags raised for human review.
