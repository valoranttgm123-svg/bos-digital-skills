#!/usr/bin/env python3
"""Validate behavioural benchmark case coverage and schema."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MANIFEST = ROOT / "evals" / "cases.json"
EXPECTED_SCENARIOS = {"happy-path", "missing-input", "safety-boundary"}


def main() -> int:
    errors: list[str] = []
    if not MANIFEST.is_file():
        print(f"Missing benchmark manifest: {MANIFEST.relative_to(ROOT)}")
        return 1

    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON in evals/cases.json: {exc}")
        return 1

    skill_dirs = {path.name for path in SKILLS_DIR.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()}
    declared = data.get("skills")
    cases = data.get("cases")
    if not isinstance(cases, list):
        print("Benchmark manifest must include a cases array.")
        return 1
    if declared != len(skill_dirs):
        errors.append(f"Manifest declares {declared!r} skills but repository contains {len(skill_dirs)}")
    if not skill_dirs:
        errors.append("No skill folders were found")

    ids: set[str] = set()
    by_skill: Counter[str] = Counter()
    scenarios_by_skill: dict[str, set[str]] = {}

    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            errors.append(f"Case #{index} must be an object")
            continue
        required = ("test_id", "skill", "scenario_type", "prompt", "acceptance_criteria", "critical_failures")
        for field in required:
            if field not in case:
                errors.append(f"Case #{index}: missing {field}")
        test_id = case.get("test_id", "")
        skill = case.get("skill", "")
        scenario = case.get("scenario_type", "")
        prompt = case.get("prompt", "")
        criteria = case.get("acceptance_criteria")
        failures = case.get("critical_failures")

        if not isinstance(test_id, str) or not test_id:
            errors.append(f"Case #{index}: test_id must be a non-empty string")
        elif test_id in ids:
            errors.append(f"Duplicate test_id: {test_id}")
        else:
            ids.add(test_id)
        if skill not in skill_dirs:
            errors.append(f"Case #{index}: unknown or missing skill {skill!r}")
        else:
            by_skill[skill] += 1
            scenarios_by_skill.setdefault(skill, set()).add(scenario)
        if scenario not in EXPECTED_SCENARIOS:
            errors.append(f"Case #{index}: unsupported scenario_type {scenario!r}")
        if not isinstance(prompt, str) or len(prompt.strip()) < 40:
            errors.append(f"Case #{index}: prompt must contain at least 40 characters")
        if not isinstance(criteria, list) or len(criteria) < 2 or not all(isinstance(x, str) and x.strip() for x in criteria):
            errors.append(f"Case #{index}: acceptance_criteria must contain at least two non-empty strings")
        if not isinstance(failures, list) or len(failures) < 1 or not all(isinstance(x, str) and x.strip() for x in failures):
            errors.append(f"Case #{index}: critical_failures must contain at least one non-empty string")

    for skill in sorted(skill_dirs):
        count = by_skill[skill]
        scenarios = scenarios_by_skill.get(skill, set())
        if count != 3:
            errors.append(f"{skill}: expected exactly 3 scenarios, found {count}")
        if scenarios != EXPECTED_SCENARIOS:
            errors.append(f"{skill}: expected scenarios {sorted(EXPECTED_SCENARIOS)}, found {sorted(scenarios)}")

    if errors:
        print("Benchmark validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"Benchmark validation passed: {len(skill_dirs)} skills, {len(cases)} scenarios, 3 per skill.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
