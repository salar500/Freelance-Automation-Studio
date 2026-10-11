# ADR-0008 — Approval-bound manifests and local package attestation

- Status: PROPOSED; 2026-10-11. No adoption or implementation authorized.
- Context: Processing/validation/review/export represent different truths and reports can change after approval.
- Problem: Avoid automatic approval, stale exports and circular report/manifest hashes.
- Requirements affected: REQ-0019 REQ-0020 REQ-0022 REQ-0031; NFR-0018; individual unresolved details remain proposed.
- Alternatives considered: Single success flag; mutable folder approval; immutable approved payload manifest plus attestation/export record.
- Evaluation criteria: correctness, security/privacy, supported Windows/offline behavior, free suitable licensing, recovery, modularity/testability, resources and minimal dependencies.
- Evidence: [design assessment](../specifications/P3-reporting-packaging.md); [source/license/support register](../specifications/P3-technology-evaluation.md#source-evidence-register). Documentary facts only; no runtime feasibility evidence.
- Proposed decision: Propose explicit J human approval of immutable payload/evidence digests; N verifies bytes and produces separate sanitized attestation plus final export digests.
- Rationale: Exact scope/invalidation and noncircular manifest computation keep verifiable local handoff.
- Consequences: Asserted local identity and same-user tampering limitations remain; valid subset delivery interpretation not finalized.
- Risks: RISK-0002 RISK-0003; all OPEN per [risk register](../governance/09-execution-book.md).
- Verification prerequisites: Owner review scope/identity/partial-subset disposition, changed-file races, immutable evidence and export integrity tests.
- Owner approval requirement: explicit approval of this ADR's exact scope after missing support/license/business evidence is resolved; P3 phase approval alone does not adopt technology or settle open requirements. Preserve history and mark supersession rather than overwriting approved decisions later.
