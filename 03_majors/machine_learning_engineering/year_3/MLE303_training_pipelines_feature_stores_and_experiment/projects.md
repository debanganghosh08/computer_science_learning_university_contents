# MLE303 · Labs and projects

Everything runs on a laptop with Docker, using open-source tools: DVC or lakeFS, pandera or Great Expectations, Feast with a local Redis online store, MLflow, and Airflow, Dagster or Kubeflow Pipelines (on `kind` or `minikube`). Public data: NYC TLC trip records, the Olist Brazilian e-commerce dataset, or another time-stamped dataset approved by your instructor. Every lab ends with a short "rerun proof": run it twice and show identical outputs.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Notebook to package | Restructure a Kaggle notebook into a package with a CLI, Hydra config, a uv lock file and a Dockerfile | Repo; a run on a second machine with matching metrics | 4 h |
| 2 · DVC and lakeFS | Version data and a 3-stage pipeline with DVC; branch, change and roll back a dataset in lakeFS | `dvc.yaml`, `dvc repro` log; lakeFS branch and merge history | 4 h |
| 3 · Validation and contracts | pandera schema and a GX Core suite; plant 5 data bugs; draft a data contract | Which bugs each tool caught; the contract document | 4 h |
| 4 · Point-in-time joins and backfills | `ASOF` joins in DuckDB; a leakage test; a 90-day idempotent backfill; review assistant-written feature code for time-travel bugs | Join code, tests, backfill diff (empty on rerun), the bug you found in the AI code | 4 h |
| 5 · Feast offline and online | Entities, feature views, historical retrieval, materialisation to Redis, online lookups | Feast repo; a training set from `get_historical_features`; online p99 latency for 100-entity lookups | 4 h |
| 6 · Streaming features | Replay events through a Kafka-compatible broker (Redpanda or Kafka in Docker), compute 10-minute windows, push to the online store | Freshness plot (event time to online availability); a late-event test | 5 h |
| 7 · Tracking, sweeps and determinism | MLflow runs with a full manifest; an Optuna or Ray Tune sweep with early stopping; a bit-for-bit repeatable run | MLflow screenshots or export; sweep summary; determinism proof | 4 h |
| 8 · Orchestration | The pipeline as an Airflow 3 DAG with retries, assets and a backfill; then the same pipeline as Dagster assets with partitions or as a Kubeflow pipeline on a local cluster | DAG code; backfill log; proof that rerunning a day is safe; a one-page comparison of the two orchestrators | 8 h (2 weeks) |
| 9 · Resumable, tested training | Checkpoint and resume; unit, data, smoke-training and behaviour tests in CI | CI run; resume proof (same final metrics after a kill) | 4 h |
| 10 · Skew and lineage | Fix 4 planted skew bugs; log served features; emit OpenLineage events; trace a prediction to its data | Skew report; lineage graph for one prediction | 4 h |

## Projects

### P1 · A reproducible training package (L1, ~6 hours)

**Real-world inspiration.** Sculley et al. (2015) describe how ML systems accumulate "pipeline jungles" and glue code; Shankar et al. (2022) found versioning to be one of three factors that decide whether a deployment succeeds. Teams lose weeks when nobody can rebuild the model that is in production.

**What to build.** A training package for a tabular model with versioned data (DVC), a data-validation gate (pandera), configuration (Hydra), experiment tracking (MLflow) and a container image.

**Acceptance criteria**
- `make train` (or one equivalent command) runs data validation, training and evaluation inside the container.
- Every MLflow run records parameters, metrics, the Git commit, the DVC data hash, the lock-file hash and hardware.
- A classmate rebuilds your model on their machine and their predictions match yours within a documented tolerance (exact match for the GBDT on CPU).
- The pipeline fails with a clear message when a planted schema violation is introduced.
- The README explains how to reproduce any past run from its MLflow run ID.

**Stretch goals.** A GitHub Actions workflow that runs a smoke training on every pull request; a lakeFS branch per experiment.

**What it proves to an employer.** You produce work other engineers can run, trust and build on, the first thing a team checks in a new ML engineer.

### P2 · A point-in-time feature platform (L2, ~15 hours)

**Real-world inspiration.** Uber's Michelangelo shared about 10,000 features across teams through a feature store (2017); Instacart moved to real-time features flowing from Kafka through Flink into a feature store (2022). Both exist to make features correct as of the prediction moment and identical in training and serving.

**What to build.** On NYC TLC trip data (or a food-delivery-like dataset), a Feast-based feature platform with at least 12 features: batch aggregates (zone-level demand over 7 days), streaming aggregates (pickups in the last 10 minutes, computed from a replayed event stream), and on-demand features (hour of day, distance). Materialisation runs on a schedule in your orchestrator. A small FastAPI service fetches online features for a prediction request.

**Acceptance criteria**
- A leakage test proves every training row's feature timestamps are at or before its label timestamp; a deliberately broken join makes the test fail.
- Online and offline values for the same entity and timestamp agree for 1,000 sampled requests (excluding documented streaming lag).
- Streaming features are available online within 30 seconds of the event time at the replay rate you report.
- Online retrieval p99 for 100 entities is reported under a load test, with hardware stated.
- A rerun of the 30-day backfill produces byte-identical offline data.
- A 2-page design note explains which features are batch, streaming or on-demand and why.

**Stretch goals.** Feature-level data-quality checks on materialisation; a cost estimate for running the same platform on a managed service.

**What it proves to an employer.** You understand the hardest data problem in production ML, correct and consistent features, and can build the infrastructure that solves it.

### P3 · A continuous-training pipeline with promotion gates (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Metaflow was built at Netflix, whose README says the company runs over 3,000 AI and ML projects on it; Uber's Michelangelo grew to more than 5,000 production models (2024). Platforms like these exist so that retraining is routine, safe and auditable rather than a hero effort.

**What to build.** A scheduled pipeline (Dagster, Airflow or Kubeflow) that, each simulated day: ingests a new data partition, validates it, computes features through your feature store, trains a candidate with tracked experiments, evaluates it against the production model overall and on key slices, registers it in MLflow with full lineage if it passes, and records why if it does not. Simulate 60 days of data with at least one bad-data day and one gradual drift.

**Acceptance criteria**
- 60 simulated days run end to end unattended; the dashboard or log shows each day's decision (promoted, rejected, blocked by validation).
- The bad-data day is blocked by validation before training; the drift period triggers at least one promotion of a retrained model.
- Every registered model links to its data version, feature definitions version, code commit, parameters and evaluation report.
- The rebuild test reproduces the model from day 30 from recorded inputs and matches its predictions within tolerance.
- Chaos tests: killing a task mid-run and rerunning it leaves no duplicate or partial data.
- A runbook (2–3 pages) covers rollback, backfill, a failed validation and a feature-store outage.
- A cost report estimates compute and storage per month at the simulated scale.

**Stretch goals.** An LLM-labelled auxiliary dataset tracked as a versioned asset with its prompts; OpenLineage integration with a lineage UI (for example Marquez).

**What it proves to an employer.** You can build the training side of an ML platform, the work of ML platform engineers and senior ML engineers, and you can show it working, not just describe it.

## Feeds into

- [MLE403 Ranking and Recommendation](../../year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md): feature freshness and point-in-time correctness at recommender scale.
- [MLE401 MLOps](../../year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md): P3's registry and gates connect to deployment, canaries, monitoring and retraining triggers.
- [OV04 MLOps and ML Platform Engineering](../../../../04_overlaps/OV04_mlops_ml_platform/README.md): P2 and P3 are the starting point for platform work.
- [DEN304 Orchestration and Pipelines](../../../data_engineering/year_3/DEN304_orchestration_and_pipelines_airflow_and_dagster/README.md): the data-engineering view of the same orchestrators, for those who want more depth.
