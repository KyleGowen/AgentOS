# OS Thought Partner

## Job

Help translate AgentOS course projects into my Codex setup and keep the system coherent as it grows.

## Tool Foundation

This AgentOS is being built in Codex.

| Field | Value |
|---|---|
| Tool | Codex |
| Version | 26.623.81905 |
| Release date | 2026-07-01 |
| Install state | Fresh install |
| Custom configuration | None yet |

Because this is a fresh Codex install, assume no custom agents, skills, memories, MCP servers, automations, or local conventions exist unless they are documented in this repository.

## Cross-device access

The durable source of truth is the GitHub repository:
<https://github.com/KyleGowen/AgentOS>.

Use the GitHub repository as the portable AgentOS state across all signed-in
Codex and ChatGPT devices. Connect the ChatGPT GitHub app to
`KyleGowen/AgentOS` so ChatGPT can query the live repository rather than
relying on uploaded snapshots. A ChatGPT Project named **AgentOS** is a useful
portable conversation surface, but the repository—not chat history or built-in
model memory—is the shared source of truth. The project instructions are
captured in `os/agents/os-thought-partner-chatgpt-project.md`.

Use uploaded files only as a fallback when GitHub access is unavailable. Put
durable shared memory in the reviewable files under `os/memory/`, then commit
and push it. Use Codex with the local folder for edits, tests, git history, and
other filesystem work. Do not treat a ChatGPT Project or a Codex chat as a
replacement for the GitHub repository.

For a newly opened Codex checkout, use
`prompts/codex-project-init.md` to load the shared memory protocol and current
AgentOS state before accepting substantive work.

One-time setup in ChatGPT:

1. In **Settings → Apps**, connect GitHub and authorize the
   `KyleGowen/AgentOS` repository.
2. Create a new ChatGPT Project named `AgentOS / OS Thought Partner`.
3. Open Project settings and paste the contents of
   `os/agents/os-thought-partner-chatgpt-project.md` into Project instructions.
4. In the first project chat, add GitHub with `@GitHub` or the **+ → More** tools menu.
5. Start with: `Use the connected GitHub repository KyleGowen/AgentOS as the live source. Summarize the current AgentOS state, identify stale or missing context, and wait for my next task.`

ChatGPT Projects can keep their own chats, files, and instructions together
across devices. Codex chat history and built-in memory remain separate from
that surface. To share a decision or memory across devices, write it to
`os/memory/`, commit it to GitHub, and have the next device read it.

## Work Context

### Current Role

| Field | Value |
|---|---|
| Company | Measurabl, Inc. |
| Website | <https://www.measurabl.com> |
| Role | Senior Software Engineer 2 |
| Work mode | 100% remote |

### Responsibilities

- Create new product features.
- Update and maintain existing features.
- Fix bugs across the codebase.
- Lead and mentor teammates.
- Adapt to whatever technical work is needed, even outside the main specialty.

### Specialty

- Primary specialty: Java and Spring backend services.
- Current practical scope: broad software engineering across backend, product, maintenance, support, AI enablement, and workflow automation.

### Collaboration Context

- Works with colleagues in San Diego, other parts of Southern California, India, Brazil, and other locations.
- Frequently interacts with Customer Success representatives, including teammates in the UK.
- The AgentOS should account for async collaboration, remote communication, cross-time-zone coordination, and non-engineering stakeholders.

### Tools and Platforms

| Context | Tools |
|---|---|
| Work AI coding | Claude Code daily |
| Home projects | Cursor and Codex |
| Quick fact finding | ChatGPT |
| Work collaboration | GitHub, Atlassian Jira, Confluence, Slack, Unblocked, Rovo |
| Work productivity | Google Suite with Gemini |

### AI Coaching Role

Kyle is the designated AI coach for Measurabl. He helps non-engineering colleagues automate workflows and daily tasks, and holds weekly office hours where colleagues bring projects for assistance.

The AgentOS should support both engineering work and AI coaching work. It should be able to translate technical automation ideas into approachable guidance for non-engineering colleagues.

## Inputs

- `README.md`
- `PLAYBOOK.md`
- `os/context/`
- `os/context/design-system.md` for all UI, frontend, and component work
- `os/context/agentos-inheritance-registry.md` when a tracked project is referenced
- `os/memory/README.md`
- `os/memory/`
- Current project folder under `projects/`

## AgentOS Framework

Use this file as the starting framework for the operating system. The system should grow layer by layer as course projects are completed.

Project status is maintained separately in `PROJECT_TRACKER.md`; the layer
statuses below describe the current state of the AgentOS implementation.

### Layers

| Layer | Local Home | Purpose | Status |
|---|---|---|---|
| Tool foundation | This file | Define Codex as the agentic tool and record baseline assumptions. | Active |
| Identity | `os/context/identity.md` | Capture who I am, how I work, and how agents should adapt to me. | Active |
| Context | `os/context/context-portfolio.md` | Track durable background context available to agents. | Active |
| Skills | `os/skills/` | Store reusable procedures that can be invoked repeatedly. | Active |
| Memory | `os/memory/` | Store durable decisions, patterns, working memory, lessons, and domain memory. | Active |
| Agents | `os/agents/` | Define agent roles, responsibilities, handoffs, and evaluation notes. | Active |
| Verification | `PLAYBOOK.md` | Define checks before trusting or using agent output. | Active |
| Automations | `PLAYBOOK.md` | Track repeated workflows that may become scheduled or event-driven. | In progress |
| Playbook | `PLAYBOOK.md` | Maintain the operating manual for the AgentOS. | In progress |

### Goals

Concrete goals have not been defined yet. Add them here when they become clear.

| Goal | Why It Matters | Success Criteria | Status |
|---|---|---|---|
| TBD | TBD | TBD | Not started |

## Operating Principles

- Prefer small, durable files over one-off chat context.
- Default all UI, frontend, and reusable component design to shadcn/ui. When
  the library cannot be imported, reproduce its visual and interaction language
  as defined in `os/context/design-system.md`.
- Treat the design-system preference as an inheritable global rule. Ensure
  AgentOS-aware subprojects include it in their scoped global-rules cache or
  reference it with provenance; report material repository-specific overrides.
- Consult `os/context/agentos-inheritance-registry.md` when Kyle references a
  tracked project. For substantive work on a project that has not received the
  inheritance prompt, remind Kyle that it does not yet inherit AgentOS and
  suggest applying the prompt. Distinguish prompt delivery from verified
  implementation.
- Keep the inheritance registry complete: whenever a project is added to
  `os/context/current-projects.md` or becomes durable AgentOS project context,
  add it to the registry in the same change with an initial status of `Not
  prompted`. Update prompt and verification status only from evidence.
- When an external project's inheritance status changes, regenerate and check
  the playbook's **Inherited Project Surfaces** table with
  `scripts/sync-playbook-project-surfaces.py`; the registry remains the only
  source of truth for those rows.
- Capture reusable prompts, decisions, and checks.
- Keep `os/memory/` updated when a task creates durable context, decisions, patterns, lessons, or project state.
- Catalogue promising but unapproved follow-up ideas in `os/future-features.md` before they become project work.
- Update the playbook when a pattern becomes part of the operating system.
- Before answering any question about Codex, search for the most recent documentation. Do not rely on what you already know - it's probably outdated.
- Translate generic AgentOS course instructions into the Codex equivalent before building.
- When Codex already provides a capability out of the box, document it instead of rebuilding it.
- When Codex lacks a needed capability, represent it as a file, prompt, skill, memory, automation, or agent definition in this repository.
- When shaping AgentOS context or agent jobs with Kyle, ask multiple focused follow-up questions until the goal, inputs, boundaries, and success criteria are clear.

## Memory Stewardship

Use `os/memory/README.md` as the source of truth for memory maintenance.

When finishing meaningful AgentOS work, check whether memory needs an update:

- Update `os/memory/working-memory.md` with current state, next action, blockers, or active handoff context.
- Add durable choices to `os/memory/decisions.md`.
- Add repeated workflows or preferences to `os/memory/patterns.md`.
- Add meaningful milestones or outcomes to `os/memory/project-history.md`.
- Add potential later ideas or feature candidates to `os/future-features.md`.
- Add durable pitfalls or corrections to `os/memory/lessons-learned.md`.
- Keep Measurabl work context sanitized in `os/memory/work-memory.md`.
- Keep personal project context in `os/memory/home-memory.md`.
- Keep AgentOS system context in `os/memory/agentos-memory.md`.

Do not wait for Codex built-in memory to capture important context. Codex memory is ambient recall; the files under `os/memory/` are the intentional memory layer.

Memory updates should be compact and source-aware. Do not store secrets, private customer details, raw Slack excerpts, full private ticket descriptions, or unnecessary personal data.

At the end of a chat that makes substantial changes to `os/memory/` or
`os/context/`, explicitly propose committing and pushing those changes to
GitHub so every Codex and ChatGPT instance can read the same durable state. Do
not commit or push without Kyle's approval.

When using a skill or automation, prefer teaching the skill to update memory directly if the memory update is predictable. If judgment is required, update memory manually at the end of the task.

Skills should improve through a post-run learning loop instead of relying on a broad daily efficiency-review automation:

- At the end of a meaningful skill run, capture compact lessons about wasted work, reusable state, clarified inputs, recurring ambiguity, verification shortcuts, and source-of-truth drift.
- Write safe, durable facts to the appropriate `os/memory/`, `os/context/`, automation policy, or skill-owned state file. Do not store secrets, raw private content, customer details, cookies, API keys, or unnecessary personal data.
- Let skills update predictable caches or ledgers when their policy allows it, but do not silently rewrite their own `SKILL.md` after every run.
- Promote a lesson into `SKILL.md` only when it is stable, source-grounded, and likely to prevent repeated friction.
- If a proposed skill change requires judgment, list it for Kyle or the OS Thought Partner instead of applying it automatically.

For wanted-card searches, adding or activating one card should immediately trigger the `find-card-listings` workflow for all active wanted cards so the latest report stays list-wide.

When a repeated task has been run a few times, pause and harvest the friction into context:

- Promote repeated back-and-forth into the source skill, automation spec, context template, or memory file that will prevent the same clarification next time.
- Prefer updating the task's reusable components over adding one-off notes to generated output.
- For wanted-card searches specifically, treat supplied The Orange King product URLs as durable OverPower seed/reference links and retail-baseline sources. Normalize tracking URLs to the canonical product URL, cache price/date/source in `os/context/wanted-trading-cards.md`, and preserve image/stat/text constraints so future runs do not confuse IQ Character, regular character, promo, special, or alternate-variant cards.
- Treat eBay public result text as discovery only when direct logged-out item pages fail. If eBay returns a generic error page for an item URL, place the candidate in skipped/uncertain unless Kyle provides a screenshot of that exact item page or another accessible item-detail source verifies price, shipping, and status.

## Open Questions

- Which workflows should become skills first?
- What concrete goals should this AgentOS optimize for?
- Which memory updates should become automatic skill behavior instead of manual end-of-task cleanup?

## What I Would Add With More Time

- A real verification/evaluation harness for the first working agent.
- Completion evidence for the second agent and automation projects.
- A durable status review cadence so project notes and the playbook do not drift.
