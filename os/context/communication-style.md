# Communication Style

Last updated: 2026-07-02

Use this file when drafting content in Kyle's tone and style, especially technical plans, design discussions, code review comments, architecture notes, Confluence pages, Slack updates, and disagreement-aware recommendations.

## Source Notes

This file is based on Kyle's stated writing preferences and references to private Confluence examples. The linked examples require Atlassian authentication and were not readable from this workspace at creation time.

Referenced samples:

- MongoDB TimeScaleDB Discussion.
- GRESB 2025 Technical Plan.
- Disclosure SFDR Report Technical Layout.

If pasted or exported samples become available later, use them to tune this file with concrete phrasing examples.

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

Useful section patterns:

- Context.
- Problem.
- Recommendation.
- Options considered.
- Tradeoffs.
- Risks.
- Open questions.
- Next steps.

## Disagreement And Conflict

When writing disagreement-aware content:

- Represent the other side's point of view fairly before responding.
- Avoid strawmen, dunking, or victory-lap language.
- Say why a position is understandable, even if Kyle disagrees with it.
- Use "I think" or "my read is" when the claim is judgment-based.
- Use firmer language when the evidence is strong or the risk is material.
- Prefer "this creates risk because..." over "this is wrong because...".
- Make it easy for the other person to agree without feeling cornered.

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
- Does it acknowledge uncertainty and opposing views where appropriate?
- Does it use humor only where it helps?
- Are code comments, log messages, and technical examples written like a professional human wrote them?
- Would Kyle plausibly put his name on it?
