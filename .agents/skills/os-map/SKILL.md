---
name: os-map
description: Open and maintain the current AgentOS structure map. Use when Kyle asks to view, open, refresh, or summarize the OS map, visualize the AgentOS hierarchy, or see its agents, skills, automations, and inherited project surfaces.
---

# OS Map

Show `projects/10-playbook/agentos-system-map.html`, a browser-ready nested map
of the current AgentOS structure. Keep it a concise visual index; source files
remain authoritative for detailed procedures and current state.

## Workflow

1. Work from the AgentOS repository root. Read `AGENTS.md`, `PLAYBOOK.md`,
   `os/agents/README.md`, `os/skills/catalog.md`,
   `os/context/agentos-inheritance-registry.md`, and the automations table in
   `PLAYBOOK.md`.
2. Run `python3 scripts/sync-playbook-project-surfaces.py` and then its
   `--check` mode before relying on inherited-project rows.
3. Compare those sources with `projects/10-playbook/agentos-system-map.html`.
   Update the map only if its visible names, automation states, or inherited
   project list are stale. Keep the map name-only and nested; do not copy
   detailed procedures, work content, secrets, or private operational state.
4. Open the HTML file in Codex when that capability is available. Otherwise,
   return a clickable absolute local-file link.
5. State that the map is a current snapshot and name any source that could not
   be verified. Do not commit, push, or change the inheritance registry merely
   to make the map look complete.

## Boundaries

- Treat `os/context/agentos-inheritance-registry.md` as the only authority for
  whether an external project inherits AgentOS.
- Treat `os/skills/catalog.md` and the owning project as the authority for
  skills. A catalogued archive is not proof that a skill is installed or active.
- Treat the `PLAYBOOK.md` automations table and its referenced policy files as
  the authority for automation status; do not infer a scheduled job from an
  agent or skill alone.
- Preserve the shadcn/ui-inspired quiet visual language in
  `os/context/design-system.md` when editing the map.

## Monthly Review

Once each month, run this workflow as a manual review. Use the map to recall
installed skills and the documented recurring tasks at each project layer.
Verify a proposed skill archive or removal against its owning source before
changing it; do not remove a skill merely because the map looks crowded.

Show a project-local recurring task only when its owning project documents its
name and schedule. If that source is unavailable, keep the task explicitly
unverified rather than inferring it from an agent or skill.

## Post-Run Learning

After a meaningful map refresh, record only durable source-of-truth or
automation-status lessons. Do not rewrite this skill automatically.
