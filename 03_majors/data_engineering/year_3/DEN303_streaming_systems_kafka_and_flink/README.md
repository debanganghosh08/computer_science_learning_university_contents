# DEN303 · Streaming Systems: Kafka and Flink

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [DEN403](../../year_4/DEN403_data_engineering_for_ai_unstructured_data/README.md), [OV10A](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10A_payment_systems_engineering_upi_cards/README.md), [OV10B](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10B_fraud_detection_and_risk_systems/README.md), [DEN501](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md) |

Part of the [Data Engineering major](../../README.md). [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) covered logs, consumer groups and exactly-once processing in outline, and [BE304](../../../backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md) covers queues and events from a service builder's side. This course is about building data pipelines on unbounded streams: Kafka internals, Flink's event-time and state model, change data capture, and the operations that keep a stream correct for months.

## Why this course matters now

Many decisions now have to be made within seconds of an event. Uber's SIGMOD 2021 paper on its real-time data infrastructure describes petabytes of data a day and use cases such as fraud detection, customer incentives and ML prediction that must react within seconds. India's PhonePe uses Kafka as the write-ahead log in front of its payment record store (2024). The tools changed a lot recently. Apache Kafka 4.0 (March 2025) runs only on its own KRaft consensus, without ZooKeeper. Kafka 4.2 (February 2026) declared share groups, Kafka's queue semantics, production-ready. Apache Flink 2.0 (March 2025) moved operator state to remote storage with the ForSt backend, and the Flink community now ships Flink Agents, a subproject for event-driven AI agents. AI assistants write Kafka producer configuration and Flink SQL well, but they routinely mix up processing time and event time, promise "exactly-once" without saying across which boundary, and forget that a watermark stalls when one partition goes idle. Reasoning about order, time, state and failure is what this course trains.

## Learning outcomes

By the end you can:

1. **Explain** how a Kafka partition stores, replicates and serves records (segments, indexes, ISR, high watermark, leader epochs), and **choose** durability settings for a stated loss tolerance.
2. **Design** topic, key and partition layouts for a workload, and **predict** ordering, parallelism and hot-partition behaviour.
3. **Implement** producers and consumers with correct delivery semantics, and **demonstrate** duplicates and losses under injected failures before fixing them.
4. **Build** exactly-once pipelines with idempotent producers, transactions and Flink two-phase-commit sinks, and **state precisely** where the guarantee ends.
5. **Implement** event-time processing in Flink with watermarks, windows, allowed lateness, side outputs and keyed state, and **measure** correctness against a batch recomputation.
6. **Operate** stateful jobs: checkpoints, savepoints, upgrades, rescaling, backpressure and consumer lag.
7. **Capture** database changes with Debezium, explain stream-table duality, and **maintain** a correct materialised table from a changelog.
8. **Evaluate** streaming designs (Flink, Kafka Streams, Spark Structured Streaming, batch) for a use case on latency, correctness, cost and operating burden.

## Chapters and lessons

### Chapter 1 · The log and the streaming mindset (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The log as a data structure | Append-only, ordered, replayable; logs as the integration backbone (Kafka paper, NetDB 2011) | Write a 100-line file-backed log with offsets and a reader that resumes after a crash |
| 1.2 Bounded vs unbounded data | Batch as a special case of streaming; latency vs completeness vs cost (Dataflow model, VLDB 2015) | Classify 8 company use cases by the latency each really needs |
| 1.3 Time | Event time, ingestion time, processing time; clock skew and out-of-order arrival on mobile networks | Replay Wikimedia's live recent-changes stream; plot event-time vs arrival-time lag |
| 1.4 Delivery semantics | At-most-once, at-least-once, effectively-once; idempotent sinks vs transactional sinks | Show duplicates appear when a consumer crashes after writing and before committing |

**Check your understanding:** (1) Why is "real time" a requirement to question, not accept? (2) A phone records a payment at 10:59 and it reaches the server at 11:07: which hourly window should count it, and what does that cost? (3) Why is "exactly-once delivery" impossible in general, yet "exactly-once effect" achievable?

### Chapter 2 · Kafka storage and replication internals (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Topics, partitions, segments | Segment files, offset and time indexes, page cache and zero-copy reads | Inspect segment and index files with `kafka-dump-log` after producing 1M records |
| 2.2 Replication | Leaders, followers, in-sync replicas (ISR), high watermark, leader epochs, `acks`, `min.insync.replicas`, unclean leader election | Kill brokers under `acks=1` and `acks=all`; count lost acknowledged records |
| 2.3 KRaft | Controller quorum on Raft, metadata log, no ZooKeeper since Kafka 4.0 | Run a 3-controller, 3-broker cluster; kill the active controller and time the failover |
| 2.4 Retention and compaction | Time and size retention, log compaction, tombstones, `min.cleanable.dirty.ratio`; compacted topics as tables | Compact a topic of customer updates and show the latest value per key survives |
| 2.5 Tiered storage and Kafka-compatible systems | Offloading old segments to object storage (KIP-405); Kafka-protocol systems such as Redpanda and WarpStream; what "compatible" usually leaves out | Configure tiered storage on a local cluster with MinIO; read old offsets back |

**Check your understanding:** (1) Why can `acks=all` with `min.insync.replicas=1` still lose data? (2) What does a consumer see during compaction, and why might it read a key's old value? (3) Why did removing ZooKeeper simplify operations, and what must you still run?

### Chapter 3 · Producers, consumers and partitioning (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Producers | Batching, `linger.ms`, compression, idempotence, ordering with `max.in.flight.requests.per.connection`, retries and delivery timeouts | Measure throughput and p99 latency across 6 producer settings |
| 3.2 Keys and partitions | Key choice for ordering, sticky partitioning, hot keys, changing partition counts and what it breaks | Find the hot partition in a skewed merchant-ID stream; redesign the key |
| 3.3 Consumer groups | Assignment, rebalances, cooperative sticky assignment, the broker-side rebalance protocol (KIP-848), static membership | Trigger a rebalance storm; fix it with static membership and timeouts |
| 3.4 Offsets and commits | Auto vs manual commit, commit after processing, storing offsets with results | Build a consumer that writes to PostgreSQL and commits offsets in the same transaction |
| 3.5 Share groups | Queue semantics on Kafka (KIP-932, production-ready in 4.2): per-record acknowledgement, no partition ownership, when to prefer them | Process a job queue with a share group; compare with a consumer group under a slow consumer |

**Check your understanding:** (1) Why does increasing a topic's partition count break per-key ordering for existing keys? (2) When is committing offsets in your sink's transaction better than Kafka transactions? (3) What workload does a share group fit that a consumer group fits badly?

### Chapter 4 · Schemas and contracts on the wire (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Serialisation | JSON vs Avro vs Protobuf: size, speed, evolution rules | Serialise 1M payment events three ways; compare bytes and CPU |
| 4.2 Schema registries | Subjects, IDs in the message header, compatibility modes (backward, forward, full) | Make a breaking change and watch the registry reject it |
| 4.3 Evolving event schemas | Adding optional fields, renaming via aliases, event versioning, upcasting | Evolve an order event through 3 versions with old consumers still running |
| 4.4 Poison messages | Dead-letter topics, error budgets, replay after a fix; Kafka Streams dead-letter support (KIP-1034, 4.2) | Inject malformed events; route them to a DLQ and replay after a fix |

**Check your understanding:** (1) Which compatibility mode lets old consumers read new data, and which lets new consumers read old data? (2) Why is a schema registry part of the data contract (DEN401) and not just tooling? (3) What must a DLQ record carry so that a replay is safe?

### Chapter 5 · Flink fundamentals: dataflows, event time and windows (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Flink's model | JobManager, TaskManagers, slots, operator chaining, parallelism; DataStream API vs Table API and Flink SQL | Run a word count on a Kafka topic in DataStream and SQL; compare the job graphs |
| 5.2 Watermarks | Bounded out-of-orderness, per-partition watermarks, idle sources and stalled watermarks | Reproduce a stalled watermark from one idle partition; fix it with idleness detection |
| 5.3 Windows | Tumbling, sliding and session windows; triggers; window state size | Compute 1-minute, 5-minute sliding and session metrics on Wikimedia edits |
| 5.4 Lateness | Allowed lateness, side outputs for late data, retractions and updates downstream | Measure how many events miss each window at 0 s, 30 s and 5 min lateness |
| 5.5 Correctness testing | Compare streaming output with a batch recomputation over the same event-time range | Build a checker that diffs Flink results with DuckDB over the archived topic |

**Check your understanding:** (1) Why does a watermark represent a guess, and what is the cost of guessing too early or too late? (2) Session windows merge: what does that mean for state and output? (3) Your streaming totals differ from the batch totals by 0.3%: list the causes you would check.

### Chapter 6 · State, checkpoints and exactly-once (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Keyed state | Value, list and map state; state TTL; state size estimation | Keep a per-card rolling 24-hour spend; estimate state for 50M cards |
| 6.2 State backends | Heap, RocksDB (LSM, see CS211 Chapter 5), and ForSt disaggregated state in Flink 2.x | Compare checkpoint size and duration on heap vs RocksDB for the same job |
| 6.3 Checkpoints | Asynchronous barrier snapshotting (Carbone et al., 2015), aligned vs unaligned checkpoints, incremental checkpoints | Kill a TaskManager mid-run; verify results equal an uninterrupted run |
| 6.4 End-to-end exactly-once | Kafka idempotent producer and transactions (KIP-98), `read_committed`, Flink two-phase-commit sinks, idempotent upserts | Prove no duplicates in the sink across 50 random crashes |
| 6.5 Savepoints and upgrades | Operator UIDs, state schema evolution, rescaling, blue-green job upgrades | Change job logic and parallelism from a savepoint without losing state |

**Check your understanding:** (1) Why do Kafka transactions not give exactly-once effects in a database sink by themselves? (2) What breaks if you forget to set operator UIDs? (3) Why does disaggregated state make rescaling faster, and what does it cost on the read path?

### Chapter 7 · Streaming joins and enrichment (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Stream–stream joins | Interval joins, state bounds, why unbounded joins grow forever | Join payment-initiated and payment-completed events within 10 minutes |
| 7.2 Stream–table joins | Temporal joins against versioned tables, lookup joins with caching, broadcast state | Enrich orders with the merchant category valid at event time |
| 7.3 Changelog semantics | Insert, update-before, update-after and delete rows in Flink SQL; append vs upsert sinks; changelog operators (Flink 2.3) | Write an aggregation to an upsert sink and explain each changelog row |
| 7.4 Kafka Streams and Spark | KStream and KTable, Kafka Streams' broker-side rebalance protocol (GA in 4.2); Spark Structured Streaming micro-batches and Real-Time Mode (4.1) | Implement the same enrichment in Kafka Streams and compare the operating model with Flink |

**Check your understanding:** (1) Why is a lookup join to a live database not reproducible on replay, and when is that acceptable? (2) What is the difference between an append stream and an upsert stream for a downstream warehouse? (3) When would you pick Kafka Streams over Flink?

### Chapter 8 · Change data capture and stream–table duality (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Log-based CDC | Reading PostgreSQL WAL (logical decoding) and MySQL binlog; snapshots then streaming; Debezium 3.x | Stream a PostgreSQL table's changes to Kafka with Debezium; update, delete and truncate rows |
| 8.2 Correctness of CDC | Ordering per key, transaction boundaries, schema changes, replica identity, heartbeats, replication-slot growth | Show a replication slot filling the disk when the connector stops; set alerts |
| 8.3 Outbox pattern | Writing events in the same transaction as state; avoiding dual writes | Replace a dual write with an outbox and prove no lost events under crash |
| 8.4 Duality | A table is the fold of a changelog; a changelog is the diff of a table; compacted topics, KTables, materialised views, streaming databases | Rebuild a table from a compacted CDC topic and diff it with the source |
| 8.5 CDC into the lakehouse | Upserts into Iceberg or Delta, merge-on-read vs copy-on-write (preview of [DEN305](../DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md)); Flink CDC pipelines | Land CDC into an Iceberg table and query it as of two timestamps |

**Check your understanding:** (1) Why is log-based CDC safer than polling a `updated_at` column? (2) What happens downstream when someone runs `ALTER TABLE` on the source? (3) Why does the outbox pattern need idempotent consumers anyway?

### Chapter 9 · Real-time use cases (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Fraud and risk signals | Velocity features (count and sum per card or device over sliding windows), rules plus model scores, latency budgets (Uber's fraud use case, SIGMOD 2021; deeper in [OV10B](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10B_fraud_detection_and_risk_systems/README.md)) | Compute 5 velocity features on a synthetic UPI-style payment stream (illustrative) with p99 under 1 s |
| 9.2 ETA and logistics signals | Live supply and demand per zone, travel-time aggregates, late GPS pings (illustrative food-delivery scenario) | Maintain per-zone rolling delivery times from replayed NYC TLC trips |
| 9.3 Real-time features for ML and AI | Online and offline feature consistency, point-in-time correctness, freshness SLAs; streaming embeddings (preview of [DEN403](../../year_4/DEN403_data_engineering_for_ai_unstructured_data/README.md)) | Serve the same feature from stream and batch; measure skew between them |
| 9.4 Lambda, Kappa and reprocessing | Recomputing history through the stream vs a parallel batch path; backfills for streams | Reprocess 30 days of history through the same Flink job and compare with batch |

**Check your understanding:** (1) Which fraud features need exactly-once, and which tolerate at-least-once? (2) Why do online and offline features drift apart, and how do you detect it? (3) When is a 5-minute batch better than a stream?

### Chapter 10 · Operating streaming systems (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Monitoring | Consumer lag (records and time), end-to-end latency, checkpoint duration, backpressure, watermark lag | Build a dashboard with these 6 signals and alert thresholds |
| 10.2 Capacity planning | Partitions per topic, throughput per partition, broker disk and network, Flink parallelism and state size | Size a cluster for 50,000 events/s with 7-day retention |
| 10.3 Incidents | Rebalance storms, stuck consumers, poison pills, a replication slot filling disk, checkpoint timeouts | Run a game day with 3 injected failures; write the incident report |
| 10.4 Managed or self-run | Amazon MSK, Confluent Cloud, managed Flink services vs self-managed on Kubernetes; cost drivers (cross-zone traffic, retention, partitions) | Cost a 3-zone deployment two ways |

**Check your understanding:** (1) Why is lag in seconds more useful than lag in records? (2) What is the first thing you check when checkpoints start timing out? (3) Which costs do managed Kafka services often charge separately?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · A log from scratch | Crash-safe log and reader |
| 2 | 2 | Lab 2 · Losing acknowledged writes | Loss table per durability setting |
| 3 | 2 | Lab 3 · KRaft and compaction | Failover timing; **P1 due** |
| 4 | 3 | Lab 4 · Producer and consumer semantics | Transactional offset sink |
| 5 | 4 | Lab 5 · Schema evolution | Three-version evolution |
| 6 | 5 | Lab 6 · Watermarks and windows | Stalled-watermark fix |
| 7 | 5 | Lab 6 (cont.) | Mid-term (AI off): semantics and time |
| 8 | 6 | Lab 7 · Crash testing exactly-once | 50-crash report |
| 9 | 6 | Lab 8 · Savepoints and upgrades | Upgrade without state loss; **P2 due** |
| 10 | 7 | Lab 9 · Streaming joins | Temporal-join correctness check |
| 11 | 8 | Lab 10 · Debezium CDC | CDC table rebuilt and diffed |
| 12 | 9 | Lab 11 · Velocity features | Latency and correctness report |
| 13 | 9 | Lab 11 (cont.) | Reprocessing comparison |
| 14 | 10 | Game day | **P3 due**, incident report |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** drafting producer, consumer and Debezium connector configurations; writing Flink SQL and DataStream boilerplate; generating synthetic event generators with controllable lateness, skew and duplicates; explaining Kafka configuration interactions; summarising a broker log during an incident. Tools: Claude Code, GitHub Copilot, Cursor; vendor assistants in managed consoles where available.
- **Do without AI (drills):** drawing the sequence of a producer retry that causes a duplicate; computing which window an out-of-order event lands in under a given watermark; the durability-setting loss analysis in Lab 2; the mid-term and final. These are the reasoning steps you will need during an incident.
- **Verify AI output by:** (1) a batch recomputation over the archived topic that must match the streaming output; (2) crash and restart tests with injected failures (kill brokers, TaskManagers, connectors) and a duplicate and loss count; (3) checking every configuration name and default against the documentation for your exact Kafka and Flink versions; (4) asking "exactly-once between which two points?" and testing that boundary.
- **Where AI still fails here (show it yourself):** in Labs 6 and 7, ask an assistant for a "real-time hourly revenue" Flink job and a "reliable Kafka consumer". Check whether it uses processing time where event time is needed, sets no watermark idleness, commits offsets before the sink write, claims exactly-once for a non-transactional sink, or uses configuration keys from the ZooKeeper era. Keep a log of each claim, the test that refuted or confirmed it, and the fix.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–11 and game day | 25% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Mid-term (AI off): semantics and time | 10% |
| Final exam (AI off) | 20% |
| Oral defence of P3 | 10% |

**Mastery gate.** You pass when you can, without AI: (1) given a pipeline diagram and its configurations, state exactly where duplicates or losses can occur and fix each; (2) build a Flink job whose event-time results match a batch recomputation exactly after 20 random crashes; (3) diagnose two of three injected incidents (rebalance storm, stalled watermark, replication-slot growth) within 45 minutes from metrics and logs.

## Industry reality

Kafka began at LinkedIn as a log for activity data and operational metrics (NetDB 2011). Flink's checkpointing comes from the asynchronous barrier snapshot design (2015). Both are now Apache projects with frequent releases: Kafka 4.3.1 (June 2026) and 4.2.2 (September 2026), Flink 2.3.0 (June 2026), Flink CDC 3.7.0 (October 2026), and Debezium 3.7 (September 2026). Uber's published architecture uses Kafka, Flink, Pinot and Presto for real-time analytics and decisions. PhonePe uses Kafka as the write-ahead log for its payment record store. In practice, most streaming work is not exotic algorithms: it is choosing keys, handling late and duplicate data, and running stateful jobs through upgrades and failures.

**Interview questions from this course**

1. *"How does Kafka guarantee that an acknowledged write is not lost?"* A strong answer covers replication, ISR, high watermark, `acks=all` together with `min.insync.replicas`, unclean leader election, and what `fsync` does and does not do. It ends with the remaining failure modes.
2. *"Design exactly-once processing from Kafka to a database."* Cover idempotent producers and transactions, `read_committed`, the sink boundary, idempotent upserts or storing offsets in the sink transaction, and how to test with crashes.
3. *"Explain watermarks and late data."* Cover event vs processing time, bounded out-of-orderness, idle partitions, allowed lateness, side outputs, retractions downstream, and the latency vs completeness trade-off.
4. *"Design a real-time fraud feature pipeline for a payments app."* Cover keys (card, device, account), sliding-window velocity features, state size and TTL, latency budget, online and offline consistency, replay for backfill, and monitoring of feature freshness.
5. *"How would you replicate a production PostgreSQL table into the lakehouse in near real time?"* Cover log-based CDC with Debezium, initial snapshot, ordering per key, deletes and tombstones, schema changes, replication-slot monitoring, and upserts into Iceberg or Delta with compaction.

## Resources (free first)

- **Course:** [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp), streaming module (free); [Confluent Developer courses](https://developer.confluent.io/courses/) (free, vendor-written).
- **Documentation:** [Apache Kafka](https://kafka.apache.org/documentation/); [Apache Flink (stable)](https://nightlies.apache.org/flink/flink-docs-stable/); [Debezium](https://debezium.io/documentation/); [Spark Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html).
- **Reading:** Tyler Akidau, ["Streaming 101"](https://www.oreilly.com/radar/the-world-beyond-batch-streaming-101/) (free article).
- **Papers:** [Kafka: a distributed messaging system for log processing](https://notes.stephenholiday.com/Kafka.pdf) (NetDB 2011); [MillWheel](https://research.google/pubs/millwheel-fault-tolerant-stream-processing-at-internet-scale/) (VLDB 2013); [The Dataflow Model](https://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf) (VLDB 2015); [Lightweight Asynchronous Snapshots for Distributed Dataflows](https://arxiv.org/abs/1506.08603) (2015); [Real-time Data Infrastructure at Uber](https://arxiv.org/abs/2104.00087) (SIGMOD 2021).
- **Live and replayable data:** [Wikimedia EventStreams](https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams_HTTP_Service) (public server-sent events of edits); [GH Archive](https://www.gharchive.org/) hourly files replayed as a stream; [NYC TLC trips](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) replayed by event time.
- **Paid, worth it:** Akidau, Chernyak and Lax, *Streaming Systems* (O'Reilly, 2018); Kleppmann and Riccomini, *Designing Data-Intensive Applications*, 2nd ed. (O'Reilly, 2026), stream-processing chapter.

## Sources

All checked October 2026.

- Apache Kafka downloads and blog: 4.0.0 (18 Mar 2025), 4.2.0 (17 Feb 2026), 4.3.0 (22 May 2026), 4.3.1 (25 Jun 2026), 4.2.2 (29 Sep 2026). https://kafka.apache.org/community/downloads/ ; https://kafka.apache.org/blog
- Apache Kafka 4.2.0 release announcement (share groups production-ready; Streams rebalance protocol GA; KIP-1034). https://kafka.apache.org/blog/2026/02/17/apache-kafka-4.2.0-release-announcement/
- Apache Flink 2.0.0 announcement (24 Mar 2025: ForSt disaggregated state, materialised tables, removed DataSet and Scala APIs). https://flink.apache.org/2025/03/24/apache-flink-2.0.0-a-new-era-of-real-time-data-processing/
- Apache Flink posts (2.3.0 on 25 Jun 2026; Flink CDC 3.7.0 on 10 Oct 2026; Flink Agents 0.3). https://flink.apache.org/posts/
- Debezium releases (3.7.0.Final, 29 Sep 2026). https://debezium.io/releases/
- Fu and Soman, "Real-time Data Infrastructure at Uber" (SIGMOD 2021). https://arxiv.org/abs/2104.00087
- PhonePe Tech, "Demystifying TStore" (Aug 2024). https://tech.phonepe.com/demystifying-tstore-the-backbone-of-billions-of-transactions-at-phonepe/
- Apache Spark 4.1.0 release notes (Real-Time Mode). https://spark.apache.org/releases/spark-release-4.1.0.html

_Last reviewed: 2026-10_
