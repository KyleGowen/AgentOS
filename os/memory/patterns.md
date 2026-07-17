# Patterns

Repeated workflows, preferences, and recurring shapes that may become skills, automations, or playbook rules.

## Memory Maintenance

- Update memory at the end of a meaningful task rather than continuously during the task.
- Promote durable items out of `working-memory.md` into decisions, patterns, lessons, project history, or domain memory.
- Compact aggressively so old context does not drown out current context.
- Prefer source links or source names over copied private content.
- Use Codex generated memories for ambient recall only; required behavior and durable AgentOS context should live in repo files.
- If a memory update would include private work source material, store a source pointer instead of copying the content.

## AgentOS Project Work

- Start by checking the canonical project tracker, then inspect the relevant project folder and `os/` artifact area.
- If a project scaffold exists under the wrong name, align it with the canonical tracker instead of letting duplicate project folders drift.
- Keep build notes concrete: inputs, decisions, output, evidence, and reflection.
- Prefer single-responsibility agents over broad assistants when creating new AgentOS jobs.
- Split workflows into separate agents when the trigger, inputs, or outputs differ meaningfully, such as pre-session prep versus post-session follow-up.
- When shaping AgentOS context or agent jobs with Kyle, interview with focused follow-up questions until the goal, inputs, boundaries, and success criteria are clear.
- Review-prep digests should be compact, link-heavy, source-grounded, and use bullets instead of long paragraphs.
- Review-prep agents should separate prompts or possible comment angles from final PR comments unless Kyle explicitly asks for draft comments.

## Personal Productivity Connectors

- When Kyle asks to accept all appointments from a sender, use the `accept-sender-appointments` Codex skill: search bounded unread Gmail from the named sender, accept matching Google Calendar events once, then mark the requested sender messages read.
- Keep mailbox mutations narrow: operate on explicit Gmail message IDs from the sender search, and do not delete, archive, forward, or broadly mark categories read.
- For AgentOS automations, keep a harness-neutral spec under `os/automations/` and make the Codex scheduled job a thin runner over that spec so the workflow can be replicated outside Codex.

## Personal Collecting Automations

- Wanted trading card scans should be read-only: use logged-out eBay access, never bid or buy, omit ended/completed/sold listings from active reports, and compare OverPower only against The Orange King retail site, not its eBay account; compare Magic against Brute Force MTG.
- Keep wanted-card targets in `os/context/wanted-trading-cards.md` and treat scheduled listing reports as replaceable output rather than durable memory.
- Cache retail baseline price, checked date, and source URL in the wanted-card details after the first lookup; scheduled runs should reuse cached baselines unless Kyle asks for a refresh.
- Use US/domestic shipping for Kyle's listing totals when visible, and never include sold/completed/ended eBay listings in active opportunity tables.
- Adding or activating a wanted-card target should immediately run the wanted-card listing workflow for all active cards and replace the latest full-list report.
- For Magic wanted-card retail baselines, use Brute Force MTG's direct product search URL (`/products/search?q=<card>&c=1`) with a browser user-agent if needed, match exact product rows, and allow out-of-stock rows to provide the cached retail baseline price with stock status noted.
- For eBay wanted-card listing prices, treat search results, product pages, and item-card tiles as discovery only; the individual item detail page price plus shipping is authoritative for reports.
- For OverPower wanted-card retail baselines, a supplied The Orange King product page is the best seed: normalize away tracking params, read Shopify product JSON/title/price/availability/image, and cache the canonical URL and price in the wanted-card entry.
- For OverPower IQ Character wanted cards, require exact character, IQ Character variant, stats, art/background, and visible text cues; exclude regular/original characters, PowerSurge, specials, power cards, teamworks, and alternate named IQ variants by default.

## Kyle Collaboration

- Ask focused questions when preferences materially change the system.
- Once preferences are clear, make concrete progress.
- Challenge assumptions when evidence is weak, especially for work that affects customers, reporting, auditability, or data correctness.
- When interviewing Kyle, prefer a few meaningful tradeoff questions over a broad questionnaire.

## Monitorless Home Server Work

- When helping with Kyle's Home Media Server, assume Codex may be used remotely from mobile and the server may not have a monitor attached.
- Prefer read-first checks, compact summaries, explicit next actions, and stepwise instructions that are easy to follow remotely.
- Treat storage, drive letters, Docker bind mounts, Plex writes, downloads, deletes, path repairs, and service setting changes as live-server safety concerns.
- Use the project repo as source of truth for detailed current state; keep AgentOS memory summary-level and free of secrets, tracker details, torrent data, and raw operational logs.

## Fitness Digest From Repo Evidence

- When helping with Kyle's DDR/ITG Machine, use the backup and digest repo as source evidence for play cadence, song time, difficulty range, score progress, and notable songs.
- Summarize trends compactly and encouragingly, but avoid medical advice or claims that the source data does not support.
- Treat non-secret scores, player labels, levels, percentages, play time, and digest summaries as acceptable context.
- Protect GitHub PATs, local config, raw backup files, raw XML uploads, and unnecessary personal detail.
- Confirm before force-push, restore, schedule changes, save/config edits, backup repo mutation, or live-machine changes.
