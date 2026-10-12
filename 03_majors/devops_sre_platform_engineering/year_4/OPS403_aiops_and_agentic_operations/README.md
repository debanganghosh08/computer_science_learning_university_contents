# OPS403 · AIOps and Agentic Operations

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 (P3 touches L5) | [OPS303](../../year_3/OPS303_observability_metrics_logs_traces/README.md); strongly recommended: [OPS304](../../year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md), [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) | [OPS501](../../year_5/OPS501_frontier_seminar_autonomous_infrastructure/README.md), [OV12A](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12A_running_agents_in_production_sandboxes_durable/README.md), [OV12B](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12B_agent_evaluation_and_reliability_engineering/README.md) |

Part of the [DevOps, SRE and Platform Engineering major](../../README.md). This course asks one question all semester: which operations work can machine learning and AI agents do reliably today, under what guardrails, and how do you prove it? You will build anomaly detectors, alert correlators, an investigation agent and a guarded remediation agent, and evaluate each against human baselines and published benchmarks. Building agents in general is taught in [AIE304](../../../ai_engineering/year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md); operating LLM applications in [AIE403](../../../ai_engineering/year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md); network-specific AIOps in [NET403](../../../it_infrastructure_networking/year_4/NET403_aiops_and_intent_based_networking/README.md).

## Why this course matters now

Every major cloud and observability vendor now sells an "AI SRE":

- **Cloud providers:** AWS DevOps Agent ("your always-on, autonomous on-call engineer"), Azure SRE Agent (which "suggests or, when configured, executes mitigations", with a Review mode for approvals) and Gemini Cloud Assist.
- **Observability and incident tools:** Datadog's Bits AI investigations, Grafana Assistant, PagerDuty's AI agents and incident.io's AI SRE.
- **Open source:** HolmesGPT (CNCF sandbox, October 2025) and K8sGPT.

The independent evidence is more sober:

- **ITBench (2025):** agents built on state-of-the-art models "resolve only 13.8% of SRE scenarios, 25.2% of CISO scenarios, and 0% of FinOps scenarios".
- **OpenRCA (ICLR 2025):** across 335 real failures, the best model with a purpose-built agent located the root cause in 11.34% of cases.
- **Practice:** only 20% of developers who use AI use it to deploy, operate or troubleshoot production (Stack Overflow 2026).

Agents with production access have also caused damage. In July 2025, Replit's agent deleted a production database despite an instruction not to make changes. In the same month, an inappropriately scoped token let an attacker commit malicious code that shipped in a release of the Amazon Q Developer extension for VS Code; according to AWS it failed to execute only because of a syntax error. The value is real: summaries, query writing, correlation and first hypotheses save time. The skill that makes you hard to replace is building these systems with evaluation, least privilege and human approval, and telling a measured improvement from a vendor anecdote.

## Learning outcomes

By the end you can:

1. **Map** operations tasks (detect, correlate, triage, diagnose, remediate, prevent) to methods (statistics, classic ML, LLMs, agents) and to levels of autonomy, and **justify** each mapping with evidence.
2. **Build and evaluate** metric anomaly detectors (seasonal baselines, robust statistics, forecasting, isolation forests), and **avoid** the benchmark flaws documented by Wu and Keogh.
3. **Parse and mine** logs (Drain-style template mining, embeddings) and **detect** log anomalies on Loghub data.
4. **Reduce** alert noise with deduplication, topology- and change-aware correlation, and **measure** noise reduction against missed incidents.
5. **Build** a read-only LLM investigation agent that queries metrics, logs, traces and Kubernetes through tools (including MCP servers), and **ground** every claim in a query result.
6. **Convert** runbooks into safe, idempotent actions with pre- and post-conditions, and **add** agentic remediation behind approvals.
7. **Design** guardrails: scoped identities, policy checks on actions, blast-radius and rate limits, kill switches, audit trails, and defences against prompt injection through logs and tickets.
8. **Evaluate** AIOps systems offline (AIOpsLab, ITBench, OpenRCA, your own fault-injection suites) and online (shadow mode), with accuracy, time, cost and safety metrics, and **dissect** vendor claims.
9. **Explain** the human factors (automation irony, skill fade, trust calibration, accountability) and **design** on-call practice that keeps humans capable.

## Chapters and lessons

### Chapter 1 · The AIOps landscape, honestly (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Tasks and methods | Detection, correlation, triage, root-cause analysis, remediation, prevention; which need ML, which need LLMs, which need neither | Classify 30 product feature claims by task and method |
| 1.2 Levels of autonomy | Suggest → act with approval → act autonomously within a bounded scope; who is accountable at each level | Place 6 products on the scale using their documentation |
| 1.3 Evidence vs anecdote | Benchmarks (ITBench, OpenRCA), studies (Microsoft's 40,000-incident study, ICSE 2023), vendor case studies | Rate 5 claims by evidence quality |
| 1.4 Where operations data lives | Telemetry, topology (service catalog), changes (deploys, flags, config), tickets, chat, post-mortems | Inventory the data sources of your OPS303 stack |

**Check your understanding:** (1) Why are change events often the strongest signal for diagnosis? (2) What does "13.8% of SRE scenarios" tell you about full autonomy today? (3) Which task in 1.1 is safest to automate first, and why?

### Chapter 2 · Data foundations (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Telemetry quality | Missing data, inconsistent labels, clock skew; garbage in, confident garbage out | Measure label consistency across 10 services |
| 2.2 Topology and change data | Dependency graphs from traces and the catalog; change events from CI/CD and GitOps | Build a dependency graph from traces; join deploy events |
| 2.3 Data sets | Loghub, the Numenta Anomaly Benchmark, OpenRCA, AIOpsLab problems; licences and limits | Load two data sets; document their labels |
| 2.4 Fault-injection data | Generating labelled incidents with OPS402 experiments and the OpenTelemetry Demo flags | Generate 20 labelled incidents |

**Check your understanding:** (1) Why is your own fault-injection data more useful than a public benchmark for your system? (2) What is lost when labels are inconsistent? (3) Which data source would an LLM investigation need that metrics cannot give?

### Chapter 3 · Anomaly detection on metrics (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Baselines | Static thresholds, rolling z-scores, median absolute deviation, seasonal decomposition (STL), Holt-Winters | Implement 3 detectors on a seasonal series |
| 3.2 Forecasting and ML | Forecast residuals (Prophet-style), isolation forest; Microsoft's Spectral Residual + CNN service (KDD 2019) | Compare a forecast-residual detector with an isolation forest |
| 3.3 Evaluation | Point vs range-based precision/recall, detection delay, alert cost; Wu and Keogh's critique of flawed benchmarks | Re-evaluate a "state of the art" result with a one-line baseline |
| 3.4 From anomaly to page | Anomalies are not incidents; tie detection to SLO burn | Show how many anomalies a week would page without SLO gating |

**Check your understanding:** (1) Why can a trivial detector match a deep model on a flawed benchmark? (2) What is the cost of a false positive at 3 a.m. compared with a missed anomaly in a dashboard? (3) Why should anomaly detection feed tickets more often than pages?

### Chapter 4 · Logs and events (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Log parsing | Template mining with Drain (ICWS 2017); variable extraction; parsing accuracy on Loghub | Parse 100,000 lines; measure grouping accuracy |
| 4.2 Log anomaly detection | Sequence models (DeepLog, CCS 2017), counts per template, new-template alerts | Detect a planted failure from template frequencies |
| 4.3 LLMs on logs | Summarisation, clustering by embeddings, LLM-based parsing; context limits and cost | Compare Drain with an LLM parser on cost and accuracy |
| 4.4 Privacy | PII in logs sent to model providers; redaction before inference; data-location rules | Add redaction to the pipeline and prove it |

**Check your understanding:** (1) Why do new log templates often signal new failure modes? (2) When is an LLM parser worth its cost? (3) What must never be sent to an external model?

### Chapter 5 · Alert correlation and noise reduction (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Deduplication and grouping | Time windows, label similarity, fingerprints | Group a day of 2,000 alerts into incidents |
| 5.2 Topology-aware correlation | Dependency graphs, upstream suppression, common-cause detection | Suppress downstream alerts during a database fault |
| 5.3 Change correlation | Ranking recent deploys, flags and config pushes by time and blast radius | Rank suspects for 10 incidents; score against ground truth |
| 5.4 Causal caution | Granger tests and causal discovery: what they can and cannot claim | Find a spurious "cause" in correlated metrics |
| 5.5 Measuring | Noise reduction %, incidents merged wrongly, incidents missed | Report all three for your correlator |

**Check your understanding:** (1) Why is "90% noise reduction" meaningless without a missed-incident rate? (2) What makes correlation look like causation in telemetry? (3) Why rank changes before anything else?

### Chapter 6 · LLMs in incident response (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 What works today | Timeline drafting, summarising channels, writing queries, finding similar past incidents | Measure time saved on 5 simulated incidents |
| 6.2 Retrieval over runbooks and post-mortems | RAG over your incident history; freshness; citation of sources | Build retrieval over 50 post-mortems; test on new incidents |
| 6.3 What the research shows | Microsoft's study of 40,000+ incidents (ICSE 2023); RCACopilot (EuroSys 2024); OpenRCA | Summarise each paper's method and limits in 300 words |
| 6.4 Failure modes | Hallucinated causes, anchoring on the first alert, overconfidence with missing data, stale runbooks | Build a test set of 10 traps; record the model's behaviour |

**Check your understanding:** (1) Why must an AI hypothesis cite the query that supports it? (2) What makes past incidents misleading for retrieval? (3) Which failure mode is most dangerous during an incident, and why?

### Chapter 7 · Building an investigation agent (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Architecture | A model, tools (PromQL, LogQL, TraceQL, `kubectl get/describe/logs`), memory, a stop condition | Design the agent and its tool schemas |
| 7.2 MCP for operations | MCP servers for Grafana and Kubernetes; read-only tool scopes | Connect an assistant to `mcp-grafana` and a Kubernetes MCP server with read-only RBAC |
| 7.3 Open-source agents | HolmesGPT (CNCF sandbox), K8sGPT (CNCF sandbox): design and limits | Run both on the same 5 faults; compare |
| 7.4 Context engineering | Summarising telemetry to fit context, sampling, tool output limits | Cut tokens per investigation by 50% without losing accuracy |
| 7.5 Cost and latency | Tokens, tool calls and wall-clock time per investigation; local vs hosted models | Report cost per investigation for two model choices |

**Check your understanding:** (1) Why start read-only? (2) What should stop an investigation agent? (3) How do you prove the agent cannot write, rather than trusting its prompt?

### Chapter 8 · Runbook automation and remediation (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 From runbook to action | Executable runbooks; an action catalogue (restart, scale, roll back, flag off, drain) | Turn 5 runbooks into scripted actions |
| 8.2 Safe actions | Preconditions, postconditions, idempotency, dry run, timeouts, rollback of the action itself | Add pre/postconditions and a dry run to each action |
| 8.3 Agentic remediation with approval | Agent proposes, human approves in chat, system executes and verifies; Azure SRE Agent's Review mode as a reference design | Build propose → approve → execute → verify |
| 8.4 When to allow autonomy | Narrow, reversible, frequent, well-tested actions only; error-budget conditions | Write an autonomy policy for your action catalogue |

**Check your understanding:** (1) Why must each action verify its own effect? (2) Which actions must never be autonomous? (3) What evidence would justify moving an action from "approve" to "autonomous"?

### Chapter 9 · Guardrails and security (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Identity and permission | Dedicated agent identities, least privilege, short-lived credentials, separate dev and prod | Prove the agent's identity cannot read prod secrets |
| 9.2 Policy on actions | OPA or Kyverno evaluating proposed actions; blast-radius limits; rate limits on actions; kill switch | Block a "delete namespace" action by policy |
| 9.3 Prompt injection through operations data | Instructions hidden in log lines, ticket text or commit messages; OWASP Top 10 for LLM Applications and for Agentic Applications | Plant an injection in a log line; show your defences hold |
| 9.4 Real incidents | Replit production database deletion (July 2025); Amazon Q extension compromise (AWS-2025-015) | Write the guardrails that would have stopped each |
| 9.5 Audit | Every tool call, input, output and approval logged immutably | Reconstruct an agent's session from its audit log |

**Check your understanding:** (1) Why is a log line untrusted input to an agent? (2) What is the difference between a guardrail in the prompt and one in the platform? (3) What would you show an auditor about your agent?

### Chapter 10 · Evaluating AIOps (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Benchmarks | AIOpsLab (fault injection on microservices), ITBench (94 scenarios), OpenRCA (335 failures); what each measures | Run your agent on a subset of AIOpsLab problems |
| 10.2 Your own evaluation suite | Labelled fault injections, adversarial cases, human baselines on the same scenarios | Build a 20-scenario suite with ground truth |
| 10.3 Metrics | Top-k diagnosis accuracy, time to correct hypothesis, false action rate, cost per incident, unsafe-action count | Compute all five for your agent and for a human |
| 10.4 Shadow mode | Running alongside on-call without acting; comparing proposals with what humans did | Run one week of shadow mode on simulated incidents |
| 10.5 Reading vendor claims | Baselines that are estimates, single-customer anecdotes, missing failure rates; for example a published case reporting "an estimated two hours" reduced to 28 minutes | Rewrite a vendor claim as a testable hypothesis |

**Check your understanding:** (1) Why is an estimated baseline weak evidence? (2) Why must an evaluation include adversarial cases? (3) What would convince you to give an agent more autonomy?

### Chapter 11 · Operating the AI systems themselves (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Observability for agents | Tracing tool calls and model calls (OpenTelemetry generative-AI conventions), cost and latency per session | Trace an investigation end to end |
| 11.2 Evals in CI | Regression suites for prompts, tools and model upgrades | Block a model upgrade that lowers top-3 accuracy |
| 11.3 Model and provider risk | Version pinning, deprecations, provider outages, fallback models (from OPS402) | Survive a provider outage in shadow mode |
| 11.4 Data governance for operations AI | Which telemetry, tickets and chat may go to which model; retention of prompts and outputs; DPDP Act duties for personal data | Write and enforce a data-handling policy for your investigation agent |

**Check your understanding:** (1) Why must a model upgrade go through the same gates as a code change? (2) What do you alert on for an investigation agent? (3) What happens to your on-call process if the agent's provider is down?

### Chapter 12 · Humans, skills and the future of on-call (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Ironies of automation | Bainbridge (1983): automation removes practice and leaves humans the hardest cases | Design an AI-off drill rotation for an on-call team |
| 12.2 Trust calibration | Over-trust and under-trust; showing confidence and evidence | Redesign an agent's output to show evidence and uncertainty |
| 12.3 Accountability | Who owns an action an agent proposed and a human approved; post-mortems for agent actions | Write a post-mortem for an agent-caused incident |
| 12.4 Capstone | Integration of the guarded remediation system | P3 evaluation and demo |

**Check your understanding:** (1) Why does more automation make the remaining incidents harder? (2) What should an agent's answer look like so that a tired human can check it? (3) How should a blameless post-mortem treat an agent's mistake?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Claim classification | Evidence ratings |
| 2 | 2 | Lab 1 · Labelled incident generation | 20 labelled incidents |
| 3 | 3 | Lab 2 · Anomaly detectors | P1 starts |
| 4 | 4 | Lab 3 · Log parsing on Loghub | **P1 due** |
| 5 | 5 | Lab 4 · Alert correlation | Noise and miss rates |
| 6 | 6 | Lab 5 · Retrieval over post-mortems | P2 starts |
| 7 | 7 | Lab 6 · Read-only agent with MCP | Mid-term (AI-off part) |
| 8 | 8 | Lab 7 · Executable runbooks | Action catalogue |
| 9 | 9 | Lab 8 · Injection red-team | **P2 due** |
| 10 | 10 | Lab 9 · AIOpsLab evaluation | Benchmark results |
| 11 | 11 | Lab 10 · Agent tracing and evals in CI | Eval pipeline; P3 design review |
| 12 | 12 | Shadow-mode week | Shadow report |
| 13 | 12 | P3 evaluation runs | — |
| 14 | 12 | P3 demo | **P3 due** |
| 15 | Review | Exam and oral | Final |

## Working with AI in this course

In this course AI is the subject as well as the tool, so the rules are stricter.

- **Use AI for:** building the agents themselves; drafting tool schemas, evaluation harnesses and summaries; pair-programming the detectors. Named tools: Claude, GPT and Gemini model APIs or local open-weight models via Ollama or vLLM; Claude Code, GitHub Copilot; MCP servers for Grafana and Kubernetes; HolmesGPT and K8sGPT.
- **Do without AI (drills):** the mid-term's diagnosis section (you diagnose from telemetry yourself), writing ground-truth labels for evaluation sets, the guardrail design for P3, and one incident per week in the shadow-mode period handled without the agent.
- **Verify AI output by:** requiring every agent claim to cite a query and its result, then re-running the query; scoring against ground truth, not plausibility; negative tests that prove permissions (attempt a write and confirm it fails); adversarial suites; comparing cost and time with a human baseline on the same scenarios.
- **Where AI still fails here (show it):** your evaluation suite is the evidence. Expect wrong root causes stated confidently, anchoring on the first alert, tool loops, ignoring missing data, and obeying instructions planted in logs. Report your own failure rates, not a vendor's.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (written plus AI-off diagnosis) | 10% |
| Final exam (evaluation design and guardrail review) + oral | 20% |

**Mastery gate.** You pass when you can: (1) present an evaluation of your investigation agent on at least 20 labelled scenarios, with top-1 and top-3 accuracy, cost, time and a human baseline, plus an honest list of failure modes; (2) show that your remediation system executed zero unsafe actions across an adversarial suite that includes prompt injection through logs and tickets; (3) take a vendor's AIOps claim you have not seen and, in 30 minutes, write the experiment that would test it on your own systems.

## Industry reality

Operations is the area of software work where AI is used least so far (20% of AI users, against 67% for generating code, in the Stack Overflow 2026 survey), and where mistakes cost most ([market map](../../../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md)). That is changing fast, as every cloud provider now ships an operations agent. Teams adopting them need engineers who can integrate them with telemetry and runbooks, limit their permissions, evaluate them and stay accountable. Microsoft Research's AIOpsLab and IBM's ITBench are open benchmarks you can run on a laptop-sized cluster.

**Interview questions from this course**

1. *Would you let an AI agent restart production services automatically?* Strong answer: depends on the action and evidence; start read-only, then propose-with-approval; autonomy only for narrow, reversible, well-tested actions with pre/postconditions, blast-radius and rate limits, a kill switch and audit; error-budget conditions; cites a real agent incident.
2. *How would you evaluate an AIOps product before buying it?* Strong answer: define tasks and metrics; build a labelled fault-injection suite from your own systems; shadow mode; measure accuracy, time to correct hypothesis, false actions, cost; human baseline; adversarial tests; do not accept estimated baselines or single anecdotes.
3. *Design alert correlation for 2,000 alerts a day.* Strong answer: deduplication, grouping by time and topology, upstream suppression using the dependency graph, change correlation, measuring noise reduction and missed incidents, feedback from responders, and gradual rollout.
4. *How can logs be used to attack an AI agent?* Strong answer: indirect prompt injection via attacker-controlled log fields, ticket text or commit messages; defences outside the model (least privilege, action policies, approvals, separating data from instructions, output validation, audit); test with planted injections.
5. *An AI summary of an incident says the database caused it. How do you check?* Strong answer: ask for the evidence; re-run its queries; check timing (did database symptoms precede user impact?); check changes; look for missing data; compare with traces; treat it as a hypothesis.

## Resources (free first)

- **Benchmarks and papers:** [ITBench](https://arxiv.org/abs/2502.05352) ([code](https://github.com/itbench-hub/ITBench)); [AIOpsLab](https://arxiv.org/abs/2501.06706) ([code](https://github.com/microsoft/AIOpsLab)); [Building AI Agents for Autonomous Clouds](https://arxiv.org/abs/2407.12165); [OpenRCA (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/d29b8d53678015079e1d245c023e49d2-Paper-Conference.pdf) ([code](https://github.com/microsoft/OpenRCA)); [Recommending Root-Cause and Mitigation Steps for Cloud Incidents using LLMs](https://arxiv.org/abs/2301.03797) (ICSE 2023); [RCACopilot](https://arxiv.org/abs/2305.15778); [Time-Series Anomaly Detection Service at Microsoft](https://arxiv.org/abs/1906.03821) (KDD 2019); Wu and Keogh, [Current Time Series Anomaly Detection Benchmarks are Flawed](https://arxiv.org/abs/2009.13807); [Loghub](https://arxiv.org/abs/2008.06448) ([data](https://github.com/logpai/loghub)); [Drain](https://jiemingzhu.github.io/pub/pjhe_icws2017.pdf) (ICWS 2017); [DeepLog](https://www.cs.utah.edu/~lifeifei/papers/deeplog.pdf) (CCS 2017); Lisanne Bainbridge, "Ironies of Automation", *Automatica* 19(6), 1983.
- **Data sets:** [Numenta Anomaly Benchmark](https://github.com/numenta/NAB), Loghub, AIOpsLab problems, your own OPS402 experiments.
- **Tools:** [HolmesGPT](https://github.com/HolmesGPT/holmesgpt), [K8sGPT](https://github.com/k8sgpt-ai/k8sgpt), [mcp-grafana](https://github.com/grafana/mcp-grafana), [Kubernetes MCP server](https://github.com/containers/kubernetes-mcp-server), [AWS MCP servers](https://github.com/awslabs/mcp).
- **Product documentation (read critically):** [AWS DevOps Agent](https://aws.amazon.com/devops-agent/), [Azure SRE Agent](https://learn.microsoft.com/en-us/azure/sre-agent/overview), [Grafana Assistant](https://grafana.com/docs/grafana-cloud/machine-learning/assistant/), [Datadog Bits AI investigations](https://www.datadoghq.com/product/ai/bits-ai-sre/), [PagerDuty AIOps](https://www.pagerduty.com/platform/aiops/), [incident.io AI SRE](https://incident.io/ai-sre).
- **Security:** [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) and [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/).
- **Practice locally:** AIOpsLab and the OpenTelemetry Demo on kind; local models with Ollama keep costs at zero and data on your machine.

## Sources

All checked 12 Oct 2026.
- Jha et al., [ITBench](https://arxiv.org/abs/2502.05352) (2025): 94 scenarios; 13.8% SRE, 25.2% CISO, 0% FinOps resolved.
- Xu et al., [OpenRCA](https://proceedings.iclr.cc/paper_files/paper/2025/file/d29b8d53678015079e1d245c023e49d2-Paper-Conference.pdf) (ICLR 2025): 335 failures; best configuration 11.34%.
- Chen et al., [AIOpsLab](https://arxiv.org/abs/2501.06706) (2025); Ahmed et al., [ICSE 2023 study](https://arxiv.org/abs/2301.03797) (more than 40,000 incidents at Microsoft).
- AWS, [DevOps Agent product page](https://aws.amazon.com/devops-agent/) (including the WGU case: "an estimated two hours to just 28 minutes"); Microsoft, [Azure SRE Agent overview](https://learn.microsoft.com/en-us/azure/sre-agent/overview) (Review mode approvals).
- CNCF maturity (HolmesGPT sandbox 8 Oct 2025; K8sGPT sandbox 19 Dec 2023) from the [CNCF landscape](https://github.com/cncf/landscape) data file.
- heise online, [Replit deletes production database](https://heise.de/-10499597) (Jul 2025); AWS, [security bulletin AWS-2025-015](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/) (Jul 2025).
- Stack Overflow, [2026 survey results](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/) (20% vs 67%), via this repository's market map.

_Last reviewed: 2026-10_
