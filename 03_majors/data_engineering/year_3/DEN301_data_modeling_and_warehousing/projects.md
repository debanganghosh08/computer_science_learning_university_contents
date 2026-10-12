# DEN301 · Labs and projects

All labs run on a laptop with DuckDB, PostgreSQL and dbt (the Apache-2.0 `dbt-oss` distribution or dbt v2). Labs 6 and 7 also use one cloud warehouse free tier: the BigQuery sandbox (1 TB of query processing per month free, per GH Archive's notes) or a Snowflake trial. Labs 2–4 are done without AI assistants. From Lab 5 on, AI tools are allowed, but every submission includes a reconciliation query that proves the numbers.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Row store vs column store | Run 10 analytic queries on Olist in PostgreSQL and DuckDB; explain the gap with plans and bytes read | Timing table, two annotated plans, one-page explanation | 3 h |
| 2 · Grain hunting | Find and fix three planted grain violations (order vs order line, daily vs event, mixed currency) | Corrected models and a test per violation that would have caught it | 4 h |
| 3 · Idempotent SCD2 | Implement SCD2 with a hash diff in SQL; run it 3 times on the same input and on out-of-order input | Code, a test proving no change on re-run, and an as-of join | 5 h |
| 4 · Vault and OBT | Load a hub, link and two satellites from two sources; build a PIT table, a star mart and an OBT | Row counts per layer, storage and bytes-scanned comparison | 6 h |
| 5 · Parquet anatomy | Write NYC TLC trips with different sort orders, row-group sizes and encodings | Size table, `parquet_metadata()` excerpts, a prediction-vs-actual table of skipped row groups | 4 h |
| 6 · Warehouse economics | Predict bytes scanned (BigQuery dry run) or credits (Snowflake) for 8 queries, then run them | Prediction sheet with error per query and the cause of the biggest miss | 4 h |
| 7 · Pruning and clustering | Partition and cluster a 1-billion-row synthetic events table; measure 6 query shapes | Before/after profiles, pruning ratios, and a recommendation | 5 h |
| 8 · dbt with static analysis | Layer the Olist project (staging, intermediate, marts) with incremental models and model versions; run strict static analysis | Repository passing `dbt build`, zero strict findings, and a re-run diff that is empty | 8 h |
| 9 · Ledger reconciliation | Model a synthetic wallet with authorisations, captures, refunds and settlements | Reconciliation queries that balance to zero, and two planted breaks found | 4 h |
| 10 · AI against your marts | Ask an AI assistant 20 business questions before and after documenting your marts | Scored answer sheet, failure taxonomy (fan-out, SCD join, time zone, grain) | 4 h |

## Projects

### P1 · E-commerce star schema (L1, ~6 hours)

**Real-world inspiration:** every marketplace keeps an orders mart. The [Olist dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) is a real, anonymised marketplace export: orders, items, payments, reviews, sellers and customers in normalised tables.

**What to build:** a DuckDB star schema with `fct_order_items` (one row per order line), `fct_payments` (one row per payment instalment), and conformed `dim_customer`, `dim_seller`, `dim_product` and `dim_date`. Add a bus matrix, a one-paragraph grain statement per fact, and 10 business queries (GMV by seller state by month, late-delivery rate, average items per order, payment-type mix).

**Acceptance criteria:**
- Each fact has a uniqueness test at its declared grain, and it passes.
- The sum of `price + freight_value` in your fact equals the source sum exactly, and the order count matches the source `orders` table.
- Payment totals reconcile to order totals for at least 99% of orders, and every exception is listed with its cause.
- All 10 queries return the same answer when run against the source tables with hand-written joins.

**Stretch goals:** a role-playing date dimension (purchase, approved, delivered, estimated); an accumulating snapshot of the order lifecycle.

**What it proves to an employer:** you can declare grain and prove your numbers, which is what a first data-engineering ticket usually needs.

### P2 · Mandi price warehouse with history (L2, ~15 hours)

**Real-world inspiration:** India's Open Government Data platform ([data.gov.in](https://www.data.gov.in/)) publishes daily wholesale commodity prices from agricultural markets (the Agmarknet "current daily price" resource, with a free API key). Prices arrive late, get corrected, and market metadata changes when districts are reorganised.

**What to build:** a daily incremental pipeline (Python + dbt on DuckDB) that loads the price feed into a periodic snapshot fact `fct_market_price_daily` (grain: market × commodity × variety × date) with min, max and modal price. Add `dim_market` as SCD2 (state, district, market name), `dim_commodity`, and `dim_date` with Indian fiscal quarters and crop seasons. Keep the raw responses in a bronze folder so any day can be rebuilt.

**Acceptance criteria:**
- **Idempotency:** loading the same day twice, or replaying the last 7 days, leaves the fact table byte-for-byte identical (checked by a hash of the sorted table).
- **Late data:** a correction that arrives 3 days late replaces the old value and is recorded in an audit column. No duplicates appear at the declared grain.
- **History:** a provided district-change file creates new `dim_market` versions. An as-of query returns the old district for prices before the change date.
- **Semantics:** no query sums prices across markets or days. Spreads and volatility use correct non-additive logic, and a test fails if someone adds `SUM(modal_price)` to a mart.
- **Freshness:** a check fails if the newest loaded date is more than 2 days behind the run date.

**Stretch goals:** a monthly snapshot with arrival-volume weighting; a backfill of 3 years; a short write-up of price spreads for one commodity across states.

**What it proves to an employer:** you can build an incremental, history-aware model on messy public data and prove it is idempotent.

### P3 · Ride-hailing warehouse at scale (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** ride-hailing and delivery companies measure each trip as a lifecycle: request, driver on scene, pickup, drop-off. NYC's TLC publishes high-volume for-hire vehicle (HVFHV) trips with request, pickup and drop-off timestamps (plus an on-scene timestamp for accessible vehicles only, per the TLC data dictionary), alongside yellow and green taxi trips, as monthly Parquet files ([TLC trip records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)). Partly populated milestones like this are normal in real lifecycle data.

**What to build:** a warehouse over at least 24 months of yellow, green and HVFHV data (hundreds of millions of rows):

- a Data Vault integration layer that treats the three feeds as separate sources (hubs for zone and base, a trip link, source-specific satellites);
- a serving star with `fct_trip` (one row per trip) and an accumulating snapshot of trip milestones with wait-time measures (request to pickup for all HVFHV trips; on-scene measures only where populated, with the coverage reported);
- conformed `dim_zone` (taxi zones), `dim_base`, `dim_date` and `dim_time`;
- an OBT for one dashboard;
- documentation for every model, and a decision record explaining each layer.

Run it in DuckDB locally and in one cloud warehouse.

**Acceptance criteria:**
- **Correctness:** monthly row counts and fare totals per source reconcile with the raw Parquet files to within 0.01%. Every excluded row (negative fares, impossible timestamps) is counted in a quarantine table, with a reason code.
- **Grain:** uniqueness and not-null tests pass on every fact key. A fan-out test confirms that joining any dimension leaves fact totals unchanged.
- **History:** zone or base attribute changes are handled with SCD2, and an as-of test covers them.
- **Performance and cost:** 10 defined queries each meet a written budget (for example, at most 5 GB scanned or 0.05 credits). Before/after profiles show the partitioning and clustering choices that achieved it.
- **Rebuild:** the whole warehouse rebuilds from raw files with one command, and a second run produces identical marts.
- **AI-readiness:** an AI assistant answers at least 16 of 20 provided business questions correctly against your documented marts. Every wrong answer is analysed.
- **Write-up:** a 4-page design document covering grain, history, cost and the star vs vault vs OBT trade-offs, plus a 5-minute recorded walkthrough.

**Stretch goals:** a bitemporal fare-correction model; a comparison of the same marts on Snowflake and BigQuery with cost per query; an Iceberg-backed version of the gold layer (preview of [DEN305](../DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md)).

**What it proves to an employer:** you can model a real, large, multi-source business process end to end, defend each modelling choice with numbers, and make the result trustworthy for both analysts and AI assistants.

## Feeds into

- [DEN401 Data Quality, Observability and Data Contracts](../../year_4/DEN401_data_quality_observability_and_data_contracts/README.md): P3's tests and reconciliations become monitored contracts.
- [DEN305 Lakehouse Architecture](../DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md): the same models on Iceberg and Delta tables.
- [DEN402 Cloud Data Platforms](../../year_4/DEN402_cloud_data_platforms_snowflake_bigquery/README.md): cost per query across engines.
- [OV06 Data Platform and Analytics Engineering](../../../../04_overlaps/OV06_data_platform_analytics_engineering/README.md): semantic layers on top of these marts.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): P3 is a common capstone starting point.
