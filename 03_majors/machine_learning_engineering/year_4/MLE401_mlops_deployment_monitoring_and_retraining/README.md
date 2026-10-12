# MLE401 · MLOps: Deployment, Monitoring and Retraining

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [MLE301](../../year_3/MLE301_machine_learning_algorithms_from_scratch/README.md) (and in practice [MLE303](../../year_3/MLE303_training_pipelines_feature_stores_and_experiment/README.md)) | [MLE501](../../year_5/MLE501_frontier_seminar_ml_research_engineering/README.md), [OV04 MLOps and ML Platform Engineering](../../../../04_overlaps/OV04_mlops_ml_platform/README.md), [IND401](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) |

## Why this course matters now

A model creates value only after it is deployed, watched and kept fresh. At Uber, the Michelangelo platform served more than 5,000 production models and up to 10 million real-time predictions per second at peak (2024). The tool landscape keeps moving: TorchServe was archived in August 2025, NVIDIA renamed Triton Inference Server to Dynamo-Triton in March 2025, KServe joined the CNCF as an incubating project in 2025, Modular acquired BentoML in February 2026, and Seldon Core moved to a source-available licence in January 2024. A course that teaches one tool's buttons is out of date within a year; this one teaches the patterns (packaging contracts, serving modes, progressive delivery, drift and performance monitoring, retraining triggers, incident response) using current open-source tools as examples. Coding agents now write Dockerfiles, Kubernetes manifests and CI workflows in minutes. Deciding how a model is rolled out, what counts as "broken", when to retrain and when to roll back is still the job of an engineer who will be paged at 3 a.m.

## Learning outcomes

By the end you can:

1. **Package** a model with a typed signature, a pinned environment and a safe serialisation format, and **explain** why unpickling untrusted files is dangerous.
2. **Deploy** models for batch, online (REST/gRPC) and streaming inference, and **choose** among them by latency, cost and freshness.
3. **Operate** a model registry with promotion stages, approvals and model cards, and **implement** GitOps-style deployment.
4. **Build** CI/CD/CT pipelines for ML with code, data and model tests as gates.
5. **Run** shadow, canary and blue/green releases with automated analysis and rollback.
6. **Monitor** service health, data quality, drift and model performance (including with delayed labels), and **design** alerts that are actionable.
7. **Design** retraining policies (scheduled, triggered, champion/challenger) and **evaluate** their cost and risk.
8. **Respond** to ML incidents with runbooks, rollbacks and blameless postmortems, and **meet** governance needs such as audit logs and kill switches.
9. **Explain** what changes for LLM-based systems (prompts as artefacts, tracing, evaluation in the loop, token cost) and what stays the same.

## Chapters and lessons

### Chapter 1 · MLOps foundations (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Why MLOps | Hidden technical debt (Sculley et al., 2015); the gap between a notebook and a service | List the debts in a provided "working" ML repo |
| 1.2 Maturity levels | Google's levels 0 (manual), 1 (pipeline automation), 2 (CI/CD automation) | Place 3 described teams on the scale; plan one step up |
| 1.3 Delivery metrics | DORA metrics (deployment frequency, lead time, change failure rate, recovery time) adapted to models | Define the 4 metrics for a model team |
| 1.4 Roles | ML engineer, ML platform engineer, SRE, data engineer: who owns what | Write a RACI for a model release |

**Check your understanding:** Why does an ML system have more ways to fail than an ordinary service? What does "level 2" automate that "level 1" does not? Which DORA metric matters most for a fraud model, and why?

### Chapter 2 · Packaging models (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Serialisation formats | pickle/joblib, safetensors, ONNX, `torch.export`; the arbitrary-code-execution risk of unpickling (Python docs warning) | Switch a model from pickle to safetensors or ONNX; add a loader that refuses files from outside the registry |
| 2.2 Signatures and contracts | Input/output schemas, versioned APIs, backward compatibility | Add a signature to an MLflow model; reject a malformed request |
| 2.3 Containers | Slim images, multi-stage builds, CPU vs GPU base images, reproducible builds | Cut an image from 3 GB to under 800 MB |
| 2.4 Supply chain | Dependency pinning, image scanning, model provenance, SBOMs | Scan your image and fix the critical findings |

**Check your understanding:** Why is a model file a code-execution risk? What breaks when a client sends a new optional field? Why should training and serving images share a base?

### Chapter 3 · Serving patterns (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Batch inference | Scheduled scoring into a table; partitioning; idempotent writes | Score 10 M rows with DuckDB or Spark; rerun safely |
| 3.2 Online inference | REST vs gRPC, request batching, timeouts, p99; FastAPI as a baseline | Serve a model; load-test to find the knee of the latency curve |
| 3.3 Model servers | KServe InferenceService, Ray Serve, BentoML, NVIDIA Dynamo-Triton, Seldon MLServer; dynamic batching | Deploy the same model on KServe and Ray Serve; compare |
| 3.4 Streaming inference | Consuming events from Kafka, scoring, producing decisions; exactly-once vs at-least-once | A streaming scorer with replay and deduplication |
| 3.5 Autoscaling | Horizontal autoscaling, scale-to-zero and cold starts, GPU sharing | Measure cold-start latency; set a minimum replica count |

**Check your understanding:** When is batch inference strictly better than online? What does dynamic batching trade away? Why is scale-to-zero a bad idea for a checkout fraud model?

### Chapter 4 · Registries and promotion (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Model registry | Versions, aliases ("champion", "challenger"), tags, lineage (MLflow) | Register 3 versions; promote by alias |
| 4.2 Approvals | Human sign-off, automated checks, model cards attached to versions | A promotion that requires a passed evaluation report |
| 4.3 GitOps for models | Desired state in Git, Argo CD sync, environment promotion (dev → staging → prod) | Promote a model by pull request |
| 4.4 Rollback | Keeping the previous version warm; database and feature compatibility | Roll back in under 2 minutes; time it |

**Check your understanding:** Why separate "registered" from "deployed"? What makes a rollback unsafe even when the old model is available? Who should be able to approve a production promotion?

### Chapter 5 · CI/CD/CT for ML (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Continuous integration | Unit tests, data tests, smoke training, model behaviour tests in CI | GitHub Actions workflow with 4 test stages |
| 5.2 Continuous delivery | Build → push → deploy to staging → integration tests → promote | Automated staging deployment on merge |
| 5.3 Continuous training | Pipelines triggered by schedule or event; promotion gates (from MLE303) | Connect your MLE303 pipeline to the registry and CD |
| 5.4 Test pyramid for ML | What to test at each level; the ML Test Score (Breck et al., 2017) | Score your system on the rubric; fix the two lowest items |

**Check your understanding:** Why does CI for ML need data? What is the smallest training run that still catches real bugs? What should block a deployment automatically, and what needs a human?

### Chapter 6 · Progressive delivery (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Shadow deployment | Mirroring traffic, comparing predictions, cost of shadows | Shadow a challenger for 24 simulated hours; diff its outputs |
| 6.2 Canary releases | Traffic splitting, automated analysis, rollback criteria (Argo Rollouts, Flagger) | Canary with an automatic abort on p99 or error rate |
| 6.3 Blue/green and A/B | Instant switch vs experiment; when each fits | Blue/green switch with a smoke test |
| 6.4 Bandits for model selection | Thompson sampling across model variants; when bandits beat fixed A/B tests | Simulate bandit vs A/B regret |

**Check your understanding:** What can a shadow deployment not tell you? Why must canary analysis compare against the baseline at the same time, not yesterday's numbers? When is a bandit the wrong tool?

### Chapter 7 · Monitoring the service and the data (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Golden signals | Latency, traffic, errors, saturation (Google SRE book); Prometheus, Grafana, OpenTelemetry | Instrument your service; build a dashboard |
| 7.2 Data quality in production | Missing values, schema changes, out-of-range values at serving time | Alert on a schema change from an upstream team |
| 7.3 Drift metrics | PSI, KS, Wasserstein, Jensen–Shannon; prediction drift; window sizes | Compute drift with Evidently on simulated weekly data |
| 7.4 Drift that matters | Drift vs performance; feature importance weighting; avoiding alert fatigue | Tune thresholds to cut false alerts by half without missing the planted shift |

**Check your understanding:** Why can strong drift leave accuracy unchanged? Why is prediction drift often the most useful early signal? What makes an alert actionable?

### Chapter 8 · Monitoring model performance (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Delayed labels | Label maturity, joining predictions to outcomes, backfilled metrics | Build the prediction–outcome join for a 30-day label delay |
| 8.2 Performance without labels | Proxy metrics; confidence-based performance estimation (NannyML's CBPE idea) and its assumptions | Estimate accuracy before labels arrive; compare later |
| 8.3 Segment monitoring | Per-slice metrics in production; minimum sample sizes | Detect a regression confined to one city |
| 8.4 SLOs for ML | Service-level objectives for latency, availability, freshness and quality | Write SLOs and error budgets for your P2 model |

**Check your understanding:** What do you monitor for a loan model whose labels take 6 months? When does confidence-based estimation fail? Why might a global metric hide a production incident?

### Chapter 9 · Retraining (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Triggers | Scheduled, drift-triggered, performance-triggered, data-volume-triggered | Compare 4 policies on a simulated year of data |
| 9.2 Champion/challenger | Offline gates, shadow, canary; never promote untested retrains | Automate a challenger evaluation |
| 9.3 Continual and online learning | Incremental updates vs full retrains; catastrophic forgetting; FSDL's continual-learning lecture | Online logistic regression vs weekly retraining on drifting data |
| 9.4 Cost and risk | Compute cost, labelling cost, risk of retraining on corrupted data | A cost–benefit table for daily vs weekly retraining |

**Check your understanding:** Why can retraining on fresh data make a model worse? What safeguards stop a bad data day from reaching production? When is weekly retraining wasteful?

### Chapter 10 · Incidents, reliability and governance (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 ML incident patterns | Upstream schema change, stale features, skew, feedback loops, bad labels; the AI Incident Database | Classify 10 public incidents by root cause |
| 10.2 Runbooks and on-call | Detection, triage, mitigation (rollback, fallback, kill switch), communication | Write a runbook; run a 30-minute game day |
| 10.3 Blameless postmortems | Timeline, contributing factors, action items (Google SRE workbook) | Write the postmortem for your game day |
| 10.4 Governance | Audit logs, access control, kill switches and human override (as in the RBI's 2026 draft model-risk guidance), model inventory | Add an audit log and an override path to your service |

**Check your understanding:** Why is "roll back the model" not always the fastest mitigation? What belongs in an ML-specific runbook that a generic one lacks? Why should a regulated model have a kill switch?

### Chapter 11 · What changes with LLMs (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 New artefacts | Prompts, retrieval indexes, tool definitions and evaluation sets versioned like models | Version a prompt and an evaluation set together |
| 11.2 Tracing | Spans for each LLM call and tool call (MLflow tracing, Langfuse, Arize Phoenix, OpenTelemetry) | Trace a small LLM feature; find the slowest step |
| 11.3 Evaluation in the loop | Offline evals as release gates; online feedback; regression suites | Gate a prompt change on an eval suite |
| 11.4 Cost and latency | Tokens per request, caching, model routing; GPU serving (preview of MLE404) | Cost dashboard per feature and per user |

**Check your understanding:** Which classic MLOps practices transfer unchanged to LLM features? Why is a prompt change a deployment? What does tracing show that request logs do not?

### Chapter 12 · Platforms and integration (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Platform architecture | Michelangelo's evolution; open-source stacks (Kubeflow, KServe, MLflow, Feast) vs managed (SageMaker AI, Databricks, Google's Agent Platform) | Map your course stack to Michelangelo's components |
| 12.2 Build vs buy | Team size, compliance, cost, lock-in | Decision record for a 30-engineer fintech |
| 12.3 Tool churn | Archived and relicensed projects (TorchServe, Seldon Core); exit plans | Write an exit plan for one dependency |
| 12.4 Integration | Everything together in P3 | P3 build and demo |

**Check your understanding:** What should never depend on a single vendor's proprietary format? What did TorchServe's archiving teach about choosing serving tools? What is the minimum platform a 5-person ML team needs?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1–2 | Lab 1 · Packaging and safe serialisation | — |
| 2 | 2–3 | Lab 2 · Serving patterns: batch and online | — |
| 3 | 3 | Lab 2 (continued): model servers and streaming | **P1 due** |
| 4 | 4 | Lab 3 · Registry, GitOps and rollback | — |
| 5 | 5 | Lab 4 · CI/CD/CT | — |
| 6 | 6 | Lab 5 · Shadow and canary | — |
| 7 | 7 | Lab 6 · Service and drift monitoring | Mid-term (AI off) |
| 8 | 8 | Lab 7 · Delayed labels and performance estimation | **P2 due** |
| 9 | 9 | Lab 8 · Retraining policies | — |
| 10 | 10 | Lab 9 · Game day and postmortem | — |
| 11 | 11 | Lab 10 · Tracing and eval gates for an LLM feature | — |
| 12 | 12 | Build-vs-buy memo | — |
| 13 | 12 | P3 build | — |
| 14 | 12 | P3 game day and demo | **P3 due** |
| 15 | Review | P3 presentation | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** Dockerfiles, Kubernetes manifests, Helm values, CI workflows and Grafana dashboards; explaining unfamiliar error messages; drafting runbooks and postmortems from your timeline; AIOps-style log summarisation during game days.
- **Do without AI (drills):** choose a serving pattern and justify it; design canary analysis criteria; write drift alert thresholds and justify them; triage a simulated incident from dashboards alone; write the rollback steps from memory. The mid-term and final are AI-off.
- **Verify AI output by:** applying manifests to a local cluster (`kind`) and running smoke tests; scanning generated images; checking every tool API and flag against current documentation; testing the rollback path, not just the deploy path; replaying a recorded incident against your alerts.
- **Where AI still fails here:** assistants still suggest TorchServe and other archived or relicensed tools; they generate manifests without resource limits, readiness probes or pod disruption budgets; they load models with `pickle` from untrusted paths; and they propose drift thresholds with no link to performance. In Lab 1 you list every unsafe or outdated suggestion an assistant makes for a deployment task.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 45% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 20% |

**Mastery gate.** You pass when you can: (1) take a trained model and, within one working day, deliver it as a containerised online service behind a canary with automated rollback, dashboards and drift monitoring; (2) during a 45-minute game day with an unannounced fault (bad upstream data, skew or a latency regression), detect it from your monitoring, mitigate it and write the postmortem; (3) without AI, design a retraining policy for a model with delayed labels and defend its triggers and safeguards.

## Industry reality

MLOps work is done by ML engineers, ML platform engineers and SREs who support ML teams. Public platforms show the scale: Uber's Michelangelo (2017, 2024), Netflix's Metaflow, Instacart's real-time ML platform (2022). Managed platforms (Amazon SageMaker AI, Databricks, Google's Gemini Enterprise Agent Platform, which absorbed Vertex AI in April 2026) and open-source stacks (Kubeflow, which became a CNCF graduated project in July 2026; KServe; MLflow; Feast) offer the same patterns under different names.

**Interview questions from this course**

1. *How would you roll out a new version of a fraud model?* Strong answer: offline gates; shadow to compare predictions; canary with automated analysis on latency, errors, prediction distribution and business guardrails; rollback criteria; label-delay awareness; communication with risk teams.
2. *Labels arrive 30 days late. How do you monitor the model?* Strong answer: data-quality and drift monitors; prediction distribution; proxy outcomes; performance estimation with stated assumptions; segment monitoring; backfilled true metrics when labels mature.
3. *When should a model be retrained?* Strong answer: compare scheduled vs triggered policies; validation gates; champion/challenger; cost; risk of training on corrupted data; evidence from backtests.
4. *Batch or online inference for a daily product recommendation email and for checkout fraud?* Strong answer: batch for the email (cheaper, simpler, latency irrelevant), online for fraud (fresh features, sub-100 ms budget), with fallbacks.
5. *Your model's prediction distribution shifted overnight. Walk me through the response.* Strong answer: check upstream data and schema changes, deployments and feature freshness first; compare with the shadow or previous version; mitigate by rollback or fallback if user impact is real; root-cause; postmortem; add a test or monitor.

## Resources (free first)

- **Courses and guides:** Made With ML (MLOps) — https://madewithml.com/courses/mlops/ ; Full Stack Deep Learning, continual learning lecture — https://fullstackdeeplearning.com/course/2022/lecture-6-continual-learning/ ; Google Cloud, "MLOps: Continuous delivery and automation pipelines in machine learning" — https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning ; Chip Huyen, "Data Distribution Shifts and Monitoring" — https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html ; Google SRE book, monitoring — https://sre.google/sre-book/monitoring-distributed-systems/ ; SRE workbook, postmortem culture — https://sre.google/workbook/postmortem-culture/
- **Serving:** KServe — https://kserve.github.io/website/ ; Ray Serve — https://docs.ray.io/en/latest/serve/index.html ; BentoML — https://docs.bentoml.com/ ; NVIDIA Dynamo-Triton — https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/ ; MLServer — https://mlserver.readthedocs.io/ ; safetensors — https://huggingface.co/docs/safetensors/index ; ONNX — https://onnx.ai/
- **Delivery:** GitHub Actions — https://docs.github.com/en/actions ; Argo CD — https://argo-cd.readthedocs.io/ ; Argo Rollouts — https://argo-rollouts.readthedocs.io/ ; Flagger — https://docs.flagger.app/ ; DORA — https://dora.dev/
- **Monitoring:** Prometheus — https://prometheus.io/docs/introduction/overview/ ; OpenTelemetry — https://opentelemetry.io/docs/ ; Evidently — https://docs.evidentlyai.com/ ; NannyML — https://nannyml.readthedocs.io/ ; Langfuse — https://langfuse.com/docs ; Arize Phoenix — https://arize.com/docs/phoenix/ ; SageMaker Model Monitor — https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html
- **Incidents:** AI Incident Database — https://incidentdatabase.ai/

## Sources

- Uber, "From Predictive to Generative – How Michelangelo Accelerates Uber's AI Journey" (2 May 2024) — https://www.uber.com/blog/from-predictive-to-generative-ai/ (checked 2026-10)
- TorchServe documentation ("no longer actively maintained"; repository archived 7 Aug 2025) — https://docs.pytorch.org/serve/ and https://github.com/pytorch/serve (checked 2026-10)
- NVIDIA, Dynamo-Triton product page ("formerly NVIDIA Triton Inference Server") — https://developer.nvidia.com/triton-inference-server ; Dynamo documentation — https://docs.nvidia.com/dynamo/latest/ (checked 2026-10)
- CNCF KServe project page (incubating) — https://www.cncf.io/projects/kserve/ ; CNCF Kubeflow project page (graduated) — https://www.cncf.io/projects/kubeflow/ (checked 2026-10)
- Modular, "BentoML joins Modular" (Feb 2026) — https://www.modular.com/blog/bentoml-joins-modular ; Seldon Core licence (Business Source License 1.1 from January 2024; MLServer remains Apache 2.0) — https://docs.seldon.ai/seldon-core-1/getting-started/license ; ClickHouse acquires Langfuse (Jan 2026) — https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability (checked 2026-10)
- Python `pickle` documentation security warning — https://docs.python.org/3/library/pickle.html (checked 2026-10)
- Sculley et al. (2015) — https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html ; Breck et al. (2017) — https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ (checked 2026-10)
- RBI draft model-risk guidance (24 Jun 2026; kill-switch and human-override expectations) — https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=63006 (checked 2026-10)
- Versions (PyPI and GitHub releases, checked 2026-10): KServe 0.21.0, Ray 2.59.0, BentoML 1.4.39, Dynamo-Triton 2.73.0, ai-dynamo 1.5.1, Argo Rollouts 1.10.0, Flagger 1.45.0, Evidently 0.7.23, MLflow 3.17.0

_Last reviewed: 2026-10_
