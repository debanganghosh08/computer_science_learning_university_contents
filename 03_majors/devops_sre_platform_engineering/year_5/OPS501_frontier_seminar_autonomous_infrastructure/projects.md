# OPS501 · Labs and projects

This seminar's labs are reproductions: each one takes a claim from a paper on the reading list and checks it on a laptop. Projects grow from a specification (P1) to a reproduction (P2) to original research (P3). Everything runs locally: TLC or the P checker, Z3, Batfish in Docker, kind clusters, AIOpsLab environments, and local or capped-budget models. Labs 2 and 3 are done without AI assistance, because writing invariants is the skill being assessed.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Oscillating autoscaler | Simulate an autoscaler with metric lag; show oscillation; fix it with damping or stabilization windows | Simulation, plots, explanation in control terms | 4 h |
| 2 · Deploy-lock spec | Write a TLA+ spec of a deployment lock used by two pipelines; find a two-writer bug with TLC; fix and re-check | Spec, counterexample trace, fixed spec | 5 h |
| 3 · Failover runbook spec | Specify a database failover runbook (promote replica, repoint clients); find a split-brain trace | Spec, trace, revised runbook | 5 h |
| 4 · Policy reasoning with Z3 | Encode a small IAM-like policy language in SMT; answer "can any principal outside the account read this bucket?" | Encoder, 5 queries with results | 4 h |
| 5 · Batfish | Load a sample multi-router network; find an unintended reachability and a routing loop | Batfish notebook, findings | 3 h |
| 6 · Operator testing | Write a toy Kubernetes operator; test it with a Sieve-style perturbation harness (stale reads, crash mid-reconcile) | Operator, harness, bugs found | 6 h |
| 7 · Metastability model | Build a model of a retry-driven system; map stable and metastable regions; show a self-healing restart loop sustaining the failure | Model, phase plot, write-up | 4 h |
| 8 · Benchmark reproduction | Reproduce one published number from AIOpsLab, ITBench or OpenRCA on a subset, with your own cost reporting | Setup, results, discrepancy analysis | 6 h |

## Projects

### P1 · Specify and break an infrastructure protocol (L1, ~6 hours)

**Real-world inspiration:** AWS engineers used TLA+ to find subtle design bugs before shipping ([CACM 2015](https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf)); Azure Cosmos DB publishes [TLA+ specifications](https://github.com/Azure/azure-cosmos-tla) of its consistency levels.

**What to build:** a TLA+ or P specification of one protocol from your own Year 3–4 work: GitOps reconciliation with manual break-glass edits, a canary controller deciding promote or abort, or leader election for a remediation agent.

**Acceptance criteria:**
- **Properties:** at least two safety invariants and one liveness property, stated in plain English and in the specification language.
- **Bug found:** the model checker finds a counterexample in the first version (seeded or real), and the trace is explained step by step.
- **Fix verified:** the corrected specification passes for a stated model size (for example 3 nodes, 2 concurrent changes), and the state-space size is reported.
- **AI check:** an AI-drafted invariant for the same protocol is evaluated, with an explanation of whether it is trivially true or too weak to catch your bug.

**Stretch goals:** a P model whose test traces drive tests of your real implementation.

**What it proves to an employer:** you can find design bugs before they become outages, a skill AWS and others describe as part of normal engineering.

### P2 · Reproduce a result (L2, ~15 hours)

**Real-world inspiration:** [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md)'s reproduction practice applied to infrastructure research.

**What to build:** reproduce one result from the reading list. Suggested options:
- Sieve-style testing of an open-source operator, finding at least one real or planted bug class from the paper;
- the metastable-failure behaviour described in the OSDI 2022 study, in a simulator or on a small cluster;
- a published AIOpsLab, ITBench or OpenRCA result on a subset with a current model;
- an Autopilot-style vertical-scaling recommender evaluated on your own workload traces.

**Acceptance criteria:**
- **Faithfulness:** a table maps every step of your setup to the paper's method, and lists each difference with its likely effect.
- **Result:** you reproduce the paper's qualitative finding, or you show convincingly why you could not.
- **Rigor:** at least 3 independent runs with variance reported; cost (compute, tokens) reported.
- **Artefact:** one command reproduces your results from a clean checkout; a classmate succeeds using only your README.

**Stretch goals:** a small extension (a new workload, a new fault type, a newer model) with results.

**What it proves to an employer:** you can read research critically and turn it into working evidence, which research-engineering and staff roles require.

### P3 · Original research on bounded autonomy (L3, portfolio-grade, ~30 hours or more)

**Real-world inspiration:** the gap between the AgentOps vision ([AIOpsLab](https://arxiv.org/abs/2501.06706)) and measured agent performance ([ITBench](https://arxiv.org/abs/2502.05352): 13.8% of SRE scenarios); verified controllers ([Anvil](https://www.usenix.org/conference/osdi24/presentation/sun-xudong)); real agent incidents in 2025.

**What to build:** a research project with a clear question. Example questions:
- Can model-checking an agent's remediation plan against a specification of the system prevent unsafe actions without blocking useful ones?
- Can a metastability-aware controller detect and break sustaining loops automatically?
- Does a realistic, contamination-resistant RCA benchmark change the ranking of agents?
- Can configuration validators learned from past incidents catch new incidents?

You may build on your [OPS403](../../year_4/OPS403_aiops_and_agentic_operations/README.md) P3 or [OPS402](../../year_4/OPS402_chaos_engineering_and_resilience/README.md) P3.

**Acceptance criteria:**
- **Paper:** a 6-page workshop-format paper (introduction, related work citing at least 10 papers from or beyond the reading list, method, evaluation, threats to validity, conclusion).
- **Evaluation:** results compared with at least one baseline, with confidence intervals or variance across at least 3 runs, and costs reported.
- **Safety and ethics:** any agent with actions runs only in sandboxed environments; the paper includes a safety section.
- **Artefact:** public (or shareable) repository; one-command reproduction; artefact evaluated by a classmate using an artefact-evaluation checklist.
- **Review:** two peer reviews received and answered in a response letter; the defence talk answers questions on limitations.

**Stretch goals:** submit to a workshop or student research competition at a systems or SRE venue; open-source a tool from the project.

**What it proves to an employer:** you can create new knowledge in infrastructure reliability, which sets you apart for research-engineering roles, PhD programmes, or a founder path in operations tooling.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is designed to become a thesis chapter.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): safe operations automation is an active startup area.
- [OV12B Agent Evaluation and Reliability Engineering](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12B_agent_evaluation_and_reliability_engineering/README.md): evaluation methods developed here.
