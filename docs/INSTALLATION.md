# Installation Guide

BOS Digital Skills is organized with one skill per directory under `skills/`. Each skill contains a `SKILL.md` file with the required `name` and `description` frontmatter fields.

## 1. List available skills

Run:

    npx skills add valoranttgm123-svg/bos-digital-skills --list

Review the names before installing.

## 2. Install every skill

To install all skills globally for all compatible agents detected by the Skills CLI:

    npx skills add valoranttgm123-svg/bos-digital-skills --all -g -y

The flags mean:
- `--all`: install every discovered skill to all detected supported agents.
- `-g`: use the user/global installation scope rather than the current project.
- `-y`: skip interactive confirmation prompts.

## 3. Install selected skills

Creator Studio only:

    npx skills add valoranttgm123-svg/bos-digital-skills --skill bos-viral-content-studio -g -y

Instagram and YouTube:

    npx skills add valoranttgm123-svg/bos-digital-skills --skill instagram-growth-agent --skill youtube-creator-agent -g -y

Install into the current project instead of global scope by omitting `-g`.

## 4. Verify installation

List installed skills:

    npx skills list

For global installations:

    npx skills list -g

Inspect the agent-specific skill directory shown by the CLI and confirm the selected skill folder contains `SKILL.md`. Restart or reload the relevant agent if it does not discover a newly installed skill immediately.

## 5. Update skills

Check for changes:

    npx skills check

Update global skills:

    npx skills update -g -y

## Troubleshooting

### "No valid skills found"

1. Confirm the repository contains `skills/<skill-name>/SKILL.md`.
2. Confirm each file begins with YAML frontmatter delimited by `---`.
3. Confirm `name` is lowercase kebab-case and matches its folder.
4. Confirm `description` is present and non-empty.
5. Run the repository validator: `python tests/validate_skills.py`.
6. List the repository again with `npx skills add valoranttgm123-svg/bos-digital-skills --list`.

### "Authentication failed"

The repository is intended to be public. Confirm the URL is exactly:

    https://github.com/valoranttgm123-svg/bos-digital-skills

If a public clone still fails, check network access to GitHub and update Git/Node tooling. GitHub CLI authentication can be checked with:

    gh auth status -h github.com

Do not paste access tokens, passwords, or SSH private keys into chat.

### Agent does not use the skill

- Confirm the CLI installed the skill for the intended agent.
- Confirm that the agent supports the Agent Skills convention and the selected installation path.
- Restart/reload the agent.
- Mention the skill's purpose explicitly in a test prompt.
- Check the agent's documentation for its currently supported skills directory.

## Compatibility note

The Skills CLI supports a set of agents and installation targets that can change over time. A successful repository install does not prove every agent implements every skill instruction or has the tools required to execute a workflow. Always verify within the target agent.
