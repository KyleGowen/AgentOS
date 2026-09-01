# Future Features

Potential AgentOS improvements that are useful enough to remember but not yet
ready to schedule, design, or implement.

Use this file for ideas that need a home before they become a skill update,
automation, agent, context file, or project. Keep entries compact and promote
them into the right source file once Kyle decides to build them.

## Intake Rules

- Capture the idea, source, likely home, and next decision.
- Mark whether the idea is `candidate`, `needs research`, `ready to design`, or
  `promoted`.
- Keep private details out of this file. Link to local sanitized artifacts when
  helpful.
- Do not treat an entry here as approved implementation work.

## Ideas

| Idea | Source | Likely Home | Status | Next Decision |
|---|---|---|---|---|
| Add actual SDGE interval usage import and rate-aware annotations. Use SDG&E Green Button export data for electric/gas interval usage, including import/export where available, and use SDG&E rate data to annotate costs instead of inferring kWh or solar generation from charges. | SDGE energy-alert dashboard iteration, 2026-07-30 | `catalog-sdge-energy-alerts` skill and `os/data/sdge-energy-alerts/` | candidate | Decide whether Kyle wants to export/provide Green Button data, then design an importer and dashboard charts for actual usage/export data. |
| Define AgentOS post-course maturity. Replace course-completion milestones with explicit operating outcomes, evidence standards, review cadence, and next-level capabilities. | Kyle, 2026-08-17 Thought Partner refresh; all projects confirmed complete 2026-09-01 | `os/agents/os-thought-partner.md`, `PROJECT_TRACKER.md`, and `PLAYBOOK.md` | ready to design | Choose the maturity dimensions and success criteria that should guide AgentOS. |

## Existing Documented Candidates

These are already documented in their owning files; keep them here only as an
index so future planning scans have one place to start.

| Candidate | Owning File | Notes |
|---|---|---|
| AI office-hours prep automation | `PLAYBOOK.md`; `os/agents/ai-office-hours-prep-agent.md` | Future scheduled run before Tuesday office hours. |
| AI office-hours follow-up automation | `PLAYBOOK.md`; `os/agents/ai-office-hours-follow-up-agent.md` | Future post-session run after Kyle provides notes. |
| PR review prep scheduled digest | `PLAYBOOK.md`; `os/agents/pr-review-prep-agent.md` | Future workday digest once work GitHub identity and access details are finalized. |
