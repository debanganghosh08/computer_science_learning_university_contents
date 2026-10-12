# DEN304 · Labs and projects

Labs run locally with Docker Compose (Airflow 3.x, Dagster, PostgreSQL, MinIO, DuckDB) or on a local Kubernetes cluster (kind) for Labs 10–11. Labs 3 and 5 are done without AI assistants. Every pipeline you submit must pass the integrity test suite from Lab 10, and every "idempotent" claim must be backed by a run-twice diff.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Cron to graph | Turn 6 cron scripts with hidden dependencies into a graph; list every failure the cron setup hides | Graph, failure map, and a one-page migration plan | 3 h |
| 2 · Airflow from the inside | Run Airflow 3; trace one task through scheduler, executor, worker and API server logs | Annotated log excerpts and an architecture sketch | 3 h |
| 3 · Time and runs | Predict runs and data intervals for 5 schedule, start-date and catchup configurations | Predictions, actual runs, and an explanation of each miss | 3 h |
| 4 · Assets and events | Trigger a DAG from a file-landing event and from an upstream asset | Working event-driven pipeline; latency vs a 5-minute poll | 4 h |
| 5 · Idempotency and backfill | Fix 5 hidden non-determinism bugs; backfill 90 days twice under a concurrency cap | Fixed DAG, identical-output proof, warehouse load chart | 5 h |
| 6 · Dagster assets and partitions | Daily and regional partitions, a monthly downstream asset, 5 asset checks, automation conditions | Asset graph screenshot, check results, run-count comparison | 6 h |
| 7 · Prefect, Kestra, durable execution | Port one pipeline to Prefect and one step to Kestra; model a 3-day approval with a durable workflow | Code and a comparison table (failure handling, visibility, effort) | 5 h |
| 8 · Critical path | Compute and shorten the critical path of a 40-node graph | Before/after path length and the changes made | 3 h |
| 9 · Deadlines and alerts | Freshness SLOs, Airflow Deadline Alerts, Dagster freshness checks, 3 runbooks | SLO table, alert rules, runbooks | 4 h |
| 10 · Testing pyramid in CI | Integrity, unit, container-based integration and data tests in CI under 10 minutes | Green CI run and one intentionally failing run per level | 6 h |
| 11 · Airflow 2 → 3 migration | Migrate a 20-DAG Airflow 2 project; use Ruff's `AIR` rules | Migrated project with tests passing and a list of every change | 5 h |
| 12 · LLM step with a cost cap | Add a model-based classification step with caching, retries and a spend limit | Cost per run, cache hit rate, and reproducibility check | 4 h |

## Projects

### P1 · Monthly trip-file ingestion (L1, ~6 hours)

**Real-world inspiration:** NYC's TLC publishes trip records monthly, typically about two months late ([TLC](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)). Late, irregular publication like this is normal for government and partner data feeds.

**What to build:** an Airflow 3 DAG that ingests yellow and green trip files from January 2024 onwards into date-partitioned Parquet with DuckDB. It must:

- wait for each month's file with a deferrable check rather than a poking sensor;
- validate row counts and schema;
- write one partition per month;
- record each load in an audit table.

**Acceptance criteria:**
- Deploying with catchup creates exactly one run per month, with correct data intervals, which you predict in the README before deploying.
- Re-running any month produces identical files (same row count and content hash) and one audit row marked as a re-run.
- A month whose file is not yet published waits without holding a worker slot, and fails with a clear message after a set timeout.
- The DAG passes the integrity tests (no top-level I/O, retries set, owner set, parse time under 1 second).

**Stretch goals:** the same pipeline in Dagster with monthly partitions; a notification when a new month is published.

**What it proves to an employer:** you understand schedules, data intervals and idempotent partition loads, which are the basics every data team checks first.

### P2 · Partitioned asset platform for public data (L2, ~15 hours)

**Real-world inspiration:** platform teams expose data as assets with owners, freshness objectives and checks rather than as opaque jobs. Government open-data APIs ([data.gov.in](https://www.data.gov.in/)) and event archives ([GH Archive](https://www.gharchive.org/)) arrive late, have gaps, and are sometimes corrected.

**What to build:** a Dagster project with two sources:

- **GH Archive:** hourly partitions feed daily repository metrics, which feed weekly ecosystem metrics.
- **data.gov.in:** a daily mandi price resource loaded through its API.

Use time partitions with partition mappings, asset checks (blocking and warning), automation conditions instead of fixed schedules, resources that switch between DuckDB (local) and a warehouse (staging), and freshness checks with alerts. Then implement the GH Archive daily asset again in Airflow 3 using assets, and compare the two tools.

**Acceptance criteria:**
- **Backfill:** a 90-day backfill of hourly partitions completes under a concurrency cap of 8. Running it a second time produces identical daily and weekly outputs (table hash).
- **Late data:** a deliberately delayed hour triggers rematerialisation of the affected day and week only, verified from run history.
- **Checks:** a planted bad partition (duplicate events, negative counts) is blocked from the weekly asset by a blocking check. A warning check reports a 30% volume drop without blocking.
- **Freshness:** freshness objectives are defined for every asset. Stopping the source for 6 hours fires exactly one alert per affected asset.
- **Environments:** the same code runs locally on DuckDB and in staging against a warehouse, with no code changes, only resource configuration.
- **Comparison:** a 2-page write-up compares Dagster and Airflow for this project (lines of code, backfill behaviour, observability, failure handling).

**Stretch goals:** branch deployments in CI; an OpenLineage integration that emits lineage events (preview of [DEN404](../../year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md)).

**What it proves to an employer:** you can build an asset-centric platform with partitions, checks and freshness objectives that recovers from late and bad data without manual clean-up.

### P3 · Production orchestration with deadlines (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** a company's morning reports depend on a chain of database replication, batch jobs, dbt models and increasingly AI enrichment steps, all due before business hours. Razorpay describes over 3,000 Airflow workflows with dbt on its platform ([AWS blog, 2026](https://aws.amazon.com/blogs/big-data/how-razorpay-achieved-11-performance-improvement-and-21-cost-reduction-with-amazon-emr/)). The deadlines and failure scenarios below are illustrative.

**What to build:** orchestration, in Airflow 3 or Dagster on Kubernetes, for a platform that combines:

- CDC-landed operational tables (reuse DEN303 P2, or a provided snapshot feed);
- a daily Spark job (reuse DEN302 P2 or P3);
- a dbt project of at least 40 models (reuse DEN301 work);
- an LLM step that classifies free-text records (for example, GitHub issue titles) with caching, retries and a daily spend cap;
- publication of gold tables only after checks pass.

Define data SLOs with a 06:00 IST deadline for three gold assets. Implement deadline alerts and runbooks. Run CI/CD across dev, staging and production namespaces. Include a backfill command with impact analysis.

**Acceptance criteria:**
- **Deadline reliability:** over 14 simulated days, with 5 injected failures (a late upstream, a failed Spark executor, a bad dbt model change, an LLM API outage, a full disk), the gold assets meet the 06:00 deadline on at least 12 days. Every miss is detected by an alert at least 30 minutes before the deadline.
- **Idempotency:** a 60-day backfill run twice produces identical gold tables, and the LLM step's cached outputs make the second run cost at most 5% of the first.
- **Safety:** no gold table is published when a blocking check fails. A provided bad change to a dbt model is stopped in staging by CI.
- **Recovery:** each injected failure has a tested runbook. A teammate following only the runbook restores service in a dry run.
- **Cost:** orchestration and LLM spend per day is reported, and the LLM step never exceeds its cap (tested by forcing cache misses).
- **Write-up:** design document (graph, ownership, SLOs, failure modes), incident reports for 2 of the injected failures, and a 5-minute recorded demo of a backfill with impact analysis.

**Stretch goals:** event-driven triggering end to end, with no schedules except the deadline checks; OpenLineage emission and a lineage view; a read-only operations agent that drafts incident summaries, with every action logged.

**What it proves to an employer:** you can run a deadline-bound data platform: correct under retries and backfills, protected by checks, observable, recoverable by others, and cost-capped even with AI steps in the graph.

## Feeds into

- [DEN404 Data Governance, Lineage and Privacy Engineering](../../year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md): lineage from these pipelines powers impact analysis and audits.
- [DEN401 Data Quality, Observability and Data Contracts](../../year_4/DEN401_data_quality_observability_and_data_contracts/README.md): checks and SLOs become contracts and incident processes.
- [OV06A Building a Modern Data Platform](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06A_building_a_modern_data_platform/README.md): P3 is the orchestration layer of a full platform.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): runbooks and on-call practice carry straight into co-op work.
