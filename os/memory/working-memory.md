# Working Memory

Current, short-lived context that should help the next session pick up the thread.

Update this at the end of a meaningful task, project shift, or planning session. Keep it aggressively compact: current state, next action, blockers, and anything likely to matter in the next few sessions.

## Active AgentOS Work

- Cross-device memory protocol is active: committed `main` in `KyleGowen/AgentOS` is the shared durable source for every signed-in Codex and ChatGPT instance. Chat history and built-in memory are surface-specific; record portable knowledge in `os/context/` or `os/memory/`, then commit and push it from Codex.
- Project 07 is complete using ThraxOS, not the AI Office Hours Prep Agent. ThraxOS already has a custom Codex agent, context, skills, memory, safety rules, verification procedures, and real operating history.
- Project 08 is in progress with a ThraxOS verification plan, four-item under-one-minute checklist, scenario set, and sanitized run-record template in `projects/08-test-and-verify/verification-plan.md`. Next handoff: execute the representative read-only health snapshot, score it, and capture Kyle's reflection.

## Active Work Projects

- See `work-memory.md` for sanitized work context.

## Active Home Projects

- See `home-memory.md` for personal project context.
- SDGE energy alerts run weekly Monday at 7:00 AM Pacific under Codex automation `sdge-energy-alerts`; the policy is `os/automations/sdge-energy-alerts.md`, and the dashboard is `os/reports/sdge-energy-alerts/index.html`. On 2026-07-31, parser/chart coverage expanded to usage-to-date, time-of-use kWh buckets, gas therms, and meter endings; the visible one-year dashboard window has usage data backfilled, and 92 older usage-report messages remain for a targeted `usage-backfill-ids` Gmail enrichment pass.
- Wanted-card listings are configured for daily 6:00 AM Pacific runs under Codex automation `wanted-card-listings`, but the live job is currently paused because the required isolated logged-out browser is unavailable. Adding or activating a target still triggers an immediate full-list refresh when the workflow is runnable. The context currently contains 15 Active targets, with twice-weekly Monday/Friday retail-baseline refreshes. Auction prices must come from fresh uncached item-page data; the latest full-list report is `os/automation-output/wanted-card-listings/latest.md`.
- Wanted-card scans now require a separate Codex-launched private/incognito browser profile, which Kyle authorized on 2026-07-27. It must visibly remain logged out; raw eBay requests are supplementary only because they can return HTTP 403.

## Recently Completed

- 2026-08-16: Completed Project 07 - The Build.
- 2026-08-13: Audited all AgentOS course project statuses against repository evidence and live automation configuration.
- 2026-07-05: Completed Project 06 - The Job.
- 2026-07-03: Completed Project 05 - Your Connections.
- 2026-07-03: Completed Project 04 - Your Memory.

## Clear Soon

- Add temporary handoff notes here when they do not belong in persistent memory.
