---
name: ticket-to-pr
description: End-to-end Measurabl Jira ticket implementation workflow. Use when the user gives Codex a Jira ticket id such as WILD-1234 and wants the work taken through ticket research, code research, implementation planning, minimal-diff development, unit and integration tests, branch/commit/push, and a draft GitHub PR for human review.
---

# Ticket To Draft PR

Use this workflow to take a Measurabl Jira ticket from research to a draft PR.
The ticket id and any extra user context are the inputs. Work through the phases
in order. Prefer accuracy over speed; do not fabricate ticket contents,
acceptance criteria, or product behavior.

## Guardrails

- Open only a draft PR. Never merge, mark ready for review, or send anything externally on the user's behalf.
- Call out customer-facing, pricing, contract, compliance, or commitment risk and name the team that should verify it.
- Keep customer names, account ids, contract values, operational metrics, and other confidential data out of tests, fixtures, code, commit messages, and PR bodies. Use synthetic values.
- Never write secrets into files, configs, logs, commits, or PR text. Use already-authenticated CLIs/connectors or short-lived environment variables.
- Branch and commit only in the final branch/commit phase unless the user explicitly asks earlier.
- Stage only files you changed. Do not sweep in unrelated untracked or pre-existing modified files.

## Phase 1: Research The Ticket

1. Fetch the named Jira ticket with the available Jira or Atlassian connector/MCP. If no Jira tool is available or authenticated, ask the user for the ticket content or authorization path before claiming ticket facts.
2. Capture the ticket summary and acceptance criteria verbatim. In Jira, acceptance criteria may be in a custom field rather than the description.
3. Follow the trail: parent/epic, linked tickets, tickets referenced in the description, and background spikes. These often contain the why, edge cases, and worked examples.
4. If a ticket payload is too large, save or inspect it outside the main context and extract only the description, acceptance criteria, comments, links, and decisive fields. Preserve key findings as short quotes.
5. Weave in any extra context the user supplied, especially vendor guidance, examples, or constraints.

## Phase 2: Research The Code

- Map the relevant code paths, utilities, and matching tests. Use fast repository search first, then read critical files directly.
- Parallelize independent search/read/test discovery when tools allow it.
- Find existing tests that encode current behavior, including tests that assert the opposite of the requested change.
- Distinguish unit tests, integration tests, scenario/declarative suites, and any required test matrix or README updates.
- Read the few critical files yourself before planning so the plan is grounded in code, not search summaries.

## Phase 3: Plan And Get Approval

For non-trivial work, present a concise plan and wait for explicit user approval
before editing. Include:

- Context: problem, why now, and intended outcome.
- Recommended approach only.
- Specific files to change, with repeated patterns described once.
- Existing functions, utilities, or patterns to reuse, with paths.
- Test strategy and verification commands.
- Risks, review flags, or cases that may need product/customer-success/compliance confirmation.

Ask the user only for decisions that cannot be resolved from the ticket, code,
or sensible local defaults. Prefer minimal-diff solutions and avoid speculative
refactors.

## Phase 4: Implement The Fix

- Make the smallest change that satisfies the acceptance criteria.
- Match surrounding code style, naming, and comment density.
- Reuse existing helpers and patterns found during code research.
- Reference the ticket id in comments or Javadocs only where documenting a behavior decision is useful.
- Replace stale references to superseded tickets when the new ticket changes that behavior.
- Remove code made dead by the change.

## Phase 5: Test

- Add or update unit tests for the changed logic.
- Update tests for the changed unit to the new expectations when behavior intentionally changes.
- For legacy tests that assert old behavior and should remain as historical coverage, disable or skip at the narrowest method/scenario level with a note citing the ticket and pointing to new coverage, unless the user asks to update them instead.
- Add or update integration/scenario tests when the ticket affects contracts, response shapes, filtering, persistence, or user-visible behavior.
- Determine expected values from implementation code, not guesses, especially for null-vs-0, filtering, and response-building behavior.
- Keep fixtures synthetic and update any required suite matrix or README.
- Run affected tests and report real summary lines. If a suite requires a service or environment that is not available locally, say so and rely on CI for that suite. Always at least test-compile touched modules when practical.

## Phase 6: Branch, Commit, Push, Draft PR

1. Create or switch to a ticket-prefixed branch from the default branch when ready, unless already on a suitable branch.
2. Commit only the intended files with a clear message. Include required project trailers or generated-by lines when the repo defines them.
3. Push the branch.
4. Open a draft PR against the default branch. Prefer `gh pr create --draft --base <default>` when available; otherwise use the GitHub connector. Use real multi-line PR body text.
5. In the PR body include: what and why, ticket link, worked example where useful, change list, local test results, CI-only caveats, and review/approval flags.
6. Report the PR URL and stop at draft.

## Done

Summarize what changed, test results, PR URL, and any flags for human review.
