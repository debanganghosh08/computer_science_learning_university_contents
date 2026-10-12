# FND115 · Databases I: Data Modeling and SQL

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 1 · 2 | 4 (≈ 120 hours) | L0 → L2 | [FND101](../../semester_1/FND101_programming_i_computational_thinking_with_python/README.md) | [CS211](../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [DAN301](../../../03_majors/data_analysis/year_3/DAN301_spreadsheets_to_sql_analytical_querying_in_depth/README.md), [DAN302](../../../03_majors/data_analysis/year_3/DAN302_business_statistics_and_experimentation/README.md), [DAN304](../../../03_majors/data_analysis/year_3/DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md), [DAN305](../../../03_majors/data_analysis/year_3/DAN305_product_and_business_analytics_metrics_funnels/README.md) |

## Why this course matters now

Nearly every system that matters (bookings, payments, orders, grades) keeps its truth in a database. In the 2025 Stack Overflow survey, PostgreSQL was the most used database (55.6% of respondents) and the most admired. SQLite's maintainers estimate that over a trillion SQLite databases are in active use, mostly inside phones and applications. AI assistants now write SQL from plain English, and the public benchmarks show both progress and limits. On BIRD, the best system reaches 82.95% execution accuracy against 92.96% for human experts. On Spider 2.0's enterprise workflows, the strongest model in the original paper solved 17.1% of tasks. The model does not know what your business means by "active user", whether a join silently doubles revenue, or whether two people can book the same seat. Designing schemas that make bad data impossible, and checking that a query answers the question that was actually asked, is human work, and this course trains it.

## Learning outcomes

By the end you can:

1. Explain the relational model (relations, keys, relational algebra) and why SQL is declarative.
2. Write correct SQL in PostgreSQL 18 and SQLite, from `SELECT` to joins, grouping, subqueries, CTEs, recursive CTEs and window functions, including correct handling of `NULL`.
3. Turn a written business description into an ER model and then into a normalised (3NF/BCNF) schema, and justify any denormalisation.
4. Enforce business rules in the database with types and constraints (`NOT NULL`, `UNIQUE`, `CHECK`, foreign keys, exclusion constraints).
5. Load, change and migrate data safely and repeatably with versioned migrations and backups you have tested.
6. Read `EXPLAIN ANALYZE` output, design indexes for a workload, and show the speed-up with measurements.
7. Use transactions and isolation levels to prevent lost updates and double booking, and explain the anomaly each level allows.
8. Use SQL from Python safely (parameterised queries, transactions) and evaluate AI-generated SQL against a set of questions with known answers.

## Chapters and lessons

### Chapter 1 · The relational model (week 1)

| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Why a database | Concurrency, integrity, durability and querying, compared with files; Codd's relational model (1970): relations, tuples, attributes, domains, keys | Answer the same three questions with a Python dict, SQLite and PostgreSQL; list what broke or got easier |
| 1.2 PostgreSQL and SQLite | Client-server vs embedded; `psql` meta-commands; the `sqlite3` shell; when SQLite is the right choice | Load the Indian Railways timetable CSV from data.gov.in into both |
| 1.3 Declarative thinking | Logical processing order: `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT` | Rewrite five Python loops as single SQL queries |
| 1.4 Relational algebra | Selection, projection, join, union, difference, rename | Translate six queries between algebra and SQL |

**Check your understanding:** (1) Name two problems a CSV file cannot solve when 100 people write at once. (2) Why can't `WHERE` use a column alias defined in `SELECT`? (3) When would you ship SQLite instead of PostgreSQL?

### Chapter 2 · Querying and aggregating one table (weeks 2–3)

| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Filtering and sorting | `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT`, expressions, aliases | 20 questions on the timetable data |
| 2.2 `NULL` | Three-valued logic, `IS NULL`, `COALESCE`, `NULLIF`, `NULL` inside `IN` and comparisons | Predict 10 `NULL` results, then run them |
| 2.3 Types that bite | `numeric` for money (never `float`), `text`, `timestamp` vs `timestamptz`, `Asia/Kolkata`, intervals | Compute train journey durations that cross midnight |
| 2.4 Aggregates | `COUNT(*)` vs `COUNT(col)` vs `COUNT(DISTINCT col)`, `SUM`, `AVG`, `MIN`, `MAX` | The 20 stations with the most departures |
| 2.5 Grouping | `GROUP BY`, `HAVING`, the `FILTER` clause, `CASE` | Success and failure rates per bank on a synthetic UPI-style dataset (illustrative) |
| 2.6 Time series | `date_trunc`, `generate_series` to fill missing days, `ROLLUP` for subtotals | Daily volume with zero-filled gaps and a monthly subtotal |

**Check your understanding:** (1) Why does `WHERE x <> 5` drop rows where `x` is `NULL`? (2) Why is `float` wrong for rupees and paise? (3) What is the difference between filtering in `WHERE` and in `HAVING`?

### Chapter 3 · Joins and set operations (week 4)

| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Inner joins | Join keys, `ON` vs `USING`, joining a table to itself | Show each train with its source and destination station names |
| 3.2 Outer, semi- and anti-joins | `LEFT JOIN`, `EXISTS`, `NOT EXISTS`; the `NOT IN` plus `NULL` trap | Stations with no departures; users with no transactions |
| 3.3 Fan-out | Why totals double after a one-to-many join; aggregating before joining | Find and fix a revenue report that double-counts |
| 3.4 Set operations | `UNION` vs `UNION ALL`, `INTERSECT`, `EXCEPT`; comparing two result sets | Direct trains between two stations, with stop order respected |

**Check your understanding:** (1) Why can `NOT IN (subquery)` return no rows at all? (2) How do you notice fan-out before it reaches a dashboard? (3) Why is `EXCEPT` in both directions a good test that two queries are equal?

### Chapter 4 · Entity-relationship modelling (weeks 5–6)

| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Entities and relationships | Chen's ER model (1976) and crow's-foot notation; cardinality and participation | Model a college library |
| 4.2 Many-to-many relationships | Associative entities and attributes on relationships | Passengers, bookings and berths |
| 4.3 Weak entities and keys | Identifying relationships; natural vs surrogate keys; composite keys | Coaches and berths inside a specific train run on a specific date |
| 4.4 Case study: rail reservations (illustrative) | Stations, trains, ordered stops, train runs, coaches, berths, bookings, passengers, PNRs, CNF/RAC/WL status | A full ER diagram in Mermaid with a one-page design note |
| 4.5 Case study: UPI-style payments (illustrative) | Users, virtual payment addresses, bank accounts, payment requests, transactions, mandates, disputes; money records are append-only | An ER diagram plus a list of invariants the schema must enforce |

**Check your understanding:** (1) Why is "a booking has a seat" too vague to model? (2) When does a relationship need its own table? (3) Why should a payment record never be updated in place?

### Chapter 5 · Normalisation and schema definition (weeks 6–7)

| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Functional dependencies | Update, insert and delete anomalies; finding dependencies in real data | Find the dependencies in a messy 2,000-row spreadsheet |
| 5.2 Normal forms | 1NF, 2NF, 3NF, BCNF; lossless decomposition | Normalise the spreadsheet to BCNF and show one lossy decomposition |
| 5.3 DDL and types | `CREATE TABLE`, `bigint`, `numeric`, `timestamptz`, `uuid` (with `uuidv7()` in PostgreSQL 18), generated columns, when `jsonb` helps and when it hides a schema | DDL for the rail model |
| 5.4 Constraints | Primary and foreign keys with `ON DELETE`, `UNIQUE`, `CHECK`, `NOT NULL`; exclusion constraints and PostgreSQL 18 temporal `WITHOUT OVERLAPS` | A constraint that rejects overlapping bookings of one berth |
| 5.5 Deliberate denormalisation | Read-heavy reporting, partitioning; Zerodha's published PostgreSQL setup as a case study | A one-page "normalise or not" decision for three scenarios |

**Check your understanding:** (1) Which anomaly appears if a station's name is stored on every stop row? (2) Why enforce a rule in the database when the app already checks it? (3) Give a case where denormalising is the right call, and what it costs.

### Chapter 6 · Changing data safely (week 8)

| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 DML | `INSERT`, `UPDATE`, `DELETE`, `RETURNING` (with `OLD`/`NEW` in PostgreSQL 18), upserts with `ON CONFLICT` | An idempotent daily loader: running it twice changes nothing |
| 6.2 Bulk loading | `COPY`, the SQLite `.import` command, staging tables, validating before merging | Load 10⁶ synthetic rows; time `COPY` against a Python insert loop |
| 6.3 Migrations as code | Versioned forward and backward SQL files; Flyway and Alembic concepts; expand-then-contract changes | Five migrations applied to a fresh database in CI |
| 6.4 Backup and restore | `pg_dump` and `pg_restore`; SQLite `.backup`; an untested backup is not a backup | A timed restore drill |

**Check your understanding:** (1) Why add a new `NOT NULL` column in three steps on a live table? (2) What makes a loader idempotent? (3) How do you know your backup works?

### Chapter 7 · Subqueries, CTEs and views (week 9)

| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Subqueries | Scalar and correlated subqueries; `EXISTS`; `LATERAL` | Latest transaction per user with `LATERAL` |
| 7.2 Common table expressions | `WITH` for readability and testing parts of a query | Rewrite a 60-line nested query as named steps |
| 7.3 Recursive CTEs | Hierarchies and graphs in SQL | Stations reachable within two train changes; compare with the BFS from [FND112](../FND112_data_structures_and_algorithms_i/README.md) |
| 7.4 Views | Views, materialised views and refresh | A materialised daily dashboard view |

**Check your understanding:** (1) When is a correlated subquery fine, and when is it a performance trap? (2) What stops a recursive CTE from looping forever on a cyclic graph? (3) When does a materialised view return wrong answers?

### Chapter 8 · Window functions (week 10)

| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Ranking | `OVER`, `PARTITION BY`, `ROW_NUMBER`, `RANK`, `DENSE_RANK` | Top 3 merchants per city by volume (synthetic data) |
| 8.2 Row-to-row | `LAG`, `LEAD`, first and last values | Time between consecutive payments per user |
| 8.3 Running calculations | Running totals, moving averages; `ROWS` vs `RANGE` vs `GROUPS` frames | A 7-day moving average of daily volume |
| 8.4 Gaps, islands and sessions | Streaks, sessions split by 30-minute gaps | The longest daily activity streak per user |

**Check your understanding:** (1) Why can't you filter on a window function in `WHERE`? (2) When do `RANK` and `DENSE_RANK` give different answers? (3) Why does the default frame surprise people when `ORDER BY` is present?

### Chapter 9 · Indexes and query plans (weeks 11–12)

| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 How an index finds rows | A B-tree as sorted pages a few levels deep; heap tables; leaf scans (CS211 covers the internals) | Estimate pages read with and without an index for three queries |
| 9.2 Reading plans | `EXPLAIN (ANALYZE, BUFFERS)`; sequential, index and bitmap scans; nested-loop, hash and merge joins; estimates vs actual rows | Read six plans and find the misestimate |
| 9.3 Designing indexes | Selectivity, column order in composite indexes, covering (`INCLUDE`), partial and expression indexes, B-tree skip scan in PostgreSQL 18 | Make a query on 10⁶ rows at least 100× faster and record before and after |
| 9.4 What indexes cost | Slower writes, storage, unused indexes; N+1 query patterns from application code | Measure insert throughput with 0, 3 and 8 indexes |

**Check your understanding:** (1) Why does `WHERE lower(email) = …` ignore an index on `email`? (2) Why does column order matter in `(city, created_at)`? (3) When is a sequential scan the right plan?

### Chapter 10 · Transactions and concurrency (week 13)

| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 ACID | `BEGIN`, `COMMIT`, `ROLLBACK`, savepoints | A transfer that can never leave money half-moved |
| 10.2 Isolation | Dirty reads, non-repeatable reads, phantoms, lost updates, write skew; Read Committed (PostgreSQL's default), Repeatable Read, Serializable | Reproduce a lost update with two `psql` sessions, then prevent it |
| 10.3 Double booking | `SELECT … FOR UPDATE`, unique and exclusion constraints, optimistic version columns, retrying serialisation failures | 50 concurrent clients book one berth; exactly one succeeds |
| 10.4 Idempotency and SQLite | Idempotency keys for payment requests; SQLite's single writer and WAL mode | A payment endpoint that is safe to replay |

**Check your understanding:** (1) Which anomaly does Read Committed allow that causes double booking? (2) Why must code that uses Serializable be ready to retry? (3) How does an idempotency key differ from a unique constraint on the amount?

### Chapter 11 · SQL from programs, and AI-written SQL (week 14)

| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Drivers | Python `sqlite3` and psycopg 3; parameters; transactions in code; connection pooling basics | Port the loader and a report to Python |
| 11.2 SQL injection, the defender's view | Parameterised queries, least-privilege roles; OWASP Top 10:2025 lists Injection as A05 | Review five code snippets and fix the injectable ones |
| 11.3 ORMs | SQLAlchemy Core vs ORM; N+1 queries; when to write SQL yourself | Find an N+1 problem by logging the queries an ORM sends |
| 11.4 Verifying text-to-SQL | Gold questions, comparing result sets, checking `NULL`s and duplicates, read-only roles, `EXPLAIN` | Build a 25-question harness with gold SQL and grade an assistant's answers |

**Check your understanding:** (1) Why does an ORM not make injection impossible? (2) An AI query returns plausible numbers. Name three checks before you trust it. (3) Why should AI-generated SQL run under a read-only role?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Two databases | Both loaded, first queries |
| 2–3 | 2 | Lab 2 · Single-table drills; Lab 3 · Aggregation | 40 graded queries |
| 4 | 3 | Lab 4 · Joins | Fan-out bug fixed; P1 starts |
| 5–6 | 4 | Lab 5 · ER modelling studio | Two reviewed ER diagrams; P1 due |
| 6–7 | 5 | Lab 6 · Normalise and constrain | BCNF schema with DDL; P2 starts |
| 8 | 6 | Lab 7 · Migrations and loading | CI migrations |
| 9 | 7 | Lab 8 · CTEs and recursion | Reachability query |
| 10 | 8 | Window-function set | 12 queries; P2 due |
| 11–12 | 9 | Lab 9 · Indexes | Before/after plans; P3 starts |
| 13 | 10 | Lab 10 · Concurrency | Lost-update reproduction and fix |
| 14 | 11 | Text-to-SQL harness | Graded assistant report |
| 15 | Review and exam | Practical exam (AI off) and P3 demo | P3 due |

## Working with AI in this course

- **Use AI for:** a first draft of a query from a schema you paste in, which you then verify; explaining an `EXPLAIN` plan (checked against the PostgreSQL docs); generating realistic synthetic data; reviewing an ER model for missing constraints; translating between SQLite and PostgreSQL dialects.
- **Do without AI (drills):** 10 queries a week written by hand against a schema printed on paper; normalising a table by hand; predicting `NULL` results; drawing ER diagrams; reading a plan before running it.
- **Verify AI output by:**
  - running it on a fixture with known answers;
  - comparing it with a second method (pandas, or a differently written query, using `EXCEPT` in both directions);
  - checking row counts before and after each join;
  - testing empty, `NULL` and duplicate cases;
  - running `EXPLAIN ANALYZE` at realistic volume;
  - executing it only under a read-only role.
- **Where AI still fails here:** BIRD and Spider 2.0 (above) show a measurable gap, largest on messy, enterprise-scale schemas. In your harness, look for and log:
  - join fan-out;
  - `NOT IN` with `NULL`s;
  - time-zone mistakes (UTC vs IST);
  - business terms such as "active" or "failed" given one silent meaning;
  - dialect mix-ups;
  - SQL assembled from strings. Veracode's 2025 study found that 45% of AI-generated code samples introduced OWASP Top 10 flaws.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 20% |
| Practical exam, AI off: 1-hour design plus 2-hour SQL | 30% |

**Mastery gate.** You pass when you can, with AI off, take an unseen business description and produce a normalised schema with constraints in 45 minutes. Then, in 75 minutes, you answer 10 questions on a provided dataset, including one window function, one recursive CTE and one anti-join, with results that match the answer key exactly. Finally, you make one slow query at least 10× faster with an index and prove it with `EXPLAIN ANALYZE`.

## Industry reality

PostgreSQL 18 (September 2025) added asynchronous I/O, `uuidv7()`, virtual generated columns, B-tree skip scan and temporal constraints. Zerodha has described running about 20 TB of PostgreSQL across sharded nodes, with monthly partitions and denormalised tables for bulk end-of-day loads. PhonePe has described TStore, its transaction store built on HBase with a schema registry that checks compatibility. That is a reminder that relational design ideas (schemas, invariants, compatibility) outlive any one database. Stripe has described Ledger, its double-entry system for tracking money movement. Data analyst, data engineer and backend interviews test SQL directly, and often live.

**Interview questions from this course**

1. *"Return the top 3 products by revenue in each category."* Window function with `DENSE_RANK` vs `ROW_NUMBER` and how ties should behave; an alternative with `LATERAL`; `NULL` revenue; which index helps.
2. *"After adding a join, revenue doubled. Why?"* One-to-many fan-out; aggregating before joining; why `COUNT(DISTINCT)` hides rather than fixes it; tests that catch it.
3. *"Normalise this orders spreadsheet. Would you ever denormalise it?"* Functional dependencies, anomalies, 3NF/BCNF; read patterns and materialised views; the cost of keeping copies consistent.
4. *"This query is slow. What do you do?"* Measure with `EXPLAIN ANALYZE`; check estimates vs actual rows; selectivity and composite column order; functions on indexed columns; the write cost of each index.
5. *"Two users book the last seat at the same moment. Walk me through what happens."* Transactions and isolation levels; `SELECT … FOR UPDATE` or a unique or exclusion constraint; optimistic versioning; retries; idempotency keys for the payment step.

## Resources (free first)

- **Courses:** [CS50's Introduction to Databases with SQL](https://cs50.harvard.edu/sql/); [Stanford Databases: Relational Databases and SQL](https://www.edx.org/learn/relational-databases/stanford-university-databases-relational-databases-and-sql) (edX); [CMU 15-445/645](https://15445.courses.cs.cmu.edu/) (internals, for later).
- **Documentation:** [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html), [window functions](https://www.postgresql.org/docs/current/tutorial-window.html), [`WITH` queries](https://www.postgresql.org/docs/current/queries-with.html), [constraints](https://www.postgresql.org/docs/current/ddl-constraints.html), [`EXPLAIN`](https://www.postgresql.org/docs/current/using-explain.html), [transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html), [explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html); [SQLite SQL reference](https://www.sqlite.org/lang.html), [appropriate uses](https://www.sqlite.org/whentouse.html), [WAL mode](https://www.sqlite.org/wal.html); [psycopg 3](https://www.psycopg.org/psycopg3/docs/); [SQLAlchemy](https://docs.sqlalchemy.org/en/20/).
- **Performance:** [Use The Index, Luke](https://use-the-index-luke.com/) (Winand).
- **Practice:** [PostgreSQL Exercises](https://pgexercises.com/); [SQLBolt](https://sqlbolt.com/); [Select Star SQL](https://selectstarsql.com/).
- **Modelling and security:** [Mermaid ER diagrams](https://mermaid.js.org/syntax/entityRelationshipDiagram.html); [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).
- **Papers:** E. F. Codd, "A Relational Model of Data for Large Shared Data Banks", *CACM* 13(6), 1970, [doi:10.1145/362384.362685](https://doi.org/10.1145/362384.362685); P. Chen, "The Entity-Relationship Model", *ACM TODS* 1(1), 1976, [doi:10.1145/320434.320440](https://doi.org/10.1145/320434.320440).
- **Datasets:** [Indian Railways Train Time Table](https://www.data.gov.in/catalog/indian-railways-train-time-table) (Ministry of Railways, Open Government Data Platform India).

## Sources

All checked 12 Oct 2026.

- Stack Overflow Developer Survey 2025, technology section (databases) — https://survey.stackoverflow.co/2025/technology
- SQLite, "Most Widely Deployed and Used Database Engine" — https://www.sqlite.org/mostdeployed.html · SQLite 3.54.0 (9 Oct 2026) — https://www.sqlite.org/changes.html
- PostgreSQL 18 release announcement (25 Sep 2025) — https://www.postgresql.org/about/news/postgresql-18-released-3142/ · versioning policy (18.x current; 19 in beta) — https://www.postgresql.org/support/versioning/
- BIRD text-to-SQL leaderboard (updated 9 Oct 2026) — https://bird-bench.github.io/
- Spider 2.0 (ICLR 2025) — https://spider2-sql.github.io/ · paper — https://arxiv.org/abs/2411.07763
- Veracode, 2025 GenAI Code Security Report (30 Jul 2025) — https://www.veracode.com/blog/genai-code-security-report/
- OWASP Top 10:2025 — https://top10.owasp.org/2025
- Zerodha Tech, "Working with PostgreSQL" (22 Apr 2021) — https://zerodha.tech/blog/working-with-postgresql/
- PhonePe Tech, "Demystifying TStore" (6 Aug 2024) — https://tech.phonepe.com/demystifying-tstore-the-backbone-of-billions-of-transactions-at-phonepe/
- Stripe, "Ledger: Stripe's system for tracking and validating money movement" — https://stripe.com/blog/ledger-stripe-system-for-tracking-and-validating-money-movement

_Last reviewed: 2026-10_
