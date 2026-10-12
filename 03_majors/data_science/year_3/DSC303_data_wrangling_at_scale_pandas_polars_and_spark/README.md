# DSC303 · Data Wrangling at Scale: pandas, Polars and Spark

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) (assumes [FND115](../../../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md) SQL) | [DSC403](../../year_4/DSC403_recommender_systems_and_personalization/README.md), [DSC401](../../year_4/DSC401_time_series_analysis_and_forecasting/README.md), [DSC404](../../year_4/DSC404_data_science_in_production_deployment_monitoring/README.md), [DEN302](../../../data_engineering/year_3/DEN302_batch_processing_with_spark/README.md) |

Part of the [Data Science major](../../README.md). This course is about getting analysis-ready data correctly and fast, on one machine or a small cluster. Building and operating pipelines is the Data Engineering major's job ([DEN302](../../../data_engineering/year_3/DEN302_batch_processing_with_spark/README.md), [DEN304](../../../data_engineering/year_3/DEN304_orchestration_and_pipelines_airflow_and_dagster/README.md)).

## Why this course matters now

Most errors in published and business analyses are not modelling errors; they are a join that duplicated rows, a date parsed as month-first, a filter that dropped a state, or an aggregation over the wrong unit. The tools also moved fast in 2026: pandas 3.0 (21 January 2026) made copy-on-write behaviour and a dedicated string data type the defaults; Polars 2.0 (6 October 2026) shipped with breaking changes; DuckDB reached 1.5 and PySpark 4.2 (July 2026). DuckDB and Polars scan Parquet lazily and can stream aggregations over data larger than memory, so a laptop handles work that once needed a cluster; you will measure how far it goes in P2. Assistants such as Claude Code, GitHub Copilot, ChatGPT and the Databricks Assistant write wrangling code instantly, and the code usually runs. Whether it is *right* (no silent fan-out, no lost rows, no misparsed Devanagari digits, no timezone shift) is something you must check with invariants, and that checking discipline is what this course builds.

## Learning outcomes

By the end you can:

1. **Model** a messy source as tidy tables with explicit keys, types and units, and **validate** it with a schema (pandera) and invariant tests.
2. **Write** idiomatic, fast pandas 3 code (copy-on-write, `str` dtype, nullable types, method chains) and **explain** its memory behaviour.
3. **Predict** the row count of any join before running it, and **detect** fan-out, orphan keys and duplicate entities.
4. **Use** Polars' lazy API and DuckDB SQL over Parquet, read their query plans, and **choose** between pandas, Polars, DuckDB and Spark for a given size and team.
5. **Profile and speed up** a slow wrangling job by at least 10× with measurements, not guesses.
6. **Run** Spark DataFrame jobs, **diagnose** shuffles and skew, and **fix** them with broadcast joins, salting or adaptive query execution.
7. **Clean** Indian administrative and market data: mixed scripts, lakh/crore formats, renamed districts, and Local Government Directory (LGD) codes.
8. **Turn** a notebook into a reproducible, tested package and **prove** that pandas, Polars and DuckDB versions of a pipeline give identical outputs.

## Chapters and lessons

### Chapter 1 · Tidy data and the columnar world (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Tidy data | Variables in columns, observations in rows, one table per unit (Wickham, 2014); wide vs long | Reshape three untidy government tables into tidy form |
| 1.2 Spreadsheet hygiene | Broman and Woo (2018): dates, blanks, merged cells, colour as data | Write the cleaning spec for a real Excel file from data.gov.in |
| 1.3 Types and units | Integers vs floats with missing values, decimals for money, categorical vs string, units in names | Find three type bugs in a provided dataset |
| 1.4 Arrow and Parquet | Columnar memory, row groups, compression, statistics, why Parquet beats CSV | Convert a 2 GB CSV to Parquet and compare size and scan time |

**Check your understanding:** (1) What is the unit of observation in a table of "district × year × crop" yields, and what is its key? (2) Why does storing money as float cause audit failures? (3) What does Parquet's per-row-group min/max let a query engine skip?

### Chapter 2 · pandas in depth (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 pandas 3 semantics | Copy-on-write by default; the end of chained assignment; the default `str` dtype and its missing-value sentinel | Migrate a pandas 2 notebook and log every behaviour change |
| 2.2 Indexing and selection | `loc`/`iloc`, boolean masks, `query`, MultiIndex costs and when to avoid it | Rewrite index-heavy code as plain columns and compare clarity and speed |
| 2.3 Group-by done well | `agg` with named aggregations, `transform` vs `apply`, the cost of Python-level `apply` | Replace three `apply` calls with vectorised group operations; measure |
| 2.4 Reshaping and windows | `melt`, `pivot_table`, `rolling`, `expanding`, `ewm`, time-based windows | Compute 7-day rolling active users per city |
| 2.5 Memory and dtypes | Categoricals, nullable integer and Arrow-backed types, downcasting, `memory_usage(deep=True)` | Cut a DataFrame's memory by 5× without losing information |

**Check your understanding:** (1) Why did chained assignment stop working in pandas 3, and what replaces it? (2) When is `transform` the right tool and `apply` the wrong one? (3) What is the memory cost of an object column of short strings?

### Chapter 3 · Cleaning real data (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Missing and sentinel values | NA codes (-99, "NA", "--"), structural vs random missingness | Inventory every missing-value code in a survey extract |
| 3.2 Indian formats | Lakh/crore separators, DD/MM dates, fiscal years (April–March), Devanagari and other digit scripts, `unicodedata` normalisation | Parse a mandi-price file with mixed formats without loss |
| 3.3 Names and codes | District and state renames, splits and spellings; joining on LGD codes instead of names | Map 50 messy district names to LGD codes with a documented fuzzy-match threshold (RapidFuzz) |
| 3.4 Deduplication | Exact vs near duplicates, entity keys, survivor rules | Deduplicate a merchant list and report precision on a hand-checked sample |
| 3.5 Validation as code | pandera schemas, range and uniqueness checks, failing loudly | Write a schema that catches each bug from Lesson 1.3 |

**Check your understanding:** (1) Why is joining on district names across census years unsafe? (2) How do you choose a fuzzy-match threshold, and how do you know its error rate? (3) What should a pipeline do when a validation check fails at 2 a.m.?

### Chapter 4 · Joins at scale, correctly (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Join cardinality | One-to-one, one-to-many, many-to-many; `validate=` and `indicator=` in pandas | Predict then verify the row count of ten joins |
| 4.2 Anti-joins and orphans | Finding keys that exist on one side only; referential checks | Report every order without a matching customer |
| 4.3 As-of and range joins | `merge_asof`, DuckDB `ASOF JOIN`, interval overlaps | Attach the price in force at each transaction time |
| 4.4 Slowly changing dimensions | Type 2 history tables; joining facts to the right version | Join sales to the store manager at the time of sale |
| 4.5 Entity resolution basics | Blocking, pairwise scoring, clustering; evaluation with a labelled sample | Link two company lists without exact keys |

**Check your understanding:** (1) Your join turned 1 million orders into 1.3 million rows. List three causes and how to find which one. (2) Why is an as-of join safer than "latest value" for model features? (3) What is lost if you deduplicate before joining a history table?

### Chapter 5 · Polars (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Expressions | Columns as expressions, contexts (`select`, `with_columns`, `group_by`, `filter`), no index | Translate a 40-line pandas script to Polars |
| 5.2 Lazy execution | `scan_parquet`, query plans (`explain`), predicate and projection pushdown | Show a plan before and after a filter is pushed into the scan |
| 5.3 Streaming and out-of-core | The streaming engine, memory limits, sink operations | Aggregate a dataset larger than RAM |
| 5.4 Polars 2.0 changes | Reading release notes; deprecations (for example `cut`/`qcut`); pinning versions | Upgrade a project and fix the breakages with tests |
| 5.5 Dataframe-agnostic code | Narwhals for libraries that accept pandas, Polars and others | Write one feature function that runs on both libraries |

**Check your understanding:** (1) Why can a lazy query use less memory than the same eager steps? (2) What does projection pushdown save on a 100-column Parquet file? (3) How do you protect a project from breaking changes in a major release?

### Chapter 6 · DuckDB and SQL for data science (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 An in-process analytical database | Vectorised execution, querying Parquet and CSV directly, zero-copy exchange with Arrow, pandas and Polars | Query a year of NYC taxi Parquet files without loading them |
| 6.2 Window functions | `ROW_NUMBER`, `LAG`, running totals, `QUALIFY`, frames | Find each user's first and second purchase in one query |
| 6.3 Analytical SQL patterns | Sessionisation, funnels, gaps and islands, top-k per group | Sessionise click data with a 30-minute inactivity rule |
| 6.4 Mixing SQL and Python | When to push work to SQL; parameterised queries; reproducible `.sql` files | Rebuild a pandas feature pipeline as DuckDB SQL and diff outputs |

**Check your understanding:** (1) When is SQL clearer than dataframe code, and when is it worse? (2) What does `QUALIFY` do that `WHERE` cannot? (3) Why can DuckDB read a Parquet file faster than pandas can parse the same CSV?

### Chapter 7 · Performance engineering (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Measure first | Wall time, peak memory, `%timeit`, `memray`/`tracemalloc`, py-spy | Profile a slow notebook and find its top three costs |
| 7.2 Vectorisation and algorithmic fixes | Avoiding Python loops, sorting once, hashing vs sorting joins | Speed up a feature job 10× and show each step's gain |
| 7.3 Layout for speed | Partitioning by date, row-group size, sorted data, file counts | Re-partition data and measure query times |
| 7.4 Benchmarking honestly | Warm vs cold cache, representative queries, the DuckDB Labs db-benchmark methodology | Write a fair three-engine benchmark for your own query |

**Check your understanding:** (1) Why can a benchmark on a warm cache mislead you? (2) What is the cost of 100,000 tiny Parquet files? (3) Which is faster for a top-k per group: a sort or a heap, and why?

### Chapter 8 · Spark basics for data scientists (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 When you need a cluster | Data size, concurrency, existing platform; local mode as a learning tool | Decide pandas/Polars/DuckDB/Spark for six scenarios |
| 8.2 The DataFrame model | Lazy plans, transformations vs actions, partitions, the Spark UI | Read a physical plan and the stages it creates |
| 8.3 Shuffles and joins | Wide vs narrow dependencies; sort-merge vs broadcast joins | Make a join 5× faster with a broadcast hint |
| 8.4 Skew | Hot keys, salting, adaptive query execution's skew-join handling | Reproduce and fix one straggler task |
| 8.5 Spark Connect and pandas API on Spark | Thin clients, `pyspark.pandas`, where the pandas API on Spark behaves differently | Port a pandas notebook and list every difference you hit |

**Check your understanding:** (1) Why does `collect()` on a big DataFrame crash your driver? (2) What makes one task take ten times longer than the others? (3) When would you recommend against Spark?

### Chapter 9 · Time, text and geography in wrangling (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Time zones and calendars | UTC storage, IST display, DST in partner countries, resampling, business calendars | Fix an event log that mixes UTC and IST |
| 9.2 Text cleaning | Regex, Unicode NFC/NFKC, transliteration variants of the same name | Normalise product names written in Hindi, Hinglish and English |
| 9.3 Geography | Pincodes, lat/long, spatial joins, H3 hexagons | Assign delivery points to H3 cells and aggregate demand |
| 9.4 Panels | Balanced vs unbalanced panels, filling gaps explicitly, lag creation without leakage | Build a store × day panel with explicit zero-sale days |

**Check your understanding:** (1) Why store timestamps in UTC? (2) What goes wrong if you compute lags before filling missing days? (3) Why are pincodes poor proxies for neighbourhoods?

### Chapter 10 · Reproducibility: notebooks, scripts and packages (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Notebook failure modes | Hidden state, out-of-order execution, unpinned environments | Find the hidden-state bug in a shared notebook |
| 10.2 Reactive notebooks and scripts | marimo's reactive execution; when to move code to modules | Convert a Jupyter notebook to marimo and to a script |
| 10.3 Environments and project layout | `uv` lockfiles, Cookiecutter Data Science layout, config files | Rebuild a classmate's project on a clean machine in under 10 minutes |
| 10.4 Testing data code | pytest with small fixtures, pandera, property-based tests (Hypothesis), data versioning (DVC) | Write tests that fail on each bug from Chapters 3–4 |

**Check your understanding:** (1) Which belongs in a notebook and which in a module? (2) What does a lockfile protect you from that `requirements.txt` without versions does not? (3) What is a good fixture size for a data test?

### Chapter 11 · AI-assisted wrangling and cross-engine verification (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Prompting for wrangling | Giving schemas, keys and invariants to the assistant; asking for SQL and dataframe versions | Generate a pipeline from a written spec |
| 11.2 Invariants as acceptance tests | Row counts, key uniqueness, conservation of totals, null budgets | Write invariants first, then accept generated code only if they pass |
| 11.3 Cross-engine diffing | Run pandas, Polars and DuckDB versions; compare with checksums and tolerance rules | Find the engine that disagrees and explain why |
| 11.4 Documenting data | Data dictionaries, datasheets for datasets (Gebru et al.), change logs | Publish a datasheet for your P3 panel |

**Check your understanding:** (1) Which invariant catches a silent fan-out? (2) Why can two engines disagree on the same SQL (null ordering, float sums, string collation)? (3) What must a datasheet say about known errors?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · pandas 3 migration log | Tidy-data exercise |
| 2 | 2 | Lab 1 (cont.): Group-by and windows | — |
| 3 | 2–3 | Lab 2 · Cleaning Indian market data | — |
| 4 | 4 | Lab 3 · Join cardinality | **P1 due** |
| 5 | 5 | Lab 4 · Polars lazy plans | — |
| 6 | 5–6 | Lab 5 · DuckDB over NYC TLC Parquet | — |
| 7 | 6 | Lab 5 (cont.) | Mid-term practical (AI off) |
| 8 | 7 | Lab 6 · Profiling and 10× speed-up | — |
| 9 | 8 | Lab 7 · Spark local mode | — |
| 10 | 8 | Lab 7 (cont.): skew | **P2 due** |
| 11 | 9 | Lab 8 · Time zones and H3 | — |
| 12 | 10 | Lab 9 · Notebook to package | P3 checkpoint |
| 13 | 11 | Lab 10 · Cross-engine diff | — |
| 14 | 11 | Datasheet clinic | **P3 due** |
| 15 | Review | Live wrangling exam | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** translating between pandas, Polars, DuckDB SQL and PySpark; regex drafts; boilerplate for schemas and tests; reading unfamiliar error messages and query plans. Claude Code, GitHub Copilot, ChatGPT, Gemini in Colab and the Databricks Assistant all help here.
- **Do without AI (drills):** predicting join row counts; writing window-function SQL; reading a query plan; the weekly 20-minute "clean this file" sprint; the mid-term and final practicals.
- **Verify AI output by:** (1) writing invariants before you prompt (row counts, unique keys, totals conserved, null budgets) and running them on the output; (2) cross-engine diffing on the same input; (3) checking the library version the code assumes against your lockfile; (4) spot-checking 20 random rows by hand against the raw source.
- **Where AI still fails here:** you will measure it. Lab 1 asks you to log each assistant suggestion that relies on behaviour changed in pandas 3.0 (chained assignment, object-dtype checks); Lab 2 logs errors on Indian formats (lakh separators, DD/MM dates, Devanagari digits); Lab 10 records silent row losses. The course summary at week 14 compiles the class log into a list of the failure modes you actually observed.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 40% |
| Mid-term practical (AI off) | 10% |
| Final practical (AI off) | 25% |

**Mastery gate.** You pass when you can, AI off, in 3 hours: (1) take an unseen messy multi-file dataset to a validated tidy table with a passing schema and documented assumptions; (2) answer five analytical questions with joins and window functions whose row counts you predicted in writing beforehand; (3) speed up a supplied slow job at least 5× and explain each gain with a measurement.

## Industry reality

How much SQL, dataframe code and Spark a data scientist writes depends on the employer's platform; a common pattern is SQL against a warehouse followed by pandas or Polars for the final shaping, with Spark where the data already live on a Spark platform. Public examples of scale-out wrangling include the NYC Taxi and Limousine Commission trip records, published monthly as Parquet, which are a standard benchmark for laptop-scale engines, and the DuckDB Labs-maintained database-like ops benchmark comparing dataframe and SQL engines. In India, joining datasets across government sources depends on stable administrative codes such as those in the Local Government Directory, and on research platforms such as SHRUG that already harmonise villages and towns across census rounds.

**Interview questions from this course**

1. *Compute 7-day rolling active users per city from an events table.* Strong answer: deduplicates to user-day first, fills missing days explicitly, uses a time-based window or a self-join on dates, handles time zones, and states the complexity and the edge cases (first 6 days, cities with gaps).
2. *Your join returned more rows than the left table. Walk me through it.* Strong answer: checks key uniqueness on the right side, many-to-many relationships, null keys, type mismatches and duplicated source loads; uses validation flags or counts per key to prove the cause.
3. *You have 200 GB of Parquet and a 16 GB laptop.* Strong answer: lazy scans with DuckDB or Polars, column pruning and filter pushdown, partition-aware queries, streaming aggregation, sampling for exploration, and a clear threshold for moving to Spark or a warehouse.
4. *One Spark task takes 40 minutes while the rest take 2.* Strong answer: identifies skew from the Spark UI, finds the hot key, applies AQE skew-join handling, salting or a broadcast join, and verifies the result is unchanged.
5. *How do you make a colleague's notebook analysis reproducible?* Strong answer: pinned environment with a lockfile, parameters in config, top-to-bottom execution, data versions recorded, tests on key invariants, and a single command that rebuilds every number.

## Resources (free first)

- **Texts:** Wes McKinney, *Python for Data Analysis*, 3rd ed. (free online) — https://wesmckinney.com/book/ ; Wickham, Çetinkaya-Rundel and Grolemund, *R for Data Science* (2e) — https://r4ds.hadley.nz/ ; Wickham, "Tidy Data" — https://doi.org/10.18637/jss.v059.i10 ; Broman and Woo, "Data Organization in Spreadsheets" — https://doi.org/10.1080/00031305.2017.1375989
- **Documentation:** pandas (including the 3.0 release notes) — https://pandas.pydata.org/docs/whatsnew/v3.0.0.html ; Polars user guide — https://docs.pola.rs/ ; DuckDB — https://duckdb.org/docs/ ; Apache Spark — https://spark.apache.org/docs/latest/ ; Apache Arrow — https://arrow.apache.org/ ; Narwhals — https://narwhals-dev.github.io/narwhals/ ; pandera — https://pandera.readthedocs.io/ ; marimo — https://marimo.io/ ; uv — https://docs.astral.sh/uv/ ; Cookiecutter Data Science — https://cookiecutter-data-science.drivendata.org/ ; Hypothesis — https://hypothesis.readthedocs.io/ ; RapidFuzz — https://rapidfuzz.github.io/RapidFuzz/ ; H3 — https://h3geo.org/
- **Benchmarks:** database-like ops benchmark — https://duckdblabs.github.io/db-benchmark/
- **Data:** NYC TLC trip records — https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page ; Agmarknet mandi prices — https://agmarknet.gov.in/ ; Open Government Data platform — https://data.gov.in/ ; Local Government Directory — https://lgdirectory.gov.in/ ; SHRUG — https://www.devdatalab.org/shrug ; GH Archive (GitHub event logs) — https://www.gharchive.org/
- **Paid, optional:** Damji et al., *Learning Spark* (2nd ed., O'Reilly) for deeper Spark internals; DEN302 covers the same ground for free.

## Sources

- pandas, "What's new in 3.0.0 (January 21, 2026)" — https://pandas.pydata.org/docs/whatsnew/v3.0.0.html (checked 2026-10)
- Polars release py-2.0.0 (6 Oct 2026) — https://github.com/pola-rs/polars/releases (checked 2026-10)
- PyPI release pages: duckdb 1.5.6 (28 Sep 2026) https://pypi.org/project/duckdb/ ; pyspark 4.2.0 (14 Jul 2026) https://pypi.org/project/pyspark/ (checked 2026-10)
- Wickham, "Tidy Data", *Journal of Statistical Software* 59(10) (2014) — https://doi.org/10.18637/jss.v059.i10 (checked 2026-10)
- Broman and Woo, "Data Organization in Spreadsheets", *The American Statistician* (2018) — https://doi.org/10.1080/00031305.2017.1375989 (checked 2026-10)
- Gebru et al., "Datasheets for Datasets" (arXiv 1803.09010) — https://arxiv.org/abs/1803.09010 (checked 2026-10)
- DuckDB Labs, db-benchmark — https://duckdblabs.github.io/db-benchmark/ ; NYC TLC trip record data — https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page ; Development Data Lab, SHRUG — https://www.devdatalab.org/shrug (checked 2026-10)

_Last reviewed: 2026-10_
