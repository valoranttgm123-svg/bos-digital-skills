#!/usr/bin/env python3
"""Validate Agent Skills folder layout and required SKILL.md frontmatter.

Uses only the Python standard library so contributors do not need extra packages.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.DOTALL)


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md")) if SKILLS_DIR.exists() else []

    if not SKILLS_DIR.is_dir():
        fail("Missing skills/ directory", errors)
    if not skill_files:
        fail("No skills/*/SKILL.md files were found", errors)

    names: set[str] = set()
    for skill_file in skill_files:
        folder_name = skill_file.parent.name
        content = skill_file.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(content)
        if not match:
            fail(f"{skill_file.relative_to(ROOT)}: missing valid --- frontmatter delimiters", errors)
            continue

        frontmatter = match.group(1)
        name_match = re.search(r"(?m)^name:\s*([^\s#]+)\s*$", frontmatter)
        desc_match = re.search(r"(?m)^description:\s*(.*?)\s*$", frontmatter)

        if not name_match:
            fail(f"{skill_file.relative_to(ROOT)}: missing name", errors)
            continue
        if not desc_match or not desc_match.group(1).strip().strip('"').strip("'"):
            fail(f"{skill_file.relative_to(ROOT)}: missing non-empty description", errors)
            continue

        name = name_match.group(1).strip().strip('"').strip("'")
        description = desc_match.group(1).strip().strip('"').strip("'")

        if not NAME_RE.fullmatch(name):
            fail(f"{skill_file.relative_to(ROOT)}: name must be lowercase kebab-case; got {name!r}", errors)
        if len(name) > 64:
            fail(f"{skill_file.relative_to(ROOT)}: name exceeds 64 characters", errors)
        if folder_name != name:
            fail(f"{skill_file.relative_to(ROOT)}: folder {folder_name!r} does not match name {name!r}", errors)
        if len(description) > 1024:
            fail(f"{skill_file.relative_to(ROOT)}: description exceeds 1024 characters", errors)
        if name in names:
            fail(f"Duplicate skill name: {name}", errors)
        names.add(name)

    if errors:
        print("Agent Skills validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"Agent Skills validation passed: {len(skill_files)} skill(s).")
    for skill_file in skill_files:
        print(f" - {skill_file.parent.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
