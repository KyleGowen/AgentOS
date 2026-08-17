# Agents

This folder tracks agent definitions, roles, handoffs, and evaluation notes.

## Active Agents

| Agent | Job | Status |
|---|---|---|
| `os-thought-partner.md` | Translate AgentOS course projects into this Codex setup and keep the system coherent as it grows. | Active |
| `ai-office-hours-prep-agent.md` | Prepare source-grounded agenda briefs before weekly AI office hours. | Active v1 |
| `ai-office-hours-follow-up-agent.md` | Turn completed AI office-hours sessions into source-grounded follow-up packets. | Active v1 |
| `pr-review-prep-agent.md` | Find Measurabl PRs where Kyle is tagged and prepare compact review-prep digests. | Active v1 |
| `sdge-energy-agent.md` | Maintain the policy-scoped SDGE Energy Use Alert ledger and dashboard. | Active |

## Notes

- Keep agents single-responsibility when possible.
- Add project-specific agents here as they become real.
- The OS Thought Partner has a portable ChatGPT Project companion in
  `os-thought-partner-chatgpt-project.md`; keep it aligned with the main agent
  definition and repository memory rules.

## New Specialized-Agent Checklist

AgentOS-native agents inherit the root `AGENTS.md`; they do not inherit every
AgentOS document or another agent's data by default. Before registering one,
make sure its canonical definition includes:

- a single, distinct job and clear invocation triggers;
- its required sources, beginning with root `AGENTS.md` and the definition
  itself;
- the specific context files and durable state it may use, plus any excluded
  context that would be unsafe or irrelevant;
- privacy, authorization, and mutation boundaries;
- verification and reporting expectations; and
- its relationship or explicit non-relationship to other agents.

If the agent has a Codex profile, keep it as a thin launcher that points to
the canonical definition. Keep schedules in automation policy and repeatable
procedures in skills, so one source remains authoritative for each concern.
