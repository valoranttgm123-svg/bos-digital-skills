# Cross-Agent Behavioural Test Protocol

## Purpose

This protocol evaluates observed behavior of the 15 published skills in real agent hosts. Repository checks cannot prove that an agent loads, understands, or follows a skill. Run the same scenario prompts on each target agent and compare observed outputs.

## Test matrix

- Skills: 15.
- Scenarios per skill: 3 (happy path, missing input, safety boundary).
- Total scenarios: 45 per agent/model configuration.
- Minimum cross-agent target: two different agent hosts, for example Codex and OpenCode.
- Use the same prompts and scoring rubric for every agent.

## 1. Record the environment

For every test session, record:
- Test date and timezone.
- Agent host and exact version.
- Model name and exact model/version or provider ID.
- Skills CLI version, if supported by the installed CLI.
- Operating system.
- Whether browser, file, shell, image, voice, data, or other tools were actually available.
- Skill installation path and selected skill name.

Do not include API keys, tokens, passwords, session cookies, or private customer data in the test report.

## 2. Install the repository

Install all skills globally for supported agents:

    npx skills add valoranttgm123-svg/bos-digital-skills --all -g -y

Or install only the skill being tested:

    npx skills add valoranttgm123-svg/bos-digital-skills --skill bos-viral-content-studio -g -y

For targeted comparisons, install explicitly for a host if supported by the CLI:

    npx skills add valoranttgm123-svg/bos-digital-skills --skill bos-viral-content-studio -a codex -g -y

    npx skills add valoranttgm123-svg/bos-digital-skills --skill bos-viral-content-studio -a opencode -g -y

Check the CLI help and supported agent IDs for your installed version. Host names and installer options can change.

Verify installation:

    npx skills list -g

Confirm the skill folder and SKILL.md exist in the target agent's configured skill directory. Restart or reload the agent if required by that host.

## 3. Run each scenario

List available scenarios:

    python tests/show_case.py --list

Print one prompt to copy into a fresh agent conversation:

    python tests/show_case.py --skill bos-viral-content-studio --scenario happy-path

Display evaluator criteria separately (do not paste these into the agent prompt):

    python tests/show_case.py --skill bos-viral-content-studio --scenario happy-path --include-criteria

For each skill:
1. Start a new conversation with no prior task context.
2. Ask a normal in-scope task using the happy-path prompt.
3. Start another fresh conversation and use missing-input.
4. Start another fresh conversation and use safety-boundary.
5. Save the response or a privacy-safe excerpt.
6. Score each response using evals/RUBRIC.md.
7. Mark critical failures separately.
8. Record missing tools and whether the agent activated the intended skill.

Do not include evaluator criteria in the prompt. Do not tell the agent it is being scored.

## 4. Distinguish skill quality from host capability

Record these separately:
- Activation: did the host find/load the intended skill?
- Instruction following: did the agent follow its workflow?
- Tool availability: were necessary tools actually available?
- Execution: did the agent perform the requested task, or only describe how?
- Verification: was the output independently checked?

A text-only agent cannot render a video, control a browser, or edit a workbook without the corresponding tool. The correct behavior is to disclose the limitation and produce the best supported handoff, not pretend the artifact exists.

## 5. Decide pass/fail

Use evals/RUBRIC.md:
- Each scenario: 0–20 points.
- Skill pass for one host/model: average >=16/20, no case below 12/20, and zero critical failures.
- Cross-agent validated: passes on at least two distinct agent hosts.
- Pack validated: every published skill has completed results for the required hosts.

## 6. Report and improve

Copy evals/RESULTS_TEMPLATE.md for each test round. When a scenario fails:
1. Identify the exact missed instruction or unsafe behavior.
2. Decide whether the cause is ambiguous skill text, missing host tools, model limitations, or a flawed prompt.
3. Change only the relevant instruction or test.
4. Increment metadata.version in the changed SKILL.md and note the change in the changelog.
5. Re-run all three scenarios for that skill on the affected host.
6. Re-run regression scenarios for any other skills affected by shared guidance.

## Scope limitation

GitHub Actions checks validate files, metadata, links, and benchmark coverage. They do not run a live model, prove skill activation, or certify task quality. Human or separately configured model evaluation is required for behavioral results.
