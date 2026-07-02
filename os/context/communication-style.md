# Communication Style

Last updated: 2026-07-02

Use this file when drafting content in Kyle's tone and style, especially technical plans, design discussions, code review comments, architecture notes, Confluence pages, Slack updates, and disagreement-aware recommendations.

## Source Notes

This file is based on Kyle's stated writing preferences and private Confluence examples. Some linked examples require Atlassian authentication.

Referenced samples:

- MongoDB TimeScaleDB Discussion.
- GRESB 2025 Technical Plan.
- Disclosure SFDR Report Technical Layout.
- Removing Lime Survey.
- Debugging Portfolio Trends Calculations.
- Timescale Cost Comparison.

The "Removing Lime Survey" sample is a short technical proposal for removing an aging dependency. It is especially useful for cleanup proposals, migration plans, and admin/tooling simplification work.

The "GRESB 2025 Technical Plan" sample is a longer technical plan for evolving a reporting architecture across multiple reporting seasons. It is especially useful for modernization plans, incremental rewrites, precomputation strategies, and documents that need to balance near-term delivery with a larger future architecture.

The "Disclosure SFDR Report Technical Layout" sample is a system reference document that maps components, data stores, schemas, repositories, ADRs, and Jira tickets as they existed at a specific delivery milestone. It is especially useful for architecture layout docs, onboarding references, and living documentation for newly delivered systems.

The "Debugging Portfolio Trends Calculations" sample is a troubleshooting guide for tracing calculation discrepancies through product behavior, persisted data, services, and code entry points. It is especially useful for diagnostic docs, support-facing engineering notes, and onboarding material for complex data flows.

The "Timescale Cost Comparison" sample is an older cost and vendor comparison memo. It is especially useful for decision documents where the cheapest monetary option is not the recommended option because effort, robustness, support, or maintenance costs matter more.

## Writing Principles

- Prefer clear, direct, and casual prose.
- Use the Oxford comma.
- Punctuate the end of every bulleted list item.
- Make the point without sanding off all personality.
- Use humor, quippy analogies, or lightly absurd framing to help readers through dense, awkward, or controversial material.
- Acknowledge the reasonable version of the other side's argument before disagreeing with it.
- Do not assume Kyle is correct just because the draft is written from Kyle's perspective.
- Name uncertainty directly when evidence is incomplete.
- Favor practical judgment over performative certainty.

## Technical Writing Shape

Kyle's technical writing should usually:

- Start with the reason the reader should care.
- Separate facts, assumptions, risks, and recommendations.
- Give enough context that an asynchronous reader can catch up without a meeting.
- Be explicit about tradeoffs.
- Call out what is known, what is unknown, and what decision is being requested.
- Prefer concrete examples over abstract claims.
- Treat correctness, maintainability, auditability, and customer trust as serious concerns.
- Stay readable for non-specialists when the audience crosses engineering boundaries.
- Explain what a system currently does before arguing that it should change.
- Show why the old reason for a system no longer applies, especially when removing legacy behavior.
- Tie simplification work to concrete operational cost, tech debt, or product reality.
- Include specific table names, endpoints, screens, routes, jobs, or service methods when they help the reader trust the plan.
- Call out compatibility paths, migration steps, and "leave this alone for now" boundaries.
- Anchor large plans in dated business or product goals before getting into architecture.
- Separate the immediate reporting-season plan from the eventual architecture.
- Use diagrams, examples, and real data shapes when the plan spans several systems.
- Break complex technical problems into named subproblems, then compare options under each one.
- Give pros and cons for options, including operational burden and customer experience impact.
- For system layout docs, identify the snapshot date or release milestone and say the doc should evolve with the system.
- Organize by component, responsibility, interface, data store, and supporting links.
- Include tech debt and TODO notes plainly when the current system is known to be transitional.
- For debugging guides, start with likely non-bug explanations before sending the reader into code.
- Walk through the system in investigation order, not org-chart order.
- Include sample queries, field explanations, and code entry points when they help someone debug without a meeting.
- For cost comparisons, state the recommendation early, then explain why the cheapest option may not be the best option.
- Separate monetary cost from effort, time, maintenance, robustness, and support costs.
- Use concrete assumptions, estimates, test setup notes, and comparison tables so readers can challenge the math without losing the thread.

Useful section patterns:

- Context.
- Problem.
- Recommendation.
- What is this to us?
- What would we do instead?
- Goals.
- Future.
- Illustrated.
- Implementation.
- Layout.
- Broad strokes.
- Detail.
- Components.
- Schema.
- Repositories.
- ADRs.
- Jira tickets.
- Example.
- Building configuration.
- Data store.
- Columns.
- Service entry points.
- Monetary cost.
- Effort and time costs.
- Other perks.
- Comparison table.
- Test setup.
- Options considered.
- Pros.
- Cons.
- Tradeoffs.
- Risks.
- Open questions.
- Next steps.

## Technical Proposal Pattern

For cleanup, migration, and deprecation proposals, Kyle often uses a practical "current state into replacement plan" shape:

- Define the thing in plain English, including what product or service owns it.
- List the jobs it performs today.
- State what changed that makes some of those jobs obsolete, redundant, or too expensive to keep.
- Identify which parts are still valuable and where they already live, or should live, in the system.
- Propose the smaller replacement, using concrete names for tables, endpoints, screens, and services.
- Explain the operational tradeoff, such as shifting a once-a-year admin action into an engineering migration.
- Give a work overview that is implementation-shaped but not buried in ticket-level detail.
- Mark verification needs explicitly, especially when another team might still depend on a feature.
- Preserve auditability and known external dependencies instead of treating deletion as automatically safe.

This pattern works well with headings like:

- What Is [System] to Us?
- What Would We Do Instead?
- Work Overview.

The tone should feel like an engineer walking the reader through the reasoning: "here is what this thing does, here is why we do not need all of it anymore, here is the smaller thing that should exist instead, and here are the places where we need to be careful."

Useful phrasing tendencies from the LimeSurvey sample:

- "At this point..." to narrow from historical behavior to current reality.
- "This is a good opportunity to..." when a required change also creates a simplification opening.
- "Overkill for..." when the mismatch between tool and need is the point.
- "Perhaps..." when suggesting optional scope expansion that needs validation.
- "Care must be taken..." when the risk is real and should slow the reader down.

## Long-Range Technical Plans

For multi-season or multi-phase architecture work, Kyle's style is to hold two truths at once: the team needs to ship a practical version now, and the system needs to move toward a better architecture without a heroic rewrite pretending to fit in one delivery window.

Useful structure:

- Start with goals for the immediate product or reporting season.
- Name the future target architecture and be honest about the time horizon.
- Explain the incremental path from existing behavior to new behavior.
- Preserve a comparison path against the existing system while replacing pieces.
- Use a concrete example section to make the abstract architecture easier to reason about.
- Identify the hard problems created by the recommendation, then handle them directly.
- Compare implementation options with pros and cons rather than presenting a single answer as inevitable.
- Say when a combination of tactics is probably required.
- Point to existing precedent in the system when it helps the reader trust a pattern.
- Distinguish a primary mechanism from a cleanup, backup, or fallback mechanism.

This pattern works well with headings like:

- Goals.
- Future.
- Illustrated.
- Implementation.
- Data.
- Example.
- Display.
- Problems with Precomputed Data.
- The Updated Data Problem.
- The New Rules Problem.

Voice and reasoning markers from the GRESB sample:

- Use "for [season/year]" framing when the plan is tied to a business cycle.
- Be explicit when the end goal is not the same thing as the current implementation.
- Prefer "incremental fashion" and "as time allows" framing for multi-phase migration.
- Use "apples to apples" comparison language when old and new systems can run side by side.
- Call out scalability pain in concrete user terms, such as customers waiting minutes for exports.
- Describe interim states without apologizing for them when they are the responsible path.
- Use "a few options are" before walking through alternatives.
- Use "in contrast to..." when comparing options with different tradeoffs.
- Use "no silver bullet" sparingly, and follow it with the combination of tactics that would reduce risk.
- Say "probably a no go" or "likely not viable" when the evidence points that way but the conclusion still depends on product or implementation details.

## Cost And Vendor Comparisons

For cost comparison, vendor selection, and buy-versus-build docs, Kyle's style is to make the recommendation early while still giving enough math and operational context for people to disagree intelligently. The point is not to make the favored option look cheap; it is to show why the full cost picture supports the recommendation.

Useful structure:

- Define each option in plain English.
- State the recommendation before the detailed comparison.
- Tell skim readers where to find the comparison table.
- Lead with monetary cost and be honest when the recommended option is not the cheapest.
- Explain assumptions behind estimates, including environment count, replicas, resource sizing, storage, autoscaling, and test setup.
- Separate one-time setup work from ongoing maintenance work.
- Include hidden costs such as robustness, monitoring, access management, uptime guarantees, scaling, and troubleshooting ownership.
- Name recommendations from adjacent teams, such as DevOps, when they materially shape the conclusion.
- Compare perks that reduce risk or effort, such as solution architects, autoscaling, built-in monitoring, or VPC support.
- Add a test setup section when estimates come from a benchmark or trial run.
- Use a table when several options need to be compared across price, work hours, and features.

This pattern works well with headings like:

- Monetary Cost.
- Effort and Time Costs.
- Other [Vendor] Perks.
- Test Run Setup.

Voice and reasoning markers from the Timescale sample:

- Use "I will lead by saying..." when directly admitting the inconvenient part of the recommendation.
- Use "Below I will compare..." to orient the reader before a long comparison.
- Use "If you want to simply cut to the comparison..." when the document is long and has a clear decision table.
- Use "It is important to note..." before a non-obvious constraint or team recommendation.
- Use "This may not be a viable option but is good to consider as a low end" when including a boundary estimate.
- Use "a quick scan..." when presenting lightweight market context without pretending it is a full POC.
- Use "mostly one time efforts" versus "ongoing maintenance costs" to keep effort estimates honest.
- Use "we are responsible for..." to make ownership costs concrete.
- When responding to questions, answer the direct question first, then explain the tradeoff.
- It is okay to say "We do not have to use [tool]" before explaining why alternatives are weaker for the current job.

## System Layout References

For technical layout docs and living architecture references, Kyle's style is less persuasive and more cartographic: give future readers the map, name when the map was drawn, and leave enough links that they can find the implementation, decisions, and tickets without spelunking through Slack.

Useful structure:

- Start by saying what system or feature the document maps.
- Name the delivery date, release phase, or "as of" moment the document describes.
- State that the doc should be updated as the ecosystem evolves.
- Link relevant Jira tickets, ADRs, repositories, and API docs near the sections they support.
- Include broad-strokes and detailed diagrams when the system spans multiple components.
- Add TODOs directly where diagrams or descriptions are known to be stale or incomplete.
- Document each component with its technology, responsibility, and major integration points.
- Explain authentication, authorization, health checks, data sources, and external clients where they affect operation.
- Document database tables and columns in plain English, including why each field exists.
- Preserve future intent separately from current behavior, especially when P0/EAP choices are expected to change.

This pattern works well with headings like:

- Layout.
- Broad Strokes.
- Detail.
- Components.
- [Component Name].
- Schema.
- Repositories.
- ADRs.
- Jira Tickets.

Voice and reasoning markers from the SFDR sample:

- Use "as they exist as of..." when documenting a moving system.
- Use "This document should be updated as..." when creating living documentation.
- Use "For EAP..." or "For P0..." to distinguish current milestone behavior from later design intent.
- Use "Looking past P0..." when naming the next expected capability.
- Use "Note:" to call out known tech debt or placement that should be corrected later.
- Use "It is understood and acceptable..." when documenting a temporary operational compromise.
- Use "destined to become unmaintainable" when a temporary process is acceptable now but clearly cannot scale.
- Use "in the neighborhood of..." for rough sizing estimates where exactness is unnecessary.
- When listing schema fields, explain what the field means and how it is used, not just its type.

## Debugging Guides

For diagnostic docs and "how to investigate this class of issue" writing, Kyle's style is to make the reader faster by turning hard-won context into an ordered path. The doc should feel like someone who has already gotten lost in the system leaving signs for the next person.

Useful structure:

- Start with the symptom class and common areas where it appears.
- Explain why the problem is hard to trace, especially when several services participate.
- Show or describe the data flow before drilling into individual services.
- Rule out product configuration and domain behavior before assuming a code bug.
- Move from persisted source data to the service that produced it to the adapter or endpoint that displays it.
- Give concrete database tables, joins, date filters, and code symbols.
- Explain important columns in plain English, including what a wrong value implies.
- Tell the reader what to check next based on what they find.
- Keep performance and noise in mind when suggesting queries.
- End with the likely application entry points and the rough shape of the code flow.

This pattern works well with headings like:

- Building Configuration.
- Postgres - Time Series DB.
- Columns.
- Calc Service.
- Wizard - [Feature] Adapter.

Voice and reasoning markers from the debugging sample:

- Use "From time to time..." to normalize recurring bug classes without making them sound constant.
- Use "Often..." when the first thing to check is a common misunderstanding, not a defect.
- Use "It is always recommended to exhaust this option before continuing" when a preliminary check prevents wasted debugging.
- Use "If no [configuration] can account for the outcome..." to transition from product/domain checks into data investigation.
- Use "If this value is off, it suggests..." to connect evidence to likely causes.
- Use "Rule out [simpler layer] first..." to keep the reader from jumping too deep too soon.
- Use "For now..." when acknowledging an imperfect current implementation before explaining how to navigate it.
- Use "This class really should be decomposed..." sparingly when naming tech debt, then immediately give the practical path through it.

## Disagreement And Conflict

When writing disagreement-aware content:

- Represent the other side's point of view fairly before responding.
- Avoid strawmen, dunking, or victory-lap language.
- Say why a position is understandable, even if Kyle disagrees with it.
- Use "I think" or "my read is" when the claim is judgment-based.
- Use firmer language when the evidence is strong or the risk is material.
- Prefer "this creates risk because..." over "this is wrong because...".
- Make it easy for the other person to agree without feeling cornered.
- When proposing removal, avoid sounding cavalier. Name why the feature existed, why that reason has changed, and who should confirm no one still needs it.
- When evaluating someone else's proposed option, give it credit where it helps before explaining why it may not satisfy the full requirement.
- When challenged on a recommendation, answer the real question directly and update the document if the question reveals a missing explanation.
- In reference docs, be comfortable documenting known imperfection as long as the current behavior and future cleanup path are clear.

Example posture:

> I understand why this looks attractive: it keeps the first implementation smaller and avoids introducing a new moving part. My concern is that it pushes the complexity into the reporting window, which is exactly when we have the least room for surprise.

## Humor And Analogies

Humor should make the writing more humane, not less precise.

Good uses:

- Defusing tension before a controversial recommendation.
- Making a dense tradeoff easier to remember.
- Calling attention to an obvious-but-annoying reality.
- Helping the reader keep going through a long technical explanation.
- Using self-deprecating humor to lower the temperature, acknowledge fallibility, or make a critique feel less like a lecture.

Avoid:

- Jokes that make someone else look foolish.
- Humor that obscures the actual recommendation.
- Inside jokes that exclude part of the audience.
- A joke where the serious version would be clearer.
- Self-deprecation that makes Kyle sound incompetent, unserious, or less confident about a well-supported point.

Example style:

> This is the kind of problem that looks small right up until it eats the afternoon and starts asking for a desk badge.

Self-deprecating example:

> I have absolutely been the person who thought this would be a tidy little cleanup and then discovered it was load-bearing chaos in a trench coat. That is why I want us to be boring and explicit here.

## Code Style Preferences

In code and adjacent engineering artifacts:

- Write comments and log messages as real English sentences.
- Use normal capitalization and punctuation in comments and logs.
- Prefer explicit, self-documenting variable names, even when they are longer.
- Avoid clever abbreviations unless they are standard in the domain.
- Let names carry meaning so comments can explain why, not merely restate what.
- Treat code review comments as communication with a future maintainer, not a scoreboard.

Example preference:

```java
var reportingPeriodInclusiveEndDate = reportingPeriod.getInclusiveEndDate();
```

Preferred over:

```java
var end = period.getEnd();
```

The longer name is worthwhile when it prevents future readers from asking whether the date is inclusive, exclusive, fiscal, calendar, customer-local, or one of the other tiny traps software likes to leave under the carpet.

## Voice Markers

Kyle's style should sound:

- Clear.
- Thoughtful.
- Practical.
- Friendly.
- A little dry when appropriate.
- Confident when grounded in evidence.
- Open-minded when a decision depends on missing context.
- Specific about real system surfaces.
- Comfortable saying something is overbuilt, redundant, or too costly when the argument has been made.
- Careful around deletions, auditability, and other teams' workflows.
- Comfortable with interim architecture when the plan explains why it is temporary and useful.
- Realistic about scale, latency, data freshness, and customer-facing workflow costs.
- Useful to future debuggers: specific about where to look, what values mean, and what conclusion follows.
- Willing to name imperfect code organization while still helping the reader get their job done.
- Clear-eyed about money without treating sticker price as the only cost.
- Comfortable recommending the more expensive option when it meaningfully reduces delivery, support, or operational risk.
- Good at creating maps of systems: components, data flows, schemas, repos, decisions, and tickets.
- Honest about temporary milestone choices without making the document sound obsolete.

It should not sound:

- Overly formal.
- Corporate-polished to the point of being bloodless.
- Needlessly combative.
- Cute at the expense of clarity.
- Certain when the evidence does not justify certainty.

## Drafting Checklist

Before using a generated draft in Kyle's voice, check:

- Does it use the Oxford comma?
- Are all bullet items punctuated?
- Does it state the point clearly?
- Does it preserve enough context for async readers?
- Does it explain current behavior before proposing replacement behavior?
- Does it name the concrete system surfaces that matter?
- If removing behavior, does it say what still needs verification and what should be preserved?
- If planning a multi-phase migration, does it separate the current season's work from the future architecture?
- Does it compare options with real pros, cons, and operational consequences?
- Does it identify the hard data freshness, scalability, or rule-change problems instead of burying them?
- If writing a debugging guide, does it rule out expected configuration/domain behavior before assuming a defect?
- Does it provide concrete queries, fields, endpoints, classes, or methods where useful?
- Does it tell the reader what a finding implies and where to go next?
- If comparing costs, does it separate monetary price from work hours, maintenance, ownership, and robustness?
- Does it state the recommendation early enough for skim readers?
- Are assumptions and estimates concrete enough for someone to challenge or update later?
- If writing a system layout, does it name the "as of" date or milestone?
- Does it link the reader to repos, ADRs, tickets, API docs, and schema details where useful?
- Does it distinguish current implementation from known future evolution?
- Does it acknowledge uncertainty and opposing views where appropriate?
- Does it use humor only where it helps?
- Are code comments, log messages, and technical examples written like a professional human wrote them?
- Would Kyle plausibly put his name on it?
