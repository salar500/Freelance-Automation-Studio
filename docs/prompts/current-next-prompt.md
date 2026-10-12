# P5 portable core — bounded workload/resource verification

ROLE: Python performance/reliability engineer and QA architect.
PROJECT: Freelance Automation Studio.
MODE: Bounded prototype implementation/measurement only after explicit owner approval of this follow-up. Do not execute automatically or beginP6.

CONTEXT: Existing experiments/p5_portable_core standard-library CLI uses hostPython3.12.14/Linux/sqlite3.53.1;50tests passed(29original+21crash-consistency). Schema2journals paths,reconciles/quarantines partial/missing/tampered outputs,terminal eligibility/outcome commit atomically,and real subprocess crash recovery is idempotent. P5BLOCKED,B02/B04OPEN,B03RESOLVED;productionADRsPROPOSED. No Windows inventory is a prerequisite for this bounded cloud experiment.

CHECKPOINT: Read AGENTS/master/development/testing/security/execution books,current prompt,P5report/matrix/decisionpackage,prototypeREADME/source/tests. Verify feature/p5-portable-core at the controlled implementation checkpoint:commit title feat: add P5 portable processing core and crash recovery,parent15acfb58dfa9f9616b60b2c41c771953cbfc878c,and localHEAD matching origin branch;inspect actual SHA/status rather than assuming a hash;inspect actual Git status and preserve every unrelated doc/source;checkpoint task did not authorize this workload execution. Run existing focused suite once before changes. Never discard earlier tests/evidence.

OBJECTIVE: Measure synthetic bounded1000/10000record workloads for duplicate handling,SQLite progress costs,cancellation and recovery;record hardware/environment/time/output sizes/memory measurement method/limitations. Use standardlibrary time/tracemalloc/resource where available,not assumed Windows metrics. Stop on unacceptable resource use;do not extrapolate to100k/Windows/released-app performance without evidence. Preserve deterministic output/original hashes.

SCOPE: Add reproducible synthetic workload harness/test fixtures outside runtime client data;implement only measured small optimizations if actual bottlenecks justify them,keeping durable crash/cancel semantics. Consider bounded progress batching only if tests establish loss-of-progress versus loss-of-output semantics explicitly. Do not prematurely add async frameworks/microservices/newdependencies/UI/installer/othermodules/production33entityschema.

DELIVERABLES: Existing portable source/tests/README and relevant P5 docs only;actual commands/dataset/environment/measurement table/artifact checksums/limits. Preserve50existing tests;add meaningful tests for changed behavior. No silent numericNFRapproval;reported measurements are not performance promises.

VERIFY: Changed tests first,then fullportable suite once afterchanges;CLI/data-integrity/crash/cancel/recovery regressions as justified. Docslinks/IDs/status/protectedhashes/Gitdiff scope.239original product acceptance cases remainNOT_RUN unless complete procedures genuinely executed;prototype execution separate. No WindowsGUI/native/installer/security/physicalpowerloss claims fromLinux.

RESTRICTIONS: No downloads/installations/Qt/.NET/runtimeartifactexecution/realclientdata/externalAPI/AIruntime,productionADRapproval,Gitstage/commit/push/merge/reset/clean,deployment orP6. ExistingPythonstdlib prototype execution authorized only by owner approval of this task. Cleanup owned disposable data only;retain failure evidence.

ACCEPTANCE: Reproducible actual measurements,verified output/original integrity,cancel/recovery correctness,no unexplained regressions. Missing measurements/errors recorded honestly;P5overallBLOCKED untilremainingnative/distribution prerequisites genuinely met.

FINAL: Baseline/files;actual executable/workload commands;measurement method/results;tests/counts;integrity/cancel/recovery evidence;limits;Git/blocker/ADR states;exactlyONE nextrecommendedaction. SaveONE complete approval-gated nextprompt;do not execute it. Stop for ownerreview.
