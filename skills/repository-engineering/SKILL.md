---
name: repository-engineering
description: Audit, understand, modify, test, and document an existing software repository. Use for bug fixes, refactoring, feature implementation, build failures, CI issues, dependency changes, and engineering handoffs. Preserve project conventions and avoid unsupported claims.
license: Apache-2.0
metadata:
  author: BOS Digital Indonesia
  version: "1.0.0"
---

# Repository Engineering

Work as a careful engineer inside an existing codebase. Treat the repository's current source, tests, documentation, and user instructions as the source of truth.

## Phase 1 — Establish context

1. Confirm repository root and current branch. Do not assume the shell started in the project directory.
2. Inspect README, AGENTS.md, CONTRIBUTING, architecture docs, package manifests, lockfiles, CI workflows, and relevant code before editing.
3. Check git status, recent commits, and uncommitted user changes. Never overwrite or discard user work.
4. Identify runtime, framework, versions, test runner, build command, and supported platforms.
5. Search for existing implementations and patterns before adding abstractions or dependencies.

## Phase 2 — Plan a bounded change

1. Translate the request into observable acceptance criteria.
2. Identify the smallest files and components that need changing.
3. Identify dependencies, migrations, compatibility impacts, security boundaries, and unknowns.
4. For multi-step or risky work, write a short plan and checkpoints.
5. Do not expand scope to unrelated refactors.

## Phase 3 — Implement

- Follow local naming, formatting, error-handling, and architectural conventions.
- Preserve public APIs and data formats unless the user explicitly requests a change.
- Add or update focused tests for behavior changes and regressions.
- Validate inputs at trust boundaries. Avoid logging secrets or private data.
- Keep secrets out of source code, tests, fixtures, and commit messages.
- Avoid dependencies unless they materially improve the solution; explain additions.
- Make compatibility and migration behavior explicit.

## Phase 4 — Verify

1. Run targeted tests first, then broader tests, build, lint, and type checks as appropriate.
2. If a test cannot run, state why; never imply it passed.
3. Inspect the final diff for unrelated edits, secrets, generated files, and formatting noise.
4. Check final status and confirm no user changes were lost.
5. Report exact commands and pass/fail outcomes.

## Git and release authorization

Do not commit, push, publish a release, deploy, merge a pull request, modify repository visibility, or rewrite history unless the user explicitly authorizes that specific action. Creating a local patch is not authorization to publish it. Never force-push or reset away user changes.

## Output format

- Repository state: root, branch, working tree, relevant conventions.
- Findings: root cause or implementation context with file paths.
- Plan and changes: concise summary.
- Verification: commands actually run and results.
- Remaining risks: untested paths, environment gaps, migration concerns.
- Handoff: exact next steps, with no claims beyond verified evidence.
