# DAN304 · Labs and projects

Every lab and project is a dbt project in a Git repository with a README, a green CI run on GitHub Actions, `sqlfluff` passing, and a generated docs site. DuckDB is the default warehouse so that everything runs free on a laptop; BigQuery (sandbox) is used where a lab says so. Every claim of "no change" is backed by a data diff.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · jaffle-shop on DuckDB | Install dbt with the DuckDB adapter; build, test and document the `jaffle-shop` example; break and fix one test | Repo, a DAG drawn by hand before you looked, and the `dbt build` log | 3 h |
| 2 · Layered project | Restructure a flat 12-model project into staging, intermediate and marts with naming conventions | Before/after DAGs; a table mapping every old model to its new home | 4 h |
| 3 · Bus matrix, grain and SCD | Bus matrix for an illustrative quick-commerce business; build `dim_customer` as Type 2 with a snapshot; point-in-time join | Matrix, snapshot config, and a test proving each order joins to exactly one customer version | 5 h |
| 4 · Test suite and unit tests | 25 generic tests, 3 singular tests, 2 unit tests, one enforced contract, source freshness | Test plan with owner and severity; evidence that each test fails when you break the data on purpose | 4 h |
| 5 · Incremental under late data | Convert an event model to incremental with `merge` and with `microbatch`; inject 2% late events | Diff against full refresh for each configuration; the lookback window that reaches zero diff | 4 h |
| 6 · Docs, lineage, exposures | Write useful descriptions for 10 models; declare exposures for your DAN303 dashboards; impact analysis of a rename | Docs site; an impact-analysis note listing every affected exposure | 3 h |
| 7 · Slim CI and data diffs | GitHub Actions running modified models and children with deferral; `audit_helper` comparison on a refactor | Workflow file; CI run under 5 minutes; a zero-difference report | 4 h |
| 8 · Semantic models | Define entities, dimensions, measures and 6 metrics in MetricFlow; repeat 3 metrics in Cube or a Power BI semantic model | Metric definitions; a table showing identical results across both tools and an independent SQL query | 5 h |
| 9 · AI over raw vs semantic | 30 gold questions; one assistant answers over raw tables, then over your semantic layer with descriptions and verified queries | Accuracy for both conditions, failure categories, and 3 examples of out-of-scope questions handled correctly or not | 4 h |
| 10 · Versions and migration | Ship `fct_orders` v2 with a breaking change and a deprecation date; migrate a 400-line legacy query into models | Version config, migration note for consumers, and a reconciliation of the legacy and new outputs | 4 h |

## Projects

### P1 · Marketplace star schema in dbt (L1, ~6 hours)

**Real-world inspiration.** Marketplaces model orders, items, payments, sellers and reviews into a star schema so that every dashboard starts from the same facts. The Olist Brazilian e-commerce dataset has exactly this shape.

**What to build.** A dbt project on DuckDB from the raw Olist CSVs: one staging model per source table, an `fct_order_items` fact, an `fct_orders` fact, and `dim_customer`, `dim_seller`, `dim_product` and `dim_date` (with both calendar and Indian-style April–March fiscal attributes, as practice for later work).

**Acceptance criteria**
- A grain statement is in the description of every fact and dimension.
- At least 20 tests pass, including uniqueness at the declared grain and relationships from every foreign key.
- The sum of item prices plus freight in `fct_order_items` reconciles with payments in `fct_orders` within a documented tolerance, and every exception is explained.
- `dbt build` from a clean clone completes in under 2 minutes on a laptop.
- `sqlfluff lint` returns zero violations.

**Stretch goals.** Add an accumulating snapshot for the order lifecycle (purchase, approval, carrier hand-off, delivery); publish the docs site with GitHub Pages.

**What it proves to an employer.** You can turn raw source tables into a documented, tested dimensional model, which is the first task of most analytics engineering jobs.

### P2 · Incremental event marts with governed metrics (L2, ~15 hours)

**Real-world inspiration.** Product analytics teams process large event streams every day, and late or duplicate events are the main cause of numbers changing after the fact. The GA4 sample e-commerce dataset in BigQuery is real (obfuscated) event data.

**What to build.** Using the BigQuery public dataset `ga4_obfuscated_sample_ecommerce` (or an export of it into DuckDB): staging that flattens nested event parameters, a deduplicated `fct_events`, an incremental `fct_sessions`, a daily `fct_user_activity` periodic snapshot, and a semantic layer with 8 metrics (sessions, users, conversion rate, revenue per user, add-to-cart rate, 7-day retention, AOV, purchase frequency). CI builds modified models and their children.

**Acceptance criteria**
- After replaying a batch with 2% late events, incremental models match a full refresh with zero differences (data diff report committed).
- All 8 metrics match an independent hand-written SQL query exactly for 3 date ranges.
- Ratio metrics are defined as ratios of sums, and a test proves that they do not average daily ratios.
- CI runs on every pull request in under 5 minutes, with lint, build and tests.
- Bytes processed per daily run on BigQuery are reported, with partition pruning shown.

**Stretch goals.** Microbatch strategy with backfill; an exposure-linked Metabase or Looker Studio dashboard reading the semantic layer; a second semantic-layer implementation and a cross-tool reconciliation.

**What it proves to an employer.** You can run event models that stay correct under late data, and you can make metrics consistent by construction rather than by meetings.

### P3 · Governed analytics layer for a payments business, with an AI evaluation (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Indian payment aggregators and fintechs report gross payment value, success rates, refunds and settlement times to merchants, finance and regulators, and these numbers must agree everywhere. NPCI publishes monthly UPI aggregates that give realistic orders of magnitude. The business below is illustrative and simulated; it does not describe any real company.

**What to build.**
1. A seeded data generator for an illustrative payment aggregator: merchants, payment attempts (UPI, cards, net banking), failures with reason codes, refunds, chargebacks and daily settlements, with realistic messiness (duplicates, late status updates, time-zone mixing).
2. A dbt project with: a payment-attempt transaction fact, a refund fact, a settlement accumulating snapshot, a daily merchant balance periodic snapshot (semi-additive), Type 2 merchant dimension, contracts on all public models, access groups, and one versioned model.
3. A semantic layer with 12 metrics, including GPV, payment success rate, refund rate, take rate, net revenue and settlement turnaround time, each with an owner and a definition note.
4. A migration: a provided 400-line legacy "monthly merchant MIS" SQL report rebuilt as models, with a parallel-run reconciliation.
5. An AI evaluation: 30 gold questions answered by one assistant over raw tables and over the semantic layer.
6. Exposures for at least two dashboards (Evidence, Metabase or Power BI).

**Acceptance criteria**
- The full build and all tests run from a clean clone with one command; at least 60 tests; every public model has an enforced contract.
- The legacy and new MIS outputs match to the paisa for 3 months, or every difference is explained and approved in a written note.
- Semi-additive balances are never summed across days in any metric or dashboard (a singular test enforces it).
- AI evaluation reports accuracy in both conditions with the same 30 questions, a failure taxonomy, and the out-of-scope behaviour.
- Docs site, lineage, an architecture diagram and a 2-page design note explaining grain choices and trade-offs.
- Code-review defence: a reviewer plants one bug in your project, and you find it with your tests or diffs within 20 minutes.

**Stretch goals.** Deploy the warehouse to BigQuery with partitioned, clustered facts; add data contracts on the generator's output; publish the metric definitions in the Apache Ossie format.

**What it proves to an employer.** You can build the trusted layer that finance, product and AI assistants all read from, prove it matches the legacy numbers, and measure how much it improves AI answers. This is the core of analytics engineering roles at fintechs, global capability centres and product companies.

## Feeds into

- [DAN404 Data Governance, Quality and Privacy for Analysts](../../year_4/DAN404_data_governance_quality_and_privacy_for_analysts/README.md): contracts, owners and metric governance extend to access, PII and audit.
- [DAN401 AI-Augmented Analytics](../../year_4/DAN401_ai_augmented_analytics_text_to_sql_copilots/README.md): the Lab 9 and P3 evaluations grow into a full text-to-SQL evaluation programme.
- [DAN403 Domain Analytics](../../year_4/DAN403_domain_analytics_finance_marketing_operations/README.md): finance and operations models reuse the fact types from P3.
- [OV06 Data Platform and Analytics Engineering](../../../../04_overlaps/OV06_data_platform_analytics_engineering/README.md): OV06A builds the platform underneath; OV06B builds self-serve analytics with AI on top of the semantic layer.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): P3 is a strong co-op portfolio piece.
