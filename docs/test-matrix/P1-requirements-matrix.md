# P1 requirements traceability and test definitions

Status: proposed coverage; all application tests NOT_RUN. This is the authoritative TEST allocation/definition register and initial matrix. Requirement statements live in the [requirements book](../governance/01-requirements-book.md), result semantics in the [testing book](../governance/06-testing-book.md). Each pair has a nominal/property check and an adverse/boundary check. Test priority inherits the requirement; relevant risk is identified in its requirement entry. No test execution is implied by allocation.

## Test prerequisites and procedure conventions
Prerequisites for every TEST: approved requirement and capability profile, implemented product, synthetic local fixture set, declared OS/tool versions, isolated temporary workspace, no real client secrets, and read-only original-fixture hashes. Website cases require a controlled test site and explicit authorization with request-observation evidence; deny cases verify no prohibited request occurs. Upgrade/Windows/screen-reader/usability cases require the appropriate Windows installations, assistive technology or consenting representative participants. Performance cases use the approved WP-1 replacement/profile with recorded measurements.

For each case set up the named inputs/condition, perform the stated acceptance procedure, compare observable output against the stated expected behavior, verify original hashes and collect local evidence (result report, output hashes, request trace or measurement as appropriate). “Expected” below is the assertion, not an actual outcome. Exact fixtures/automated commands are pending approved design/implementation; these are defined acceptance procedures, not runnable scripts.

## Requirement -> design -> implementation -> tests -> acceptance evidence
Each row has explicit pending fields. Doc-review evidence in the P1 report validates coverage only, not product behavior. P1 documentation is conditionally approved; exact requirement details/open decisions remain pending owner disposition. P2 links are conditional design references, not final architecture.

### REQ-0001
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0001 — Navigation](../governance/01-requirements-book.md#req-0001--navigation) | [conditional P2 UX](P2-ux-coverage.md#req-0001); [proposed P3 architecture](P3-architecture-coverage.md#req-0001); adoption and implementation pending | pending: authorized implementation | [TEST-0001](#test-0001), [TEST-0002](#test-0002) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0001
- Requirement: REQ-0001; purpose: Navigation nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: From the main view, reach clients, projects, job creation, history and settings without losing a saved job; show active project and job identity.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0002
- Requirement: REQ-0001; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Switch views with an unsaved edit; offer save/discard/cancel and cancel retains the edit.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0002
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0002 — Client records](../governance/01-requirements-book.md#req-0002--client-records) | [conditional P2 UX](P2-ux-coverage.md#req-0002); [proposed P3 architecture](P3-architecture-coverage.md#req-0002); adoption and implementation pending | pending: authorized implementation | [TEST-0003](#test-0003), [TEST-0004](#test-0004) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0003
- Requirement: REQ-0002; purpose: Client records nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Create, edit and archive a local client using a display name and optional notes; archived clients remain linked to history.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0004
- Requirement: REQ-0002; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Reject a blank display name; archiving does not erase project files or job evidence.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0003
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0003 — Project records](../governance/01-requirements-book.md#req-0003--project-records) | [conditional P2 UX](P2-ux-coverage.md#req-0003); [proposed P3 architecture](P3-architecture-coverage.md#req-0003); adoption and implementation pending | pending: authorized implementation | [TEST-0005](#test-0005), [TEST-0006](#test-0006) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0005
- Requirement: REQ-0003; purpose: Project records nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Create a named project linked to a client and chosen local workspace; list only its jobs when selected.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0006
- Requirement: REQ-0003; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Reject unavailable workspace before saving; changing projects does not move or overwrite files.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0004
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0004 — Job creation](../governance/01-requirements-book.md#req-0004--job-creation) | [conditional P2 UX](P2-ux-coverage.md#req-0004); [proposed P3 architecture](P3-architecture-coverage.md#req-0004); adoption and implementation pending | pending: authorized implementation | [TEST-0007](#test-0007), [TEST-0008](#test-0008) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0007
- Requirement: REQ-0004; purpose: Job creation nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Save a draft with unique job ID, project, module, input references and configuration; reopen with the same saved values.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0008
- Requirement: REQ-0004; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Reject execution of an incomplete draft and list missing fields without deleting it.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0005
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0005 — File import](../governance/01-requirements-book.md#req-0005--file-import) | [conditional P2 UX](P2-ux-coverage.md#req-0005); [proposed P3 architecture](P3-architecture-coverage.md#req-0005); adoption and implementation pending | pending: authorized implementation | [TEST-0009](#test-0009), [TEST-0010](#test-0010) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0009
- Requirement: REQ-0005; purpose: File import nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Select one or several supported local files; show path, size and format before processing; cancel import leaves the draft unchanged.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0010
- Requirement: REQ-0005; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Missing, unreadable or unsupported files are rejected with per-file reasons and no input modification.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0006
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0006 — Module selection](../governance/01-requirements-book.md#req-0006--module-selection) | [conditional P2 UX](P2-ux-coverage.md#req-0006); [proposed P3 architecture](P3-architecture-coverage.md#req-0006); adoption and implementation pending | pending: authorized implementation | [TEST-0011](#test-0011), [TEST-0012](#test-0012) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0011
- Requirement: REQ-0006; purpose: Module selection nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: List the four initial module categories and supported capabilities; choose one module per job and validate its configuration.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0012
- Requirement: REQ-0006; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: An unavailable capability cannot execute and explains its limitation without silently selecting another module.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0007
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0007 — Reusable templates](../governance/01-requirements-book.md#req-0007--reusable-templates) | [conditional P2 UX](P2-ux-coverage.md#req-0007); [proposed P3 architecture](P3-architecture-coverage.md#req-0007); adoption and implementation pending | pending: authorized implementation | [TEST-0013](#test-0013), [TEST-0014](#test-0014) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0013
- Requirement: REQ-0007; purpose: Reusable templates nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Save named/versioned configuration templates without client file contents or credentials; creating a job from a template makes an independent draft.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0014
- Requirement: REQ-0007; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Editing a template does not mutate prior jobs; invalid or obsolete options require explicit correction before use.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0008
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0008 — Input validation](../governance/01-requirements-book.md#req-0008--input-validation) | [conditional P2 UX](P2-ux-coverage.md#req-0008); [proposed P3 architecture](P3-architecture-coverage.md#req-0008); adoption and implementation pending | pending: authorized implementation | [TEST-0015](#test-0015), [TEST-0016](#test-0016) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0015
- Requirement: REQ-0008; purpose: Input validation nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Before planning, validate required fields, input accessibility, supported formats and option ranges; show each error with its field/file.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0016
- Requirement: REQ-0008; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: An invalid field or changed input stops planning; validation does not execute macros or modify inputs.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0009
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0009 — Execution plan](../governance/01-requirements-book.md#req-0009--execution-plan) | [conditional P2 UX](P2-ux-coverage.md#req-0009); [proposed P3 architecture](P3-architecture-coverage.md#req-0009); adoption and implementation pending | pending: authorized implementation | [TEST-0017](#test-0017), [TEST-0018](#test-0018) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0017
- Requirement: REQ-0009; purpose: Execution plan nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Before start, display inputs, operations, output paths, review requirements and whether network access is required; require confirmation of this plan.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0018
- Requirement: REQ-0009; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: A changed input/configuration after confirmation invalidates the plan and requires revalidation.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0010
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0010 — Destructive-action consent](../governance/01-requirements-book.md#req-0010--destructive-action-consent) | [conditional P2 UX](P2-ux-coverage.md#req-0010); [proposed P3 architecture](P3-architecture-coverage.md#req-0010); adoption and implementation pending | pending: authorized implementation | [TEST-0019](#test-0019), [TEST-0020](#test-0020) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0019
- Requirement: REQ-0010; purpose: Destructive-action consent nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: For every proposed overwrite/delete or irreversible action, display exact target, effect and recovery availability; require a fresh explicit confirmation.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0020
- Requirement: REQ-0010; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Reject/cancel yields no destructive effect; template or previous-job consent cannot approve a new action.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0011
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0011 — Processing](../governance/01-requirements-book.md#req-0011--processing) | [conditional P2 UX](P2-ux-coverage.md#req-0011); [proposed P3 architecture](P3-architecture-coverage.md#req-0011); adoption and implementation pending | pending: authorized implementation | [TEST-0021](#test-0021), [TEST-0022](#test-0022) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0021
- Requirement: REQ-0011; purpose: Processing nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Run only the validated, confirmed plan and record actual start/end, outcome and processed-item counts under its job ID.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0022
- Requirement: REQ-0011; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Injected operation failure prevents success classification and does not trigger unplanned operations.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0012
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0012 — Progress](../governance/01-requirements-book.md#req-0012--progress) | [conditional P2 UX](P2-ux-coverage.md#req-0012); [proposed P3 architecture](P3-architecture-coverage.md#req-0012); adoption and implementation pending | pending: authorized implementation | [TEST-0023](#test-0023), [TEST-0024](#test-0024) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0023
- Requirement: REQ-0012; purpose: Progress nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Show current job state, current operation, completed/total items when known and recent activity; unknown totals are labeled indeterminate.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0024
- Requirement: REQ-0012; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: A stalled operation is not reported complete; estimates are labeled estimates rather than measured completion.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0013
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0013 — Cancellation](../governance/01-requirements-book.md#req-0013--cancellation) | [conditional P2 UX](P2-ux-coverage.md#req-0013); [proposed P3 architecture](P3-architecture-coverage.md#req-0013); adoption and implementation pending | pending: authorized implementation | [TEST-0025](#test-0025), [TEST-0026](#test-0026) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0025
- Requirement: REQ-0013; purpose: Cancellation nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Accept cancellation during a running job; cease starting new items and classify output as cancelled/partial with item dispositions.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0026
- Requirement: REQ-0013; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Cancel at start, mid-item and near completion; preserve originals and never present an incomplete output as approved delivery.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0014
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0014 — Failure reporting](../governance/01-requirements-book.md#req-0014--failure-reporting) | [conditional P2 UX](P2-ux-coverage.md#req-0014); [proposed P3 architecture](P3-architecture-coverage.md#req-0014); adoption and implementation pending | pending: authorized implementation | [TEST-0027](#test-0027), [TEST-0028](#test-0028) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0027
- Requirement: REQ-0014; purpose: Failure reporting nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Record a failed item/operation, safe cause, affected outputs and permitted next action; retain a failure report even when no output is produced.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0028
- Requirement: REQ-0014; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Unreadable output destination and malformed input both show an actionable failure without exposing credentials.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0015
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0015 — Retry](../governance/01-requirements-book.md#req-0015--retry) | [conditional P2 UX](P2-ux-coverage.md#req-0015); [proposed P3 architecture](P3-architecture-coverage.md#req-0015); adoption and implementation pending | pending: authorized implementation | [TEST-0029](#test-0029), [TEST-0030](#test-0030) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0029
- Requirement: REQ-0015; purpose: Retry nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Allow a new linked attempt of a failed/cancelled job after revalidation; identify what will rerun and isolate its outputs.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0030
- Requirement: REQ-0015; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Changed inputs invalidate reuse; retry must not overwrite an earlier successful output without new consent.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0016
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0016 — Interrupted-job recovery](../governance/01-requirements-book.md#req-0016--interrupted-job-recovery) | [conditional P2 UX](P2-ux-coverage.md#req-0016); [proposed P3 architecture](P3-architecture-coverage.md#req-0016); adoption and implementation pending | pending: authorized implementation | [TEST-0031](#test-0031), [TEST-0032](#test-0032) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0031
- Requirement: REQ-0016; purpose: Interrupted-job recovery nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: After restart, identify interrupted jobs and offer inspection plus eligible resume or safe retry; retain prior evidence and classify unfinished outputs.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0032
- Requirement: REQ-0016; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: For a non-resumable operation, explain the limitation and offer safe retry; never mark the interrupted run successful.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0017
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0017 — Evidence capture](../governance/01-requirements-book.md#req-0017--evidence-capture) | [conditional P2 UX](P2-ux-coverage.md#req-0017); [proposed P3 architecture](P3-architecture-coverage.md#req-0017); adoption and implementation pending | pending: authorized implementation | [TEST-0033](#test-0033), [TEST-0034](#test-0034) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0033
- Requirement: REQ-0017; purpose: Evidence capture nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Every started run produces a local record with job/attempt ID, timestamps, module/tool versions, input hashes, normalized configuration, item outcomes, output hashes and warnings.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0034
- Requirement: REQ-0017; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: If durable evidence cannot be written, do not start or finalize as success; redact secrets and identify unavailable evidence.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0018
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0018 — Output validation](../governance/01-requirements-book.md#req-0018--output-validation) | [conditional P2 UX](P2-ux-coverage.md#req-0018); [proposed P3 architecture](P3-architecture-coverage.md#req-0018); adoption and implementation pending | pending: authorized implementation | [TEST-0035](#test-0035), [TEST-0036](#test-0036) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0035
- Requirement: REQ-0018; purpose: Output validation nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Apply declared module output checks; report pass/fail/uncertain per output and link them to the run evidence.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0036
- Requirement: REQ-0018; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: An unreadable or mismatched output fails validation and cannot enter the approved package.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0019
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0019 — Human review](../governance/01-requirements-book.md#req-0019--human-review) | [conditional P2 UX](P2-ux-coverage.md#req-0019); [proposed P3 architecture](P3-architecture-coverage.md#req-0019); adoption and implementation pending | pending: authorized implementation | [TEST-0037](#test-0037), [TEST-0038](#test-0038) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0037
- Requirement: REQ-0019; purpose: Human review nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Present uncertain or failed validation findings with evidence and allow recorded accept/reject plus rationale by a locally identified reviewer.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0038
- Requirement: REQ-0019; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: No response is not approval; rejection retains evidence and excludes the output from approved packaging.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0020
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0020 — Delivery approval](../governance/01-requirements-book.md#req-0020--delivery-approval) | [conditional P2 UX](P2-ux-coverage.md#req-0020); [proposed P3 architecture](P3-architecture-coverage.md#req-0020); adoption and implementation pending | pending: authorized implementation | [TEST-0039](#test-0039), [TEST-0040](#test-0040) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0039
- Requirement: REQ-0020; purpose: Delivery approval nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Require explicit reviewer approval tied to exact output hashes and run ID before labeling a package ready for client delivery.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0040
- Requirement: REQ-0020; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Changing any approved file invalidates approval; validation success alone is insufficient.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0021
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0021 — Reports](../governance/01-requirements-book.md#req-0021--reports) | [conditional P2 UX](P2-ux-coverage.md#req-0021); [proposed P3 architecture](P3-architecture-coverage.md#req-0021); adoption and implementation pending | pending: authorized implementation | [TEST-0041](#test-0041), [TEST-0042](#test-0042) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0041
- Requirement: REQ-0021; purpose: Reports nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Generate a human-readable local report listing plan, item counts, outcomes, warnings, validation findings and approval state.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0042
- Requirement: REQ-0021; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Partial/failed/cancelled runs remain distinguishable; report-generation failure is recorded rather than hidden as success.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0022
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0022 — Deliverable packaging](../governance/01-requirements-book.md#req-0022--deliverable-packaging) | [conditional P2 UX](P2-ux-coverage.md#req-0022); [proposed P3 architecture](P3-architecture-coverage.md#req-0022); adoption and implementation pending | pending: authorized implementation | [TEST-0043](#test-0043), [TEST-0044](#test-0044) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0043
- Requirement: REQ-0022; purpose: Deliverable packaging nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Create a local package containing only selected approved outputs and a manifest of paths/hashes; show contents for review.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0044
- Requirement: REQ-0022; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Exclude raw inputs, unrelated client files and credentials by default; a hash mismatch prevents ready-for-delivery status.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0023
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0023 — Export](../governance/01-requirements-book.md#req-0023--export) | [conditional P2 UX](P2-ux-coverage.md#req-0023); [proposed P3 architecture](P3-architecture-coverage.md#req-0023); adoption and implementation pending | pending: authorized implementation | [TEST-0045](#test-0045), [TEST-0046](#test-0046) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0045
- Requirement: REQ-0023; purpose: Export nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Export selected reports/evidence/packages to a user-chosen local destination and preserve source records.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0046
- Requirement: REQ-0023; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Cancel changes nothing; existing destination collision requires a new name or explicit overwrite consent.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0024
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0024 — History](../governance/01-requirements-book.md#req-0024--history) | [conditional P2 UX](P2-ux-coverage.md#req-0024); [proposed P3 architecture](P3-architecture-coverage.md#req-0024); adoption and implementation pending | pending: authorized implementation | [TEST-0047](#test-0047), [TEST-0048](#test-0048) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0047
- Requirement: REQ-0024; purpose: History nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Find local attempts by client/project/date/module/outcome and inspect their evidence and approval state.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0048
- Requirement: REQ-0024; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Missing external files are shown as unavailable; historical records are not silently rewritten to imply success.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0025
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0025 — Settings](../governance/01-requirements-book.md#req-0025--settings) | [conditional P2 UX](P2-ux-coverage.md#req-0025); [proposed P3 architecture](P3-architecture-coverage.md#req-0025); adoption and implementation pending | pending: authorized implementation | [TEST-0049](#test-0049), [TEST-0050](#test-0050) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0049
- Requirement: REQ-0025; purpose: Settings nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Persist local preferences for default output location and proposed job defaults; show effective values before execution.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0050
- Requirement: REQ-0025; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Invalid settings are rejected; changing a preference does not alter completed jobs or already confirmed plans.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0026
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0026 — Local data management](../governance/01-requirements-book.md#req-0026--local-data-management) | [conditional P2 UX](P2-ux-coverage.md#req-0026); [proposed P3 architecture](P3-architecture-coverage.md#req-0026); adoption and implementation pending | pending: authorized implementation | [TEST-0051](#test-0051), [TEST-0052](#test-0052) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0051
- Requirement: REQ-0026; purpose: Local data management nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: List managed records/output storage and offer selective archive/delete with affected evidence references and consent.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0052
- Requirement: REQ-0026; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Never delete original input files through history cleanup; deletion lists affected records and handles locked files as partial failure.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0027
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0027 — Offline gating](../governance/01-requirements-book.md#req-0027--offline-gating) | [conditional P2 UX](P2-ux-coverage.md#req-0027); [proposed P3 architecture](P3-architecture-coverage.md#req-0027); adoption and implementation pending | pending: authorized implementation | [TEST-0053](#test-0053), [TEST-0054](#test-0054) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0053
- Requirement: REQ-0027; purpose: Offline gating nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Allow local-job planning/execution/review/export with no connectivity; network-dependent jobs explain target connectivity requirements before start.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0054
- Requirement: REQ-0027; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: With network unavailable, a website job reports a specific connectivity failure while local jobs remain usable.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0028
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0028 — Target authorization](../governance/01-requirements-book.md#req-0028--target-authorization) | [conditional P2 UX](P2-ux-coverage.md#req-0028); [proposed P3 architecture](P3-architecture-coverage.md#req-0028); adoption and implementation pending | pending: authorized implementation | [TEST-0055](#test-0055), [TEST-0056](#test-0056) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0055
- Requirement: REQ-0028; purpose: Target authorization nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Before any live website request, require a local authorization record covering target hosts/paths, actions, expiry and permission evidence; attach it to the plan.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0056
- Requirement: REQ-0028; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Missing/expired authorization, out-of-scope redirects and unauthorized hosts/actions are blocked before the prohibited request.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0029
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0029 — Job concurrency controls](../governance/01-requirements-book.md#req-0029--job-concurrency-controls) | [conditional P2 UX](P2-ux-coverage.md#req-0029); [proposed P3 architecture](P3-architecture-coverage.md#req-0029); adoption and implementation pending | pending: authorized implementation | [TEST-0057](#test-0057), [TEST-0058](#test-0058) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0057
- Requirement: REQ-0029; purpose: Job concurrency controls nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Detect plans writing to the same target and prevent conflicting simultaneous writes; report the blocked job and conflict.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0058
- Requirement: REQ-0029; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Two simultaneous attempts with colliding destinations cannot silently corrupt or overwrite each other's outputs.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0030
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0030 — Client-data locality](../governance/01-requirements-book.md#req-0030--client-data-locality) | [conditional P2 UX](P2-ux-coverage.md#req-0030); [proposed P3 architecture](P3-architecture-coverage.md#req-0030); adoption and implementation pending | pending: authorized implementation | [TEST-0059](#test-0059), [TEST-0060](#test-0060) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0059
- Requirement: REQ-0030; purpose: Client-data locality nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: No job or diagnostic action uploads local client inputs, outputs, logs or reports; website tests use only explicitly authorized synthetic test data.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0060
- Requirement: REQ-0030; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Any local client file selected for a website request is blocked; only separately authorized synthetic test values may be sent. No cloud storage or telemetry is enabled.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0031
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0031 — Review audit](../governance/01-requirements-book.md#req-0031--review-audit) | [conditional P2 UX](P2-ux-coverage.md#req-0031); [proposed P3 architecture](P3-architecture-coverage.md#req-0031); adoption and implementation pending | pending: authorized implementation | [TEST-0061](#test-0061), [TEST-0062](#test-0062) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0061
- Requirement: REQ-0031; purpose: Review audit nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Store review/consent decisions with local reviewer label, timestamp, decision, rationale where required and exact artifact/plan reference.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0062
- Requirement: REQ-0031; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: An altered artifact is displayed as changed since approval; a local identity label is not represented as verified external authentication.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0032
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0032 — Supported capability disclosure](../governance/01-requirements-book.md#req-0032--supported-capability-disclosure) | [conditional P2 UX](P2-ux-coverage.md#req-0032); [proposed P3 architecture](P3-architecture-coverage.md#req-0032); adoption and implementation pending | pending: authorized implementation | [TEST-0063](#test-0063), [TEST-0064](#test-0064) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0063
- Requirement: REQ-0032; purpose: Supported capability disclosure nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Show supported formats/features and limits for each operation before start; fail explicitly when a requested feature cannot be preserved.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0064
- Requirement: REQ-0032; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Unsupported embedded content or format is not silently dropped; conversion with stated losses requires human review.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0033
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0033 — CSV interpretation](../governance/01-requirements-book.md#req-0033--csv-interpretation) | [conditional P2 UX](P2-ux-coverage.md#req-0033); [proposed P3 architecture](P3-architecture-coverage.md#req-0033); adoption and implementation pending | pending: authorized implementation | [TEST-0065](#test-0065), [TEST-0066](#test-0066) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0065
- Requirement: REQ-0033; purpose: CSV interpretation nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: For CSV jobs, show delimiter, encoding, header choice and preview; permit explicit override and persist the chosen interpretation.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0066
- Requirement: REQ-0033; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Ambiguous encoding/delimiter or inconsistent field counts blocks processing until resolved; UTF-8 quoted multiline fields round-trip in the declared profile.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0034
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0034 — Spreadsheet selection](../governance/01-requirements-book.md#req-0034--spreadsheet-selection) | [conditional P2 UX](P2-ux-coverage.md#req-0034); [proposed P3 architecture](P3-architecture-coverage.md#req-0034); adoption and implementation pending | pending: authorized implementation | [TEST-0067](#test-0067), [TEST-0068](#test-0068) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0067
- Requirement: REQ-0034; purpose: Spreadsheet selection nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: For proposed XLSX inputs, list sheets and allow explicit sheet/range/header selection with preview.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0068
- Requirement: REQ-0034; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Missing sheet/range and encrypted or unsupported workbook features fail safely; no macros are executed.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0035
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0035 — Data cleaning](../governance/01-requirements-book.md#req-0035--data-cleaning) | [conditional P2 UX](P2-ux-coverage.md#req-0035); [proposed P3 architecture](P3-architecture-coverage.md#req-0035); adoption and implementation pending | pending: authorized implementation | [TEST-0069](#test-0069), [TEST-0070](#test-0070) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0069
- Requirement: REQ-0035; purpose: Data cleaning nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Configure trim, empty-value handling and exact duplicate removal independently; report changed/removed counts and retain input order unless configured otherwise.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0070
- Requirement: REQ-0035; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Unselected columns remain unchanged; duplicates differing outside the configured key are retained according to the shown rule.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0036
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0036 — Filter and sort](../governance/01-requirements-book.md#req-0036--filter-and-sort) | [conditional P2 UX](P2-ux-coverage.md#req-0036); [proposed P3 architecture](P3-architecture-coverage.md#req-0036); adoption and implementation pending | pending: authorized implementation | [TEST-0071](#test-0071), [TEST-0072](#test-0072) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0071
- Requirement: REQ-0036; purpose: Filter and sort nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Apply typed filter conditions and explicit sort keys/directions; record selected/excluded counts and stable tie behavior.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0072
- Requirement: REQ-0036; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Invalid numeric/date conversion produces a row-level finding; locale interpretation is explicit and never silently guessed.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0037
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0037 — Column mapping](../governance/01-requirements-book.md#req-0037--column-mapping) | [conditional P2 UX](P2-ux-coverage.md#req-0037); [proposed P3 architecture](P3-architecture-coverage.md#req-0037); adoption and implementation pending | pending: authorized implementation | [TEST-0073](#test-0073), [TEST-0074](#test-0074) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0073
- Requirement: REQ-0037; purpose: Column mapping nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Select, rename and reorder columns using a displayed mapping; preview the resulting schema.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0074
- Requirement: REQ-0037; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Reject duplicate output names or missing source columns before execution.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0038
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0038 — Join and combine](../governance/01-requirements-book.md#req-0038--join-and-combine) | [conditional P2 UX](P2-ux-coverage.md#req-0038); [proposed P3 architecture](P3-architecture-coverage.md#req-0038); adoption and implementation pending | pending: authorized implementation | [TEST-0075](#test-0075), [TEST-0076](#test-0076) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0075
- Requirement: REQ-0038; purpose: Join and combine nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Combine compatible tables or join on configured keys; report unmatched keys and duplicate-key policy before applying it.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0076
- Requirement: REQ-0038; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Conflicting schemas and many-to-many expansion exceeding the approved plan stop or require a revised plan, not silent truncation.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0039
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0039 — Rule-based validation](../governance/01-requirements-book.md#req-0039--rule-based-validation) | [conditional P2 UX](P2-ux-coverage.md#req-0039); [proposed P3 architecture](P3-architecture-coverage.md#req-0039); adoption and implementation pending | pending: authorized implementation | [TEST-0077](#test-0077), [TEST-0078](#test-0078) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0077
- Requirement: REQ-0039; purpose: Rule-based validation nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Evaluate required-value, type, allowed-value and uniqueness rules; emit row/column findings linked to the rule.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0078
- Requirement: REQ-0039; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Invalid rows are flagged rather than silently deleted; no configured rules is reported as no rules evaluated, not full validation.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0040
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0040 — Spreadsheet export](../governance/01-requirements-book.md#req-0040--spreadsheet-export) | [conditional P2 UX](P2-ux-coverage.md#req-0040); [proposed P3 architecture](P3-architecture-coverage.md#req-0040); adoption and implementation pending | pending: authorized implementation | [TEST-0079](#test-0079), [TEST-0080](#test-0080) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0079
- Requirement: REQ-0040; purpose: Spreadsheet export nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Produce proposed CSV/XLSX outputs with declared encoding/schema and validate row/column counts plus configured preservation properties.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0080
- Requirement: REQ-0040; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Formula text, leading zeros and date values are preserved under the declared profile or flagged unsupported before start; export failure never overwrites the source.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0041
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0041 — Spreadsheet change summary](../governance/01-requirements-book.md#req-0041--spreadsheet-change-summary) | [conditional P2 UX](P2-ux-coverage.md#req-0041); [proposed P3 architecture](P3-architecture-coverage.md#req-0041); adoption and implementation pending | pending: authorized implementation | [TEST-0081](#test-0081), [TEST-0082](#test-0082) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0081
- Requirement: REQ-0041; purpose: Spreadsheet change summary nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Report original/output counts, changed cells/rows, rejected records and rule results with deterministic local evidence.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0082
- Requirement: REQ-0041; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Sensitive cell values are omitted from general logs; any detailed client-data evidence remains local and explicitly included for review.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0042
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0042 — Website test scope](../governance/01-requirements-book.md#req-0042--website-test-scope) | [conditional P2 UX](P2-ux-coverage.md#req-0042); [proposed P3 architecture](P3-architecture-coverage.md#req-0042); adoption and implementation pending | pending: authorized implementation | [TEST-0083](#test-0083), [TEST-0084](#test-0084) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0083
- Requirement: REQ-0042; purpose: Website test scope nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Choose an authorized base target, permitted routes and request budget before a run; report the effective allowlist.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0084
- Requirement: REQ-0042; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: A redirect, link or asset outside approved target scope is blocked and reported unless separately authorized.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0043
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0043 — Availability and links](../governance/01-requirements-book.md#req-0043--availability-and-links) | [conditional P2 UX](P2-ux-coverage.md#req-0043); [proposed P3 architecture](P3-architecture-coverage.md#req-0043); adoption and implementation pending | pending: authorized implementation | [TEST-0085](#test-0085), [TEST-0086](#test-0086) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0085
- Requirement: REQ-0043; purpose: Availability and links nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Check configured pages and permitted links for response status and navigation errors; list tested and untested URLs with reasons.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0086
- Requirement: REQ-0043; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Timeout/TLS failure is recorded distinctly from a broken link; never disable certificate verification to pass.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0044
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0044 — Content assertions](../governance/01-requirements-book.md#req-0044--content-assertions) | [conditional P2 UX](P2-ux-coverage.md#req-0044); [proposed P3 architecture](P3-architecture-coverage.md#req-0044); adoption and implementation pending | pending: authorized implementation | [TEST-0087](#test-0087), [TEST-0088](#test-0088) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0087
- Requirement: REQ-0044; purpose: Content assertions nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Evaluate explicit text, element-presence and attribute assertions on approved pages and report expected versus observed values.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0088
- Requirement: REQ-0044; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: A missing selector or ambiguous multiple match fails the relevant assertion; no assertions is labeled no assertions configured.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0045
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0045 — Interaction scenarios](../governance/01-requirements-book.md#req-0045--interaction-scenarios) | [conditional P2 UX](P2-ux-coverage.md#req-0045); [proposed P3 architecture](P3-architecture-coverage.md#req-0045); adoption and implementation pending | pending: authorized implementation | [TEST-0089](#test-0089), [TEST-0090](#test-0090) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0089
- Requirement: REQ-0045; purpose: Interaction scenarios nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Run explicitly configured navigation/form scenarios with approved synthetic test values; record steps and assertions.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0090
- Requirement: REQ-0045; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: A state-changing submission requires authorization for that action; absence of authorization blocks the step without posting data.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0046
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0046 — Regression baselines](../governance/01-requirements-book.md#req-0046--regression-baselines) | [conditional P2 UX](P2-ux-coverage.md#req-0046); [proposed P3 architecture](P3-architecture-coverage.md#req-0046); adoption and implementation pending | pending: authorized implementation | [TEST-0091](#test-0091), [TEST-0092](#test-0092) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0091
- Requirement: REQ-0046; purpose: Regression baselines nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Compare current findings to a reviewed versioned baseline and classify new, unchanged and resolved issues.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0092
- Requirement: REQ-0046; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Missing/stale baseline yields no regression verdict; accepting a new baseline requires recorded human review.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0047
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0047 — Visual evidence](../governance/01-requirements-book.md#req-0047--visual-evidence) | [conditional P2 UX](P2-ux-coverage.md#req-0047); [proposed P3 architecture](P3-architecture-coverage.md#req-0047); adoption and implementation pending | pending: authorized implementation | [TEST-0093](#test-0093), [TEST-0094](#test-0094) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0093
- Requirement: REQ-0047; purpose: Visual evidence nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Capture local screenshots for configured viewports and compare against approved baselines using declared tolerance/ignored regions.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0094
- Requirement: REQ-0047; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Unstable regions or rendering differences are flagged uncertain; visual comparison cannot silently replace a baseline.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0048
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0048 — Viewport checks](../governance/01-requirements-book.md#req-0048--viewport-checks) | [conditional P2 UX](P2-ux-coverage.md#req-0048); [proposed P3 architecture](P3-architecture-coverage.md#req-0048); adoption and implementation pending | pending: authorized implementation | [TEST-0095](#test-0095), [TEST-0096](#test-0096) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0095
- Requirement: REQ-0048; purpose: Viewport checks nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Run configured pages at proposed desktop/mobile viewport sizes and record overflow and configured layout assertions.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0096
- Requirement: REQ-0048; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Unavailable viewport capability is reported as not run; viewport emulation is not claimed as testing on a real mobile device.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0049
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0049 — Basic accessibility checks](../governance/01-requirements-book.md#req-0049--basic-accessibility-checks) | [conditional P2 UX](P2-ux-coverage.md#req-0049); [proposed P3 architecture](P3-architecture-coverage.md#req-0049); adoption and implementation pending | pending: authorized implementation | [TEST-0097](#test-0097), [TEST-0098](#test-0098) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0097
- Requirement: REQ-0049; purpose: Basic accessibility checks nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Evaluate declared automated checks such as accessible names, image alternatives and label associations; report rule ID and element evidence.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0098
- Requirement: REQ-0049; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Report automated scope/limitations and never label the entire site accessibility-compliant from automated results alone.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0050
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0050 — Website results](../governance/01-requirements-book.md#req-0050--website-results) | [conditional P2 UX](P2-ux-coverage.md#req-0050); [proposed P3 architecture](P3-architecture-coverage.md#req-0050); adoption and implementation pending | pending: authorized implementation | [TEST-0099](#test-0099), [TEST-0100](#test-0100) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0099
- Requirement: REQ-0050; purpose: Website results nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Produce per-page/step PASS, FAIL, UNCERTAIN, BLOCKED or NOT_RUN results with timing, authorization reference and evidence.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0100
- Requirement: REQ-0050; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: A network outage or blocked external asset cannot be converted into a passing website assertion; sensitive test data is redacted.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0051
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0051 — Document import](../governance/01-requirements-book.md#req-0051--document-import) | [conditional P2 UX](P2-ux-coverage.md#req-0051); [proposed P3 architecture](P3-architecture-coverage.md#req-0051); adoption and implementation pending | pending: authorized implementation | [TEST-0101](#test-0101), [TEST-0102](#test-0102) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0101
- Requirement: REQ-0051; purpose: Document import nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: For proposed PDF/TXT/DOCX profiles, identify page/section counts and declared support limitations before processing.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0102
- Requirement: REQ-0051; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Corrupt/encrypted files fail with a safe explanation; restricted documents are not decrypted or modified without legitimate authorization and supported access.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0052
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0052 — PDF split](../governance/01-requirements-book.md#req-0052--pdf-split) | [conditional P2 UX](P2-ux-coverage.md#req-0052); [proposed P3 architecture](P3-architecture-coverage.md#req-0052); adoption and implementation pending | pending: authorized implementation | [TEST-0103](#test-0103), [TEST-0104](#test-0104) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0103
- Requirement: REQ-0052; purpose: PDF split nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Split a PDF using explicit page ranges into separately named outputs; verify selected page counts and order.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0104
- Requirement: REQ-0052; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Reject out-of-range/empty selections; overlapping ranges are shown in the plan rather than silently deduplicated.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0053
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0053 — PDF merge](../governance/01-requirements-book.md#req-0053--pdf-merge) | [conditional P2 UX](P2-ux-coverage.md#req-0053); [proposed P3 architecture](P3-architecture-coverage.md#req-0053); adoption and implementation pending | pending: authorized implementation | [TEST-0105](#test-0105), [TEST-0106](#test-0106) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0105
- Requirement: REQ-0053; purpose: PDF merge nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Merge selected PDFs in a user-confirmed file/page order and validate combined page count.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0106
- Requirement: REQ-0053; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Incompatible/restricted input causes a failure or explicit exclusion review; missing pages cannot silently pass validation.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0054
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0054 — Page reorganization](../governance/01-requirements-book.md#req-0054--page-reorganization) | [conditional P2 UX](P2-ux-coverage.md#req-0054); [proposed P3 architecture](P3-architecture-coverage.md#req-0054); adoption and implementation pending | pending: authorized implementation | [TEST-0107](#test-0107), [TEST-0108](#test-0108) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0107
- Requirement: REQ-0054; purpose: Page reorganization nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Rotate/reorder or omit pages only as specified in the confirmed plan and report source-to-output page mapping.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0108
- Requirement: REQ-0054; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Duplicate/invalid page references are rejected unless explicit duplication is intended; originals remain unchanged.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0055
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0055 — Text extraction](../governance/01-requirements-book.md#req-0055--text-extraction) | [conditional P2 UX](P2-ux-coverage.md#req-0055); [proposed P3 architecture](P3-architecture-coverage.md#req-0055); adoption and implementation pending | pending: authorized implementation | [TEST-0109](#test-0109), [TEST-0110](#test-0110) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0109
- Requirement: REQ-0055; purpose: Text extraction nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Extract available text to local outputs with page references and report pages without a usable text layer.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0110
- Requirement: REQ-0055; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Scanned/no-text pages are flagged, not reported as successfully transcribed; OCR is not assumed part of the initial baseline.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0056
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0056 — Template substitution](../governance/01-requirements-book.md#req-0056--template-substitution) | [conditional P2 UX](P2-ux-coverage.md#req-0056); [proposed P3 architecture](P3-architecture-coverage.md#req-0056); adoption and implementation pending | pending: authorized implementation | [TEST-0111](#test-0111), [TEST-0112](#test-0112) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0111
- Requirement: REQ-0056; purpose: Template substitution nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: For approved text/document templates, replace declared placeholders from local supplied values and list resolved/unresolved fields.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0112
- Requirement: REQ-0056; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Missing required fields block finalization; embedded scripts/macros are never executed.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0057
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0057 — Batch document jobs](../governance/01-requirements-book.md#req-0057--batch-document-jobs) | [conditional P2 UX](P2-ux-coverage.md#req-0057); [proposed P3 architecture](P3-architecture-coverage.md#req-0057); adoption and implementation pending | pending: authorized implementation | [TEST-0113](#test-0113), [TEST-0114](#test-0114) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0113
- Requirement: REQ-0057; purpose: Batch document jobs nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Apply one confirmed operation to selected documents, generating distinct outputs and per-file outcomes.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0114
- Requirement: REQ-0057; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: One corrupt file is recorded as failure; continue remaining files only under the shown continue-on-error option, with the overall run partial.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0058
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0058 — Document validation](../governance/01-requirements-book.md#req-0058--document-validation) | [conditional P2 UX](P2-ux-coverage.md#req-0058); [proposed P3 architecture](P3-architecture-coverage.md#req-0058); adoption and implementation pending | pending: authorized implementation | [TEST-0115](#test-0115), [TEST-0116](#test-0116) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0115
- Requirement: REQ-0058; purpose: Document validation nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Reopen generated documents and verify declared page/section count, order and required content properties.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0116
- Requirement: REQ-0058; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Unsupported fidelity-sensitive content is flagged before start; extraction cannot claim preservation of visual layout.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0059
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0059 — Document review evidence](../governance/01-requirements-book.md#req-0059--document-review-evidence) | [conditional P2 UX](P2-ux-coverage.md#req-0059); [proposed P3 architecture](P3-architecture-coverage.md#req-0059); adoption and implementation pending | pending: authorized implementation | [TEST-0117](#test-0117), [TEST-0118](#test-0118) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0117
- Requirement: REQ-0059; purpose: Document review evidence nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Provide before/after page/field mapping and a local reviewable result summary; require review of uncertain layout/content fidelity.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0118
- Requirement: REQ-0059; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: A signed input is preserved and output explicitly marked as not preserving signature validity when modified; no claim of valid signatures without verification.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0060
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0060 — Maintenance workspace](../governance/01-requirements-book.md#req-0060--maintenance-workspace) | [conditional P2 UX](P2-ux-coverage.md#req-0060); [proposed P3 architecture](P3-architecture-coverage.md#req-0060); adoption and implementation pending | pending: authorized implementation | [TEST-0119](#test-0119), [TEST-0120](#test-0120) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0119
- Requirement: REQ-0060; purpose: Maintenance workspace nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Select a local website workspace and explicit allowed files; display which files are within the authorized job scope.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0120
- Requirement: REQ-0060; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Reject paths escaping that workspace, including traversal and link-based escape; exclude version-control metadata and secrets.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0061
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0061 — Template project generation](../governance/01-requirements-book.md#req-0061--template-project-generation) | [conditional P2 UX](P2-ux-coverage.md#req-0061); [proposed P3 architecture](P3-architecture-coverage.md#req-0061); adoption and implementation pending | pending: authorized implementation | [TEST-0121](#test-0121), [TEST-0122](#test-0122) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0121
- Requirement: REQ-0061; purpose: Template project generation nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Generate a local website from an approved, licensed template with declared placeholders into a new output location.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0122
- Requirement: REQ-0061; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: An occupied destination requires consent or a different location; no remote package fetch or script execution occurs implicitly.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0062
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0062 — Maintenance change plan](../governance/01-requirements-book.md#req-0062--maintenance-change-plan) | [conditional P2 UX](P2-ux-coverage.md#req-0062); [proposed P3 architecture](P3-architecture-coverage.md#req-0062); adoption and implementation pending | pending: authorized implementation | [TEST-0123](#test-0123), [TEST-0124](#test-0124) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0123
- Requirement: REQ-0062; purpose: Maintenance change plan nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Preview proposed content/asset/link/template edits as a file-level change set before applying them to a separate output copy.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0124
- Requirement: REQ-0062; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Unknown files and unexpected source hashes invalidate the plan; no change outside the previewed set is permitted.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0063
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0063 — Content and asset updates](../governance/01-requirements-book.md#req-0063--content-and-asset-updates) | [conditional P2 UX](P2-ux-coverage.md#req-0063); [proposed P3 architecture](P3-architecture-coverage.md#req-0063); adoption and implementation pending | pending: authorized implementation | [TEST-0125](#test-0125), [TEST-0126](#test-0126) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0125
- Requirement: REQ-0063; purpose: Content and asset updates nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Replace only explicitly mapped text/assets in the output copy and report each affected file/location.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0126
- Requirement: REQ-0063; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Missing or ambiguous match blocks the affected edit rather than globally replacing unrelated content.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0064
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0064 — Local link checks](../governance/01-requirements-book.md#req-0064--local-link-checks) | [conditional P2 UX](P2-ux-coverage.md#req-0064); [proposed P3 architecture](P3-architecture-coverage.md#req-0064); adoption and implementation pending | pending: authorized implementation | [TEST-0127](#test-0127), [TEST-0128](#test-0128) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0127
- Requirement: REQ-0064; purpose: Local link checks nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Validate selected relative links and referenced assets within the generated workspace and report unresolved references.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0128
- Requirement: REQ-0064; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: External links are marked not checked unless a separately authorized website QA job is created; local validation remains offline.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0065
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0065 — Backup and rollback](../governance/01-requirements-book.md#req-0065--backup-and-rollback) | [conditional P2 UX](P2-ux-coverage.md#req-0065); [proposed P3 architecture](P3-architecture-coverage.md#req-0065); adoption and implementation pending | pending: authorized implementation | [TEST-0129](#test-0129), [TEST-0130](#test-0130) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0129
- Requirement: REQ-0065; purpose: Backup and rollback nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: If an explicitly approved in-place operation is offered, create and verify a recoverable local backup before writing; offer rollback with a displayed scope.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0130
- Requirement: REQ-0065; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Backup failure prevents modification; rollback with changed destination files requires fresh consent and records partial failure.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0066
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0066 — Change review and packaging](../governance/01-requirements-book.md#req-0066--change-review-and-packaging) | [conditional P2 UX](P2-ux-coverage.md#req-0066); [proposed P3 architecture](P3-architecture-coverage.md#req-0066); adoption and implementation pending | pending: authorized implementation | [TEST-0131](#test-0131), [TEST-0132](#test-0132) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0131
- Requirement: REQ-0066; purpose: Change review and packaging nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Present the final changed-file manifest, validation findings and review state before packaging local website output.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0132
- Requirement: REQ-0066; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Unapproved changed files are excluded from approved delivery; a package cannot imply the website was deployed.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### REQ-0067
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ REQ-0067 — Deployment boundary](../governance/01-requirements-book.md#req-0067--deployment-boundary) | [conditional P2 UX](P2-ux-coverage.md#req-0067); [proposed P3 architecture](P3-architecture-coverage.md#req-0067); adoption and implementation pending | pending: authorized implementation | [TEST-0133](#test-0133), [TEST-0134](#test-0134) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0133
- Requirement: REQ-0067; purpose: Deployment boundary nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Maintenance jobs produce local artifacts only; display that deployment and platform automation are outside this baseline.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0134
- Requirement: REQ-0067; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: A template containing a publishing command or external automation cannot trigger it as part of generation or maintenance.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0001
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0001 — Performance responsiveness](../governance/01-requirements-book.md#nfr-0001--performance-responsiveness) | [conditional P2 UX](P2-ux-coverage.md#nfr-0001); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0001); adoption and implementation pending | pending: authorized implementation | [TEST-0135](#test-0135), [TEST-0136](#test-0136) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0135
- Requirement: NFR-0001; purpose: Performance responsiveness nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Proposed profile WP-1: p95 navigation/validation-feedback response <=500 ms while a local job runs, across 100 interactions; long validation shows progress within 1 s.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0136
- Requirement: NFR-0001; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: On a larger-than-profile workload show processing state, not a frozen interface; measurement must name hardware and dataset.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0002
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0002 — Batch processing budget](../governance/01-requirements-book.md#nfr-0002--batch-processing-budget) | [conditional P2 UX](P2-ux-coverage.md#nfr-0002); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0002); adoption and implementation pending | pending: authorized implementation | [TEST-0137](#test-0137), [TEST-0138](#test-0138) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0137
- Requirement: NFR-0002; purpose: Batch processing budget nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Proposed WP-1 CSV workload: clean/filter/export 100,000 rows x 20 columns <=60 s over 5 runs with cold/warm conditions reported; report median and worst run.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0138
- Requirement: NFR-0002; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Exceeding the budget is a failed target, not suppressed; no measurement exists in P1.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0003
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0003 — Reliability](../governance/01-requirements-book.md#nfr-0003--reliability) | [conditional P2 UX](P2-ux-coverage.md#nfr-0003); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0003); adoption and implementation pending | pending: authorized implementation | [TEST-0139](#test-0139), [TEST-0140](#test-0140) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0139
- Requirement: NFR-0003; purpose: Reliability nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: All injected read/write/parse/permission/network failures in the agreed fault suite produce a non-success disposition with retrievable evidence and zero silently dropped items.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0140
- Requirement: NFR-0003; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Disk-full or evidence failure cannot leave a run marked successful without valid durable evidence.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0004
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0004 — Security input boundaries](../governance/01-requirements-book.md#nfr-0004--security-input-boundaries) | [conditional P2 UX](P2-ux-coverage.md#nfr-0004); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0004); adoption and implementation pending | pending: authorized implementation | [TEST-0141](#test-0141), [TEST-0142](#test-0142) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0141
- Requirement: NFR-0004; purpose: Security input boundaries nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: 100% of traversal/link escape, embedded macro/script and unsafe template fixtures in the approved negative suite are rejected or safely inert.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0142
- Requirement: NFR-0004; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Malformed fixtures cannot execute code or write outside the confirmed workspace.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0005
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0005 — Privacy](../governance/01-requirements-book.md#nfr-0005--privacy) | [conditional P2 UX](P2-ux-coverage.md#nfr-0005); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0005); adoption and implementation pending | pending: authorized implementation | [TEST-0143](#test-0143), [TEST-0144](#test-0144) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0143
- Requirement: NFR-0005; purpose: Privacy nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: During local jobs and diagnostic/report flows, observed outbound connections carrying client content are zero; logs contain zero seeded secret values.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0144
- Requirement: NFR-0005; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Seed a credential and confidential cell in test inputs; check general logs/packages for unintended disclosure.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0006
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0006 — Offline operation](../governance/01-requirements-book.md#nfr-0006--offline-operation) | [conditional P2 UX](P2-ux-coverage.md#nfr-0006); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0006); adoption and implementation pending | pending: authorized implementation | [TEST-0145](#test-0145), [TEST-0146](#test-0146) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0145
- Requirement: NFR-0006; purpose: Offline operation nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: On a clean installed machine with network disabled and no external sign-in, all approved local core/spreadsheet/document/maintenance scenarios complete including review/export.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0146
- Requirement: NFR-0006; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Website live checks report connectivity limitations without disabling local workflows.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0007
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0007 — Usability](../governance/01-requirements-book.md#nfr-0007--usability) | [conditional P2 UX](P2-ux-coverage.md#nfr-0007); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0007); adoption and implementation pending | pending: authorized implementation | [TEST-0147](#test-0147), [TEST-0148](#test-0148) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0147
- Requirement: NFR-0007; purpose: Usability nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Proposed usability target: at least 4 of 5 representative operators complete create/configure/run/review/export scenario without assistance within 10 minutes after a short orientation.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0148
- Requirement: NFR-0007; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Record failures and required assistance; do not invent participant results or generalize from developer-only use.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0008
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0008 — Accessibility](../governance/01-requirements-book.md#nfr-0008--accessibility) | [conditional P2 UX](P2-ux-coverage.md#nfr-0008); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0008); adoption and implementation pending | pending: authorized implementation | [TEST-0149](#test-0149), [TEST-0150](#test-0150) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0149
- Requirement: NFR-0008; purpose: Accessibility nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: All essential desktop workflows are operable by keyboard with visible focus and meaningful control labels; test 100% of essential controls with a Windows screen reader.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0150
- Requirement: NFR-0008; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Focus traps, inaccessible destructive confirmations or unlabeled essential controls fail the gate.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0009
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0009 — Maintainability](../governance/01-requirements-book.md#nfr-0009--maintainability) | [conditional P2 UX](P2-ux-coverage.md#nfr-0009); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0009); adoption and implementation pending | pending: authorized implementation | [TEST-0151](#test-0151), [TEST-0152](#test-0152) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0151
- Requirement: NFR-0009; purpose: Maintainability nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Every production module/public interface has an owner, contract and linked requirement/tests; every scoped change passes the approved review and relevant quality checks.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0152
- Requirement: NFR-0009; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: A public change without updated contract/trace tests is rejected at review.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0010
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0010 — Modularity](../governance/01-requirements-book.md#nfr-0010--modularity) | [conditional P2 UX](P2-ux-coverage.md#nfr-0010); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0010); adoption and implementation pending | pending: authorized implementation | [TEST-0153](#test-0153), [TEST-0154](#test-0154) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0153
- Requirement: NFR-0010; purpose: Modularity nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: A representative new module can be registered through approved extension boundaries without editing unrelated module internals; existing module regression scenarios still pass.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0154
- Requirement: NFR-0010; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Removing/disabling one optional module does not prevent other module workflows from starting.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0011
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0011 — Recoverability](../governance/01-requirements-book.md#nfr-0011--recoverability) | [conditional P2 UX](P2-ux-coverage.md#nfr-0011); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0011); adoption and implementation pending | pending: authorized implementation | [TEST-0155](#test-0155), [TEST-0156](#test-0156) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0155
- Requirement: NFR-0011; purpose: Recoverability nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: In 100% of interruption points in the approved suite, restart identifies the incomplete attempt and offers truthful inspect/resume-or-retry choices with preserved originals.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0156
- Requirement: NFR-0011; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: A crash during output write cannot produce approved-ready state; recovery limitations must be shown.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0012
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0012 — Data integrity](../governance/01-requirements-book.md#nfr-0012--data-integrity) | [conditional P2 UX](P2-ux-coverage.md#nfr-0012); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0012); adoption and implementation pending | pending: authorized implementation | [TEST-0157](#test-0157), [TEST-0158](#test-0158) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0157
- Requirement: NFR-0012; purpose: Data integrity nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: SHA-256 hashes of original input files are identical before/after all ordinary successful, failed, cancelled and interrupted jobs in the integrity suite.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0158
- Requirement: NFR-0012; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Explicitly consented in-place changes are excluded from this ordinary-job comparison and require backup/rollback verification.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0013
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0013 — Resource consumption](../governance/01-requirements-book.md#nfr-0013--resource-consumption) | [conditional P2 UX](P2-ux-coverage.md#nfr-0013); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0013); adoption and implementation pending | pending: authorized implementation | [TEST-0159](#test-0159), [TEST-0160](#test-0160) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0159
- Requirement: NFR-0013; purpose: Resource consumption nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Proposed WP-1: peak application memory <=1 GiB on the CSV budget workload, idle CPU <=2% averaged over 60 s after settling; report processes and measurement method.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0160
- Requirement: NFR-0013; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Exceeding available resources fails gracefully with evidence, not corrupted outputs or silent truncation.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0014
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0014 — Windows compatibility](../governance/01-requirements-book.md#nfr-0014--windows-compatibility) | [conditional P2 UX](P2-ux-coverage.md#nfr-0014); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0014); adoption and implementation pending | pending: authorized implementation | [TEST-0161](#test-0161), [TEST-0162](#test-0162) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0161
- Requirement: NFR-0014; purpose: Windows compatibility nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: All release-critical scenarios and install/upgrade/uninstall checks pass on each owner-approved Windows 10 edition/build/architecture with standard-user job execution.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0162
- Requirement: NFR-0014; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Linux checks or vendor statements alone cannot satisfy this requirement; exact target remains an open decision.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0015
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0015 — Installation](../governance/01-requirements-book.md#nfr-0015--installation) | [conditional P2 UX](P2-ux-coverage.md#nfr-0015); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0015); adoption and implementation pending | pending: authorized implementation | [TEST-0163](#test-0163), [TEST-0164](#test-0164) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0163
- Requirement: NFR-0015; purpose: Installation nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Clean install and launch succeeds using documented free dependencies with no subscription, external sign-in, cloud service or AI runtime; bundled/downloaded prerequisites are disclosed.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0164
- Requirement: NFR-0015; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Disconnected installed operation works; whether offline installation media is required remains a proposal for owner review.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0016
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0016 — Upgrade preservation](../governance/01-requirements-book.md#nfr-0016--upgrade-preservation) | [conditional P2 UX](P2-ux-coverage.md#nfr-0016); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0016); adoption and implementation pending | pending: authorized implementation | [TEST-0165](#test-0165), [TEST-0166](#test-0166) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0165
- Requirement: NFR-0016; purpose: Upgrade preservation nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Supported upgrade scenarios preserve client/project metadata, templates, history and approved outputs with pre/post verification and documented recovery.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0166
- Requirement: NFR-0016; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Interrupted/failed upgrade either restores usable previous state or exposes an explicit recovery procedure; no silent deletion.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0017
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0017 — Testability](../governance/01-requirements-book.md#nfr-0017--testability) | [conditional P2 UX](P2-ux-coverage.md#nfr-0017); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0017); adoption and implementation pending | pending: authorized implementation | [TEST-0167](#test-0167), [TEST-0168](#test-0168) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0167
- Requirement: NFR-0017; purpose: Testability nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Every approved REQ/NFR has defined tests/fixtures, declared environment, actual result and evidence at its implementation/release gate; zero-test runs cannot count as coverage.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0168
- Requirement: NFR-0017; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Unavailable tests are NOT_RUN/BLOCKED with reasons, never PASS.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0018
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0018 — Auditability](../governance/01-requirements-book.md#nfr-0018--auditability) | [conditional P2 UX](P2-ux-coverage.md#nfr-0018); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0018); adoption and implementation pending | pending: authorized implementation | [TEST-0169](#test-0169), [TEST-0170](#test-0170) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0169
- Requirement: NFR-0018; purpose: Auditability nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: 100% of run records and approvals link job/attempt, inputs/configuration, artifact hashes, outcome and reviewer/time; stale hashes invalidate approvals.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0170
- Requirement: NFR-0018; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Missing/tampered evidence is detected as unverifiable; no claim of cryptographic identity or tamper-proof storage is assumed.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0019
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0019 — Determinism](../governance/01-requirements-book.md#nfr-0019--determinism) | [conditional P2 UX](P2-ux-coverage.md#nfr-0019); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0019); adoption and implementation pending | pending: authorized implementation | [TEST-0171](#test-0171), [TEST-0172](#test-0172) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0171
- Requirement: NFR-0019; purpose: Determinism nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: With identical input/configuration/tool versions, 3 repeated deterministic local runs have identical normalized data/content and validation findings; variable timestamps/IDs are documented exclusions.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0172
- Requirement: NFR-0019; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Live website observations are time-dependent and record capture context; do not assert identical live content.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0020
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0020 — Dependency and licensing compliance](../governance/01-requirements-book.md#nfr-0020--dependency-and-licensing-compliance) | [conditional P2 UX](P2-ux-coverage.md#nfr-0020); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0020); adoption and implementation pending | pending: authorized implementation | [TEST-0173](#test-0173), [TEST-0174](#test-0174) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0173
- Requirement: NFR-0020; purpose: Dependency and licensing compliance nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Before adoption, 100% of runtime dependencies have provenance/version/license/obligations and Windows support assessment; all redistribution obligations are met.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0174
- Requirement: NFR-0020; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Unknown/incompatible licenses block selection; proprietary required runtime or paid API fails policy compliance.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0021
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0021 — No runtime AI](../governance/01-requirements-book.md#nfr-0021--no-runtime-ai) | [conditional P2 UX](P2-ux-coverage.md#nfr-0021); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0021); adoption and implementation pending | pending: authorized implementation | [TEST-0175](#test-0175), [TEST-0176](#test-0176) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0175
- Requirement: NFR-0021; purpose: No runtime AI nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: All release-critical workflows pass with AI services unavailable; dependency/source/network review finds zero required runtime AI integrations.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0176
- Requirement: NFR-0021; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: A missing development AI credential cannot prevent installation, launch or job execution.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0022
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0022 — Safe recovery logs](../governance/01-requirements-book.md#nfr-0022--safe-recovery-logs) | [conditional P2 UX](P2-ux-coverage.md#nfr-0022); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0022); adoption and implementation pending | pending: authorized implementation | [TEST-0177](#test-0177), [TEST-0178](#test-0178) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0177
- Requirement: NFR-0022; purpose: Safe recovery logs nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Each failure/cancellation/interruption records safe cause and next action; seeded secrets appear zero times in logs, and configurable retention deletes only consented managed data.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0178
- Requirement: NFR-0022; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Log write failure is surfaced and does not cause unauthorized writes or input deletion.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0023
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0023 — Authorization enforcement](../governance/01-requirements-book.md#nfr-0023--authorization-enforcement) | [conditional P2 UX](P2-ux-coverage.md#nfr-0023); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0023); adoption and implementation pending | pending: authorized implementation | [TEST-0179](#test-0179), [TEST-0180](#test-0180) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0179
- Requirement: NFR-0023; purpose: Authorization enforcement nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: 100% of unauthorized host/path/action/expiry/redirect test cases are blocked before the prohibited request; TLS verification remains enabled.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0180
- Requirement: NFR-0023; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Network-enabled modules cannot bypass authorization through assets, redirects or retries.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

### NFR-0024
| Requirement | Design | Implementation | Test cases | Acceptance evidence | Approval |
| --- | --- | --- | --- | --- | --- |
| [ NFR-0024 — Efficient disk management](../governance/01-requirements-book.md#nfr-0024--efficient-disk-management) | [conditional P2 UX](P2-ux-coverage.md#nfr-0024); [proposed P3 architecture](P3-architecture-coverage.md#nfr-0024); adoption and implementation pending | pending: authorized implementation | [TEST-0181](#test-0181), [TEST-0182](#test-0182) | pending: product test run; [P1 document review only](../milestone-reports/MS-0002-P1.md) | conditional documentation approval only; requirement details pending disposition |

#### TEST-0181
- Requirement: NFR-0024; purpose: Efficient disk management nominal/property acceptance.
- Input/condition: synthetic supported inputs or representative configuration for this requirement; use the positive workload/properties below and shared prerequisites.
- Procedure / expected result: Show planned/estimated output and backup storage before disk-intensive work; storage-shortage suite produces explicit failures without damaging originals; estimates are labeled.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

#### TEST-0182
- Requirement: NFR-0024; purpose: adverse/boundary acceptance.
- Input/condition and procedure / expected result: Cleanup never deletes client originals, unselected exports or unrelated files to regain space.
- Actual result: NOT_RUN; no application exists; run environment/evidence: pending implementation and relevant Windows gate.

## Scenario coverage cross-check
Positive behavior and invalid/adverse boundaries: paired cases for every entry. Parsing/unsupported data: import, module disclosure and format-specific tests. Processing failures: processing/error/reliability tests. Data integrity: preservation and module validation tests. Cancellation: cancellation test pair. Recovery: interruption/retry/rollback tests. Unauthorized operations: target authorization/security/network and deployment boundaries. Human approval: review/consent/delivery approval/hash invalidation tests. Offline: offline gating and offline quality tests. Performance boundaries: responsiveness/batch/resource/storage cases. These labels are coverage claims about defined tests, not execution results.
