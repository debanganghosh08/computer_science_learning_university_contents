# DEN401 · Data Quality, Observability and Data Contracts

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [DEN301](../../year_3/DEN301_data_modeling_and_warehousing/README.md) | [DEN501](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md), [DEN404](../DEN404_data_governance_lineage_and_privacy_engineering/README.md), [OV06A](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06A_building_a_modern_data_platform/README.md) |

Part of the [Data Engineering major](../../README.md). [DEN301](../../year_3/DEN301_data_modeling_and_warehousing/README.md) taught you to prove one model's numbers with reconciliation queries. This course scales that to a platform: hundreds of tables, dozens of producing teams, sources that change without warning, and consumers (dashboards, ML models, AI assistants) that act on the data automatically. Analysts' view of the same topic is in [DAN404](../../../data_analysis/year_4/DAN404_data_governance_quality_and_privacy_for_analysts/README.md); here you build the systems.

## Why this course matters now

Bad data costs real money, and it often arrives quietly. In May 2022, Unity Software said that a fault in its platform, together with ingesting bad data from a large customer, had reduced the accuracy of its Audience Pinpointer ad-targeting tool. It estimated the impact at about $110 million in 2022 and said it was deploying monitoring, alerting and recovery systems in response. The tooling has matured since. dbt v2's engine statically validates every model, and its strict mode produces column-level lineage. Great Expectations (GX Core 1.24), Soda and Elementary are widely used open-source checkers. The Open Data Contract Standard (v3.2.0, under the LF AI & Data Foundation's Bitol project) gives contracts a shared YAML format. AI assistants now write data tests in bulk and summarise incidents. They tend to write tests that pass, such as `not_null` on columns that are never null, rather than tests that would have caught last month's incident. Choosing what to test, setting thresholds that page the right person, and getting two teams to agree on a contract and keep it are human work, and they are what make a data engineer hard to replace.

## Learning outcomes

By the end you can:

1. **Define** quality for a dataset in measurable terms (validity, completeness, uniqueness, consistency, timeliness, accuracy) tied to its consumers' decisions.
2. **Implement** layered tests (dbt data and unit tests, model contracts, reconciliation, Great Expectations or Soda checks) and **measure** test effectiveness by planting defects.
3. **Build** statistical monitors for volume, freshness, schema and distribution that respect seasonality, and **tune** them to a target false-alarm rate.
4. **Design** an observability service from warehouse metadata, query logs and OpenLineage events, and **use** lineage for impact and root-cause analysis.
5. **Write** data contracts in ODCS YAML, **enforce** them at producer CI, schema registry, transformation and runtime, and **run** a versioned breaking change.
6. **Lead** a data incident from detection to restatement and blameless review, using quarantine, rollback and time travel.
7. **Validate** unstructured and AI-bound data (documents, chunks, embeddings) with checks suited to it.
8. **Audit** AI-generated tests and monitors for weak coverage, and **justify** the cost of checks against the risk they remove.

## Chapters and lessons

### Chapter 1 · What quality means (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Fitness for use | Quality dimensions; the same table can be good enough for a trend chart and wrong for invoicing | Write quality requirements for one table from the views of 3 consumers |
| 1.2 Where defects come from | Source bugs, pipeline bugs, semantic drift (a field changes meaning), late and duplicate data, unit and time-zone errors | Classify 20 described incidents by origin |
| 1.3 The cost of bad data | Decisions taken on wrong numbers, model retraining on bad inputs (the Unity 2022 case), lost trust | Estimate the cost of a one-week error in a pricing feed (illustrative) |
| 1.4 Prevention, detection, response | Contracts and tests prevent; monitors detect; incident processes respond; where each is cheapest | Map your DEN301 P3 checks onto the three layers and find the gaps |

**Check your understanding:** (1) Why is "accuracy" the hardest dimension to test automatically? (2) Give an example of semantic drift that no schema check would catch. (3) Why should quality requirements be written per consumer, not per table?

### Chapter 2 · Testing data in pipelines (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 dbt data tests | Generic and singular tests, `severity`, `warn_if`/`error_if` thresholds, `store_failures` | Add 30 tests to a dbt project; classify each as blocking or warning |
| 2.2 dbt unit tests | Testing transformation logic on fixed inputs and expected outputs before data arrives | Unit-test an SCD2 model and a sessionisation model |
| 2.3 Contracts on models | Enforced column names and types, constraints; dbt v2 static analysis in strict mode | Break an upstream column type; watch the build fail at compile time, not in production |
| 2.4 Reconciliation | Control totals from source to target, row-count parity, cross-system checks (warehouse vs ledger vs payment gateway file) | Reconcile a payments mart against a provided settlement file |
| 2.5 Testing the tests | Mutation testing for data: plant defects (duplicates, NULL bursts, shifted dates, unit changes) and count how many your suite catches | Measure your suite's catch rate; raise it from the baseline to at least 80% |

**Check your understanding:** (1) What is the difference between a data test and a unit test, and why do you need both? (2) A suite of 300 tests catches 2 of 10 planted defects: what does that tell you? (3) Why are reconciliations more valuable than column-level tests for money?

### Chapter 3 · Validation frameworks (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Great Expectations | GX Core: expectations, expectation suites, validation definitions, checkpoints, Data Docs | Validate a daily NYC TLC load with 15 expectations; publish Data Docs |
| 3.2 Soda | SodaCL checks, thresholds, anomaly checks, scans in pipelines | Express the same 15 checks in SodaCL; compare effort and output |
| 3.3 DataFrame and Spark checks | Pandera schemas for pandas and Polars; Deequ (and PyDeequ) for Spark | Add Deequ checks to the DEN302 P2 job |
| 3.4 Where checks run | At ingestion, after transformation, before publication; blocking vs warning; quarantine tables; write-audit-publish (from [DEN305](../../year_3/DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md)) | Design check placement for a 5-stage pipeline with a quarantine path |

**Check your understanding:** (1) Why should most checks run before publication rather than after? (2) What does a quarantine table need so that rows can be repaired and replayed? (3) When is a framework overkill compared with a few SQL assertions?

### Chapter 4 · Statistical monitoring (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Profiling | Null rates, distinct counts, min/max, quantiles, value frequencies; profiles as baselines | Profile 90 days of a table and store daily profiles |
| 4.2 Seasonality-aware baselines | Day-of-week and holiday effects (Diwali sale days, month-end), robust statistics (median and MAD), forecasting baselines | Build a volume monitor that does not fire on every Sunday |
| 4.3 Distribution drift | Population stability index, Kolmogorov–Smirnov test, category share shifts | Detect a planted change in payment-method mix |
| 4.4 Alert economics | False positives vs missed incidents, multiple testing across thousands of metrics, alert fatigue | Tune thresholds to at most 1 false alert per week on 200 metrics, then measure misses |

**Check your understanding:** (1) Why does a mean-and-standard-deviation threshold fail on heavy-tailed volumes? (2) Monitoring 2,000 metrics at a 1% false-positive rate gives how many false alerts a day, and what do you do about it? (3) What does a volume drop look like for a table loaded from a source that publishes late?

### Chapter 5 · Data observability (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Signals | Freshness, volume, schema changes, distribution, lineage; query-level signals (failed jobs, runtime spikes) | List the metadata sources your warehouse exposes for each signal |
| 5.2 Collecting metadata | `information_schema`, query and load history views, orchestrator run metadata, OpenLineage events | Build a collector that writes these signals to a metrics table every 15 minutes |
| 5.3 Tools | Elementary (dbt-native, open source), commercial observability platforms; build vs buy | Install Elementary on your dbt project; compare it with your collector |
| 5.4 Data SLOs | Freshness and completeness objectives per asset (from [DEN304](../../year_3/DEN304_orchestration_and_pipelines_airflow_and_dagster/README.md)), error budgets, burn alerts | Define SLOs for 5 gold assets and an error-budget report |
| 5.5 Dashboards for owners | One view per owner: what is late, what failed, what changed | Build an owner dashboard from your signals |

**Check your understanding:** (1) Which signal catches a silently truncated load, and which catches a unit change? (2) Why do warehouse query logs help detect problems that pipeline logs miss? (3) What should a data error budget allow a team to do?

### Chapter 6 · Lineage for impact and root cause (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Lineage models | Table-level vs column-level lineage; static (parsed from SQL) vs runtime (emitted by jobs) | Compare dbt's lineage with OpenLineage events for the same project |
| 6.2 OpenLineage and Marquez | Runs, jobs, datasets and facets; integrations with Airflow, Spark and dbt | Emit lineage from Airflow and Spark into Marquez |
| 6.3 Impact analysis | Who is affected by a broken table, column or change; notifying owners | Answer "what breaks if `customer.city` becomes nullable?" in under 5 minutes |
| 6.4 Root-cause analysis | Walking upstream, correlating changes (deploys, schema changes, source incidents) with anomalies | Find the root cause of 3 injected incidents using lineage plus change logs |

**Check your understanding:** (1) Why does static SQL lineage miss some dependencies, and what fills the gap? (2) How does column-level lineage shrink the blast radius you need to communicate? (3) Name two root causes lineage alone cannot reveal.

### Chapter 7 · Data contracts (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 What a contract is | An agreement between producer and consumer: schema, semantics, quality rules, service levels, ownership, versioning, support channel | Write a one-page contract for an orders event in plain language |
| 7.2 Open Data Contract Standard | ODCS v3.2 YAML sections (fundamentals, schema, data quality, SLA, team, roles, servers); the `datacontract` CLI | Convert your contract to ODCS and test it against a real table |
| 7.3 Enforcement points | Producer CI checks on pull requests, schema registry compatibility for streams (from [DEN303](../../year_3/DEN303_streaming_systems_kafka_and_flink/README.md)), dbt model contracts, runtime validation | Block a breaking producer change in CI before it merges |
| 7.4 Change management | Versioned contracts, deprecation windows, dual publishing, consumer sign-off | Run a breaking change through v1 and v2 with a 2-week overlap |
| 7.5 The organisation | Producer ownership, data products and data mesh principles, negotiating with application teams, what to do when a producer refuses | Role-play a contract negotiation between a payments team and the data team |

**Check your understanding:** (1) Why must contracts be enforced where the producer works, not only in the warehouse? (2) What belongs in a contract's semantics section that a schema cannot express? (3) What do you do when a critical producer will not sign a contract?

### Chapter 8 · Quality for messy, unstructured and AI-bound data (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Ingestion hazards | CSV quoting, encodings (UTF-8 vs legacy encodings for Indic scripts), Excel date serials, API pagination gaps | Load 5 broken public files without silent corruption |
| 8.2 Deduplication and entity resolution | Exact and fuzzy duplicates, blocking keys, similarity thresholds; Indian name and address variation | Deduplicate a merchant list with precision and recall measured on a labelled sample |
| 8.3 Document and chunk quality | Empty or tiny chunks, OCR garbage rate, language detection, boilerplate share, near-duplicate documents (continued in [DEN403](../DEN403_data_engineering_for_ai_unstructured_data/README.md)) | Write 8 checks for a document-chunk table and run them on Indian court-judgment text |
| 8.4 Embedding and label quality | Embedding dimension and norm checks, model-version consistency, label agreement rates | Detect a planted batch embedded with the wrong model |

**Check your understanding:** (1) Why do fuzzy deduplication thresholds need a labelled sample? (2) What would a RAG system do with 5% of chunks that are OCR noise? (3) Why must every embedding row record the model and version that produced it?

### Chapter 9 · Incident management for data (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Detection and triage | Severity by consumer impact, incident commander role, first 15 minutes (Google SRE incident practices adapted to data) | Run a tabletop exercise on a doubled revenue figure |
| 9.2 Containment | Stop the line, quarantine, roll back tables with time travel, pause downstream publication | Roll back a gold table to the last good snapshot and pause consumers |
| 9.3 Communication and restatement | Status updates to consumers, restatement notes with exact affected ranges, finance and regulatory consumers | Write the restatement note for a corrected month |
| 9.4 Blameless reviews | Timeline, contributing factors, action items with owners; tracking time to detect and time to resolve | Write a review for a provided incident and propose 3 preventive checks |

**Check your understanding:** (1) Why is "stop publishing" often the right first action? (2) What makes a restatement note trustworthy? (3) Which incident metric tells you your monitoring is improving?

### Chapter 10 · Quality at organisational scale, with AI in the loop (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Ownership and scorecards | Owners for every asset, quality scorecards, tiering assets by criticality | Tier 50 assets and assign check requirements per tier |
| 10.2 Economics | The cost of checks (compute, alerts, maintenance) vs the risk removed; test debt | Remove 20% of checks with no loss in mutation catch rate |
| 10.3 AI-generated tests and monitors | Assistants proposing tests from schemas and profiles; why they skew towards tests that pass; using planted defects to judge them | Generate tests with an assistant; measure their catch rate against your own |
| 10.4 AI triage | LLM summaries of incidents from lineage, logs and diffs; hallucinated root causes; human sign-off | Compare an AI incident summary with your own review; list every factual error |
| 10.5 Capstone review | Present P3 | Oral defence |

**Check your understanding:** (1) Why should check requirements depend on an asset's tier? (2) What evidence would justify deleting a check? (3) How do you stop an AI triage summary from becoming the official record without verification?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Quality requirements | Requirements for 3 consumers |
| 2 | 2 | Lab 2 · dbt tests and unit tests | Test suite |
| 3 | 2 | Lab 3 · Mutation testing | Catch-rate report; **P1 due** |
| 4 | 3 | Lab 4 · GX, Soda and Deequ | Same checks in 3 tools |
| 5 | 4 | Lab 5 · Seasonal monitors | False-alarm tuning report |
| 6 | 5 | Lab 6 · Metadata collector | Signals table |
| 7 | 5 | Lab 6 (cont.) | Mid-term (AI off): tests, statistics, SLOs |
| 8 | 6 | Lab 7 · Lineage with Marquez | Impact-analysis drill |
| 9 | 7 | Lab 8 · Contracts in CI | Blocked breaking change; **P2 due** |
| 10 | 7 | Lab 8 (cont.) | Versioned change with overlap |
| 11 | 8 | Lab 9 · Messy and unstructured data | Dedup and chunk-quality reports |
| 12 | 9 | Lab 10 · Incident drill | Rollback, restatement note, review |
| 13 | 10 | Lab 11 · AI-generated tests | Catch-rate comparison |
| 14 | 10 | Capstone review | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** drafting test YAML from schemas and profiles; translating checks between dbt, GX, Soda and Deequ; drafting ODCS contracts from existing tables; summarising an incident timeline from logs, as a draft only. Tools: Claude Code, GitHub Copilot, Cursor; dbt v2's language server and agent skills; warehouse assistants for metadata queries.
- **Do without AI (drills):** deciding which tests matter for a consumer; computing false-alarm rates and thresholds; running impact analysis from lineage; writing the restatement note and the blameless review. These are judgement and accountability tasks.
- **Verify AI output by:** (1) measuring every generated test suite against planted defects (mutation catch rate), not by counting tests; (2) back-testing monitors on 90 days of history to count false alarms; (3) running contracts against real data with the `datacontract` CLI; (4) checking every causal claim in an AI incident summary against lineage and change logs.
- **Where AI still fails here (show it yourself):** in Lab 11, generate tests for a 20-model project with an assistant and with your own method. Plant 10 defects. Record which suite catches more, how many generated tests could never fail on this data, and which incidents neither suite caught. In Lab 10, ask an assistant for a root cause from the logs alone and record every unsupported claim.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–11 | 25% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 20% |
| Oral defence of P3 | 10% |

**Mastery gate.** You pass when you can, without AI: (1) given a 20-model project and its consumers, design a test and monitor suite that catches at least 8 of 10 unseen planted defects with at most 1 false alarm on a clean week; (2) write and enforce an ODCS contract that blocks a breaking producer change in CI; (3) lead a simulated incident (detect, contain with time travel, communicate, restate, review) within 2 hours, with a restatement note that names the exact affected rows and dates.

## Industry reality

Unity's 2022 disclosure is one of the clearest public examples of a data-quality incident with a reported financial impact: about $110 million, with monitoring, alerting and recovery systems named as the response. Data teams commonly combine dbt tests and contracts, a validation framework (GX, Soda or Deequ), an observability layer (Elementary or a commercial platform), and lineage via OpenLineage. Data contracts gained a shared format with ODCS. Contract enforcement in producer CI and schema registries is what makes them more than documentation.

**Interview questions from this course**

1. *"How do you make sure the data in a pipeline is correct?"* A strong answer layers prevention (contracts, schema enforcement, unit tests), detection (data tests, reconciliations, statistical monitors) and response (quarantine, rollback, incident process). It ties tests to consumer requirements and explains how the suite's effectiveness is measured.
2. *"What is a data contract, and how do you enforce one?"* Cover schema, semantics, quality rules, SLAs, ownership and versioning; enforcement in producer CI, schema registries, model contracts and runtime checks; and how breaking changes are versioned.
3. *"Build a volume anomaly detector for a table with weekly seasonality and sale-day spikes."* Cover baselines by day of week, robust statistics, holiday calendars, forecast intervals, threshold tuning to a false-alarm budget, and back-testing on history.
4. *"The CFO says yesterday's revenue number is wrong. Walk me through the next 2 hours."* Cover triage and severity, checking freshness and recent changes, lineage walk upstream, reconciliation to source, containment (pause and roll back), communication, restatement, and the review.
5. *"How would you check data quality for a RAG ingestion pipeline?"* Cover parse success rates, empty or tiny chunks, OCR noise, duplicates, language, embedding model consistency, freshness relative to the source, and retrieval-level evaluation in [DEN403](../DEN403_data_engineering_for_ai_unstructured_data/README.md).

## Resources (free first)

- **Documentation:** dbt [data tests](https://docs.getdbt.com/docs/build/data-tests), [unit tests](https://docs.getdbt.com/docs/build/unit-tests), [model contracts](https://docs.getdbt.com/docs/mesh/govern/model-contracts) and [source freshness](https://docs.getdbt.com/reference/resource-properties/freshness); [Great Expectations GX Core](https://docs.greatexpectations.io/docs/core/introduction/); [Soda Core](https://github.com/sodadata/soda-core) and [Soda docs](https://docs.soda.io/); [Deequ](https://github.com/awslabs/deequ); [Pandera](https://pandera.readthedocs.io/); [Elementary](https://github.com/elementary-data/elementary); [OpenLineage](https://openlineage.io/docs/); [Marquez](https://marquezproject.ai/).
- **Contracts:** [Open Data Contract Standard](https://github.com/bitol-io/open-data-contract-standard) ([docs](https://bitol-io.github.io/open-data-contract-standard/latest/)); [Data Contract CLI](https://github.com/datacontract/datacontract-cli).
- **Incident practice:** Google SRE book, [Managing Incidents](https://sre.google/sre-book/managing-incidents/) and [Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) (free).
- **Organisation:** Zhamak Dehghani, ["Data Mesh Principles and Logical Architecture"](https://martinfowler.com/articles/data-mesh-principles.html) (free).
- **Datasets:** [NYC TLC trip records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) (real outliers and late files); [data.gov.in](https://www.data.gov.in/) feeds; [Indian High Court Judgments](https://registry.opendata.aws/indian-high-court-judgments/) for document-quality checks.
- **Paid, worth it:** Moses, Gavish and Vorwerck, *Data Quality Fundamentals* (O'Reilly, 2022); Jones, *Driving Data Quality with Data Contracts* (Packt, 2023).

## Sources

All checked October 2026.

- Unity Software Q1 2022 earnings call transcript (11 May 2022): bad data from a large customer, Audience Pinpointer accuracy, ≈ $110 million 2022 impact, monitoring and alerting response. https://www.fool.com/earnings/call-transcripts/2022/05/11/unity-software-inc-u-q1-2022-earnings-call-transcr/
- dbt, "Upgrading to v2" (static analysis, strict mode, column-level lineage). https://docs.getdbt.com/docs/dbt-versions/dbt-upgrade/upgrading-to-v2
- Great Expectations, GX Core introduction (version 1.24.0). https://docs.greatexpectations.io/docs/core/introduction/
- Bitol, Open Data Contract Standard README (current version v3.2.0; Apache 2.0; LF AI & Data Foundation). https://github.com/bitol-io/open-data-contract-standard
- OpenLineage project site. https://openlineage.io/

_Last reviewed: 2026-10_
