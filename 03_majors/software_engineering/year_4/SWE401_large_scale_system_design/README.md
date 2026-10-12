# SWE401 · Large-Scale System Design

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [SWE301](../../year_3/SWE301_software_architecture_and_design_patterns/README.md); assumes [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) and [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md); recommended [SWE305](../../year_3/SWE305_concurrency_and_performance_engineering/README.md) | [SWE501](../../year_5/SWE501_frontier_seminar_agentic_software_engineering/README.md); supports [CAR401](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) and [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

## Why this course matters now

Large-scale design is where small decisions multiply. UPI processed about 24.07 billion transactions in September 2026, an average of roughly 802 million a day (NPCI data as reported). IRCTC's public record is 28,434 train tickets booked in a single minute (12 November 2022). Slack moved 99% of its query load onto Vitess after per-workspace sharding produced hot spots and outgrew the largest hardware (2020). Discord replaced 177 Cassandra nodes with 72 ScyllaDB nodes and cut p99 message-fetch latency from 40–125 ms to about 15 ms (2023). At this scale, the hard parts are the partition key, the hot key, the retry storm, the consistency the user sees, and the region that fails. AI assistants now produce a fluent "system design answer" for any prompt, and that is the problem: the template (load balancer, Redis, Kafka, sharding) arrives without numbers, without the access pattern that decides the database, and without the failure that matters. This course teaches the method senior engineers use: requirements and estimates first, choices justified by access patterns and failure modes, designs written as documents that survive review. CS212 gave you the distributed-systems theory and SWE301 the architecture vocabulary; this course applies both to real systems at Indian and global scale.

## Learning outcomes

By the end you can:

1. **Turn** an ambiguous product request into functional requirements, SLOs, constraints and explicit non-goals.
2. **Estimate** traffic, storage, bandwidth, fleet size and cost from first principles, and **state** the assumption each number depends on.
3. **Choose** storage (relational, key-value, wide-column, document, search, object, NewSQL) from access patterns, and **defend** the choice against two alternatives.
4. **Design** partitioning, replication, caching and asynchronous processing for a target load, and **handle** hot keys, thundering herds and rebalancing.
5. **Specify** the consistency each user-facing operation needs and **implement** it with idempotency keys, sagas, outboxes and reconciliation.
6. **Design** for failure: availability arithmetic, multi-AZ and multi-region topologies, cell-based isolation, graceful degradation.
7. **Write** a design document and **run** a design review that finds real risks.
8. **Validate** a design with a prototype and a load test of its riskiest path.

## Chapters and lessons

### Chapter 1 · From request to requirements (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Clarifying scope | Users, use cases, read/write paths, non-goals; the questions that change the design | 10 clarifying questions for "design a food-delivery tracking system"; rank by impact |
| 1.2 SLOs as design inputs | Availability, latency percentiles, durability, freshness; error budgets as constraints | Write SLOs for a payment-status API with reasons for each number |
| 1.3 API and data model first | Resource APIs, idempotency, pagination; entities and access patterns table | API sketch and access-pattern table for a URL shortener |
| 1.4 Design documents | Context, goals and non-goals, design, alternatives considered, cross-cutting concerns (Google-style design docs) | Outline a design doc for the shortener |

**Check your understanding:** Which single requirement most often changes the database choice? Why should non-goals be written down? What is the difference between an SLO and a capacity target?

### Chapter 2 · Back-of-the-envelope estimation (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Latency numbers | Memory, SSD, network within a zone, across regions; why they matter for chatty designs | Recite and use Jeff Dean's latency table; update it with today's hardware |
| 2.2 Traffic | Daily volume → average QPS → peak QPS (peak factors from evidence, not habit) | From 24.07 billion UPI transactions in a 30-day month, compute average TPS (≈ 9,300); argue a peak factor |
| 2.3 Storage and bandwidth | Record sizes, replication factor, indexes, retention, growth | 5-year storage for a messaging app under stated assumptions |
| 2.4 Fleet and cost | Per-node throughput from benchmarks, headroom, N+2; cloud cost per month | Size a fleet for the shortener at 50,000 redirects/s; price it |
| 2.5 Sanity checks | Order-of-magnitude checks; comparing with published numbers (Slack's 2.3M queries/s peak on Vitess) | Find the error in 3 flawed estimates |

**Check your understanding:** Why is "peak = 2× average" a dangerous default for ticket openings or festival sales? Which estimate most often turns out wrong by 10×, and why? How do you estimate per-node throughput without a benchmark?

### Chapter 3 · Choosing storage (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Relational at scale | Postgres/MySQL limits, read replicas, Vitess sharding (Slack) | Decide when a single Postgres primary is enough for a startup; show the numbers |
| 3.2 Key-value and wide-column | Dynamo-style systems (DynamoDB), Cassandra and ScyllaDB (Discord); partition and clustering keys | Model Discord-style channel messages with a bucketed partition key |
| 3.3 Document, search and time-series | MongoDB, Elasticsearch/OpenSearch, time-series stores; when search is a secondary index | Decide where product search lives for a marketplace |
| 3.4 Object storage and data lakes | S3-style storage, lifecycle tiers, immutable logs | Design media storage for a chat app with CDN delivery |
| 3.5 NewSQL | Spanner (TrueTime), CockroachDB, TiDB, YugabyteDB: global transactions and their latency cost | Compare a cross-region transaction's latency in NewSQL vs a single-region primary |

**Check your understanding:** Why does a wide-column store force you to design tables per query? When is distributed SQL worth its write latency? What made Slack's per-workspace sharding fail for its largest customers?

### Chapter 4 · Partitioning and replication in practice (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Shard keys | Even distribution vs locality; compound keys; tenant-based sharding | Choose shard keys for orders, messages and payments; justify each |
| 4.2 Hot keys | Celebrity users, popular trains, viral links; key splitting, request coalescing (Discord's Rust data services), caching | Simulate a hot key; apply two mitigations; compare |
| 4.3 Rebalancing | Consistent hashing, virtual nodes, range splits; moving data online | Simulate adding 2 nodes to 10 with and without virtual nodes |
| 4.4 Secondary indexes | Local vs global indexes; scatter-gather cost | Estimate the cost of "find all orders for a restaurant" under each design |
| 4.5 Replication choices | Leader–follower, multi-leader, leaderless quorums; read-your-writes in practice | Pick a replication model for a profile service vs a ledger |

**Check your understanding:** Why does a perfectly uniform hash make range queries expensive? How does request coalescing protect a database from a hot partition? When is a global secondary index worth its write cost?

### Chapter 5 · Caching (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Patterns | Cache-aside, read-through, write-through, write-behind; what each risks | Pick a pattern for 4 data types (prices, sessions, feeds, balances) |
| 5.2 Invalidation | TTLs with jitter, delete-on-write, versioned keys; stale-set races | Reproduce a stale-set race; fix it with leases (Memcache at Facebook) |
| 5.3 Thundering herds | Request coalescing, early refresh, negative caching | Cold-start a cache under load with and without coalescing |
| 5.4 CDN and edge | Static vs dynamic content, cache keys, purge | Design caching for a cricket-score page during a final |

**Check your understanding:** Why should account balances almost never be cache-aside? What problem do Memcache leases solve? Why does adding TTL jitter matter at scale?

### Chapter 6 · Queues, streams and workflows (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Logs and partitions | Kafka-style partitioned logs; ordering per key; consumer groups and lag | Partition an order-events topic so per-order ordering holds |
| 6.2 Delivery semantics | At-most/at-least-once; "exactly-once" as idempotent effects | Show a duplicate effect; make the consumer idempotent |
| 6.3 Delayed and scheduled work | Delay queues, timers at scale, outbox | Seat-hold expiry for 10 million holds per hour |
| 6.4 Durable workflows | Workflow engines (Temporal) for multi-step processes with retries | Model a refund as a durable workflow; kill the worker mid-run |

Mechanics of brokers and stream processors are in [BE304](../../../backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md).

**Check your understanding:** Why does ordering only exist per partition? What is the real meaning of "exactly once" in a payment flow? When is a workflow engine better than a queue plus cron jobs?

### Chapter 7 · Search, feeds and location (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Inverted indexes | Indexing pipelines, near-real-time refresh, relevance basics | Index 1 million product titles; measure query latency |
| 7.2 Typeahead | Prefix tries, top-k per prefix, freshness | Design autocomplete for railway station names in 12 Indian languages |
| 7.3 Feeds | Fan-out on write vs on read; hybrid for high-follower accounts | Estimate write amplification for both strategies |
| 7.4 Geospatial | Geohash, S2 cells, Uber's H3 hexagons; nearby search | Find nearby delivery partners with H3; compare with a naive scan |

**Check your understanding:** Why do feed systems treat high-follower accounts differently? What does a hexagonal grid fix compared with square cells? When should search be eventually consistent with the source of truth?

### Chapter 8 · Correctness at scale: consistency, idempotency, money (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Consistency in product terms | Which screens need linearisable reads; read-your-writes; monotonic reads | Annotate every read in a booking flow with the consistency it needs |
| 8.2 Idempotency keys | Client-generated keys, stored results, expiry (Stripe's public design) | Implement idempotent payment creation; replay 1,000 duplicate requests |
| 8.3 Sagas and reconciliation | Compensation; outbox; daily and real-time reconciliation against a ledger | Design reconciliation between your ledger and a bank's settlement file |
| 8.4 Time and ordering | Clock skew, hybrid logical clocks, Spanner's TrueTime idea | Show an ordering bug from clock skew; fix with logical ordering |

**Check your understanding:** Why is reconciliation a design component and not an operations afterthought? What breaks if idempotency keys expire too early? Which user-facing reads in a payment app can be stale, and for how long?

### Chapter 9 · Case studies I: the classics, done properly (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 URL shortener | ID generation (counters, Snowflake-style, hashing), redirects at scale, analytics pipeline | Full design doc with estimates |
| 9.2 Distributed rate limiter | Per-key limits across a fleet; Redis Lua scripts vs local approximations | Compare accuracy and latency of central vs local+sync limiters |
| 9.3 Notification system | Channels, templates, preferences, retries, provider failover, deduplication | Design for 50 million notifications in 10 minutes (illustrative) |
| 9.4 Review practice | Peer design reviews with a checklist | Review two classmates' designs |

**Check your understanding:** Why do sequential short IDs leak business information? Which rate-limiter design would you choose for a login endpoint, and why? How do you stop a notification system from sending the same OTP twice?

### Chapter 10 · Case studies II: Indian and global scale (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Messaging at WhatsApp scale (illustrative numbers) | Persistent connections, presence, delivery and read receipts, offline queues, group fan-out, media via object storage, end-to-end encryption (Signal Protocol) constraining server design | Full design for 500 million daily users under stated assumptions |
| 10.2 Tatkal-style surge booking | Burst admission (virtual waiting rooms, token buckets), inventory per train/class/date, holds with TTL, bot defence, fairness; IRCTC's public 28,434-tickets-per-minute record as the scale anchor | Design for 10× the record; internal IRCTC details are not public, so label assumptions |
| 10.3 UPI-scale payments | Hub-and-spoke switch between payer and payee banks, idempotent request IDs, timeouts and status-check flows, reversals, reconciliation; ≈ 802 million transactions/day average in Sept 2026 | Design a payment-service-provider backend for 5% of UPI volume; specify failure handling for a timed-out debit |
| 10.4 Chat history storage (Discord, 2023) | Bucketed partitions, hot channels, request coalescing, migration between databases | Reproduce the data model and the coalescing idea at small scale |

**Check your understanding:** What is the hardest consistency problem in a timed-out UPI debit, and who resolves it? Why is fairness a design requirement in Tatkal booking, not only a policy? What does end-to-end encryption remove from a messaging server's options?

### Chapter 11 · Failure, regions and cost (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Availability arithmetic | Serial vs parallel dependencies; nines and minutes; correlated failures | Compute availability of a design; find the weakest link |
| 11.2 Multi-AZ and multi-region | Active–passive, active–active, data residency (RBI's 2018 directive on storing payment system data in India) | Choose a topology for an Indian payment app; justify RPO and RTO |
| 11.3 Cells and blast radius | Cell-based architecture; shuffle sharding; the AWS us-east-1 event of 19–20 Oct 2025 (a DNS automation race left DynamoDB's regional endpoint empty) | Redesign the shortener into cells; compute blast radius |
| 11.4 Cost as a requirement | Unit economics per request; storage tiers; egress | Cost per 1,000 payments for your Chapter 10 design |

**Check your understanding:** Why does adding a dependency usually lower availability even if it is "highly available"? What does a cell boundary protect you from that multi-AZ does not? When does data residency force a design choice?

### Chapter 12 · Design reviews and validation (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Writing for reviewers | One-page summary, diagrams, alternatives, risks, rollout plan | Final P3 design doc |
| 12.2 Running a review | Roles, pre-reading, pre-mortems, decision records | Chair a review of another team's design |
| 12.3 Prototype the riskiest path | Spikes and load tests on the part most likely to fail | Load-test your design's hot path at target scale on a small fleet |
| 12.4 AI as reviewer and adversary | Ask models for failure modes and missing requirements; verify each | Compare AI-found and panel-found risks for your design |

**Check your understanding:** What makes a design review produce decisions instead of opinions? Which part of your design did the load test prove wrong? Which AI-suggested risks were real, and how did you check?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Requirements and SLOs | — |
| 2 | 2 | Lab 2 · Estimation drills | — |
| 3 | 3 | Lab 3 · Same data, three databases | **P1 due** |
| 4 | 4 | Lab 4 · Hot keys and rebalancing | — |
| 5 | 5 | Lab 5 · Cache races and herds | — |
| 6 | 6 | Lab 6 · Idempotent consumers and delayed jobs | — |
| 7 | 7 | Lab 7 · Search and geospatial | Mid-term (AI off): 60-minute design + estimates |
| 8 | 8 | Lab 8 · Idempotency and reconciliation | — |
| 9 | 9 | Design review practice | — |
| 10 | 10 | Lab 9 · Surge admission | — |
| 11 | 10 | Lab 9 (cont.) | **P2 due** |
| 12 | 11 | Lab 10 · Failure and cells | — |
| 13 | 12 | P3 prototype and load test | — |
| 14 | 12 | P3 design review panel | **P3 due** |
| 15 | Review | Mock HLD interviews | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** brainstorming clarifying questions and failure modes; checking your arithmetic; generating load-test scripts and synthetic data; summarising papers and engineering blogs (then reading the parts that matter); acting as a hostile reviewer of your design doc.
- **Do without AI (drills):** estimates; the access-pattern table; the first draft of every design; timed 45–60-minute design sessions; the mid-term and final. Interviews and real design reviews test your own reasoning in real time.
- **Verify AI output by:** recomputing every number; checking every product limit (partition throughput, message size, connection limits) in the vendor's official documentation; prototyping and load-testing the riskiest path; asking "what access pattern justifies this component?" for every box.
- **Where AI still fails here (show it):** in Lab 2 and in the Chapter 9 review practice you give the same prompt to two assistants and grade the answers against a rubric. Record where they (a) skip estimates or make arithmetic errors, (b) add components with no access pattern that needs them, (c) claim exactly-once delivery without idempotent effects, or (d) ignore a stated constraint such as data residency. Keep the graded answers as evidence.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| P1, P2, P3 | 10%, 15%, 25% |
| Mid-term (AI off) | 10% |
| Final exam (AI off): two timed designs + oral | 20% |

**Mastery gate.** You pass when you can: (1) with AI off, design a system you have not seen in 60 minutes with requirements, estimates within an order of magnitude of the reference, justified storage and partitioning, explicit consistency per operation, and three failure scenarios with mitigations; (2) write a design document that a panel of two senior reviewers approves after at most one revision; (3) show a load test of your design's riskiest path that meets its stated SLO at target per-node throughput.

## Industry reality

Where this is used (public sources): Slack's Vitess migration and its 2.3 million queries per second peak (2020); Discord's message storage migration (2023); Facebook's "Scaling Memcache" (NSDI 2013) and TAO (USENIX ATC 2013); Amazon's Dynamo paper (SOSP 2007); Google's Spanner (OSDI 2012); Stripe's public explanation of idempotency keys; AWS's guidance on cell-based architecture. UPI and IRCTC volumes are published by NPCI and IRCTC; their internal designs are not, so every design of them in this course is labelled illustrative.

**Interview questions from this course**

1. *Design a URL shortener for 100 million new links a month.* Strong answer: clarifies read/write ratio and analytics; estimates QPS and storage; ID scheme with trade-offs; key-value storage; caching for hot links; analytics via async pipeline; abuse handling; failure modes.
2. *Design WhatsApp-style 1:1 and group messaging.* Strong answer: persistent connections and gateway layer, message IDs and ordering per conversation, delivery/read receipts, offline storage and push, group fan-out limits, media via object storage, what end-to-end encryption implies for the server.
3. *Design ticket booking for a train-ticket surge at 10:00 sharp.* Strong answer: admission control (waiting room, rate limiting), inventory partitioned per train/class/date, holds with TTL, idempotent payment confirmation, fairness and bot defence, degraded modes, load-test plan.
4. *Design the backend of a UPI payment app.* Strong answer: idempotent transaction IDs, state machine with pending/timeout states, status-check and reversal handling, ledger and reconciliation, notification, data residency, SLOs; separates what is public (NPCI flows) from assumptions.
5. *Your system's database is at 80% CPU and growth is 10% a month. What do you do?* Strong answer: measures first (query profile, hot partitions), quick wins (indexes, caching, read replicas), then vertical scaling vs sharding with a shard-key analysis; timeline from the growth rate; migration plan with dual writes or a proxy layer like Vitess.

## Resources (free first)

- **Courses and primers:** MIT 6.5840 Distributed Systems — https://pdos.csail.mit.edu/6.824/ ; The System Design Primer — https://github.com/donnemartin/system-design-primer ; AWS Builders' Library — https://aws.amazon.com/builders-library/
- **Design docs:** Malte Ubl, "Design Docs at Google" — https://www.industrialempathy.com/posts/design-docs-at-google/
- **Papers:** Dynamo (SOSP 2007) — https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf ; Scaling Memcache at Facebook (NSDI 2013) — https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala ; TAO (ATC 2013) — https://www.usenix.org/conference/atc13/technical-sessions/presentation/bronson ; Spanner (OSDI 2012) — https://research.google/pubs/spanner-googles-globally-distributed-database-2/ ; The Tail at Scale — https://research.google/pubs/the-tail-at-scale/
- **Engineering blogs:** Discord, "How Discord Stores Trillions of Messages" — https://discord.com/blog/how-discord-stores-trillions-of-messages ; Slack, "Scaling Datastores at Slack with Vitess" — https://slack.engineering/scaling-datastores-at-slack-with-vitess/ ; Stripe, "Designing robust and predictable APIs with idempotency" — https://stripe.com/blog/idempotency ; Uber H3 — https://h3geo.org/ ; Signal Protocol specifications (used by WhatsApp for end-to-end encryption) — https://signal.org/docs/
- **Indian systems (public facts):** NPCI UPI statistics — https://www.npci.org.in/what-we-do/upi/product-statistics ; IRCTC internet ticketing — https://www.irctc.com/internet-ticketing.php
- **Paid, optional:** Kleppmann, *Designing Data-Intensive Applications*; Petrov, *Database Internals*; Xu, *System Design Interview* (vols. 1–2) for interview practice only.

## Sources

- UPI September 2026 volume (24.07 billion; 802 million/day average), reported from NPCI data — https://www.outlookmoney.com/banking/upi-processes-2407-billion-transactions-worth-rs-2937-lakh-crore-in-september (checked 2026-10)
- IRCTC, Internet Ticketing (28,434 tickets per minute, 12 Nov 2022) — https://www.irctc.com/internet-ticketing.php (checked 2026-10)
- Slack Engineering, "Scaling Datastores at Slack with Vitess" (1 Dec 2020) — https://slack.engineering/scaling-datastores-at-slack-with-vitess/ (checked 2026-10)
- Discord, "How Discord Stores Trillions of Messages" (Mar 2023) — https://discord.com/blog/how-discord-stores-trillions-of-messages (checked 2026-10)
- AWS, post-event summary of the 19–20 Oct 2025 us-east-1 disruption — https://aws.amazon.com/message/101925/ (checked 2026-10)
- Reserve Bank of India, "Storage of Payment System Data" (6 Apr 2018) — https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244 (checked 2026-10)
- AWS Well-Architected, "Reducing the Scope of Impact with Cell-Based Architecture" — https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.html (checked 2026-10)

_Last reviewed: 2026-10_
