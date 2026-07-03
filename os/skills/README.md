# Skills

This folder tracks reusable skills created during the course.

Codex-executable repo skills live in `.agents/skills/`. This `os/skills/`
folder is the AgentOS catalog for documenting triggers, process, outputs, and
verification.

Use `catalog.md` to track reusable skills in their native tool format and their
project-local Codex translations. Preserve native skill files under
`native/<tool>/<skill-name>/` before adapting them.

For each skill, capture:

- Trigger: when to use it.
- Inputs: required context or files.
- Process: steps the agent should follow.
- Output: expected artifact or decision.
- Verification: how to check the result.

## `/complete NN`

- Codex location: `.agents/skills/complete/`
- Trigger: `/complete NN`, where `NN` is a two-digit AgentOS project number.
- Inputs: Existing `PROJECT_TRACKER.md` entry and matching project notes folder.
- Process: Mark the project complete, mirror status into docs, validate the skill, then commit and push.
- Output: Updated tracker, README Project Index, project notes, and any related playbook sections.
- Verification: Run the skill validator and dry-run invalid or unknown inputs before committing.

## `/ticket-to-pr`

- Codex location: `.agents/skills/ticket-to-pr/`
- Native archive: `os/skills/native/claude/ticket-to-pr/SKILL.md`
- Trigger: a Measurabl Jira ticket id plus a request to take it through development to a draft PR.
- Inputs: Jira ticket content, related tickets, repository code, tests, GitHub access, and any user-provided constraints.
- Process: Research ticket, research code, plan for approval, implement, test, branch/commit/push, and open a draft PR.
- Output: Draft PR URL, implementation summary, test results, and review flags.
- Verification: Validate the Codex skill and forward-test on a real Measurabl ticket.

## `/resolve-pr-comments`

- Codex location: `.agents/skills/resolve-pr-comments/`
- Native archive: `os/skills/native/claude/resolve-pr-comments/SKILL.md`
- Trigger: a GitHub PR URL or `owner/repo#number` plus a request to address review comments.
- Inputs: PR metadata, linked Jira ticket, review comments across all GitHub surfaces, thread ids, repository code, tests, and user approval.
- Process: Read PR, read linked Jira ticket, collect comments, triage agree/disagree/informational, plan for approval, fix or reply, commit/push, and resolve fixed threads.
- Output: Pushed fixes, PR replies, resolved fixed threads, test results, and follow-up notes.
- Verification: Validate the Codex skill and forward-test on a real Measurabl PR.

## Excelsior Cursor Skills

- Codex locations: `.agents/skills/add-card/`, `.agents/skills/add-community-deck/`, `.agents/skills/pdf-to-png/`, `.agents/skills/ship/`, `.agents/skills/start/`, `.agents/skills/start-aws-db-tunnel/`
- Native archives: `os/skills/native/cursor/<skill-name>/SKILL.md`
- Trigger: Excelsior-specific Cursor slash commands or natural-language equivalents.
- Inputs: Excelsior repo files, local dev services, images/PDFs/deck JSON, AWS/GitHub/npm tooling depending on the skill.
- Process: Preserve native Cursor skill text, translate to Codex `SKILL.md` frontmatter/body, validate the Codex skill, and mature through real Excelsior use.
- Output: Tool-specific Excelsior workflow results such as catalog migrations, community deck imports, image conversions, dev stack health, release pushes, or DB tunnels.
- Verification: Validate each Codex skill and forward-test in the Excelsior repo before marking mature.
