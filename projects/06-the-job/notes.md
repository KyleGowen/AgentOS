# Project 06: The Job

Status: Complete

Completed: 2026-07-05

Historical note: Project 06 selected the AI Office Hours Prep Agent as the
first job definition. On 2026-08-16, Kyle selected the already-operating
ThraxOS specialist as the Project 07 build. This preserves the Project 06
artifact while allowing Project 07 to use the stronger working-agent evidence.

Course page: <https://aidbagentos.ai/projects>

## Goal

Create a one-page job description for the first agent that runs on this
AgentOS.

## Inputs

- Course instructions from the Project 06 screenshot.
- `os/agents/os-thought-partner.md`
- `os/context/ai-coaching.md`
- `os/context/current-projects.md`
- Kyle's planning choices from this session.

## Build Notes

### Decisions

- The first job is the AI Office Hours Prep Agent.
- Keep the agent single-responsibility: pre-office-hours preparation only.
- Scope v1 to weekly Tuesday AI office hours.
- Require user-provided current inputs before producing a final agenda brief.
- Optimize the output for a concise agenda brief.
- Use source grounding as the trust gate.
- Exclude unsourced agenda items instead of listing them as low confidence.
- Exclude follow-up drafting, post-session notes, and external-system updates.
- Document the future weekly schedule as an automation candidate, but do not
  implement automation in Project 06.

### Prompts

```text
Help me create an AI Office Hours Prep Agent as my Project 06 job. It should
prepare a source-grounded agenda brief before weekly office hours, ask enough
follow-up questions to make the context trustworthy, and stay out of follow-up
drafting or post-session work.
```

### Output

- `os/agents/ai-office-hours-prep-agent.md`

## Evidence

- Files:
  - `os/agents/ai-office-hours-prep-agent.md`
  - `os/agents/README.md`
  - `os/agents/os-thought-partner.md`
  - `PLAYBOOK.md`
  - `projects/06-the-job/notes.md`
  - `os/memory/agentos-memory.md`
  - `os/memory/decisions.md`
  - `os/memory/patterns.md`

## Reflection

What worked:

- A single-responsibility pre-session agent was easier to define and verify than
  a broader AI coaching assistant.
- Separating prep from follow-up made the agent boundary clearer.

What I would improve:

- Add a future follow-up agent for post-session notes, action items, and draft
  communications.

What should be added to the playbook:

- The AI Office Hours Prep Agent should be listed as a real AgentOS job and a
  future automation candidate.
