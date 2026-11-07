# Changelog

All notable changes to BOS Digital Skills are recorded here. This project uses date-based release notes until tagged releases are published.

## 2026-11-07 — Creator Studio v1.0.2 QA Hardening

### Fixed
- Added stop-the-line rules for arithmetic component totals, IDR currency symbols, revenue-versus-expense semantics, Indonesian copyediting, exact transcript parity, duration units, rights evidence, and truthful completion status.
- Expanded the Creator Studio happy-path benchmark with regression checks for issues observed in the latest 45-second Reels package.
- Added a critical-failure condition for unsupported claims that calculations, synchronization, rights, or generated deliverables were verified.

## 2026-11-07 — Creator Studio v1.0.1 QA Update

### Fixed
- Added checks for scene/narration semantic consistency, Indonesian rupiah formatting, clean creative concepts, and cross-file CTA/subtitle parity.
- Added a reusable SRT validator and a checked 45-second sample transcript/SRT pair.
- Tightened the happy-path benchmark acceptance criteria based on the actual Codex output reviewed in this conversation.

## 2026-11-07 — Creator Studio Quality Hardening

### Added
- Explicit cross-deliverable consistency checks for scene meaning, voice-over, captions, and SRT text.
- Rupiah-specific currency notation and subtitle readability safeguards.
- SRT validator for cue order, timestamps, overlaps, duration, characters-per-second, and optional exact transcript matching.
- A clean 45-second Indonesian SRT/voice-over sample used by CI and the Windows local test runner.
- Additional Creator Studio benchmark acceptance criteria based on observed test failures.

### Clarifications
- Subtitle timing validation does not replace listening against final rendered audio.
- Rights and technical checklist items must be marked verified only when evidence exists.

## 2026-11-07 — Benchmark & Testing Suite

### Added
- 45 behavioral evaluation prompts covering all 15 published skills.
- Three scenario types per skill: normal task, missing inputs, and safety boundary.
- A 0–20 scoring rubric, critical-failure gates, and cross-agent pass criteria.
- A repeatable test protocol for Codex, OpenCode, and other compatible hosts.
- A results template to record agent/model versions, tool availability, scores, and failures.
- A prompt runner for listing and printing benchmark scenarios.
- A stricter repository validator for metadata, layout, basic Markdown integrity, and local links.
- A benchmark-manifest validator for scenario coverage and acceptance criteria.
- GitHub Actions checks for static validation, benchmark coverage, strict Agent Skills structure validation, and additional content-quality diagnostics.

### Clarifications
- Repository CI validates files and benchmark coverage; it does not execute live AI models.
- No cross-agent behavioral pass is claimed until scenarios are actually run and scored on each host/model.
- The community skill-validator is an additional diagnostic tool; it is not the Agent Skills specification itself.

## 2026-11-07 — Expanded Skill Catalog

### Added
- BOS Viral Content Studio
- Instagram Growth Agent
- YouTube Creator Agent
- Browser Automation Agent
- AI Design Studio
- UMKM Copilot
- Excel Data Analyst
- Deep Research & Fact Checker
- App Analyzer & Rebuilder
- AI Workflow & MCP Builder

The public catalog now contains 15 skills.
