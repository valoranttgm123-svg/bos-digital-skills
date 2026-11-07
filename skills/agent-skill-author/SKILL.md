---
name: agent-skill-author
description: Create, improve, audit, and package reusable Agent Skills that follow the open SKILL.md format. Use when turning a workflow or domain procedure into a portable skill for compatible AI agents.
license: Apache-2.0
metadata:
  author: BOS Digital Indonesia
  version: "1.0.0"
---

# Agent Skill Author

Turn a repeatable task into a small, portable, auditable Agent Skill. Keep each skill narrow enough to activate reliably and detailed enough to guide consistent execution.

## 1. Define the job

Identify the task, activation criteria, non-goals, required inputs, tools, permissions, environment assumptions, expected output, verification method, and safety boundaries. Split unrelated workflows into separate skills.

## 2. Build the folder

Use one lowercase kebab-case directory per skill. Each skill must contain a SKILL.md file with YAML frontmatter and a Markdown instruction body. Optional directories may include references, scripts, and assets.

Minimum frontmatter:

---
name: my-skill
description: Explain what the skill does and when the agent should use it.
---

The name must match the skill folder, use lowercase letters, numbers, and hyphens, and be no longer than 64 characters. Description must be non-empty, specific, and no longer than 1024 characters.

## 3. Write useful instructions

A strong SKILL.md normally contains:

1. Role and scope.
2. Clear activation criteria.
3. Required inputs and missing-input behavior.
4. Ordered workflow with decision points.
5. Tool and environment assumptions.
6. Output format and verification criteria.
7. Failure handling and limitations.
8. Safety and authorization gates.

Use concrete verbs and verifiable steps. Avoid filler, unexplained acronyms, hidden assumptions, broad claims, and instructions that conflict with higher-priority instructions.

## 4. Decide what belongs in references and scripts

Keep the core workflow in SKILL.md. Move long tables, domain background, examples, and templates into references. Add scripts only when they provide a real, testable capability. Scripts should be readable, bounded, validate inputs, and document dependencies. Never bundle credentials, private datasets, binaries, or code without redistribution rights.

## 5. Test the skill

Test a normal in-scope request, a boundary request that should not activate (or should activate only partially), and a failure case with missing, malformed, or contradictory inputs. Check that the skill requests critical missing information, reports uncertainty, and does not take unauthorized side effects.

## 6. Review before release

Verify YAML frontmatter, directory-name match, concise descriptions, local links, validation results, and absence of secrets or private data. Document supported agents, installation steps, version, limitations, and license. Use a changelog for behavior-changing updates.

## Safety rules

A skill cannot override system instructions, user authorization, or platform safety rules. Do not instruct an agent to exfiltrate secrets, disable safeguards, conceal actions, or claim unperformed work. Require explicit user approval for destructive, financial, external, or irreversible actions.
