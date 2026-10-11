# ADR-0007 — Explicit format, formula and fidelity profiles

- Status: PROPOSED; 2026-10-11. No adoption or implementation authorized.
- Context: CSV/XLSX/PDF/DOCX/website templates have unsupported features and uncertain transformations.
- Problem: Do not promise universal lossless conversion or automatic judgment.
- Requirements affected: REQ-0032 REQ-0040 REQ-0058 REQ-0059; NFR-0012; individual unresolved details remain proposed.
- Alternatives considered: Universal formats; explicit operation support/fidelity profiles; office automation/external conversion.
- Evaluation criteria: correctness, security/privacy, supported Windows/offline behavior, free suitable licensing, recovery, modularity/testability, resources and minimal dependencies.
- Evidence: [design assessment](../specifications/P3-module-designs.md); [source/license/support register](../specifications/P3-technology-evaluation.md#source-evidence-register). Documentary facts only; no runtime feasibility evidence.
- Proposed decision: Propose explicit assessed profiles and declared EXACT_REQUIRED/BEST_EFFORT/CONTENT_ONLY document concepts; new fuzzy/OCR/conversion capabilities stay conditional.
- Rationale: Safe limitations and review are testable and avoid misleading data-loss promises.
- Consequences: Feature/locale/formula/font/metadata and memory profiles require owner requirement disposition and PoC.
- Risks: RISK-0005 RISK-0006 RISK-0011; all OPEN per [risk register](../governance/09-execution-book.md).
- Verification prerequisites: Synthetic edge/fidelity/formula/decompression fixtures and exact selected parser/renderer licenses before support advertising.
- Owner approval requirement: explicit approval of this ADR's exact scope after missing support/license/business evidence is resolved; P3 phase approval alone does not adopt technology or settle open requirements. Preserve history and mark supersession rather than overwriting approved decisions later.
