# BOS Digital Skills

Portable, open Agent Skills by **BOS Digital Indonesia**. The skills use the open Agent Skills format and are intended for compatible coding agents and AI assistants.

## Included skills

| Skill | What it helps with |
|---|---|
| [xauusd-research-backtesting](skills/xauusd-research-backtesting/SKILL.md) | Evidence-based XAUUSD strategy research, backtesting design, metrics, and robustness checks |
| [windows-powershell-automation](skills/windows-powershell-automation/SKILL.md) | Safe Windows diagnosis, PowerShell administration, and automation |
| [repository-engineering](skills/repository-engineering/SKILL.md) | Software repository audits, implementation, testing, and engineering handoffs |
| [small-business-operations](skills/small-business-operations/SKILL.md) | Practical operating procedures for retail, food, printing, and service businesses |
| [agent-skill-author](skills/agent-skill-author/SKILL.md) | Create, review, and maintain portable Agent Skills |

## Install

Install every skill globally for the agents detected on your computer:

    npx skills add valoranttgm123-svg/bos-digital-skills --all --global --yes

Install only one skill:

    npx skills add valoranttgm123-svg/bos-digital-skills --skill xauusd-research-backtesting --global --yes

You can also install from a specific skill directory using the direct GitHub path supported by the Skills CLI.

## Compatibility

Skills follow the Agent Skills open format. Actual availability and installation paths depend on each agent's support and configuration. The repository does not grant an agent new tools, credentials, broker access, or system permissions.

## Safety and limitations

- Skills are instructions, not verified financial signals or autonomous permissions.
- XAUUSD historical results must be calculated from identified, suitable data. Never fabricate prices or backtest metrics.
- Windows changes that may disrupt a system require user authorization. Prefer read-only diagnostics first.
- Business payment records, customer information, and employee data must be protected.
- Review scripts and instructions before running them. Never place credentials, API keys, or private datasets in this repository.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) when available, or open an issue describing the proposed change.

## License

Apache-2.0. See [LICENSE](LICENSE).
