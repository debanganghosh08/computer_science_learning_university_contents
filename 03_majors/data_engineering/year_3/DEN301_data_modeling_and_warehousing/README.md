# DEN301 · Data Modeling and Warehousing

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [DEN401](../../year_4/DEN401_data_quality_observability_and_data_contracts/README.md), [DEN305](../DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md), [DEN402](../../year_4/DEN402_cloud_data_platforms_snowflake_bigquery/README.md), [OV06A](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06A_building_a_modern_data_platform/README.md) |

Part of the [Data Engineering major](../../README.md). [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) taught how one database stores and executes a query. This course is about modelling data so that thousands of queries, written by people and by AI tools, return correct numbers cheaply, and about the warehouse engines those queries run on. Metric definitions, BI and semantic layers are taught in [DAN304](../../../data_analysis/year_3/DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md); this course stops at well-modelled, tested tables.

## Why this course matters now

Most wrong numbers in a company are modelling bugs, not code bugs: a fact table joined to a history table without a date condition, a mixed grain that counts an order once per item, a "customer" defined three ways. The model also decides cost. In Fivetran's 2022 benchmark on TPC-DS data, one big denormalised table ran about 25–50% faster than a star schema across Redshift, Snowflake and BigQuery, but on Redshift it tripled storage from about 30 GB to over 90 GB. Razorpay reports that its Delta Lake medallion platform on Amazon EMR serves over 6 PB of queries a day (2026). AI tools now write most first-draft SQL: on the BIRD text-to-SQL benchmark the best system reached about 83% execution accuracy in September 2026 against a human baseline of about 93%, and the top entry on the Spider 2.0-DBT leaderboard (agents completing real dbt projects) scored 65.6 in October 2026. dbt v2's engine now statically checks every model's columns and types before anything runs. None of these tools decides the grain, chooses how history is kept, or notices that a join silently doubled revenue. That is the job this course trains.

## Learning outcomes

By the end you can:

1. **Explain** why OLTP and OLAP workloads need different schemas and storage, with numbers from your own benchmark.
2. **Design** a dimensional model from a business description: bus matrix, declared grain, fact table type, conformed dimensions, and measure additivity.
3. **Implement** slowly changing dimensions (types 1, 2 and 6) with idempotent `MERGE` statements and point-in-time joins, and **prove** they are idempotent by re-running them.
4. **Build** a Data Vault 2.0 layer (hubs, links, satellites, PIT tables) and a star schema on top of it, and **argue** when each approach (star, vault, one big table) is the right one.
5. **Measure** how encoding, sort order and partitioning change file size and bytes scanned, using DuckDB, Parquet metadata and warehouse query profiles.
6. **Explain** how an MPP warehouse distributes, prunes and joins data (Redshift distribution styles, Snowflake micro-partitions, BigQuery slots), and **predict** the cost of a query before running it.
7. **Write** incremental transformation models (merge, insert-overwrite, lookback windows) that give the same result on re-run and on backfill.
8. **Audit** AI-generated SQL and models for grain errors, fan-out joins, wrong SCD joins and time-zone mistakes, using reconciliation queries.

## Chapters and lessons

### Chapter 1 · Two workloads: OLTP and OLAP (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Workload shapes | OLTP: point reads and writes, short transactions, normalised rows. OLAP: scans of millions of rows, aggregates, few columns. HTAP engines and their limits | Run 10 analytic queries on the Olist e-commerce dataset in PostgreSQL and DuckDB; tabulate time and data read |
| 1.2 Why warehouses denormalise | 3NF prevents update anomalies; warehouses are append-mostly, so join cost dominates. Read amplification vs write anomalies | Count the joins needed for "revenue by seller state by month" in 3NF vs a star |
| 1.3 Architectures | Inmon's normalised enterprise warehouse plus marts; Kimball's bus architecture; Data Vault; the lakehouse medallion (bronze, silver, gold) and where each layer sits | Draw all four for the same company; mark where history and business rules live |
| 1.4 From questions to a model | Kimball's four steps: business process, grain, dimensions, facts. Requirements interviews: ask for decisions, not reports | Interview a classmate playing a food-delivery operations head; write 12 questions the model must answer |

**Check your understanding:** (1) A column store answers `SUM(amount)` 30× faster than PostgreSQL on the same machine: name two mechanisms responsible. (2) Why is "the OLTP schema is already normalised, so just query it" a cost and correctness risk at scale? (3) In a medallion design, which layer should hold deduplicated, conformed data, and why not the gold layer?

### Chapter 2 · Facts and grain (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Declaring the grain | One row = one what? Atomic grain vs aggregated grain; mixed-grain tables as the main source of double counting | Find the grain violation in a provided `orders_items` table that inflates GMV |
| 2.2 Fact table types | Transaction, periodic snapshot (daily balances), accumulating snapshot (order lifecycle milestones), factless facts (attendance, promotions shown) | Model a loan account three ways; say which questions each answers |
| 2.3 Additivity | Additive, semi-additive (balances: never sum across time), non-additive (ratios, distinct counts); store numerator and denominator | Rewrite a dashboard that averages averages |
| 2.4 Bus matrix and conformed dimensions | Shared dimensions across processes; drill-across queries; fan traps and chasm traps | Build a bus matrix for orders, payments, deliveries and refunds |
| 2.5 Special dimensions | Degenerate (order number), junk (flags), role-playing (order date, ship date, delivery date) | Add three role-playing date keys and write the queries |

**Check your understanding:** (1) Why can't you sum a daily balance snapshot across a month, and what can you compute instead? (2) Two fact tables share `dim_customer`; why must you aggregate each fact to the common grain before joining them? (3) What question can an accumulating snapshot answer that a transaction fact cannot without self-joins?

### Chapter 3 · Dimensions in depth (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Keys | Surrogate vs natural keys; sequences vs hash keys (MD5/SHA-256 of business keys); the unknown-member row (`-1`) instead of NULL foreign keys | Show how a reused natural key (recycled phone number) corrupts history; fix with surrogates |
| 3.2 Calendars and time zones | Date and time dimensions; Indian fiscal year (April–March); sale-event calendars; storing UTC plus local date; IST at UTC+05:30 | Build a date dimension for 2015–2035 with fiscal quarters and holiday flags |
| 3.3 Hierarchies and many-to-many | Fixed, ragged and parent-child hierarchies; bridge tables with weighting factors | Model "one customer, several bank accounts, joint holders" and avoid double counting |
| 3.4 Rapidly changing attributes | Mini-dimensions for banded attributes (age band, credit band), outriggers | Move a daily-changing loyalty tier out of a 50M-row customer dimension |
| 3.5 Semi-structured attributes | JSON and VARIANT columns (Snowflake VARIANT, BigQuery JSON, Spark 4.1 VARIANT with shredding); when to promote a field to a column | Query a nested GitHub event payload, then promote three fields and compare bytes scanned |

**Check your understanding:** (1) Why are hash keys convenient for parallel loading, and what collision and skew risks do they bring? (2) A report shows sales on the wrong day for orders placed at 11:45 p.m. IST: where in the model is the bug? (3) When does a bridge table's weighting factor give a correct total, and when is no weighting correct?

### Chapter 4 · Slowly changing dimensions and time (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 SCD types | Type 0 (fixed), 1 (overwrite), 2 (new row with `valid_from`, `valid_to`, `is_current`), 3 (previous value column), 4 (history table), 6 (1+2+3) | Choose a type for 10 attributes of a merchant dimension and justify each |
| 4.2 SCD2 with MERGE | Change detection with a hash of tracked columns; closing and opening rows in one transaction; dbt snapshots (timestamp vs check strategy); Spark 4.2 Auto CDC for type 1 | Implement SCD2 in DuckDB SQL; run it three times on the same input and prove the table does not change |
| 4.3 Late and early arrivals | Late-arriving dimensions (inferred members), early-arriving facts, reprocessing windows | Load facts before their customers exist; backfill the attributes later without breaking keys |
| 4.4 Bitemporal data | Valid time vs recorded (transaction) time; restatements in finance; "as known on" vs "as true on" queries | Answer "what did we report for March, as of 5 April?" from a bitemporal table |
| 4.5 Point-in-time joins | Joining facts to the dimension version valid at event time; the same idea prevents label leakage in ML training sets ([MLE303](../../../machine_learning_engineering/year_3/MLE303_training_pipelines_feature_stores_and_experiment/README.md)) | Write the as-of join; show the wrong answer from joining on `is_current` |

**Check your understanding:** (1) Your SCD2 job ran twice after a retry and now some customers have two current rows: what invariant failed, and what test catches it? (2) Why do regulators and auditors care about transaction time, not just valid time? (3) What does joining on `is_current = true` do to last year's revenue by region?

### Chapter 5 · Data Vault 2.0 and One Big Table (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Hubs, links, satellites | Business keys in hubs, relationships in links, descriptive history in satellites; load date and record source on every row | Vault-model customers, merchants and payments from two source systems |
| 5.2 Loading patterns | Insert-only loads, hash-diff change detection, parallel independent loads, multi-active and effectivity satellites | Load three daily batches; verify no update statement was needed |
| 5.3 Serving from a vault | Point-in-time (PIT) and bridge tables; business vault rules; information marts as stars | Build a PIT table and a star mart on top of the vault |
| 5.4 When a vault pays off | Many changing sources, audit and lineage needs, regulated industries; the cost: more joins, more tables, more skill | Write a one-page recommendation for a bank vs a 20-person startup |
| 5.5 One Big Table | Wide pre-joined tables; Fivetran's 2022 benchmark (faster queries, 3× storage on Redshift); OBT for single consumers, BI extracts and ML feature tables | Build OBT and star versions of the same mart; measure bytes scanned and storage in DuckDB |

**Check your understanding:** (1) Why does an insert-only vault make backfills and audits easier than a type 1 star? (2) An OBT has 400 columns and every dimension change forces a full rebuild: what does that cost, and how would you limit it? (3) Name one question that is easy on a vault and hard on a star.

### Chapter 6 · Columnar storage and compression (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Column stores | NSM vs DSM vs PAX (recap from CS211); C-Store (2005) and MonetDB/X100 (2005) as the ancestors of today's engines | Read the C-Store paper's introduction; list the ideas present in DuckDB |
| 6.2 Encodings | Dictionary, run-length, delta, bit-packing, frame-of-reference; why sort order changes compression | Sort NYC TLC trips by pickup zone vs by time; compare Parquet sizes |
| 6.3 Skipping data | Min/max statistics (zone maps), data skipping, late materialisation, predicate pushdown | Use `parquet_metadata()` in DuckDB to predict which row groups a filter skips; then check |
| 6.4 Nested data | Dremel's repetition and definition levels; why nested columns can still be scanned column by column | Encode a 3-level nested record by hand into repetition and definition levels |

**Check your understanding:** (1) Why does sorting by a low-cardinality column first usually shrink files? (2) A filter on `customer_id` skips nothing: what about the data layout explains it? (3) When does late materialisation stop helping?

### Chapter 7 · Warehouse internals: MPP and separated storage (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Shared-nothing MPP | Hash, round-robin and replicated distribution; co-located joins vs redistribution vs broadcast; Redshift `KEY`, `EVEN`, `ALL`, `AUTO` and sort keys | Given three tables and two queries, choose distribution keys and count the rows each join moves |
| 7.2 Separation of storage and compute | Snowflake's architecture (SIGMOD 2016): immutable micro-partitions, virtual warehouses, cloud services layer, result cache; per-second billing with a 60-second minimum | Run the same query on X-Small and Medium warehouses; compute credits and speed-up |
| 7.3 Dremel and BigQuery | Tree execution, slots, in-memory shuffle tier, Colossus storage (Dremel papers, 2010 and 2020); on-demand bytes-scanned billing vs reserved slots | Dry-run five queries on the GH Archive public dataset; predict bytes before running |
| 7.4 Reading query profiles | Snowflake Query Profile, BigQuery execution graph, DuckDB `EXPLAIN ANALYZE`; spilling, exploding joins, pruning ratios | Diagnose three slow queries from their profiles alone |
| 7.5 Concurrency and workload management | Queues, multi-cluster warehouses, reservations and assignments; noisy neighbours; isolating ELT from dashboards | Design a workload-isolation plan for ELT, BI and ad hoc users |

**Check your understanding:** (1) Why does a join on two tables distributed by the join key avoid network traffic, and what happens when one key is skewed? (2) A BigQuery query reads 2 TB though it filters to one day: give two causes. (3) Why can doubling a Snowflake warehouse size leave cost unchanged?

### Chapter 8 · Partitioning, clustering and physical design (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Partitioning | By event date vs ingestion date; partition granularity; too many small partitions; partition expiry | Partition a 1-billion-row synthetic events table two ways and compare pruning |
| 8.2 Clustering | Snowflake clustering keys and clustering depth; BigQuery clustered tables; Z-order and Hilbert curves; Delta liquid clustering (preview of [DEN305](../DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md)) | Cluster on two columns; measure skipped micro-partitions or blocks for 6 query shapes |
| 8.3 Pre-computation | Materialised views, aggregate tables, incremental refresh, result caches; staleness contracts | Replace a dashboard's 40-second query with an aggregate; define how stale it may be |
| 8.4 Cost as a design input | Bytes scanned, partitions pruned, spill and slot-time as the units of cost | Write a "cost budget" for 10 key queries and verify it |

**Check your understanding:** (1) Why can partitioning by a high-cardinality column make queries slower? (2) Clustering helps reads but costs background compute: how do you decide it is worth it? (3) A materialised view is "always fresh" in the docs: what does that guarantee, and what does it cost?

### Chapter 9 · Transformations and incremental models (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 ELT layering | Sources, staging (rename and cast only), intermediate, marts; naming conventions; one model, one grain | Refactor a 600-line SQL script into layered models |
| 9.2 dbt as the reference tool | Models, `ref`, sources, materialisations (view, table, incremental, ephemeral), snapshots, model versions; dbt v2 (Rust engine, static analysis, column-level lineage in strict mode) and the Apache-2.0 `dbt-oss` distribution | Build the Olist marts in dbt on DuckDB; run with static analysis in strict mode and fix every finding |
| 9.3 Incremental strategies | Append, merge, delete+insert, insert-overwrite by partition; lookback windows for late data; idempotent re-runs | Make an incremental model survive a 3-day-late batch and a re-run of yesterday |
| 9.4 SQL patterns | Deduplication with `ROW_NUMBER()` and `QUALIFY`, sessionisation, gaps and islands, `MERGE` semantics, NULLs in joins and `NOT IN` | Solve 12 timed SQL problems AI-off |
| 9.5 Reconciliation | Row counts and control totals from source to mart; uniqueness at the declared grain; tests as code (deepened in [DEN401](../../year_4/DEN401_data_quality_observability_and_data_contracts/README.md)) | Add reconciliation tests that catch a planted fan-out join |

**Check your understanding:** (1) Why is `INSERT INTO ... SELECT` without a key unsafe for an incremental model that may be retried? (2) How long should a lookback window be, and what data tells you? (3) A `NOT IN` subquery returns zero rows after a NULL appears in the source: explain why.

### Chapter 10 · Modelling real domains, and modelling for AI consumers (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Payments and ledgers | Double-entry facts, authorisation vs capture vs settlement, refunds and chargebacks, reconciliation with bank files (illustrative UPI-style flows; payments depth in [OV10A](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10A_payment_systems_engineering_upi_cards/README.md)) | Model payments so that "money in = money out + balance change" is a testable query |
| 10.2 Marketplaces and logistics | Accumulating snapshot of an order: placed, accepted, picked up, delivered, cancelled; time-between-milestone measures (illustrative food-delivery scenario) | Build the snapshot from an event stream; compute p50/p90 delivery times by zone |
| 10.3 Event and clickstream data | Event schemas, sessionisation, identity stitching (anonymous to logged-in), bot filtering | Sessionise GH Archive events per actor with a 30-minute gap rule |
| 10.4 Designing for AI and human consumers | Descriptions on every table and column, grain stated in docs, conformed names, sample queries; metric definitions as code (Spark 4.2 metric views, semantic layers in [OV06B](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06B_semantic_layers_and_self_serve_analytics_with_ai/README.md)) | Ask an AI assistant 20 business questions against your undocumented marts, then document them and re-ask; score both runs |
| 10.5 Evolving models safely | Additive changes, deprecation windows, versioned models, communicating breaking changes to consumers | Ship a breaking change to `dim_customer` with a two-version overlap |

**Check your understanding:** (1) Why is a ledger modelled as immutable entries instead of an updatable balance column? (2) What did documentation change in your AI-assistant experiment, and which failures did it not fix? (3) Why should a breaking model change be versioned rather than announced?

### Chapter 11 · Design reviews and modelling under ambiguity (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 The 45-minute modelling interview | Clarify, list questions, declare grain, draw facts and dimensions, handle history, discuss scale | Three timed mock interviews (ride-hailing, edtech, hospital) |
| 11.2 Trade-off memos | Star vs vault vs OBT; warehouse vs lakehouse; cost, skills and audit needs | Write a 2-page decision record for a stated organisation |
| 11.3 Reviewing AI-generated models | Checklist: grain, keys, fan-out, SCD join, time zone, NULL handling, incremental idempotency | Review five AI-generated dbt models; find at least eight defects |
| 11.4 Defending a design | Answering "why not just…?" with evidence | Oral defence of P3 |

**Check your understanding:** (1) What three questions would you ask before choosing a fact table's grain? (2) Which review checklist item catches the most bugs in your logs, and why? (3) When is "it depends" an acceptable answer in a design review, and what must follow it?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Row store vs column store | Benchmark table and explanation |
| 2 | 2 | Lab 2 · Grain hunting | Bus matrix for a marketplace |
| 3 | 3 | Lab 2 (cont.) | **P1 due** |
| 4 | 4 | Lab 3 · Idempotent SCD2 | SCD2 code + re-run proof |
| 5 | 5 | Lab 4 · Vault and OBT | Benchmark note |
| 6 | 6 | Lab 5 · Parquet anatomy | Encoding and sort-order report |
| 7 | 7 | Lab 6 · Warehouse economics | Cost-prediction sheet |
| 8 | 7 | Lab 6 (cont.) | Mid-term (AI off): modelling + cost estimation |
| 9 | 8 | Lab 7 · Pruning and clustering | **P2 due** |
| 10 | 9 | Lab 8 · dbt with static analysis | Layered dbt project |
| 11 | 9 | Lab 8 (cont.) | Incremental model passes re-run and late-data tests |
| 12 | 10 | Lab 9 · Ledger reconciliation | Reconciliation queries |
| 13 | 10 | Lab 10 · AI against your marts | Before/after scoring report |
| 14 | 11 | Mock modelling interviews | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** first drafts of staging models and column descriptions; generating synthetic source data with planted defects (late rows, duplicate keys, recycled natural keys); translating SQL between DuckDB, Snowflake, BigQuery and Spark dialects; explaining an unfamiliar query profile. Tools: Claude Code, GitHub Copilot or Cursor in the editor; platform assistants such as Gemini in BigQuery and the BigQuery Data Engineering Agent (generally available from April 2026, per Google), Snowflake Cortex and Databricks Assistant; dbt v2's language server and static analysis; DuckDB's CLI agent mode (October 2026).
- **Do without AI (drills):** declaring grain and drawing a bus matrix from a written brief; writing SCD2 `MERGE` statements; computing bytes scanned and credits for a query on paper; the 12 timed SQL problems in Chapter 9; the mid-term and final.
- **Verify AI output by:** (1) a uniqueness test at the declared grain; (2) control totals that match the source (row counts, sum of amounts) before and after every join; (3) re-running the model twice and diffing the result; (4) reading the query profile or `EXPLAIN` on realistic volumes, not on 10 rows; (5) running dbt in strict static-analysis mode, which catches wrong columns and types but not wrong logic.
- **Where AI still fails here (show it yourself):** published benchmarks put limits on the tools. BIRD's best is about 83% against a 93% human baseline (September 2026). ELT-Bench (April 2025) found the best agent tested built only 3.9% of the required data models correctly, although newer models score higher on the Spider 2.0-DBT leaderboard. In Lab 10 you collect your own evidence by asking an assistant to "add customer region to the revenue report" on an SCD2 dimension. Record whether it joins on `is_current` (wrong for history), fans out a join across two facts, or buckets IST timestamps by UTC date. Log every case where the SQL ran but the number was wrong.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 (tests plus short write-ups) | 25% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Mid-term (AI off): modelling and cost estimation | 10% |
| Final exam (AI off) | 20% |
| Oral defence of P3 | 10% |

**Mastery gate.** You pass when you can, without AI: (1) turn a one-page business brief into a bus matrix and a star schema with a declared grain for every fact, in 45 minutes; (2) write an SCD2 `MERGE` that produces identical results on a second run, and an as-of join that uses it correctly; (3) find a planted double-counting bug in a 10-model dbt project within 30 minutes using reconciliation queries; and (4) cut a provided query's bytes scanned by at least 80% through partitioning, clustering or remodelling, and show the before and after profiles.

## Industry reality

Kimball's dimensional techniques (grain, conformed dimensions, SCD types) remain the shared vocabulary of warehouse teams, and the Kimball Group's technique list is still the standard reference. The engines underneath changed. Snowflake separated storage and compute on cloud object storage (SIGMOD 2016). BigQuery descends from Google's Dremel (VLDB 2010; retrospective in VLDB 2020). Lakehouse table formats bring the same modelling onto open files (DEN305). Razorpay's 2026 write-up describes a medallion architecture on open-source Delta Lake with dbt transformations and over 3,000 workflows. Denormalisation is a measured trade, not a rule: Fivetran's 2022 benchmark shows faster queries and much more storage for one big table.

**Interview questions from this course**

1. *"Design the warehouse for a food-delivery app."* A strong answer asks which decisions the data serves, then declares grains: order-line transactions, an accumulating snapshot of the order lifecycle, and a daily rider snapshot. It names conformed dimensions (customer, restaurant, rider, zone, date with IST handling), picks SCD types per attribute, and discusses late events and cost.
2. *"What is a slowly changing dimension? Implement type 2."* Cover `valid_from`/`valid_to`/`is_current`, change detection with a hash, closing and inserting in one transaction, idempotency on re-run, and the as-of join that consumers must use.
3. *"Star schema, Data Vault or one big table?"* Cover consumers, source volatility, audit needs, team skill, storage vs compute cost (cite the OBT trade-off), and that layers can combine (vault for integration, stars or OBT for serving).
4. *"This revenue dashboard doubled overnight. Debug it."* Check grain changes, a new join that fans out, duplicate loads from a retried job, SCD rows with two current versions, and time-zone boundaries. Reconcile against source control totals.
5. *"Why is this BigQuery or Snowflake query expensive?"* Read the profile: bytes scanned vs bytes needed, missing partition filter, clustering not used, exploding join, spill. Fix and quantify the saving.

## Resources (free first)

- **Course:** [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) (free; modules on data warehousing with BigQuery and analytics engineering with dbt and DuckDB).
- **Reference:** Kimball Group, [Dimensional Modeling Techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/) (free); [CMU 15-445/645 Fall 2026](https://15445.courses.cs.cmu.edu/fall2026/) lectures on storage models and compression.
- **Documentation:** [Snowflake warehouses](https://docs.snowflake.com/en/user-guide/warehouses-overview); [BigQuery](https://cloud.google.com/bigquery/docs/introduction); [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html); [DuckDB](https://duckdb.org/docs/stable/); [dbt](https://docs.getdbt.com/) (including [upgrading to v2](https://docs.getdbt.com/docs/dbt-versions/dbt-upgrade/upgrading-to-v2)); [Apache Parquet format](https://parquet.apache.org/docs/file-format/); [Data Vault Alliance](https://www.datavaultalliance.com/).
- **Papers:** [C-Store](https://web.stanford.edu/class/cs345d-01/rl/cstore.pdf) (2005); [MonetDB/X100](https://www.cidrdb.org/cidr2005/papers/P19.pdf) (2005); [Dremel](https://research.google/pubs/dremel-interactive-analysis-of-web-scale-datasets-2/) (2010) and [Dremel: a decade](https://www.vldb.org/pvldb/vol13/p3461-melnik.pdf) (2020); The Snowflake Elastic Data Warehouse ([SIGMOD 2016](https://dl.acm.org/doi/10.1145/2882903.2903741)).
- **Datasets:** [Olist Brazilian e-commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce); [NYC TLC trip records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) (Parquet, monthly); [GH Archive](https://www.gharchive.org/) (BigQuery public dataset); TPC-H and TPC-DS generators via [DuckDB's tpch extension](https://duckdb.org/docs/stable/core_extensions/tpch) and [TPC](https://www.tpc.org/tpcds/).
- **Paid, worth it:** Kimball and Ross, *The Data Warehouse Toolkit*, 3rd ed. (Wiley, 2013); Kleppmann and Riccomini, *Designing Data-Intensive Applications*, 2nd ed. (O'Reilly, 2026); Reis and Housley, *Fundamentals of Data Engineering* (O'Reilly, 2022).

## Sources

All checked October 2026.

- Fivetran, "Star schema vs. OBT for data warehouse performance" (Kaminsky, 16 Aug 2022). https://www.fivetran.com/blog/star-schema-vs-obt
- AWS Big Data Blog, "How Razorpay achieved 11% performance improvement and 21% cost reduction with Amazon EMR" (9 Mar 2026). https://aws.amazon.com/blogs/big-data/how-razorpay-achieved-11-performance-improvement-and-21-cost-reduction-with-amazon-emr/
- BIRD text-to-SQL leaderboard (top ≈ 82.95%, 7 Sep 2026; human 92.96%). https://bird-bench.github.io/
- Spider 2.0 leaderboards (Spider 2.0-DBT top 65.6, self-reported entries). https://spider2-sql.github.io/
- Jin, Zhu and Kang, "ELT-Bench: An End-to-End Benchmark for Evaluating AI Agents on ELT Pipelines" (arXiv 2504.04808, Apr 2025). https://arxiv.org/abs/2504.04808
- dbt, "Upgrading to v2" (updated 8 Oct 2026). https://docs.getdbt.com/docs/dbt-versions/dbt-upgrade/upgrading-to-v2
- Google Cloud, Data Engineering Agent documentation. https://docs.cloud.google.com/bigquery/docs/data-engineering-agent-pipelines
- DuckDB news (agent mode in the CLI, 9 Oct 2026). https://duckdb.org/news/
- Snowflake, "Overview of warehouses" (credits per size, per-second billing). https://docs.snowflake.com/en/user-guide/warehouses-overview
- Apache Spark 4.1.0 and 4.2.0 release notes (VARIANT GA; metric views; Auto CDC). https://spark.apache.org/releases/spark-release-4.1.0.html ; https://spark.apache.org/releases/spark-release-4-2-0.html

_Last reviewed: 2026-10_
