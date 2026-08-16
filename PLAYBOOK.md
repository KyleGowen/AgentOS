# My Agentic OS Playbook

Last updated: 2026-08-16

Project status source: `PROJECT_TRACKER.md` (last audited 2026-08-16).

## My OS Foundation

### Identity

| Scope | File | Summary | Status |
|---|---|---|---|
| Me | `os/context/identity.md` | Personal preferences, rules, voice, and operating principles. | Active |

### Context

| File | What It Covers | Status |
|---|---|---|
| `os/context/context-portfolio.md` | Durable background context for agents. | Active |
| `os/context/excelsior.md` | Summary-level Excelsior routing and permanent scoped inheritance boundary. | Active |
| `os/future-features.md` | Potential follow-ups and later ideas before they become projects, skills, agents, or automations. | Active |

### Skills

| Scope | Skill Name | When I Use It | What It Produces |
|---|---|---|---|
| Me | `/complete` | Mark AgentOS course projects complete. | Updated tracker, project notes, README, and related docs. |
| Agent-specific | Measurabl and Excelsior skill translations | Repeated work workflows imported from Claude Code and Cursor. | Codex repo skills and native archives. |
| Me | `accept-sender-appointments` | Accept trusted sender appointment invitations and clean up matching mail. | Calendar RSVPs, read-state cleanup, and compact run summary. |
| Me | `find-card-listings` | Scan eBay for wanted OverPower and Magic cards without bidding or logging in. | Price-sorted active listing tables with baseline notes. |
| Me | `catalog-sdge-energy-alerts` | Process unread SDGE Energy Use Alert emails from Gmail. | Structured utility records and an HTML time-series dashboard. |
| Agent-specific | `thraxos` | Safely inspect, configure, and maintain Thraximundar and its ITGMania ecosystem. | Verified machine status, guarded operations, and durable ThraxOS memory. |

### Memory

| Type | How It Works | Update Cadence | Status |
|---|---|---|---|
| Working memory | `os/memory/working-memory.md` plus Codex built-in memory for ambient recall. | End of meaningful task | Active |
| Persistent memory | `os/memory/` files separated by decisions, patterns, history, lessons, and domain. | End of task, compacted aggressively | Active |

### Connections

| Service | What I Use It For | Connection Type | Status |
|---|---|---|---|
| GitHub | Version control, evidence links, commits, and pushes. | Git / GitHub | Active |
| Google Calendar | Meeting prep, schedule awareness, and focus-block planning. | Google Calendar connector | Active, personal Gmail currently |
| Google Drive | Docs, Sheets, Slides, and file discovery for planning and AI coaching workflows. | Google Drive connector | Active, personal Gmail currently |
| ChatGPT Project | Cross-device OS Thought Partner chats grounded in the live AgentOS repository. | ChatGPT Project + connected GitHub app | Active; project `AgentOS` |
| Atlassian Jira and Confluence | Work ticket research, linked source documents, and implementation planning. | Atlassian connector or MCP | Desired |
| Slack | Async updates and incident context. | Slack connector | Deferred; requires work admin approval |
| Excelsior | Product work and release support with compact global AgentOS inheritance. | Repo-local cache plus Git/GitHub | Active |

### Verification

My checks before using a meaningful agent result (under one minute):

- [ ] **Right job:** Did it answer the request and honor the stated scope and constraints?
- [ ] **Evidence is current:** Are important claims traceable to an identified, current source or clearly marked unverified?
- [ ] **Safe by default:** Did it protect secrets and stop for explicit approval before consequential writes?
- [ ] **Useful result:** Is the answer concise, clear about uncertainty, and actionable?

For the current Project 08 ThraxOS evaluation, scenarios, expected behavior,
and the run-record template live in
`projects/08-test-and-verify/verification-plan.md`. Review the checklist after
each meaningful run and hold a five-minute retrospective after a high-stakes
operation or after three meaningful runs.

## Course Projects

The current course status is maintained in `PROJECT_TRACKER.md`. Projects 00–07
are complete; Project 08 is in progress; and
Projects 09–11 are in progress with explicit evidence gaps recorded in the
tracker and project notes.

## My Agents

### Agent 1: OS Thought Partner

| | |
|---|---|
| Job | Help translate course projects into my chosen agentic tool and keep the system coherent. |
| Identity files | `os/agents/os-thought-partner.md` |
| Agent-specific skills | TBD |
| Connections used | GitHub, local files |
| What's working | TBD |
| What needs improvement | TBD |

### Agent 2: AI Office Hours Prep Agent

| | |
|---|---|
| Job | Prepare source-grounded agenda briefs before weekly AI office hours. |
| Identity files | `os/agents/ai-office-hours-prep-agent.md` |
| Agent-specific skills | TBD |
| Connections used | Local AgentOS context; user-provided office-hours inputs |
| What's working | Single-responsibility pre-session prep with a source-grounded trust gate. |
| What needs improvement | Future automation before Tuesday office hours; separate follow-up agent for post-session work. |

### Agent 3: AI Office Hours Follow-Up Agent

| | |
|---|---|
| Job | Turn completed AI office-hours sessions into source-grounded follow-up packets. |
| Identity files | `os/agents/ai-office-hours-follow-up-agent.md` |
| Agent-specific skills | TBD |
| Connections used | Local AgentOS context; user-provided post-session inputs |
| What's working | Single-responsibility post-session follow-up with drafts and record updates kept review-only. |
| What needs improvement | Future automation after office hours; possible skill for processing session documents. |

### Agent 4: PR Review Prep Agent

| | |
|---|---|
| Job | Find Measurabl PRs where Kyle is tagged and prepare compact review-prep digests. |
| Identity files | `os/agents/pr-review-prep-agent.md` |
| Agent-specific skills | TBD |
| Connections used | GitHub; `os/context/engineering-review.md`; `os/memory/pr-review-prep-state.md` |
| What's working | Read-only review prep with links, repository, changed file count, build status, gist, and suggested review prompts. |
| What needs improvement | Replace `MEASURABL_GITHUB_LOGIN` with Kyle's exact work GitHub identity; future scheduled digest. |

### Agent 5: ThraxOS

| | |
|---|---|
| Job | Safely operate and maintain Thraximundar, its ITGMania ecosystem, backups, song packs, play data, and machine memory. |
| Identity files | `KyleGowen/ThraxOS` root `AGENTS.md`; `.codex/agents/thraxos.toml` |
| Agent-specific skills | `KyleGowen/ThraxOS/.agents/skills/thraxos/` and routed project skills |
| Connections used | Local Windows host, GitHub source repositories, live machine state |
| What's working | Real custom Codex specialist with context, runbooks, guarded scripts, persistent memory, and operating history. |
| What needs improvement | Capture a compact representative ThraxOS run and reflection as the first Project 08 verification record. |

### How My Agents Relate

The OS Thought Partner helps design, maintain, and evolve the AgentOS. The AI
Office Hours Prep Agent is a narrower job agent that prepares Kyle for a
recurring work responsibility. The AI Office Hours Follow-Up Agent handles the
separate post-session responsibility of turning completed sessions into
reviewable follow-up packets. The PR Review Prep Agent supports Kyle's
engineering review work by preparing a read-only digest of PRs that need his
attention. ThraxOS is the dedicated machine specialist and the selected Project
07 working-agent build; its detailed source of truth remains the separate
`KyleGowen/ThraxOS` repository.

## Automations

| Automation | Trigger | What It Does | Status |
|---|---|---|---|
| AI office-hours prep | Weekly before Tuesday office hours | Run the AI Office Hours Prep Agent once Kyle has provided current agenda inputs. | Future candidate |
| AI office-hours follow-up | After Tuesday office hours | Run the AI Office Hours Follow-Up Agent once Kyle has provided current post-session notes. | Future candidate |
| PR review prep | Workday morning or on demand | Run the PR Review Prep Agent to find tagged Measurabl PRs and prepare the review queue. | Future candidate |
| Auto-accept appointments | Daily at 6:00 AM Pacific | Run `accept-sender-appointments` for active senders in `os/automations/auto-accept-appointments.md`. | Active; Codex id `auto-accept-trusted-appointments` |
| Wanted card listings | Daily at 6:00 AM Pacific, and immediately after adding or activating a wanted card | Run `find-card-listings` for all active cards in `os/context/wanted-trading-cards.md`, using logged-out eBay access and retail baselines. | Paused; Codex id `wanted-card-listings`; list-change trigger documented; isolated browser access is currently unavailable |
| SDGE energy alerts | Weekly Monday at 7:00 AM Pacific | Run `catalog-sdge-energy-alerts` for SDGE-label mail from `notices@sdge.com`, update the flat-file database, clean processed unread messages, and regenerate the dashboard. | Active; Codex id `sdge-energy-alerts` |

## What's Working Best

1. TBD

## Gaps & Next Steps

### Current Next Steps

- Capture a sanitized representative ThraxOS run, verified result, and reflection as the first Project 08 verification record.
- Select one additional agent for the Project 09 evaluation.
- Finish the Project 10 operating-manual cleanup and Project 11 completion notes.

### Next Quarter

- Turn the strongest repeated workflows into skills, agents, and automations.
- Review `os/future-features.md` and promote selected ideas into their owning source files.

## Reflection

**Before AgentOS:** TBD

**Now:** TBD

**What surprised me:** TBD

**What I'd tell someone starting:** TBD
