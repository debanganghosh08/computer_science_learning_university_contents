# OV04 · MLOps and ML Platform Engineering

| Composed of | Overlap courses | When | Typical entry majors | Market pages |
|---|---|---|---|---|
| [MLE401](../../03_majors/machine_learning_engineering/year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md) · [OPS401](../../03_majors/devops_sre_platform_engineering/year_4/OPS401_platform_engineering_and_internal_developer/README.md) · [CLD404](../../03_majors/cloud_engineering/year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md) | [OV04A](OV04A_ml_platform_engineering/README.md) · [OV04B](OV04B_llmops_at_scale/README.md) | Year 4 (semesters 7–8), or semesters 8–9 on the stretched plan | Machine Learning Engineering, DevOps/SRE, Cloud Engineering, AI Engineering, Deep Learning | [MLE](../../06_career_and_market_readiness/01_market_map/roles/MLE_machine_learning_engineering.md) · [OPS](../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md) · [CLD](../../06_career_and_market_readiness/01_market_map/roles/CLD_cloud_engineering.md) · [AIE](../../06_career_and_market_readiness/01_market_map/roles/AIE_ai_engineering.md) |

## The job this overlap maps to

An **ML platform engineer** builds and runs the shared system that lets many teams train, evaluate, deploy and monitor models without each team rebuilding GPU clusters, pipelines and serving stacks. Since 2023 the same teams also run **LLMOps at scale**: the gateway every product calls models through, self-hosted inference fleets, evaluation services, fine-tuning pipelines, and the cost and safety controls around them.

Titles: ML Platform Engineer, MLOps Engineer, ML Infrastructure Engineer, AI Platform Engineer, LLMOps Engineer, Inference Platform Engineer. The work, concretely:

- Run GPU capacity on Kubernetes with fair-share queues and quotas.
- Provide notebooks, training jobs, pipelines, a feature store, experiment tracking and a model registry as self-service products.
- Provide a model-serving golden path with autoscaling, canaries and SLOs.
- Run an LLM gateway with routing, budgets, logging and redaction for dozens of teams.
- Operate self-hosted LLM inference (vLLM, SGLang, KServe, llm-d) next to model APIs.
- Attribute every GPU-hour and every token to a team and a product.

Uber's Michelangelo is a well-documented example of this role's output: a single platform that grew from predictive models to generative AI ([Uber, May 2024](https://www.uber.com/blog/from-predictive-to-generative-ai/)), and Uber's GenAI Gateway serves model access for close to 30 teams through one OpenAI-compatible interface ([Uber, Jul 2024](https://www.uber.com/blog/genai-gateway/)).

## Why this overlap exists

ML engineers know models but often not platforms; platform engineers know golden paths but not GPUs, training jobs or model evaluation; cloud engineers know capacity but not ML lifecycles. ML platforms fail in the gaps: idle GPUs reserved by one team while another queues for days, models that cannot be reproduced, a provider's model update that silently degrades ten products, a token bill nobody can attribute. The composed courses each cover one side; the overlap courses join them.

**Demand evidence (checked October 2026).**

| Signal | Figure | Source |
|---|---|---|
| AI and ML specialists | Third fastest-growing job to 2030 globally; also among India's fastest-growing roles | [WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf) |
| Skills in US AI postings | AWS +1,358% against a decade earlier; scalability +733%; workflow management +818% | [AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) |
| Deployment gap | Organisational AI use at 88%, but agent deployment "in the single digits across nearly all business functions" | [AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) |
| Platforms | 90% of organisations had adopted at least one internal platform | [DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) |
| Kubernetes as the AI substrate | 82% of container users run Kubernetes in production; the CNCF frames Kubernetes as the operating layer for AI workloads | [CNCF, Jan 2026](https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/) |

**Analysis.** The gap between AI pilots and AI in production is largely a platform gap: evaluation, serving, cost control and reliability. That is the work this overlap trains for.

## Before you start

Catalog prerequisites for both overlap courses ([catalog.json](../../catalog.json)): **MLE303** Training Pipelines, Feature Stores and Experiment Tracking; **OPS303** Observability; **CLD303** Containers and Kubernetes. Corequisites: **MLE401**, **OPS401** and **CLD404**, taken alongside. Note that CLD404 itself requires [CLD304](../../03_majors/cloud_engineering/year_3/CLD304_cloud_networking_vpcs_dns_load_balancing/README.md) and MLE401 requires MLE301. This is the heaviest overlap in the university: plan it with an adviser.

## How to sequence the courses

**Standard plan (strong ML or platform background).**

| Semester | Composed and prerequisite courses | Overlap course |
|---|---|---|
| 5 (Y3) | MLE303, OPS303, CLD303 (take the ones outside your major as electives; move one to semester 6 if needed) | — |
| 6 (Y3) | CLD304 (for CLD404), MLE301 (for MLE401) if not in your major | — |
| 7 (Y4) | **MLE401**, **OPS401** | **OV04A** ML Platform Engineering |
| 8 (Y4) | **CLD404** | **OV04B** LLMOps at Scale |

**Stretched plan.** If semester 7 is full, take OV04A in semester 8 alongside CLD404 and OV04B in semester 9 as part of [THS501](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) project work; the DevOps major page recommends this route.

Division of labour: **MLE401** teaches deploying, monitoring and retraining *a model*; **OPS401** teaches building *a platform as a product*; **CLD404** teaches *GPU infrastructure and inference engines*. **OV04A** builds the multi-tenant ML platform from those parts. **OV04B** runs LLM access, inference, evaluation and cost for a whole organisation. [AIE403](../../03_majors/ai_engineering/year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md) covers LLMOps for one application team; OV04B is the platform view across many.

## The two overlap courses

| Course | Semester | What you can do at the end |
|---|---|---|
| [OV04A · ML Platform Engineering](OV04A_ml_platform_engineering/README.md) | 7 | Build a multi-tenant ML platform on Kubernetes: GPU scheduling with quotas, notebooks, training and pipeline services, feature store, registry, serving golden path, SLOs and cost attribution |
| [OV04B · LLMOps at Scale](OV04B_llmops_at_scale/README.md) | 8 | Run an organisation's LLM layer: gateway, self-hosted inference fleets, capacity planning, evaluation platform, fine-tuning pipelines, cost attribution, safety controls and incident response |

## Capstone: an internal AI platform for two product teams

**Brief.** Build an internal ML and LLM platform on a Kubernetes cluster with GPU nodes (cloud credits, an Indian GPU cloud, or the IndiaAI compute portal described in CLD404) and serve two illustrative product teams: a fraud-scoring team (tabular model, real-time inference) and a support-assistant team (LLM with retrieval). The platform must let both teams train, evaluate, ship and observe their models through self-service.

**Acceptance criteria (all measurable).**

1. **Self-service.** A new team gets a namespace, quotas, notebook, pipeline template and serving template from one template run in under 15 minutes.
2. **Scheduling.** Kueue (or equivalent) enforces per-team GPU quotas with borrowing; in a contention test, the guaranteed team's job starts within 5 minutes while the borrowing team's jobs are preempted cleanly and resume from checkpoints.
3. **Reproducibility.** Any production model can be traced to its code commit, data snapshot, parameters and evaluation run; retraining from the record reproduces metrics within a stated tolerance.
4. **Serving.** The fraud model serves at p99 < 50 ms at 500 requests per second; the LLM path meets a stated time-to-first-token SLO at a stated concurrency; both deploy by canary with automatic rollback.
5. **Gateway.** All LLM calls go through one gateway with per-team keys, token budgets, fallback between a self-hosted model and an external API, and PII redaction; a provider outage drill keeps the assistant answering with a degraded model.
6. **Evaluation gates.** A model or prompt change cannot reach production unless it passes its evaluation suite; a planted regression is blocked.
7. **Cost.** GPU-hours and tokens are attributed to each team with less than 5% unattributed; average GPU utilisation of the inference pool is reported with a plan to raise it.
8. **Operations.** Platform SLOs (job start latency, serving availability, gateway error rate) with dashboards and runbooks; one game day covering a GPU node failure and a provider outage.

## Roles it leads to

| Role | What people in it do | Entry route |
|---|---|---|
| MLOps Engineer | Pipelines, deployment, monitoring and retraining for production models | Direct entry with the capstone as evidence |
| ML Platform Engineer | Builds the shared ML platform as a product for many teams | Direct entry or after a year as MLOps or platform engineer |
| AI Platform / LLMOps Engineer | Runs gateways, inference fleets, evaluation services and cost controls for LLM products | Direct entry for students strong in OV04B |
| ML Infrastructure / Inference Engineer | GPU clusters, schedulers, inference engines, performance | Often after CLD404 and MLE404-level depth |

## Sources

All checked 12 Oct 2026.

- Uber, "From Predictive to Generative – How Michelangelo Accelerates Uber's AI Journey" (2 May 2024) — https://www.uber.com/blog/from-predictive-to-generative-ai/
- Uber, "Navigating the LLM Landscape: Uber's Innovation with GenAI Gateway" (11 Jul 2024) — https://www.uber.com/blog/genai-gateway/
- World Economic Forum, Future of Jobs Report 2025 — https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- Stanford HAI, AI Index Report 2026 — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- Google Cloud / DORA, Announcing the 2025 DORA report — https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- CNCF Annual Cloud Native Survey (20 Jan 2026) — https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/

_Last reviewed: 2026-10_
