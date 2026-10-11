# ADR-0002 — Conditional desktop stack candidate

- Status: PROPOSED; 2026-10-11. No adoption or implementation authorized.
- Context: Windows10 initial target but exact owner edition/build unknown; target facts cannot be obtained from cloud Linux.
- Problem: Select supported maintainable free stack without assuming current runtimes fit any Win10 laptop.
- Requirements affected: REQ-0001; NFR-0008 NFR-0014 NFR-0015 NFR-0020; individual unresolved details remain proposed.
- Alternatives considered: Native .NET/WPF; Python/PySide; Tauri/Rust/WebView2; Electron/Node.
- Evaluation criteria: correctness, security/privacy, supported Windows/offline behavior, free suitable licensing, recovery, modularity/testability, resources and minimal dependencies.
- Evidence: [design assessment](../specifications/P3-technology-evaluation.md); [source/license/support register](../specifications/P3-technology-evaluation.md#source-evidence-register). Documentary facts only; no runtime feasibility evidence.
- Proposed decision: Evaluate .NET10/WPF first only on vendor-listed exact target; evaluate alternatives if target mismatch. No final selection.
- Rationale: Native shell limits browser UI dependencies; MIT headline licenses and support-source evidence exist, but exact OS/transitives block adoption.
- Consequences: Possible target conflict; native .NET candidate does not solve browser engine compatibility.
- Risks: RISK-0001 RISK-0003; all OPEN per [risk register](../governance/09-execution-book.md).
- Verification prerequisites: Owner target, release-tag/runtime/native package/licenses, offline UI/assistive-tool P5 proof.
- Owner approval requirement: explicit approval of this ADR's exact scope after missing support/license/business evidence is resolved; P3 phase approval alone does not adopt technology or settle open requirements. Preserve history and mark supersession rather than overwriting approved decisions later.
