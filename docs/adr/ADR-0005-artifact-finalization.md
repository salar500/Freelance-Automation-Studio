# ADR-0005 — Recoverable database/filesystem publication

- Status: PROPOSED; 2026-10-11. No adoption or implementation authorized.
- Context: Filesystem and SQLite do not share an atomic transaction.
- Problem: Prevent partially written output from appearing verified/approved after interruption.
- Requirements affected: REQ-0017 REQ-0018; NFR-0011 NFR-0012; individual unresolved details remain proposed.
- Alternatives considered: Store all blobs in DB; raw direct output writes; staged intents with rename/reconcile; external object store.
- Evaluation criteria: correctness, security/privacy, supported Windows/offline behavior, free suitable licensing, recovery, modularity/testability, resources and minimal dependencies.
- Evidence: [design assessment](../specifications/P3-persistence-artifacts.md); [source/license/support register](../specifications/P3-technology-evaluation.md#source-evidence-register). Documentary facts only; no runtime feasibility evidence.
- Proposed decision: Evaluate stage/validate/hash -> durable prepared intent -> supported same-volume rename -> verified DB finalization and restart reconciliation.
- Rationale: Preserves files and provenance while making each crash boundary detectable; local files remain independently inspectable.
- Consequences: Atomic visibility is not power-loss durability; cross-volume export needs weaker explicit protocol.
- Risks: RISK-0002 RISK-0009; all OPEN per [risk register](../governance/09-execution-book.md).
- Verification prerequisites: Windows filesystem flush/rename/TOCTOU/interruption/disk-full/backup consistency proof in P5.
- Owner approval requirement: explicit approval of this ADR's exact scope after missing support/license/business evidence is resolved; P3 phase approval alone does not adopt technology or settle open requirements. Preserve history and mark supersession rather than overwriting approved decisions later.
