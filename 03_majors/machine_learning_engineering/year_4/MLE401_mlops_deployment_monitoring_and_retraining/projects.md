# MLE401 · Labs and projects

The lab environment is a local Kubernetes cluster (`kind` or `minikube`) with KServe or Ray Serve, MLflow, Argo CD and Argo Rollouts (or Flagger), Prometheus and Grafana, and Evidently. A free-tier cloud account is optional. Use a model you built earlier (the MLE305 fraud model or the MLE303 pipeline model) so the focus stays on operations. Traffic is simulated by replaying public data with a load generator (for example Locust or k6).

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Packaging and safe serialisation | Move a model from pickle to safetensors or ONNX; add a typed signature; build a slim, scanned image; ask an assistant for a deployment and log every outdated or unsafe suggestion | Image size before/after; scan report; the AI-suggestion log | 4 h |
| 2 · Serving patterns | Batch scoring of 10 M rows with idempotent writes; a FastAPI online service; the same model on KServe and Ray Serve with dynamic batching; a Kafka-based streaming scorer with replay; load tests | Batch rerun proof; latency-vs-RPS curves with the knee marked; p50/p99 comparison across servers; duplicate-handling test | 9 h (2 weeks) |
| 3 · Registry, GitOps and rollback | MLflow aliases; promotion by pull request through Argo CD; timed rollback | Promotion history; rollback time | 3 h |
| 4 · CI/CD/CT | GitHub Actions with unit, data, smoke-training and behaviour tests; automated staging deploy; CT trigger from the MLE303 pipeline | Workflow file; a run blocked by a failing data test | 4 h |
| 5 · Shadow and canary | Shadow a challenger; canary with automated analysis that aborts on p99, error rate or prediction-distribution shift | Analysis template; a recorded automatic abort | 4 h |
| 6 · Service and drift monitoring | Golden-signal dashboards; data-quality and drift monitors over 12 simulated weeks with a planted shift | Dashboard export; alert thresholds tuned to halve false alerts without missing the shift | 4 h |
| 7 · Delayed labels and performance estimation | Prediction–outcome joins with a 30-day delay; confidence-based performance estimation vs realised performance; per-city monitoring | Estimated vs actual accuracy plot; a detected one-city regression | 4 h |
| 8 · Retraining policies | Simulate a year of drifting data; compare scheduled, drift-triggered and performance-triggered retraining | Accuracy, compute cost and number of bad promotions per policy | 4 h |
| 9 · Game day and postmortem | A teammate injects an unannounced fault; you detect, mitigate and write a blameless postmortem | Timeline, mitigation evidence, postmortem with action items | 3 h |
| 10 · Tracing and eval gates for an LLM feature | Trace a small LLM-backed classifier (MLflow tracing or Langfuse); gate a prompt change on an evaluation set; cost per 1,000 requests | Trace screenshots; a blocked prompt change; cost dashboard | 4 h |

## Projects

### P1 · Production-ready model service (L1, ~6 hours)

**Real-world inspiration.** Uber's 2017 Michelangelo post describes online serving with p95 latency under 5 ms for models without remote feature lookups; most teams start with something far simpler, and the gap is closed by the practices in this course.

**What to build.** A containerised online inference service for one of your models, with a typed request schema, health and readiness endpoints, structured logs, Prometheus metrics, and a load-test report.

**Acceptance criteria**
- The image is under 800 MB (CPU model), pinned, scanned, with no critical vulnerabilities left unexplained.
- Invalid requests return a clear 4xx error; the service never crashes on malformed input (fuzz test with 1,000 random payloads).
- p99 latency and maximum sustainable RPS are reported from a load test, with hardware stated.
- Every prediction is logged with model version, request ID and feature values (or a hash, where privacy requires).
- The model loads only from the registry, in a safe format.

**Stretch goals.** gRPC endpoint; request batching with a measured throughput gain; a batch-scoring job sharing the same feature code.

**What it proves to an employer.** You can ship a model as a dependable service, not a notebook.

### P2 · Safe release and monitoring for a fraud model (L2, ~15 hours)

**Real-world inspiration.** Stripe Radar decides on each payment in under 100 ms (Stripe, 2023); the RBI's 2026 draft model-risk guidance expects kill-switch and human-override mechanisms for AI models. Releasing and watching such a model safely is a core MLOps job.

**What to build.** Take your MLE305 or MLE302 fraud model to a local Kubernetes deployment with GitOps, a shadow phase, a canary with automated analysis and rollback, monitoring of service health, drift and delayed-label performance, and a kill switch that routes decisions to a rules fallback.

**Acceptance criteria**
- A challenger is promoted through shadow and canary entirely by pull requests and automated analysis; a deliberately worse challenger is aborted automatically.
- Rollback to the previous model completes in under 2 minutes, measured.
- Dashboards cover golden signals, prediction distribution, top-feature drift and matured-label precision/recall by week.
- The kill switch switches traffic to the rules fallback within 30 seconds and is audit-logged.
- SLOs (latency, availability, freshness, quality) are written with error budgets.
- A runbook covers 4 scenarios: upstream schema change, feature-store outage, drift alert, performance drop.

**Stretch goals.** Thompson-sampling bandit across two variants on simulated traffic; per-segment canary analysis.

**What it proves to an employer.** You can be trusted with a high-stakes model in production: release discipline, observability and incident readiness.

### P3 · A small ML platform with continuous training (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Uber's Michelangelo grew from one platform for training and serving (2017) to more than 5,000 production models (2024); Netflix runs thousands of ML projects on Metaflow; Kubeflow, KServe and MLflow offer an open-source path to the same capabilities. Illustrative scenario: a 5-person ML team at an Indian lending start-up needs a lean version of the same platform.

**What to build.** An end-to-end platform on a local cluster: the MLE303 continuous-training pipeline feeding an MLflow registry, GitOps deployment with progressive delivery, monitoring with drift and delayed-label performance, automatic retraining triggers with promotion gates, and an LLM-feature path with tracing and eval gates. Then run a two-week simulation (accelerated time) with injected faults.

**Acceptance criteria**
- One `make up` brings the platform up from scratch on a laptop with 16 GB RAM, documented.
- During the simulation, at least two models are retrained and promoted automatically, and one bad candidate is blocked by gates.
- Three injected faults (bad data batch, latency regression, feature skew) are each detected by monitoring within the simulated hour, mitigated, and written up as postmortems.
- Every production prediction can be traced to model version, training data version and code commit.
- A platform README documents architecture, SLOs, runbooks, costs (estimated for a cloud deployment at 100 RPS) and an exit plan for each third-party dependency.
- A 20-minute demo shows a full release, an incident and a rollback.

**Stretch goals.** Multi-tenant namespaces with quotas; an internal "model card required" admission policy; cost attribution per model.

**What it proves to an employer.** You can design and run the platform that ML teams depend on, the core of ML platform engineering roles and the [OV04](../../../../04_overlaps/OV04_mlops_ml_platform/README.md) overlap.

## Feeds into

- [OV04 MLOps and ML Platform Engineering](../../../../04_overlaps/OV04_mlops_ml_platform/README.md): P3 is the starting point for OV04A (ML platform engineering) and OV04B (LLMOps at scale).
- [MLE501 Frontier Seminar](../../year_5/MLE501_frontier_seminar_ml_research_engineering/README.md): the same discipline applied to research code and experiments.
- [MLE404 Efficient Inference](../../year_4/MLE404_efficient_inference_quantization_distillation/README.md): serving optimisations plug into P1–P3's services.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): runbooks, SLOs and postmortems carry over to real teams.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): monitoring and retraining policy studies are strong capstone topics.
