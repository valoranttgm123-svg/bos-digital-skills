# Benchmark and Testing Suite

BOS Digital Skills separates deterministic repository checks from live AI behavior evaluation.

## Automated repository checks

Run from the repository root:

    python tests/validate_skills.py
    python tests/validate_benchmark.py
    python tests/validate_srt.py examples/creator/verified-sample-45s.srt --expected-duration 45 --transcript examples/creator/verified-sample-45s-vo.txt --strict-cps --require-contiguous

On Windows PowerShell, run the complete local static check and prompt-runner smoke test:

    .\tests\Run-LocalChecks.ps1

To also install and run the additional Go-based community quality validator (requires Go and network access):

    .\tests\Run-LocalChecks.ps1 -InstallQualityValidator

These checks verify the catalog's skill metadata, naming/layout, Markdown basics, internal links, and completeness/shape of the behavioral test manifest.

For deeper specification and quality diagnostics, GitHub Actions installs the community-maintained `skill-validator` v1.6.2 CLI from `github.com/agent-ecosystem/skill-validator/cmd/skill-validator` and runs it on `skills/`. Its Go module requires Go 1.25.5 or newer. The Windows optional runner uses the same pinned version. It is an additional quality tool, not the Agent Skills specification itself.

## Behavioral benchmark

- evals/cases.json contains 45 prompts: three scenarios for each of the 15 skills.
- evals/RUBRIC.md defines a consistent 0–20 score and critical-failure gates.
- evals/TEST_PROTOCOL.md explains fresh-session, two-host testing.
- evals/RESULTS_TEMPLATE.md records model, host, tool availability, scores, and failures.
- tests/show_case.py prints prompts for manual execution in Codex, OpenCode, or another compatible agent.

On Windows, `tests/Run-LocalChecks.ps1` runs the local checks and prompt-runner smoke test. The example SRT and transcript under `examples/creator/` provide a known-good fixture for the timing and text-parity validator.

## Important distinction

CI can prove that files are structurally valid and evaluation cases are present. It cannot prove that Codex, OpenCode, or another model activated a skill or performed a task correctly. That requires running the prompts in the actual host/model and recording observed results.

See the Agent Skills specification at https://agentskills.io/specification, Skills CLI documentation at https://www.skills.sh/docs/cli, and skill-validator at https://github.com/agent-ecosystem/skill-validator.
