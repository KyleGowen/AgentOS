# Memory

This folder is the intentional memory layer for AgentOS.

Codex built-in memories are enabled for ambient recall, but important AgentOS memory should live here because these files are reviewable, portable, and editable.

## How This Memory Works

Use this as a lightweight notebook, not an encyclopedia.

- Update memory at the end of a meaningful task, project shift, or planning session.
- Keep working memory short and aggressively compacted.
- Move durable items into the right persistent file.
- Include links, ticket IDs, PRs, document names, or source notes when available.
- Keep work and home project context separated.
- Do not store secrets, private customer details, raw Slack excerpts, full private ticket descriptions, or unnecessary personal data.

## Cross-device Memory Protocol

The `main` branch of `KyleGowen/AgentOS` is the shared, durable memory source
for every signed-in Codex and ChatGPT instance.

- GitHub shares only committed repository files. ChatGPT/Codex chat history,
  hidden conversation context, and built-in model memory are not shared
  memory.
- On Codex, open or clone this repository, read `AGENTS.md`, then read the
  relevant files under `os/memory/` before relying on prior decisions.
- On ChatGPT, use the `AgentOS` Project with the connected GitHub app and
  explicitly ask it to read the relevant repository files.
- To make new knowledge portable, update the correct context or memory file,
  then commit and push it from Codex. A ChatGPT conclusion is provisional until
  it has been recorded in the repository.
- Use the smallest appropriate file: active state in `working-memory.md`,
  durable choices in `decisions.md`, recurring behavior in `patterns.md`, and
  system-wide rules in `agentos-memory.md`.

## Files

| File | Purpose |
|---|---|
| `working-memory.md` | Current state, next actions, blockers, and temporary context. |
| `decisions.md` | Durable decisions with context, reason, and evidence. |
| `patterns.md` | Repeated workflows and preferences that may become skills or automations. |
| `project-history.md` | Compact milestones and meaningful outcomes. |
| `people-and-collaboration.md` | Useful collaboration context, using roles or first names when appropriate. |
| `lessons-learned.md` | Durable pitfalls, surprises, and corrections. |
| `work-memory.md` | Sanitized Measurabl work memory. |
| `home-memory.md` | Personal project memory. |
| `agentos-memory.md` | AgentOS course and system-building memory. |

## Working Memory Rules

`working-memory.md` should answer: "What does the next session need to know to continue?"

Keep:

- Current project state.
- Next action.
- Active blockers or open questions.
- Context likely to matter in the next few sessions.

Move or remove:

- Decisions -> `decisions.md`.
- Repeated workflows -> `patterns.md`.
- Meaningful outcomes -> `project-history.md`.
- Mistakes or durable warnings -> `lessons-learned.md`.
- Stale notes -> delete after promotion or when no longer useful.

## Persistent Memory Rules

Persistent memory should hold stable context that should influence future work.

Good memory:

- Durable preferences.
- Repeated workflows.
- Project milestones.
- Important decisions.
- Known risks and pitfalls.
- Sanitized project summaries.
- Source pointers that help future verification.

Poor memory:

- Secrets.
- Raw private messages.
- Full private ticket descriptions.
- Customer-specific details that do not belong in this repo.
- One-off chatter.
- Stale active context.

## People Memory Rules

People memory is allowed when it helps collaboration.

- Prefer roles, stakeholder groups, first names, or private aliases.
- Store collaboration preferences, responsibilities, and handoff needs.
- Avoid unnecessary identifying details.
- Do not store sensitive personal information.

## Compaction

Compact aggressively.

When working memory grows, ask:

1. Is this still active?
2. Is this durable enough to promote?
3. Is there a source system that should remain the source of truth?
4. Would future Kyle be annoyed if this disappeared?

If the answer is no, remove it.

## Update Checklist

At the end of a meaningful task:

- Update `working-memory.md` with current state and next action.
- Add any durable choice to `decisions.md`.
- Add repeated behavior to `patterns.md`.
- Add meaningful outcomes to `project-history.md`.
- Add durable warnings to `lessons-learned.md`.
- Keep work and home context in their domain files.
