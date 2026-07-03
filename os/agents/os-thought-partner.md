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
- `os/memory/README.md`
- `os/memory/`
- Current project folder under `projects/`

## AgentOS Framework

Use this file as the starting framework for the operating system. The system should grow layer by layer as course projects are completed.

### Layers

| Layer | Local Home | Purpose | Status |
|---|---|---|---|
| Tool foundation | This file | Define Codex as the agentic tool and record baseline assumptions. | Active |
| Identity | `os/context/identity.md` | Capture who I am, how I work, and how agents should adapt to me. | Draft |
| Context | `os/context/context-portfolio.md` | Track durable background context available to agents. | Draft |
| Skills | `os/skills/` | Store reusable procedures that can be invoked repeatedly. | Planned |
| Memory | `os/memory/` | Store durable decisions, patterns, working memory, lessons, and domain memory. | Draft |
| Agents | `os/agents/` | Define agent roles, responsibilities, handoffs, and evaluation notes. | Active |
| Verification | `PLAYBOOK.md` | Define checks before trusting or using agent output. | Draft |
| Automations | `PLAYBOOK.md` | Track repeated workflows that may become scheduled or event-driven. | Planned |
| Playbook | `PLAYBOOK.md` | Maintain the operating manual for the AgentOS. | Draft |

### Goals

Concrete goals have not been defined yet. Add them here when they become clear.

| Goal | Why It Matters | Success Criteria | Status |
|---|---|---|---|
| TBD | TBD | TBD | Not started |

## Operating Principles

- Prefer small, durable files over one-off chat context.
- Capture reusable prompts, decisions, and checks.
- Keep `os/memory/` updated when a task creates durable context, decisions, patterns, lessons, or project state.
- Update the playbook when a pattern becomes part of the operating system.
- Before answering any question about Codex, search for the most recent documentation. Do not rely on what you already know - it's probably outdated.
- Translate generic AgentOS course instructions into the Codex equivalent before building.
- When Codex already provides a capability out of the box, document it instead of rebuilding it.
- When Codex lacks a needed capability, represent it as a file, prompt, skill, memory, automation, or agent definition in this repository.

## Memory Stewardship

Use `os/memory/README.md` as the source of truth for memory maintenance.

When finishing meaningful AgentOS work, check whether memory needs an update:

- Update `os/memory/working-memory.md` with current state, next action, blockers, or active handoff context.
- Add durable choices to `os/memory/decisions.md`.
- Add repeated workflows or preferences to `os/memory/patterns.md`.
- Add meaningful milestones or outcomes to `os/memory/project-history.md`.
- Add durable pitfalls or corrections to `os/memory/lessons-learned.md`.
- Keep Measurabl work context sanitized in `os/memory/work-memory.md`.
- Keep personal project context in `os/memory/home-memory.md`.
- Keep AgentOS system context in `os/memory/agentos-memory.md`.

Do not wait for Codex built-in memory to capture important context. Codex memory is ambient recall; the files under `os/memory/` are the intentional memory layer.

Memory updates should be compact and source-aware. Do not store secrets, private customer details, raw Slack excerpts, full private ticket descriptions, or unnecessary personal data.

When using a skill or automation, prefer teaching the skill to update memory directly if the memory update is predictable. If judgment is required, update memory manually at the end of the task.

## Open Questions

- Which workflows should become skills first?
- What concrete goals should this AgentOS optimize for?
- Which memory updates should become automatic skill behavior instead of manual end-of-task cleanup?

## What I Would Add With More Time

- Context files for Excelsior.
- Skills for diagnosing and fixing Excelsior's build pipeline.
- Context files for Planted.
- Context files for Vimanas.
