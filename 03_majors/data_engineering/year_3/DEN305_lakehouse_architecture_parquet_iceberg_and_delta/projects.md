# DEN305 · Labs and projects

The lab environment is local: MinIO as S3-compatible storage, Spark 4.x, Trino, Flink 2.x, DuckDB, and an Apache Polaris or Unity Catalog OSS container. Labs 2, 4 and 5 are done without AI assistants. In every lab you inspect the metadata files on storage, not only the engine's output.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Breaking a Hive table | Corrupt a directory-based table with a concurrent writer and a killed job; observe what readers see | Failure log with reader outputs at each step | 3 h |
| 2 · Footer parser | Parse Parquet footers in a short script; match DuckDB's `parquet_metadata()` | Parser and a comparison on 3 files | 4 h |
| 3 · Writer tuning | Write one NYC TLC month with 6 encoding, codec, sort and row-group settings | Size, write-time and read-time table; recommended setting | 4 h |
| 4 · Metadata trees | Make 5 commits in Iceberg and Delta; draw the metadata tree and log from the actual files | Diagrams cross-checked against file listings | 4 h |
| 5 · Toy table format and conflicts | A minimal table format with conditional writes on MinIO; then real Iceberg and Delta concurrent-writer tests | Code and a conflict matrix (overlapping/disjoint partitions × operation types) | 6 h |
| 6 · COW vs MOR | Delete and update 0.1%, 1% and 10% of rows under copy-on-write and merge-on-read | Bytes rewritten, read slowdown, and cost after compaction | 4 h |
| 7 · Evolution and WAP | Schema and partition evolution; time travel; write-audit-publish with branches | Queries across evolution boundaries; a WAP run that blocks bad data | 4 h |
| 8 · Small files and compaction | Stream for 2 hours with 1-minute commits; compact, expire snapshots, remove orphans | File counts, planning times, and a maintenance policy | 5 h |
| 9 · Catalogs | Connect Spark, Trino and DuckDB to one Polaris catalog; register Delta tables in Unity Catalog OSS | Multi-engine query log and credential-vending notes | 4 h |
| 10 · Engine shoot-out | TPC-DS subset on Iceberg from Spark, Trino and DuckDB | Timing table with an explanation per query | 4 h |
| 11 · Interoperability | Delta UniForm read from an Iceberg-only engine; upgrade a table to Iceberg v3 and test readers | Compatibility matrix | 3 h |
| 12 · Streaming commits | Tune Flink commit intervals for freshness vs file count; keep a CDC table under 1 minute of staleness | Freshness vs file-count plot and a CDC staleness report | 5 h |

## Projects

### P1 · Parquet layout forensics (L1, ~6 hours)

**Real-world inspiration:** the NYC TLC publishes its trip records as Parquet, and its "Working with Parquet" guide exists because file layout decides what users pay to read the data ([TLC](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)). Choosing sort order and row-group size is one of the cheapest performance wins in any lake.

**What to build:** a report and a small tool. The tool reads any Parquet file's footer and prints row groups, column chunk sizes, encodings, statistics and page-index presence. The report compares 4 layouts of one year of yellow-taxi trips (unsorted; sorted by pickup time; sorted by pickup zone then time; small vs large row groups) on 8 typical queries.

**Acceptance criteria:**
- The tool's output matches DuckDB's `parquet_metadata()` for every row group and column on 3 test files.
- For each query and layout, the report predicts bytes read from statistics before running, then measures them. At least 6 of 8 predictions are within 20%.
- The recommended layout reduces bytes read for the 8-query mix by at least 50% compared with the unsorted layout.

**Stretch goals:** add bloom filters and show which queries benefit; compare ZSTD levels for storage cost vs CPU time.

**What it proves to an employer:** you understand the file format under every lakehouse well enough to predict and cut I/O.

### P2 · Multi-engine Iceberg lakehouse (L2, ~15 hours)

**Real-world inspiration:** companies adopt open tables so that several engines can share one copy of the data under one catalog. Flipkart's Lambert platform streams into Iceberg and serves queries across clouds ([Rootconf 2025 proposal](https://hasgeek.com/rootconf/rootconf-2025-cfp/sub/streaming-data-lakehouse-at-scale-learnings-from-b-26j5viDUZhMmqixR64vPEp)).

**What to build:** a bronze/silver/gold lakehouse on MinIO with Apache Polaris as the Iceberg REST catalog. Load 6 months of GH Archive events, or 2 years of NYC TLC trips. Spark writes the tables; Trino and DuckDB read them. You must:

- add a column and evolve the partitioning from daily to hourly mid-life;
- publish gold tables through write-audit-publish with branches;
- tag the snapshot behind each monthly report.

**Acceptance criteria:**
- **Consistency across engines:** 10 gold queries return identical results from Spark, Trino and DuckDB.
- **Evolution without rewrite:** partition evolution rewrites 0 bytes of existing data (shown from metadata), and queries spanning both partition schemes are correct.
- **WAP:** a planted bad batch (duplicate events) fails its audit on the branch and never appears on `main`. A good batch is published atomically.
- **Reproducibility:** each tagged monthly report reproduces exactly from its tag after 3 more months of writes and one schema change.
- **Hygiene:** after a maintenance run, the table has no orphan files, snapshots older than the retention window are expired, and the average data file is at least 128 MB.

**Stretch goals:** register the same data as Delta tables in Unity Catalog OSS and compare; expose a gold table to a cloud warehouse as an external Iceberg table.

**What it proves to an employer:** you can build an open, multi-engine lakehouse with safe publication and reproducible history.

### P3 · Operating a streaming CDC lakehouse with erasure (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Razorpay runs a Delta Lake medallion platform with over 60 streaming pipelines (2026), and Flipkart targets data queryable within 15 minutes at over 120 TB a day. Every such platform also has to delete personal data on request. Under India's DPDP Rules 2025 and the EU's GDPR, that includes copies in history (see [DEN404](../../year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md)).

**What to build:** run a lakehouse continuously for 72 hours with:

- a 20,000 events/s append stream into an Iceberg table via Flink;
- a CDC upsert stream from PostgreSQL (reuse DEN303 P2) into a merge-on-read table;
- silver and gold tables built incrementally from change feeds or row lineage;
- an automated maintenance service (compaction, clustering, snapshot expiry, orphan removal) with a compute budget;
- a right-to-erasure workflow that removes one user's data from bronze, silver and gold, including history.

Write a cost model for the whole design.

**Acceptance criteria:**
- **Freshness:** p95 event-to-queryable latency is at most 2 minutes for the append table and 1 minute for the CDC table across the 72 hours. Both are plotted.
- **Read performance:** p95 time for 6 benchmark queries stays within 2× of a freshly compacted copy throughout the run.
- **Correctness:** the CDC table equals the source PostgreSQL table at 3 checkpoints during the run (full key-and-column diff).
- **Maintenance budget:** maintenance compute stays under a stated budget (for example, 15% of ingestion compute), and no maintenance job causes a writer commit to fail more than 3 times in a row.
- **Erasure:** after the workflow runs, no live snapshot, retained snapshot or file on storage contains the user's rows (verified by scanning all data files for their keys). An erasure report lists every table, the snapshots expired and the files rewritten or deleted.
- **Recovery:** the catalog container is killed and restored. Writers resume with no lost or duplicated commits.
- **Write-up:** design document, cost model (storage, requests, compute, retention), a runbook for 3 failure scenarios, and a 5-minute recorded walkthrough of the metadata before and after maintenance.

**Stretch goals:** repeat the CDC table with deletion vectors (Iceberg v3) and compare with position deletes; run the same design on DuckLake with data inlining and compare small-commit behaviour; add a Delta UniForm mirror and measure its metadata lag.

**What it proves to an employer:** you can run a streaming lakehouse as a production system: fresh, fast, within budget, recoverable, and able to delete personal data provably. Teams hire senior platform engineers for exactly these responsibilities.

## Feeds into

- [OV06A Building a Modern Data Platform](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06A_building_a_modern_data_platform/README.md) and [OV06B Semantic Layers and Self-Serve Analytics with AI](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06B_semantic_layers_and_self_serve_analytics_with_ai/README.md): this course is their entry requirement.
- [DEN404 Data Governance, Lineage and Privacy Engineering](../../year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md): P3's erasure workflow becomes a governed, audited process.
- [DEN402 Cloud Data Platforms](../../year_4/DEN402_cloud_data_platforms_snowflake_bigquery/README.md): managed open tables on each platform.
- [DEN403 Data Engineering for AI](../../year_4/DEN403_data_engineering_for_ai_unstructured_data/README.md): snapshots as dataset versions, and Lance for embeddings.
- [DEN501 Frontier Seminar](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md): metadata planning and vectorised readers.
