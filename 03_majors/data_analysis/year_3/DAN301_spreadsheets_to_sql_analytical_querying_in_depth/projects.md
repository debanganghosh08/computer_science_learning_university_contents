# DAN301 · Labs and projects

Every lab and project ships with three things: the workbook or SQL files in a Git repository, a test or reconciliation that proves the numbers, and a short write-up stating the grain, the assumptions and what you checked. SQL runs on DuckDB locally and on the BigQuery sandbox; spreadsheets use Excel for Microsoft 365 or Google Sheets.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Spreadsheet triage | Turn a messy, merged-cell MIS export into a tidy Excel Table; fix types (dates as text, lakh-formatted numbers, trailing spaces) | Cleaned workbook, a list of every fix, and a reconciliation of the grand total before and after | 3 h |
| 2 · `LAMBDA` library and workbook audit | Write 5 named `LAMBDA`s (fiscal quarter, safe ratio, week start, IST date from UTC timestamp, growth %) with test cells; audit a provided 12-tab workbook | The library with passing test cells; an audit report naming the 4 planted errors and the control that would catch each | 4 h |
| 3 · Power Query pipeline | Combine 12 monthly CSVs, unpivot a wide report, anti-merge to find customers with no orders | Query file; proof that adding a 13th month needs zero edits; native-query screenshot showing folding where possible | 4 h |
| 4 · Grain and dedup | Write a grain statement for 8 TheLook tables; deduplicate a click log with retries using `QUALIFY` | Grain sheet; dedup query; before/after counts; the tie-breaker you chose and why | 3 h |
| 5 · Window gauntlet | 15 window-function problems: frames, moving averages over a date spine, top-N with ties, deciles, carry-forward | Queries plus your written prediction for each frame question made before running it | 6 h |
| 6 · Recursion and subtotals | Roll up a 5-level category tree; produce city × category subtotals with `GROUPING SETS`; pivot a long KPI table | Queries, a cycle-detection test, and a labelled subtotal output | 4 h |
| 7 · Cohort matrix | Monthly first-order cohorts and a retention matrix with immature cells masked | Query, a heatmap, and a check against a Sheets pivot of the same data | 4 h |
| 8 · Sessions and funnels | Sessionize the GA4 sample events; ordered 4-step funnel within 24 hours; last non-direct touch attribution | Queries, step drop-off table, and one paragraph on how strict vs loose funnels differ on this data | 5 h |
| 9 · Cost diet | Take 5 deliberately wasteful queries and cut bytes processed without changing results | Dry-run bytes before and after, two-way `EXCEPT` proof for each, and a cost table in rupees at list price | 4 h |
| 10 · Test and lint | Fixture tests for your Lab 7 and Lab 8 queries; SQLFluff config; a reviewer checklist | Passing tests in CI (GitHub Actions), a lint-clean repo, and 5 review comments on a classmate's queries | 4 h |

## Projects

### P1 · Self-refreshing monthly MIS report (L1, ~6 hours)

**Real-world inspiration.** Reporting analysts in Indian banks, NBFCs and retailers rebuild the same monthly MIS workbook by hand, and copy-paste errors are common. The EuSpRIG catalogue and the 2020 Public Health England incident show what unaudited workbooks cost.

**What to build.** Choose one source: (a) the UCI Online Retail II dataset (1,067,371 transaction rows, 2009–2011), split into monthly files; or (b) NPCI's monthly UPI statistics, downloaded by hand (the site blocks automated fetching). Build a workbook in which Power Query ingests every monthly file from a folder, a `PIVOTBY` or PivotTable produces the report, named `LAMBDA`s compute every derived metric, and a "Checks" tab proves the numbers.

**Acceptance criteria**
- Dropping next month's file into the folder and pressing Refresh updates every figure, with no formula edits.
- The "Checks" tab has at least 6 assertions (row counts per month, grand total equals the sum of raw rows, no negative quantities outside returns, no unmatched lookups, no blank keys, fiscal-quarter mapping covers every date), and all show TRUE.
- Cancelled invoices (Online Retail II invoice numbers starting with "C") or failed transactions are handled explicitly and documented.
- No hard-coded numbers in report cells; every input lives on one "Assumptions" tab.
- A one-page "How this works" tab a new colleague can follow.

**Stretch goals.** Rebuild the same report in Google Sheets with `QUERY`; compare the effort. Add a variance column that flags any month-on-month change above 2 standard deviations.

**What it proves to an employer.** You can take over a fragile recurring report and make it correct, refreshable and auditable in a day, which is the first task many analysts are given.

### P2 · E-commerce analytics query pack (L2, ~15 hours)

**Real-world inspiration.** Product and growth teams at marketplaces ask the same family of questions every week: retention, funnels, top sellers, delivery times. Uber's QueryGPT and Swiggy's Hermes both organise SQL knowledge by business domain for the same reason.

**What to build.** A Git repository of 15 documented queries over the BigQuery public datasets `thelook_ecommerce` and `ga4_obfuscated_sample_ecommerce`, also runnable in DuckDB on exported extracts. It must cover: deduplication, revenue by IST day with a date spine, 7-day moving average, top 3 products per category with ties, delivery-time deciles, monthly cohort retention, revenue retention, sessionization, an ordered 4-step funnel, first vs last-touch channel credit, a gaps-and-islands streak, a recursive rollup, `GROUPING SETS` subtotals, an as-of join, and one query of your choice.

**Acceptance criteria**
- Each query starts with a header stating the business question, the output grain, the definitions used and known limitations.
- Every query has a fixture test with a hand-computed answer; all 15 pass in CI.
- BigQuery and DuckDB outputs agree for every query (two-way `EXCEPT` on the same extract, with float tolerance stated).
- `sqlfluff lint` returns zero violations under the committed config.
- A cost table lists dry-run bytes for each query on BigQuery; no query scans a column it does not use.

**Stretch goals.** Parameterise the date range; add a `make` target that runs everything; publish a small static results page with Evidence or Quarto.

**What it proves to an employer.** You write warehouse SQL that is correct, tested, portable and cheap to run, and you document the assumptions a reviewer needs.

### P3 · Marketplace retention and delivery deep-dive with an AI audit (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Marketplaces live or die on repeat purchase, and late deliveries hurt it. The Olist Brazilian e-commerce dataset (about 100,000 orders from 2016 to 2018, with orders, items, payments, reviews, customers and sellers in separate tables) is one of the few public datasets with this full structure. The analysis questions below are illustrative and do not describe Olist's own decisions.

**What to build.**
1. A DuckDB warehouse built from the raw Olist CSVs with a staging layer (types, deduplication, and a documented time-zone choice, since Brazil spans several time zones) and grain statements for every table.
2. A tested SQL library answering: customer cohort retention; repeat-purchase rate by state; delivery-time deciles and late-delivery rate by seller cohort; the relationship between lateness and review score; seller concentration (top 10% share of revenue); and a point-in-time join of each order to the seller's rolling 90-day late rate at order time.
3. An AI audit: write 25 gold questions with gold SQL and gold results; have two assistants (for example, Claude and Gemini) draft SQL from the schema plus your definitions; score by result equality; classify every failure.
4. A two-page memo to a (fictional) head of marketplace operations with one recommendation, its expected effect, and the uncertainty.

**Acceptance criteria**
- Full rebuild from raw CSVs runs with one command in under 5 minutes on a laptop.
- At least 30 assertions (uniqueness, not-null, accepted values, reconciliation of payments to order totals within a stated tolerance) pass; any reconciliation gap is explained.
- Retention matrix masks immature cohort cells, and the memo explains why.
- The lateness and review-score analysis states clearly that it shows association, not cause, and names two confounders.
- AI audit reports accuracy per assistant with the 25-question denominator, a failure taxonomy table, and at least 3 failures that ran without error but returned wrong numbers.
- Oral defence: you rewrite any one query from the library live, AI off, in under 10 minutes.

**Stretch goals.** Load the same model into BigQuery and compare cost; add a Looker Studio or Metabase dashboard on top; rerun the AI audit after adding column descriptions and five example queries to the prompt, and measure the change.

**What it proves to an employer.** You can own an analysis end to end: model raw data, prove every number, use AI to go faster while catching its mistakes, and turn the result into a decision someone can act on.

## Feeds into

- [DAN304 Analytics Engineering](../DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md): your CTE pipelines become dbt models and your assertions become dbt tests.
- [DAN305 Product and Business Analytics](../DAN305_product_and_business_analytics_metrics_funnels/README.md): cohorts, funnels and sessions become metric trees and product decisions.
- [DAN401 AI-Augmented Analytics](../../year_4/DAN401_ai_augmented_analytics_text_to_sql_copilots/README.md): the P3 gold harness grows into a full text-to-SQL evaluation.
- [DAN403 Domain Analytics](../../year_4/DAN403_domain_analytics_finance_marketing_operations/README.md): revenue cohorts and point-in-time joins return in finance and operations work.
- [CAR301 Career Lab I](../../../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md): P2 and P3 are portfolio pieces; Chapter 11's timed rounds continue there.
