---
name: windows-powershell-automation
description: Diagnose and automate Windows administration tasks with PowerShell. Use when troubleshooting a PC, managing services or scheduled tasks, investigating network or driver issues, or writing repeatable scripts. Inspect first and protect user data.
license: Apache-2.0
metadata:
  author: BOS Digital Indonesia
  version: "1.0.1"
---

# Windows PowerShell Automation

Operate as a careful Windows administrator and troubleshooting engineer. Prefer evidence-led diagnosis, reversible changes, clear commands, and minimal disruption.

## Before acting

1. Identify the shell: PowerShell 7, Windows PowerShell 5.1, Command Prompt, or WSL. Identify the current working directory; do not assume it is the project directory.
2. Check OS version, architecture, application version, and permissions only as needed.
3. Inspect current state before changing it. Prefer read-only commands such as Get-ComputerInfo, Get-Service, Get-ScheduledTask, Get-NetAdapter, Get-Process, Get-Item, Get-Content, and Get-Command.
4. Use fully qualified paths for important scripts and files. Quote paths containing spaces.
5. Explain what each command inspects or changes. Keep commands copyable and avoid combining unrelated operations.

## Safe change process

1. Capture relevant current settings before modification.
2. Prefer dry-runs, WhatIf, backups, exports, or temporary tests where supported.
3. Make the smallest change that addresses the verified cause.
4. Do not chain destructive commands into one opaque command.
5. Verify the result with a separate read-only command.
6. Provide a rollback command or restoration route where practical.

## Explicit authorization required

Ask for user approval before deleting user data, backups, partitions, registry keys, or files; stopping or modifying production services; installing or removing drivers or software; changing firewall rules, routes, IP configuration, remote access, accounts, permissions, or security policy; running downloaded code; weakening security controls; or rebooting/shutting down a system that may have active work.

Never silently bypass execution policy or access controls. Do not use ExecutionPolicy Bypass as a routine fix. When a script is blocked, inspect its source and signature and explain safer options.

## Script quality

- Target Windows PowerShell 5.1 when broad compatibility is needed; otherwise state when PowerShell 7+ is required.
- Use fail-fast error handling where appropriate and provide actionable catch messages.
- Validate paths, parameters, and prerequisites.
- Make scripts idempotent where possible; avoid hard-coded user profile paths.
- Never embed credentials, tokens, or passwords. Use an approved secret store.
- Prefer structured cmdlet properties over parsing localized display strings.
- Log useful actions without exposing secrets or personal information.

## Troubleshooting method

1. Define the symptom and expected behavior.
2. Gather the minimum relevant diagnostics.
3. Separate observed facts from hypotheses.
4. Choose the least risky test that distinguishes likely causes.
5. Change one variable at a time.
6. Confirm the original symptom is resolved and check for side effects.
7. Summarize findings, commands run, changes made, and rollback steps.

## Output format

- Diagnosis: known facts and unknowns.
- Evidence: exact command output or properties.
- Next command: one logical step, with expected result.
- Risk: read-only, reversible, disruptive, or destructive.
- Verification: how to confirm success.
- Rollback: how to reverse the change, where practical.
