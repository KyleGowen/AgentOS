# Engineering Review

Last updated: 2026-07-02

Use this file when reviewing engineering work for Kyle. This is universal review
context, with a specific section for GRESB and reporting changes.

Source note:

- This file is generated from Kyle's interview responses on 2026-07-02.
- Do not add review preferences here unless Kyle has explicitly provided them.

## Review Posture

Kyle's highest review priority is data accuracy and reporting accuracy.

After that, Kyle looks for:

- Efficiency issues.
- Opportunities to improve performance.
- Opportunities to reduce machine work.
- Variable naming conventions.
- General coding best practices Kyle believes in.

Kyle generally lets Co-Pilot or Unblocked handle obvious syntax problems and
obvious errors.

Kyle will not approve a PR if it lacks tests that exercise new paths or updated
tests for changed paths, except in cases where tests are not reasonable, such as
documentation-only changes or some particular sections of the Measurabl frontend
code.

Urgency rule:

- Hard stops remain.
- Preferences can go.

## What To Prioritize

Prioritize issues in this order:

1. Data accuracy and reporting accuracy.
2. Behavioral accuracy.
3. Automated tests for new paths and changed paths.
4. Efficiency and performance.
5. Naming and readability.
6. General coding best practices.

Hard-stop data and reporting risks:

- Data is misrepresented.
- Behavior is inaccurate.
- Data is double-counted.
- Data is missing.
- Data is placed into incorrect fields.
- Output uses `null` where `0` is expected, or `0` where `null` is expected.
- Tests exercise incorrect behavior.
- Floor areas are misrepresented.

Feature-readiness risks:

- Integration tests are not added when developing a new feature.
- A new Controller class is added without accompanying integration tests.

Efficiency and performance issues worth calling out:

- A `for` loop hits the database on every iteration.
- Code makes extraneous trips to the database.
- Code makes extra calls to other services over the network.
- High-traffic, low-change calls may have caching opportunities.

When calling out caching opportunities, acknowledge that cache eviction work
would need to go with it.

Naming and readability issues that need attention:

- Non-descriptive names.
- Abbreviations that are not defined or well known.
- Vague names that could mean more than one thing.
- Completely unrelated names, such as `x` or `object`.

Minor styling, formatting, performance improvements, and naming conventions can
be mentioned without blocking when they are preferences and do not affect
behavior or self-documentation.

## Java And Backend Practices

Kyle consistently looks for these Java and backend review issues:

- Do not log and throw. Throw the message that would have been logged.
- Protect Java code from `NullPointerException` risks.
- Avoid bespoke code when out-of-the-box framework features would solve the
  problem.
- Avoid stuttering code with long `if` / `else` chains when a `switch`, factory,
  dependency injection, or specialized objects would structure it better.
- Avoid repeated database calls in loops by pulling needed data into a `Map<>`
  above the loop and referring to the map inside the loop.

## Review Comment Style

Kyle does not explicitly label review comments with severity labels such as
`blocking`, `nit`, `question`, or `suggestion`. The wording should carry the
severity.

For blocking comments, use direct but non-combative wording, such as:

- "I think this may create a risk because..."
- "I'm pretty sure this is going to cause X."
- "This will need to change before we merge because of X."

For non-blocking recommendations, use wording such as:

- "This is just a recommendation but we could also do X."
- "What do you think about X?"
- "What if we structured this code block like [code snippet]? Do you prefer
  that?"
- "I think we could squeeze a little bit more efficiency out of this code if we
  do X."

When disagreeing with an approach, Kyle likes to:

- Supply a code snippet.
- Explain the tradeoff.
- Ask the author to make their choice.

Avoid tones that sound:

- Demanding.
- Angry.
- Frustrated.
- Annoyed.
- Belittling.

## Mentoring Review Mode

When reviewing work from lower-titled colleagues, Kyle uses a softer tone and
asks questions.

Kyle does not ask for revision unless the issue breaks a hard rule or will
misrepresent customer data.

Useful mentoring-style phrasing:

- "What do you think about X?"
- "What if we structured this code block like [code snippet]? Do you prefer
  that?"
- "I think we could squeeze a little bit more efficiency out of this code if we
  do X."

## Tests And Verification

Kyle expects automated tests for new paths and changed paths.

Expected test types:

- Unit tests.
- Integration tests when there are large behavioral changes.
- Integration tests for new features.
- Integration tests when adding entirely new Controller classes.

Kyle specifically expects integration tests when:

- A bug can be easily tested with a black-box approach: set up data, call the
  endpoint, and verify the output.
- A new Controller class is added.
- A new feature is being developed.

PR descriptions should include evidence that testing happened, such as:

- Screenshots.
- A human-written testing description.
- Copy-pasted output.

Manual testing is only enough for:

- Label changes.
- Text changes.
- Files that do not diff usefully in GitHub, such as images or `.xlsx` files.

Manual testing is not enough for logic additions.

Bad tests include:

- Tests that exercise incorrect behavior.
- Assertions that are not specific.
- `any()` matchers in assertions.
- `any()` matchers in mocked `when()` clauses where they can lead to false
  positives.
- Tests that cover more than one concept.
- Tests that are hard to read.
- Tests that are too long.
- Tests that look cluttered enough that readers will have a hard time.

Acceptable uses of `any()`:

- `verify(never(any()))`-style assertions.
- Test file setup.

If a change is hard to test, the author should ask for help testing.

## GRESB And Reporting Review

GRESB and reporting changes require extra care because Kyle's highest review
priority is data accuracy and reporting accuracy.

Expected source evidence:

- An engineer would cite a Jira ticket.
- The Jira ticket should be written by Product, currently Neil Pegram or Zach
  Shelin.
- Kyle and Kristen Mulder are often called on to explain or know of methodology
  nuances or changes.
- Kyle has a Gemini Gem that helps detect year-over-year rule changes, but do
  not add details about that Gem unless Kyle provides more context.

If methodology is unclear, or someone says "Product said this is right," ask for
a link to the decision. There must be a written record to refer to.

GRESB and reporting hard stops:

- Data ends up in the wrong field.
- Data is overcounted.
- Data is missing.
- Floor areas are misrepresented.

Areas that need extra suspicion:

- Emissions data, specifically the factors used to get CO2 data.
- Floor area distribution when dividing up a building.
- Date ranges that overlap month or year boundaries.
- Aggregation.
- Loss of data precision.

GRESB and reporting PR descriptions should include:

- How the behavior worked last year.
- How the behavior is changing for this year.
- An integration test in `gresb-integration-tests` that replicates the new
  behavior, or an update to an existing test that adds the new behavior.
