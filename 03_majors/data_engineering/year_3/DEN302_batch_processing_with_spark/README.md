# DEN302 · Batch Processing with Spark

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [DEN402](../../year_4/DEN402_cloud_data_platforms_snowflake_bigquery/README.md), [DEN305](../DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md), [DEN501](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md) |

Part of the [Data Engineering major](../../README.md). [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) Chapter 10 introduced MapReduce, RDD lineage, shuffles and salting in one week. This course spends a semester on making large batch jobs correct, fast and cheap, and on knowing when a single machine beats a cluster. Data scientists meet Spark for exploration in [DSC303](../../../data_science/year_3/DSC303_data_wrangling_at_scale_pandas_polars_and_spark/README.md); this course is about production jobs.

## Why this course matters now

Spark is still the default engine for large batch jobs on open data. Apache Spark 4.0 shipped in May 2025 with ANSI SQL semantics on by default. Spark 4.1 (December 2025) added declarative pipelines, a real-time streaming mode and a generally available VARIANT type. Spark 4.2 (July 2026) made Arrow-optimised Python UDFs the default and added a searchable SQL plan view to the web UI. The bill for this work is large and visible. Razorpay reports processing over 1 PB a day with Spark and Delta Lake, and says that moving to Amazon EMR with Spot task nodes, Graviton instances and Spark tuning cut cost by 21% and improved performance by 11% (2026). Yet much data is small. A founding BigQuery engineer recalls that, for customers spending over $1,000 a year, 90% of queries processed under 100 MB. AI assistants (Databricks Assistant, Claude Code, GitHub Copilot) write PySpark quickly. They also call `collect()` on large data, wrap built-in functions in Python UDFs, cache everything and repartition to one file. Reading a physical plan, finding the skewed task in the Spark UI, and deciding that the job should not be on Spark at all are still human skills.

## Learning outcomes

By the end you can:

1. **Explain** how a Spark application becomes jobs, stages and tasks, and **predict** where shuffles occur from a DataFrame program.
2. **Read** a physical plan from `explain("formatted")`, and **identify** the Catalyst rules and adaptive query execution (AQE) decisions that shaped it.
3. **Choose** a join strategy (broadcast hash, shuffle hash, sort-merge, storage-partitioned) for given table sizes, and **force or prevent** it with evidence.
4. **Diagnose** skew, spill, small files and driver bottlenecks in the Spark UI and event logs, and **fix** each with a measured speed-up.
5. **Size** executors and partitions for a stated cluster and job, and **calculate** the cost per run.
6. **Write** idempotent batch jobs that overwrite partitions atomically, evolve schemas safely and can be backfilled.
7. **Compare** PySpark with Scala, built-in functions with pandas and Arrow UDFs, and Spark with DuckDB, Polars and Ray Data, using benchmarks you ran.
8. **Test** Spark jobs with unit, property and volume tests, and **audit** AI-generated Spark code for anti-patterns.

## Chapters and lessons

### Chapter 1 · From MapReduce to Spark's execution model (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Why Spark replaced MapReduce | In-memory reuse, lineage-based recovery, DAG scheduling (RDD paper, NSDI 2012) | Re-implement a 3-stage MapReduce job as one Spark job; count disk writes in each |
| 1.2 Driver, executors, cluster managers | Standalone, YARN and Kubernetes; deploy modes; dynamic allocation | Run the same job in local mode and on a 3-node Kubernetes cluster (kind) |
| 1.3 Jobs, stages, tasks | Actions trigger jobs; wide dependencies cut stages; one task per partition | Predict the stage count for 5 programs, then check in the UI |
| 1.4 Spark Connect | Client-server architecture (Spark 3.4+); thin clients in Python, Scala, Go, Rust and Swift; what runs where | Run a PySpark Connect client against a remote server; find which process executes the plan |

**Check your understanding:** (1) Why does lineage make recomputation cheaper than replication for most batch data, and when does it not? (2) Which of `map`, `filter`, `groupBy`, `join`, `union` create a stage boundary, and under what condition does a join not? (3) What can a Spark Connect client no longer do that a classic driver could?

### Chapter 2 · DataFrames and Spark SQL (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 From RDD to DataFrame | Schemas, column expressions, lazy evaluation, actions vs transformations; why typed columns enable optimisation | Rewrite an RDD word count and a join as DataFrames; compare plans and run time |
| 2.2 Reading data | Explicit schemas vs inference; Parquet, JSON, CSV and Avro; corrupt-record handling; `maxPartitionBytes` and file splits | Read a month of GH Archive JSON with and without an explicit schema; time both |
| 2.3 ANSI SQL semantics | ANSI mode on by default since 4.0: overflow and invalid casts raise errors instead of returning NULL | Find three queries whose results changed between ANSI off and on |
| 2.4 Semi-structured data | Structs, arrays, maps, `explode`, VARIANT (GA in 4.1) with shredding | Flatten nested event payloads two ways; compare bytes read |
| 2.5 SQL scripting and views | Spark SQL, temporary views, SQL scripting (GA in 4.1), when to use SQL vs DataFrame code | Port a 200-line PySpark job to SQL and back; keep tests green |

**Check your understanding:** (1) Why can schema inference on JSON read the whole dataset twice? (2) A job "worked" for years and fails after upgrading to Spark 4: what changed, and why is that a good thing? (3) When is VARIANT better than a fixed struct schema, and when is it worse?

### Chapter 3 · Catalyst, AQE and Tungsten (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Catalyst | Unresolved → analysed → optimised logical plan → physical plan; rule-based rewrites (predicate pushdown, column pruning, constant folding) (Spark SQL paper, SIGMOD 2015) | Annotate the four plan stages of a 3-table query |
| 3.2 Statistics and the cost-based optimiser | `ANALYZE TABLE`, column statistics, join reordering; why statistics go stale | Show a join order change after computing statistics |
| 3.3 Adaptive query execution | Runtime re-optimisation at stage boundaries: coalescing shuffle partitions, switching to broadcast, splitting skewed partitions | Run with AQE off and on; record each AQE decision from the plan |
| 3.4 Tungsten and code generation | Whole-stage code generation, binary row format, off-heap memory; where codegen stops (Python UDFs, some expressions) | Read the generated code for a filter-project-aggregate stage |
| 3.5 Native engines | Photon (Databricks, SIGMOD 2022), Apache Gluten with Velox, Apache DataFusion Comet: vectorised C++ or Rust execution under Spark's planner | Read Photon's evaluation section; list which operators gain most and why |

**Check your understanding:** (1) Why can't Catalyst push a filter through a Python UDF? (2) AQE converted your sort-merge join to a broadcast join at runtime: what information did it have that the planner lacked? (3) Why does vectorised execution help most on scans and aggregations?

### Chapter 4 · Partitions and shuffles (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Input partitions | File splits, row groups, `maxPartitionBytes`; the small-files problem on read | Read 100,000 small files vs 100 compacted files; compare task counts and time |
| 4.2 Shuffle mechanics | Sort-based shuffle, map output files, fetch, external shuffle service; push-based shuffle (LinkedIn's Magnet, VLDB 2020); checksum-based stage retry (4.1) | Measure shuffle read/write bytes for `groupBy` vs `reduceByKey`-style partial aggregation |
| 4.3 Shuffle partitions | `spark.sql.shuffle.partitions`, AQE coalescing, target partition size (~100–200 MB as a starting point) | Sweep partition counts from 8 to 4,000 on a 50 GB aggregation; plot run time |
| 4.4 `repartition` vs `coalesce` | Full shuffle vs merge; `repartition(col)` for writes; range partitioning | Fix a job that writes 20,000 tiny files with one `repartition` and justify the number |
| 4.5 Partitioned writes | `partitionBy`, dynamic partition overwrite, partition explosion, file-size targets | Write NYC TLC trips partitioned by month; count files and sizes |

**Check your understanding:** (1) Why is a shuffle the most expensive thing a Spark job does, in network, disk and failure terms? (2) When does `coalesce(10)` make a job slower than `repartition(10)`? (3) A write produced 3 million files: give the two settings or code changes you would check first.

### Chapter 5 · Join strategies (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Broadcast hash join | Size thresholds, driver memory, broadcast timeouts; hints | Find the size at which broadcasting stops paying on your cluster |
| 5.2 Sort-merge and shuffle hash joins | When each is chosen; spill behaviour; join keys with NULLs | Compare both on a 200 GB × 20 GB join |
| 5.3 Avoiding shuffles | Bucketing; storage-partitioned joins for V2 sources such as Iceberg; pre-partitioned data | Join two Iceberg tables bucketed on the same key; confirm no exchange in the plan |
| 5.4 Special joins | Range and interval joins, anti and semi joins, `NEAREST BY` top-K ranking join (4.2) | Join GPS points to time windows efficiently; then try a nearest-neighbour join |
| 5.5 Join correctness | Duplicate keys and row explosion, NULL-safe equality (`<=>`), data type mismatches that disable pushdown | Detect a planted row-explosion join with a pre-join key-uniqueness check |

**Check your understanding:** (1) Why can a broadcast join crash the driver even when executors have plenty of memory? (2) What must two tables share for a storage-partitioned join to skip the shuffle? (3) A join returns 40× more rows than expected: what do you check, in what order?

### Chapter 6 · Skew (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Seeing skew | Task-duration and shuffle-read distributions in the Stages tab: max vs median, stragglers | Find the hot key in a GH Archive job (bots and very active repositories) |
| 6.2 AQE skew handling | Skewed partition detection thresholds; what it can and cannot split | Show AQE fixing one skewed join and failing on a skewed aggregation |
| 6.3 Salting and hot-key isolation | Salting the large side and exploding the small side; separating the top-k keys; two-phase aggregation | Cut a skewed join's longest task from minutes to seconds; report the speed-up |
| 6.4 Skew at the source | Partition skew from upstream (one huge file, one huge date); fixing layout instead of code | Fix a skewed daily partition by sub-partitioning on hour |

**Check your understanding:** (1) Why does adding executors not speed up a job dominated by one skewed task? (2) What does salting cost, and when is it not worth it? (3) How would you detect a new hot key before it breaks tonight's job?

### Chapter 7 · Memory, caching and the Spark UI (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Unified memory | Execution vs storage memory, overhead memory, off-heap; spill to disk; driver vs executor OOM | Reproduce a driver OOM (`collect`) and an executor OOM (huge partition); fix both |
| 7.2 Caching and checkpoints | `cache`/`persist` levels, when caching hurts, eviction, `checkpoint` vs `localCheckpoint` to truncate lineage | Show a job that gets slower with `cache()` and one that gets 5× faster |
| 7.3 The Spark UI in depth | Jobs, Stages, SQL/DataFrame (plan with metrics), Storage, Executors and Environment tabs; Spark 4.2's searchable plan view; event logs and the History Server | Diagnose 6 recorded event logs without the code |
| 7.4 Executor sizing | Cores per executor, memory per core, dynamic allocation, GC pauses; Spot and Graviton economics (Razorpay case) | Size a cluster for a 2 TB nightly job; compute cost per run on two instance types |
| 7.5 Tuning method | Measure, form a hypothesis, change one thing, re-measure; keep a tuning log | Tune a job end to end and present the log |

**Check your understanding:** (1) Why do most Spark OOMs come from data layout rather than memory settings? (2) When does `cache()` change results, not just speed? (3) The Executors tab shows high GC time on 2 of 50 executors: what does that suggest?

### Chapter 8 · Python and the JVM (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 How PySpark runs | Py4J to the JVM, Python worker processes, serialisation costs | Profile a Python UDF and a built-in function doing the same work |
| 8.2 Arrow | Columnar transfer, pandas UDFs, Arrow-optimised Python UDFs (default in 4.2), `toPandas` and `createDataFrame` costs | Rewrite a row-at-a-time UDF as a vectorised UDF; measure speed-up |
| 8.3 Python data sources and UDTFs | Custom readers and table functions in Python | Write a Python data source for a paginated public API |
| 8.4 Scala and Java | Datasets, typed APIs, library ecosystems; when JVM code still wins | Port one hot UDF to Scala and compare |

**Check your understanding:** (1) Why is a Python UDF a black box to Catalyst and Tungsten? (2) When is "PySpark vs Scala" a non-question for performance, and when is it decisive? (3) What does Arrow remove from the Python–JVM boundary?

### Chapter 9 · Writing data correctly (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Atomic output | Output committers, task and job commits, why object storage renames are not atomic; table formats as the fix | Kill a job mid-write to Parquet and to Iceberg; inspect what readers see |
| 9.2 Idempotent jobs | Deterministic inputs, partition overwrite, `MERGE` by key, no `now()` inside transforms | Make a daily job safe to run twice and to backfill 90 days |
| 9.3 Schema evolution | Adding, widening, renaming columns; schema enforcement on write | Evolve a table schema without breaking two downstream readers |
| 9.4 Declarative pipelines | Spark Declarative Pipelines (4.1): datasets and flows declared, Spark plans order, retries and checkpoints; Auto CDC (4.2) | Rebuild a 4-step job as a declarative pipeline; compare code size and failure behaviour |

**Check your understanding:** (1) Why can a job that "succeeded" leave partial output visible on S3-compatible storage without a table format? (2) List three hidden sources of non-determinism in a batch job. (3) What do declarative pipelines take away from you, and what do they give?

### Chapter 10 · When a single machine wins (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Data sizes in practice | Working sets vs total storage; recent-data access patterns; "Big Data is Dead" claims and their limits | Measure your project's real working set |
| 10.2 DuckDB and Polars | Vectorised in-process engines, out-of-core execution, Polars lazy and streaming modes | Run the same pipeline at 1, 10 and 100 GB on Spark (local), DuckDB and Polars |
| 10.3 Ray Data | Task-parallel pipelines for ML and unstructured data (images, documents, GPUs) | Run batch embedding on 100,000 documents with Ray Data (preview of [DEN403](../../year_4/DEN403_data_engineering_for_ai_unstructured_data/README.md)) |
| 10.4 Choosing | Cost, latency, operations burden, team skills, data growth; a decision checklist | Write a decision record: Spark or DuckDB for three stated workloads |

**Check your understanding:** (1) Where did the single-node engines in your benchmark stop winning, and what resource ran out? (2) Why can a cluster be cheaper even when it is slower? (3) Which workloads does Ray Data fit better than Spark?

### Chapter 11 · Testing and operating batch jobs (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Testing | Local `SparkSession` fixtures, `assertDataFrameEqual` (PySpark 3.5+), property-based tests with generated DataFrames, golden files | Write 15 tests for P2's job, including empty input and NULL keys |
| 11.2 Volume and performance tests | Synthetic data at production scale, regression thresholds on run time and shuffle bytes | Add a CI check that fails if shuffle bytes grow by over 20% |
| 11.3 Deployment targets | Kubernetes (Spark operator), Amazon EMR, Dataproc, Databricks; packaging dependencies | Deploy one job to two targets and compare start-up overhead |
| 11.4 Cost attribution and incident review | Cost per job, per table and per team; reading a failed job's logs; a short blameless review | Write a post-incident review for a job that missed its deadline |

**Check your understanding:** (1) Why do Spark unit tests on 10 rows miss most production failures, and what fills the gap? (2) How do you attribute cluster cost to individual jobs on shared clusters? (3) What belongs in a post-incident review of a late batch job?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Jobs, stages and the UI | Stage predictions vs actual |
| 2 | 2 | Lab 2 · Schemas and ANSI semantics | Read benchmark |
| 3 | 3 | Lab 3 · Plan reading | Annotated plans; **P1 due** |
| 4 | 4 | Lab 4 · Shuffle sweep | Partition-count plot |
| 5 | 4 | Lab 4 (cont.) | Small-files fix |
| 6 | 5 | Lab 5 · Join strategies | Join decision table |
| 7 | 6 | Lab 6 · Skew clinic | Mid-term (AI off): plans, stages, joins |
| 8 | 7 | Lab 7 · Memory and caching | OOM reproductions |
| 9 | 7 | Lab 8 · Event-log forensics | Six diagnoses; **P2 due** |
| 10 | 8 | Lab 9 · Arrow and UDFs | Speed-up report |
| 11 | 9 | Lab 10 · Kill-mid-write | Idempotency proof |
| 12 | 10 | Lab 11 · Single-node shoot-out | Benchmark and decision record |
| 13 | 11 | Lab 12 · Tests in CI | Test suite |
| 14 | 11 | P3 tuning and review | **P3 due** |
| 15 | Review | Live tuning exam | Final exam (AI off) + P3 oral |

## Working with AI in this course

- **Use AI for:** drafting PySpark from a clear specification; translating between PySpark, Scala and Spark SQL; generating synthetic skewed datasets; explaining an unfamiliar plan node or configuration; writing test fixtures. Tools: Claude Code, GitHub Copilot, Cursor; Databricks Assistant on Databricks; Spark's own `explain` output as context for the assistant.
- **Do without AI (drills):** predicting stages and shuffles from code; reading physical plans; diagnosing the six event logs in Lab 8; the mid-term and the live tuning exam. You cannot judge a tuning suggestion until you can read the evidence yourself.
- **Verify AI output by:** (1) reading `explain("formatted")` before running; (2) comparing shuffle bytes, spill and task-time distributions before and after a suggested change; (3) checking results with `assertDataFrameEqual` against a reference run; (4) running on production-sized data, because most anti-patterns only hurt at scale.
- **Where AI still fails here (show it yourself):** in Lab 9 and Lab 11, ask an assistant to "speed up" three provided jobs and log every suggestion. Typical failures to look for: `collect()` or `toPandas()` on large data, Python UDFs replacing built-in functions, blanket `cache()`, `repartition(1)` before writes, raising memory instead of fixing skew, and configuration names that do not exist in your Spark version. Record each suggestion, its measured effect, and whether the plan changed the way the assistant claimed.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–12 | 25% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Mid-term (AI off) | 10% |
| Live tuning exam (AI off) | 20% |
| Oral defence of P3 | 10% |

**Mastery gate.** You pass when you can, without AI: (1) given a job with three planted problems (a skewed join, a small-files read, a Python UDF on the hot path) and its Spark UI, make it at least 5× faster within 2 hours and explain each fix from evidence; (2) predict the number of stages and exchanges in an unseen physical plan and explain each one; (3) write a daily batch job that produces identical output when run twice or backfilled, and prove it with a test.

## Industry reality

Spark runs under most lakehouse platforms (Databricks, Amazon EMR, Google Dataproc, Microsoft Fabric's Spark runtime). Razorpay's 2026 account gives a concrete picture of a large Indian batch platform: over 20 TB ingested and over 1 PB processed daily, Airflow scheduling more than 3,000 workflows, dbt on EMR, and cost cut by 21% with Spot task nodes, Graviton and Spark tuning. Native vectorised engines under Spark's planner (Photon, Gluten with Velox, DataFusion Comet) show where performance work is going. Single-node engines such as DuckDB and Polars now handle many workloads that used to need a cluster.

**Interview questions from this course**

1. *"Explain narrow and wide transformations and what a stage is."* A strong answer defines both with examples, ties stages to shuffle boundaries, and explains the consequences for failures (recompute lineage up to the last shuffle) and for performance.
2. *"A join is slow and one task runs for 40 minutes. What do you do?"* Confirm skew in the Stages tab, identify the hot keys, check whether AQE skew handling applied, then use salting, isolation of hot keys or a broadcast of the small side. Quantify the result and add a monitor.
3. *"Broadcast or sort-merge join?"* Cover size thresholds, driver memory, AQE runtime switching, statistics, storage-partitioned joins, and what happens when the "small" table grows.
4. *"`repartition` vs `coalesce`, and how many output files should a job write?"* Cover full shuffle vs merge, skew from `coalesce`, target file sizes for downstream readers, and table-format compaction.
5. *"When would you not use Spark?"* Cover data size and working set, latency, operational cost, DuckDB or Polars for single-node work, warehouse SQL for analytics, and Ray Data for GPU-heavy unstructured pipelines. Support the answer with benchmark numbers.

## Resources (free first)

- **Course:** [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp), batch-processing module (free).
- **Documentation:** [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html); [tuning guide](https://spark.apache.org/docs/latest/tuning.html); [web UI](https://spark.apache.org/docs/latest/web-ui.html); [monitoring and event logs](https://spark.apache.org/docs/latest/monitoring.html); [ANSI compliance](https://spark.apache.org/docs/latest/sql-ref-ansi-compliance.html); [Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html); [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html); [DuckDB](https://duckdb.org/docs/stable/); [Polars](https://docs.pola.rs/); [Ray Data](https://docs.ray.io/en/latest/data/data.html).
- **Papers:** [Resilient Distributed Datasets](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/zaharia) (NSDI 2012); [Spark SQL](https://people.csail.mit.edu/matei/papers/2015/sigmod_spark_sql.pdf) (SIGMOD 2015); [Magnet push-based shuffle](https://www.vldb.org/pvldb/vol13/p3382-shen.pdf) (VLDB 2020); [Photon](https://people.eecs.berkeley.edu/~matei/papers/2022/sigmod_photon.pdf) (SIGMOD 2022); [MapReduce](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf) (OSDI 2004).
- **Projects to read:** [Apache Gluten](https://github.com/apache/incubator-gluten); [Apache DataFusion Comet](https://github.com/apache/datafusion-comet).
- **Datasets:** [GH Archive](https://www.gharchive.org/) (hourly JSON since 2011); [NYC TLC trip records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page); TPC-DS via [TPC](https://www.tpc.org/tpcds/).
- **Paid, worth it:** Chambers and Zaharia, *Spark: The Definitive Guide* (O'Reilly, 2018; predates Spark 4 but the execution model is unchanged); Kleppmann and Riccomini, *Designing Data-Intensive Applications*, 2nd ed. (O'Reilly, 2026), batch-processing chapter.

## Sources

All checked October 2026.

- Apache Spark news: 4.0.0 (23 May 2025), 4.1.0 (16 Dec 2025), 4.2.0 (14 Jul 2026). https://spark.apache.org/news/index.html
- Spark 4.1.0 release notes (Declarative Pipelines, Real-Time Mode, VARIANT GA, SQL scripting GA, checksum-based shuffle retry). https://spark.apache.org/releases/spark-release-4.1.0.html
- Spark 4.2.0 release notes (Arrow-optimised Python UDFs by default, `NEAREST BY` join, Auto CDC, Spark UI plan view, Java 25). https://spark.apache.org/releases/spark-release-4-2-0.html
- Spark ANSI compliance (`spark.sql.ansi.enabled` true by default). https://spark.apache.org/docs/latest/sql-ref-ansi-compliance.html
- AWS Big Data Blog, Razorpay on Amazon EMR (9 Mar 2026). https://aws.amazon.com/blogs/big-data/how-razorpay-achieved-11-performance-improvement-and-21-cost-reduction-with-amazon-emr/
- Jordan Tigani, "Big Data is Dead" (MotherDuck, 2023; figures are the author's recollection of BigQuery usage). https://motherduck.com/blog/big-data-is-dead/

_Last reviewed: 2026-10_
