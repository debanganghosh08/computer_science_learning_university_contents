# OPS403 · Labs and projects

The lab environment is a kind cluster with the OpenTelemetry Demo (or AIOpsLab's microservice environments), the observability stack from [OPS303](../../year_3/OPS303_observability_metrics_logs_traces/README.md), and fault injection from [OPS402](../OPS402_chaos_engineering_and_resilience/README.md). For models, use a local open-weight model through Ollama or vLLM where possible, and a hosted API with a hard monthly spending cap (for example ₹1,000 or $10) where you need a stronger model. Never send real company data, secrets or personal data to any model. Labs 1 and 8 are done without AI coding assistance (you may still call models as the system under test).

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Labelled incident generation | Generate 20 incidents with known root causes using demo feature flags and Chaos Mesh; record ground truth | Incident manifest with cause, start/end times and affected services | 4 h |
| 2 · Anomaly detectors | Implement rolling z-score, STL residual and isolation forest detectors; evaluate on NAB and your own data with range-based metrics and a trivial baseline | Code, evaluation table, one-page critique | 5 h |
| 3 · Log parsing on Loghub | Implement or run Drain; measure grouping accuracy; detect a planted failure from template counts | Parser output, accuracy, detection evidence | 4 h |
| 4 · Alert correlation | Group 2,000 alerts using time, labels, topology and change events; measure noise reduction and misses | Correlator, metrics report | 5 h |
| 5 · Retrieval over post-mortems | Retrieval over 50 post-mortems (public and your own); test on 10 new incidents | Retrieval quality table, examples of good and misleading matches | 4 h |
| 6 · Read-only agent with MCP | An investigation agent using Grafana and Kubernetes MCP servers with read-only RBAC; test write attempts | Agent code, RBAC manifests, negative-test log | 6 h |
| 7 · Executable runbooks | Turn 5 runbooks into actions with pre/postconditions, dry run and self-verification | Action catalogue, dry-run outputs | 4 h |
| 8 · Injection red-team | Plant prompt injections in log lines, ticket text and a commit message; attack a classmate's agent; defend yours | Attack cases, outcomes, fixes | 4 h |
| 9 · AIOpsLab evaluation | Run your agent on a subset of AIOpsLab problems; compare with a baseline agent | Results with failure analysis | 5 h |
| 10 · Agent tracing and evals in CI | Trace every model and tool call; add a regression eval that blocks a worse model or prompt | Traces, CI run that fails on regression | 4 h |

## Projects

### P1 · Anomaly detection, honestly evaluated (L1, ~6 hours)

**Real-world inspiration:** Microsoft's production anomaly-detection service ([KDD 2019](https://arxiv.org/abs/1906.03821)) and Wu and Keogh's warning that popular benchmarks "are flawed and are creating the illusion of progress" ([arXiv](https://arxiv.org/abs/2009.13807)).

**What to build:** three detectors applied to (a) the Numenta Anomaly Benchmark and (b) two weeks of your own Prometheus metrics with injected faults, plus an evaluation report.

**Acceptance criteria:**
- **Metrics:** precision, recall and detection delay with range-based scoring, reported for each detector and each data set.
- **Baseline:** a trivial baseline (for example a one-line threshold on differences) is included, and you state honestly whether your detectors beat it.
- **Operational cost:** the expected false pages per week at your chosen threshold are computed, and a threshold is chosen for "ticket" vs "page".
- **Reproducibility:** one command reproduces every number; seeds fixed.

**Stretch goals:** gate anomalies on SLO burn and show how many pages disappear.

**What it proves to an employer:** you can evaluate an ML claim in operations without fooling yourself, which few people can.

### P2 · A read-only incident investigation agent (L2, ~15 hours)

**Real-world inspiration:** open-source SRE agents such as [HolmesGPT](https://github.com/HolmesGPT/holmesgpt) and [K8sGPT](https://github.com/k8sgpt-ai/k8sgpt), and Microsoft's [RCACopilot](https://arxiv.org/abs/2305.15778).

**What to build:** an agent that, given an alert, investigates with read-only tools (PromQL, LogQL or ClickHouse SQL, TraceQL, Kubernetes get/describe/logs, recent deploys and flag changes) and returns a ranked list of hypotheses, each with the queries and results that support it.

**Acceptance criteria:**
- **Accuracy:** on 10 labelled faults from Lab 1 that it has not seen during development, the correct service is ranked first in at least 6 and in the top 3 in at least 8.
- **Speed and cost:** median investigation under 3 minutes; median cost under ₹40 (about $0.50) per investigation with a hosted model, or zero with a local model, reported with token counts.
- **Grounding:** 100% of stated causes cite at least one query whose result supports them; a reviewer re-runs 10 citations and they reproduce.
- **Read-only proof:** a negative test suite (create, delete, scale, exec) fails 100% at the RBAC layer, not because of the prompt.
- **Baseline:** a classmate investigates the same 10 faults with dashboards only; you report both times and accuracies.

**Stretch goals:** retrieval over past post-mortems; an "I don't know" answer when evidence is insufficient, with its rate measured.

**What it proves to an employer:** you can build useful AI tooling for on-call and prove how good it is, with safety by construction.

### P3 · A guarded remediation agent with an evaluation harness (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Azure SRE Agent's Review mode, in which an administrator approves actions ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/sre-agent/overview)); ITBench's finding that agents resolved 13.8% of SRE scenarios ([arXiv](https://arxiv.org/abs/2502.05352)); the July 2025 Replit and Amazon Q incidents ([heise](https://heise.de/-10499597), [AWS-2025-015](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/)).

**What to build:** extend P2 into a system that can act, safely:
- an action catalogue of 6 actions (restart a deployment, scale, roll back, turn off a feature flag, drain a node, pause a GitOps sync), each with preconditions, postconditions, dry run and self-verification;
- propose → approve in chat → execute → verify, with an autonomy policy that allows at most one narrow action without approval;
- a policy engine (OPA or Kyverno) checking each action, blast-radius and rate limits, a kill switch, and an immutable audit log;
- an evaluation harness of at least 20 scenarios: 15 labelled faults and 5 adversarial cases (prompt injection in logs and tickets, misleading alerts, a scenario where the right answer is "do nothing");
- a one-week shadow mode before any action is enabled.

**Acceptance criteria:**
- **Safety:** zero unsafe actions executed across the adversarial suite, and zero actions outside the catalogue ever executed (proven by the audit log and by policy-denial logs).
- **Effectiveness:** on the 15 labelled faults, time to mitigation with the agent plus human approval is at least 30% lower than the human-only baseline measured on the same scenarios.
- **Precision of action:** the false action rate (proposed actions that were wrong or unnecessary) is at most 10% of proposals, and every wrong proposal is analysed.
- **Kill switch:** disabling the agent takes under 10 seconds and stops in-flight actions safely (tested).
- **Audit:** a reviewer reconstructs any session (inputs, tool calls, model outputs, approvals, effects) from the log alone.
- **Report:** a paper-style write-up with method, results with confidence intervals, failure analysis and a recommendation on which actions (if any) deserve autonomy.

**Stretch goals:** run the same harness on AIOpsLab problems and compare with published results; test two different models and a local model, reporting the cost and accuracy trade-off.

**What it proves to an employer:** you can bring AI agents into production operations the way a careful company would, which is one of the newest and scarcest skills in the field.

## Feeds into

- [OPS501 Frontier Seminar](../../year_5/OPS501_frontier_seminar_autonomous_infrastructure/README.md): P3 is the starting point for research on bounded autonomy.
- [OV12A Running Agents in Production](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12A_running_agents_in_production_sandboxes_durable/README.md) and [OV12B Agent Evaluation and Reliability Engineering](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12B_agent_evaluation_and_reliability_engineering/README.md).
- [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): AIOps benchmarks are ready-made reproduction targets.
- [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): an evaluated, safe operations agent is a credible product seed.
