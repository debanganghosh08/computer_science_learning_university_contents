# DAN304 · Analytics Engineering: dbt, Modeling and Semantic Layers

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [FND115](../../../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | [DAN404](../../year_4/DAN404_data_governance_quality_and_privacy_for_analysts/README.md), [DAN401](../../year_4/DAN401_ai_augmented_analytics_text_to_sql_copilots/README.md), [OV06A](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06A_building_a_modern_data_platform/README.md), [OV06B](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06B_semantic_layers_and_self_serve_analytics_with_ai/README.md) |

Part of the [Data Analysis major](../../README.md). Assumes the warehouse SQL, grain discipline and query testing from [DAN301](../DAN301_spreadsheets_to_sql_analytical_querying_in_depth/README.md) and the star schemas from [DAN303](../DAN303_data_visualization_and_storytelling/README.md); taking DAN301 first is strongly recommended. Ingestion, orchestration and lakehouse storage belong to Data Engineering ([DEN304](../../../data_engineering/year_3/DEN304_orchestration_and_pipelines_airflow_and_dagster/README.md), [DEN305](../../../data_engineering/year_3/DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md)). This course owns the layer between raw tables and every number a business reads.

## Why this course matters now

Analytics engineering applies software engineering to analysis: models in version control, tests, documentation, code review and one agreed definition per metric. In dbt Labs' 2025 survey of 459 data practitioners, 80% used AI in their daily work (up from 30% a year earlier), yet poor data quality was still the most-cited challenge (over 56%), and increasing trust in data remained the top objective. The tools are consolidating: Fivetran and dbt Labs completed their merger on 1 June 2026, and dbt's documentation now describes a Rust-based engine (v2) that understands SQL across dialects and catches errors before they reach the warehouse. Semantic layers have become the context that AI tools read. Snowflake's Cortex Analyst generates SQL from semantic views and verified queries, Looker's Conversational Analytics is grounded in LookML, and Microsoft warns that Copilot returns "generic or inaccurate results" on unprepared models. In one benchmark, GPT-4 answered 16% of enterprise questions correctly over raw SQL schemas and 54% over a knowledge-graph representation of the same data (Sequeda et al., 2023). The person who designs the grain, the tests and the metric definitions decides whether AI answers are right.

## Learning outcomes

By the end you can:

1. **Design** a dimensional model with Kimball's four-step process: business process, grain, dimensions, facts. **Choose** between a star schema and a one-big-table design, and **justify** the choice.
2. **Build** a layered dbt project (sources, staging, intermediate, marts) with clear naming, `ref`/`source` lineage and appropriate materialisations.
3. **Test** data and logic: generic and singular tests, unit tests with mocked inputs, source freshness and enforced model contracts, with severity thresholds that match the risk.
4. **Implement** incremental models (merge, insert-overwrite and microbatch strategies) and snapshots for slowly changing dimensions. **Handle** late-arriving data correctly.
5. **Ship** analytics code through Git, pull-request review and CI that builds only modified models and their dependents. **Prove** a refactor changed no numbers.
6. **Define** metrics once in a semantic layer (MetricFlow or an equivalent) and **serve** them consistently to BI tools and AI assistants.
7. **Prepare** a semantic model for AI consumption (descriptions, synonyms, verified queries) and **measure** the accuracy change.
8. **Govern** models across teams with access levels, versions, owners and deprecation.

## Chapters and lessons

### Chapter 1 · The analytics engineering job (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 From reports to products | ELT (load raw, transform in the warehouse); why trust, not tooling, is the goal | Map a messy reporting setup (illustrative) to an ELT design |
| 1.2 The stack in 2026 | Ingestion (Fivetran, Airbyte), warehouse (BigQuery, Snowflake, Databricks, DuckDB), transformation (dbt, SQLMesh, Dataform), BI, semantic layer | Draw the stack for 3 company sizes |
| 1.3 dbt engines | dbt v1 (Python) and v2 (Rust, SQL-aware, default install per dbt docs, Oct 2026); adapters; what runs where | Install dbt with the DuckDB adapter; run the `jaffle-shop` project |
| 1.4 The role | Analytics engineer vs data analyst vs data engineer; what each owns | Read 5 job posts; tabulate the skills asked for |

**Check your understanding:** Why did transformation move from ETL tools into the warehouse? What does an analytics engineer own that a data engineer usually does not? Why is "trust in data" a better goal than "more dashboards"?

### Chapter 2 · dbt fundamentals (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Models and the DAG | `ref`, `source`, compiled SQL, the dependency graph, selectors | Build 6 models; draw the DAG by hand, then compare with `dbt docs` |
| 2.2 Layers | Staging (one per source table: rename, cast, dedupe), intermediate (business logic), marts (facts and dimensions) | Restructure a flat project into layers |
| 2.3 Materialisations | View, table, ephemeral, incremental, materialised view; cost and freshness trade-offs | Choose and justify a materialisation for 8 models |
| 2.4 Jinja and macros | Variables, loops, macros, packages (`dbt-utils`); when Jinja makes SQL unreadable | Write a macro for Indian fiscal-year columns; refactor one over-templated model |
| 2.5 Seeds and configuration | Seeds for small reference tables; `dbt_project.yml` configs and inheritance | Seed a state-code-to-region mapping |

**Check your understanding:** Why should staging models do almost no business logic? When is an ephemeral model a bad idea? What does `ref` give you that a hard-coded table name does not?

### Chapter 3 · Dimensional modelling for analysts (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Four steps | Business process, grain, dimensions, facts (Kimball); the bus matrix of processes × conformed dimensions | Bus matrix for an illustrative quick-commerce business |
| 3.2 Fact tables | Transaction, periodic snapshot, accumulating snapshot, factless; additive, semi-additive (balances) and non-additive (ratios) facts | Model order lines, daily inventory snapshots and an order-lifecycle accumulating snapshot |
| 3.3 Dimensions | Surrogate keys, conformed, role-playing dates (order, ship, deliver), degenerate and junk dimensions | Build `dim_customer`, `dim_product`, `dim_date` with Indian fiscal attributes |
| 3.4 Slowly changing dimensions | Type 1 vs Type 2; dbt snapshots (timestamp vs check strategy); point-in-time joins | Track a customer's city changes; join orders to the city valid at order time |
| 3.5 Star vs one big table | Wide denormalised tables in columnar warehouses; when they help BI and AI tools, when they multiply inconsistency | Benchmark a star and a wide table on 3 dashboard queries |
| 3.6 Other patterns | Data vault and activity schema in outline; why most analytics teams still use stars | One-page comparison memo |

**Check your understanding:** Why must the grain be declared before choosing facts? Why can you not sum an account-balance fact across days? What breaks if you join today's customer attributes to last year's orders?

### Chapter 4 · Testing data and logic (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Generic tests | `unique`, `not_null`, `accepted_values`, `relationships`; `dbt-utils` and `dbt-expectations` tests | Add 25 tests to your marts |
| 4.2 Singular tests | SQL that returns failing rows; reconciliation to finance totals; business rules | "Refunds never exceed the original payment" |
| 4.3 Unit tests | Mocked inputs and expected outputs for model logic (dbt unit tests) | Unit-test the cohort and fiscal-year logic |
| 4.4 Freshness and contracts | Source freshness SLAs; enforced model contracts (column names, types, constraints) | A contract on `fct_orders` that fails on a type change |
| 4.5 Test strategy | What to test at sources vs marts; severity, `warn_if`/`error_if` thresholds; alert fatigue | Write a test plan with owners and severities |

**Check your understanding:** What is the difference between a data test and a unit test, and which catches a wrong `CASE` statement? Why can too many failing-but-ignored tests be worse than none? Which three tests would you put on every fact table?

### Chapter 5 · Incremental models and snapshots (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Why incremental | Processing only new data; cost and run time; the correctness risk | Convert a 50-million-row event model to incremental |
| 5.2 Strategies | Append, `merge` with `unique_key`, `delete+insert`, `insert_overwrite` by partition, `microbatch` | Implement two strategies; compare cost and results |
| 5.3 Late-arriving data | Lookback windows, idempotent reruns, backfills, full refresh policy | Inject 2% late events; show which configuration loses them |
| 5.4 Partitioning and clustering | dbt configs for BigQuery and Snowflake; pruning-friendly filters | Partition and cluster a fact table; measure bytes saved |

**Check your understanding:** Why can an incremental model drift from a full refresh over months? What does "idempotent" mean for a daily job, and how do you test it? When is a full refresh the right answer?

### Chapter 6 · Documentation and lineage (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Writing definitions | Descriptions that say what, grain, caveats and owner, not "the customer id column" | Document 10 models and 60 columns |
| 6.2 Docs site and lineage | `dbt docs`, column-level lineage, impact analysis before a change | Trace which dashboards break if a column is renamed |
| 6.3 Exposures | Declaring dashboards, notebooks and ML models that depend on models | Add exposures for your DAN303 dashboards |
| 6.4 Catalogues | How dbt metadata feeds catalogues (DataHub, OpenMetadata, Unity Catalog) | Load your project metadata into one catalogue |

**Check your understanding:** What makes a column description useful to a stranger, or to an AI assistant? Why declare exposures at all? How does lineage change the cost of renaming a column?

### Chapter 7 · Version control and CI/CD for analytics (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Git for analysts | Branches, small pull requests, review checklists for SQL models | Review 3 classmates' PRs with the DAN301 checklist |
| 7.2 Environments | Development and production schemas, targets, secrets out of code | Separate dev and prod targets on DuckDB and BigQuery |
| 7.3 Slim CI | Build only modified models and their children (`state:modified+`), defer to production | A GitHub Actions workflow that runs in under 5 minutes |
| 7.4 Proving a refactor | Data diffs: row counts, key sets and aggregates before vs after (`audit_helper`) | Refactor a model and prove zero changes |
| 7.5 Linting and pre-commit | SQLFluff with dbt templater; YAML checks | Pre-commit hooks that block unlinted SQL |

**Check your understanding:** Why should CI build downstream models, not just the one you changed? How do you prove a refactor changed no numbers? What belongs in a pull request description for a model change?

### Chapter 8 · Semantic layers and metrics (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Why metrics drift | Five dashboards, five "revenue" definitions; metrics in BI tools vs metrics in code | Find 4 conflicting definitions in an illustrative BI estate |
| 8.2 Semantic models | Entities (join keys), dimensions, measures; MetricFlow (Apache 2.0 since late 2025) | Semantic models for orders and customers |
| 8.3 Metric types | Simple, ratio, cumulative, derived and conversion metrics; time grains and offsets | Define GMV, net revenue, AOV, repeat rate and 7-day conversion |
| 8.4 Other semantic layers | LookML, Cube, Power BI semantic models, Snowflake semantic views, Databricks metric views, Malloy | Define the same 3 metrics in a second tool; compare |
| 8.5 Interchange and governance | The Open Semantic Interchange specification (now Apache Ossie): one YAML/JSON format across tools; metric owners and certification | Export your metrics through an Ossie converter or document the mapping by hand |

**Check your understanding:** Why is a ratio metric defined as ratio of sums, and where do BI tools get this wrong? What should the semantic layer own, and what should stay in marts? What happens to trust when two tools compute "active users" differently?

### Chapter 9 · Semantic layers as AI context (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Evidence | Sequeda et al. (16% vs 54%); vendor guidance from Microsoft, Snowflake and Google | Summarise what each vendor says the model needs |
| 9.2 Preparing a model for AI | Descriptions, synonyms, sample values, hidden fields, verified queries and answers | Prepare your semantic model for an assistant |
| 9.3 Measuring the gain | A 30-question gold set; accuracy over raw tables vs over the semantic layer | Run the comparison with one assistant; report the change |
| 9.4 Failure modes that remain | Questions outside the model, ambiguous terms, stale definitions, permissions | Write the "out of scope" behaviour you want and test it |

**Check your understanding:** Why does an AI assistant do better over a semantic layer than over raw tables? What should an assistant do when a question is outside the model? Who must approve a "verified answer"?

### Chapter 10 · Governing models across teams (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Groups and access | Private, protected and public models; owners | Restrict intermediate models to their group |
| 10.2 Versions and deprecation | Model versions, migration windows, deprecation dates | Ship `fct_orders` v2 with a breaking change and a migration plan |
| 10.3 Multi-project setups | Cross-project references, data products, domain ownership | Split your project into two with a public interface |
| 10.4 Migrating legacy SQL | Moving stored procedures and spreadsheet logic into dbt; reconciling during parallel runs | Migrate a 400-line legacy report query into 5 models with a passing reconciliation |

**Check your understanding:** Why make most models private? How long should a deprecated model live, and who decides? What is the riskiest week of a migration, and how do you de-risk it?

### Chapter 11 · AI in the analytics engineering workflow (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Generating models and docs | dbt's built-in assistant, Claude Code, Cursor and GitHub Copilot for models, YAML, tests and descriptions | Generate a staging layer for a new source; review every line |
| 11.2 Failure modes | Plausible joins at the wrong grain, tests that cannot fail, descriptions that restate column names, hallucinated macros | Find the 6 planted problems in an AI-generated project |
| 11.3 Guardrails | CI, contracts, data diffs and review as the safety net for AI-written code | Make CI catch each planted problem |
| 11.4 Final polish | Portfolio-ready README, lineage screenshots, test coverage summary | P3 submission and review |

**Check your understanding:** How do you tell a test that protects something from a test that cannot fail? Why do AI-written descriptions often add no information, and how do you fix that? Which guardrail catches a wrong-grain join that passes all generic tests?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · jaffle-shop on DuckDB | Stack diagram |
| 2 | 2 | Lab 2 · Layered project | — |
| 3 | 3 | Lab 3 · Bus matrix and grain | Bus matrix |
| 4 | 3 | Lab 3 (cont.) · SCD snapshots | **P1 due** |
| 5 | 4 | Lab 4 · Test suite and unit tests | Test plan |
| 6 | 5 | Lab 5 · Incremental under late data | Mid-term (modelling, AI off) |
| 7 | 6 | Lab 6 · Docs, lineage, exposures | — |
| 8 | 7 | Lab 7 · Slim CI and data diffs | — |
| 9 | 8 | Lab 8 · Semantic models | **P2 due** |
| 10 | 8 | Lab 8 (cont.) · Second semantic layer | — |
| 11 | 9 | Lab 9 · AI accuracy over raw vs semantic | Accuracy report |
| 12 | 10 | Lab 10 · Versions and migration | — |
| 13 | 11 | AI-generated project audit | — |
| 14 | 11 | Polish | **P3 due** |
| 15 | Review | Code review defence of P3 | Final practical (AI off) |

## Working with AI in this course

- **Use AI for:** scaffolding staging models and YAML from a source schema; drafting column descriptions you then rewrite; suggesting tests; explaining adapter-specific configs; converting legacy SQL dialects. dbt's assistant, Claude Code, Cursor and GitHub Copilot all do this.
- **Do without AI (drills):** grain statements and bus matrices; dimensional designs on paper; predicting incremental behaviour under late data; reviewing a PR; the mid-term and final practical.
- **Verify AI output by:**
  - compiling and running every generated model in CI;
  - reconciling each new mart against an independent query;
  - running data diffs on every refactor;
  - mutation-testing your tests (break the data on purpose and check that a test fails);
  - reading every description for information a stranger could not guess from the column name.
- **Where AI still fails here:** on Spider 2.0-DBT, a benchmark of 68 dbt project tasks, the top leaderboard entry scored 65.6 (October 2026), well below the scores reported for single-query text-to-SQL. Your own audit in Chapter 11 is the evidence that matters: log every AI-written model that compiled and passed generic tests but produced wrong numbers.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 25% |
| Mid-term (modelling, AI off) | 10% |
| Final practical (AI off) + code-review defence of P3 | 15% |

**Mastery gate.** You pass when you can: (1) with AI off, design a star schema with a bus matrix for an unseen business description in 45 minutes, stating the grain of every fact; (2) with AI off, given a dbt project with a planted wrong-grain join, a broken incremental filter and a test that cannot fail, find and fix all three in 60 minutes; (3) define 5 metrics in a semantic layer whose results match an independent SQL calculation exactly, and show an AI assistant answering 10 questions through it with accuracy measured against a gold set.

## Industry reality

"Analytics engineer" is now a common title at product companies and global capability centres, and job posts typically list dbt, SQL, a cloud warehouse, Git and a BI tool. GitLab publishes its data team's dbt conventions in its public handbook, one of the few large real-world examples you can read. The Fivetran and dbt Labs merger (completed 1 June 2026) and the open-sourcing of MetricFlow (October 2025) show where the industry is heading: ingestion, transformation and metric definitions in one governed layer that BI tools and AI agents both read.

**Interview questions from this course**

1. *"Design the data model for an order-to-delivery process."* Strong answer: names the business processes; declares grains; an order-line transaction fact and an accumulating snapshot for lifecycle timestamps; conformed customer, product, store and date dimensions; Type 2 where history matters.
2. *"Your incremental model's numbers drift from a full refresh. Why?"* Strong answer: late-arriving or updated rows outside the filter window, a missing or non-unique `unique_key`, time-zone boundaries; fixes with lookback windows, merge strategy and a scheduled reconciliation.
3. *"How do you make sure revenue means the same thing everywhere?"* Strong answer: one definition in a semantic layer with an owner; BI tools and assistants read it; deprecate local calculations; tests that reconcile to finance; change control on definitions.
4. *"What tests would you put on a fact table?"* Strong answer: key uniqueness at the declared grain; not-null foreign keys; relationships to dimensions; accepted values; reconciliation to a source total; freshness; unit tests for complex logic; severity thresholds.
5. *"How would you prepare our data for an AI assistant?"* Strong answer: a governed semantic layer, precise descriptions and synonyms, verified queries, hidden technical fields, a gold evaluation set, permission-aware access, and an out-of-scope response.

## Resources (free first)

- **dbt:** [dbt Learn](https://learn.getdbt.com/) (free courses); [How we structure our dbt projects](https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview); docs on [unit tests](https://docs.getdbt.com/docs/build/unit-tests), [model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts), [microbatch](https://docs.getdbt.com/docs/build/incremental-microbatch), [snapshots](https://docs.getdbt.com/docs/build/snapshots), [semantic models](https://docs.getdbt.com/docs/build/semantic-models); [jaffle-shop](https://github.com/dbt-labs/jaffle-shop); [dbt-utils](https://github.com/dbt-labs/dbt-utils); [dbt-expectations](https://github.com/calogica/dbt-expectations).
- **Modelling:** [Kimball dimensional modelling techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/); [Power BI star schema guidance](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema).
- **Semantic layers:** [MetricFlow](https://github.com/dbt-labs/metricflow); [Apache Ossie (formerly OSI)](https://github.com/open-semantic-interchange/OSI); [Cube docs](https://cube.dev/docs); [Databricks metric views](https://docs.databricks.com/aws/en/metric-views/); [Snowflake Cortex Analyst](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst); [Malloy](https://www.malloydata.dev/).
- **Alternatives:** [SQLMesh](https://sqlmesh.readthedocs.io/).
- **Real project:** [GitLab data team dbt guide](https://handbook.gitlab.com/handbook/enterprise-data/platform/dbt-guide/).
- **Paid, optional:** Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit*, 3rd ed. (Wiley, 2013).

## Sources

All checked 12 Oct 2026.

- dbt Labs, *2025 State of Analytics Engineering* (29 Apr 2025; 459 respondents) — https://www.getdbt.com/resources/state-of-analytics-engineering-2025
- TechTarget, "Fivetran, DBT Labs complete merger to form data layer for AI" (1 Jun 2026) — https://www.techtarget.com/data-technologies/news/366643590/Fivetran-DBT-Labs-complete-merger-to-form-data-layer-for-AI
- dbt Labs press release, MetricFlow open-sourced under Apache 2.0 (14 Oct 2025) — https://tools.prnewswire.com/en-us/live/20813/release/20251014EN96968 · MetricFlow repository — https://github.com/dbt-labs/metricflow
- dbt documentation, the dbt engine (v1 and v2) — https://docs.getdbt.com/docs/fusion/about-fusion
- Apache Ossie (formerly Open Semantic Interchange) repository — https://github.com/open-semantic-interchange/OSI
- Sequeda, Allemang and Jacob, "A Benchmark to Understand the Role of Knowledge Graphs on Large Language Model's Accuracy for Question Answering on Enterprise SQL Databases" (arXiv 2311.07509, Nov 2023) — https://arxiv.org/abs/2311.07509
- Snowflake, Cortex Analyst — https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst · Google Cloud, Conversational Analytics in Looker — https://docs.cloud.google.com/looker/docs/conversational-analytics-overview · Microsoft, Copilot for Power BI overview — https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
- Spider 2.0 leaderboard (Spider 2.0-DBT) — https://spider2-sql.github.io/
- Kimball Group, dimensional modelling techniques — https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/

_Last reviewed: 2026-10_
