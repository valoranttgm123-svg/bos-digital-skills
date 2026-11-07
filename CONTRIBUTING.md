# Contributing

Thank you for improving BOS Digital Skills.

## Propose a change

1. Open an issue describing the use case, intended users, and why an existing skill does not already cover it.
2. Keep each skill focused on one repeatable job.
3. Use lowercase kebab-case for the directory and the matching frontmatter `name`.
4. Include a specific, non-empty frontmatter `description` that says what the skill does and when to use it.
5. Add workflow steps, required inputs, output expectations, verification, limitations, and safety boundaries.
6. Add or update examples when behavior changes.
7. Run `python tests/validate_skills.py` before opening a pull request.

## Content requirements

- Do not include secrets, private user data, proprietary files, or content without redistribution rights.
- Do not claim a tool was executed or an outcome verified unless it happened.
- Do not add instructions that bypass security, access controls, platform rules, or user approval.
- For time-sensitive domains, tell the agent to verify current primary sources.
- Keep documentation direct and useful. Avoid keyword stuffing and unsupported claims about popularity or virality.

## Pull request checklist

- [ ] Skill folder name matches frontmatter name.
- [ ] `SKILL.md` has YAML frontmatter with `name` and `description`.
- [ ] New or changed workflows have examples.
- [ ] Safety and permission boundaries are clear.
- [ ] Validator passes.
- [ ] README/catalog and installation docs are updated when needed.
