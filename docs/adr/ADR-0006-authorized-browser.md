# ADR-0006 — Conditional supported browser automation and strict scope

- Status: PROPOSED; 2026-10-11. No adoption or implementation authorized.
- Context: Website QA needs authorized requests and evidence; current Playwright sources list Windows11+ not native Win10.
- Problem: Avoid unsupported browser adoption or hidden scope escapes.
- Requirements affected: REQ-0028 REQ-0042 REQ-0045 REQ-0050; NFR-0023; individual unresolved details remain proposed.
- Alternatives considered: Current Playwright engine; evidenced alternative driver/browser; scoped nonbrowser checks; defer live capability.
- Evaluation criteria: correctness, security/privacy, supported Windows/offline behavior, free suitable licensing, recovery, modularity/testability, resources and minimal dependencies.
- Evidence: [design assessment](../specifications/P3-security-offline-network.md); [source/license/support register](../specifications/P3-technology-evaluation.md#source-evidence-register). Documentary facts only; no runtime feasibility evidence.
- Proposed decision: Keep Playwright research candidate blocked for native Win10 support unless exact supported configuration is evidenced; evaluate safe supported alternatives without changing OS target.
- Rationale: Correct target support and request authorization outrank tool convenience.
- Consequences: Alternative driver support/enforcement not verified; browser interception is not proof of all child traffic confinement.
- Risks: RISK-0001 RISK-0008; all OPEN per [risk register](../governance/09-execution-book.md).
- Verification prerequisites: Exact engine/driver/OS license support, request/redirect/DNS/service-worker/WebRTC/download containment proof; no obsolete insecure workaround.
- Owner approval requirement: explicit approval of this ADR's exact scope after missing support/license/business evidence is resolved; P3 phase approval alone does not adopt technology or settle open requirements. Preserve history and mark supersession rather than overwriting approved decisions later.
