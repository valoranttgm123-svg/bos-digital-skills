#!/usr/bin/env python3
"""Validate Agent Skill structure, required metadata, and basic Markdown integrity."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.DOTALL)
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s*(\x60{3,}|~{3,})")
ALLOWED_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
PLACEHOLDERS_RE = re.compile(r"\b(TODO|TBD|FIXME)\b", re.IGNORECASE)


def parse_frontmatter(frontmatter: str) -> tuple[dict[str, str], dict[str, str], list[str]]:
    """Parse the constrained scalar/map subset used by this repository."""
    top: dict[str, str] = {}
    metadata: dict[str, str] = {}
    errors: list[str] = []
    active_map = False

    for line_no, line in enumerate(frontmatter.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  "):
            if not active_map:
                errors.append(f"frontmatter line {line_no}: indented value outside metadata map")
                continue
            child = re.match(r"^  ([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
            if not child:
                errors.append(f"frontmatter line {line_no}: invalid metadata entry")
                continue
            key, value = child.groups()
            if key in metadata:
                errors.append(f"frontmatter line {line_no}: duplicate metadata key {key!r}")
            if not value:
                errors.append(f"frontmatter line {line_no}: metadata value for {key!r} is empty")
            metadata[key] = value.strip("\"'")
            continue

        active_map = False
        item = re.match(r"^([a-z][a-z0-9-]*):\s*(.*?)\s*$", line)
        if not item:
            errors.append(f"frontmatter line {line_no}: invalid top-level field")
            continue
        key, value = item.groups()
        if key in top:
            errors.append(f"frontmatter line {line_no}: duplicate field {key!r}")
        top[key] = value.strip("\"'")
        if key == "metadata":
            active_map = True
        elif not value:
            errors.append(f"frontmatter line {line_no}: field {key!r} has an empty value")

    return top, metadata, errors


def check_local_links(markdown_file: Path, content: str, errors: list[str]) -> None:
    for target in LINK_RE.findall(content):
        target = target.strip().split("#", 1)[0].split("?", 1)[0]
        if not target or target.startswith(("https://", "http://", "mailto:", "data:")):
            continue
        resolved = (markdown_file.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{markdown_file.relative_to(ROOT)}: local link escapes repository: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{markdown_file.relative_to(ROOT)}: broken local link: {target}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-count", type=int, default=15)
    args = parser.parse_args()
    errors: list[str] = []
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md")) if SKILLS_DIR.exists() else []

    if not SKILLS_DIR.is_dir():
        errors.append("Missing skills/ directory")
    if not skill_files:
        errors.append("No skills/*/SKILL.md files were found")
    if args.expected_count is not None and len(skill_files) != args.expected_count:
        errors.append(f"Expected {args.expected_count} skills, found {len(skill_files)}")

    names: set[str] = set()
    for skill_file in skill_files:
        rel = skill_file.relative_to(ROOT)
        content = skill_file.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(content)
        if not match:
            errors.append(f"{rel}: missing valid YAML frontmatter delimiters")
            continue

        top, metadata, parse_errors = parse_frontmatter(match.group(1))
        errors.extend(f"{rel}: {message}" for message in parse_errors)

        unknown = sorted(set(top) - ALLOWED_FIELDS)
        if unknown:
            errors.append(f"{rel}: unsupported frontmatter field(s): {', '.join(unknown)}")

        name = top.get("name", "")
        description = top.get("description", "")
        if not name:
            errors.append(f"{rel}: missing required name")
        if not description:
            errors.append(f"{rel}: missing required non-empty description")
        if name and not NAME_RE.fullmatch(name):
            errors.append(f"{rel}: name must use lowercase letters, numbers, and single hyphens")
        if len(name) > 64:
            errors.append(f"{rel}: name exceeds 64 characters")
        if name and skill_file.parent.name != name:
            errors.append(f"{rel}: folder name {skill_file.parent.name!r} does not match name {name!r}")
        if name in names:
            errors.append(f"{rel}: duplicate skill name {name!r}")
        names.add(name)
        if len(description) > 1024:
            errors.append(f"{rel}: description exceeds 1024 characters")
        if description and len(description) < 30:
            errors.append(f"{rel}: description is too short to identify purpose and activation context")
        if "compatibility" in top and not 1 <= len(top["compatibility"]) <= 500:
            errors.append(f"{rel}: compatibility must be 1–500 characters when present")
        if "license" in top and not top["license"]:
            errors.append(f"{rel}: license cannot be empty")
        if "metadata" in top and not metadata:
            errors.append(f"{rel}: metadata must be a non-empty key/value map")

        body = content[match.end():]
        words = re.findall(r"\b[\w'-]+\b", body)
        if len(words) < 100:
            errors.append(f"{rel}: instruction body is too short ({len(words)} words; minimum 100)")
        if len(content.splitlines()) > 500:
            errors.append(f"{rel}: SKILL.md exceeds the recommended 500-line limit")
        if len(re.findall(r"(?m)^#{1,6}\s+\S", body)) < 3:
            errors.append(f"{rel}: add at least three descriptive section headings")
        if PLACEHOLDERS_RE.search(body):
            errors.append(f"{rel}: unresolved TODO/TBD/FIXME placeholder found")

        fence_stack: list[str] = []
        for line in body.splitlines():
            fence = FENCE_RE.match(line)
            if fence:
                marker = fence.group(1)[0]
                if fence_stack and fence_stack[-1] == marker:
                    fence_stack.pop()
                else:
                    fence_stack.append(marker)
        if fence_stack:
            errors.append(f"{rel}: unclosed Markdown code fence(s)")
        check_local_links(skill_file, body, errors)

    for markdown_file in sorted(ROOT.rglob("*.md")):
        if ".git" in markdown_file.parts or "node_modules" in markdown_file.parts:
            continue
        check_local_links(markdown_file, markdown_file.read_text(encoding="utf-8"), errors)

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"Skill validation passed: {len(skill_files)} skill(s), metadata, basic Markdown, and local links.")
    for skill_file in skill_files:
        print(f" - {skill_file.parent.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
