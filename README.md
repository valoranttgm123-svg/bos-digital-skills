# BOS Digital Skills

[![Validate skills](https://github.com/valoranttgm123-svg/bos-digital-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/valoranttgm123-svg/bos-digital-skills/actions/workflows/validate-skills.yml)

Portable, open Agent Skills by **BOS Digital Indonesia**. Each skill is a focused instruction package that compatible AI agents can load when relevant.

## Skill catalog

### Creator and social media

| Skill | What it does |
|---|---|
| [bos-viral-content-studio](skills/bos-viral-content-studio/SKILL.md) | Creator workflow for trend research, hooks, short/long video scripts, storyboards, voice-over briefs, subtitles, editing, and publishing |
| [instagram-growth-agent](skills/instagram-growth-agent/SKILL.md) | Ethical Instagram profile strategy, content pillars, editorial calendars, organic distribution, and analytics |
| [youtube-creator-agent](skills/youtube-creator-agent/SKILL.md) | YouTube channel strategy, topic research, scripts, titles, thumbnails, Shorts, metadata, and analytics |

### Automation and development

| Skill | What it does |
|---|---|
| [browser-automation-agent](skills/browser-automation-agent/SKILL.md) | Authorized browser workflows, web research, testing, and safe form automation |
| [repository-engineering](skills/repository-engineering/SKILL.md) | Repository audits, implementation, bug fixing, tests, CI, and engineering handoffs |
| [windows-powershell-automation](skills/windows-powershell-automation/SKILL.md) | Safe Windows diagnosis, PowerShell administration, and automation |
| [app-analyzer-rebuilder](skills/app-analyzer-rebuilder/SKILL.md) | Authorized application analysis, architecture mapping, modernization, and clean rebuild planning |
| [ai-workflow-mcp-builder](skills/ai-workflow-mcp-builder/SKILL.md) | AI workflows, MCP tools/servers, tool contracts, permissions, tests, and deployment |

### Business, data, and research

| Skill | What it does |
|---|---|
| [umkm-copilot](skills/umkm-copilot/SKILL.md) | Indonesian UMKM operations, pricing, inventory, sales, payment reconciliation, and reporting |
| [small-business-operations](skills/small-business-operations/SKILL.md) | Repeatable procedures for retail, food and beverage, printing, photocopy, and service businesses |
| [excel-data-analyst](skills/excel-data-analyst/SKILL.md) | Excel/CSV inspection, cleaning, reconciliation, metrics, charts, and management reporting |
| [deep-research-fact-checker](skills/deep-research-fact-checker/SKILL.md) | Source-backed research, claim verification, current information, evidence ledgers, and uncertainty reporting |
| [xauusd-research-backtesting](skills/xauusd-research-backtesting/SKILL.md) | Evidence-based XAUUSD strategy research, backtesting design, metrics, costs, and robustness checks |

### Skill development

| Skill | What it does |
|---|---|
| [agent-skill-author](skills/agent-skill-author/SKILL.md) | Create, audit, test, and maintain reusable Agent Skills |

**15 skills** are currently included. Install everything or select only the skills you need.

## Install

List skills available in this repository:

    npx skills add valoranttgm123-svg/bos-digital-skills --list

Install all skills globally for all locally detected compatible agents:

    npx skills add valoranttgm123-svg/bos-digital-skills --all -g -y

Install only the creator studio globally:

    npx skills add valoranttgm123-svg/bos-digital-skills --skill bos-viral-content-studio -g -y

Install selected creator tools:

    npx skills add valoranttgm123-svg/bos-digital-skills --skill instagram-growth-agent --skill youtube-creator-agent -g -y

See [docs/INSTALLATION.md](docs/INSTALLATION.md) for selection, updates, troubleshooting, and compatibility notes.

## Examples and guides

- [Creator production playbook](docs/CREATOR_PRODUCTION_PLAYBOOK.md)
- [Safety and permission boundaries](docs/SAFETY_AND_PERMISSIONS.md)
- [Examples](examples/)
- [Contributing guide](CONTRIBUTING.md)

## Compatibility

The repository uses the open Agent Skills folder convention: each skill lives at `skills/<skill-name>/SKILL.md` and has YAML frontmatter with `name` and `description`. Actual loading behavior depends on the agent and installer version. Skills provide instructions; they do not grant new tools, credentials, account access, or system permissions.

## Safety and limitations

- Skills are workflow instructions, not a guarantee of output quality, views, sales, profit, search rankings, or financial returns.
- Current trends, platform rules, laws, product specs, and market data must be verified from current sources when relevant.
- Never fabricate metrics, sources, testimonials, payment status, historical prices, backtest results, or production outcomes.
- Obtain explicit approval before consequential external actions such as publishing, sending, buying, deleting, transferring money, or changing production systems.
- Respect copyright, privacy, platform terms, licenses, and applicable law.
- Do not commit credentials, API keys, private datasets, customer details, or confidential application artifacts.

## Validation

Run the standard-library validator locally:

    python tests/validate_skills.py

A GitHub Actions workflow runs the same validation on pushes and pull requests.

## License

Apache-2.0. See [LICENSE](LICENSE).
