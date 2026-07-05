# DDR/ITG Machine

This file summarizes Kyle's StepMania, DDR, and ITGMania setup for AgentOS routing, fitness insight, and score-history interpretation.

Source repos:

- Tooling: <https://github.com/KyleGowen/itgmania-backup>
- Backup and digest evidence: <https://github.com/KyleGowen/Thraximundar-Backup>

## Purpose

DDR/ITG Machine is Kyle's active rhythm-game hobby log and exercise project. The physical Windows nukbox machine is Thraximundar. Kyle plays StepMania, DDR, and ITGMania for exercise about 1-2 times per week.

AgentOS should understand this project as a hobby and fitness-progress context first, with the ITGMania backup tooling as the preservation and evidence layer.

Future agents should default to digest-coach behavior: summarize recent play activity, trends, difficulty progression, score progress, and notable songs from the backup digest in a friendly, non-medical way.

## Current Snapshot

Snapshot date: 2026-07-05.

Source: `KyleGowen/Thraximundar-Backup` README and latest digest.

| Area | Current summary |
|---|---|
| Latest backup | Jul 5, 2026 at 3:01 AM |
| Next backup | Jul 6, 2026 at 3:00 AM |
| Recent 30-day KYLE song time | 5h 37m 16s |
| Recent KYLE difficulty range | Levels 8-10 in the 30-day table |
| Recent KYLE 30-day level counts | Level 8: 1, level 9: 5, level 10: 2 |
| Latest KYLE digest run | Jul 3, 2026: 32m 11s in songs |
| Other visible player labels | LIZY, SAM!, and Player appear in digest summaries |

Representative recent KYLE score highlights from the Jul 3, 2026 digest:

- `Untouched` from `Anthem Series - The Girls`, Challenge 9, 88.41% DP.
- `Chained To The Rhythm` from `Ben Speirs' SPEIRMIX GALAXY`, Challenge, 90.05% DP.
- `Someone (Giuseppe Ottaviani Remix)` from `Misc. Collected`, Hard 9, 79.15% DP.

These are summary examples, not a source of truth. Re-read the backup repo for current score data.

## Backup Architecture

The backup tool lives in `KyleGowen/itgmania-backup`.

Summary:

- Windows PowerShell 5.1+ tool.
- Uses Git for Windows.
- Uses a user-level Windows scheduled task and cron-style schedule.
- Backs up ITGMania install and save data into a separate backup repo.
- Force-pushes the backup repo as a unidirectional backup state.
- Produces digest output from score and file changes.

Important backup rules:

- Songs are intentionally never backed up because they are too large for GitHub.
- Files over 100 MB are skipped and reported.
- `config.json` contains a GitHub PAT and must not be committed, mirrored, or summarized with secret values.
- The backup destination repo is `KyleGowen/Thraximundar-Backup`.

## Data Flow

Use the tool repo for implementation details and the backup repo for current evidence.

| Data | Source of truth |
|---|---|
| Backup tool behavior | `KyleGowen/itgmania-backup/README.md` and `CONTEXT.md` |
| Installer, schedule, and cron behavior | `Install-ITGManiaBackup.ps1`, `CronRunner.ps1`, and tool README |
| Digest and meter parsing behavior | `CONTEXT.md` and `.cursor/rules/digest-and-stats.mdc` |
| Generated score digest | `KyleGowen/Thraximundar-Backup/README.md` and `digests/` |
| Current save and upload data | `KyleGowen/Thraximundar-Backup/ITGMania/` |

Data flow summary:

- Upload XML records all plays.
- Stats XML stores top scores per chart.
- Digests report new high scores and pack/song changes.
- The 30-day meter tables use Upload data when available, then fall back to Stats XML and digests.

## Fitness And Progress Interpretation

Use play cadence, song time, difficulty levels, and score movement as lightweight signals.

Good summaries:

- Note consistency, such as whether Kyle is still playing roughly 1-2 times per week.
- Call out recent song time and difficulty range.
- Mention representative score improvements or high-effort sessions.
- Separate rhythm-game skill progress from exercise consistency when useful.
- Stay encouraging without inflating the data.

Avoid:

- Medical advice.
- Weight, injury, or health claims not present in the source material.
- Treating one digest as a complete fitness record.
- Over-profiling other visible players.

## Safety Boundaries

Read-only analysis of public repo content is fine.

Require explicit confirmation before:

- Force-pushing or mutating the backup repo.
- Restoring save data.
- Editing ITGMania saves, upload records, Stats XML, or config.
- Changing backup schedule or installed task behavior.
- Touching local `config.json` or any GitHub PAT.
- Running live-machine actions on Thraximundar.

Do not store in AgentOS:

- GitHub PATs.
- Local `config.json`.
- Private credentials.
- Raw full backup files.
- Raw XML upload files.
- Large digest mirrors.
- Unnecessary personal detail about other players.

Non-secret score details, representative songs, player labels, levels, percentages, play time, and digest summaries are acceptable when they help future agents understand the project.

## Agent Routing

When Kyle asks about this project:

- Start from this file for durable context.
- Use the backup repo for current digest evidence.
- Use the tooling repo for how backup, install, cron, force-push, and score parsing work.
- Prefer compact digest-coach summaries unless Kyle asks for detailed score analysis.
- For Windows machine work, give remote-friendly, stepwise instructions.
- For mutation or restore work, ask for explicit confirmation before acting.
