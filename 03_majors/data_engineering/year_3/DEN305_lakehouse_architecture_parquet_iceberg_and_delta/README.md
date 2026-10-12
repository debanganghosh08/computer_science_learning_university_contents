# DEN305 · Lakehouse Architecture: Parquet, Iceberg and Delta

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [OV06A](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06A_building_a_modern_data_platform/README.md), [OV06B](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06B_semantic_layers_and_self_serve_analytics_with_ai/README.md), [DEN402](../../year_4/DEN402_cloud_data_platforms_snowflake_bigquery/README.md), [DEN404](../../year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md), [DEN501](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md) |

Part of the [Data Engineering major](../../README.md). [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) built pages, logs and MVCC inside one database. A lakehouse rebuilds the same guarantees (atomic commits, snapshots, schema enforcement, indexes) out of immutable files on object storage, so that Spark, Trino, Flink, DuckDB and cloud warehouses can all share one copy of the data. This course takes that design apart, from Parquet bytes to catalogs, and teaches you to run it. [CLD305](../../../cloud_engineering/year_3/CLD305_cloud_storage_and_managed_databases/README.md) covers object storage itself from the cloud side.

## Why this course matters now

Open table formats are where most new analytical data lands. In 2023, researchers from Berkeley, Stanford and Databricks reported that over 70% of bytes written by Databricks customers went to Delta Lake, and that Uber and Netflix run their analytics stacks on Hudi and Iceberg respectively. The formats keep moving. The Apache Iceberg specification's version 3 (deletion vectors, row lineage, VARIANT and geospatial types, default values) is complete and adopted, and version 4 is in development. Delta Lake 4.4.1 (October 2026) supports Spark 4.2 and catalog-managed tables. DuckLake 1.0 (April 2026) stores lakehouse metadata in a SQL database. Catalogs became the control point: Apache Polaris graduated to a top-level Apache project in February 2026, and Unity Catalog's open-source 0.6.0 shipped in August 2026. Flipkart describes a Flink-and-Iceberg platform, code-named Lambert, that ingests over 120 TB of compressed data a day and makes it queryable within 15 minutes (Rootconf 2025 talk proposal). AI assistants can write a `MERGE INTO` or a compaction call. They are much weaker at predicting what a design does to small files, snapshot growth, concurrent writers and the storage bill after six months. That is what this course trains.

## Learning outcomes

By the end you can:

1. **Decode** a Parquet file by hand (footer, row groups, column chunks, pages, encodings, statistics, page index), and **tune** writers for a stated read pattern.
2. **Explain** how Iceberg, Delta Lake and Hudi achieve atomic commits and snapshot isolation on object storage, and **reproduce** conflicts between concurrent writers.
3. **Choose** between copy-on-write and merge-on-read (position deletes, equality deletes, deletion vectors) for a workload, with measured read and write costs.
4. **Evolve** schemas and partitioning without rewriting data, and **use** time travel, branches and tags for audits, rollbacks and write-audit-publish.
5. **Operate** tables: compaction, clustering, snapshot expiry, orphan-file removal, and a maintenance budget.
6. **Deploy** and **compare** catalogs (Iceberg REST catalog with Polaris, Unity Catalog OSS, Glue, Nessie, DuckLake) and explain credential vending and multi-engine access.
7. **Query** the same tables from Spark, Trino, DuckDB and Flink, and **explain** differences in planning and performance.
8. **Design** a lakehouse for a stated organisation (layout, formats, catalog, engines, maintenance, cost), and **defend** it against a warehouse-only alternative.

## Chapters and lessons

### Chapter 1 · From data lakes to lakehouses (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The Hive-era lake | Directories as tables, the Hive Metastore, partition listing, no atomic multi-file commits, no schema enforcement | Break a Hive-style table with a concurrent write and a half-finished job |
| 1.2 Object storage semantics | Strong read-after-write consistency on Amazon S3 (since December 2020), no atomic rename, request costs and rate limits, conditional writes (2024) | Measure LIST and GET latency and cost for 10,000 small vs 100 large objects on MinIO and one cloud bucket |
| 1.3 The lakehouse idea | Open files + a transactional metadata layer + caching and indexing (Lakehouse paper, CIDR 2021); medallion layers | Write a one-page comparison of a warehouse, a lake and a lakehouse for one company |
| 1.4 Who uses what | Delta, Iceberg and Hudi adoption as reported in the CIDR 2023 comparison paper; open formats inside cloud warehouses | List which engines in your environment can read and write each format |

**Check your understanding:** (1) Why can't a Hive-style table give readers a consistent snapshot during a write? (2) What does strong consistency on S3 solve, and what does it not solve for multi-file commits? (3) Why is "open format" not the same as "no lock-in"?

### Chapter 2 · Parquet internals (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 File layout | Magic bytes, row groups, column chunks, data and dictionary pages, the Thrift footer | Parse a Parquet footer with a 100-line script; compare with `parquet_metadata()` in DuckDB |
| 2.2 Encodings and compression | PLAIN, dictionary, RLE/bit-packing hybrid, delta encodings, byte-stream split; Snappy vs ZSTD levels | Write the same NYC TLC month with 6 encoding and codec settings; tabulate size, write and read time |
| 2.3 Statistics and indexes | Row-group min/max, page index (column and offset indexes), bloom filters; why sorted data skips better | Predict pages skipped for 5 filters, then measure bytes read |
| 2.4 Nested and new types | Repetition and definition levels (from Dremel), logical types, VARIANT and geospatial types in recent Parquet and Spark versions | Inspect how a nested GitHub event payload is stored column by column |
| 2.5 Writing good files | Row-group size, file size targets, sort order, dictionary fallbacks; Parquet vs ORC vs Avro; Arrow in memory vs Parquet on disk | Tune a writer so that a common dashboard query reads less than 5% of the bytes |

**Check your understanding:** (1) Why can a bigger row group make point lookups slower but scans faster? (2) When does dictionary encoding fall back, and how do you notice? (3) A filter on a sorted column still reads every page: list three causes.

### Chapter 3 · Table formats: the metadata layer (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Iceberg's tree | Table metadata file, snapshots, manifest lists, manifests, data and delete files; column IDs | Create a table, make 5 commits, and draw its metadata tree from the actual files |
| 3.2 Delta's log | `_delta_log` JSON commits, checkpoints, protocol versions and table features | Replay a Delta log by hand to compute the live file set at version 7 |
| 3.3 Hudi's timeline | Timeline of instants, file groups and slices, copy-on-write and merge-on-read tables, record-level index | Inspect a Hudi table after inserts, upserts and a compaction |
| 3.4 Comparing designs | Metadata size and planning cost, commit latency, update support (CIDR 2023 comparison) | Measure planning time as snapshot count grows to 10,000 in each format |

**Check your understanding:** (1) Why do Iceberg's column IDs make renaming a column safe? (2) What does a Delta checkpoint save a reader from? (3) Which design makes a "list all files in this snapshot" call cheapest, and why?

### Chapter 4 · ACID on object storage (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Commit protocols | Optimistic concurrency; atomic pointer swap in a catalog (Iceberg); put-if-absent log entries (Delta) using conditional writes or a lock service | Implement a toy table format with conditional writes on MinIO |
| 4.2 Conflicts | Validation on commit, conflict detection by files and partitions, retries, isolation levels (serialisable vs write-serialisable) | Run 2 writers updating overlapping and disjoint partitions; record which commits fail |
| 4.3 Readers during writes | Snapshot isolation for readers, long-running readers vs snapshot expiry | Keep a reader on an old snapshot while compacting; see what expiry does to it |
| 4.4 Multi-table transactions | Why most formats commit one table at a time; catalog-level transactions; Spark 4.2's DataSource V2 transaction management | Design a two-table update that stays consistent for readers |

**Check your understanding:** (1) What exactly is the "atomic operation" in an Iceberg commit, and who provides it? (2) Two streaming jobs write to the same table: why do they conflict more than two batch jobs? (3) What can a reader see if snapshot expiry deletes files it still needs?

### Chapter 5 · Row-level changes (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Copy-on-write | Rewriting whole files on update or delete; write amplification | Delete 0.1% of rows in a 50 GB table; measure bytes rewritten |
| 5.2 Merge-on-read | Position deletes, equality deletes, binary deletion vectors (Iceberg v3, Delta), Hudi log files; read-side cost | Repeat 5.1 with merge-on-read; measure read slowdown until compaction |
| 5.3 `MERGE INTO` at scale | Matching strategies, file pruning on the join key, cardinality violations | Upsert 1M CDC changes into a 500M-row table under 3 layouts |
| 5.4 Change feeds | Delta change data feed, Iceberg row lineage (v3) and incremental reads; Spark 4.2's `CHANGES` clause | Build an incremental downstream job that reads only changed rows |

**Check your understanding:** (1) Why are equality deletes cheap to write and expensive to read, and why does Iceberg v4 stop new writers from producing them? (2) When is copy-on-write the right choice despite write amplification? (3) What does row lineage let you do that snapshot diffs cannot?

### Chapter 6 · Evolution, time travel and branches (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Schema evolution | Add, drop, rename, reorder and widen columns; Delta column mapping; what breaks old readers | Evolve a schema 6 times and query every historical snapshot |
| 6.2 Hidden partitioning | Partition transforms (day, hour, bucket, truncate, and multi-argument transforms in v3); partition evolution without rewrite | Change daily partitioning to hourly mid-life; query across the boundary |
| 6.3 Time travel | Snapshot and timestamp queries, rollback, retention settings and their storage cost | Roll back a bad write, then compute the storage cost of 30 days of retention |
| 6.4 Branches, tags and write-audit-publish | Iceberg branches and tags; writing to a branch, validating, then publishing | Implement WAP: a failing check keeps bad data off the main branch |

**Check your understanding:** (1) Why does hidden partitioning prevent the classic "forgot the partition filter" full scan? (2) Time travel and privacy deletion requests pull in opposite directions: how do you reconcile them (see [DEN404](../../year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md))? (3) What does write-audit-publish give you that a staging table does not?

### Chapter 7 · Table maintenance (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Small files | Where they come from (streaming, over-partitioning, many writers); planning and read costs | Stream into a table for 2 hours at 1-minute commits; count files and planning time |
| 7.2 Compaction and clustering | Bin-packing, sort and Z-order rewrites, Delta `OPTIMIZE` and liquid clustering, Hudi compaction and clustering | Compact the streamed table; measure query time and rewrite cost |
| 7.3 Expiry and clean-up | Expiring snapshots, rewriting manifests, removing orphan files, `VACUUM`; safety windows | Find and remove orphan files left by a killed job without touching live data |
| 7.4 Maintenance budgets | Scheduling maintenance, conflicts with writers, managed options (Amazon S3 Tables, managed services that optimise automatically) | Write a maintenance policy with a monthly compute budget and verify it |

**Check your understanding:** (1) Why can aggressive compaction conflict with streaming writers? (2) What makes orphan-file removal dangerous, and what safety window do you choose? (3) How do you decide that a table is worth clustering?

### Chapter 8 · Catalogs (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Why catalogs matter | Names to metadata pointers, atomic commits, access control, discovery | List every responsibility a catalog has in your P2 design |
| 8.2 The Iceberg REST catalog | The OpenAPI specification, server-side commits, credential vending; Apache Polaris as an implementation | Run Polaris; connect Spark, Trino and DuckDB to the same table |
| 8.3 Unity Catalog and Delta | Unity Catalog OSS (0.6.0, August 2026), the Unity Catalog Delta API, catalog-managed Delta tables (Delta 4.x) | Register Delta tables in Unity Catalog OSS and read them from two engines |
| 8.4 Other designs | AWS Glue, Project Nessie (Git-like branches across tables), DuckLake (metadata in a SQL database, 1.0 in April 2026) | Compare commit latency for 1,000 small commits on Polaris and DuckLake |

**Check your understanding:** (1) Why is the catalog, not the file format, now the main point of lock-in? (2) What problem does credential vending solve for multi-engine access? (3) What does DuckLake gain and lose by putting metadata in a database instead of files?

### Chapter 9 · Query engines on the lakehouse (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Planning with metadata | Manifest and partition pruning, column statistics, delete-file application, split planning | Trace a Trino query's split planning on a 10,000-file table |
| 9.2 Trino | Coordinator and workers, connectors, dynamic filtering, fault-tolerant execution | Run TPC-DS queries on Iceberg with and without dynamic filtering |
| 9.3 Spark, Flink and DuckDB | Spark as the main writer and maintainer; Flink for streaming writes; DuckDB's Iceberg extension and DuckLake for single-node analytics | Run the same 10 queries on 3 engines; explain the fastest per query |
| 9.4 Warehouses reading open tables | Snowflake Iceberg tables, BigQuery BigLake tables, Fabric OneLake (Delta), Redshift reading Iceberg; who writes and who only reads | Expose one table to a warehouse; compare cost and speed with native tables |

**Check your understanding:** (1) Why can the same table be fast in one engine and slow in another? (2) What breaks if two engines write the same table with different format versions? (3) When should the warehouse own the table instead of reading an open one?

### Chapter 10 · Interoperability (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Translating metadata | Delta UniForm (Iceberg metadata written with Delta commits, atomic since Delta 4.3), Apache XTable (incubating) | Read a UniForm table from an Iceberg-only engine; check freshness after commits |
| 10.2 Version compatibility | Iceberg v1–v3 readers and writers, Delta protocol features and `DROP FEATURE`, the v4 direction (relative paths) | Upgrade a table to v3; find which engines in your stack can no longer read it |
| 10.3 Choosing a format | Ecosystem, engines, update patterns, streaming, catalog choice, team skills | Write a format decision record for three organisations |

**Check your understanding:** (1) What can go wrong when two metadata formats describe the same data files? (2) Why should a format upgrade be treated like a database migration? (3) Which factor usually decides between Iceberg and Delta in practice?

### Chapter 11 · Streaming lakehouses and AI data (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Streaming writes | Flink and Kafka Connect sinks for Iceberg, commit intervals vs freshness vs small files; Flipkart's 15-minute queryability target | Tune commit interval for a 20,000 events/s stream; plot freshness vs file count |
| 11.2 Upserts from CDC | Merge-on-read for CDC, equality deletes vs deletion vectors, compaction cadence (continuing [DEN303](../DEN303_streaming_systems_kafka_and_flink/README.md) P2) | Keep a CDC table under 1 minute of staleness with bounded read cost |
| 11.3 Inlining and small commits | DuckLake's data inlining (small changes stored in the catalog database until flushed) | Compare 1,000 tiny inserts on DuckLake with and without inlining |
| 11.4 Data for AI on the lakehouse | Multimodal and embedding columns, the Lance format for random access, dataset snapshots as training-data versions (continued in [DEN403](../../year_4/DEN403_data_engineering_for_ai_unstructured_data/README.md)) | Store embeddings for 1M documents in Parquet and in Lance; compare random-access reads |

**Check your understanding:** (1) What is the real trade-off when a stakeholder asks for 1-minute freshness on a lakehouse table? (2) Why do CDC tables need more maintenance than append-only tables? (3) Why is a table snapshot a natural version identifier for a training dataset?

### Chapter 12 · Designing a lakehouse (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Reference designs | Ingestion, bronze/silver/gold, catalog, engines, maintenance, governance hooks; Razorpay's Delta medallion as a public example | Draw a full design for a mid-size Indian fintech (illustrative) |
| 12.2 Cost model | Storage, requests, compute for queries and maintenance, egress; retention multipliers | Build a spreadsheet model; find the top two cost drivers |
| 12.3 Migration | Migrating Hive tables in place vs by shadow copy; validation; cut-over | Migrate a Hive-style table to Iceberg with zero reader downtime |
| 12.4 Design review | Defending choices under questioning | Oral defence of P3 |

**Check your understanding:** (1) Which costs grow with retention, and which with query volume? (2) What would make you recommend a warehouse-only design instead? (3) How do you prove a migration lost no rows and changed no values?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Breaking a Hive table | Failure log |
| 2 | 2 | Lab 2 · Footer parser | Parser and metadata comparison |
| 3 | 2 | Lab 3 · Writer tuning | Encoding and codec table; **P1 due** |
| 4 | 3 | Lab 4 · Metadata trees | Drawn trees for 3 formats |
| 5 | 4 | Lab 5 · Toy table format and conflicts | Conflict matrix |
| 6 | 5 | Lab 6 · COW vs MOR | Read/write cost table |
| 7 | 6 | Lab 7 · Evolution and WAP | Mid-term (AI off): formats and commits |
| 8 | 7 | Lab 8 · Small files and compaction | Maintenance policy |
| 9 | 8 | Lab 9 · Catalogs | Multi-engine access; **P2 due** |
| 10 | 9 | Lab 10 · Engine shoot-out | Benchmark and explanations |
| 11 | 10 | Lab 11 · Interoperability | Compatibility matrix |
| 12 | 11 | Lab 12 · Streaming commits | Freshness vs file-count plot |
| 13 | 11 | Lab 12 (cont.) | CDC staleness report |
| 14 | 12 | Design review | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining specification sections (the Iceberg spec, the Delta `PROTOCOL.md`); generating test tables and concurrent-writer harnesses; drafting engine configuration for Spark, Trino and Flink catalogs; translating maintenance procedures between formats. Tools: Claude Code, GitHub Copilot, Cursor; DuckDB's CLI agent mode and the DuckDB skills for Claude Code (September 2026) for local exploration.
- **Do without AI (drills):** decoding a Parquet footer and computing skipped row groups; drawing an Iceberg metadata tree from files; replaying a Delta log by hand; predicting which concurrent commits conflict. The mid-term tests these.
- **Verify AI output by:** (1) inspecting the actual metadata files after every operation, not the engine's success message; (2) counting files, bytes and snapshots before and after maintenance; (3) checking every claimed feature against the specification and your exact engine versions (support for v3 features differs across engines); (4) running concurrent-writer tests rather than trusting a description of isolation.
- **Where AI still fails here (show it yourself):** ask an assistant to "make this streaming table fast" and to "delete this user's data from the lakehouse". Record whether it suggests compaction schedules that conflict with the writer, forgets that old snapshots and orphan files still hold deleted rows, mixes Delta and Iceberg procedure names, or claims engine support for v3 features that your engine version lacks. Verify each claim against metadata files and engine release notes.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–12 | 25% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 20% |
| Oral defence of P3 | 10% |

**Mastery gate.** You pass when you can, without AI: (1) from a directory of Iceberg metadata and data files, determine the live file set of a given snapshot and explain every file's role; (2) given two concurrent operations on a table, predict whether the second commit succeeds, retries or fails, and verify it; (3) take a degraded streaming table (thousands of small files, deletion files, 50,000 snapshots) and restore query time to within 2× of a freshly written table, under a stated compute budget, without breaking readers.

## Industry reality

The CIDR 2023 comparison paper reports Delta, Hudi and Iceberg in production at Databricks customers, Uber and Netflix respectively. Netflix described creating and migrating to Iceberg in 2020. Public Indian examples include Razorpay's Delta Lake medallion platform on Amazon EMR, which earlier used Hudi (2026), and Flipkart's Lambert streaming lakehouse on Flink and Iceberg (Rootconf 2025 proposal). Cloud providers now sell managed open tables (Amazon S3 Tables, BigQuery BigLake, Snowflake Iceberg tables), so the lakehouse and warehouse categories overlap.

**Interview questions from this course**

1. *"How does Iceberg (or Delta) give ACID transactions on S3?"* A strong answer covers immutable data files, a metadata tree or log, optimistic concurrency, the atomic step (catalog pointer swap or conditional put), conflict validation and retries, and snapshot isolation for readers.
2. *"Copy-on-write or merge-on-read for a CDC table updated every minute?"* Cover write amplification vs read cost, deletion vectors vs equality deletes, compaction cadence and its conflict with writers, and how to measure the trade-off.
3. *"Queries on our lakehouse got 10× slower over three months. Why?"* Cover small files, growing snapshots and manifests, unapplied delete files, lost clustering, missing statistics, and the maintenance plan that fixes and prevents each.
4. *"Iceberg or Delta?"* Cover engines and ecosystem, catalog choice, update patterns, streaming support, interoperability (UniForm, XTable), team skills, and why the catalog decision matters as much as the format.
5. *"A user asks to be forgotten. How do you delete their data from a lakehouse?"* Cover row-level deletes, deletion vectors vs rewrites, snapshot expiry and time-travel retention, orphan files, backups and downstream copies, and how to prove deletion.

## Resources (free first)

- **Specifications:** [Apache Iceberg table spec](https://iceberg.apache.org/spec/) and [REST catalog OpenAPI](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml); [Delta Lake protocol](https://github.com/delta-io/delta/blob/master/PROTOCOL.md); [Apache Parquet format](https://parquet.apache.org/docs/file-format/); [DuckLake](https://ducklake.select/).
- **Documentation:** Iceberg [maintenance](https://iceberg.apache.org/docs/latest/maintenance/) and [branching](https://iceberg.apache.org/docs/latest/branching/); [Delta Lake](https://docs.delta.io/latest/index.html) and [UniForm](https://docs.delta.io/latest/delta-uniform.html); [Hudi table types](https://hudi.apache.org/docs/table_types); [Apache Polaris](https://polaris.apache.org/); [Unity Catalog OSS](https://docs.unitycatalog.io/); [Project Nessie](https://projectnessie.org/); [Apache XTable](https://xtable.apache.org/); [Trino Iceberg connector](https://trino.io/docs/current/connector/iceberg.html); [DuckDB Iceberg extension](https://duckdb.org/docs/stable/core_extensions/iceberg/overview); [Amazon S3 conditional writes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes.html) and [consistency](https://aws.amazon.com/s3/consistency/).
- **Papers:** [Lakehouse](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) (CIDR 2021); [Delta Lake](https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf) (VLDB 2020); [Analyzing and Comparing Lakehouse Storage Systems](https://www.cidrdb.org/cidr2023/papers/p92-jain.pdf) (CIDR 2023); [Dremel](https://research.google/pubs/dremel-interactive-analysis-of-web-scale-datasets-2/) (VLDB 2010).
- **Course:** [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) (free; data lake and platform modules).
- **Paid, worth it:** Kleppmann and Riccomini, *Designing Data-Intensive Applications*, 2nd ed. (O'Reilly, 2026).

## Sources

All checked October 2026.

- Jain, Kraft, Power, Das, Stoica and Zaharia, "Analyzing and Comparing Lakehouse Storage Systems" (CIDR 2023): Delta over 70% of bytes written by Databricks customers; Uber on Hudi, Netflix on Iceberg; cites Gooch, "Why and How Netflix Created and Migrated to a New Table Format: Iceberg" (2020). https://www.cidrdb.org/cidr2023/papers/p92-jain.pdf
- Apache Iceberg spec, format versioning (v1–v3 complete and adopted; v4 under development, not adopted). https://iceberg.apache.org/spec/
- Apache Iceberg releases (1.12.0 latest). https://iceberg.apache.org/releases/
- Delta Lake releases (4.0.0 on 9 Jun 2025 through 4.4.1 on 5 Oct 2026; catalog-managed tables; UniForm atomic Iceberg conversion in 4.3.0). https://github.com/delta-io/delta/releases
- Apache Incubator, Polaris status (entered incubation 9 Aug 2024; graduated 15 Feb 2026). https://incubator.apache.org/projects/polaris.html
- Unity Catalog releases (0.6.0, 20 Aug 2026). https://github.com/unitycatalog/unitycatalog/releases
- DuckDB news ("DuckLake v1.0", 13 Apr 2026; data inlining, 2 Apr 2026). https://duckdb.org/news/
- Flipkart Data Platform, "Streaming data lakehouse at scale" (Rootconf 2025 talk proposal). https://hasgeek.com/rootconf/rootconf-2025-cfp/sub/streaming-data-lakehouse-at-scale-learnings-from-b-26j5viDUZhMmqixR64vPEp
- AWS Big Data Blog, Razorpay on Amazon EMR (9 Mar 2026). https://aws.amazon.com/blogs/big-data/how-razorpay-achieved-11-performance-improvement-and-21-cost-reduction-with-amazon-emr/
- Apache XTable (incubating). https://xtable.apache.org/

_Last reviewed: 2026-10_
