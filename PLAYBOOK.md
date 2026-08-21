# My Agentic OS Playbook

Last updated: 2026-08-17

Project status source: `PROJECT_TRACKER.md` (last audited 2026-08-17).

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
| Me | `os-map` | Open or refresh the current AgentOS structure map. | Browser-ready nested map of agents, skills, automations, and inherited projects. |
| Agent-specific | Measurabl and Excelsior skill translations | Repeated work workflows imported from Claude Code and Cursor. | Codex repo skills and native archives. |
| Me | `accept-sender-appointments` | Accept trusted sender appointment invitations and clean up matching mail. | Calendar RSVPs, read-state cleanup, and compact run summary. |
| Me | `find-card-listings` | Scan eBay for wanted OverPower and Magic cards without bidding or logging in. | Price-sorted active listing tables with baseline notes. |
| Agent-specific | `catalog-sdge-energy-alerts` | SDGE Energy Agent processes policy-scoped SDGE Energy Use Alert emails from Gmail. | Structured utility records and an HTML time-series dashboard. |
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

The completed Project 08 ThraxOS evaluation, scenarios, expected behavior, and
run records live in
`projects/08-test-and-verify/verification-plan.md`. Review the checklist after
each meaningful run and hold a five-minute retrospective after a high-stakes
operation or after three meaningful runs.

## Course Projects

The current course status is maintained in `PROJECT_TRACKER.md`. Projects 00–09
are complete. Projects 10–11 are in progress with explicit evidence gaps
recorded in the tracker and project notes.

## Project Surfaces & Ownership

This is the map for navigating AgentOS across project boundaries. It is not a
second copy of project procedures: AgentOS-native agent definitions live in
`os/agents/`, the full skill inventory is `os/skills/catalog.md`, and each
project owns its own detailed agents, skills, runbooks, and current state.

### Inherited Project Surfaces

Only external projects that have received the AgentOS inheritance prompt appear
below. The table is generated from the inheritance registry, so it does not
mistake an unprompted project for one governed by AgentOS.

<!-- BEGIN GENERATED INHERITED PROJECT SURFACES -->
> Generated from `os/context/agentos-inheritance-registry.md` by `scripts/sync-playbook-project-surfaces.py`. Do not edit this table manually.
> Project-local agents, skills, and runbooks remain authoritative in the linked project.

| Project | Detailed authority | Inheritance state | Evidence / next check |
|---|---|---|---|
| ThraxOS | Project-local agents and skills; [https://github.com/KyleGowen/ThraxOS](https://github.com/KyleGowen/ThraxOS) | Prompt delivered; Verified 2026-08-16 | `projects/08-test-and-verify/runs/2026-08-16-thraxos-selective-inheritance.md`; the local cache matched committed AgentOS `main`, while upstream freshness was explicitly unverified. |
| Excelsior | Project-local agents and skills; [https://github.com/KyleGowen/excelsior](https://github.com/KyleGowen/excelsior) | Prompt delivered; Verified 2026-08-16 | Excelsior commit `33c1afe5`; AgentOS commit `b85ae39`; `os/context/excelsior.md`. |
<!-- END GENERATED INHERITED PROJECT SURFACES -->

## My Agents

### Agent 1: OS Thought Partner

| | |
|---|---|
| Job | Help translate course projects into my chosen agentic tool and keep the system coherent. |
| Identity files | `os/agents/os-thought-partner.md` |
| Agent-specific skills | `os-map` |
| Connections used | GitHub, local files |
| What's working | Active source-grounded maintenance of the playbook, map, and inherited-project surfaces. |
| What needs improvement | Define concrete goals, decide which workflows merit skills, and identify which memory updates can safely become automatic. |

### Agent 2: AI Office Hours Prep Agent

| | |
|---|---|
| Job | Prepare source-grounded agenda briefs before weekly AI office hours. |
| Identity files | `os/agents/ai-office-hours-prep-agent.md` |
| Agent-specific skills | None yet; the workflow is defined in the agent record. |
| Connections used | Local AgentOS context; user-provided office-hours inputs |
| What's working | Single-responsibility pre-session prep with a source-grounded trust gate. |
| What needs improvement | Future automation before Tuesday office hours; separate follow-up agent for post-session work. |

### Agent 3: AI Office Hours Follow-Up Agent

| | |
|---|---|
| Job | Turn completed AI office-hours sessions into source-grounded follow-up packets. |
| Identity files | `os/agents/ai-office-hours-follow-up-agent.md` |
| Agent-specific skills | None yet; the workflow is defined in the agent record. |
| Connections used | Local AgentOS context; user-provided post-session inputs |
| What's working | Single-responsibility post-session follow-up with drafts and record updates kept review-only. |
| What needs improvement | Future automation after office hours; possible skill for processing session documents. |

### Agent 4: PR Review Prep Agent

| | |
|---|---|
| Job | Find Measurabl PRs where Kyle is tagged and prepare compact review-prep digests. |
| Identity files | `os/agents/pr-review-prep-agent.md` |
| Agent-specific skills | None yet; the GitHub-oriented workflow is defined in the agent record. |
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
| What needs improvement | Keep upstream freshness distinct from the locally verified inheritance cache when live fetch checks are unavailable. |

### Agent 6: SDGE Energy Agent

| | |
|---|---|
| Job | Maintain the policy-scoped SDGE Energy Use Alert ledger and local dashboard. |
| Identity files | `os/agents/sdge-energy-agent.md`; thin Codex launcher `.codex/agents/sdge-energy-agent.toml` |
| Agent-specific skills | `catalog-sdge-energy-alerts` |
| Connections used | Gmail, limited to `notices@sdge.com` messages in the `SDGE` label |
| What's working | Active weekly workflow with a ledger-first processing model and local dashboard. |
| What needs improvement | Continue scheduled runs and revisit notable-change reporting after another comparable bill record. |

### How My Agents Relate

The OS Thought Partner helps design, maintain, and evolve the AgentOS. The AI
Office Hours Prep Agent is a narrower job agent that prepares Kyle for a
recurring work responsibility. The AI Office Hours Follow-Up Agent handles the
separate post-session responsibility of turning completed sessions into
reviewable follow-up packets. The PR Review Prep Agent supports Kyle's
engineering review work by preparing a read-only digest of PRs that need his
attention. ThraxOS is the dedicated machine specialist and the selected Project
07 working-agent build; its detailed source of truth remains the separate
`KyleGowen/ThraxOS` repository. The SDGE Energy Agent is a separate home-utility
data steward: it shares AgentOS governance with ThraxOS but has no handoff,
shared operational state, or machine-management authority.

## Automations

| Automation | Trigger | What It Does | Status |
|---|---|---|---|
| AI office-hours prep | Weekly before Tuesday office hours | Run the AI Office Hours Prep Agent once Kyle has provided current agenda inputs. | Future candidate |
| AI office-hours follow-up | After Tuesday office hours | Run the AI Office Hours Follow-Up Agent once Kyle has provided current post-session notes. | Future candidate |
| PR review prep | Workday morning or on demand | Run the PR Review Prep Agent to find tagged Measurabl PRs and prepare the review queue. | Future candidate |
| Auto-accept appointments | Daily at 8:00 AM and 8:00 PM Pacific | Run `accept-sender-appointments` for active senders in `os/automations/auto-accept-appointments.md`. | Active; Codex id `auto-accept-trusted-appointments` |
| Wanted card listings | Daily at 6:00 AM Pacific, and immediately after adding or activating a wanted card | Run `find-card-listings` for all active cards in `os/context/wanted-trading-cards.md`, using logged-out eBay access and retail baselines. | Paused; Codex id `wanted-card-listings`; list-change trigger documented; isolated browser access is currently unavailable |
| SDGE energy alerts | Weekly Monday at 7:00 AM Pacific | Run `catalog-sdge-energy-alerts` for SDGE-label mail from `notices@sdge.com`, update the flat-file database, clean processed unread messages, and regenerate the dashboard. | Active; Codex id `sdge-energy-alerts` |

## What's Working Best

1. **ThraxOS:** Its automated tasks are working well, and it makes managing the
   ITG machine substantially easier than doing so manually.

## Gaps & Next Steps

### Current Next Steps

- Confirm this manual remains an accurate, useful snapshot of the operating
  system, and establish a lightweight monthly review cadence.
- Finish the Project 11 completion notes, including end-to-end run and failure
  handling evidence for the active automations.

### Next Quarter

- Turn the strongest repeated workflows into skills, agents, and automations.
- Review `os/future-features.md` and promote selected ideas into their owning source files.

### Monthly OS Map Review

Once each month, run `os-map` to refresh and review the AgentOS map. Use it to
recall the installed skills, review the documented recurring-task status at
each project layer, and identify skills that may be ready to archive or remove.
Treat the map as an index: confirm each proposed change against its owning
skill, automation policy, or project source before changing it. This is a
manual review cadence, not a scheduled automation.

## Reflection

**Before AgentOS:** I retyped the same prompts and guidelines into all of my
projects. The consistency was there, but setting each project up was
repetitive.

**Now:** My projects inherit big-picture preferences and skills from AgentOS,
so I do not have to tell each one the same thing.

**What surprised me:** The ease of how well AgentOS can manage itself.

**What I'd tell someone starting:** Keep it high level, and think about big
projects and small tasks separately.
