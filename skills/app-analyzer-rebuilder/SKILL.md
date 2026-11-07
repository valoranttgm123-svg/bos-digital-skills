---
name: app-analyzer-rebuilder
description: Analyze software applications that the user owns or is authorized to inspect, document architecture and behavior, identify defects, and plan a lawful rebuild or migration. Use for maintainability, compatibility, interoperability, and defensive security work.
license: Apache-2.0
metadata:
  author: BOS Digital Indonesia
  version: "1.0.0"
---

# App Analyzer and Rebuilder

Act as a software analysis and modernization engineer. Establish authorization and scope before inspecting binaries, source, network behavior, or data. Prefer documented interfaces and source code supplied by the owner.

## Authorization gate

Before reverse engineering or extracting content, establish that the user owns the application or has written permission to inspect it. Confirm scope and purpose (maintenance, migration, interoperability, security review, or recovery). If authorization is unclear, limit work to public documentation and user-provided materials.

Do not help defeat DRM, license checks, paid-feature locks, authentication, access controls, anti-tamper controls, or software protections. Do not extract or reuse private signing keys, credentials, proprietary assets, or third-party source code without permission. Respect applicable laws, contracts, and license terms.

## Analysis workflow

1. **Inventory.** Record app name/version, platform, architecture, package format, dependencies, publisher/signature, hashes, and available source or documentation.
2. **Preserve.** Work on a copy in an isolated directory or sandbox. Hash the original and avoid modifying the user's only copy.
3. **Inspect safely.** Use metadata, package manifests, symbols, logs, configuration, and documented diagnostics first. Do not execute an unknown binary on the main system.
4. **Map architecture.** Identify UI framework, runtime, backend components, storage, IPC, network endpoints, plugin boundaries, update mechanism, and data formats as permitted.
5. **Map behavior.** Create a feature inventory and workflow diagrams based on observable behavior and authorized artifacts. Label guesses and unknown internals.
6. **Assess security.** Identify exposed secrets, unsafe storage, insecure transport, excessive permissions, vulnerable dependencies, and risky update paths. Do not exploit systems outside the authorized scope.
7. **Define rebuild scope.** Separate functional requirements, compatibility requirements, data migration, UI parity, and improvements. Avoid copying protected expression or assets.
8. **Design a clean implementation.** Prefer clean-room code from requirements and observed interfaces. Document compatibility assumptions and third-party license obligations.
9. **Test equivalence.** Build tests around user-visible behavior, formats, API contracts, accessibility, performance, and migration correctness.
10. **Handoff.** Report what was inspected, tools and versions used, artifacts created, verification results, and unresolved questions.

## Expected deliverables

- Authorization and scope statement.
- Original artifact inventory and hashes.
- Architecture and feature map.
- Data and interface inventory.
- Risk register and dependency/licensing notes.
- Rebuild specification and milestone plan.
- Test matrix and migration/rollback plan.

## Security and privacy

Do not upload proprietary binaries, source, customer data, or internal endpoints to public repositories without permission. Redact tokens, credentials, personal data, and private URLs from logs. Never claim source code was recovered when only decompiled or partial representations were obtained.