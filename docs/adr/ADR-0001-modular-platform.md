# ADR-0001 — Modular monolith with isolated execution adapters

- Status: PROPOSED; 2026-10-11. No adoption or implementation authorized.
- Context: Four extensible local modules need consistent job/review/evidence semantics without cloud/service dependencies.
- Problem: Avoid inconsistent private implementations and UI parser crashes.
- Requirements affected: REQ-0006 REQ-0011 REQ-0029; NFR-0009 NFR-0010; individual unresolved details remain proposed.
- Alternatives considered: All-in-process application; modular monolith plus bounded workers; local services; microservices/cloud.
- Evaluation criteria: correctness, security/privacy, supported Windows/offline behavior, free suitable licensing, recovery, modularity/testability, resources and minimal dependencies.
- Evidence: [design assessment](../specifications/P3-system-components.md); [source/license/support register](../specifications/P3-technology-evaluation.md#source-evidence-register). Documentary facts only; no runtime feasibility evidence.
- Proposed decision: Prefer local modular monolith with shared services and contract-bound workers for risky operations.
- Rationale: Fewer deployable services and one semantic owner, with manageable IPC cost.
- Consequences: Worker packaging and recovery complexity; pure deterministic helpers may stay in process.
- Risks: RISK-0004 RISK-0007; all OPEN per [risk register](../governance/09-execution-book.md).
- Verification prerequisites: Contract extension proof, acyclic dependencies, ordinary-user offline deployment and fault containment in P5.
- Owner approval requirement: explicit approval of this ADR's exact scope after missing support/license/business evidence is resolved; P3 phase approval alone does not adopt technology or settle open requirements. Preserve history and mark supersession rather than overwriting approved decisions later.
