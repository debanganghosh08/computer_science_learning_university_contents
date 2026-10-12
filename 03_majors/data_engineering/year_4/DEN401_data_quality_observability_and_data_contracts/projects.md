# DEN401 · Labs and projects

The labs reuse your DEN301 dbt projects and DEN303/DEN304 pipelines where possible, so you are testing systems you already understand. Tools: dbt (with `dbt-oss` or v2), DuckDB or a warehouse free tier, Great Expectations, Soda Core, Deequ, Elementary, Marquez, and the `datacontract` CLI. Labs 3 and 5 are done without AI assistants. Every test suite is judged by planted defects caught, never by test count.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Quality requirements | Write measurable quality requirements for one table from 3 consumers' viewpoints | Requirements table with thresholds and owners | 2 h |
| 2 · dbt tests and unit tests | 30 data tests with severities, 4 unit tests, enforced model contracts | Passing project, plus a failing build from a planted type change | 5 h |
| 3 · Mutation testing | Plant 10 defects (duplicates, NULL bursts, shifted dates, unit change, truncated load) and measure catch rate | Catch-rate table before and after improving the suite | 4 h |
| 4 · GX, Soda and Deequ | Express the same 15 checks in three tools on NYC TLC and a Spark job | Check outputs, effort notes and a recommendation | 5 h |
| 5 · Seasonal monitors | Volume and freshness monitors with day-of-week and holiday baselines; back-test 90 days | False alarms and misses per threshold setting | 5 h |
| 6 · Metadata collector | Collect freshness, volume, schema and run signals every 15 minutes; compare with Elementary | Signals table, owner dashboard, comparison notes | 6 h |
| 7 · Lineage with Marquez | Emit OpenLineage events from Airflow, Spark and dbt; answer 3 impact questions | Lineage graph screenshots and answers with timings | 4 h |
| 8 · Contracts in CI | ODCS contract for an orders event and table; block a breaking change in producer CI; then ship it as v2 with overlap | CI logs (blocked and passing), contract versions, consumer sign-off note | 6 h |
| 9 · Messy and unstructured data | Load 5 broken public files safely; deduplicate a merchant list; write 8 chunk-quality checks on court-judgment text | Precision/recall for deduplication, chunk-quality report | 5 h |
| 10 · Incident drill | Contain a doubled-revenue incident with time-travel rollback; write the restatement note and review | Timeline, rollback evidence, restatement note, review | 4 h |
| 11 · AI-generated tests | Compare an assistant's test suite with yours on 10 planted defects | Catch rates, never-failing-test count, uncaught defects | 3 h |

## Projects

### P1 · Proving a test suite works (L1, ~6 hours)

**Real-world inspiration:** most teams can say how many tests they have, and few can say how many real defects those tests would catch. Mutation testing is a standard way to measure test strength in software, and the same idea applies to data.

**What to build:** take your DEN301 P1 Olist project (or a provided equivalent) and build a defect injector. It is a script that applies one of 10 defect types to the raw data: duplicate order lines, NULL customer IDs, a currency unit change, timestamps shifted by 5.5 hours, a truncated day, swapped columns, orphan foreign keys, negative prices, a new category value, and a late batch. Then build a test suite that catches them.

**Acceptance criteria:**
- The injector applies each defect reproducibly from a seed and can restore clean data.
- Your suite catches at least 8 of 10 defect types, each with exactly the test you expected to catch it, and passes on clean data.
- Each test is labelled blocking or warning with a one-line reason.
- The README lists the uncaught defects and explains why catching them would need a different kind of check.

**Stretch goals:** add a reconciliation against a "source system" export; run the injector in CI on every pull request.

**What it proves to an employer:** you measure quality controls instead of assuming them.

### P2 · Observability for late, seasonal public data (L2, ~15 hours)

**Real-world inspiration:** public data arrives late, in bursts and with seasonal patterns. NYC TLC publishes monthly with roughly a two-month delay ([TLC](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)), and daily Indian market-price feeds on [data.gov.in](https://www.data.gov.in/) follow trading days and holidays. Monitors that ignore seasonality page people for nothing; monitors that are too loose miss real breaks.

**What to build:** an observability service over 3 pipelines (NYC TLC monthly, a data.gov.in daily feed, and GH Archive hourly). It includes:

- a metadata collector;
- seasonality-aware volume and freshness monitors;
- schema-change detection;
- distribution-drift checks on 5 key columns;
- OpenLineage emission into Marquez;
- data SLOs with error budgets;
- an owner dashboard.

Back-test it on 12 months of history.

**Acceptance criteria:**
- **Back-test:** over 12 months of history, monitors raise at most 1 false alert per week across all assets. Every alert is labelled true or false in a review sheet.
- **Detection:** on 6 planted incidents (missing day, half-volume load, schema change, new category, unit change, stuck source), at least 5 are detected within the SLO window, and the detection time is reported for each.
- **Root cause:** for each detected incident, lineage plus change logs identify the upstream cause within 15 minutes in a timed drill.
- **SLOs:** freshness and completeness SLOs exist for every gold asset, with a monthly error-budget report.

**Stretch goals:** compare your service with Elementary's built-in monitors on the same incidents; add Indian holiday calendars to the baselines.

**What it proves to an employer:** you can build monitoring that people trust because it is tested against history and planted failures.

### P3 · Contract-driven data platform with incident response (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** most data incidents start in an upstream application team that did not know someone depended on a field. Unity's 2022 disclosure shows what undetected bad input data can cost a business ([earnings call](https://www.fool.com/earnings/call-transcripts/2022/05/11/unity-software-inc-u-q1-2022-earnings-call-transcr/)). Contracts, enforced where producers work, are the structural fix. The platform below is illustrative.

**What to build:** a two-team setup in one repository.

**Producer team: an orders service.**
- PostgreSQL tables and Kafka order events, with its own CI.

**Data team: the platform.**
- CDC and event ingestion, dbt models, and gold tables for finance and operations.

**Across both teams:**
- ODCS contracts for 2 events and 3 tables, enforced in producer CI, in the schema registry, through dbt model contracts and by runtime checks;
- quarantine paths;
- write-audit-publish for gold tables;
- asset tiers with check requirements;
- an incident runbook, run in a game day with 6 injected defects of different kinds.

**Acceptance criteria:**
- **Prevention:** 3 breaking producer changes (type change, renamed field, semantic change with a new enum meaning) are blocked in producer CI or at the registry. One is then shipped correctly as a versioned change with a 2-week (simulated) overlap.
- **Detection:** at least 5 of 6 game-day defects are detected before they reach a gold table, and the sixth is detected within 1 hour of publication.
- **Containment:** no blocked defect reaches a gold table (verified by scanning gold snapshots). The one that does is rolled back with time travel, and consumers are notified by an automated message.
- **Restatement:** a restatement note names the exact affected rows, dates and corrected values, generated from a diff of snapshots.
- **Coverage:** every tier-1 asset has an owner, a contract, freshness and completeness SLOs, and a mutation catch rate of at least 80%.
- **Write-up:** design document, the contracts, two incident reviews, and a 5-minute recorded game-day walkthrough.

**Stretch goals:** an AI triage assistant that drafts incident summaries from lineage and logs, with every claim linked to evidence and a human approval step; a cost report for all checks and monitors.

**What it proves to an employer:** you can make data reliable across team boundaries, both technically and organisationally, and lead an incident to a clean, documented resolution. That is a senior data engineer's job.

## Feeds into

- [DEN501 Frontier Seminar](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md): quality for real-time AI data systems.
- [DEN404 Data Governance, Lineage and Privacy Engineering](../DEN404_data_governance_lineage_and_privacy_engineering/README.md): contracts and lineage become governance controls.
- [DEN403 Data Engineering for AI](../DEN403_data_engineering_for_ai_unstructured_data/README.md): chunk and embedding quality checks.
- [OV06A Building a Modern Data Platform](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06A_building_a_modern_data_platform/README.md): the quality layer of a full platform.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): data-quality measurement is a strong capstone topic.
