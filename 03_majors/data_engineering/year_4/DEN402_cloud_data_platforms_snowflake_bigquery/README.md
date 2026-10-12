# DEN402 · Cloud Data Platforms: Snowflake, BigQuery and Databricks

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [DEN302](../../year_3/DEN302_batch_processing_with_spark/README.md) | [OV06A](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06A_building_a_modern_data_platform/README.md), [DEN501](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md), [CLD403](../../../cloud_engineering/year_4/CLD403_finops_and_cloud_cost_engineering/README.md) |

Part of the [Data Engineering major](../../README.md). [DEN301](../../year_3/DEN301_data_modeling_and_warehousing/README.md) explained warehouse internals in general, and [DEN302](../../year_3/DEN302_batch_processing_with_spark/README.md) and [DEN305](../../year_3/DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md) taught the open-source engines and formats. This course is about the managed platforms most employers pay for (Snowflake, BigQuery, Databricks, Amazon Redshift and Microsoft Fabric): how each is built, how each bills, how to keep the bill under control, and how to choose and migrate between them. General cloud cost practice is in [CLD403](../../../cloud_engineering/year_4/CLD403_finops_and_cloud_cost_engineering/README.md); here the focus is data workloads.

## Why this course matters now

A data platform is often one of a company's largest software bills, and its cost is driven by engineering decisions. Each platform bills a different unit:

- **Snowflake:** credits per running warehouse. Each size up doubles the rate, from 1 credit an hour for X-Small to 512 for 6X-Large, billed per second with a 60-second minimum.
- **BigQuery:** bytes scanned on demand, or slot-hours under its Standard, Enterprise and Enterprise Plus editions.
- **Databricks:** Databricks Units (DBUs).
- **Amazon Redshift Serverless:** Redshift Processing Units (RPUs).
- **Microsoft Fabric:** shared capacity units.

Public cases show the stakes. Razorpay reports cutting cost by 21% and improving performance by 11% on a platform that processes over 1 PB a day, through instance choice, Spot capacity and tuning (2026). Every platform now ships AI inside it: Snowflake Cortex, Databricks Assistant, Gemini in BigQuery with a Data Engineering Agent that Google says has been generally available since April 2026, and Copilot in Fabric. These tools write SQL and pipelines on the platform. Someone still has to read a query profile, spot the unpartitioned scan that costs as much as a laptop every day, judge whether a vendor benchmark applies to their workload, and design a migration that does not change a single number.

## Learning outcomes

By the end you can:

1. **Explain** the architecture of Snowflake, BigQuery, Databricks, Redshift and Fabric (storage, compute, metadata, caching, concurrency), and **predict** how each will execute a given workload.
2. **Translate** a workload into each platform's billing unit, and **estimate** its monthly cost within ±25% before running it.
3. **Tune** queries and tables on each platform (clustering, partitioning, distribution and sort keys, materialisation, caching, warehouse or slot sizing) and **prove** the gain with profiles.
4. **Attribute** cost to teams, pipelines and queries from billing exports and system tables, and **cut** a real cost baseline by at least 30% without breaking service objectives.
5. **Configure** platform security and governance (roles, masking and row policies, network isolation, customer-managed keys, residency), and **map** them to DEN404's requirements.
6. **Use** in-platform AI features responsibly: measure their accuracy on your schema, cap their cost, and govern their data access.
7. **Benchmark** platforms fairly for a stated workload, and **critique** vendor benchmarks.
8. **Plan** a migration between platforms (dialect translation, data movement, validation by data diff, cut-over, exit costs) and **justify** a platform choice in a decision record.

## Chapters and lessons

### Chapter 1 · The managed-platform landscape (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Architecture families | Shared-nothing MPP with managed storage (Redshift RA3), separated storage and elastic compute (Snowflake), serverless distributed query (BigQuery on Dremel), Spark-based lakehouse (Databricks), SaaS on one lake (Fabric OneLake) | Place 8 platforms (including ClickHouse Cloud and MotherDuck) in a table by architecture and billing unit |
| 1.2 What you actually buy | Storage, compute, metadata services, data transfer, support; editions and feature tiers | List every line item on a sample bill from each platform |
| 1.3 Open tables everywhere | Snowflake Iceberg tables, BigQuery BigLake, Databricks Unity Catalog with Delta and Iceberg, Fabric on Delta Parquet, Redshift reading Iceberg | Read one Iceberg table from three platforms |
| 1.4 Free tiers and trials for practice | BigQuery sandbox, Snowflake and Databricks trials, Fabric trial capacity; setting hard budget alerts first | Set up all accounts with budget alerts before running any query |

**Check your understanding:** (1) Why does separating storage from compute change how teams share a platform? (2) Which billing unit punishes a badly written query most directly, and which punishes an idle cluster? (3) What does supporting open tables change, and not change, about lock-in?

### Chapter 2 · Snowflake (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Architecture | Storage layer with immutable micro-partitions, virtual warehouses, cloud services layer (SIGMOD 2016); Gen1 and Gen2 standard warehouses | Load NYC TLC data; inspect micro-partition counts and clustering information |
| 2.2 Caches | Result cache, warehouse local disk cache, metadata-only queries; why benchmarks must control for them | Run one query 4 ways and explain each timing |
| 2.3 Warehouses | Sizes and credits, per-second billing with a 60-second minimum, auto-suspend and auto-resume, multi-cluster warehouses for concurrency, resource monitors | Find the cheapest size for a nightly job by measuring 4 sizes |
| 2.4 Data features | Time Travel and Fail-safe retention, zero-copy cloning, secure data sharing, Streams and Tasks, Dynamic Tables | Build an incremental pipeline with Dynamic Tables; compare with dbt incremental models |
| 2.5 Performance | Clustering keys and automatic clustering cost, search optimisation, Query Profile reading, spilling | Fix 3 slow queries using only Query Profile evidence |

**Check your understanding:** (1) Why can a larger warehouse cost the same or less for a job? (2) What does zero-copy cloning share, and what starts costing money after the clone? (3) When does automatic clustering cost more than it saves?

### Chapter 3 · BigQuery (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Architecture | Dremel execution tree, slots, in-memory shuffle, Colossus storage (VLDB 2010 and 2020 papers) | Read the execution graph of a GH Archive query; map stages to the Dremel model |
| 3.2 On-demand vs editions | Bytes-scanned billing with a free monthly tier; Standard, Enterprise and Enterprise Plus editions; slot-hours with a 1-minute minimum; reservations, autoscaling and commitments | Cost the same workload under on-demand and an edition using dry runs and `INFORMATION_SCHEMA.JOBS` |
| 3.3 Storage design | Partitioned and clustered tables, partition filters required, logical vs physical storage billing, long-term storage | Repartition and cluster a table; measure bytes billed for 10 queries |
| 3.4 Acceleration and pipelines | Materialised views, BI Engine, search indexes; Dataform for SQL pipelines; BigLake for open tables | Replace a scheduled query with a materialised view; compare cost and staleness |
| 3.5 Agents on BigQuery | Gemini in BigQuery and the Data Engineering Agent (pipelines from natural language, with instruction files) | Ask the agent to build a 3-step pipeline; review it with your DEN304 checklist |

**Check your understanding:** (1) Why does `SELECT *` with `LIMIT 10` still bill a full scan on demand? (2) When do editions beat on-demand pricing, and what new risk do they add? (3) What does a required partition filter prevent?

### Chapter 4 · Databricks (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Architecture | Control plane and compute plane, classic vs serverless compute, all-purpose vs job clusters, SQL warehouses | Run the DEN302 P2 job on a job cluster and serverless; compare DBUs and start-up time |
| 4.2 Photon and Delta features | Photon vectorised engine (SIGMOD 2022), liquid clustering, deletion vectors, predictive optimisation | Measure a query mix with Photon on and off; cluster a table with liquid clustering |
| 4.3 Unity Catalog | Catalogs, schemas, grants, lineage, volumes, external locations, system tables | Grant least-privilege access to 3 personas; read lineage from system tables |
| 4.4 Lakeflow | Ingestion connectors, declarative pipelines, jobs (the Databricks Data Engineer exam now weights Lakeflow Jobs at 16%) | Build an ingestion-to-gold pipeline with declarative pipelines and a job |
| 4.5 Cost visibility | Billing system tables, cluster policies, tags, autoscaling and auto-termination | Build a cost report by team and job from `system.billing` tables |

**Check your understanding:** (1) Why is an all-purpose cluster the wrong place for scheduled jobs? (2) What does Photon speed up, and what does it not? (3) What can cluster policies enforce that guidelines cannot?

### Chapter 5 · Amazon Redshift and Microsoft Fabric (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Redshift | RA3 nodes and managed storage, distribution styles and sort keys, concurrency scaling, Redshift Spectrum, zero-ETL integrations | Choose distribution and sort keys for a star schema; verify with `EXPLAIN` |
| 5.2 Redshift Serverless | RPUs, base capacity, usage limits | Cost a spiky workload on provisioned vs Serverless |
| 5.3 Fabric | OneLake as one lake per tenant, Delta Parquet as the shared format, lakehouse and warehouse items, Spark and T-SQL engines, Direct Lake for Power BI | Build a lakehouse and a warehouse item over the same OneLake data |
| 5.4 Fabric capacity | Capacity units shared by all workloads, smoothing and throttling, workload isolation | Overload a trial capacity and observe throttling; design isolation |

**Check your understanding:** (1) What happens to a Redshift join when distribution keys do not match? (2) Why can one heavy Spark notebook slow down Power BI users in a Fabric capacity? (3) When is provisioned capacity cheaper than serverless?

### Chapter 6 · Pricing models and fair benchmarks (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Normalising units | Credits, slots, DBUs, RPUs and capacity units translated to cost per query, per pipeline run and per month | Build a calculator that converts a workload profile into each platform's bill, using prices you record with the date |
| 6.2 Benchmark design | Cold vs warm runs, caching, concurrency, loading time, data layout, tuning effort; TPC-H and TPC-DS and their limits | Write a benchmark protocol for your P2 workload |
| 6.3 Reading vendor benchmarks | Selected queries, tuned vs untuned competitors, list price vs discounted price | Critique two public vendor benchmark posts |
| 6.4 Hidden costs | Egress, cross-region replication, metadata-heavy small queries, minimum billing increments, idle time | Find 5 hidden costs in a provided month of billing data |

**Check your understanding:** (1) Why is "cost per query" misleading for a platform billed by capacity? (2) What would make a benchmark unfair to the platform that loses it? (3) Which hidden cost grows with the number of tiny queries?

### Chapter 7 · Cost control engineering (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Attribution | Tags, labels and query tags; billing exports; the FinOps Foundation's FOCUS format for normalised billing data | Attribute one month of spend to teams and pipelines on two platforms |
| 7.2 Guardrails | Budgets, resource monitors, slot caps, cluster policies, query timeouts, maximum bytes billed | Add 5 guardrails and test that each one triggers |
| 7.3 Workload fixes | Partition filters, clustering, incremental models instead of full rebuilds, materialisation choices, scheduling off-peak, right-sizing | Cut a provided baseline by at least 30% and keep every SLO green |
| 7.4 Commitments and capacity | Reserved capacity, commitments, Spot and Graviton-style instance choices (the Razorpay case) | Model a 1-year commitment; find the break-even utilisation |
| 7.5 Unit economics | Cost per dashboard, per active customer, per model training run; reporting cost to non-engineers | Write a one-page cost report for a business audience |

**Check your understanding:** (1) Why do most cost wins come from a few queries and pipelines? (2) What is the risk of a commitment sized on last year's usage? (3) How do you stop cost savings from silently breaking a freshness SLO?

### Chapter 8 · Security, governance and residency on platforms (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Access control | Role hierarchies, least privilege, service identities, access reviews | Design roles for analysts, engineers, ML and an external partner |
| 8.2 Policies on data | Masking policies, row access policies, policy tags, tag-based policies (continued in [DEN404](../DEN404_data_governance_lineage_and_privacy_engineering/README.md)) | Mask PII by role on two platforms; verify with each role |
| 8.3 Network and keys | Private connectivity, IP allow-lists, customer-managed keys, audit logs | Turn on audit logging and find who read a sensitive table |
| 8.4 Residency | Region choice; India's RBI directive (April 2018) that payment-system data be stored only in India; DPDP Act transfer rules | Design a platform layout for an Indian payments company that meets the RBI directive |

**Check your understanding:** (1) Why should masking be a policy on the data rather than a view per team? (2) What must an audit log answer during a breach investigation? (3) Which platform features help, and which complicate, data residency?

### Chapter 9 · AI inside data platforms (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 LLM functions in SQL | Snowflake Cortex AI functions, BigQuery AI functions with Gemini, Databricks AI Functions; per-row cost and rate limits | Classify 100,000 support tickets in SQL on one platform; report cost per 1,000 rows |
| 9.2 Vector search on the platform | Built-in vector types and indexes vs external vector stores (preview of [DEN403](../DEN403_data_engineering_for_ai_unstructured_data/README.md)) | Build semantic search over a documents table on one platform |
| 9.3 Assistants and agents | Text-to-SQL assistants, pipeline agents, MCP access to platforms; measuring accuracy on your own schema | Score an assistant on 30 questions over your marts; compare with BIRD-style accuracy claims |
| 9.4 Governing AI use | What data AI features may see, logging prompts and outputs, cost caps, model version pinning | Write an AI-use policy for a data platform and enforce two parts of it |

**Check your understanding:** (1) Why can an LLM function in a `SELECT` become the most expensive part of a pipeline? (2) Why is accuracy on a public benchmark weak evidence for accuracy on your schema? (3) Which controls must exist before an agent may run DDL?

### Chapter 10 · Choosing and migrating (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Decision framework | Workload mix, team skills, ecosystem, governance, open formats, cost predictability, exit cost | Write decision records for a startup, an Indian bank and a global retailer (illustrative) |
| 10.2 SQL translation | Dialect differences; transpilers such as SQLGlot; vendor migration tools; what translation cannot fix (semantics, NULL and time-zone behaviour) | Translate 50 queries with SQLGlot; hand-fix and document the failures |
| 10.3 Moving and validating data | Bulk export to Parquet or Iceberg, incremental sync, data-diff validation by key and checksum | Migrate a schema between two platforms and prove equality |
| 10.4 Cut-over | Parallel runs, consumer migration, rollback plan, decommissioning | Write the cut-over runbook for P3 |

**Check your understanding:** (1) Why is "the queries ran" not proof that a migration is correct? (2) Which dialect differences change results silently? (3) What is the real exit cost of a platform?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Accounts, budgets and the landscape | Budget alerts live; platform table |
| 2 | 2 | Lab 2 · Snowflake warehouses and caches | Sizing report |
| 3 | 2 | Lab 3 · Query Profile clinic | Three fixes; **P1 due** |
| 4 | 3 | Lab 4 · BigQuery on-demand vs editions | Cost comparison |
| 5 | 3 | Lab 5 · Partitioning, clustering and the DE agent | Bytes-billed report, agent review |
| 6 | 4 | Lab 6 · Databricks compute and Photon | DBU comparison |
| 7 | 4 | Lab 7 · Unity Catalog and billing tables | Mid-term (AI off): architectures and cost units |
| 8 | 5 | Lab 8 · Redshift keys and Fabric capacity | Key design, throttling notes |
| 9 | 6 | Lab 9 · Benchmark protocol | Protocol and calculator; **P2 due** |
| 10 | 7 | Lab 10 · Attribution and guardrails | Attributed bill |
| 11 | 7 | Lab 11 · 30% cost cut | Before/after cost with SLOs |
| 12 | 8 | Lab 12 · Policies and residency | Masking and audit evidence |
| 13 | 9 | Lab 13 · AI functions and assistants | Cost and accuracy report |
| 14 | 10 | Migration review | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** drafting platform-specific SQL and configuration; translating between dialects (always followed by a data diff); summarising billing exports; explaining unfamiliar profile operators. Tools: Snowflake Cortex, Databricks Assistant, Gemini in BigQuery and its Data Engineering Agent, Copilot in Fabric; Claude Code, GitHub Copilot or Cursor with platform CLIs.
- **Do without AI (drills):** estimating a workload's monthly cost in each billing unit; choosing Redshift distribution keys; reading Query Profiles and execution graphs; the mid-term and final. You must be able to check a cost or performance claim yourself.
- **Verify AI output by:** (1) dry runs and `EXPLAIN` before execution; (2) comparing bytes, credits, DBUs or slot-time before and after any suggested change; (3) data diffs for every translated or rewritten query; (4) checking every feature or setting name against the platform's current documentation, because platform features and names change often.
- **Where AI still fails here (show it yourself):** in Lab 13, score an in-platform assistant on 30 questions over your own marts and log each wrong answer by cause (wrong join, wrong grain, wrong filter, invented column). In Lab 11, ask an assistant to "cut this platform's cost by 30%". Record which suggestions were generic (auto-suspend everything), which were harmful (dropping clustering on a hot table), and which actually helped, measured on the bill.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–13 | 25% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 20% |
| Oral defence of P3 | 10% |

**Mastery gate.** You pass when you can, without AI: (1) given a workload description, estimate its monthly cost on Snowflake, BigQuery and Databricks within ±25% of measured cost; (2) given one month of query history and billing data, find and implement changes that cut cost by at least 30% with every freshness and latency objective still met; (3) explain, on a whiteboard, why the same query behaves differently on two platforms, using their architectures.

## Industry reality

All five platforms are in wide use, and many companies run two or more. Razorpay's 2026 account describes moving from a third-party platform to Amazon EMR with Spark and open-source Delta Lake, with measured savings. Platform vendors have converged on open table formats, built-in AI functions and agents, and serverless compute. Engineers who understand billing units and can prove savings are valued because the bills are large and visible.

**Interview questions from this course**

1. *"Explain Snowflake's architecture and how it bills."* A strong answer covers micro-partitions on object storage, virtual warehouses, the cloud services layer, caches, credits by size, per-second billing with a 60-second minimum, auto-suspend, and multi-cluster warehouses for concurrency.
2. *"Our BigQuery bill doubled. What do you do?"* Query `INFORMATION_SCHEMA.JOBS` for top spenders, check partition filters and clustering, look for repeated full scans and `SELECT *`, consider materialised views, compare on-demand vs editions, and add maximum-bytes-billed guardrails.
3. *"Snowflake, BigQuery or Databricks for our company?"* Cover the workload mix (SQL analytics vs Spark and ML vs streaming), team skills, open-table strategy, governance, cost predictability, ecosystem and exit cost. End with a recommendation and what would change it.
4. *"A Databricks job costs too much. How do you investigate?"* Cover billing system tables, cluster type (all-purpose vs job vs serverless), autoscaling and idle time, Photon suitability, data layout and skew (from DEN302), and spot or instance choices.
5. *"How would you migrate 500 dbt models from Redshift to Snowflake?"* Cover dialect translation and its limits, data movement through open formats, parallel runs, data-diff validation by key, consumer cut-over, rollback, and decommissioning.

## Resources (free first)

- **Documentation:** Snowflake [warehouses](https://docs.snowflake.com/en/user-guide/warehouses-overview), [cost overview](https://docs.snowflake.com/en/user-guide/cost-understanding-overall), [Time Travel](https://docs.snowflake.com/en/user-guide/data-time-travel), [Dynamic Tables](https://docs.snowflake.com/en/user-guide/dynamic-tables-about), [Iceberg tables](https://docs.snowflake.com/en/user-guide/tables-iceberg); BigQuery [editions](https://cloud.google.com/bigquery/docs/editions-intro), [partitioned tables](https://cloud.google.com/bigquery/docs/partitioned-tables), [`INFORMATION_SCHEMA.JOBS`](https://cloud.google.com/bigquery/docs/information-schema-jobs), [Data Engineering Agent](https://docs.cloud.google.com/bigquery/docs/data-engineering-agent-pipelines); Databricks [Photon](https://docs.databricks.com/aws/en/compute/photon), [liquid clustering](https://docs.databricks.com/aws/en/delta/clustering), [billing system tables](https://docs.databricks.com/aws/en/admin/system-tables/billing); Amazon Redshift [Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-serverless.html) and [distribution and sort keys](https://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html); Microsoft Fabric [OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview) and [capacity licences](https://learn.microsoft.com/en-us/fabric/enterprise/licenses).
- **Course:** [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) (free; BigQuery warehousing module).
- **Tools:** [SQLGlot](https://github.com/tobymao/sqlglot) (open-source SQL transpiler).
- **Papers:** The Snowflake Elastic Data Warehouse ([SIGMOD 2016](https://dl.acm.org/doi/10.1145/2882903.2903741)); [Dremel](https://research.google/pubs/dremel-interactive-analysis-of-web-scale-datasets-2/) and [Dremel: a decade](https://www.vldb.org/pvldb/vol13/p3461-melnik.pdf); [Photon](https://people.eecs.berkeley.edu/~matei/papers/2022/sigmod_photon.pdf) (SIGMOD 2022).
- **Regulation:** RBI, [Storage of Payment System Data](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244) (6 April 2018).
- **Certifications** (optional; see the [major page](../../README.md) for an honest value note): SnowPro Core and SnowPro Advanced: Data Engineer; Google Cloud Professional Data Engineer; Databricks Certified Data Engineer Associate and Professional; AWS Certified Data Engineer – Associate; Microsoft Certified: Fabric Data Engineer Associate (DP-700).

## Sources

All checked October 2026.

- Snowflake, "Overview of warehouses" (credits per size from X-Small 1 to 6X-Large 512 per hour; per-second billing, 60-second minimum; Gen2 not default and not in all regions). https://docs.snowflake.com/en/user-guide/warehouses-overview
- Google Cloud, BigQuery editions (Standard, Enterprise, Enterprise Plus; slot-hours with a 1-minute default minimum; autoscaling; optional commitments). https://cloud.google.com/bigquery/docs/editions-intro
- GH Archive (BigQuery: 1 TB of data processed per month free). https://www.gharchive.org/
- Google Cloud, Data Engineering Agent documentation; Google Cloud blog update giving general availability on 22 Apr 2026. https://docs.cloud.google.com/bigquery/docs/data-engineering-agent-pipelines
- Databricks, Data Engineer Associate exam page (topic weights including Lakeflow Jobs 16%; $200; 90 minutes; valid 2 years). https://www.databricks.com/learn/certification/data-engineer-associate
- AWS Big Data Blog, Razorpay on Amazon EMR (9 Mar 2026). https://aws.amazon.com/blogs/big-data/how-razorpay-achieved-11-performance-improvement-and-21-cost-reduction-with-amazon-emr/
- Reserve Bank of India, "Storage of Payment System Data", RBI/2017-18/153 (6 Apr 2018). https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244

_Last reviewed: 2026-10_
