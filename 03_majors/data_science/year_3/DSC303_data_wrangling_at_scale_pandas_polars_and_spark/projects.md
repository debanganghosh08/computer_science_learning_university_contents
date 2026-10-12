# DSC303 · Labs and projects

Every lab and project follows **invariants first**: before writing transformation code, write down the checks the output must pass (row counts, unique keys, conserved totals, allowed nulls, value ranges) and encode them as tests. Generated code is accepted only when the tests pass. Record peak memory and wall time for every pipeline you submit, with your hardware stated.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · pandas 3 in depth | Run a pandas 2-era notebook under pandas 3 and fix copy-on-write and string-dtype breakages (and ask an assistant to fix it too); then named aggregations, `transform`, rolling and time-based windows on an events table | Diff of fixes; a log of each assistant suggestion that relied on old behaviour; three `apply` calls replaced with measured speed-ups | 6 h (2 weeks) |
| 2 · Cleaning Indian market data | Agmarknet mandi prices: units, lakh/crore formats, DD/MM dates, commodity and market name variants | pandera schema; cleaning report with counts of each fix | 4 h |
| 3 · Join cardinality (AI off) | Predict, then verify, row counts for ten joins including many-to-many and null keys; anti-joins; `merge_asof` | Prediction sheet vs actual counts; explanations for misses | 3 h |
| 4 · Polars lazy plans | Translate Lab 1 to Polars; inspect plans with `explain`; stream an aggregation larger than RAM | Plans before/after pushdown; memory and time table | 3 h |
| 5 · DuckDB over Parquet | One year of NYC TLC trip records queried in place: window functions, `QUALIFY`, sessionisation | SQL files; results; query times cold and warm | 4 h (2 weeks) |
| 6 · Profiling and 10× speed-up | Profile a slow feature job; apply vectorisation, dtypes, partitioning | Profile reports before and after; table of gains per change | 3 h |
| 7 · Spark local mode and skew | Run a join-heavy job in local Spark; read the UI; reproduce and fix skew with broadcast, salting and AQE | Screenshots of stages; timings; proof outputs are unchanged | 5 h (2 weeks) |
| 8 · Time zones and H3 | Repair a mixed UTC/IST log; assign points to H3 cells; build a store × day panel with explicit zeros | Notebook; invariant tests for the panel | 3 h |
| 9 · Notebook to package | Turn a Jupyter analysis into a `uv`-locked package with tests and a marimo or script entry point | Repository a classmate rebuilds from scratch in under 10 minutes | 4 h |
| 10 · Cross-engine diff | Implement the same pipeline in pandas, Polars and DuckDB; diff with checksums | Diff report; the root cause of every disagreement (nulls, float order, collation) | 3 h |

## Projects

### P1 · A clean, validated mandi-price dataset (L1, ~6 hours)

**Real-world inspiration.** Agmarknet publishes daily arrival and price reports from agricultural markets across India. Researchers, traders and policy teams use it, and every user re-cleans the same problems: unit inconsistencies, renamed markets, duplicated reports and mixed date formats.

**What to build.** A script that downloads (or reads supplied extracts of) one year of prices for five commodities in three states and produces a tidy Parquet table with a schema, a data dictionary and a cleaning log.

**Acceptance criteria**
- The output is keyed by (market code, commodity, variety, date) and the key is unique, enforced by a test.
- A pandera schema validates types, units (₹ per quintal) and plausible price ranges; rows that fail are written to a quarantine file with reasons.
- Market and district names are mapped to LGD codes where possible; unmatched names are listed with their counts.
- The cleaning log reports, for each rule, how many rows it changed.
- 30 randomly sampled output rows are checked by hand against the source and all match.

**Stretch goals.** A weekly price index per commodity and state with documented weights; an alert when a market stops reporting.

**What it proves to an employer.** You can turn a messy public source into something others can trust, and you can show exactly what you changed.

### P2 · One question, three engines, a year of trips (L2, ~15 hours)

**Real-world inspiration.** Ride-hailing and delivery companies compute demand by zone and hour to set prices and position supply. The NYC Taxi and Limousine Commission publishes trip records as monthly Parquet files, large enough that naive pandas code struggles on a laptop.

**What to build.** A pipeline that computes, for a full year of trips (yellow taxi plus high-volume for-hire vehicle files; report the total row count you processed), hourly demand and median trip duration by pickup zone, flags anomalous hours, and outputs a feature table for a forecasting model. Implement it in pandas, Polars (lazy) and DuckDB, and write a short engineering report.

**Acceptance criteria**
- Invariants are written first and pass on all three implementations: trip counts per month match a direct count of the source files; no trip is assigned to two zones; dropped rows (invalid timestamps, negative durations) are counted and justified.
- The three outputs are identical up to a documented tolerance, proven by checksums on sorted output.
- A performance table reports wall time and peak memory for each engine on stated hardware; the fastest implementation runs in under 16 GB of RAM.
- The report recommends one engine for this team (illustrative: three data scientists, no cluster) and justifies it.
- The repository rebuilds the results with one command from raw files.

**Stretch goals.** Run the Polars or DuckDB version on two years of data with streaming; add a PySpark implementation in local mode and explain where it is slower and why.

**What it proves to an employer.** You can process data at realistic scale on modest hardware, prove correctness across implementations, and make a reasoned tooling decision.

### P3 · A reproducible India district panel (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Research on India's development, health and labour markets depends on joining datasets across sources and years, despite district splits, renames and changing codes. The SHRUG platform harmonises village and town data across census rounds; Local Government Directory codes provide official identifiers. Teams that get this layer right enable every later analysis.

**What to build.** A district × year panel that combines at least four public sources, for example SHRUG covariates, NFHS district indicators, PLFS district or state aggregates computed with weights, and a data.gov.in or RBI series, with explicit handling of boundary changes. Deliver Parquet files, a data dictionary, a datasheet, a crosswalk table and a test suite.

**Acceptance criteria**
- A documented crosswalk maps every district in every source year to a stable identifier, with the rule used for splits (for example, area or population weights) and a list of unresolved cases.
- Each source's totals are conserved after aggregation to the panel, within stated tolerances, proven by tests.
- The pipeline runs end to end with one command, is engine-agnostic for at least one stage (Narwhals or SQL), and finishes in under 30 minutes on a laptop.
- The datasheet states sources, licences and terms of use, collection years, known errors and recommended uses and misuses.
- A second student reproduces the panel from scratch on their machine and gets identical checksums.
- An exploratory notebook shows three correlations in the panel and states clearly that they are not causal.

**Stretch goals.** Publish the panel (where the source licences allow) with a versioned release and changelog; add a small DuckDB-backed query interface; add geometry and maps.

**What it proves to an employer.** You can build the data foundation that research and policy teams depend on, with the traceability and testing of a data engineer and the judgement of a data scientist.

## Feeds into

- [DSC301 Statistical Inference and Modeling](../DSC301_statistical_inference_and_modeling/README.md): the P3 panel supplies district covariates for small-area models.
- [DSC304 Experimental Design and Causal Inference](../DSC304_experimental_design_and_causal_inference/README.md): the P3 panel is the starting point for policy-evaluation designs.
- [DSC401 Time Series and Forecasting](../../year_4/DSC401_time_series_analysis_and_forecasting/README.md): P2's zone-hour table is a forecasting dataset.
- [DSC403 Recommender Systems](../../year_4/DSC403_recommender_systems_and_personalization/README.md): large interaction logs need the Polars, DuckDB and Spark skills from this course.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): a well-documented panel is a strong base for a thesis.
