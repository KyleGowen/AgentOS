# Skills

This folder tracks reusable skills created during the course.

For each skill, capture:

- Trigger: when to use it.
- Inputs: required context or files.
- Process: steps the agent should follow.
- Output: expected artifact or decision.
- Verification: how to check the result.

## `/complete NN`

- Trigger: `/complete NN`, where `NN` is a two-digit AgentOS project number.
- Inputs: Existing `PROJECT_TRACKER.md` entry and matching project notes folder.
- Process: Mark the project complete, mirror status into docs, validate the skill, then commit and push.
- Output: Updated tracker, README Project Index, project notes, and any related playbook sections.
- Verification: Run the skill validator and dry-run invalid or unknown inputs before committing.
