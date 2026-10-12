# BE303 · Data Modeling and Storage for Backends: Postgres, Redis and NoSQL

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [BE403](../../year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md), [BE401](../../year_4/BE401_payments_grade_systems_transactions_idempotency/README.md), [BE402](../../year_4/BE402_scalability_and_performance_caching_sharding/README.md) |

Part of the [Backend Engineering major](../../README.md). [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) taught how a database works inside: pages, B+trees, MVCC and the WAL. This course is about using one well from application code: modeling, indexing, isolation, migrations and choosing the right store.

## Why this course matters now

Most backend incidents are data incidents: a missing index, a lock held during a migration, a race that sells the last seat twice, a cache that serves stale prices. PostgreSQL is now the default choice. In the 2025 Stack Overflow survey, 58.2% of professional developers used it. In January 2026, OpenAI described running ChatGPT's main relational workload on one PostgreSQL primary with nearly 50 read replicas. To keep that safe, it allows only lightweight schema changes with a 5-second timeout, kills long-running queries, and rate-limits backfills so heavily that some take over a week. It also reported that a single ORM-generated 12-table join caused several high-severity incidents. AI assistants write schemas, ORM models and SQL quickly. Someone still has to decide whether a constraint belongs in the database, read the plan, predict which lock a migration takes, and say when Redis or DynamoDB is the better tool.

## Learning outcomes

By the end you can:

1. **Model** a business domain as tables, keys and constraints so that invalid states cannot be stored, and **justify** each denormalization with a query it serves.
2. **Design** indexes (composite, partial, expression, covering, GIN, BRIN) for a stated workload, and **prove** each one with `EXPLAIN (ANALYZE, BUFFERS)` on realistic data volumes.
3. **Choose** an isolation level and locking strategy for each write path, and **reproduce** lost updates, write skew and deadlocks before you fix them.
4. **Run** zero-downtime schema migrations (expand/contract, concurrent index builds, `NOT VALID` constraints, batched backfills) against a table under live load.
5. **Partition** large tables by time or tenant, and **operate** retention, vacuum and replication lag from an application's point of view.
6. **Use** JSONB where it helps and **refuse** it where it hides a schema.
7. **Apply** Redis patterns (cache-aside, rate limiting, leaderboards, streams, locks with fencing tokens) and **explain** their failure modes.
8. **Compare** document, wide-column and key-value stores by access pattern, and **design** a DynamoDB or Cassandra table from its queries.
9. **Audit** AI-generated schemas, ORM code and SQL for missing constraints, N+1 queries, unsafe migrations and wrong isolation assumptions.

## Chapters and lessons

### Chapter 1 · Modeling the domain (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 From nouns to tables | Entities, relationships, cardinality, the normal forms you actually use (1NF–3NF, BCNF) and why | Model a food-delivery domain: customers, restaurants, menus, orders, items, riders |
| 1.2 Keys | Natural vs surrogate keys, `bigint` identity vs UUIDv4 vs UUIDv7 (`uuidv7()` in PostgreSQL 18), exposing IDs safely | Insert 10M rows with UUIDv4 and UUIDv7 keys; compare index size and insert rate |
| 1.3 Types that prevent bugs | Money as `numeric` or integer paise (never `float`), `timestamptz`, `citext`, enums vs lookup tables, domains | Find five type bugs in a provided schema |
| 1.4 Constraints as the last line of defence | `NOT NULL`, `CHECK`, `UNIQUE`, foreign keys and `ON DELETE`, exclusion constraints, temporal `WITHOUT OVERLAPS` (PostgreSQL 18) | Make double-booking a room impossible at the database level |
| 1.5 When to denormalize | Read models, counters, materialized views, the update anomalies you accept | Add a denormalized order total and write the invariant check that keeps it honest |

**Check your understanding:** (1) Why is a `UNIQUE` constraint safer than "check, then insert" in application code, even inside a transaction? (2) What does a random UUIDv4 primary key do to a B+tree, and why does UUIDv7 help? (3) Name a constraint you would deliberately not enforce in the database, and say why.

### Chapter 2 · Indexing PostgreSQL (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 B-tree design | Column order in composite indexes, equality before range, sort order, PostgreSQL 18 skip scan | Index five queries on a 20M-row orders table; justify each column order |
| 2.2 Partial, expression and covering indexes | `WHERE status = 'pending'`, `lower(email)`, `INCLUDE`, index-only scans and the visibility map | Shrink an index by 90% with a partial index without slowing the query |
| 2.3 GIN, GiST and BRIN | Full-text search, trigram (`pg_trgm`), JSONB containment, BRIN for append-only time series | Build trigram search over 1M restaurant names; measure latency |
| 2.4 The write cost of indexes | HOT updates, `fillfactor`, write amplification, unused-index detection with `pg_stat_user_indexes` | Drop three useless indexes and measure insert throughput before and after |

**Check your understanding:** (1) Why does `(restaurant_id, created_at)` serve "latest orders for a restaurant" but `(created_at, restaurant_id)` does not? (2) When does an index-only scan still read the heap? (3) Why can adding an index make a write-heavy table slower overall?

### Chapter 3 · Reading plans and finding slow queries (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 `EXPLAIN (ANALYZE, BUFFERS)` | Nodes, loops, estimated vs actual rows, shared hit vs read, where time accumulates | Annotate ten real plans line by line |
| 3.2 Joins and estimates | Nested loop vs hash vs merge join, why estimates go wrong, `CREATE STATISTICS` for correlated columns | Fix a 100× misestimate with extended statistics |
| 3.3 Finding the culprits | `pg_stat_statements`, `auto_explain`, `log_min_duration_statement`, top-N by total time | Find the top three queries by total time on a replayed workload |
| 3.4 Queries written by ORMs | N+1 patterns, accidental cross joins, huge `IN` lists, `OFFSET` pagination; the 12-table join incident | Rewrite three ORM-generated queries and show the plan change |
| 3.5 Pagination that scales | Keyset (seek) pagination vs `OFFSET`, stable sort keys, cursors in APIs (links to BE301) | Page through 10M rows both ways and plot latency by page number |

**Check your understanding:** (1) A plan says `rows=1` and the actual is 80,000: what goes wrong next in the plan? (2) Why does `OFFSET 1000000` get slower as users page deeper? (3) Which queries should you optimize first: the slowest, or the most expensive in total?

### Chapter 4 · Transactions, isolation and locking (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Isolation in PostgreSQL | Read Committed (default), Repeatable Read (snapshot), Serializable (SSI); retrying on `40001` | Reproduce a lost update under Read Committed in two `psql` sessions |
| 4.2 Write skew and how to stop it | Snapshot anomalies, `SERIALIZABLE`, materializing conflicts, `SELECT … FOR UPDATE` | Prevent "two doctors go off call" three different ways |
| 4.3 Row locks and queues in tables | `FOR UPDATE`, `FOR NO KEY UPDATE`, `SKIP LOCKED`, `NOWAIT`; job queues in Postgres | Build a 16-worker job queue with `SKIP LOCKED`; prove no job runs twice |
| 4.4 Optimistic concurrency | Version columns, conditional `UPDATE … WHERE version = $1`, ETags end to end | Implement optimistic updates for an order and return `412` on conflict |
| 4.5 Deadlocks and lock queues | Lock ordering, deadlock detection, why one `ALTER TABLE` waiting for a lock blocks every later query; `lock_timeout` | Cause an outage-style lock queue on a test database, then prevent it |
| 4.6 Advisory locks and their limits | Session vs transaction advisory locks, leader election in one database, why not across services | Use an advisory lock to run a cron job on exactly one replica |

**Check your understanding:** (1) Why must application code retry serialization failures, and what makes a retry safe? (2) Why does a migration that "only takes a second" sometimes freeze an entire site? (3) When is optimistic concurrency worse than pessimistic locking?

### Chapter 5 · Operating Postgres as a developer (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 MVCC in practice | Dead tuples, bloat, autovacuum tuning per table, transaction-ID wraparound warnings | Create bloat with long transactions; watch vacuum fail; fix the cause |
| 5.2 Connections | Process-per-connection, `max_connections`, poolers (links to BE302) | Measure memory per connection and set a connection budget |
| 5.3 Replicas and lag | Streaming replication, replica lag, read-your-writes routing, failover consequences | Route reads to a replica and catch a read-your-writes bug in a test |
| 5.4 Backup and restore | `pg_dump` vs physical backups, WAL archiving and point-in-time recovery, restore drills | Restore to a timestamp 5 minutes before a `DELETE` without a `WHERE` |
| 5.5 Managed Postgres | RDS and Aurora, Cloud SQL, Azure Flexible Server, Neon and Supabase; what you still own | Write a one-page checklist of what a managed service does not do for you |

**Check your understanding:** (1) How can an idle-in-transaction session cause bloat in a different table? (2) Why is a backup you have never restored not a backup? (3) What can a user see if you read from a replica right after a write?

### Chapter 6 · Partitioning and large tables (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Declarative partitioning | Range, list and hash partitions; pruning; constraints and indexes on partitioned tables | Partition a 200M-row events table by month; compare plans |
| 6.2 Retention and archiving | `DROP`/`DETACH PARTITION` vs `DELETE`, `pg_partman`, archiving to object storage | Expire a month of data in milliseconds instead of hours |
| 6.3 Multi-tenant designs | Shared table with `tenant_id`, schema-per-tenant, database-per-tenant; row-level security | Enforce tenant isolation with RLS and prove a cross-tenant read fails |
| 6.4 Soft delete, audit and history | `deleted_at` traps, audit tables, temporal tables via triggers, the right-to-erasure tension | Implement audit history and a real erasure path for one user |

**Check your understanding:** (1) When does partitioning make queries slower? (2) Why is `tenant_id` usually the first column of every index in a shared-table design? (3) How do soft deletes interact with unique constraints?

### Chapter 7 · JSONB and semi-structured data (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 `jsonb` vs columns | Storage, TOAST, update cost of large documents, schema-on-read vs schema-on-write | Store product attributes both ways; compare size and query speed |
| 7.2 Indexing JSONB | GIN `jsonb_ops` vs `jsonb_path_ops`, expression indexes on extracted fields | Make a containment query use an index and explain the operator class choice |
| 7.3 SQL/JSON | `jsonb_path_query`, `JSON_TABLE` (PostgreSQL 17+), generated columns (virtual by default in 18) | Turn a JSON payload table into a relational view with `JSON_TABLE` |
| 7.4 When JSONB is a smell | Hidden schemas, untyped money, impossible constraints | Refactor a JSONB "settings" blob into columns where it matters |

**Check your understanding:** (1) Why does updating one key in a 50 KB JSONB value rewrite the whole value? (2) When is `jsonb_path_ops` the better GIN operator class? (3) Which data must never live only inside JSON?

### Chapter 8 · Schema migrations without downtime (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Which DDL locks what | Lock levels of common `ALTER TABLE` forms, fast column adds with defaults, table rewrites | Classify 15 migrations as safe, risky or rewriting |
| 8.2 Expand and contract | Add new, dual-write, backfill, switch reads, stop old writes, drop old; Stripe's four-step online migrations | Rename a column used by a live service in six safe deploys |
| 8.3 Safe building blocks | `CREATE INDEX CONCURRENTLY`, `NOT VALID` + `VALIDATE CONSTRAINT`, `lock_timeout` with retries, batched backfills with throttling | Backfill 50M rows without raising p99 by more than 20% |
| 8.4 Tools | Flyway, Liquibase (FSL licence since 5.0), Atlas, pgroll's dual-schema views, gh-ost for MySQL | Run the same migration with two tools; compare safety guarantees |
| 8.5 Change data capture | Logical replication, Debezium, using CDC to move data between stores (bridge to BE304) | Stream changes from Postgres into a search index |

**Check your understanding:** (1) Why can't you deploy "rename column" and new application code at the same moment? (2) What does `NOT VALID` buy you? (3) How do you know a backfill is hurting production before users notice?

### Chapter 9 · ORMs vs SQL (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Two ORM families | Active Record vs Data Mapper; Hibernate, SQLAlchemy 2.0, Prisma 7 (TypeScript query compiler by default), Drizzle | Implement one aggregate in two ORMs; compare generated SQL |
| 9.2 SQL-first tools | sqlc, jOOQ, Kysely; typed SQL without an object model | Port an ORM repository to sqlc or jOOQ |
| 9.3 ORM traps | N+1, lazy loading outside a transaction, accidental full loads, identity maps and stale reads | Find and fix four traps in a provided service using query logs |
| 9.4 Choosing | Team skill, query complexity, migrations ownership, testability | Write a decision record for your P3 data layer |

**Check your understanding:** (1) How do you detect N+1 queries in CI rather than in production? (2) When does an ORM's unit of work cause a lost update? (3) What should you always log in development when using an ORM?

### Chapter 10 · Redis patterns (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Data structures | Strings, hashes, lists, sets, sorted sets, streams, HyperLogLog; time complexity of each command | Build a leaderboard and a unique-visitor counter |
| 10.2 Caching | Cache-aside, write-through, TTLs and jitter, invalidation on write, stampede protection (links to BE402) | Cache a menu endpoint; prove no stale reads after an update |
| 10.3 Rate limiting and counters | Fixed window, sliding window with sorted sets, token bucket in a Lua script, atomicity | Implement a per-user token bucket and test it under concurrency |
| 10.4 Locks and their limits | `SET NX PX`, Redlock and Kleppmann's critique, fencing tokens | Show a lock-expiry race, then make it safe with a fencing token in Postgres |
| 10.5 Durability and licensing | RDB and AOF, eviction policies, replication; Redis 8 added AGPLv3 (May 2025); Valkey is the BSD-licensed Linux Foundation fork | Configure eviction for a cache vs a queue and explain the difference |

**Check your understanding:** (1) Why is a Redis lock without a fencing token unsafe for protecting a database write? (2) What happens to a cache-aside system when a hot key expires under heavy load? (3) Why must a rate limiter's read-and-increment be atomic?

### Chapter 11 · Beyond relational (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Access-pattern-first design | List queries before tables; when a relational model fights you | Write the access-pattern table for a chat app |
| 11.2 Key-value: DynamoDB | Partition and sort keys, single-table design, GSIs, hot partitions, conditional writes, transactions | Design a single-table schema for orders and riders; load-test the hot key |
| 11.3 Wide-column: Cassandra and ScyllaDB | Partitions and clustering keys, tunable consistency, tombstones, Cassandra 5.0's storage-attached indexes; Discord's message store | Model a message timeline with bucketed partitions |
| 11.4 Documents: MongoDB | Embedding vs referencing, schema validation, multi-document transactions | Model a product catalogue with variants; compare to the JSONB version |
| 11.5 Distributed SQL and others | Spanner, CockroachDB, YugabyteDB; search engines; time-series; SQLite at the edge | Write an engine decision record for three stated workloads |
| 11.6 Polyglot persistence | The cost of each extra store: consistency, backups, on-call, skills | Argue for or against adding a second store to your P3 design |

**Check your understanding:** (1) Why do DynamoDB designs start from queries while relational designs start from entities? (2) What are tombstones, and why can they make Cassandra reads slow? (3) Give a workload where PostgreSQL is the wrong primary store, and say what you would use.

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: domain model | Schema with constraints; invalid-state tests |
| 2 | 2 | Lab 2: index design | Plans before/after for 5 queries |
| 3 | 3 | Lab 3: plan clinic (no AI) | 10 diagnosed queries |
| 4 | 4 | Lab 4: anomalies | Two-session reproduction scripts; P1 due |
| 5 | 4 | Lab 5: `SKIP LOCKED` queue | Exactly-once job processing proof |
| 6 | 5 | Lab 6: restore drill | PITR to a timestamp, timed |
| 7 | 6 | Partitioning and RLS | Partition plan; tenant isolation tests |
| 8 | 7 | JSONB | Size and speed comparison; P2 starts |
| 9 | 8 | Lab 7: live migration | Migration under load with error log |
| 10 | 9 | ORM traps | Four fixes with query logs |
| 11 | 10 | Lab 8: Redis | Cache, rate limiter, fenced lock; P2 due |
| 12 | 11 | Lab 9: DynamoDB / Cassandra | Single-table design and load test; P3 design review |
| 13 | 11 | Engine decisions | Three decision records |
| 14 | — | P3 integration | P3 demo and write-up |
| 15 | Review and exam | — | Written exam and live plan-clinic exam |

## Working with AI in this course

- **Use AI for:** generating realistic synthetic data (skewed tenants, Indian names and PIN codes, bursty timestamps); drafting migrations that you then classify by lock level; explaining unfamiliar plan nodes; translating a relational model into a DynamoDB access-pattern table as a first draft; writing two-session anomaly scripts.
- **Do without AI (drills):** the Lab 3 plan clinic; deciding isolation levels and lock strategies on paper for six write paths; classifying DDL by lock level from memory; designing indexes from a query list; the live exam.
- **Verify AI output by:** running every generated query through `EXPLAIN (ANALYZE, BUFFERS)` on at least 10 million rows, not a 10-row fixture; running every migration against a copy of the table under k6 load with `lock_timeout` set and watching `pg_locks`; reproducing every claimed isolation behaviour in two sessions; turning on ORM query logging and counting queries per request.
- **Where AI still fails here (show it yourself):** text-to-SQL is not solved (see CS211, where the best BIRD system was around 83% execution accuracy in September 2026). Ask an assistant to "add a NOT NULL column with a default to a 100M-row table safely" and check whether its steps hold `ACCESS EXCLUSIVE` locks or rewrite the table. Ask it whether `REPEATABLE READ` prevents write skew in PostgreSQL, then test it. Ask for a Redis distributed lock and check for a fencing token. Ask for a DynamoDB schema and check it against your access patterns for hot partitions. Record each finding.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–9 | 30% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Written exam (modeling, isolation, lock levels, engine choice) | 20% |
| Live plan-clinic exam (no AI) | 15% |

**Mastery gate:** you pass when you can, without AI help, (a) find and fix at least four of five planted problems in a PostgreSQL database within 90 minutes: a missing composite index, a stale-statistics misestimate, an N+1 query, a lock-queue migration and a write-skew bug; (b) write and run an expand/contract migration on a 50M-row table under load with zero errors; and (c) defend the choice of primary store for a stated workload against an examiner arguing for a different one.

## Industry reality

- **OpenAI** (January 2026): one PostgreSQL primary with nearly 50 read replicas serves ChatGPT's main relational workload. New write-heavy, shardable workloads go to sharded systems such as Azure Cosmos DB. Schema changes must be lightweight and are capped at a 5-second timeout. Backfills are throttled, sometimes for over a week.
- **Notion** sharded PostgreSQL into 480 logical shards keyed by workspace ID, and **Zerodha** runs about 20 TB of PostgreSQL with monthly partitions and scheduled vacuuming (both covered in CS211).
- **Discord** moved its message store from Cassandra to ScyllaDB in 2023 after hot partitions and garbage-collection pauses. It reduced nodes from 177 to 72 and added request coalescing in a Rust data-services layer.
- **Stripe** documented a four-step dual-write pattern for moving data between stores while serving traffic (2017).
- **Licences changed under people's feet.** Redis moved to source-available licences in 2024 and added AGPLv3 with Redis 8 in May 2025. Valkey forked from Redis 7.2.4 under the Linux Foundation, and Liquibase Community moved to the Functional Source License with 5.0 (September 2025). Checking licences is part of choosing a store.

Interview questions from this course:

1. **"Design the schema for orders, items and payments in a food-delivery app."** A strong answer covers keys, money types and `timestamptz`, constraints that make invalid states impossible, indexes justified by named queries, and what you denormalize and how you keep it correct.
2. **"Two requests withdraw from the same wallet at once. How do you prevent an overdraft?"** Cover a conditional `UPDATE … WHERE balance >= amount`, or `SELECT … FOR UPDATE`, or `SERIALIZABLE` with retries. Compare their contention costs, mention a `CHECK (balance >= 0)` backstop, and say how you would test it under concurrency.
3. **"Add a NOT NULL column to a 500M-row table with zero downtime."** Cover lock levels, the fast default path, `NOT VALID` check constraints, batched backfills with throttling, `lock_timeout` with retries, and expand/contract across deploys.
4. **"Your Redis cache serves stale prices after an update. Fix it."** Cover invalidate-on-write vs TTL, the race between read-repopulate and write, versioned keys or delete-after-commit, and how you would detect staleness in production.
5. **"When would you choose DynamoDB or Cassandra over PostgreSQL?"** Cover access-pattern predictability, write scale beyond one primary, the operational model, the loss of ad hoc queries and joins, hot partitions, and the cost of a second store.

## Resources (free first)

- **PostgreSQL documentation:** [indexes](https://www.postgresql.org/docs/current/indexes.html), [EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html), [transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html), [explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html), [partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html), [JSON types and indexing](https://www.postgresql.org/docs/current/datatype-json.html), [row security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html), [continuous archiving and PITR](https://www.postgresql.org/docs/current/continuous-archiving.html).
- **Courses and guides:** [Use The Index, Luke](https://use-the-index-luke.com/) (Markus Winand, free online); CMU 15-445 for internals review (see CS211).
- **Migrations:** Stripe, [Online migrations at scale](https://stripe.com/blog/online-migrations); [pgroll](https://github.com/xataio/pgroll); [Atlas](https://atlasgo.io/); [Flyway docs](https://documentation.red-gate.com/flyway).
- **Redis and Valkey:** [Redis docs](https://redis.io/docs/latest/); [Valkey docs](https://valkey.io/docs/); Martin Kleppmann, [How to do distributed locking](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html) (2016).
- **Beyond relational:** AWS, [Best practices for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html); [Apache Cassandra docs](https://cassandra.apache.org/doc/latest/); [MongoDB data modeling](https://www.mongodb.com/docs/manual/data-modeling/); Discord, [How Discord stores trillions of messages](https://discord.com/blog/how-discord-stores-trillions-of-messages).
- **Paid, worth it:** Kleppmann and Riccomini, *Designing Data-Intensive Applications*, 2nd edition (O'Reilly, 2026); Alex DeBrie, *The DynamoDB Book*.

## Sources

All checked 12 Oct 2026.

- PostgreSQL 18 release announcement (25 Sep 2025: `uuidv7()`, virtual generated columns, skip scan, temporal constraints, async I/O): https://www.postgresql.org/about/news/postgresql-18-released-3142/ ; PostgreSQL 19 Beta 4 (24 Sep 2026): https://www.postgresql.org/about/news/postgresql-19-beta-4-3386/
- OpenAI, *Scaling PostgreSQL* (Jan 2026): https://openai.com/index/scaling-postgresql/ , as reported by VentureBeat (23 Jan 2026): https://venturebeat.com/data/how-openai-is-scaling-the-postgresql-database-to-800-million-users
- Stack Overflow Developer Survey 2025, technology (PostgreSQL 55.6% of all respondents, 58.2% of professionals): https://survey.stackoverflow.co/2025/technology
- Discord, *How Discord stores trillions of messages* (Mar 2023): https://discord.com/blog/how-discord-stores-trillions-of-messages
- Stripe, *Online migrations at scale* (2017): https://stripe.com/blog/online-migrations
- Redis 8 and AGPLv3 (Phoronix, May 2025): https://www.phoronix.com/news/Redis-8.0-Goes-AGPLv3 ; Valkey: https://valkey.io/
- Liquibase, *Liquibase Community for the future: FSL* (Sep 2025): https://www.liquibase.com/blog/liquibase-community-for-the-future-fsl
- Prisma 7 (Nov 2025; InfoQ, Jan 2026): https://www.infoq.com/news/2026/01/prisma-7-performance
- pgroll: https://github.com/xataio/pgroll
- CS211 sources for Notion, Zerodha and BIRD: [CS211 README](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md)

_Last reviewed: 2026-10_
