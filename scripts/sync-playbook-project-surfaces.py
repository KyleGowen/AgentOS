#!/usr/bin/env python3
"""Project inherited AgentOS surfaces from the registry into PLAYBOOK.md."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = ROOT / "os/context/agentos-inheritance-registry.md"
PLAYBOOK_PATH = ROOT / "PLAYBOOK.md"
BEGIN_MARKER = "<!-- BEGIN GENERATED INHERITED PROJECT SURFACES -->"
END_MARKER = "<!-- END GENERATED INHERITED PROJECT SURFACES -->"
REGISTRY_HEADER = (
    "| Project | Repository | Prompt status | Implementation status | Evidence / next check |"
)


def cell(value: str) -> str:
    """Return a Markdown-table-safe cell without inventing new project facts."""
    return value.replace("|", "\\|").replace("\n", " ").strip()


def render_source(value: str) -> str:
    value = value.strip()
    if value.startswith("<https://") and value.endswith(">"):
        url = value[1:-1]
        return f"[{url}]({url})"
    return f"`{value}`"


def read_inherited_projects(registry_text: str) -> list[dict[str, str]]:
    lines = registry_text.splitlines()
    try:
        header_index = lines.index(REGISTRY_HEADER)
    except ValueError as error:
        raise ValueError("Could not find the inheritance registry table header.") from error

    projects: list[dict[str, str]] = []
    for line in lines[header_index + 2 :]:
        stripped = line.strip()
        if not stripped.startswith("|"):
            break
        values = [part.strip() for part in stripped.strip("|").split("|")]
        if len(values) != 5:
            raise ValueError(f"Expected five cells in registry row: {line}")
        project, repository, prompt_status, implementation_status, evidence = values
        if prompt_status == "Prompt delivered" or implementation_status.startswith("Verified"):
            projects.append(
                {
                    "project": project,
                    "repository": repository,
                    "status": f"{prompt_status}; {implementation_status}",
                    "evidence": evidence,
                }
            )
    return projects


def render_section(projects: list[dict[str, str]]) -> str:
    lines = [
        BEGIN_MARKER,
        "> Generated from `os/context/agentos-inheritance-registry.md` by "
        "`scripts/sync-playbook-project-surfaces.py`. Do not edit this table manually.",
        "> Project-local agents, skills, and runbooks remain authoritative in the linked project.",
        "",
        "| Project | Detailed authority | Inheritance state | Evidence / next check |",
        "|---|---|---|---|",
    ]
    if projects:
        for project in projects:
            lines.append(
                "| {project} | Project-local agents and skills; {repository} | {status} | {evidence} |".format(
                    project=cell(project["project"]),
                    repository=cell(render_source(project["repository"])),
                    status=cell(project["status"]),
                    evidence=cell(project["evidence"]),
                )
            )
    else:
        lines.append("| None yet | — | — | — |")
    lines.append(END_MARKER)
    return "\n".join(lines)


def sync(check: bool) -> int:
    registry_text = REGISTRY_PATH.read_text()
    playbook_text = PLAYBOOK_PATH.read_text()
    section = render_section(read_inherited_projects(registry_text))
    pattern = re.compile(
        rf"{re.escape(BEGIN_MARKER)}.*?{re.escape(END_MARKER)}", re.DOTALL
    )
    updated_playbook, replacements = pattern.subn(section, playbook_text)
    if replacements != 1:
        raise ValueError(
            "Expected exactly one generated inherited-project-surfaces section in PLAYBOOK.md."
        )

    if updated_playbook == playbook_text:
        print("Playbook project surfaces are current.")
        return 0
    if check:
        print("PLAYBOOK.md project surfaces are stale. Run the sync script.")
        return 1

    PLAYBOOK_PATH.write_text(updated_playbook)
    print("Updated PLAYBOOK.md project surfaces.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit nonzero when PLAYBOOK.md is not synchronized with the registry.",
    )
    args = parser.parse_args()
    try:
        return sync(args.check)
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
