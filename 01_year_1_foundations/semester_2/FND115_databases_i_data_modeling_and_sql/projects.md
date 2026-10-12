# FND115 · Labs and projects

Use PostgreSQL 18 and a current SQLite 3 release. Every SQL answer you submit is checked against an answer key or a second, independent computation. A query that "looks right" but has not been checked counts as unfinished. Keep all schema changes in versioned migration files.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Two databases | Install PostgreSQL and SQLite; load the Indian Railways timetable CSV into both; learn the `psql` and `sqlite3` meta-commands | Load scripts and matching row counts from both engines | 3 h |
| 2 · Single-table drills | 20 filtering and sorting queries, including 10 `NULL` predictions made before running | A SQL file plus results checked against the answer key | 3 h |
| 3 · Aggregation and time | 20 queries on a synthetic UPI-style dataset, including zero-filled daily series and IST vs UTC traps | SQL with results | 4 h |
| 4 · Joins | 15 join queries, including anti-joins; find and fix a seeded fan-out bug | SQL and a one-paragraph explanation of the bug | 4 h |
| 5 · ER modelling studio | Model the rail reservation and payments domains; peer-review another learner's model against a checklist | Mermaid ER diagrams, design notes, review comments given and received | 5 h |
| 6 · Normalise and constrain | Take a messy spreadsheet to BCNF; write DDL; write 10 bad-data inserts that must all fail | DDL and a test script showing each insert rejected with the right constraint | 5 h |
| 7 · Migrations and loading | Five migrations run in CI against a fresh database; `COPY` vs a Python insert loop; an idempotent loader | Repository, CI log, timing table | 4 h |
| 8 · CTEs and recursion | Rewrite a nested query as CTEs; a recursive reachability query; a materialised view | SQL plus a comparison with your BFS results from FND112 | 4 h |
| 9 · Indexes | On a 10⁶-row table, speed up five slow queries; measure insert throughput against the number of indexes | `EXPLAIN ANALYZE` before and after each change, and a timing table | 5 h |
| 10 · Concurrency | Reproduce a lost update and a double booking; fix them with `FOR UPDATE`, a constraint, and Serializable with retry | Scripts and logs from 50 concurrent clients | 5 h |

## Projects

### P1 · Timetable analytics (L1, ~6 hours)

**Real-world inspiration.** India's Open Government Data platform publishes the [Indian Railways Train Time Table](https://www.data.gov.in/catalog/indian-railways-train-time-table). Like most public data, it is real, useful and messy.

**What to build.** A repeatable load into a normalised schema (stations, trains, stops) in SQLite and PostgreSQL, and answers to 30 questions: the busiest stations, the longest routes, trains with the most stops, direct connections between pairs, and stations served by only one train.

**Acceptance criteria**
- The load is a single script that can be re-run. Row counts reconcile with the source file, and rejected rows are logged with reasons.
- Every answer is checked a second way, with pandas or a differently written query, and `EXCEPT` in both directions returns zero rows.
- At least 5 queries use joins, 3 use `EXISTS` or `NOT EXISTS`, and 3 use window functions.
- The same SQL runs on both engines, or every dialect difference is documented.
- The README has an ER diagram and 5 findings in plain English, each linked to the query behind it.

**Stretch goals.** Compare query times in DuckDB; add one chart per finding.

**What it proves to an employer.** You can take a messy public dataset all the way to verified answers, which is the everyday work of analysts and data engineers.

### P2 · Berth reservation database (L2, ~15 hours)

**Real-world inspiration.** On long-distance trains, one berth can be sold for one part of a route and again for a later part. This project is an illustrative model of that idea, not a copy of any real system's rules.

**What to build.** A PostgreSQL schema with migrations. It covers trains, runs (a train on a date), ordered stops, coaches, berths, passengers and bookings. Each booking's segment is an `int4range` of stop numbers, and a [`btree_gist`](https://www.postgresql.org/docs/current/btree-gist.html) exclusion constraint blocks overlapping segments on the same berth and run ([range types](https://www.postgresql.org/docs/current/rangetypes.html)). Add a transactional booking function, an availability query, and waitlist promotion on cancellation.

**Acceptance criteria**
- 20 crafted test cases pass. Overlapping segments are rejected, and segments that only touch, such as A–B then B–C, are allowed.
- 50 parallel clients making 200 attempts each on one run produce zero double bookings, confirmed by a verification query. Every failed attempt ends as a clean retry or a reported error, never a crash.
- With 10⁶ bookings, the availability query for one run and segment takes under 50 ms. `EXPLAIN ANALYZE` output is shown and each index is justified.
- Cancellation promotes waitlisted passengers in first-come order, with tests.
- The database is rebuilt from migrations alone, and a restore from `pg_dump` is verified.

**Stretch goals.** Use PostgreSQL 18's temporal `WITHOUT OVERLAPS` for a time-based variant, such as platform occupancy. Port the core schema to SQLite and document which guarantees you lose.

**What it proves to an employer.** You can make the database itself guarantee a business rule under concurrency, instead of hoping the application gets it right.

### P3 · UPI-style payments ledger with analytics and an AI-SQL audit (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Stripe's [Ledger](https://stripe.com/blog/ledger-stripe-system-for-tracking-and-validating-money-movement) tracks money movement as double-entry records. Payment APIs use [idempotency keys](https://docs.stripe.com/api/idempotent_requests) so that retries never charge twice. Zerodha's [PostgreSQL write-up](https://zerodha.tech/blog/working-with-postgresql/) describes monthly partitioning at scale. All data in this project is synthetic.

**What to build**
- **Schema.** Accounts (user, merchant and system clearing accounts), journal entries, postings, and payment requests with idempotency keys and statuses. Postings are append-only, and a reversal is a new entry.
- **Generator.** About 5 million postings over 90 days for 100,000 users, 5,000 merchants and 10 banks, with realistic failures and reversals.
- **Analytics.** Twelve reports:
  - daily volume and value, and the P2P vs merchant split;
  - failure rate per bank;
  - the top merchants per city;
  - 7-day moving averages;
  - weekly cohorts by first payment;
  - a reconciliation query that finds any account whose stored balance differs from the sum of its postings.
- **AI audit.** 25 natural-language questions, each with gold SQL and a gold result set, used to grade an assistant's SQL.

**Acceptance criteria**
- **Balanced entries.** The postings in every entry sum to zero. This is enforced by a constraint trigger or deferred check, and 10 deliberate violations all fail.
- **Idempotency.** 10,000 requests replayed with duplicate keys by 32 concurrent workers create no duplicate entries.
- **Append-only.** The application role cannot `UPDATE` or `DELETE` postings, and a test proves it.
- **Reports.** Each report matches an independent pandas computation exactly and runs in under 2 seconds on the full dataset. `EXPLAIN ANALYZE` output and the indexes or materialised views used are documented.
- **AI audit report.** It gives the accuracy, an error taxonomy (fan-out, `NULL` handling, time zone, definition mismatch, dialect) and three fully analysed examples. Assistant SQL runs only under a read-only role.
- **Operations and docs.** Migrations, a timed backup-and-restore drill, and a README with the ER diagram, the list of invariants, and who can write what.

**Stretch goals.** Partition postings by month; add row-level security for merchant self-service views; load the data into DuckDB and compare analytics speed.

**What it proves to an employer.** You can design data systems that handle money, prove their invariants under concurrency, and audit AI-written SQL with evidence. Few candidates at intern level can show all three.

## Feeds into

- [CS211 Database Systems Internals](../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md): the B-trees, write-ahead logs and MVCC behind Chapters 9–10.
- The data analysis major: [DAN301](../../../03_majors/data_analysis/year_3/DAN301_spreadsheets_to_sql_analytical_querying_in_depth/README.md) (analytical SQL), [DAN304](../../../03_majors/data_analysis/year_3/DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md) (dbt and modelling) and [DAN305](../../../03_majors/data_analysis/year_3/DAN305_product_and_business_analytics_metrics_funnels/README.md) (metrics, funnels and cohorts) build on P1 and P3.
- [BE301 API Design](../../../03_majors/backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md) and the backend major reuse P2's concurrency patterns and P3's idempotency design.
- [FND114 Web Foundations](../FND114_web_foundations_http_html_css_and_javascript/README.md): P3 there stores its data with the techniques from this course.
