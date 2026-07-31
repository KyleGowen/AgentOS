---
title: AI Coaching
domain: AI enablement and coaching for Measurabl teams
owner: Kyle Gowen
role: AI Coach and Business Operations Engineer
company: Measurabl, Inc.
status: Active; Tuesday office hours primary; unscheduled 1:1s as follow-up
sessions_completed: 11 as of 2026-06-30
last_updated: 2026-07-29
---

# AI Coaching

Working context for helping Kyle run the Measurabl AI Coaching program: office
hours, follow-up 1:1s, and the "get a colleague unstuck with AI" workflow.

The goal of this file is to make coaching help sharper: better intake questions,
faster and more accurate tool selection, repeatable recipes, and clear
boundaries without re-explaining the program every session.

Grounding rule:

- Never invent participants, sessions, action items, or outcomes.
- Never invent projects, events, examples, or current-event claims.
- Treat the named program records as the source of truth.
- If a real source is not available, ask Kyle instead of filling gaps.

## Program Metadata

| Field | Value |
|---|---|
| Owner / coach | Kyle Gowen |
| Sponsor | Kumar Brahnmath, CTO |
| Kyle's current role | Business Operations Engineer; Matt Richardson is technical lead |
| Primary audience | Mixed Measurabl colleagues; non-engineers come for help, engineers often join to hang out and explore ideas |
| Cadence | Weekly Tuesday office hours plus unscheduled 1:1 working sessions when office hours produce follow-up work |
| Program direction | Chat AI to supervised automation to agentic workflows |

Coaching principle:

- A good session leaves the person further along and understanding enough that
  they should not need to come back for the same problem.
- Kyle prefers to help inside the office-hours session when possible, then fall
  back to scheduling a 1:1 when the work needs more time.

Company context:

- Measurabl is a commercial real estate sustainability and ESG platform.
- Coachees' work often touches sustainability reporting, customer or account
  data, financial systems, GTM, security concerns, tooling requests, accuracy
  guidance, and internal operations.
- Assume general familiarity with CRE, ESG, and reporting concepts, but do not
  invent product, customer, contract, or methodology details.

## Project 7 Agent Readiness Target

For Project 7, the AI Office Hours Prep Agent is complete enough when it can
turn recent meeting transcription notes plus a current, verified topic into a
pre-meeting agenda Kyle can read in under five minutes.

The brief should help Kyle:

- Recall last week's topics and relevant prior-session threads.
- Change gears quickly and speak to colleagues' open projects.
- Bring one current-event discussion starter, with enough source context that
  Kyle knows what to read before raising it.
- Include simple confidence/source ratings without adding much length.
- Prepare during-session coaching guidance and questions, not just a static
  pre-meeting agenda.

If the agent lacks enough context, it may ask up to five focused follow-up
questions. It should optimize for quick turnaround because Kyle often reads the
brief right before office hours.

## Canonical Source Files

These files live in the AI Coaching workspace tracked through Claude Cowork, not
necessarily in this AgentOS repository.

| File | Purpose |
|---|---|
| `PROJECT_CONTEXT.md` | Program mission, stakeholders, and curriculum. |
| `Office-Hours-History.md` | Rolling log of sessions and cross-session signals. |
| `MANUAL_PROCESSES.md` | 194 processes across 8 departments, with AI opportunity tiers. |
| `AI-Tool-Repository.md` | Catalog of AI capability at Measurabl, published to Confluence. |
| `Prompt-Framework-5-Steps.md` | Prompting recipe used with coachees. |
| `GTM-AI-Use-Case-Map.md` | Riley's GTM prioritization by effort and impact. |
| `MSR-AI-Coaching-Timeline.html` | Program timeline. |

When preparing for a 1:1, check the relevant participant folder in the AI
Coaching workspace before assuming the current state.

## Source Authority Model

These source priorities fill current gaps until the AI Coaching workspace defines
more explicit authority rules.

| Question | Suggested authoritative source |
|---|---|
| Current program status, schedule, sponsor, and role context | `PROJECT_CONTEXT.md`, then `Office-Hours-History.md`, then Kyle |
| Tool recommendations and access guidance | `AI-Tool-Repository.md`, then current IT or licensing notes from Kyle |
| Participant and session history | `Office-Hours-History.md`, then the relevant participant folder and meeting transcription notes |
| Current events | Fresh source lookup at briefing time; if current lookup is not available, mark the topic as needing verification |
| Workflow candidates and department patterns | `MANUAL_PROCESSES.md`, then session notes and Kyle |

The AI Coaching workspace lives in Claude Cowork, referencing files on Kyle's
work laptop. AgentOS should keep only compact routing context and source
pointers, not copied source documents.

## Known Participants And Tracks

Only use these as known examples. Do not invent additional participants.

| Person | Role / track |
|---|---|
| Kumar Brahnmath | CTO, program sponsor; product AI and customer-data analytics track. |
| Alex Pasquale | AI Club co-lead; adoption and people side; runs the pulse survey. |
| Riley Donlin | GTM AI lead and CSM; RFP automation is her top 2026 priority. |
| Matt Richardson | Engineering / governance; owns the "no SDLC outside engineering" concern; technical lead for Kyle's Business Operations Engineer work. |
| Theresa Hill | Successfully completed AI coaching project; keep details in the AI Coaching workspace. |
| Cindy Leyh | Finance systems; invoice review, sales tax, and BAI bank-file automation; has both successful completed work and a failed Gemini attempt worth remembering at a high level. |
| Shaun Czubkowski | Advanced user; Obsidian and Claude workflows, Slack incident bot, design system. |
| Andrew Thomas | Field hardware; legacy JACE module diagnosis. |
| Brianna | Gems to Google Workspace connectivity and collections work. |

## Tool Landscape At Measurabl

Coaching help is only correct if it matches what people actually have access to.

| Tool | Who has it | What it does | Coaching notes |
|---|---|---|---|
| Gemini / Gems | Non-engineering, company-wide | Chat, doc analysis, custom Gems, Workspace integration | Current default starting point for many users, but hopefully temporary as Claude access expands; no agentic actions, no external integrations, static uploads. |
| Rovo | Non-engineering | Chat and analysis using Gemini backend | Limited; rarely the right build target. |
| Claude / Cowork / API | Engineering and a growing set of coachees | Agentic, reliable file and data work | Recommended build target for repeatable automation, including for non-engineers when available. Claude licenses are expanding and may become broadly available. Access can still be IT-gated. |
| Unblocked | Company-wide | Q&A over Confluence, Jira, and GitHub, surfaced in Slack | Publishing coaching docs to Confluence makes them findable here. |
| Confluence | Company-wide | Wiki and knowledge base | Home for the AI Tool Repository and coaching materials. |
| Google Workspace | Company-wide | Gmail, Docs, Sheets, Slides | Gems integrate here; enterprise tier tracked in IT-436. |
| Salesforce, HubSpot, Jira, Zoom, Snowflake, Slack | Varies | Systems of record and data sources | Common data endpoints in "move data" requests. |

Access friction is a first-class issue. Sometimes the correct tool is clear,
usually Claude, but the real blocker is IT access or governance approval. When
recommending a tool the person does not have, the next step should be a concrete
IT help-desk ticket, governance check, and working session, not abstract debate.

## Office-Hours Intake Questions

Open unfamiliar requests with these before recommending a tool or workflow.
For pre-office-hours briefs, prioritize meeting transcription notes and ask no
more than five follow-up questions before producing a useful draft.

1. What is the actual task, end to end? Walk through how it is done today, step
   by step.
2. How often does it happen, and how long does it take?
3. Where does the data start and end? Identify the source system or file, and
   where the result needs to land.
4. Does it touch customer data? If yes, check the customer-data and
   third-party-LLM constraints before going further.
5. What does "done" look like? Ask for a concrete example of a good output.
6. What has already been tried, and where did it break?
7. What tools does the person actually have access to right now?
8. Who else needs to see, approve, or rely on this?

The intake is itself part of the coaching. Narrating why these questions matter
helps the person scope their own next problem.

## Prep Brief Shape

The AI Office Hours Prep Agent should produce a brief Kyle can read in under
five minutes.

Always include:

1. Last week's topics.
2. Relevant previous-week or prior-session threads.
3. Colleague open projects to remember.
4. Questions to ask attendees.
5. Tool-choice and governance notes.
6. One current-event discussion starter with source note and read-ahead prompt.
7. Simple confidence/source rating for each topic.

Use prep notes, not scripts. Kyle does not need suggested words to say unless he
asks for them.

## During-Session Guidance

During office hours, bias toward helping in the session. If the work is too
large, sensitive, access-blocked, or too detailed for the group setting, suggest
a follow-up 1:1.

The agent's during-session guidance should be:

- Open and curious.
- Non-prescriptive.
- Solution-oriented.
- Willing to make more time when the problem deserves it.

Avoid patronizing tones and avoid implying the colleague should already know or
already have something.

## Tool-Selection Rules

- Repeatable file or data execution work should usually route to Claude.
- Finance automation candidates have consistently routed to Claude rather than
  Gemini, including invoice review, sales tax, and BAI bank-file work.
- Live data, cited sources, and quick lookups should usually route to Gemini or
  another chat tool with current information and citations.
- Knowledge Q&A over a fixed body of documents should usually become a Gem, or
  use Unblocked if the content lives in Confluence.
- Anything agentic that sends, writes to a system, or runs unattended needs
  Claude, a human-in-the-loop review step, and Phase 2 or Phase 3 maturity.
- Non-engineers should use Cowork rather than Code for agentic work because of
  sandbox and safety concerns.
- When correctness matters and the person has Claude, prefer Claude over Gemini
  for repeatable workflows because Gemini has shown instability on some file and
  data tasks.
- The most common coaching needs right now are tool choice and governance.
- Current recurring request types include security concerns, tool requests, and
  accuracy guidance.

Decision shortcut:

- Repeatable execution: Claude.
- Lookup with citations: Gemini or another current chat tool.
- Q&A over fixed docs: Gem or Unblocked.
- Acting on a system: Claude plus human review, Phase 2 or later.

## Vague Request To Useful Workflow

Common request shapes and how to turn them into useful coaching sessions:

| Vague request | Coaching move |
|---|---|
| "Can AI help me with this broad area?" | Run intake. Pick the single highest-frequency, best-defined subtask. Build that as the teaching example. |
| "I want to automate my whole job." | Reframe to one process with clear inputs, outputs, and a human review step. Use `MANUAL_PROCESSES.md` tiers to pick a Tier 1 candidate. |
| "Move data from X to Y." | Use the spreadsheet and data movement recipes below. Usually export, transform, summarize, deliver, and review. |
| "Make the AI stop making things up." | Design the prompt or Gem with explicit declined features, known-false inputs, and a cite-or-flag rule. |
| "My Gem will not share or connect to Drive." | Treat this as known friction. Check Workspace sharing settings, remember Gems cannot point at live Drive folders, and escalate activation issues to IT-436. |
| "I want to build an autonomous agent." | Channel the ambition into a sandbox with hard guardrails. Introduce human-in-the-loop first. |

## Spreadsheet And Data-Movement Recipes

Default pattern:

1. Export.
2. Clean.
3. Transform.
4. Summarize.
5. Deliver.
6. Review checkpoint.

Common recipes:

- System export to readable summary: pull CSV or export from Salesforce, Jira,
  HubSpot, or similar; load into Claude or a lighter Gem; produce a structured
  summary or status rollup.
- Two sources to one reconciled sheet: combine a system export with a reference
  sheet such as tax rates or mappings; join, transform, and output a reviewed
  sheet.
- Recurring debrief to spreadsheet and Slack post: turn structured data into a
  summary table and a Slack-ready draft.
- Messy file to clean spreadsheet: use spreadsheet tooling for real `.xlsx`
  deliverables with formulas, formatting, charts, and recalculation; use PDF
  extraction tooling when the source is a PDF.

Guardrails:

- Confirm source columns exist before building.
- Look at a sample before assuming export shape.
- Strip or avoid customer PII in anything reusable.
- Keep sensitive data out of URLs, logs, and broadly shared docs.

## Debrief And Slack Summary Pattern

1. Take the raw data, such as call notes, an export, or a meeting doc.
2. Produce a tight structured summary with decisions, action items, owners, due
   dates, and open threads.
3. Format for Slack using short sections, bold labels, and no walls of text.
4. Draft for human review before posting.

Human review before posting is both a governance rule and a trust-builder.

## Boundaries For Non-Engineering Automation

- Customer data and third-party LLMs require caution. Newer customer contracts
  may prohibit customer data from being used to train third-party models.
- Before pointing any tool at customer data, confirm it is safe. Check the AI
  Tool Repository's "Safe with customer data?" column and loop in Matt
  Richardson's team on contract language when needed.
- When unsure, treat customer data as not safe until confirmed.
- Never give agents or AI systems secrets, credit card information, payment
  information, or similar sensitive credentials or financial data.
- Human-in-the-loop is mandatory for anything that writes to a system of record,
  sends external communications, or runs unattended.
- Prototyping should happen in Measurabl-owned sandboxes with guardrails, not
  with production data or real customer recordings.
- The governance gap is real. There are not yet SDLC controls for
  non-engineering AI use, so lightweight "test, approve, deploy, monitor"
  discipline is part of what coaching teaches.
- For solutions others will rely on, use the SRB / SDR path through Measurabl AI
  Solution Builder.
- Do not bake account names, contract values, usage metrics, or operational data
  into templates or examples.
- Do not use made-up examples in coaching materials or reusable prompts.
- Escalate rather than improvise on pricing or contract terms, legal language,
  customer-facing communications, and feature or roadmap claims.
- Involve Matt Richardson's team, IT, or the relevant governance owner when the
  work needs tool access, governance approval, or security review.

Outputs that need human review before use include external communications,
system-of-record writes, customer-facing material, security or governance
recommendations, reusable workflow templates, and anything that changes access,
approval, payment, or operational data.

## Prompting Recipe

The five-step framework taught in the program works for Gemini and Claude alike.

1. Context: topic, why, and who it is for.
2. Role: the persona or expertise to adopt.
3. Task: one clear, specific action verb.
4. Examples: show a correct example, and optionally a wrong example.
5. Constraints and format: length, tone, structure, and output format.

Full guide lives in `Prompt-Framework-5-Steps.md`.

## Curriculum Arc

Use the arc to calibrate advice. Do not give a Phase 1 user a Phase 3 answer.

| Phase | Focus |
|---|---|
| Phase 1 | Foundation: AI 101, prompting that works, first Gem, role-based use cases. |
| Phase 2 | Supervised automation: human-in-the-loop, simple agents with approval steps, Cowork intro, governance basics. |
| Phase 3 | Agentic workflows: real pipelines for specific processes, process-selection framework, SDLC for business users. |

## Successful Outcome Shape

Grounded examples of coaching that worked. Use these as models, not scripts.

- Finance automation to Claude, with a real next step: a recurring manual file
  or template task gets scoped, the correct tool is identified, and the session
  ends with a concrete unblock such as an IT ticket for access and a booked
  working session.
- Gem for repeatable knowledge work: a CSM email digest or similar workflow
  built with declined-features awareness and cite-or-flag rules.
- Ambition channeled safely: an autonomous-agent idea routed into a guardrailed
  sandbox instead of being shut down.

Common thread:

- The person leaves with a working direction and the reasoning to handle the
  next variant themselves.

## Handy Skills And Assets

| Asset | Use |
|---|---|
| `add-office-hour-notes` skill | Processes a session's Gemini Google Doc and updates program files in one pass. Trigger when a Doc URL and office-hours context appear together. |
| `AI-Tool-Repository.md` | Catalog for "what AI do I already have for X?" |
| `MANUAL_PROCESSES.md` | Menu for picking automation candidates across departments. |
| `Office-Hours-History.md` | Cross-session signals to check before a session. |

## Maintenance Notes

- Refresh this file weekly after the office-hours session.
- Update tool-selection rules and cross-session signals as the program evolves.
- Re-sync stakeholder and status facts from `PROJECT_CONTEXT.md` and
  `Office-Hours-History.md`.
- Keep detailed participant progress in the AI Coaching workspace, not in this
  repo, unless Kyle intentionally promotes a summary here.
- Promote changes here when they affect program operations, schedule, key
  players, Kyle's immediate team structure, durable tool guidance, or durable
  boundaries.
- Keep names when they help Kyle prepare, but avoid expanding this file beyond
  the recommended agent context size.
