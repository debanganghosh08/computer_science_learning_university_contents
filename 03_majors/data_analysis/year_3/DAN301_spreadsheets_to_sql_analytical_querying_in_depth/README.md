# DAN301 · Spreadsheets to SQL: Analytical Querying in Depth

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [FND115](../../../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | [DAN401](../../year_4/DAN401_ai_augmented_analytics_text_to_sql_copilots/README.md), [DAN304](../DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md), [DAN305](../DAN305_product_and_business_analytics_metrics_funnels/README.md) |

Part of the [Data Analysis major](../../README.md). FND115 taught you relational SQL, basic window functions, CTEs and query plans on PostgreSQL. This course starts where business data actually lives (spreadsheets), then takes SQL to the depth that analyst interviews and real warehouses demand. Taught alongside [DAN302](../DAN302_business_statistics_and_experimentation/README.md) and [DAN303](../DAN303_data_visualization_and_storytelling/README.md).

## Why this course matters now

Most business numbers still pass through a spreadsheet at some point, and spreadsheets fail silently. In October 2020, Public Health England left 15,841 positive COVID-19 cases out of its daily figures because results were stored in the old `.xls` format, which stops at 65,536 rows. Behind the spreadsheet sits a warehouse queried in SQL, and AI now drafts much of that SQL. Uber reports that its QueryGPT tool cut the time to write a query from about 10 minutes to about 3 across a platform that runs roughly 1.2 million interactive queries a month (2024). Yet on the BIRD text-to-SQL benchmark, the best system reaches 82.95% execution accuracy against 92.96% for human experts (October 2026). Microsoft also withdrew Excel's preview `COPILOT()` worksheet function on 14 September 2026, and cells that recalculate now show `#NAME?`. The durable skill is knowing the grain of every table, writing the query that answers the question that was actually asked, proving it correct, and knowing what it costs to run. That holds whether you, a colleague or a model wrote the first draft.

## Learning outcomes

By the end you can:

1. **Build** auditable spreadsheet analyses with structured tables, dynamic arrays, `LET`/`LAMBDA`, `GROUPBY`/`PIVOTBY` and PivotTables, and **reconcile** them to a source total.
2. **Automate** messy imports with Power Query (M), and **explain** each applied step as its SQL equivalent (filter, join, union, unpivot).
3. **State the grain** of any table or result set, and **detect** fan-out, duplicate events and wrong denominators before they reach a report.
4. **Write** analytical SQL in two warehouse dialects (DuckDB and BigQuery): window frames, `QUALIFY`, `GROUPING SETS`, recursive CTEs, `PIVOT`/`UNPIVOT` and as-of joins.
5. **Implement** the standard business patterns from scratch: cohort retention, sessionization, ordered funnels, gaps and islands, top-N with ties, and point-in-time joins.
6. **Measure and reduce** query cost and latency using partition pruning, clustering, column pruning, dry runs and approximate aggregation.
7. **Test** queries with fixtures, assertions and two-way `EXCEPT` comparisons, and **lint** them to a team style with SQLFluff.
8. **Audit** AI-generated formulas and SQL against a gold harness, and **classify** every failure you find.

## Chapters and lessons

### Chapter 1 · Spreadsheets done properly (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Tables, not ranges | Excel Tables and structured references; one header row; one fact per row; why merged cells break analysis | Convert a messy MIS report into a tidy table; list every structural fix |
| 1.2 Types that lie | Dates as serial numbers, text that looks like numbers, Indian digit grouping (lakh, crore), locale-dependent CSV imports | Find the 6 type errors planted in a sales file |
| 1.3 Lookups | `XLOOKUP` vs `VLOOKUP` (default approximate match, column-index fragility), `INDEX`/`MATCH`, exact-match defaults, missing-key handling | Rebuild a broken `VLOOKUP` report; prove the totals now match |
| 1.4 Conditional aggregation | `SUMIFS`, `COUNTIFS`, `AVERAGEIFS`, `SUMPRODUCT`; the "average of averages" trap | Compute regional averages two ways and explain the gap |
| 1.5 PivotTables | Rows, columns, values, "% of parent", calculated fields (which sum ratios, often wrongly), slicers | Pivot the UCI Online Retail II data; catch the calculated-field error |

**Check your understanding:** Why does a `VLOOKUP` without its last argument return plausible but wrong answers? When is an average of regional averages correct, and when is it wrong? A pivot shows total margin % as the sum of item margin %; what should it show, and how do you force it?

### Chapter 2 · Modern formulas and spreadsheet risk (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Dynamic arrays | Spill ranges, `FILTER`, `SORT`, `UNIQUE`, `SEQUENCE`, `#SPILL!` errors | A self-updating top-10 table with no copy-down formulas |
| 2.2 `LET` and `LAMBDA` | Naming intermediate results; reusable named functions; `MAP`, `REDUCE`, `SCAN`, `BYROW` | Write `FY_QUARTER()` for the Indian April–March fiscal year as a named `LAMBDA` |
| 2.3 `GROUPBY` and `PIVOTBY` | Formula-based pivots (Excel for Microsoft 365) with filters, sort order and totals | Replace a PivotTable with `PIVOTBY`; compare refresh behaviour |
| 2.4 Google Sheets equivalents | `QUERY` (a SQL-like language), `ARRAYFORMULA`, Connected Sheets to BigQuery | Answer the same 5 questions in Sheets and in Excel |
| 2.5 Spreadsheet risk | Public Health England 2020; the Reinhart–Rogoff spreadsheet error (Herndon, Ash and Pollin, 2013); gene names converted to dates (Ziemann et al., 2016); EuSpRIG's error catalogue | Audit a 12-tab workbook: map dependencies, find the 4 planted errors |

**Check your understanding:** Why is a named `LAMBDA` easier to test than the same logic copied into 5,000 cells? What would have caught the Reinhart–Rogoff range error before publication? Which controls would you add to a workbook that a finance team edits every month?

### Chapter 3 · Power Query: the bridge to SQL (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Queries as pipelines | Applied steps, the M language, steps you can replay on next month's file | Clean 12 monthly CSVs with one query; add a 13th file with zero edits |
| 3.2 Merge and append | Merge = join (inner, left, anti), append = `UNION ALL`; duplicate keys multiply rows | Reproduce a fan-out by merging on a non-unique key, then fix it |
| 3.3 Reshaping | Unpivot wide reports (one column per month) into long tables; pivot back for display | Unpivot a state-wise government Excel download from data.gov.in |
| 3.4 Query folding | When Power Query pushes steps to the source database as SQL, and which steps break folding | Inspect the native query for 3 pipelines; reorder steps to restore folding |
| 3.5 Knowing when to leave | 1,048,576-row sheet limit, concurrent edits, audit trails, refresh failures; Python in Excel for one-off analysis | Write a one-page "move this report to SQL" decision memo |

**Check your understanding:** Why does an anti-merge in Power Query answer "which customers never ordered", and what is its SQL form? A merge step doubled revenue: list two ways to find out why. When does query folding matter for a 20-million-row source?

### Chapter 4 · Warehouse SQL and the grain (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Two engines | DuckDB locally and the BigQuery sandbox (no credit card, 1 TiB of queries a month); reading an unfamiliar schema | Load TheLook e-commerce public dataset; write a one-line grain statement for each table |
| 4.2 Dialect differences | `QUALIFY`, `SAFE_DIVIDE`, `DATE_TRUNC` argument order, `ILIKE`, `EXCEPT`/`REPLACE` in `SELECT *`, array and struct columns | Port 10 queries from PostgreSQL to BigQuery and DuckDB |
| 4.3 Grain discipline | "One row per what?"; fan-out from joins; why `COUNT(DISTINCT)` hides the bug instead of fixing it | Find the double-counting in 5 provided reports |
| 4.4 Deduplication | Late and duplicate events; `QUALIFY ROW_NUMBER() OVER (...) = 1`; choosing the tie-breaker | Dedupe a click log where 3% of events are retried |
| 4.5 Time | UTC vs IST (`Asia/Kolkata`), day boundaries, an Indian fiscal-year date dimension built with a date spine | Daily orders by IST day vs UTC day; explain the difference |

**Check your understanding:** A table has one row per order line. Which metrics can you `SUM` safely, and which need care? Why can deduplication with `DISTINCT` silently keep two versions of the same event? A dashboard and a finance report disagree on yesterday's revenue by 4%. What is the first thing you check?

### Chapter 5 · Window functions in depth (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Frames | `ROWS` vs `RANGE` vs `GROUPS`, `EXCLUDE`, default frames and the `LAST_VALUE` trap | Predict 8 frame results on paper, then run them |
| 5.2 Period-over-period | `LAG` for week-over-week and year-over-year; gaps in dates and why you need a date spine first | 7-day moving average that stays correct on days with no orders |
| 5.3 Shares and ranks | Share of total with `SUM() OVER ()`, `RANK` vs `DENSE_RANK` vs `ROW_NUMBER`, top-N per group with ties | Top 3 categories per city by revenue, with ties handled two ways |
| 5.4 Distributions | `PERCENTILE_CONT`, `APPROX_QUANTILES`, `NTILE` deciles, median vs mean delivery time | Delivery-time deciles per city; explain where the approximation differs |
| 5.5 Nulls and carry-forward | `IGNORE NULLS`, last-known-value fills, `FIRST_VALUE` with frames | Carry forward the last known price for each product per day |

**Check your understanding:** Why does `LAST_VALUE` usually return the current row unless you change the frame? When is `RANGE BETWEEN INTERVAL 6 DAY PRECEDING` different from `ROWS BETWEEN 6 PRECEDING`? What breaks in year-over-year growth when one year has a missing week?

### Chapter 6 · Query architecture: CTEs, recursion and reshaping (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 CTE pipelines | Import CTEs, logical CTEs, a final `SELECT`; one transformation per CTE; testing each step | Refactor a 150-line nested query into named steps with row counts per step |
| 6.2 Recursive CTEs | Date spines, org charts, category trees, bill of materials, cycle detection with a path array | Roll up revenue through a 5-level category tree |
| 6.3 Subtotals | `GROUPING SETS`, `ROLLUP`, `CUBE`, `GROUPING()` to label total rows | One query that produces a city × category table with all subtotals |
| 6.4 Pivot and unpivot | `PIVOT`/`UNPIVOT` in BigQuery and DuckDB vs `CASE`-based pivots that work everywhere | Turn a long KPI table into the wide layout an executive asked for |

**Check your understanding:** When does splitting a query into CTEs change performance, and when is it only for readability? How does a recursive CTE terminate, and how do you guarantee it with cyclic data? Why can `CUBE` mislead a reader who sums the output?

### Chapter 7 · Cohorts and retention in SQL (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Cohort assignment | First-activity month, acquisition channel cohorts, fixed vs rolling cohorts | Assign every TheLook user to a first-order cohort |
| 7.2 The retention matrix | Cohort × period-since-start; N-day, bounded and unbounded retention; logo vs revenue retention | Build the full matrix in one query; check it against a pivot in Sheets |
| 7.3 Right-censoring | Young cohorts have not had time to retain; blanks are not zeros | Mark immature cells; show the misleading chart you avoided |
| 7.4 Revenue cohorts | Net revenue retention, expansion and contraction, repeat-order rate | Revenue retention by cohort for the Olist Brazilian e-commerce dataset |

**Check your understanding:** Why is "30-day retention" ambiguous until you define the window and the event? A newer cohort looks worse at month 3: list three explanations before blaming the product. Why does revenue retention above 100% not mean that customers stayed?

### Chapter 8 · Event patterns: sessions, funnels and point-in-time joins (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Sessionization | 30-minute inactivity rule with `LAG` plus a running sum; cross-midnight and cross-device sessions | Sessionize the GA4 sample e-commerce events in BigQuery |
| 8.2 Ordered funnels | Steps within a time window, in order; strict vs loose funnels; step-level drop-off | View → add-to-cart → checkout → purchase within 24 hours |
| 8.3 Gaps and islands | Streaks, outages and stock-out periods with the row-number difference trick | Longest stock-out streak per product |
| 8.4 Touch attribution in SQL | First touch and last non-direct touch from event data; why rules disagree | Compare channel credit under both rules |
| 8.5 Point-in-time joins | Slowly changing attributes, `ASOF JOIN` (DuckDB), validity intervals | Join each order to the price and the store manager valid at order time |

**Check your understanding:** How do you sessionize when events arrive late or out of order? Why can a loose funnel show more checkouts than add-to-carts? What goes wrong if you join orders to the *current* customer segment instead of the segment at order time?

### Chapter 9 · Performance and cost (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Columnar engines | Why `SELECT *` costs money; column pruning; compression; row vs column stores (internals from [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md)) | Compare bytes processed for 4 versions of one query (BigQuery dry run) |
| 9.2 Partitions and clustering | Partition pruning, clustered columns, Snowflake micro-partition pruning; filters that defeat pruning | Rewrite a query so its date filter prunes; show bytes before and after |
| 9.3 Reading plans | DuckDB `EXPLAIN ANALYZE`, BigQuery execution details; join explosions, skew, spills | Find the stage that explodes in a slow provided query |
| 9.4 Approximation and sampling | HyperLogLog (`APPROX_COUNT_DISTINCT`), `TABLESAMPLE` and its bias on clustered data | Quantify the error of approximate distinct users on 10 days of data |
| 9.5 Materialise or not | Views, materialised views, scheduled tables; freshness vs cost | Cost model for a dashboard queried 500 times a day |

**Check your understanding:** Why can wrapping a partition column in a function make a query 100 times more expensive? When is a 1% approximation error acceptable, and who decides? A query is fast in DuckDB on your laptop and slow in the warehouse: list three likely causes.

### Chapter 10 · SQL quality: style, tests and review (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Style | SQLFluff rules, consistent casing and aliasing, explicit join types, no implicit `GROUP BY 1, 2` in shared code | Lint and fix a 300-line query to a team config |
| 10.2 Fixture tests | Tiny hand-made tables with known answers; edge cases (empty, `NULL`, ties, duplicate events, time-zone boundaries) | Fixtures for your cohort and funnel queries |
| 10.3 Assertions | Uniqueness, not-null, accepted values, row counts per step, reconciliation to a finance total | Add 8 assertions; break the data and watch them fail |
| 10.4 Equivalence | Two-way `EXCEPT`, row-hash comparison, tolerance for floats | Prove a refactored query returns the same result as the original |
| 10.5 Review | A reviewer's checklist (grain, joins, filters, time zone, denominators, cost); query headers stating assumptions; Git for queries | Review a classmate's P2 query and file 5 concrete comments |

**Check your understanding:** Why is "it ran without errors" not evidence that a query is correct? Which assertion would have caught the double-counted revenue from Chapter 4? How do you test a query whose correct answer you do not know?

### Chapter 11 · AI-assisted querying with proof (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Drafting with AI | Gemini in BigQuery, Copilot in Excel, Claude and ChatGPT with a pasted schema; giving grain, definitions and dialect in the prompt | Draft 20 queries with AI from business questions |
| 11.2 The gold harness | Questions with gold SQL and gold results; scoring by result equality, not text similarity | Grade your 20 drafts; log each failure |
| 11.3 Failure taxonomy | Wrong grain, fan-out, wrong time zone, silent filter on a business term, hallucinated column, dialect mix-up | Classify your log; compare with Uber's published QueryGPT lessons |
| 11.4 Formula reproducibility | Non-deterministic AI cell functions; Excel's `COPILOT()` returning `#NAME?` after 14 Sep 2026 | Replace an AI-function column with a deterministic rule or a stored, reviewed output |
| 11.5 Timed rounds | Interview-style SQL under a 45-minute timer, AI off | Three timed sets; review your mistakes |

**Check your understanding:** Why does matching the gold SQL's text say little about correctness? What should be in the prompt so that an assistant cannot silently pick a definition of "active user"? Why must a monthly report never depend on a cell that calls a model at recalculation time?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Spreadsheet triage | Tidy-data checklist |
| 2 | 2 | Lab 2 · `LAMBDA` library and workbook audit | Audit report |
| 3 | 3 | Lab 3 · Power Query pipeline | **P1 due** |
| 4 | 4 | Lab 4 · Grain and dedup | Grain statements for 8 tables |
| 5 | 5 | Lab 5 · Window gauntlet | — |
| 6 | 5 | Lab 5 (cont.) | Mid-term, part 1 (spreadsheets, AI off) |
| 7 | 6 | Lab 6 · Recursion and subtotals | — |
| 8 | 7 | Lab 7 · Cohort matrix | Mid-term, part 2 (SQL, AI off) |
| 9 | 8 | Lab 8 · Sessions and funnels | — |
| 10 | 8–9 | Lab 8 (cont.) | **P2 due** |
| 11 | 9 | Lab 9 · Cost diet | Cost report |
| 12 | 10 | Lab 10 · Test and lint | Peer review |
| 13 | 11 | AI harness | Failure log |
| 14 | 11 | Timed rounds | **P3 due** |
| 15 | Review | Oral defence of P3 | Final practical exam |

## Working with AI in this course

- **Use AI for:** drafting `LAMBDA`s and Power Query M steps; explaining an unfamiliar dialect function; translating between PostgreSQL, BigQuery and DuckDB; generating fixture tables and edge cases; a second opinion on a query plan. Copilot in Excel, Gemini in Google Sheets and BigQuery, Claude, ChatGPT and Claude Code all do this well enough to save time.
- **Do without AI (drills):** 10 hand-written queries a week against a printed schema; grain statements; frame predictions; rebuilding a pivot by hand; the mid-terms and final exam. Many analyst loops include an AI-off SQL round, and you cannot review what you cannot write.
- **Verify AI output by:**
  - running it on a fixture with a known answer;
  - checking row counts after every join and CTE;
  - comparing with a second method (a pivot, pandas, or a different query) using `EXCEPT` both ways;
  - checking the definitions it chose for business terms;
  - estimating bytes processed with a dry run before running it on a large table.
- **Where AI still fails here:** BIRD's best system is about 10 points below human experts. On BIRD-Interact, which requires clarifying ambiguous requests, GPT-5 solved 8.67% of conversational tasks and 17.00% of agentic ones. Uber reports that hallucinated tables and columns were not fully solved in QueryGPT. In this course you collect your own evidence: every AI query that runs but returns the wrong number goes into your failure log with its root cause.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 20% |
| Mid-term, two parts (AI off) | 10% |
| Final practical exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can, with AI off: (1) in 90 minutes, answer 12 questions on an unseen warehouse schema, including a cohort retention matrix, a sessionized ordered funnel, top-N per group with ties, and a gaps-and-islands streak, with results that match the key exactly; (2) cut the bytes processed by a provided query by at least 80% without changing its result, proven by dry runs and a two-way `EXCEPT`; (3) rebuild a messy monthly spreadsheet report as a Power Query pipeline whose totals reconcile to the source to the rupee.

## Industry reality

Spreadsheets remain the interface between analysts and the rest of the business, which is why finance, operations and MIS roles in India still test Excel directly. Warehouse SQL is the analyst's main language: Uber describes about 1.2 million interactive queries a month on its data platform, with Operations contributing about 36%, and built QueryGPT around curated "workspaces" of tables and example SQL because plain retrieval lost accuracy as more tables were added (2024). Swiggy has described Hermes, its text-to-SQL tool, built on the same idea of domain-scoped metadata (2024). Both show that the hard part is the context an analyst already owns: which table, which grain, which definition.

**Interview questions from this course**

1. *"Compute monthly retention by signup cohort."* Strong answer: defines cohort and activity event; builds cohort assignment, an activity table and a cohort × month-offset count over the cohort size; handles immature cohorts; states the grain of each CTE.
2. *"Find each user's longest streak of consecutive active days."* Strong answer: deduplicates to user-day; uses the date minus `ROW_NUMBER()` island key; groups by island; discusses time zones and how gaps are defined.
3. *"Revenue doubled after you joined orders to shipments. Why, and how do you fix it?"* Strong answer: one-to-many fan-out; aggregate shipments to order grain before joining, or join at the correct grain; adds a row-count assertion; explains why `DISTINCT` is not a fix.
4. *"This dashboard query costs too much. What do you do?"* Strong answer: dry run and execution details; partition filter on the raw column; select only needed columns; pre-aggregate or materialise; quantifies the saving.
5. *"Sessionize this clickstream with a 30-minute timeout."* Strong answer: `LAG` per user ordered by timestamp, a new-session flag, a running sum for the session id; late events and ties; one-row-per-session output with start, end and event count.

## Resources (free first)

- **Spreadsheets:** Microsoft support pages for [`XLOOKUP`](https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929), [`LAMBDA`](https://support.microsoft.com/en-us/office/lambda-function-bd212d27-1cd1-4321-a34a-ccbf254b8b67), [`GROUPBY`](https://support.microsoft.com/en-us/office/groupby-function-5e08ae8c-6800-4b72-b623-c41773611505); [Power Query M reference](https://learn.microsoft.com/en-us/powerquery-m/); [Exceljet](https://exceljet.net/); Google Sheets [`QUERY`](https://support.google.com/docs/answer/3093343); [EuSpRIG horror stories](https://eusprig.org/research-info/horror-stories/).
- **SQL engines:** [DuckDB documentation](https://duckdb.org/docs/) (window functions, `QUALIFY`, `ASOF JOIN`, `PIVOT`); [BigQuery sandbox](https://docs.cloud.google.com/bigquery/docs/sandbox) and [query best practices](https://cloud.google.com/bigquery/docs/best-practices-performance-compute); [Snowflake micro-partitions](https://docs.snowflake.com/en/user-guide/tables-clustering-micropartitions); [PostgreSQL window functions](https://www.postgresql.org/docs/current/functions-window.html).
- **Quality:** [SQLFluff](https://docs.sqlfluff.com/); [Use The Index, Luke](https://use-the-index-luke.com/).
- **Practice:** [DataLemur](https://datalemur.com/) (free tier); [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/); [pgexercises](https://pgexercises.com/).
- **Datasets:** BigQuery public datasets `thelook_ecommerce` and `ga4_obfuscated_sample_ecommerce`; [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) (1,067,371 rows, CC BY 4.0); [Olist Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce); [Open Government Data Platform India](https://www.data.gov.in/).
- **Paid, optional:** Cathy Tanimura, *SQL for Data Analysis* (O'Reilly, 2021), a strong source of cohort and funnel patterns.

## Sources

All checked 12 Oct 2026.

- The Register, report on Public Health England's 15,841 missing cases and the `.xls` row limit (5 Oct 2020) — https://www.theregister.com/2020/10/05/excel_england_coronavirus_contact_error/
- Uber Engineering, "QueryGPT – Natural Language to SQL Using Generative AI" (19 Sep 2024) — https://www.uber.com/blog/query-gpt/
- Swiggy Bytes, "Hermes: A Text-to-SQL solution at Swiggy" (Jul 2024) — https://medium.com/swiggy-bytes/hermes-a-text-to-sql-solution-at-swiggy-81573fb4fb6e
- BIRD leaderboard, BIRD-Interact results (updated 9 Oct 2026) — https://bird-bench.github.io/
- Microsoft Support, COPILOT function (no longer available from 14 Sep 2026) — https://support.microsoft.com/en-us/office/copilot-function-5849821b-755d-4030-a38b-9e20be0cbf62
- Microsoft Support, GROUPBY function — https://support.microsoft.com/en-us/office/groupby-function-5e08ae8c-6800-4b72-b623-c41773611505
- Google Cloud, BigQuery sandbox limits — https://docs.cloud.google.com/bigquery/docs/sandbox
- Herndon, Ash and Pollin, "Does High Public Debt Consistently Stifle Economic Growth?", *Cambridge Journal of Economics* 38(2), 2014 (working paper April 2013), doi:10.1093/cje/bet075
- Ziemann, Eren and El-Osta, "Gene name errors are widespread in the scientific literature", *Genome Biology* 17 (2016), doi:10.1186/s13059-016-1044-7
- UCI Machine Learning Repository, Online Retail II — https://archive.ics.uci.edu/dataset/502/online+retail+ii

_Last reviewed: 2026-10_
