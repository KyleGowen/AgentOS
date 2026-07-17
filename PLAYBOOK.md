# My Agentic OS Playbook

Last updated: 2026-07-17

## My OS Foundation

### Identity

| Scope | File | Summary | Status |
|---|---|---|---|
| Me | `os/context/identity.md` | Personal preferences, rules, voice, and operating principles. | Draft |

### Context

| File | What It Covers | Status |
|---|---|---|
| `os/context/context-portfolio.md` | Durable background context for agents. | Draft |

### Skills

| Scope | Skill Name | When I Use It | What It Produces |
|---|---|---|---|
| Me | `/complete` | Mark AgentOS course projects complete. | Updated tracker, project notes, README, and related docs. |
| Agent-specific | Measurabl and Excelsior skill translations | Repeated work workflows imported from Claude Code and Cursor. | Codex repo skills and native archives. |
| Me | `accept-sender-appointments` | Accept trusted sender appointment invitations and clean up matching mail. | Calendar RSVPs, read-state cleanup, and compact run summary. |
| Me | `find-card-listings` | Scan eBay for wanted OverPower and Magic cards without bidding or logging in. | Price-sorted active listing tables with baseline notes. |

### Memory

| Type | How It Works | Update Cadence | Status |
|---|---|---|---|
| Working memory | `os/memory/working-memory.md` plus Codex built-in memory for ambient recall. | End of meaningful task | Draft |
| Persistent memory | `os/memory/` files separated by decisions, patterns, history, lessons, and domain. | End of task, compacted aggressively | Draft |

### Connections

| Service | What I Use It For | Connection Type | Status |
|---|---|---|---|
| GitHub | Version control and evidence links. | Git / GitHub | Active |
| Google Calendar | Meeting prep, schedule awareness, and focus-block planning. | Google Calendar connector | Active, personal Gmail currently |
| Google Drive | Docs, Sheets, Slides, and file discovery for planning and AI coaching workflows. | Google Drive connector | Active, personal Gmail currently |
| Atlassian Jira and Confluence | Work ticket research, linked source documents, and implementation planning. | Atlassian connector or MCP | Desired |
| Slack | Async updates and incident context. | Slack connector | Deferred; requires work admin approval |
| Excelsior | Personal project automation, card/deck workflows, local app context, and release support. | Custom MCP | Future idea |

### Verification

My checks before using AI output:

- [ ] Are factual claims traceable to a source?
- [ ] Does the output match my intent and constraints?
- [ ] Would I put my name on this?

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

### How My Agents Relate

The OS Thought Partner helps design, maintain, and evolve the AgentOS. The AI
Office Hours Prep Agent is a narrower job agent that prepares Kyle for a
recurring work responsibility. The AI Office Hours Follow-Up Agent handles the
separate post-session responsibility of turning completed sessions into
reviewable follow-up packets. The PR Review Prep Agent supports Kyle's
engineering review work by preparing a read-only digest of PRs that need his
attention.

## Automations

| Automation | Trigger | What It Does | Status |
|---|---|---|---|
| AI office-hours prep | Weekly before Tuesday office hours | Run the AI Office Hours Prep Agent once Kyle has provided current agenda inputs. | Future candidate |
| AI office-hours follow-up | After Tuesday office hours | Run the AI Office Hours Follow-Up Agent once Kyle has provided current post-session notes. | Future candidate |
| PR review prep | Workday morning or on demand | Run the PR Review Prep Agent to find tagged Measurabl PRs and prepare the review queue. | Future candidate |
| Auto-accept appointments | Every 2 hours from 7:00 AM through 11:00 PM | Run `accept-sender-appointments` for active senders in `os/automations/auto-accept-appointments.md`. | Active; Codex id `auto-accept-trusted-appointments` |
| Wanted card listings | Every 4 hours from midnight, startup when supported, and immediately after adding or activating a wanted card | Run `find-card-listings` for all active cards in `os/context/wanted-trading-cards.md`, using logged-out eBay access and retail baselines. | Active; Codex id `wanted-card-listings`; startup and list-change hooks documented |

## What's Working Best

1. TBD

## Gaps & Next Steps

### This Month

- Complete Project 00 and establish the first reusable OS context files.

### Next Quarter

- Turn the strongest repeated workflows into skills, agents, and automations.

## Reflection

**Before AgentOS:** TBD

**Now:** TBD

**What surprised me:** TBD

**What I'd tell someone starting:** TBD
