#!/usr/bin/env python3
"""Print benchmark prompts for manual execution in an AI agent host."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "evals" / "cases.json"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="list available skills and scenario types")
    parser.add_argument("--skill", help="exact skill folder/name")
    parser.add_argument("--scenario", choices=("happy-path", "missing-input", "safety-boundary"))
    parser.add_argument("--include-criteria", action="store_true", help="also print evaluator-only criteria")
    args = parser.parse_args()

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    cases = data["cases"]

    if args.list:
        for skill in sorted({case["skill"] for case in cases}):
            scenarios = sorted(case["scenario_type"] for case in cases if case["skill"] == skill)
            print(f"{skill}: " + ", ".join(scenarios))
        return 0

    if not args.skill or not args.scenario:
        parser.error("provide --skill and --scenario, or use --list")

    selected = [case for case in cases if case["skill"] == args.skill and case["scenario_type"] == args.scenario]
    if not selected:
        print(f"No scenario found for skill={args.skill!r}, scenario={args.scenario!r}")
        return 1

    case = selected[0]
    print(f"TEST ID: {case['test_id']}")
    print(f"SKILL: {case['skill']}")
    print(f"SCENARIO: {case['scenario_type']}")
    print("\nPROMPT TO SEND (copy only the prompt below):\n")
    print(case["prompt"])

    if args.include_criteria:
        print("\nEVALUATOR-ONLY ACCEPTANCE CRITERIA:")
        for item in case["acceptance_criteria"]:
            print(f"- {item}")
        print("\nCRITICAL FAILURE CONDITIONS:")
        for item in case["critical_failures"]:
            print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
