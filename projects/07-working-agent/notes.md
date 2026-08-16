# Project 07: The Build

Status: In progress

Last audited: 2026-08-16

Course page: <https://aidbagentos.ai/projects>

## Goal

Use ThraxOS as the first demonstrated working agent built on Kyle's agentic OS
principles. ThraxOS is the checked-in Codex control plane and specialist for
Thraximundar, Kyle's dedicated Windows 11 ITGMania machine.

Repository: <https://github.com/KyleGowen/ThraxOS>

## Candidate Agent

ThraxOS.

The AI Office Hours Prep Agent remains a valid AgentOS job definition from
Project 06, but Kyle explicitly selected ThraxOS as the Project 07 build on
2026-08-16 because it has stronger evidence of a complete, operating agent.

## Requirement Mapping

| Build requirement | ThraxOS evidence |
|---|---|
| Specific job | Safely operate and maintain Thraximundar, ITGMania, StepManiaX, GrooveStats, song packs, play statistics, backups, and machine memory. |
| Agent identity and instructions | `.codex/agents/thraxos.toml` and root `AGENTS.md`. |
| Dedicated context | `docs/context/` plus host paths under `config/`. |
| Reusable skills | `.agents/skills/thraxos/` and its read-only/guarded scripts. |
| Memory | `memory/FACTS.md`, `DECISIONS.md`, `PREFERENCES.md`, and `OPERATIONS_LOG.md`. |
| Safety boundaries | Root `AGENTS.md`, relevant runbooks, secret-redaction rules, approval gates, and rollback requirements. |
| Real operation | Checked-in operations history and status/backup-health procedures against the physical Thraximundar host. |
| Verification | Live-state-first rules, dated observations, read-only health scripts, parsing checks, backup checks, and explicit evidence labels. |

## Why It Qualifies

ThraxOS is not only a prompt or proposed agent. It has a callable Codex
specialist, durable operating instructions, machine-specific context, reusable
skills, guarded tooling, persistent memory, explicit authorization boundaries,
and records of real work. This satisfies the Project 07 intent to build a first
agent on top of an intentional operating system.

The ThraxOS repository owns detailed machine state. AgentOS stores only the
course decision, summary context, evidence links, and completion record.

## Completion Target

Before marking Project 07 complete, capture a compact, sanitized representative
ThraxOS invocation and verified result in this project folder. The evidence
should demonstrate:

- The ThraxOS specialist was invoked for a real task.
- It loaded its operating contract, memory, and relevant context.
- It used a relevant skill or runbook.
- It respected an authorization or privacy boundary.
- It verified the result from live or source-grounded evidence.
- Kyle recorded a short reflection on what worked and what should improve.

## Current State

The working agent already exists in `KyleGowen/ThraxOS`, and its architecture
maps cleanly to Project 07. AgentOS now recognizes ThraxOS as the selected
build. Completion remains open only for the compact course evidence record and
reflection described above.
