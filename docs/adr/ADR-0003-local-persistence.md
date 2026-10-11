# ADR-0003 — SQLite candidate and single durable writer

- Status: PROPOSED; 2026-10-11. No adoption or implementation authorized.
- Context: Local history/queue/audit/approval need transactional records and reliable backup without cloud DB.
- Problem: Keep DB relationships/durability and concurrency correct.
- Requirements affected: REQ-0024 REQ-0031; NFR-0011 NFR-0016 NFR-0018; individual unresolved details remain proposed.
- Alternatives considered: SQLite embedded; flat structured files; other embedded DB; service DB.
- Evaluation criteria: correctness, security/privacy, supported Windows/offline behavior, free suitable licensing, recovery, modularity/testability, resources and minimal dependencies.
- Evidence: [design assessment](../specifications/P3-persistence-artifacts.md); [source/license/support register](../specifications/P3-technology-evaluation.md#source-evidence-register). Documentary facts only; no runtime feasibility evidence.
- Proposed decision: Evaluate SQLite with one application writer, explicit FKs/revisions/durability and coordinated artifact intents.
- Rationale: Fits modest local queue/metadata and standard transaction support; no separate service.
- Consequences: Provider/native dependency and journal mode unchosen; busy/migration/backup behavior needs proof.
- Risks: RISK-0003 RISK-0009; all OPEN per [risk register](../governance/09-execution-book.md).
- Verification prerequisites: Exact provider/license/transitives, SQLite version/journal settings, crash/migration/backup/restore tests in P5/P11.
- Owner approval requirement: explicit approval of this ADR's exact scope after missing support/license/business evidence is resolved; P3 phase approval alone does not adopt technology or settle open requirements. Preserve history and mark supersession rather than overwriting approved decisions later.
