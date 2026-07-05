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
