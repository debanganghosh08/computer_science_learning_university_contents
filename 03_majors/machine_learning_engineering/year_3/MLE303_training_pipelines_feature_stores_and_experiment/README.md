# MLE303 · Training Pipelines, Feature Stores and Experiment Tracking

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L4 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [MLE403](../../year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md), [MLE401](../../year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md), [OV04](../../../../04_overlaps/OV04_mlops_ml_platform/README.md) |

## Why this course matters now

In an interview study of 18 ML engineers, Shankar et al. (2022) found that three things govern whether a production ML deployment succeeds: velocity, validation and versioning. This course is about all three. The tools change fast: lakeFS acquired DVC (November 2025), CoreWeave acquired Weights & Biases (May 2025), MLflow 3 (June 2025) made the logged model a first-class object and added GenAI tracing, Airflow 3 shipped in April 2025, Tecton's feature store moved to Databricks (August 2025), and Google renamed Vertex AI and is shutting its legacy feature store in February 2027. The concepts do not change: a training run you can reproduce, data you can roll back, features that are correct as of the moment of prediction, and a record of every experiment. Coding agents now write DAGs, feature definitions and tracking code quickly. Whether a backfill is idempotent, whether a join leaks the future, and whether last month's model can be rebuilt bit-for-bit are still questions a human has to answer and test.

## Learning outcomes

By the end you can:

1. **Turn** a notebook into a tested, configurable, containerised training pipeline that anyone on the team can run with one command.
2. **Version** datasets and models (DVC, lakeFS, table-format time travel) and **rebuild** any past model from its recorded inputs.
3. **Validate** data with schemas and statistical checks (pandera, Great Expectations) and **define** data contracts with producers.
4. **Build** point-in-time-correct training sets and **prove** they contain no future information.
5. **Design and operate** a feature store (Feast) with offline and online stores, materialisation and streaming features, and **decide** when a team does not need one.
6. **Track** experiments (MLflow, W&B) with enough metadata (code, data, environment, parameters) to answer "why is this model better?" months later.
7. **Orchestrate** pipelines with idempotent, retryable, backfillable tasks (Airflow, Dagster, Prefect, Kubeflow Pipelines, Metaflow) and **compare** orchestrators by their abstractions.
8. **Detect and prevent** training–serving skew, and **trace** lineage from a prediction back to the data that trained the model.

## Chapters and lessons

### Chapter 1 · From notebook to pipeline (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The ML lifecycle | Data → features → training → evaluation → registry → serving → monitoring; the 3 Vs (Shankar et al., 2022) | Map a Kaggle notebook's cells to lifecycle stages |
| 1.2 Project structure | Package layout, separation of config, code and data (Cookiecutter Data Science) | Restructure a notebook into a package with a CLI |
| 1.3 Configuration | Hierarchical configs and overrides (Hydra); no magic numbers in code | Run 3 experiment variants from config alone |
| 1.4 Environments | Lock files (uv), containers (Docker), CUDA and driver compatibility | Build a container that reproduces the run on a second machine |

**Check your understanding:** Why is a notebook a poor unit of reproducibility? What belongs in config and what in code? Why can the same code give different results in two containers?

### Chapter 2 · Data versioning (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Content addressing | Hashes as identities; immutable snapshots; why copying files is not versioning | Hash a dataset; show a one-row change produces a new identity |
| 2.2 DVC | Pointer files in Git, remote storage, pipelines (`dvc.yaml`), `dvc repro` | Version a dataset and a 3-stage pipeline with DVC |
| 2.3 lakeFS | Git-like branches and commits over object storage; isolated experiments; zero-copy branching | Branch a data lake, run a cleaning job, merge or discard |
| 2.4 Table time travel | Delta Lake and Apache Iceberg snapshots; querying a table as of a timestamp | Train on a table "as of" last Monday |
| 2.5 Cost and retention | Storage growth, garbage collection, legal deletion (right to erasure) vs reproducibility | Write a retention policy that respects deletion requests |

**Check your understanding:** Why is "the data folder on the shared drive" not a version? How does a deletion request conflict with bit-for-bit reproducibility, and how do teams resolve it? When is table time travel enough without a separate tool?

### Chapter 3 · Data validation and contracts (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Why validate | Silent data bugs; Google's data validation system (Polyzotis et al., 2019) | Plant 5 data bugs; see which ones change model accuracy |
| 3.2 Schemas in code | pandera schemas for DataFrames; types, ranges, nullability, uniqueness | Write a pandera schema; fail the pipeline on violation |
| 3.3 Expectations and suites | Great Expectations (GX Core 1.x): expectation suites, validation definitions, checkpoints | Run a GX suite on each new batch; publish the results |
| 3.4 Distribution checks | Drift between training and new batches: PSI, KS tests, category frequencies | Alert when a category's share doubles |
| 3.5 Data contracts | Producer–consumer agreements, schema evolution, breaking-change review | Draft a contract with the team that owns your events table |

**Check your understanding:** Which data bugs will not break a schema check but will break a model? Why should validation run before training, not after? Who should own a data contract?

### Chapter 4 · Point-in-time training data (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Entities, timestamps, labels | Entity keys, event time vs processing time, label time | Model a loan-default dataset as entities and events |
| 4.2 Point-in-time joins | "As-of" joins (Feast docs; DuckDB `ASOF JOIN`); TTLs for stale features | Build a training set; test that no feature timestamp exceeds its label timestamp |
| 4.3 Backfills | Recomputing history with today's code; idempotency; partitioning | Backfill 90 days of features; rerun and prove identical output |
| 4.4 Feature definitions as code | Reviewable, tested feature logic shared by training and serving | Write 10 features with unit tests |

**Check your understanding:** Why does a plain join on customer ID leak future information? What goes wrong if a backfill is not idempotent? Why does processing time differ from event time, and which should a join use?

### Chapter 5 · Feature stores (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 What a feature store does | Registry, offline store, online store, materialisation, serving API; Uber's Michelangelo as an early example | Draw the architecture and name each component in Feast |
| 5.2 Feast hands-on | Entities, feature views, data sources, `get_historical_features`, `materialize`, online retrieval | Build a Feast repo over Parquet + Redis for a delivery dataset |
| 5.3 Streaming features | Kafka → stream processor → online store (Instacart, 2022); windowed aggregates; late events | Push streaming aggregates into the online store; measure freshness |
| 5.4 Online serving performance | Key design, batch lookups, p99 latency, hot keys | Load-test online feature retrieval; cut p99 |
| 5.5 The landscape | Feast, Hopsworks, Databricks Feature Store (Unity Catalog), Tecton (moving to Databricks), Google's Agent Platform Feature Store | Choose a feature store for 3 company profiles and justify it |
| 5.6 When not to use one | Small teams, batch-only models, a few features | Argue the "no feature store" case for a 3-person startup |

**Check your understanding:** What problem does the online store solve that the offline store cannot? Why do streaming features need watermarks? When is a feature store overhead rather than help?

### Chapter 6 · Experiment tracking (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 What to record | Parameters, metrics, artefacts, code commit, data version, environment, hardware | Define a "run manifest" for your team |
| 6.2 MLflow 3 | Runs, the logged-model entity, model registry and aliases, autologging, GenAI tracing | Track 20 runs; register the best model with its lineage |
| 6.3 Weights & Biases | Runs, sweeps, artefacts, reports (now part of CoreWeave) | Run the same sweep in W&B; compare workflows |
| 6.4 Search at scale | Optuna and Ray Tune; early stopping of trials (ASHA); budgets | Tune with a 2-GPU-hour budget; compare with random search |
| 6.5 Experiment hygiene | Naming, tags, baselines, negative results, the experiment log as a team asset | Write a weekly experiment summary from tracked runs only |

**Check your understanding:** Which missing field most often makes an old result impossible to explain? Why log failed runs? What is the risk of choosing a model by the best of 500 runs on one validation set?

### Chapter 7 · Reproducibility and determinism (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Sources of randomness | Seeds, data order, dropout, non-deterministic GPU kernels (PyTorch randomness notes) | Make a training run bit-for-bit repeatable on one GPU |
| 7.2 Levels of reproducibility | Same machine, same environment, same results within tolerance; what to promise | Write the reproducibility policy for a model card |
| 7.3 The rebuild test | Rebuild last month's model from recorded inputs; compare predictions | Automate a monthly rebuild test |
| 7.4 Numerical drift | Library upgrades changing results; pinning and controlled upgrades | Upgrade one library; quantify prediction differences |

**Check your understanding:** Why might bit-for-bit reproducibility be the wrong goal for a large GPU job? What should you do when a library upgrade changes predictions slightly? Which inputs must be recorded for a rebuild to be possible?

### Chapter 8 · Orchestration (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 DAG fundamentals | Tasks, dependencies, retries, idempotency, sensors, scheduling vs triggering | Turn your pipeline into a DAG with retries |
| 8.2 Airflow 3 | Assets, DAG versioning, the task SDK; scheduler and executor roles | Run the pipeline in Airflow with a daily schedule and a backfill |
| 8.3 Asset-centric orchestration | Dagster software-defined assets and partitions; Prefect flows | Re-express the pipeline as Dagster assets; compare |
| 8.4 ML-specific orchestrators | Kubeflow Pipelines on Kubernetes (CNCF graduated, 2026); Metaflow (from Netflix); ZenML | Run one stage on Kubernetes (kind or minikube) |
| 8.5 Choosing | Team skills, infrastructure, data vs ML focus, lock-in | Write a decision record choosing an orchestrator |

**Check your understanding:** Why must every task be safe to run twice? What does an asset-centric model make easier than a task-centric one? Why is "cron plus scripts" sometimes the right answer?

### Chapter 9 · Production-quality training jobs (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Training as code | Entry points, config, logging, checkpoint and resume, graceful shutdown | Kill a training job mid-run; resume to the same final metrics |
| 9.2 Testing ML code | Unit tests for features, data tests, smoke training runs, model behaviour tests; the ML Test Score (Breck et al., 2017) | Add 4 test types to your pipeline's CI |
| 9.3 Resources and cost | CPU vs GPU, spot or preemptible instances, cost per training run | Estimate and then measure the cost of one full run |
| 9.4 Evaluation as a pipeline stage | Automatic evaluation against the current production model; promotion criteria | A pipeline step that registers a model only if it beats production on every key slice |

**Check your understanding:** Why does checkpointing make spot instances usable? What is the cheapest test that catches the most pipeline bugs? Why compare against the production model rather than a fixed number?

### Chapter 10 · Training–serving skew and lineage (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Skew sources | Different code paths, stale joins, defaults, time zones, rounding; Rules of ML #29, #31, #32, #37 | Find and fix 4 planted skew bugs |
| 10.2 Logging served features | Log features at serving time and train on them | Add a feature log; compare served vs recomputed values |
| 10.3 Lineage | OpenLineage events; linking data version, code, parameters and model version | Trace one prediction back to its training data |
| 10.4 Model registry metadata | Stages and aliases, approvals, model cards linked to runs | Promote a model with a complete lineage record |

**Check your understanding:** Why is "train on logged serving features" the strongest defence against skew? What question does lineage answer during an incident? What is the minimum metadata a registered model needs?

### Chapter 11 · Pipelines for the LLM era and integration (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Embedding pipelines | Embeddings as versioned features; re-embedding when the encoder changes | Version an embedding table with its encoder version |
| 11.2 Datasets for fine-tuning | Versioned instruction and preference datasets; deduplication and contamination checks | Build a versioned fine-tuning dataset with a contamination test |
| 11.3 Evaluation sets as assets | Golden sets versioned like code; tracing and prompt registries (MLflow GenAI) | Track an LLM-based labeller's prompts and outputs |
| 11.4 Integration | All pieces together: versioned data, validation, features, tracking, orchestration, registry | Run the P3 pipeline end to end on a schedule |

**Check your understanding:** Why does changing the embedding model force a re-index? How can a benchmark leak into a fine-tuning dataset? Which parts of a classic ML pipeline carry over unchanged to LLM work?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Notebook to package | — |
| 2 | 2 | Lab 2 · DVC and lakeFS | — |
| 3 | 3 | Lab 3 · Validation and contracts | **P1 due** |
| 4 | 4 | Lab 4 · Point-in-time joins and backfills | — |
| 5 | 5 | Lab 5 · Feast offline and online | — |
| 6 | 5–6 | Lab 6 · Streaming features | — |
| 7 | 6–7 | Lab 7 · Tracking, sweeps and determinism | Mid-term (AI off) |
| 8 | 8 | Lab 8 · Orchestration: Airflow | — |
| 9 | 8 | Lab 8 (continued): Dagster or Kubeflow | **P2 due** |
| 10 | 9 | Lab 9 · Resumable, tested training | — |
| 11 | 10 | Lab 10 · Skew and lineage | — |
| 12 | 11 | Embedding and fine-tuning datasets | — |
| 13 | 11 | Integration (P3) | — |
| 14 | 11 | Rebuild test and review (P3) | **P3 due** |
| 15 | Review | P3 demo | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating DAG and feature-definition boilerplate; translating a pipeline between orchestrators; writing pandera schemas and GX suites from a data sample; explaining tool documentation; reviewing Dockerfiles. Claude Code, GitHub Copilot, Cursor and similar assistants do this well.
- **Do without AI (drills):** write a point-in-time join in SQL; list what must be recorded to rebuild a model; decide which features need streaming; design a backfill that is safe to rerun. The mid-term and final are AI-off.
- **Verify AI output by:** a leakage test (no feature timestamp after the label timestamp); running every task twice and diffing outputs (idempotency); the rebuild test; comparing served and recomputed features; checking tool APIs against current documentation, because the APIs moved in 2024–2026 (GX Core 1.0, MLflow 3, Airflow 3, Evidently 0.7).
- **Where AI still fails here:** generated feature code joins on entity ID without a time condition; generated DAGs are not idempotent (appending instead of overwriting partitions); assistants use deprecated APIs (pre-1.0 Great Expectations, Airflow 2 imports, MLflow 2 patterns); and they suggest tools whose status changed (TorchServe archived in 2025, Google's legacy feature store shutting down in 2027). Lab 4 asks you to catch a time-travel bug in assistant-written feature code.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 45% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 20% |

**Mastery gate.** You pass when you can: (1) hand a classmate your repository and have them rebuild your registered model from a clean machine with one command, matching your predictions within the stated tolerance; (2) without AI, write a point-in-time-correct training query for a new schema and a test that proves it; (3) explain, for any registered model, exactly which data version, code commit, parameters and environment produced it.

## Industry reality

Every company that runs ML in production has some version of this stack, whether open source, managed or built in-house. Uber's Michelangelo introduced a shared feature store with around 10,000 features (2017); Instacart streams real-time features through Kafka and Flink into a feature store (2022); Netflix built Metaflow and released it as open source. The same components appear, under different names, in managed platforms (Databricks, SageMaker AI, Google's Agent Platform), so skills learned on open-source tools transfer.

**Interview questions from this course**

1. *How do you make sure a training set does not use future information?* Strong answer: event-time keys, as-of joins, TTLs, label-time cut-offs, tests asserting feature time ≤ label time, logged serving features.
2. *A model trained last quarter performs differently when retrained on the same data. What do you check?* Strong answer: data version actually identical, code and library versions, seeds and non-deterministic kernels, config differences, environment and hardware; the rebuild test.
3. *Do we need a feature store?* Strong answer: depends on online serving, feature reuse, freshness and team size; the problems it solves (skew, point-in-time, reuse) and its costs; alternatives.
4. *Design a daily retraining pipeline.* Strong answer: validation gates, idempotent tasks, backfills, evaluation against production with slices, registry promotion, rollback, lineage, alerts.
5. *What would you log for each experiment?* Strong answer: parameters, metrics with variance, code commit, data version, environment, hardware, artefacts, notes on intent and outcome, including failures.

## Resources (free first)

- **Courses:** Made With ML, MLOps course — https://madewithml.com/courses/mlops/ ; Stanford CS329S — https://stanford-cs329s.github.io/ ; Full Stack Deep Learning (2022) — https://fullstackdeeplearning.com/course/2022/
- **Versioning and validation:** DVC — https://doc.dvc.org/ ; lakeFS — https://docs.lakefs.io/latest/ ; Delta Lake time travel — https://docs.delta.io/delta-batch/#query-an-older-snapshot-of-a-table-time-travel ; Iceberg time travel — https://iceberg.apache.org/docs/latest/spark-queries/#time-travel-queries-with-sql ; pandera — https://pandera.readthedocs.io/ ; Great Expectations — https://docs.greatexpectations.io/docs/core/introduction/ ; TFDV guide — https://www.tensorflow.org/tfx/guide/tfdv
- **Features:** Feast — https://docs.feast.dev/ ; Feast point-in-time joins — https://docs.feast.dev/getting-started/concepts/point-in-time-joins ; Hopsworks — https://docs.hopsworks.ai/ ; featurestore.org (community overview) — https://www.featurestore.org/
- **Tracking and tuning:** MLflow — https://mlflow.org/docs/latest/ ; W&B (CoreWeave) — https://docs.coreweave.com/forge-home ; Optuna — https://optuna.readthedocs.io/en/stable/ ; Ray Tune — https://docs.ray.io/en/latest/tune/index.html
- **Orchestration:** Airflow — https://airflow.apache.org/docs/apache-airflow/stable/ ; Dagster — https://dagster.io/docs ; Prefect — https://docs.prefect.io/ ; Kubeflow Pipelines — https://www.kubeflow.org/docs/components/pipelines/ ; Metaflow — https://docs.metaflow.org/ ; ZenML — https://docs.zenml.io/
- **Reproducibility and structure:** Hydra — https://hydra.cc/ ; uv — https://docs.astral.sh/uv/ ; Cookiecutter Data Science — https://cookiecutter-data-science.drivendata.org/ ; PyTorch reproducibility notes — https://docs.pytorch.org/docs/stable/notes/randomness.html ; OpenLineage — https://openlineage.io/
- **Guides and papers:** Rules of ML (training–serving skew rules) — https://developers.google.com/machine-learning/guides/rules-of-ml ; Polyzotis et al., "Data Validation for Machine Learning" (MLSys 2019) — https://proceedings.mlsys.org/paper_files/paper/2019/hash/928f1160e52192e3e0017fb63ab65391-Abstract.html ; Breck et al., "The ML Test Score" — https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/

## Sources

- Shankar, Garcia, Hellerstein and Parameswaran, "Operationalizing Machine Learning: An Interview Study" (arXiv 2209.09125, Sep 2022): 18 MLEs; velocity, validation, versioning — https://arxiv.org/abs/2209.09125 (checked 2026-10)
- lakeFS, "lakeFS acquires DVC" (Nov 2025) — https://lakefs.io/blog/lakefs-acquires-dvc/ ; CoreWeave, "CoreWeave Completes Acquisition of Weights & Biases" (5 May 2025) — https://coreweave.com/blog/coreweave-completes-acquisition-of-weights-biases ; Databricks, "Tecton is Joining Databricks" (22 Aug 2025) — https://www.databricks.com/blog/tecton-joining-databricks-power-real-time-data-personalized-ai-agents (checked 2026-10)
- MLflow 3 release notes (released Jun 2025; LoggedModel, GenAI tracing, prompt registry); latest 3.17.0 (7 Oct 2026) — https://mlflow.org/releases/3 (checked 2026-10)
- Apache Airflow, "Airflow 3.0 is here" (22 Apr 2025) — https://airflow.apache.org/blog/airflow-three-point-oh-is-here/ ; CNCF Kubeflow project page (graduated Jul 2026) — https://www.cncf.io/projects/kubeflow/ (checked 2026-10)
- Google Cloud feature store documentation (Vertex AI became part of Gemini Enterprise Agent Platform, Apr 2026; Feature Store (Legacy) deprecated, shutting down 17 Feb 2027) — https://cloud.google.com/vertex-ai/docs/featurestore/latest/overview (checked 2026-10)
- Uber, "Meet Michelangelo" (2017) — https://www.uber.com/blog/michelangelo-machine-learning-platform/ ; Instacart, real-time ML (2022) — https://tech.instacart.com/lessons-learned-the-journey-to-real-time-machine-learning-at-instacart-942f3a656af3 ; Metaflow repository — https://github.com/Netflix/metaflow (checked 2026-10)
- Versions on PyPI and GitHub releases (checked 2026-10): MLflow 3.17.0, wandb 0.30.0, DVC 3.67.1, lakeFS 1.88.0, Feast 0.66.0, GX Core 1.24.0, pandera 0.34.1, Airflow 3.3.2, Dagster 1.13.26, Prefect 3.8.8, Kubeflow Pipelines 2.17.2, Metaflow 2.19.39, ZenML 0.97.0

_Last reviewed: 2026-10_
