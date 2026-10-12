# DEN304 · Orchestration and Pipelines: Airflow and Dagster

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [DEN404](../../year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md), [DEN401](../../year_4/DEN401_data_quality_observability_and_data_contracts/README.md), [OV06A](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06A_building_a_modern_data_platform/README.md) |

Part of the [Data Engineering major](../../README.md). By semester 6 you can model data ([DEN301](../DEN301_data_modeling_and_warehousing/README.md)), process it in batch ([DEN302](../DEN302_batch_processing_with_spark/README.md)) and in streams ([DEN303](../DEN303_streaming_systems_kafka_and_flink/README.md)). This course is about running hundreds of such steps every day in the right order, again after failures, and over past dates. Model training pipelines are covered in [MLE303](../../../machine_learning_engineering/year_3/MLE303_training_pipelines_feature_stores_and_experiment/README.md); here the subject is data pipelines and the platforms that schedule them.

## Why this course matters now

Orchestration is where data teams spend their on-call nights. A pipeline that runs fine once can still duplicate data on a retry, skip a day after an outage, or rebuild three years of history when someone changes a start date. Airflow, started at Airbnb in 2014, is a common default; Razorpay reports scheduling over 3,000 workflows with it (2026). Airflow 3.0 (April 2025) was a major redesign: DAG versioning, scheduler-managed backfills, data assets with event-driven triggers, and a task execution interface that lets tasks run remotely. The current release is 3.3.2 (September 2026). Dagster organises pipelines around the data assets they produce rather than the tasks they run. Transformation tools now plan their own execution graphs: Spark Declarative Pipelines (Spark 4.1) and dbt v2 (a Rust engine with static analysis, after Fivetran and dbt Labs completed their merger on 1 June 2026). AI assistants generate a working DAG in seconds. Whether it is idempotent, whether it survives a three-day backfill, and whether the 6 a.m. finance report waits for the right upstream data are still design questions, and they are the subject of this course.

## Learning outcomes

By the end you can:

1. **Explain** how an orchestrator schedules work (scheduler loop, executors, workers, metadata store, data intervals), and **predict** which runs Airflow creates for a given schedule, start date and catchup setting.
2. **Build** pipelines in Airflow 3 (TaskFlow, providers, dynamic task mapping, deferrable operators, assets) and in Dagster (assets, partitions, asset checks, automation conditions).
3. **Design** idempotent tasks and partitioned outputs so that retries and backfills of any date range give the same result.
4. **Run** backfills and reprocessing cascades safely, and **estimate** their cost and impact on downstream consumers before starting.
5. **Design** dependency graphs: task granularity, cross-pipeline dependencies, event-driven triggers instead of polling, and ownership boundaries.
6. **Define** freshness and completion objectives for data assets, and **implement** the alerts and runbooks that enforce them.
7. **Test** pipelines at four levels (DAG integrity, task logic, integration, data) and **ship** them through CI/CD with separate environments.
8. **Compare** Airflow, Dagster, Prefect, Kestra, durable-execution engines and declarative transformation tools for a stated organisation, and **audit** AI-generated pipeline code for hidden non-determinism.

## Chapters and lessons

### Chapter 1 · Why orchestration exists (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 From cron to DAGs | What cron cannot do: dependencies, retries, history, backfills, visibility; directed acyclic graphs of work | Turn 6 cron scripts with hidden dependencies into a dependency graph on paper |
| 1.2 Control plane and data plane | Orchestrators schedule and observe; engines (Spark, warehouses, Flink) do the heavy work; why tasks should not move data through the orchestrator | Identify every place a sample pipeline passes data through the orchestrator |
| 1.3 The landscape | Airflow, Dagster, Prefect, Kestra; durable-execution engines (Temporal); managed services (Amazon MWAA, Cloud Composer, Astronomer, Databricks Lakeflow Jobs); declarative graphs inside tools (dbt, Spark Declarative Pipelines) | Map 10 tools onto task-centric, asset-centric, declarative and durable-execution categories |
| 1.4 What can go wrong | Duplicate loads, skipped intervals, thundering-herd catchups, zombie tasks, silent partial success | Read three public post-incident write-ups about data pipelines and classify the failure |

**Check your understanding:** (1) Why is "the job succeeded" weaker evidence than "the table for 12 October is complete"? (2) What goes wrong when a task downloads 50 GB into the orchestrator worker's memory? (3) When is cron still the right answer?

### Chapter 2 · Airflow core (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Architecture | Scheduler, DAG processor, API server, triggerer, executors (Local, Celery, Kubernetes, Edge), metadata database; Airflow 3's task execution interface and Task SDK | Run Airflow 3 with Docker Compose; trace one task from scheduling to completion in the logs |
| 2.2 Writing DAGs | TaskFlow API, operators, hooks and provider packages; top-level code costs; DAG parsing time | Write a 5-task DAG two ways; measure parse time with a slow import at top level |
| 2.3 Time in Airflow | Schedules, timetables, data intervals, logical date, `catchup`, start dates; asset-triggered runs | Predict every run created for 5 schedule configurations, then verify |
| 2.4 Control flow | Retries with exponential backoff, trigger rules, branching, dynamic task mapping, pools, priority weights, concurrency limits | Map a task over 200 files with a pool limiting warehouse connections to 8 |
| 2.5 Waiting well | Sensors in poke vs reschedule mode, deferrable operators and the triggerer, timeouts | Replace a poke sensor holding a worker slot for 6 hours with a deferrable one; count freed slot-hours |
| 2.6 XComs and their limits | What XComs are for (small metadata), custom XCom backends, why large data belongs in storage | Refactor a DAG that passes DataFrames through XComs |

**Check your understanding:** (1) A daily DAG with `start_date` one year ago and `catchup=True` is deployed: what happens next, and how do you stop it safely? (2) Why should a task use the data interval passed to it instead of `datetime.now()`? (3) Why do deferrable operators matter more as the number of pipelines grows?

### Chapter 3 · Assets and event-driven pipelines (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Task graphs vs asset graphs | Describing pipelines by the tables and files they produce; lineage as a side effect | Redraw a 12-task DAG as the 7 assets it produces |
| 3.2 Airflow assets | Assets (renamed from datasets in Airflow 3), producer and consumer DAGs, asset events, asset watchers triggering on external messages (for example Amazon SQS) | Trigger a DAG from a file landing event instead of a schedule |
| 3.3 DAG versioning | Runs tied to the code version they started with; reviewing what changed between runs | Change a DAG mid-run; show which version each task used |
| 3.4 Dagster assets | Software-defined assets, dependencies, materialisations, the asset catalogue, dbt models as assets | Build the same 7-asset pipeline in Dagster |

**Check your understanding:** (1) What does an asset graph tell an on-call engineer that a task graph does not? (2) Why is event-driven triggering cheaper and fresher than polling sensors, and what new failure does it introduce? (3) Why does DAG versioning matter for audits?

### Chapter 4 · Idempotency, partitions and backfills (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Functional data engineering | Pure tasks, immutable partitions, overwrite-by-partition, parameterised runs (Beauchemin, 2018) | Rewrite an append-only daily task as partition overwrite |
| 4.2 Hidden non-determinism | `now()`, unordered reads, random sampling, reading "latest" upstream data, external API drift | Find 5 hidden non-determinism bugs in a provided DAG |
| 4.3 Backfills | Airflow 3 scheduler-managed backfills, Dagster partition backfills, concurrency limits, run ordering, backfill windows | Backfill 90 days with a concurrency cap; measure warehouse load |
| 4.4 Reprocessing cascades | When an upstream fix must flow downstream; impact analysis from lineage; communicating restatements | Plan and run a cascade across 4 dependent assets after a bug fix |
| 4.5 External side effects | Emails, API calls and payments in pipelines; idempotency keys; "at most once" steps | Make a notification step safe under retries |

**Check your understanding:** (1) Why is "overwrite the partition" idempotent while "append the rows" is not? (2) A backfill of 2 years would take 9 days at current concurrency: what are your options and their trade-offs? (3) How do you prove to a finance team that a restated month changed only the expected rows?

### Chapter 5 · Dagster in depth (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Partitions | Time, static, dynamic and multi-dimensional partitions; partition mappings between assets | Partition an asset by day and region; map it to a monthly downstream asset |
| 5.2 Asset checks | Checks attached to assets, blocking vs warning checks, freshness checks | Add 5 checks that stop bad data from reaching a gold asset |
| 5.3 Automation | Schedules, sensors, declarative automation conditions (materialise when upstream updates, on cron, when missing) | Replace three schedules with automation conditions; compare run counts |
| 5.4 Resources and I/O managers | Dependency injection for clients, environment-specific configuration, I/O managers for storage | Run the same code against DuckDB locally and a warehouse in staging |
| 5.5 Projects at scale | Components and the `dg` CLI, code locations, branch deployments | Split a project into two code locations owned by two teams |

**Check your understanding:** (1) When does a partition mapping between daily and monthly assets cause unexpected rematerialisations? (2) Why should some checks block downstream materialisation and others only warn? (3) What does dependency injection buy you in tests?

### Chapter 6 · Prefect, Kestra and durable execution (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Prefect | Flows and tasks as Python functions, results persistence and caching, transactions, events and automations, work pools | Port one Airflow DAG to Prefect; compare failure handling |
| 6.2 Declarative YAML orchestration | Kestra flows (used in the Data Engineering Zoomcamp), triggers, plugins; trade-offs of YAML vs code | Build the ingestion step of P1 in Kestra |
| 6.3 Durable execution | Workflows as code with replay and persisted history (Temporal); long waits, human approvals, agent loops; where it fits data work and where it does not (deeper in [BE501](../../../backend_engineering/year_5/BE501_frontier_seminar_durable_execution_serverless/README.md)) | Model a document-review workflow with a 3-day human approval step |
| 6.4 Choosing | Team skills, scale, multi-tenancy, observability, managed options, lock-in | Write a decision record for three organisations |

**Check your understanding:** (1) Which features of durable execution do batch data pipelines rarely need, and which do AI ingestion pipelines often need? (2) What does Prefect's transaction concept protect against? (3) When is YAML-defined orchestration a good fit?

### Chapter 7 · Dependency design (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Task granularity | One task per table vs per step vs per pipeline; retry cost; observability | Split a 2-hour monolithic task into restartable steps; measure recovery time after a failure at 90% |
| 7.2 Cross-pipeline dependencies | Asset-based triggers, external task sensors, shared-table hazards, ownership boundaries between teams | Replace a cross-team "wait until 4 a.m." with an asset dependency |
| 7.3 Critical paths | Longest path to a deadline, slack, the one slow upstream that delays everything | Compute the critical path for a 40-node graph and shorten it by 30% |
| 7.4 Declarative graphs inside tools | dbt's DAG, Spark Declarative Pipelines: let the tool order its own steps, orchestrate the tool as one asset group | Orchestrate a 60-model dbt project as assets with per-model visibility |

**Check your understanding:** (1) What is the cost of making tasks too small? (2) Why are time-based waits between teams a reliability bug? (3) Where should the boundary between orchestrator and transformation tool sit?

### Chapter 8 · Freshness objectives and alerting (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Data SLOs | Freshness, completeness and correctness objectives per asset; error budgets for data | Write SLOs for 5 assets with named consumers and deadlines |
| 8.2 Deadlines in tools | Airflow Deadline Alerts (replacing the older SLA feature, with a migration guide), Dagster freshness checks, `dbt freshness` | Implement the same deadline in Airflow and Dagster |
| 8.3 Alert design | Paging vs ticketing, routing by ownership, deduplication, alert fatigue | Cut a noisy alert set from 40 to 8 meaningful alerts |
| 8.4 Runbooks and on-call | Runbook structure, safe re-run instructions, escalation; blameless reviews | Write runbooks for the 3 most likely P2 failures |

**Check your understanding:** (1) Why should a freshness alert be tied to the consumer's deadline, not the job's schedule? (2) What makes a runbook step safe for someone woken at 3 a.m.? (3) When should a data incident page someone?

### Chapter 9 · Testing pipelines (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 DAG integrity tests | Import errors, cycles, missing owners and retries, forbidden top-level code, parse-time budgets | Write a test suite that fails on 6 common DAG mistakes |
| 9.2 Task logic tests | Pure functions, fixtures, mocking clients through resources | Reach 90% branch coverage on task logic without a running scheduler |
| 9.3 Integration tests | Containers for PostgreSQL, MinIO and Kafka (Testcontainers); end-to-end runs on sample data | Run the whole pipeline in CI in under 10 minutes |
| 9.4 Data tests in the pipeline | dbt data and unit tests, asset checks, reconciliation steps (deepened in [DEN401](../../year_4/DEN401_data_quality_observability_and_data_contracts/README.md)) | Add a gate that blocks publication on failed checks |
| 9.5 CI/CD and environments | Dev, staging and production; branch deployments; promoting code vs data; schema migrations with pipelines | Ship a breaking change through staging with a rollback plan |

**Check your understanding:** (1) Why do data pipelines need data tests even with 100% code coverage? (2) What should differ between staging and production, and what must not? (3) How do you roll back a pipeline change that already wrote bad data?

### Chapter 10 · Running orchestrators in production (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Deploying Airflow | Kubernetes with the official Helm chart, executor choice, scheduler high availability, metadata database tuning | Deploy on kind; run 500 tasks concurrently; find the bottleneck |
| 10.2 Secrets and connections | Secrets backends, least-privilege connections, rotating credentials | Move all connections to a secrets backend; audit what each can access |
| 10.3 Upgrades | Airflow 2 to 3 migration: removed features, provider changes, automated checks (Ruff's `AIR` rules) | Migrate a 20-DAG Airflow 2 project and keep its tests green |
| 10.4 Cost and multi-tenancy | Worker sizing, autoscaling, isolating teams, cost per pipeline | Attribute one month of orchestration cost to teams |

**Check your understanding:** (1) What fails first when an Airflow deployment grows from 50 to 5,000 DAGs? (2) Why should the orchestrator's credentials be narrower than an engineer's? (3) What is risky about upgrading the orchestrator and the DAGs in one change?

### Chapter 11 · AI in and around pipelines (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Generated pipelines | What assistants get right (boilerplate, operators) and wrong (time handling, idempotency, retries on side effects) | Review 5 AI-generated DAGs with the Chapter 4 checklist |
| 11.2 Model calls as pipeline steps | Rate limits, retries with backoff, cost caps, caching results, non-deterministic outputs, versioning prompts and models | Add an LLM classification step to a pipeline with a cost cap and cached results |
| 11.3 Agents operating pipelines | Letting an agent re-run tasks or open tickets: permissions, approval gates, audit logs ([OV12](../../../../04_overlaps/OV12_agent_infrastructure_platform/README.md) goes deeper) | Give an agent read-only access plus one approved action; log every call |
| 11.4 Capstone review | Design review of P3 | Present and defend P3 |

**Check your understanding:** (1) Why does an LLM step break the "same input, same output" rule, and how do you restore reproducibility? (2) Which pipeline actions should never be automated without a human approval? (3) What evidence would convince you that an AI-generated DAG is safe to backfill?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Cron to graph | Dependency graph and failure map |
| 2 | 2 | Lab 2 · Airflow from the inside | Traced task lifecycle |
| 3 | 2 | Lab 3 · Time and runs | Run predictions vs actual; **P1 due** |
| 4 | 3 | Lab 4 · Assets and events | Event-triggered DAG |
| 5 | 4 | Lab 5 · Idempotency and backfill | 90-day backfill report |
| 6 | 5 | Lab 6 · Dagster assets and partitions | Partitioned asset graph |
| 7 | 5 | Lab 6 (cont.) | Mid-term (AI off): runs, intervals, idempotency |
| 8 | 6 | Lab 7 · Prefect, Kestra, durable execution | Port and comparison |
| 9 | 7 | Lab 8 · Critical path | Shortened graph; **P2 due** |
| 10 | 8 | Lab 9 · Deadlines and alerts | SLOs and runbooks |
| 11 | 9 | Lab 10 · Testing pyramid in CI | Green CI pipeline |
| 12 | 10 | Lab 11 · Airflow 2 → 3 migration | Migrated project |
| 13 | 11 | Lab 12 · LLM step with cost cap | Cost and cache report |
| 14 | 11 | Design review | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** DAG and asset boilerplate; translating a pipeline between Airflow, Dagster and Prefect; writing integration-test scaffolding with containers; drafting runbooks from your notes; explaining an unfamiliar provider's operator. Tools: Claude Code, GitHub Copilot, Cursor; dbt v2's language server and agent skills for dbt work; vendor assistants in managed services.
- **Do without AI (drills):** predicting which runs a schedule creates (Lab 3 and the mid-term); finding hidden non-determinism (Chapter 4); computing a critical path; deciding whether a step is safe to retry. These are judgement calls that fail silently when they are wrong.
- **Verify AI output by:** (1) running every DAG twice for the same interval and diffing outputs; (2) running a backfill over a range that includes a known late-data day; (3) reading the rendered run parameters for each task; (4) the DAG integrity test suite from Chapter 9; (5) checking that each API and import exists in your exact Airflow or Dagster version. Airflow 3 removed or moved many Airflow 2 imports and features.
- **Where AI still fails here (show it yourself):** ask an assistant for "a daily Airflow DAG that loads yesterday's orders into the warehouse". Record whether it uses `datetime.now()` instead of the data interval, appends instead of overwriting the partition, sets retries on a step with external side effects, sets `catchup` without thinking about the start date, or uses Airflow 2 import paths and SLA parameters. Keep the log. It becomes your review checklist.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–12 | 25% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 20% |
| Oral defence of P3 | 10% |

**Mastery gate.** You pass when you can, without AI: (1) given a schedule, start date and catchup setting, list exactly which runs will be created and with which data intervals; (2) take a provided non-idempotent pipeline, make it safe to retry and backfill, and prove it by running a 30-day backfill twice with identical outputs; (3) during a simulated incident (an upstream table arrives 5 hours late and contains a bad day), restore correct downstream data before a stated deadline and write the restatement note for consumers.

## Industry reality

Airflow was started in October 2014 by Maxime Beauchemin at Airbnb and is now an Apache project. Version 3.3.2 shipped in September 2026, and the 2.11 line still received a release in March 2026. Managed Airflow is offered by AWS (MWAA), Google (Cloud Composer) and Astronomer. Dagster's asset-centric model and Prefect's Python-native flows are common in newer teams. Transformation tools are absorbing more of the graph: dbt v2 statically analyses every model, and Spark Declarative Pipelines plan dataset dependencies themselves. Razorpay's public description shows typical scale for a large Indian fintech: over 3,000 Airflow workflows, with dbt running SQL transformations on EMR (2026).

**Interview questions from this course**

1. *"What does it mean for a task to be idempotent, and how do you make a daily load idempotent?"* A strong answer covers deterministic inputs (the data interval, not the clock), partition overwrite or keyed `MERGE`, no side effects without idempotency keys, and a test that runs the task twice.
2. *"Walk me through how Airflow decides to run a task."* Cover DAG parsing, schedules or timetables and data intervals, run creation, dependency and trigger-rule evaluation, pools and concurrency, the executor and workers, and what changed in Airflow 3 (task execution interface, versioning, assets).
3. *"We need to backfill two years after fixing a bug. How?"* Cover impact analysis through lineage, the order of reprocessing, concurrency caps to protect the warehouse, validating a sample before the full run, communicating restatements, and cost.
4. *"Sensors or event-driven triggers?"* Cover worker slots held by poking sensors, reschedule mode, deferrable operators, asset events and watchers, failure modes of missed events, and reconciliation as a safety net.
5. *"How do you test a data pipeline?"* Cover DAG integrity, unit tests of task logic, integration tests with containers, data tests and asset checks, CI/CD with environments, and how to roll back data, not just code.

## Resources (free first)

- **Course:** [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp), workflow orchestration module (Kestra, free).
- **Documentation:** Airflow [best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html), [assets](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/assets.html), [backfill](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/backfill.html), [Deadline Alerts](https://airflow.apache.org/docs/apache-airflow/stable/howto/deadline-alerts.html), [project history](https://airflow.apache.org/docs/apache-airflow/stable/project.html); Dagster [assets](https://dagster.io/docs/guides/build/assets) and [asset checks](https://dagster.io/docs/guides/test/asset-checks); Prefect [transactions](https://docs.prefect.io/v3/concepts/transactions); [Kestra](https://kestra.io/docs); [Temporal](https://temporal.io/); [Spark Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html); [dbt](https://docs.getdbt.com/).
- **Essay:** Maxime Beauchemin, ["Functional Data Engineering: a modern paradigm for batch data processing"](https://maximebeauchemin.medium.com/functional-data-engineering-a-modern-paradigm-for-batch-data-processing-2327ec32c42a) (2018).
- **Datasets for pipelines:** [NYC TLC trip records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) (monthly releases with a delay of about two months, a realistic late-arrival pattern); [data.gov.in](https://www.data.gov.in/) APIs; [GH Archive](https://www.gharchive.org/) hourly files.
- **Paid, worth it:** Harenslak and de Ruiter, *Data Pipelines with Apache Airflow*, 2nd ed. (Manning); Reis and Housley, *Fundamentals of Data Engineering* (O'Reilly, 2022).

## Sources

All checked October 2026.

- Apache Airflow, "Airflow 3.0 is here" (22 Apr 2025). https://airflow.apache.org/blog/airflow-three-point-oh-is-here/
- Apache Airflow announcements (3.3.2 on 17 Sep 2026; 2.11.2 on 14 Mar 2026). https://airflow.apache.org/announcements/
- Apache Airflow, project history ("started in October 2014 by Maxime Beauchemin at Airbnb"). https://airflow.apache.org/docs/apache-airflow/stable/project.html
- Apache Airflow, Deadline Alerts and migrating from SLA (3.3.2 docs). https://airflow.apache.org/docs/apache-airflow/stable/howto/deadline-alerts.html
- AWS Big Data Blog, Razorpay on Amazon EMR (9 Mar 2026). https://aws.amazon.com/blogs/big-data/how-razorpay-achieved-11-performance-improvement-and-21-cost-reduction-with-amazon-emr/
- Fivetran, "Fivetran and dbt Labs complete merger" (1 Jun 2026). https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents
- dbt, "Upgrading to v2". https://docs.getdbt.com/docs/dbt-versions/dbt-upgrade/upgrading-to-v2
- Apache Spark 4.1.0 release notes (Spark Declarative Pipelines). https://spark.apache.org/releases/spark-release-4.1.0.html
- DataTalksClub, Data Engineering Zoomcamp (modules; next cohort January 2027). https://github.com/DataTalksClub/data-engineering-zoomcamp

_Last reviewed: 2026-10_
