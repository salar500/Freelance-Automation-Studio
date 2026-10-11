# ADR-0004 — Versioned local IPC and bounded workers

- Status: PROPOSED; 2026-10-11. No adoption or implementation authorized.
- Context: Untrusted parsers and browser children may crash or consume resources.
- Problem: Keep shell responsive and restrict effects without false sandbox claims.
- Requirements affected: REQ-0013 REQ-0014 REQ-0016; NFR-0004 NFR-0011 NFR-0013; individual unresolved details remain proposed.
- Alternatives considered: In-process libraries; inherited pipes; ACL named pipes; network service; OS-restricted process profiles.
- Evaluation criteria: correctness, security/privacy, supported Windows/offline behavior, free suitable licensing, recovery, modularity/testability, resources and minimal dependencies.
- Evidence: [design assessment](../specifications/P3-job-worker-protocol.md); [source/license/support register](../specifications/P3-technology-evaluation.md#source-evidence-register). Documentary facts only; no runtime feasibility evidence.
- Proposed decision: Propose attempt workers with versioned framed protocol, trusted launch, owned tree, scoped grants and Windows restriction assessment.
- Rationale: Contain fault lifecycle; avoid mandatory broker/TCP service; preserve clear validation/approval ownership.
- Consequences: Process isolation/Job Objects alone cannot constrain all user filesystem/network rights.
- Risks: RISK-0007 RISK-0008; all OPEN per [risk register](../governance/09-execution-book.md).
- Verification prerequisites: Effective token/ACL/child/network enforcement, nonce/schema/size/event/timeout races on target Windows in P5/P12.
- Owner approval requirement: explicit approval of this ADR's exact scope after missing support/license/business evidence is resolved; P3 phase approval alone does not adopt technology or settle open requirements. Preserve history and mark supersession rather than overwriting approved decisions later.
