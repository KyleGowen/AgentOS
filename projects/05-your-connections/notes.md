# Project 05: Your Connections

Status: Complete

Completed: 2026-07-03

## Goal

Document and configure external services, APIs, MCP servers, or CLIs used by the AgentOS.

## Current Connections

| Service | Use | Status | Notes |
|---|---|---|---|
| GitHub | Version control, evidence links, commits, pushes, PRs, and review workflows. | Active | Already catalogued in `PLAYBOOK.md`. |
| Google Calendar | Meeting prep, schedule awareness, and focus-block planning. | Active, personal Gmail currently | Work account still needs authorization if supported by the connector and Workspace policy. |
| Google Drive | Docs, Sheets, Slides, and file discovery for planning and AI coaching workflows. | Active, personal Gmail currently | Work account still needs authorization if supported by the connector and Workspace policy. |
| Atlassian Jira and Confluence | Ticket research, linked source documents, implementation planning, and work source-of-truth lookups. | Desired | High-value next connection. |
| Slack | Async updates and incident context. | Deferred | Requires work admin approval, so it is not part of the current Project 05 path. |
| Excelsior | Personal project automation, card/deck workflows, local app context, and release support. | Future idea | If there were more time, create a custom MCP for Excelsior and add it to AgentOS. |

## Future Connection Ideas

- Create an Excelsior MCP and add it to AgentOS so agents can work with Excelsior project context, common app workflows, card/deck operations, and release support through a real connection instead of only local repo reads.

## Test Prompts

### Google Calendar

```text
Use Google Calendar to pull my meetings for tomorrow and summarize what I should prepare for. Do not create or edit events.
```

### Google Drive

```text
Use Google Drive to find my recent Docs and Sheets from the last 30 days. Summarize the kinds of files you can see. Do not open sensitive docs unless I name them.
```

### Atlassian Jira And Confluence

```text
Read Jira ticket WILD-1234 and any linked Confluence docs. Summarize the goal, acceptance criteria, unknowns, and implementation risks. Do not copy private ticket text into repo files.
```
