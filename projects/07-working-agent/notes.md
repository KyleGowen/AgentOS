# Project 07: Working Agent

Status: In progress

Course page: <https://aidbagentos.ai/projects>

## Goal

Build a working AI Office Hours Prep Agent with its own identity, context, and
skills, inheriting Kyle's global AgentOS identity, preferences, memory, and
verification rules.

## Candidate Agent

AI Office Hours Prep Agent.

Files:

- `os/agents/ai-office-hours-prep-agent.md`
- `os/context/ai-coaching.md`
- `os/context/identity.md`
- `os/context/current-projects.md`

## Completion Target

The agent is complete enough for Project 07 when it can turn meeting
transcription notes, previous-session context, colleague open projects, and one
verified current-event discussion starter into a pre-meeting agenda Kyle can
read in under five minutes.

## Interview Notes

Kyle wants the agent to:

- Prepare briefs from previous sessions and one current-events topic Kyle may
  need to read before office hours.
- Help Kyle change gears quickly and speak to colleagues' open projects.
- Keep Tuesday office hours as the main format.
- Track and brief unscheduled 1:1s when they come out of office hours.
- Accept meeting transcription notes as the primary input.
- Ask no more than five follow-up questions before producing a draft.
- Include during-session coaching guidance.
- Stay open, curious, non-prescriptive, solution-oriented, and willing to give
  more time.
- Avoid patronizing tones.
- Bias toward helping during office hours and fall back to 1:1s when needed.
- Focus especially on tool choice and governance.
- Include last week's topics, relevant previous-week topics, colleague open
  projects, a current-event discussion starter, simple confidence/source
  ratings, and questions to ask attendees.

Hard boundaries:

- Never make up sessions, people, projects, events, examples, or current-event
  claims.
- Never put secrets, credit card information, payment information, or similar
  sensitive data into agents or AI systems.
- Do not fill gaps with invented data.

## Source Authority Suggestions

- Program status: `PROJECT_CONTEXT.md`, then `Office-Hours-History.md`, then
  Kyle.
- Tool recommendations: `AI-Tool-Repository.md`, then current IT or licensing
  notes from Kyle.
- Participant and session history: `Office-Hours-History.md`, then relevant
  participant folders and meeting transcription notes.
- Current events: fresh source lookup at briefing time.

## Evidence To Capture Before Completion

- Updated agent file.
- Updated AI coaching context file.
- Real test prompt and output.
- Project notes.
- Playbook update.
- Memory update.
