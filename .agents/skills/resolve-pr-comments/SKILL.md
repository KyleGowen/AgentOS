---
name: resolve-pr-comments
description: End-to-end Measurabl pull request review-comment resolution workflow. Use when the user gives Codex a GitHub PR URL or owner/repo#number and wants every human and bot review comment collected, triaged into agree/disagree, planned for approval, then after approval fixed or replied to, committed, pushed, and resolved where appropriate.
---

# Resolve PR Comments

Use this workflow to handle review feedback on a pull request from triage
through pushed fixes. The input is a PR link such as
`https://github.com/Measurabl/wizard/pull/1819` or `owner/repo#number`.

## Outcome

1. Read every open human and AI/bot comment surface on the PR.
2. Triage each actionable comment into Agree, Disagree, or Informational.
3. Produce a plan with an agree/disagree chart for user approval.
4. After approval, fix agreements, reply to disagreements, commit and push, and resolve only fixed review threads.

Do not skip the plan-approval gate. Posting replies, pushing code, and resolving
threads are outward-facing actions.

## Step 1: Read The PR

Parse `owner`, `repo`, and `number` from the PR link.

Use the available GitHub connector, `gh`, or both to gather:

- PR title, body, state, URL, author, files, base branch, and head branch.
- PR diff.
- Existing checks when relevant.

With `gh`, useful commands include:

```bash
gh pr view <number> --repo <owner>/<repo> --json title,body,headRefName,baseRefName,state,url,author,files
gh pr diff <number> --repo <owner>/<repo>
```

Note the head branch. Check it out only after the user approves the plan.

## Step 2: Read The Linked Jira Ticket

Extract the ticket key from the branch name, PR title, or PR body, such as
`WILD-1234` or `BSOD-3099`. If a Jira/Atlassian connector is available, read the
ticket description, acceptance criteria, status, and relevant parent or linked
issues.

Use the ticket to ground triage. A comment asking for behavior that the ticket
explicitly excludes is likely Disagree. A comment pointing at unmet acceptance
criteria is likely Agree. If no linked ticket is found, say so and proceed using
the PR description and code.

## Step 3: Collect Every Comment

Gather all comment surfaces, including bot authors such as Copilot, CodeRabbit,
Claude, and similar tools.

With `gh`, collect:

```bash
gh api repos/<owner>/<repo>/pulls/<number>/comments --paginate
gh api repos/<owner>/<repo>/pulls/<number>/reviews --paginate
gh api repos/<owner>/<repo>/issues/<number>/comments --paginate
```

Use GraphQL when thread ids, resolution state, or inline reply context matters:

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

Skip already resolved threads unless the user asks to revisit them.

## Step 4: Triage Comments

For every open actionable comment, read the actual code at the referenced
location and weigh it against the ticket, PR intent, and codebase conventions.
Be a genuine reviewer; AI bot comments can be wrong, stale, or out of scope.

- Agree: the comment identifies a real, in-scope change worth making.
- Disagree: the comment is incorrect, already handled, out of scope, a false positive, or conflicts with project conventions.
- Informational: the comment requests no change and needs no reply or code action.

Every disagreement needs concrete reasoning that can be posted professionally on
the PR. Cite code, ticket language, existing tests, or conventions.

## Step 5: Produce The Plan

Always present a plan for approval before editing, replying, pushing, or
resolving threads. Include a chart like:

| # | Author | Location | Comment | Verdict | Action |
|---|---|---|---|---|---|
| 1 | coderabbitai | `Foo.java:42` | Null-check `bar` | Agree | Add guard before dereference |
| 2 | alice | `Baz.java:10` | Use a `Set` here | Disagree | Order matters; reply with reasoning |

For each Disagree, include the full reply text you intend to post. For each
Agree, describe the fix. Mark uncertain items for user decision instead of
guessing.

## Step 6: Execute After Approval

1. Check out the PR branch, for example `gh pr checkout <number> --repo <owner>/<repo>`.
2. Post disagreement replies:
   - Inline thread: `gh api repos/<owner>/<repo>/pulls/<number>/comments/<comment_id>/replies -f body='<reasoning>'`
   - Conversation comment: `gh api repos/<owner>/<repo>/issues/<number>/comments -f body='<reasoning>'`, quoting the comment being answered.
3. Implement minimal fixes for agreed comments. Match surrounding code and keep diffs tight.
4. Run affected tests according to project rules. Report real summary lines.
5. Commit only intended files and include required project trailers.
6. Push to the PR branch.

## Step 7: Resolve Fixed Threads

Only after a successful push, resolve review threads for Agree comments whose
code was fixed.

```bash
gh api graphql -f query='
mutation($id:ID!){ resolveReviewThread(input:{threadId:$id}){ thread{ isResolved } } }
' -F id=<threadId>
```

Do not resolve disagreement threads. Leave them open for the human author to
read and decide.

## Done

Report what was fixed and resolved, what was disagreed with and replied to, test
results, pushed commit, and any comments left for human follow-up.

Keep PR replies professional and factual. Do not paste confidential customer
data or operational details into PR comments.
