# Codex Project Init

## Purpose

Orient a new Codex instance to this AgentOS repository without changing state.

## Prompt

```text
This is Kyle's AgentOS repository. Orient yourself before taking any action.

1. Confirm the workspace root and inspect the current Git branch and working-tree status. Do not change files.
2. Read and follow `AGENTS.md`.
3. Read `os/memory/README.md`, `os/memory/agentos-memory.md`, and `os/memory/working-memory.md`.
4. Read `os/agents/os-thought-partner.md`, `PLAYBOOK.md`, and `PROJECT_TRACKER.md`.
5. Give me a concise orientation covering:
   - the current branch and whether the worktree is clean;
   - the cross-device memory protocol;
   - the current AgentOS state and one relevant next action;
   - any stale context, ambiguity, or blocker you can verify.
6. Wait for my next task.

Treat committed `main` in `KyleGowen/AgentOS` as the shared durable AgentOS state. Chat history and built-in model memory are not shared. Do not run automations, access Gmail or Calendar, modify files, commit, push, or infer new work from the orientation alone.
```

## Expected Output

A compact, evidence-backed project orientation followed by a pause for Kyle's
next task.

## Notes

Use this after opening a fresh clone or existing checkout in Codex. `AGENTS.md`
is loaded automatically by Codex; this prompt ensures the intentional memory
layer and current project state are also read before work begins.
