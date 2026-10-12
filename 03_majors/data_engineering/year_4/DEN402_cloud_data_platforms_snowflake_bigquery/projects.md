# DEN402 · Labs and projects

Use free tiers and trials: the BigQuery sandbox, Snowflake and Databricks trial credits, and a Microsoft Fabric trial capacity. Set budget alerts and hard limits in Lab 1 before running anything else. Each lab records the list prices you used, with the date you read them, because prices change. Labs 2, 3 and 8 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Accounts, budgets and the landscape | Open all accounts with budget alerts and limits; tabulate 8 platforms by architecture and billing unit | Screenshot evidence of limits; landscape table | 3 h |
| 2 · Snowflake warehouses and caches | Run one job on 4 warehouse sizes; run one query cold, warm, from the result cache and metadata-only | Sizing report in credits and seconds; cache explanation | 4 h |
| 3 · Query Profile clinic | Fix 3 slow Snowflake queries using only Query Profile evidence | Before/after profiles and a one-paragraph diagnosis each | 4 h |
| 4 · BigQuery on-demand vs editions | Cost the same workload both ways with dry runs and `INFORMATION_SCHEMA.JOBS` | Cost comparison and break-even utilisation | 4 h |
| 5 · Partitioning, clustering and the DE agent | Cut bytes billed on 10 queries; have the Data Engineering Agent build a pipeline and review it | Bytes-billed table; agent review with defects found | 5 h |
| 6 · Databricks compute and Photon | DEN302 P2 job on job cluster vs serverless, Photon on and off | DBU and run-time comparison | 4 h |
| 7 · Unity Catalog and billing tables | Least-privilege grants for 3 personas; cost by team and job from system tables | Grants, a test per persona, cost report | 4 h |
| 8 · Redshift keys and Fabric capacity | Choose distribution and sort keys and verify with `EXPLAIN`; overload a Fabric trial capacity | Key design with plan evidence; throttling observations | 4 h |
| 9 · Benchmark protocol | Write and dry-run a fair benchmark protocol and a cost calculator | Protocol document and calculator | 4 h |
| 10 · Attribution and guardrails | Attribute a month of spend; add 5 guardrails and trigger each | Attributed bill; guardrail test log | 5 h |
| 11 · 30% cost cut | Cut a provided baseline by at least 30% with every SLO green | Before/after bills, SLO report, change log | 6 h |
| 12 · Policies and residency | Masking and row policies on two platforms; audit log query; RBI-compliant layout | Evidence per role; audit query output; layout diagram | 4 h |
| 13 · AI functions and assistants | Classify 100,000 rows with an in-SQL LLM function; score an assistant on 30 questions | Cost per 1,000 rows; accuracy and failure taxonomy | 4 h |

## Projects

### P1 · Scanning less on a public dataset (L1, ~6 hours)

**Real-world inspiration:** on-demand query billing makes every unnecessary byte cost money. [GH Archive](https://www.gharchive.org/) is available as a BigQuery public dataset with year, month and day tables, and its maintainers advise restricting queries to the needed time ranges to save the free 1 TB monthly quota.

**What to build:** 10 analytical queries over GH Archive (top repositories by new stargazers per week, issue response times for 50 repositories, language trends), first written naively. Then rewrite them, and where useful copy a subset into your own partitioned and clustered tables.

**Acceptance criteria:**
- Every query has a dry-run byte estimate recorded before it is executed.
- Total bytes billed for the 10 queries falls by at least 80% between the naive and final versions, with identical results (checked by comparing outputs).
- The README explains each saving by mechanism (table selection, column pruning, partition filter, clustering, materialisation).
- Total spend for the project stays within the free tier.

**Stretch goals:** the same queries in DuckDB over downloaded hourly files, with time and cost compared.

**What it proves to an employer:** you think about cost per query from the start, not after the bill arrives.

### P2 · Three-platform benchmark and cost calculator (L2, ~15 hours)

**Real-world inspiration:** platform choices are often made from vendor benchmarks that do not match the buyer's workload. A small, honest benchmark on your own workload is worth more.

**What to build:** load 2 years of NYC TLC trips and the taxi-zone lookup into Snowflake, BigQuery and Databricks (trials), with DuckDB on a laptop as a baseline. Run:

- a 20-query analytical mix (dashboard-style, ad hoc, and two heavy joins);
- a nightly incremental pipeline;
- a 10-user concurrency test.

Follow the protocol from Lab 9: cold and warm runs, at least 3 repetitions, documented layouts and sizes. Build a calculator that converts a workload profile into a monthly cost for each platform.

**Acceptance criteria:**
- **Reproducibility:** a second full run of the benchmark reproduces each platform's median timings within 15%.
- **Fairness:** each platform gets the same documented tuning effort (layout, clustering or partitioning, sizing). Caches are controlled and reported.
- **Cost accuracy:** for a held-out workload, the calculator's estimates fall within ±25% of measured cost on each platform.
- **Results:** cost per query, cost per pipeline run, p50/p95 latency under concurrency, and loading time are reported per platform with charts.
- **Decision record:** a 2-page recommendation for a stated organisation (for example, a 30-person Indian logistics startup), with the assumptions that would change it.
- **Budget:** total cloud spend stays within trial credits, and the spend log proves it.

**Stretch goals:** add Redshift Serverless or Fabric; include open-table access (the same Iceberg data read by each platform) and compare with native tables.

**What it proves to an employer:** you can compare platforms with evidence and turn a workload into a budget, a skill needed in every platform decision.

### P3 · Cost engineering and migration for a data platform (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** data platform bills are large enough that companies run dedicated cost programmes. Razorpay reports a 21% cost reduction alongside an 11% performance gain from platform and tuning changes ([AWS blog, 2026](https://aws.amazon.com/blogs/big-data/how-razorpay-achieved-11-performance-improvement-and-21-cost-reduction-with-amazon-emr/)). Migrations between platforms are common and risky, because a translated query can run and still return different numbers.

**What to build:** two parts on one platform environment of your choice (your P2 setup, or a provided synthetic month of query history and billing data at realistic scale).

**Part A: cost programme.**
- Attribution by team, pipeline and dashboard, normalised to a FOCUS-style schema.
- Guardrails: budgets, monitors, maximum bytes billed, cluster policies.
- A prioritised list of savings with estimated and measured impact.
- Implementation of the top changes, with SLO monitoring before and after.

**Part B: migration.**
- Move a 40-model dbt project and its data from one platform to another, using SQLGlot plus hand fixes.
- Move data through Parquet or Iceberg.
- Validate with a key-and-checksum data diff on every model.
- Write a cut-over runbook with rollback.

**Acceptance criteria:**
- **Savings:** measured cost falls by at least 30% against the baseline. Every freshness and latency SLO stays green for the comparison period (a simulated 2 weeks is acceptable).
- **Attribution:** at least 95% of spend is attributed to an owner, and the unattributed remainder is explained.
- **Guardrails:** each guardrail is triggered once in a test and blocks or alerts as designed.
- **Migration correctness:** all 40 models match between platforms. Every row-level difference found during migration is listed with its cause (NULL ordering, time zones, integer division, collation, rounding) and fix.
- **Runbook:** a cut-over and rollback runbook, dry-run end to end.
- **Write-up:** an executive cost report (one page, non-technical), an engineering report, the decision record for the migration, and a 5-minute recorded walkthrough.
- **Budget:** real cloud spend stays within a stated cap (for example, $50 or available trial credits).

**Stretch goals:** a commitment or reservation recommendation with break-even analysis; an in-platform AI feature added under a cost cap and an access policy.

**What it proves to an employer:** you can manage a data platform as a business asset. You cut spend with proof, keep service levels, and move between platforms without changing a single number.

## Feeds into

- [OV06A Building a Modern Data Platform](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06A_building_a_modern_data_platform/README.md): platform selection and cost governance.
- [CLD403 FinOps and Cloud Cost Engineering](../../../cloud_engineering/year_4/CLD403_finops_and_cloud_cost_engineering/README.md): organisation-wide FinOps practice.
- [DEN404 Data Governance, Lineage and Privacy Engineering](../DEN404_data_governance_lineage_and_privacy_engineering/README.md): platform policies as governance controls.
- [DEN501 Frontier Seminar](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md): how these engines are built inside.
- [CAR401 Career Lab II](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): P2 and P3 make strong system-design interview stories.
