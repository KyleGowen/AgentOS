# Decisions

Durable choices that future agents should understand before making related recommendations.

Each entry should include the date, context, decision, reason, and evidence when available.

## 2026-07-03 - Use Repo Files As Intentional Memory

- Context: Codex memories were enabled, but generated memories are local state and may be delayed, skipped, or imperfect.
- Decision: Use `os/memory/` as the intentional AgentOS memory layer and Codex memories as ambient recall.
- Reason: Important project knowledge should be reviewable, portable, and editable.
- Evidence: Codex memory discussion in this thread; `~/.codex/config.toml` now has `memories = true`.

## 2026-07-03 - Memory Should Be A Lightweight Notebook

- Context: Project 04 asks for working memory, persistent memory, and instructions for managing both.
- Decision: Keep memory lightweight, file-based, and separated by domain, with separate work, home, and AgentOS files.
- Reason: Kyle prefers practical systems that are easy to maintain during real project work.
- Evidence: Interview answers: notebook style, end-of-task updates, aggressive compaction, separate project files, and root `AGENTS.md` guidance.

## 2026-07-03 - Keep Work Memory Sanitized

- Context: AgentOS is a personal repository, but Kyle uses it to support Measurabl work.
- Decision: Store sanitized work project summaries, risks, workflows, and source pointers, but not private ticket descriptions, customer-specific details, secrets, or raw private excerpts.
- Reason: Future agents need enough context to help without turning this repo into a private work data store.
- Evidence: `os/context/current-projects.md` privacy boundary and memory interview answers.

## 2026-07-03 - Add Lightweight Repo Guidance For Memory

- Context: Codex does not automatically load `os/memory/README.md` unless directed there.
- Decision: Add a lightweight root `AGENTS.md` that points agents to memory rules and key context files when continuity, decisions, patterns, or AgentOS maintenance are relevant.
- Reason: Memory rules should be discoverable without duplicating the full memory manual.
- Evidence: Kyle answered "yes" to adding root guidance.

## 2026-07-03 - Use Roles Or First Names For People Memory

- Context: People memory can improve collaboration, but it should not become a store of unnecessary personal detail.
- Decision: Use roles, stakeholder groups, first names, or private aliases when helpful.
- Reason: This preserves useful collaboration context while keeping the personal repository appropriately restrained.
- Evidence: Kyle said "Roles or first names is fine."

## 2026-07-03 - Align Course Artifacts To Canonical Project Paths

- Context: The repo had an older `projects/03-memory/` scaffold, while the canonical tracker says Project 04 is `projects/04-your-memory/`.
- Decision: Use `projects/04-your-memory/` as the canonical folder and remove the stale memory scaffold.
- Reason: Duplicate project folders create drift and make future project completion harder to trust.
- Evidence: Kyle chose "align canonical."

## 2026-07-05 - First Job Agent Is AI Office Hours Prep

- Context: Project 06, The Job, asks for a one-page job description for the first agent that runs on this AgentOS.
- Decision: Create the AI Office Hours Prep Agent as the first job agent.
- Reason: Weekly AI office-hours preparation is recurring, bounded, source-groundable, and easier to verify than a broad AI coaching assistant.
- Evidence: Kyle chose weekly office-hours prep, agenda brief output, user-provided inputs, source grounding, and no follow-up drafting during Project 06 planning.

## 2026-07-05 - Split AI Office Hours Prep And Follow-Up

- Context: Kyle wanted AI Coach follow-ups to be a separate agent because he prefers single-responsibility agents.
- Decision: Add the AI Office Hours Follow-Up Agent as a post-session agent instead of expanding the prep agent.
- Reason: Prep and follow-up have different triggers, inputs, outputs, and trust checks.
- Evidence: Kyle asked to do the same for a post-office-hours agent after creating the AI Office Hours Prep Agent.

## 2026-07-05 - PR Review Prep Is A Separate Read-Only Agent

- Context: Kyle wants an agent that finds Measurabl PRs where he is review-requested or mentioned and prepares him to review them correctly.
- Decision: Add the PR Review Prep Agent as a separate read-only agent with a minimal local state file for previously reported merged PRs.
- Reason: Review prep has different inputs, output shape, and GitHub safety boundaries than comment resolution or implementation work.
- Evidence: Kyle requested compact linked PR digests with repository, changed file count, build status, high-level gist, suggested review prompts, and no repeated merged PRs.

## 2026-07-19 - Move Excelsior Work Toward Codex

- Context: Kyle has historically worked on Excelsior in Cursor, and several Cursor skills still exist as source material.
- Decision: Treat Codex as the intended primary working surface for Excelsior going forward, while preserving Cursor skills as archived references and translating durable workflows into Codex skills.
- Reason: Kyle wants Excelsior work to happen in Codex now, so AgentOS should route future Excelsior implementation, skill use, and workflow improvement toward Codex-native context instead of assuming Cursor is primary.
- Evidence: Kyle asked the OS Thought Partner to document that he is trying to work on Excelsior in Codex now instead of Cursor.

## 2026-07-20 - Daily Wanted-Card Scan At 6 AM Pacific

- Context: The public wanted-card monitor had been scheduled every four hours.
- Decision: Run its scheduled scan once per day at 6:00 AM Pacific (`America/Los_Angeles`), while retaining the immediate full-list refresh after a card is added or activated.
- Reason: Kyle requested a lower-frequency automatic search without changing the list-change safety workflow.
- Evidence: `os/automations/wanted-card-listings.md`, `PLAYBOOK.md`, and Codex automation `wanted-card-listings`.

## 2026-07-21 - Replace Daily Efficiency Review With Skill Learning Loops

- Context: The AgentOS had a daily 6:30 AM Pacific automation that reviewed scheduled automations for token and efficiency improvements.
- Decision: Delete the scheduled efficiency-review automation and move efficiency learning into each skill's post-run workflow.
- Reason: Skill-local learning captures real friction at the moment it happens, avoids a broad daily review job, and keeps behavior changes reviewable before they are promoted into `SKILL.md`.
- Evidence: Kyle asked to make the change and delete the scheduled task; `os/agents/os-thought-partner.md` now documents post-run learning rules.

## 2026-08-16 - Use ChatGPT Project As Cross-device Thought-partner Surface

- Context: Kyle wants the OS Thought Partner available across devices and is willing to keep Codex or ChatGPT open while using it.
- Decision: Keep the GitHub AgentOS repository as the durable source of truth and use a ChatGPT Project named `AgentOS / OS Thought Partner` as a portable working surface with selected uploaded source files and explicit project instructions.
- Reason: ChatGPT Projects keep related chats, files, and instructions available across phone, web, and desktop, while local Codex filesystem work remains desktop-bound.
- Boundary: Uploaded project files are snapshots; refresh them after meaningful repository changes. Use Codex with the local folder for edits, tests, and git operations.
- Evidence: `os/agents/os-thought-partner.md`, `os/agents/os-thought-partner-chatgpt-project.md`, and official OpenAI documentation on Projects and ChatGPT Work/Codex.

## 2026-08-16 - Prefer Live GitHub Context For The Thought Partner

- Context: The AgentOS repository is already available at `KyleGowen/AgentOS`, and the cross-device ChatGPT Project should not drift from repository state.
- Decision: Connect ChatGPT's GitHub app to `KyleGowen/AgentOS` and use GitHub as the live source for the OS Thought Partner. Use uploaded files only as a fallback.
- Reason: The GitHub app can search and cite repository code and documentation without maintaining a second manually refreshed copy in ChatGPT.
- Boundary: ChatGPT's GitHub app is read-only for repository analysis; use Codex for edits, commits, pushes, and other repository writes.
- Evidence: `os/agents/os-thought-partner.md`, `os/agents/os-thought-partner-chatgpt-project.md`, and official OpenAI guidance for Connecting GitHub to ChatGPT.

## 2026-08-16 - Make GitHub The Cross-device Memory Protocol

- Context: Kyle wants every signed-in Codex and ChatGPT instance to work from the same AgentOS memory scheme.
- Decision: Treat the committed `main` branch of `KyleGowen/AgentOS` as the only shared durable memory source. Store reusable context in `os/context/` and `os/memory/`, then commit and push it from Codex.
- Reason: GitHub makes the system reviewable, portable, and available to both the ChatGPT GitHub app and local Codex checkouts without pretending that chat history or built-in model memory is synchronized.
- Boundary: ChatGPT/Codex conversation history and built-in memory remain surface-specific. A conclusion is not durable or shared until it is recorded in the repository.
- Evidence: Kyle explicitly requested a shared memory scheme across all signed-in instances; `os/memory/README.md` defines the operating protocol.

## 2026-08-16 - Use ThraxOS For Project 07

- Context: Project 07 was previously scoped to the AI Office Hours Prep Agent, but `KyleGowen/ThraxOS` now contains a working Codex specialist with durable instructions, context, skills, memory, safety boundaries, verification procedures, and real operating history.
- Decision: Use ThraxOS as the Project 07 build. Keep the AI Office Hours Prep Agent and the completed Project 06 record, but do not treat it as the Project 07 candidate.
- Reason: ThraxOS is a stronger demonstration of the course requirement to build a real first agent on top of an intentional operating system.
- Historical completion boundary: Project 07 was completed on 2026-08-16 based on its demonstrated agent architecture and real operating evidence. Project 08 now owns the compact representative invocation, verified result, checklist evaluation, and Kyle's reflection.
- Evidence: `projects/07-working-agent/notes.md` and <https://github.com/KyleGowen/ThraxOS>.

## 2026-08-16 - Give Excelsior Permanent Scoped AgentOS Inheritance

- Context: Excelsior should reuse Kyle's global operating rules without loading
  unrelated AgentOS project context or duplicating large source files on every
  task.
- Decision: Keep a compact global-rules cache, source-category manifest, and
  read-only freshness script in `KyleGowen/excelsior`. Excelsior instructions
  override inherited rules for product and technical behavior; committed
  AgentOS `main` remains authoritative for global identity and governance.
- Boundary: AgentOS stores only compact, durable Excelsior summaries through the
  approved Excelsior write allowlist. Detailed or fast-changing state stays in
  Excelsior, and uncommitted AgentOS changes are never inherited.
- Evidence: Excelsior `AGENTS.md`, `.agentos/`, and
  `docs/current/AGENTOS_INHERITANCE.md`.

## 2026-08-16 - Use shadcn/ui As The Global UI Design System

- Context: Kyle wants a consistent default for all UIs, frontends, and reusable
  visual components, including work performed in AgentOS-aware subprojects.
- Decision: Use shadcn/ui as the default component and design foundation. When
  importing the library is not reasonable, preserve its visual and interaction
  language rather than inventing an unrelated system.
- Inheritance: Treat `os/context/design-system.md` as a global rule that scoped
  subproject inheritance caches must carry or reference with provenance.
- Boundary: Explicit repository design systems, customer requirements,
  technical constraints, or direct Kyle instructions may override the default;
  material overrides should be visible rather than silent.
- Evidence: Kyle's explicit preference on 2026-08-16 and
  `os/context/design-system.md`.

## 2026-08-16 - Track AgentOS Inheritance Per Project

- Context: Kyle is distributing a permanent AgentOS inheritance prompt to
  individual projects and needs reminders when a referenced project has not
  received it.
- Decision: Maintain `os/context/agentos-inheritance-registry.md`, distinguishing
  prompt delivery from verified implementation. Remind Kyle before substantive
  work on an unprompted project, without interrupting trivial mentions.
- Maintenance: Keep a row for every durable project AgentOS knows about. Add a
  `Not prompted` row in the same change that introduces new project context;
  do not rely on unlisted projects as an implicit catch-all.
- Current state: ThraxOS and Excelsior have verified selective implementations.
  ThraxOS's local cache matched committed AgentOS `main`; upstream freshness
  remains explicitly unverified.
- Evidence: `projects/08-test-and-verify/runs/2026-08-16-thraxos-selective-inheritance.md`
  and the verified Excelsior inheritance artifacts recorded in
  `os/context/excelsior.md`.

## 2026-08-17 - Generate Playbook Inherited-Project Rows From The Registry

- Context: Project 10 needs an accurate cross-project ownership map, but
  copying each external project's agents, skills, and runbooks into the main
  playbook would cause drift.
- Decision: Generate the playbook's inherited-project table from
  `os/context/agentos-inheritance-registry.md` with
  `scripts/sync-playbook-project-surfaces.py`. The registry remains the only
  source of truth; detailed project procedures remain in their owning project.
- Verification: The sync script has a `--check` mode that exits nonzero when
  the generated table is stale. Run it whenever an external inheritance status
  changes.
