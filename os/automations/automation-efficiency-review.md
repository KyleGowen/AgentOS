# Automation Efficiency Review

## Purpose

Review recent and upcoming scheduled AgentOS automation runs for ways to reduce unnecessary work, lower token usage, and improve runner efficiency without weakening safety or verification.

This file is the harness-neutral source of truth. A scheduler, agent runner, shell script, or Codex automation can implement it as long as it follows the contract below.

## Schedule

Run every morning at 6:30 AM Pacific time, observing PST/PDT.

## Scope

Review all scheduled AgentOS automations, including active Codex cron jobs and documented future automation candidates.

Known starting points:

| Source | Purpose |
|---|---|
| `PLAYBOOK.md` | Automation inventory, status, and documented future candidates. |
| `os/automations/` | Harness-neutral automation policies and runner contracts. |
| `.agents/skills/` | Codex-executable skills used by automations. |
| `$CODEX_HOME/automations/*/automation.toml` | Codex scheduler prompts, schedule, model, reasoning effort, and status. |
| `$CODEX_HOME/automations/*/memory.md` | Runner-owned state and recent run summaries when present. |
| `os/automation-output/` | Replaceable output artifacts from scheduled runs. |

## Runner Contract

1. Build the current automation inventory from `PLAYBOOK.md`, `os/automations/`, and the Codex automation config directory.
2. Include both active scheduled automations and documented future automation candidates.
3. For each active scheduled automation, inspect the most recent runner memory and output artifacts that are available.
4. For each future automation candidate, inspect the documented agent/spec to identify likely efficiency risks before the task is scheduled.
5. Compare each automation's source-of-truth spec with its scheduler prompt and schedule.
6. Identify drift, duplicated instructions, unnecessarily broad searches, repeated full reads, missing ledgers/caches, excessive reasoning effort, oversized reports, redundant verification, and stale future-candidate assumptions.
7. Preserve safety gates. Do not recommend token savings that remove required source checks, privacy boundaries, read-only restrictions, RSVP safeguards, or ambiguity handling.
8. Group recommendations by skill or automation, using the skill name when one exists and the automation name otherwise.
9. Mark each recommendation as one of:
   - `Prompt trim`
   - `State/cache`
   - `Search narrowing`
   - `Schedule/config`
   - `Output compaction`
   - `Spec drift`
   - `Skill refactor`
10. Include a short rationale, expected token/effort impact, risk, and the exact file or scheduler config to change.
11. End with a proposed approval checklist. Do not make changes during this review run.

## Report Format

Print a compact digest in Markdown:

```markdown
# Automation Efficiency Digest

Run date: YYYY-MM-DD

## Summary

- Scheduled automations reviewed: N
- Future candidates reviewed: N
- Recommended changes: N
- Highest-impact recommendation: ...

## Skill Recommendations

### `skill-or-automation-name`

| Type | Recommendation | Expected impact | Risk | Change target |
|---|---|---|---|---|
| Prompt trim | ... | ... | Low/Medium/High | `path-or-config-id` |

## Approval Checklist

- [ ] Apply low-risk prompt trims.
- [ ] Apply state/cache changes.
- [ ] Apply schedule/config fixes.
- [ ] Open a branch, commit, and push approved changes.
```

Suggested scheduled-run artifact:

| Artifact | Purpose |
|---|---|
| `os/automation-output/automation-efficiency-review/latest.md` | Latest optimization digest when file output is available. |

## Safety Rules

- Review only. Do not edit repository files, scheduler configs, email, calendar events, marketplace state, or external systems.
- Do not sign in to marketplaces or perform marketplace actions.
- Do not read private message bodies unless the reviewed automation's own policy already requires it for a specific active run inspection.
- Do not store secrets, private message content, raw customer details, cookies, API keys, or long raw logs in the digest.
- Do not propose broad deletion of verification steps; recommend narrower or cheaper verification instead.
- If evidence is missing, report the gap instead of guessing.
- Only implement changes later after Kyle explicitly approves them.

## Implementation Notes

- Current Codex automation ID: `automation-efficiency-review`.
- Codex implementation should run in `/Users/kyle/Documents/AgentOS`.
- Prefer low or medium reasoning. Increase reasoning only if the recent run evidence is ambiguous or many automations changed.
- Treat this file as policy/config, not generated output.
