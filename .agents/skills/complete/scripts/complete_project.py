#!/usr/bin/env python3
"""Mark an AgentOS project complete and mirror status into docs."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path


PROJECTS = {
    "00": "Your OS Thought Partner",
    "01": "Your Identity",
    "02": "Your Context",
    "03": "Your First Skills",
    "04": "Your Memory",
    "05": "Your Connections",
    "06": "The Job",
    "07": "The Build",
    "08": "Test & Verify",
    "09": "The Second Agent",
    "10": "Your Playbook",
    "11": "Automations",
}

ROOT = Path.cwd()
TRACKER = ROOT / "PROJECT_TRACKER.md"
README = ROOT / "README.md"
PLAYBOOK = ROOT / "PLAYBOOK.md"
SKILLS_README = ROOT / "os" / "skills" / "README.md"
MEMORY_DIR = ROOT / "os" / "memory"
WORKING_MEMORY = MEMORY_DIR / "working-memory.md"
PROJECT_HISTORY = MEMORY_DIR / "project-history.md"
SOURCE_URL = "https://aidbagentos.ai/projects"


@dataclass
class TrackerRow:
    number: str
    title: str
    folder: str
    status: str
    completed_date: str
    source: str
    current_evidence: str = ""


def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def project_folder(number: str, title: str) -> Path:
    matches = sorted((ROOT / "projects").glob(f"{number}-*"))
    if matches:
        return matches[0]
    return ROOT / "projects" / f"{number}-{slugify(title)}"


def tracker_seed() -> list[TrackerRow]:
    rows: list[TrackerRow] = []
    for number, title in PROJECTS.items():
        folder = project_folder(number, title)
        notes = folder / "notes.md"
        status = "Not started"
        completed_date = ""
        if notes.exists():
            text = notes.read_text()
            match = re.search(r"^Status:\s*(.+)$", text, re.MULTILINE)
            if match:
                status = match.group(1).strip()
            date_match = re.search(r"Completed:\s*(\d{4}-\d{2}-\d{2})", text)
            if date_match:
                completed_date = date_match.group(1)
        rows.append(
            TrackerRow(
                number=number,
                title=title,
                folder=f"`{folder.as_posix().replace(str(ROOT) + '/', '')}/`",
                status=status,
                completed_date=completed_date,
                source=f"<{SOURCE_URL}>",
            )
        )
    return rows


def parse_tracker(text: str) -> list[TrackerRow]:
    rows: list[TrackerRow] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) not in {6, 7} or cells[0] in {"Project", "---"} or set(cells[0]) == {"-"}:
            continue
        project_match = re.match(r"(\d{2})", cells[0])
        if not project_match:
            continue
        current_evidence = cells[5] if len(cells) == 7 else ""
        source = cells[6] if len(cells) == 7 else cells[5]
        rows.append(
            TrackerRow(
                number=project_match.group(1),
                title=re.sub(r"^\d{2}\s*-\s*", "", cells[0]).strip(),
                folder=cells[2],
                status=cells[3],
                completed_date="" if cells[4] == "-" else cells[4],
                source=source,
                current_evidence=current_evidence,
            )
        )
    return rows


def render_tracker_row(row: TrackerRow, include_current_evidence: bool) -> str:
    completed = row.completed_date or "-"
    if include_current_evidence:
        return (
            f"| {row.number} - {row.title} | {row.title} | {row.folder} | "
            f"{row.status} | {completed} | {row.current_evidence} | {row.source} |"
        )
    return (
        f"| {row.number} - {row.title} | {row.title} | {row.folder} | "
        f"{row.status} | {completed} | {row.source} |"
    )


def render_tracker(rows: list[TrackerRow], original_text: str | None = None) -> str:
    if original_text is not None:
        row_by_number = {row.number: row for row in rows}
        include_current_evidence = "Current Evidence / Next Gate" in original_text
        rendered: list[str] = []
        for line in original_text.splitlines():
            if line.startswith("|"):
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                project_match = re.match(r"(\d{2})", cells[0]) if cells else None
                if project_match and project_match.group(1) in row_by_number:
                    rendered.append(
                        render_tracker_row(row_by_number[project_match.group(1)], include_current_evidence)
                    )
                    continue
            rendered.append(line)
        return "\n".join(rendered).rstrip() + "\n"

    lines = [
        "# AgentOS Project Tracker",
        "",
        f"Source: <{SOURCE_URL}>",
        "",
        "| Project | Title | Local Evidence / Notes | Status | Completed Date | Current Evidence / Next Gate | Source |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(render_tracker_row(row, include_current_evidence=True))
    return "\n".join(lines) + "\n"


def load_or_create_tracker() -> tuple[list[TrackerRow], bool]:
    if TRACKER.exists():
        return parse_tracker(TRACKER.read_text()), False
    return tracker_seed(), True


def folder_from_cell(cell: str) -> Path:
    value = cell.strip().strip("`").rstrip("/")
    return ROOT / value


def update_notes(row: TrackerRow, today: str) -> str:
    folder = folder_from_cell(row.folder)
    notes = folder / "notes.md"
    if not notes.exists():
        raise SystemExit(f"Project {row.number} is tracked, but {notes} does not exist.")
    text = notes.read_text()
    text = re.sub(r"^Status:\s*.*$", "Status: Complete", text, count=1, flags=re.MULTILINE)
    if f"Completed: {today}" not in text and "Completed:" not in text:
        marker = "Status: Complete\n"
        text = text.replace(marker, f"{marker}\nCompleted: {today}\n", 1)
    return text


def render_readme_index(rows: list[TrackerRow]) -> str:
    lines = [
        "## Project Index",
        "",
        "Canonical tracker: `PROJECT_TRACKER.md`",
        "",
        "| Project | Local Folder | Status |",
        "|---|---|---|",
    ]
    for row in rows:
        lines.append(f"| {row.number} - {row.title} | {row.folder} | {row.status} |")
    return "\n".join(lines)


def update_readme(rows: list[TrackerRow]) -> str:
    text = README.read_text()
    index = render_readme_index(rows)
    pattern = r"## Project Index\n\n(?:Canonical tracker: `PROJECT_TRACKER\.md`\n\n)?\| Project \| Local Folder \| Status \|\n\|---\|---\|---\|\n(?:\|.*\|\n?)+"
    if not re.search(pattern, text):
        raise SystemExit("Could not find README Project Index table.")
    return re.sub(pattern, index + "\n", text, count=1)


def update_playbook(row: TrackerRow, today: str) -> str:
    text = PLAYBOOK.read_text()
    text = re.sub(r"^Last updated: .*$", f"Last updated: {today}", text, count=1, flags=re.MULTILINE)

    if row.number == "02" and "| Me | `/complete` |" not in text:
        old = "| Me | TBD | TBD | TBD |"
        new = "| Me | `/complete` | Mark AgentOS course projects complete. | Updated tracker, project notes, README, and related docs. |"
        text = text.replace(old, new, 1)
    if row.title == "Your First Skills":
        text = text.replace("| Agent-specific | TBD | TBD | TBD |", "| Agent-specific | Measurabl and Excelsior skill translations | Repeated work workflows imported from Claude Code and Cursor. | Codex repo skills and native archives. |")
    if row.title == "Your Memory":
        text = text.replace("| Persistent memory | `os/memory/` files with periodic consolidation. | Weekly | Planned |", "| Persistent memory | `os/memory/` files with periodic consolidation. | Weekly | Draft |")
    if row.title == "The Second Agent":
        text = text.replace("| Agent-specific skills | TBD |", "| Agent-specific skills | `/complete` plus future agent-specific workflows. |")
    if row.title == "The Build":
        text = text.replace("| GitHub | Version control and evidence links. | Git / GitHub | Active |", "| GitHub | Version control, evidence links, commits, and pushes. | Git / GitHub | Active |")
        text = text.replace(
            "Projects 00–06\nare complete; Project 07 is in progress; Project 08 is not started;",
            "Projects 00–07\nare complete; Project 08 is not started;",
        )
        text = text.replace(
            "| What needs improvement | Add the compact Project 07 representative-run evidence and reflection to AgentOS. |",
            "| What needs improvement | Capture a compact representative ThraxOS run and reflection as the first Project 08 verification record. |",
        )
    if row.title == "Test & Verify":
        text = text.replace("| TBD | TBD | TBD | Planned |", "| Completion workflow | Manual `/complete NN` trigger | Updates completion docs and pushes changes. | Active |", 1)
    if row.title == "Your Playbook":
        text = text.replace("### This Month\n\n- Complete Project 00 and establish the first reusable OS context files.", "### This Month\n\n- Keep project tracker and completion workflow current.")
    return text


def update_skills_readme() -> str:
    text = SKILLS_README.read_text()
    if "`/complete NN`" in text:
        return text
    addition = """\n## `/complete NN`\n\n- Trigger: `/complete NN`, where `NN` is a two-digit AgentOS project number.\n- Inputs: Existing `PROJECT_TRACKER.md` entry and matching project notes folder.\n- Process: Mark the project complete, mirror status into docs, validate the skill, then commit and push.\n- Output: Updated tracker, README Project Index, project notes, and any related playbook sections.\n- Verification: Run the skill validator and dry-run invalid or unknown inputs before committing.\n"""
    return text.rstrip() + "\n" + addition


def completed_project_heading(row: TrackerRow) -> str:
    return f"{row.number} - {row.title}"


def update_project_history(row: TrackerRow) -> str:
    if not PROJECT_HISTORY.exists():
        return ""
    text = PROJECT_HISTORY.read_text()
    heading = f"### {row.completed_date} - Project {completed_project_heading(row)} Completed"
    if heading in text:
        return text

    entry = "\n".join(
        [
            heading,
            "",
            f"- Marked AgentOS Project {completed_project_heading(row)} complete.",
            f"- Evidence: `{folder_from_cell(row.folder).relative_to(ROOT).as_posix()}/notes.md`.",
            "",
            "",
        ]
    )
    marker = "## Work\n"
    if marker in text:
        return text.replace(marker, entry + marker, 1)
    return text.rstrip() + "\n\n" + entry


def remove_active_project_section(text: str, title: str) -> tuple[str, bool]:
    pattern = re.compile(
        rf"^### {re.escape(title)}\n(?:^- .*\n?|\n)*",
        flags=re.MULTILINE,
    )
    return pattern.subn("", text, count=1)


def update_working_memory(row: TrackerRow) -> str:
    if not WORKING_MEMORY.exists():
        return ""
    text = WORKING_MEMORY.read_text()
    if row.number == "07":
        text = text.replace(
            "- Project 07 is in progress using ThraxOS, not the AI Office Hours Prep Agent.",
            "- Project 07 is complete using ThraxOS, not the AI Office Hours Prep Agent.",
        )
        text = text.replace(
            "- Next handoff: capture one compact, sanitized representative ThraxOS invocation and verified result plus Kyle's reflection, then use it as the Project 07 completion packet and first Project 08 verification artifact.",
            "- Next handoff: capture one compact, sanitized representative ThraxOS invocation and verified result plus Kyle's reflection as the first Project 08 verification artifact.",
        )
    text, removed = remove_active_project_section(text, row.title)
    heading = f"- {row.completed_date}: Completed Project {completed_project_heading(row)}."
    if "## Recently Completed" not in text:
        insert = f"\n## Recently Completed\n\n{heading}\n"
        marker = "\n## Clear Soon\n"
        if marker in text:
            text = text.replace(marker, insert + marker, 1)
        else:
            text = text.rstrip() + insert + "\n"
    elif heading not in text:
        text = text.replace("## Recently Completed\n\n", f"## Recently Completed\n\n{heading}\n", 1)

    if not removed and heading in text:
        return text
    return text


def write_if_changed(path: Path, new_text: str, dry_run: bool, changed: list[str]) -> None:
    if new_text == "":
        return
    old_text = path.read_text() if path.exists() else None
    if old_text == new_text:
        return
    changed.append(str(path.relative_to(ROOT)))
    if not dry_run:
        path.write_text(new_text)


def complete_project(number: str, dry_run: bool = False) -> int:
    if not re.fullmatch(r"\d{2}", number):
        print("Expected exactly one two-digit project number, such as 02.", file=sys.stderr)
        return 2

    rows, created = load_or_create_tracker()
    row_by_number = {row.number: row for row in rows}
    if number not in row_by_number:
        print(
            f"Project {number} is not in PROJECT_TRACKER.md. Add a tracker entry from {SOURCE_URL} before completing it.",
            file=sys.stderr,
        )
        return 3

    today = dt.date.today().isoformat()
    row = row_by_number[number]
    row.status = "Complete"
    row.completed_date = row.completed_date or today

    changed: list[str] = []
    original_tracker = TRACKER.read_text() if TRACKER.exists() else None
    write_if_changed(TRACKER, render_tracker(rows, original_tracker), dry_run, changed)
    write_if_changed(folder_from_cell(row.folder) / "notes.md", update_notes(row, row.completed_date), dry_run, changed)
    write_if_changed(README, update_readme(rows), dry_run, changed)
    write_if_changed(PLAYBOOK, update_playbook(row, today), dry_run, changed)
    write_if_changed(SKILLS_README, update_skills_readme(), dry_run, changed)
    write_if_changed(PROJECT_HISTORY, update_project_history(row), dry_run, changed)
    write_if_changed(WORKING_MEMORY, update_working_memory(row), dry_run, changed)

    prefix = "Would update" if dry_run else "Updated"
    if changed:
        print(f"{prefix}:")
        for path in changed:
            print(f"- {path}")
    else:
        print(f"Project {number} is already complete; no file changes needed.")
    if created and dry_run:
        print("PROJECT_TRACKER.md does not exist yet and would be created.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Mark an AgentOS project complete.")
    parser.add_argument("project_number", help="Two-digit project number, such as 02")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing files")
    args = parser.parse_args()
    return complete_project(args.project_number, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
