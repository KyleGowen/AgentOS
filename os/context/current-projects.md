# Current Projects

Last updated: 2026-08-13

Status scope: personal-project status was audited on 2026-08-13 against the
available local source repositories and artifacts below. Work-project details
remain high-level context and were not revalidated in this pass; consult Jira,
Confluence, GitHub, or Slack before using them for work planning or
prioritization.

This file tracks ongoing work, home projects, hobbies, and life context that may affect planning, prioritization, drafting, and agent routing.

If this file is more than 30 days old, warn Kyle before using it for planning or prioritization.

## Privacy Boundary

- Keep work project details high-level in this personal repository.
- Avoid personally identifying information.
- Work ticket IDs are acceptable, but do not include ticket descriptions here.
- Source-of-truth work details live in Jira, Confluence, GitHub PRs, and Slack.
- Never invent work methodology, business rules, or customer-facing claims. Ask for sources.

## Current Themes

- GRESB reporting season is winding down, but work upkeep remains important because some customers have reporting extensions.
- Excelsior v2 recently shipped, people like it, and that momentum is exciting.
- Link is becoming trustworthy off leash, which is a meaningful personal milestone.

## Work Projects

### GRESB Reporting Season

GRESB is a real estate investment reporting framework with an ESG focus. At Measurabl, Kyle helps lead engineering work that reports customer building utility and waste data according to GRESB's yearly methodology.

Current importance:

- Highest work priority for at least the next two weeks as of 2026-07-01.
- The main reporting deadline was 2026-06-30, but some customers have extensions.

Kyle's role:

- Implementer
- Technical lead
- Reviewer
- Firefighter
- Mentor
- Customer Success support

Recurring responsibilities:

- Update code to align with GRESB's changed reporting rules each year.
- Help ensure customer building utility and waste data is reported correctly.
- Support Customer Success and paid customers during reporting season.
- Review changes conservatively and ask for source documents when methodology is unclear.

Stakeholders:

- Customer Success
- Paid customers supported by Customer Success
- Directors of Sustainability at large REITs
- Property managers
- Fund managers

Risk profile:

- Misreporting data is the biggest no-no and can be a showstopper.
- Past data reporting problems have caused customer and financial loss.
- Common serious bugs include misrepresenting building utility data, emissions, data buckets, or building floor areas.
- Double-counting data is a showstopper.

Agent instructions:

- Never invent GRESB methodology rules.
- Be conservative with changes.
- Always ask for sources when rules, methodology, emissions, floor area, or bucketing are involved.
- Treat accuracy, auditability, and customer trust as more important than speed.

### Data Locking

Data locking prevents customer data from changing after it has been audited. This matters because Measurabl has automated utility data acquisition, and new incoming data can otherwise change audited data and invalidate reports.

Scope:

- Lock building, meter, and meter reading data for a date range.
- Preserve audited customer data.

Status:

- Backend work is complete.
- Handed off to the Data Manager team, which will implement the self-service interface.

Kyle's role:

- Implementer
- Technical lead

Stakeholders:

- Customer Success
- Product
- Customers
- Auditors

Agent instructions:

- Preserve the distinction between backend locking behavior and future self-service interface work.
- Treat audit consistency and data preservation as the core purpose.

### AI Coaching For Non-Engineers

Kyle is the AI Coach for non-engineering colleagues at Measurabl. He holds office hours and helps one-on-one with projects in Gemini and Claude.

Common coaching requests:

- Move data from one proprietary or spreadsheet source to another.
- Generate spreadsheet-based debriefs to send over Slack.
- Choose appropriate AI tools and understand best practices.
- Start from vague, uncertain requests and turn them into small next steps.

Kyle's role:

- AI Coach
- Mentor
- Unblocker

Coaching style:

- Prefer building the thing with the person when time allows.
- In office hours, focus on unsticking people and moving them further along.
- Good coaching means the recipient understands enough that they should not need to return for the same problem.

Routing:

- Create and use `os/context/ai-coaching.md` for deeper coaching patterns, templates, and office-hours notes.
- Kyle is also tracking this project with Claude Co-Work.

### Legacy Core Maintenance And Incidents

Kyle helps maintain legacy Core applications and assists with incidents.

Typical incident flow:

- Respond to Datadog and Sentry alerts in Slack.
- Find the right domain owners.
- Work with domain owners to ship a hot fix when needed.
- Stay involved until it is clear Kyle is no longer needed.
- Sometimes own the code fix directly.

Kyle usually does not:

- Run incident retros.
- Own incident channels.

Agent instructions:

- Help diagnose, summarize, and route incidents.
- Look for domain ownership before assuming Kyle owns the fix.
- Keep incident documentation high-level in this repo.

### Mentoring Juniors And Contractors

Kyle mentors junior engineers and contractors and helps them become capable engineering team members.

Focus areas:

- Software engineering best practices.
- Business rule context and history.
- Code quality and coding standards.
- Debugging, ownership, and judgment.

Notable context:

- Kyle had a mentee progress from intern to senior engineer while working with him. He now considers her a colleague rather than a mentee.

## Personal Projects

### Personal Project Status Audit

| Project | Status on 2026-08-13 | Evidence | Confidence / next action |
|---|---|---|---|
| Excelsior | Active development; v2/product work is ongoing | `/Users/kyle/cursored` is on `main` at `2fc8a1a7` dated 2026-08-01; the older `/Users/kyle/Projects/excelsior` checkout is at April 11 | High for local code status; production/runtime health was not verified because DNS and local services were unavailable. Reconcile the two checkouts before implementation. |
| Home Media Server / Korlash | Rebuild remains unverified and documented as awaiting minimal boot | Local repo last changed 2026-05-22; README and WIP tracker still describe the pre-boot rebuild plan with all execution checklists open | Medium for documented state, low for physical live state. Confirm hardware/Windows/drive status through the server or a fresh Korlash update. |
| DDR/ITG Machine | Active hobby project, current operational status unverified | AgentOS snapshot is from 2026-07-05; documented source repos were not present locally and remote refresh failed in this run | Low for current activity/data. Refresh `itgmania-backup` and `Thraximundar-Backup` before summarizing recent play or backup health. |
| Vimanas | Paused / background | `os/context/current-projects.md` concept and routing notes | High for priority state; no active implementation source was found or needed. |
| Planted | Personal/background concept; not separately status-tracked | `os/context/current-projects.md` description and personal-only routing note | Medium; create a dedicated project context only if it becomes active. |

### Excelsior

URL: <https://excelsior.cards>

Repository: <https://github.com/KyleGowen/excelsior>

Excelsior is Kyle's main personal software project and creative outlet. It is a web app for OverPower, a trading card game Kyle has played since childhood.

What it does:

- Browse a card database with images.
- Build and share decks.
- Track card collections.
- Serve a community of roughly 50 users.

Audience:

- Kyle as collector and deck builder.
- Online OverPower players like Kyle.
- The small community of people who play and collect the game.

Why it matters:

- Kyle built it from scratch to fill a real community need.
- The deck builder has received enough attention that the game owners contacted Kyle and have loosely asked about contracting in the future.
- It is emotionally important and should be treated as more than a disposable side project.

Current state:

- Excelsior v2 has shipped with the UI overhaul and community surfaces.
- The active local development checkout is `/Users/kyle/cursored`, whose latest
  local commit is `2fc8a1a7` on 2026-08-01 (`Add deck privacy visibility toggle`).
- `/Users/kyle/Projects/excelsior` is an older April checkout; do not treat it
  as the current implementation without reconciling it with `/Users/kyle/cursored`.
- Production and local runtime health were not verified during the 2026-08-13
  audit because DNS and the local `:8085`/`:5173` services were unavailable.

Near-term priorities:

- Add decks from the last tournament to the tournament deck section.
- Add the next card set, likely Skybound or The Few and the Cursed.

Care points:

- User data preservation is essential.
- Avoid service disruption.
- UX must work well on desktop and mobile.
- Treat the game-owner relationship delicately.

Tech stack summary:

- React 19 SPA with TypeScript.
- Vite 6, React Router 7, TanStack Query 5.
- Component-scoped CSS plus shared design tokens.
- Node.js and Express 4 backend in TypeScript.
- PostgreSQL with Flyway migrations.
- Session cookie auth plus newer JWT/Bearer routes where applicable.
- Zod, bcrypt, Firebase Admin, Pino, Helmet, CORS, compression.
- Jest, ESLint, Knip, Trivy, SOC 2 checks on HTTP changes.
- Production infrastructure uses AWS EC2, RDS PostgreSQL, S3, CloudFront, Docker, and Terraform.

Routing:

- If a request touches Excelsior, use this file as a summary.
- Prefer `os/context/excelsior.md` for detailed project context.
- Ask Kyle before touching production-impacting behavior or user data.

### Home Media Server

Repository: <https://github.com/KyleGowen/plex-server-hardware>

Context: `os/context/home-media-server.md`

Home Media Server is Kyle's Windows-native Plex server and media automation ecosystem. It documents and supports the Korlash Plex server, including Plex and qBittorrent on Windows plus a Docker media stack for the Arr ecosystem and related services.

Current state:

- The project remains active as a home operations project, but its current
  physical state is not verified in this workspace.
- The local source repo last changed on 2026-05-22. Its README and rebuild WIP
  tracker still describe the pre-boot plan: wait for parts, boot with the OS
  SSD only, then reconnect media drives incrementally.
- Do not carry forward the 2026-07-05 "stable" claim without a fresh server-side
  check or user update.
- AgentOS should keep summary-level project context; the GitHub repo remains the source of truth for detailed inventories, service docs, media ledgers, crash history, and operational scripts.

Near-term priorities:

- Balance operational reliability with media automation work.
- Keep drive/path safety, backups, service validation, skill sync, media additions, downloads/imports, collections, and poster curation in view.

Remote workflow:

- Kyle often uses Codex remotely from a mobile device because the server usually does not have a monitor attached.
- Parsec is the fallback remote desktop path when a GUI session is needed.
- Agents should prefer concise, stepwise output that works well in a mobile remote session.

Care points:

- Do not format, initialize, repartition, wipe, or casually change existing media drives.
- Confirm drive letters, qBittorrent paths, and Docker bind mounts before trusting media automation after boot, crash, Docker restart, WSL restart, or storage work.
- Treat Plex tokens, Arr API keys, qBittorrent credentials, tracker data, cookies, passkeys, and provider credentials as secrets.
- Avoid mirroring detailed media library, collection, torrent, tracker, or credential data in AgentOS.

Routing:

- Use `os/context/home-media-server.md` for durable project context.
- Use the Plex repo for detailed current state and source docs.
- Read-only checks are acceptable when relevant.
- Plex writes, downloads, deletes, path repairs, drive changes, service setting changes, and other live-server mutations require clear user intent or confirmation.

### DDR/ITG Machine

Tooling repository: <https://github.com/KyleGowen/itgmania-backup>

Backup and digest repository: <https://github.com/KyleGowen/Thraximundar-Backup>

Context: `os/context/stepmania-ddr.md`

DDR/ITG Machine is Kyle's StepMania, DDR, and ITGMania hobby-log project. The physical Windows nukbox machine is Thraximundar. The project is primarily about rhythm-game play, exercise, score history, and progress over time, with backup tooling preserving saves and producing score digests.

Current state:

- Scheduled backups and digest generation were documented as working on
  2026-07-05, but current operation was not reverified because the source repos
  are not present locally and remote refresh failed during this audit.
- Kyle plays for exercise about 1-2 times per week.
- The ITGMania backup tool protects install and save data, but songs are intentionally not backed up.
- The backup and digest repo remains the source of truth for scores, play history, and generated digest evidence.

Fitness and progress framing:

- Treat DDR/ITG as a fun exercise habit and rhythm-game skill project.
- Use play cadence, song time, difficulty range, and score improvement as lightweight fitness and progress signals.
- Avoid medical claims or prescriptive fitness advice.

Agent default:

- Act as a digest coach: summarize recent activity, trends, progress, and notable scores from the backup digest.
- It is acceptable to mention non-secret score details, representative songs, player labels, levels, percentages, play time, and digest summaries.
- Protect GitHub PATs, local `config.json`, private credentials, raw backup files, and unnecessary personal detail.

Routing:

- Use `os/context/stepmania-ddr.md` for durable project context.
- Use `KyleGowen/itgmania-backup` for backup tool behavior, install flow, cron, digest generation, and score parsing.
- Use `KyleGowen/Thraximundar-Backup` for current score, backup, and digest evidence.
- Read and summarize freely; force-push, restore, schedule changes, save/config edits, backup repo mutation, or live machine mutation require explicit confirmation.
- Give remote-friendly Windows guidance when useful.

### Vimanas

Vimanas is a paused personal game project.

Concept:

- Top-down space fighter shooting game.
- Similar inspirations include 1942, R-Type, and Gradius.
- Currently proof of concept only.
- Kyle has been designing ships, levels, enemy patterns, and related gameplay ideas.

Agentic development goal:

- Kyle wants an agentic SDLC and agentic development team that can eventually build substantial content from high-level requests.
- Example target: "build me level 17, I want it in a swamp setting with insectoid style enemies, it should be 2 minutes long with a boss at the end."
- The long-term goal is for the agent team to implement that level with only minor tweaks afterward.
- This system is far from that state today.

Routing:

- Treat Vimanas as paused or background unless Kyle explicitly invokes it.
- Capture ideas when they appear, but do not prioritize it over active projects without asking.

### Planted

Planted is a personal plant care app. It may eventually be shared with friends and family, but should be treated as personal-only for now.

What it does:

- Accepts a picture of a plant.
- Identifies genus and species.
- Provides biological facts.
- Generates a watering plan.
- Gives health tips based on the visual image.
- Tracks pruning, watering, fertilizing, and related care events.
- Includes a display mode intended for a digital picture frame style device.

OpenAI usage:

- Genus and species identification.
- Bio fact content.
- Care tips.
- Health assessment.

Routing:

- Treat Planted as personal context unless Kyle explicitly asks to productize it.
- A future plant-care context can go deeper on individual plants, goals, and recurring care problems.

## Hobbies And Life Context

Keep this section lightweight unless Kyle asks to pull on a specific area.

### Trading Card Games

Magic: The Gathering:

- Kyle mostly cares about kitchen table Commander and sometimes Limited, especially draft.
- He likes deckbuilding and has many Commander decks.
- Moxfield: <https://moxfield.com/users/BlazeOfIth>

OverPower:

- Kyle is a player and competes monthly in a West Coast webcam league.
- He usually does not play OverPower in person like he does with Magic.
- He is acquainted with the current game company, some content creators, and current tournament champions, but does not know them well.
- Excelsior is tightly connected to this hobby.

### Board Games

Current games and interests include:

- Gloomhaven: Jaws of the Lion
- Spirit Island
- Tsuro
- King of Tokyo
- King of Monster Island

### Comic Books

Kyle mostly reads Marvel, with some other current pulls.

Current pulls include:

- Amazing Spider-Man
- Absolute Batman
- Absolute Green Lantern
- Daredevil
- Incredible Hulk
- Fantastic Four
- Transformers
- Ultimate Spider-Man
- Ultimate Wolverine

### Plants And Gardening

- Kyle has indoor and outdoor plants.
- He has goals for each plant and likely recurring care problems, but those should be captured later in a more specific context file if needed.

### Link

Link is Kyle's relatively new young dog. He is a mixed dog, mostly Australian cattle dog and pit bull.

Current context:

- Kyle is training Link and helping him become a member of the family.
- Link has become much better off leash, and Kyle can now trust him in the world not to run away.
- Link's biggest issue is attachment to Kyle.
- Link chews things when home alone or when he does not have access to Kyle.

### Indoor Climbing

- Kyle climbs once a week and trains once a week outside the gym.
- Current goal: become solid on V3s.
- Secondary goal: get his daughter interested in climbing.
- His daughter comes with him once a week.

## How Agents Should Use This File

- Use this file to draft updates, remember recurring context, prioritize work, create plans and outlines, identify automation opportunities, and recognize overlapping patterns.
- When work and personal projects conflict, give Kyle options rather than choosing unilaterally. He sometimes wants to shut off work.
- Keep work and home projects separate. Home projects should not influence work projects, but work patterns may inform home project process when useful.
- If a task belongs to a more specific context file, route there when it exists. If it does not exist yet, use this file as the summary and suggest creating the narrower file.
- Preserve Kyle's distinction between active, paused, and lightweight hobby context.
