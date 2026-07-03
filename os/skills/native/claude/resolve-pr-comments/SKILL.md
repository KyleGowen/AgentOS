---
name: resolve-pr-comments
description: Given a PR link, read the PR and its linked Jira ticket, triage every review comment (agree/disagree), produce a plan with an agree/disagree chart for approval, then fix the agreements, reply to the disagreements on the PR with reasoning, commit and push, and resolve the threads that were fixed. Use when the user hands you a pull request URL and wants its review comments addressed end to end.
---

# Resolve PR Comments

End-to-end handling of review feedback on a pull request. The input is a **PR link**
(e.g. `https://github.com/Measurabl/wizard/pull/1819`, or `owner/repo#number`).

## Outcome

1. Every comment on the PR — human **and** AI/bot (Copilot, CodeRabbit, Claude, etc.) — is
   read and triaged into **Agree** or **Disagree**.
2. A **plan** is always produced for the user to review, containing an agree/disagree chart.
3. After approval: agreements are fixed in code, disagreements get a reasoned reply posted
   on the PR, the result is committed and pushed, and the threads that were fixed are resolved.

Do not skip the plan-approval gate. Posting replies, pushing code, and resolving threads are
outward-facing — present the plan and get approval before any of them.

## Step 1 — Read the PR

Parse `owner`, `repo`, and `number` from the link.

```bash
gh pr view <number> --repo <owner>/<repo> --json title,body,headRefName,baseRefName,state,url,author,files
gh pr diff <number> --repo <owner>/<repo>
```

Note the head branch (`headRefName`) — you will check it out before making fixes.

## Step 2 — Read the linked Jira ticket

Extract the ticket key from the branch name, PR title, or body (e.g. `WILD-1234`,
`BSOD-3099`; branches here are ticket-prefixed). Then read it with the Atlassian MCP:

- `mcp__atlassian__getJiraIssue` for the issue (description, acceptance criteria, status).
- If it has parent/linked issues relevant to the change, read those too.

Use the ticket to ground your triage: a comment asking for behavior the ticket explicitly
excludes is a likely **Disagree**; a comment pointing at unmet acceptance criteria is a
likely **Agree**.

## Step 3 — Collect every comment

Gather all three comment surfaces, including bot authors:

```bash
# Inline (code) review comments — has file path, line, in_reply_to_id, id
gh api repos/<owner>/<repo>/pulls/<number>/comments --paginate

# Review summaries (APPROVE / REQUEST_CHANGES / COMMENT bodies)
gh api repos/<owner>/<repo>/pulls/<number>/reviews --paginate

# PR conversation (issue-level) comments
gh api repos/<owner>/<repo>/issues/<number>/comments --paginate
```

To map inline comments to **review threads** and learn their resolution state and thread IDs
(needed to reply in-thread and to resolve later), use GraphQL:

```bash
gh api graphql -f query='
query($owner:String!,$repo:String!,$number:Int!){
  repository(owner:$owner,name:$repo){
    pullRequest(number:$number){
      reviewThreads(first:100){
        nodes{
          id isResolved isOutdated
          comments(first:50){ nodes{ id databaseId author{login} path body } }
        }
      }
    }
  }
}' -F owner=<owner> -F repo=<repo> -F number=<number>
```

Skip threads already resolved unless the user asks to revisit them.

## Step 4 — Triage each comment

For every open, actionable comment, decide **Agree** or **Disagree** by reading the actual
code at the referenced location and weighing it against the ticket. Be a genuine reviewer, not
a rubber stamp — AI bot comments are frequently wrong, out of date, or out of scope.

- **Agree** — the comment identifies a real, in-scope change worth making.
- **Disagree** — incorrect, already handled, out of scope for this ticket, a false positive,
  or a stylistic nit that conflicts with the codebase's conventions. **Every disagreement
  needs concrete reasoning** (cite the code, the ticket, or the convention).

Purely informational comments with no requested change need no action — note them as such.

## Step 5 — Produce the plan (always)

Present a plan for review with a chart of every triaged comment:

| # | Author | Location | Comment (summary) | Verdict | Action |
|---|--------|----------|-------------------|---------|--------|
| 1 | coderabbitai | `Foo.java:42` | Null-check `bar` | **Agree** | Add guard before deref |
| 2 | alice | `Baz.java:10` | Use a `Set` here | **Disagree** | Order matters — `List` is intentional; reasoning posted as reply |

For each **Disagree**, include the full reasoning text you intend to post as the PR reply.
For each **Agree**, describe the fix. Then get approval before executing.

## Step 6 — Execute (after approval)

1. Check out the PR branch: `gh pr checkout <number> --repo <owner>/<repo>`.
2. **Disagreements** — post the reasoning as a reply on the PR:
   - Inline thread: `gh api repos/<owner>/<repo>/pulls/<number>/comments/<comment_id>/replies -f body='<reasoning>'`
   - Conversation comment: `gh api repos/<owner>/<repo>/issues/<number>/comments -f body='<reasoning>'` (quote what you're responding to).
3. **Agreements** — implement the minimal fix for each. Match surrounding code; keep diffs tight.
4. Run the affected tests before pushing (per project testing rules).
5. Commit and push to the PR branch. End the commit message with the required co-author trailer.

## Step 7 — Resolve fixed threads (after a successful push)

Only after the push succeeds, resolve the review thread for **each Agree comment whose code
was fixed**:

```bash
gh api graphql -f query='
mutation($id:ID!){ resolveReviewThread(input:{threadId:$id}){ thread{ isResolved } } }
' -F id=<threadId>
```

Do **not** resolve disagreement threads — leave those open for the human author to read your
reply and decide. Report back: what was fixed and resolved, what was disagreed and replied to,
and any comments left for human follow-up.

## Notes

- This is a Measurabl repo: respect functional-deference and confidentiality rules. PR replies
  are public to the repo — keep them professional and factual; don't paste confidential
  customer data into a comment.
- If the PR has no linked ticket, say so and proceed using the PR description alone.
- If you cannot determine agree/disagree for a comment with confidence, mark it for the user
  in the plan rather than guessing.
