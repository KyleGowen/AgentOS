---
name: complete
description: Mark AgentOS course projects complete from prompts like "/complete 02", "$complete 02", or "mark AgentOS project NN complete". Use this skill when updating the project tracker, project notes, README project index, and related AgentOS documentation after a project at https://aidbagentos.ai/projects has been finished.
---

# Complete

## Workflow

Use this skill only from the AgentOS repository root.

1. Parse the request for exactly one two-digit project number, such as `02`.
2. Run `python3 .agents/skills/complete/scripts/complete_project.py NN`.
3. If the script reports an unknown project, stop and tell the user which tracker entry is missing. Do not create unknown project stubs.
4. Review `git diff -- PROJECT_TRACKER.md README.md PLAYBOOK.md os/skills/README.md projects`.
5. Run `python3 /Users/kyle/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/complete`.
6. Run a focused dry-run check for invalid and unknown inputs:
   - `python3 .agents/skills/complete/scripts/complete_project.py 7 --dry-run`
   - `python3 .agents/skills/complete/scripts/complete_project.py 13 --dry-run`
7. If validation passes, stage the changed files, commit with `Complete AgentOS project NN`, and push the current branch to `origin`.

## Behavior

- The canonical tracker is `PROJECT_TRACKER.md`.
- If the tracker is missing, the script creates it from known AgentOS course projects and local project folders.
- The script accepts only exactly two digits.
- The script updates the matching `projects/NN-*/notes.md` status to `Complete` and adds a completion note if needed.
- The script mirrors tracker status into the README Project Index.
- The script updates `PLAYBOOK.md` only for project completions that directly affect playbook sections.
- Completion is idempotent: running the same valid project again should not duplicate completion notes.

## Script

Use `scripts/complete_project.py` for all tracker and documentation updates. Use `--dry-run` when checking behavior without writing files.
