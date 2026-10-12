# DEN302 · Labs and projects

Labs run on PySpark 4.x in local mode or on a small Kubernetes cluster (kind or k3d) on a laptop with 16 GB of RAM. P3 can use any managed Spark service under a written budget cap. Labs 1, 3, 6 and 8 are done without AI assistants. Every performance claim needs before and after evidence: the plan, stage metrics, and run time over at least three runs.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Jobs, stages and the UI | Predict jobs, stages and shuffles for 5 programs, then verify in the UI | Prediction table with explanations of every miss | 3 h |
| 2 · Schemas and ANSI semantics | Read GH Archive JSON with and without explicit schemas; find behaviour changes under ANSI mode | Timing table and three ANSI-difference examples | 3 h |
| 3 · Plan reading | Annotate analysed, optimised and physical plans; record AQE decisions with AQE on and off | Annotated plans for 4 queries | 4 h |
| 4 · Shuffle sweep and small files | Sweep `spark.sql.shuffle.partitions`; fix a 20,000-file write | Run-time plot, file-count before and after | 5 h |
| 5 · Join strategies | Benchmark broadcast, shuffle hash, sort-merge and storage-partitioned joins on generated tables | Decision table with thresholds measured on your machine | 5 h |
| 6 · Skew clinic | Find and fix a hot key with AQE, salting and hot-key isolation | Longest-task time for each approach and a recommendation | 5 h |
| 7 · Memory and caching | Reproduce driver and executor OOMs; show one harmful and one helpful `cache()` | Reproduction scripts and fixes | 4 h |
| 8 · Event-log forensics | Diagnose 6 recorded event logs in the History Server without seeing the code | One paragraph per log: symptom, evidence, cause, fix | 4 h |
| 9 · Arrow and UDFs | Replace a row-wise Python UDF with built-ins, then with a vectorised UDF | Speed-up table and profiler output | 3 h |
| 10 · Kill mid-write | Kill jobs writing plain Parquet and Iceberg; inspect what readers see | Evidence of partial output and the table-format fix | 3 h |
| 11 · Single-node shoot-out | Same pipeline on Spark (local), DuckDB and Polars at 1, 10 and 100 GB | Benchmark plot and decision record | 5 h |
| 12 · Tests in CI | Unit, property and volume tests with a shuffle-bytes regression gate | Green CI run and one intentionally failing run | 4 h |

## Projects

### P1 · GitHub activity rollups (L1, ~6 hours)

**Real-world inspiration:** developer-analytics products and open-source health dashboards aggregate GitHub events daily. [GH Archive](https://www.gharchive.org/) publishes every public GitHub event as hourly gzipped JSON files since 2011.

**What to build:** a PySpark job that reads 7 days of hourly files with an explicit schema and produces three daily Parquet tables partitioned by date:

- events by type;
- the top 1,000 repositories by distinct actors;
- new contributors per repository.

Bad records go to a quarantine path with a reason.

**Acceptance criteria:**
- Counts per event type for one chosen hour match a reference computed with DuckDB directly on the raw JSON, exactly.
- Re-running the job for any day replaces that day's partition and leaves other days untouched (checked by file listing and row counts).
- Each output partition has between 1 and 8 files, each larger than 32 MB where the data allows.
- The README shows the physical plan of the heaviest query, with each exchange explained.

**Stretch goals:** a bot filter (actor names ending in `[bot]` plus a rate rule) and its effect on the rankings; the same job in DuckDB with a time comparison.

**What it proves to an employer:** you can write a clean, partitioned, re-runnable Spark job and explain its plan.

### P2 · Five years of city trips under a time budget (L2, ~15 hours)

**Real-world inspiration:** mobility platforms compute origin–destination matrices, driver earnings and demand patterns over years of trips. Razorpay's 2026 write-up shows how tuning and instance choice decide the bill for a large Indian batch platform ([AWS blog](https://aws.amazon.com/blogs/big-data/how-razorpay-achieved-11-performance-improvement-and-21-cost-reduction-with-amazon-emr/)).

**What to build:** a batch job over 5 years of NYC TLC yellow and HVFHV Parquet files. Join the trips to the taxi-zone lookup and to daily weather from [NOAA GHCN-Daily](https://registry.opendata.aws/noaa-ghcn/) (Central Park station). Produce:

- an hourly origin–destination matrix by borough pair;
- driver pay per hour by HVFHV licensee and month;
- trip demand by weather band (dry, rain, snow).

Start from a deliberately naive version (provided) that uses Python UDFs, a skewed join on the airport zones and unpartitioned output.

**Acceptance criteria:**
- **Correctness:** all three outputs match the naive version's results exactly (`assertDataFrameEqual`, order-insensitive) on a 3-month sample, and totals match on the full run.
- **Speed:** the tuned job runs at least 5× faster than the naive one on the same hardware, measured as the median of 3 runs.
- **Evidence:** a tuning log with at least 6 entries (hypothesis, change, measured effect), including one change that did not help.
- **Skew:** the longest task in the heaviest stage takes at most 3× the median task time, shown with Stages-tab screenshots or event-log metrics.
- **Output:** files are 64–512 MB with no partition holding more than 50 files, and reads of one month prune all other months.

**Stretch goals:** run on a managed service and report cost per run on two instance families; a storage-partitioned join version using Iceberg bucketed tables.

**What it proves to an employer:** you can take a slow, real job and make it fast with measured, explainable changes, which is most of what senior Spark work is.

### P3 · GitHub ecosystem batch platform (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** company data platforms run hundreds of daily Spark jobs with backfills, schema drift, hot keys and cost limits. Razorpay runs over 3,000 workflows on a Spark and Delta Lake platform. GH Archive's event schema has changed over the years (the Timeline API until 2014, the Events API from 2015), so the data drifts the way real sources do.

**What to build:** a bronze/silver/gold batch platform over at least 6 months of GH Archive data (larger if your budget allows):

- **Bronze:** raw hourly files registered in an Iceberg or Delta table.
- **Silver:** typed, deduplicated events with the payload as VARIANT or extracted structs, plus a schema-drift report.
- **Gold:** daily repository health metrics (active contributors, issue response times, release cadence) and a weekly language-ecosystem table.

Build the pipeline twice: once as hand-written jobs, and once as Spark Declarative Pipelines. Include a backfill command, data tests, a CI workflow with a shuffle-bytes regression gate, and a runbook.

**Acceptance criteria:**
- **Idempotency and backfill:** backfilling any 30-day range twice produces identical gold tables (checked with a table hash). A job killed mid-run leaves no partial data visible to readers.
- **Correctness:** gold metrics for 5 sampled repositories match values computed independently with DuckDB on raw files.
- **Skew:** the job handles the most active actors and repositories without any task exceeding 5× the stage median.
- **Cost and time:** a daily incremental run finishes in under 20 minutes on your chosen cluster, and the whole project stays within a written budget cap (for example, $30 of cloud spend), with cost per daily run reported.
- **Comparison:** a benchmark of the gold queries on Spark vs DuckDB over the gold tables, with a recommendation for which engine should serve them.
- **Operations:** a runbook covering three failure scenarios (late hour files, a schema change, an out-of-memory error), each tested by injecting the failure.
- **Write-up:** design document, tuning log, a comparison of the hand-written and declarative versions (lines of code, failure behaviour, run time), and a 5-minute walkthrough of the Spark UI for one run.

**Stretch goals:** run gold queries on a native engine (Gluten with Velox, or DataFusion Comet) and report the speed-up; a per-table cost attribution report; publish one gold table as an open dataset with a data dictionary.

**What it proves to an employer:** you can build and operate a production-shaped batch platform: correct under retries and backfills, tuned with evidence, tested in CI, and costed.

## Feeds into

- [DEN402 Cloud Data Platforms](../../year_4/DEN402_cloud_data_platforms_snowflake_bigquery/README.md): the same jobs on Databricks, EMR and Fabric with cost comparison.
- [DEN305 Lakehouse Architecture](../DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md): P3's tables become the compaction and time-travel case study.
- [DEN304 Orchestration and Pipelines](../DEN304_orchestration_and_pipelines_airflow_and_dagster/README.md): P3's backfills move under Airflow or Dagster.
- [DEN501 Frontier Seminar](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md): vectorised and native execution internals.
