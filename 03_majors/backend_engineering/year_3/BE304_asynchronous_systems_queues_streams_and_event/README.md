# BE304 · Asynchronous Systems: Queues, Streams and Event-Driven Architecture

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [BE404](../../year_4/BE404_microservices_service_mesh_and_platform_apis/README.md), [BE401](../../year_4/BE401_payments_grade_systems_transactions_idempotency/README.md), [OV02](../../../../04_overlaps/OV02_cloud_native_backend/README.md), [DEN303](../../../data_engineering/year_3/DEN303_streaming_systems_kafka_and_flink/README.md) |

Part of the [Backend Engineering major](../../README.md). Builds on replication, logs and failure models from [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) and on transactions from [BE303](../BE303_data_modeling_and_storage_for_backends_postgres/README.md). Data engineers go deeper into stream processing in [DEN303](../../../data_engineering/year_3/DEN303_streaming_systems_kafka_and_flink/README.md); this course is about the application side.

## Why this course matters now

Most real backends do their important work after the HTTP response has been sent: payment confirmations, notifications, search indexing, fraud scoring, settlement files, AI jobs that run for minutes. That work runs on queues and logs, and those tools changed quickly. Apache Kafka 4.0 (March 2025) removed ZooKeeper entirely and made a new consumer rebalance protocol generally available. Kafka 4.2 (2026) declared "Queues for Kafka" (share groups) production-ready, so one system now offers both log and queue semantics. RabbitMQ 4.0 removed classic mirrored queues in favour of Raft-based quorum queues. Amazon SQS raised its maximum message size to 1 MiB and added fair queues. AI assistants write a producer and a consumer in seconds. They do not decide what happens when the database commit succeeds and the publish fails, when a poison message blocks a partition, or when a consumer rebalances mid-batch. Lost, duplicated or out-of-order messages cause most async incidents, and finding them takes a person who can reason about delivery semantics.

## Learning outcomes

By the end you can:

1. **Decide** when work should be synchronous, queued or event-driven, and **quantify** the availability and latency effects of each choice.
2. **Explain** the difference between a queue (competing consumers, acknowledgement, redelivery) and a log (offsets, replay, retention), and **choose** between RabbitMQ, SQS, Kafka, NATS JetStream and a Postgres-backed queue for a stated workload.
3. **Configure** Kafka for durability (replication factor, `acks=all`, `min.insync.replicas`) and **explain** partitions, consumer groups, rebalancing, compaction and transactions.
4. **Build** consumers that are correct under at-least-once delivery using idempotent writes, deduplication and ordering keys.
5. **Implement** the transactional outbox with polling and with change data capture (Debezium), and **prove** that no event is lost or invented under crashes.
6. **Design** sagas with compensations, using orchestration or choreography, and **test** every failure path.
7. **Apply** event sourcing and CQRS where they fit, and **evolve** event schemas safely with a schema registry.
8. **Operate** retries, dead-letter queues, replay tools and lag-based autoscaling, and **keep** a system stable under backpressure.
9. **Trace** a request across asynchronous hops, and **review** AI-generated messaging code for lost-message and duplicate-effect bugs.

## Chapters and lessons

### Chapter 1 · Why asynchronous (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The cost of synchronous chains | Availability multiplies (five 99.9% services in a chain ≈ 99.5%), latency adds, failures cascade | Compute availability and p99 for a 5-hop synchronous checkout, then for an async version |
| 1.2 What async buys and costs | Load levelling, decoupled deploys, retries off the user path; eventual consistency, harder debugging, new failure modes | List what the user sees at each step of an async order flow |
| 1.3 Commands, events, jobs and streams | "Do this" vs "this happened"; one consumer vs many; bounded jobs vs unbounded streams | Classify 15 messages from a food-delivery system |
| 1.4 When not to go async | Read paths, strong consistency needs, tiny systems, "distributed monolith over a broker" | Argue against an over-engineered event design in a design review |

**Check your understanding:** (1) Why does putting a queue between two services not remove the dependency between them? (2) Which user-facing promises become harder once work is asynchronous? (3) Is "order placed" a command or an event, and who should be allowed to publish it?

### Chapter 2 · Queues and logs (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Queue semantics | Competing consumers, acknowledgement, redelivery, visibility timeouts, per-message state in the broker | Simulate a consumer crash and observe redelivery in RabbitMQ and SQS |
| 2.2 Log semantics | Append-only partitions, offsets owned by consumers, retention, replay; Jay Kreps' 2013 essay *The Log* on logs as the unifying abstraction | Replay a day of events into a new consumer from offset zero |
| 2.3 Ordering | Total order per partition only, partition keys, the parallelism–ordering trade-off | Pick partition keys for orders, riders and payments; show what breaks with the wrong key |
| 2.4 Converging models | Kafka share groups (KIP-932), RabbitMQ streams, NATS JetStream | Fill a feature matrix of five systems from their docs, then test two claims |

**Check your understanding:** (1) Why can a log replay history but a classic queue cannot? (2) Why does Kafka guarantee order only within a partition? (3) What do share groups give up compared with consumer groups?

### Chapter 3 · Brokers and job queues in practice (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 RabbitMQ | Exchanges, bindings, routing keys, prefetch and manual acks; quorum queues (Raft), streams; classic mirroring removed in 4.0 | Route events by type with a topic exchange; tune prefetch for throughput vs fairness |
| 3.2 Amazon SQS | Standard vs FIFO queues, message group IDs, the 5-minute deduplication interval, visibility timeout (default 30 s, max 12 h), retention up to 14 days, 1 MiB messages, fair queues, long polling | Process an SQS FIFO queue in parallel by message group without breaking per-group order |
| 3.3 Postgres as a queue | `SELECT … FOR UPDATE SKIP LOCKED`, River and pgmq, transactional enqueue, when it stops scaling | Enqueue a job in the same transaction as a business write |
| 3.4 Job frameworks | Celery, Sidekiq, BullMQ; scheduled and recurring jobs; uniqueness; job timeouts | Build a nightly report job that cannot run twice concurrently |
| 3.5 Deadline-bound batches | Fan-out work with a hard deadline, worker pools, progress tracking. Example: Zerodha reported emailing 1.5 million contract notes in under 25 minutes after a backend revamp (Feb 2024) | Generate and send 100,000 PDFs within a deadline on a laptop (P1) |

**Check your understanding:** (1) What happens in SQS if processing takes longer than the visibility timeout? (2) Why is a transactional enqueue in Postgres attractive, and what limits it? (3) How does prefetch affect fairness between fast and slow consumers?

### Chapter 4 · Kafka internals (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Topics, partitions and replicas | Leaders, followers, in-sync replicas, `acks`, `min.insync.replicas`, unclean leader election | Kill brokers during writes with `acks=1` and `acks=all`; count lost messages |
| 4.2 KRaft | The metadata quorum that replaced ZooKeeper (Kafka 4.0), controllers, leader epochs | Run a 3-controller KRaft cluster locally and fail a controller |
| 4.3 Storage | Segments, indexes, retention by time and size, log compaction and tombstones, tiered storage | Compact a "latest price per item" topic and verify what survives |
| 4.4 Consumer groups | Partition assignment, the KIP-848 rebalance protocol (default from 4.0), offset commits, rebalance storms | Measure pause time during rebalances with the classic and the new protocol |
| 4.5 Idempotent producers and transactions | Producer IDs and sequence numbers, transactional writes across partitions, `read_committed`, consume-transform-produce | Build an exactly-once pipeline from topic A to topic B; break it by writing to a database |
| 4.6 Share groups | Queue-style consumption with per-record acknowledgement (production-ready in 4.2), when to prefer them | Process slow, independent jobs with a share group; compare with a consumer group |

**Check your understanding:** (1) With `acks=all` and `min.insync.replicas=2` on a 3-replica topic, what happens when two brokers fail? (2) Why does Kafka's exactly-once guarantee stop at the boundary of Kafka? (3) What causes a rebalance storm, and how do you stop one?

### Chapter 5 · Delivery semantics and idempotent consumers (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 At-most, at-least, exactly once | Where acks and commits happen relative to side effects; why "exactly once" means exactly-once effects | Place the commit in three positions and show loss or duplication for each |
| 5.2 Idempotent consumers | Natural idempotency (upserts, conditional writes), processed-message tables, deduplication windows | Make an email-sending consumer safe under redelivery |
| 5.3 Ordering in practice | Version numbers, last-writer-wins and its traps, handling out-of-order events | Apply shuffled order events and still reach the correct final state |
| 5.4 Poison messages | Messages that always fail, blocking partitions, skip-and-park strategies | Unblock a partition stuck on one bad message without losing it |

**Check your understanding:** (1) Why is committing the offset before processing "at most once"? (2) What makes a deduplication table itself a consistency problem? (3) Why does a single poison message hurt a log more than a queue?

### Chapter 6 · The dual-write problem and the outbox (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Dual writes fail | Commit-then-publish and publish-then-commit both lose or invent events under crashes | Crash a naive service 100 times; count lost and phantom events |
| 6.2 Transactional outbox | Write the event row in the same transaction; relay by polling; ordering and cleanup | Implement a polling relay with `SKIP LOCKED` |
| 6.3 Outbox with CDC | Debezium's outbox event router (`aggregatetype` → topic, `aggregateid` → key), logical replication slots and their risks | Run Debezium and prove zero loss across database and connector restarts |
| 6.4 The inbox pattern | Recording consumed message IDs in the consumer's transaction; exactly-once effects end to end | Combine outbox and inbox between two services and prove it with crash tests |

**Check your understanding:** (1) Why can't you "just retry the publish" after a commit? (2) What happens to a Postgres primary if a CDC replication slot stops being consumed? (3) Why does the outbox key choice decide ordering downstream?

### Chapter 7 · Sagas and long-running workflows (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Why not distributed transactions | Two-phase commit's blocking and availability cost (CS212); sagas as a sequence of local transactions (Garcia-Molina and Salem, 1987) | Rewrite a 2PC booking flow as a saga |
| 7.2 Orchestration vs choreography | Central coordinator vs event chains; visibility, coupling and debugging | Implement one saga both ways; compare what you can observe |
| 7.3 Compensations | Semantic undo, pivot transactions, retriable steps, compensations that themselves fail | Design compensations for hotel, train seat and payment steps |
| 7.4 Timeouts and human steps | Waiting days for an event, timers, manual intervention queues; why durable execution engines exist (Temporal, Restate; see BE501) | Add a 24-hour payment timeout to the saga |

**Check your understanding:** (1) Why can't every step be compensated, and what do you do about it? (2) When does choreography become impossible to reason about? (3) What isolation anomalies can other users see in the middle of a saga?

### Chapter 8 · Event sourcing and CQRS (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Events as the source of truth | Aggregates, event streams, optimistic concurrency on stream versions, rebuilding state | Event-source a wallet with deposits, holds and captures |
| 8.2 Projections and read models | CQRS, projection lag, rebuilding projections, snapshots | Rebuild a read model from 10M events; time it |
| 8.3 Event schema evolution | Upcasting, weak schemas, versioned event types, never editing history | Change an event's shape without breaking old streams |
| 8.4 When not to | Cost, complexity, GDPR-style erasure and the DPDP Act vs immutable logs, crypto-shredding | Write a decision record for and against event sourcing for one domain |

**Check your understanding:** (1) Why do event-sourced systems still need snapshots? (2) How do you delete a user's personal data from an immutable event log? (3) What does CQRS give you without event sourcing?

### Chapter 9 · Retries, dead letters and replay (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Retry strategies | Immediate vs delayed retries, exponential backoff with jitter, retry budgets | Show a retry storm, then fix it with jitter and budgets |
| 9.2 Retry topics and DLQs | Uber's ladder of retry topics and DLQ (2018); SQS redrive; RabbitMQ quorum-queue delivery limits | Build a three-level retry ladder with a DLQ |
| 9.3 Triage and replay | DLQ dashboards, classifying failures, safe replay with idempotency, bulk redrive | Fix a bug, then replay 50,000 dead-lettered messages safely |
| 9.4 Alerting | DLQ depth and age, oldest-message age, error-rate by message type | Write three alerts that would page someone for the right reason |

**Check your understanding:** (1) Why can retrying a message immediately make an outage worse? (2) What must be true before replaying a DLQ? (3) Which is the better alert: DLQ depth or oldest message age?

### Chapter 10 · Backpressure and flow control (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Lag as the key metric | Consumer lag in messages and in time, Little's law for consumer count | Size a consumer fleet for a target lag from measured processing time |
| 10.2 Scaling consumers | Partition count as the parallelism ceiling, autoscaling on lag (KEDA), rebalance costs | Autoscale consumers on lag in kind and measure recovery time |
| 10.3 Protecting fragile downstreams | Rate-limited consumers, concurrency caps, circuit breakers in consumers, pausing partitions | Keep a slow partner API within its rate limit during a backlog |
| 10.4 Producer-side backpressure | Bounded buffers, blocking vs dropping, load shedding at ingestion | Choose block, drop or spill for three producer types and justify each |

**Check your understanding:** (1) Why can't you scale Kafka consumers beyond the partition count, and what changes with share groups? (2) Lag is rising but CPU is low: what are three likely causes? (3) When is dropping messages the right choice?

### Chapter 11 · Event contracts and observability (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Schemas and registries | Avro, Protobuf and JSON Schema; compatibility modes (backward, forward, full); schema registries | Make a breaking change fail in CI before it reaches the topic |
| 11.2 Envelopes and catalogues | CloudEvents attributes, AsyncAPI documents, event ownership, an event catalogue | Document every event in your P3 with owners and consumers |
| 11.3 Tracing async flows | Context propagation in message headers, span links, end-to-end latency from produce to effect | Trace an order from API call to notification across three hops |
| 11.4 Testing async systems | Testcontainers for Kafka and RabbitMQ, contract tests for events, crash and partition injection | Write a test that kills a consumer mid-batch and checks invariants |
| 11.5 Choosing a messaging stack | Throughput, ordering, replay, operations, managed offerings, cost | Write the messaging decision record for P3 |

**Check your understanding:** (1) Why is "backward compatible" the usual default for event schemas, and what does it allow? (2) How do you measure the latency of something that happens asynchronously? (3) Which async behaviours can unit tests never catch?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Availability arithmetic | Sync vs async design note |
| 2 | 2 | Lab 1: queues vs logs | Redelivery and replay demonstrations |
| 3 | 3 | Lab 2: RabbitMQ, SQS and Postgres queues | Ordered FIFO processing; transactional enqueue |
| 4 | 4 | Lab 3: Kafka durability | Loss counts by `acks` setting; P1 due |
| 5 | 4 | Lab 3 (cont.): rebalances and transactions | Rebalance pause measurements |
| 6 | 5 | Lab 4: idempotent consumers (no AI) | Crash-test report |
| 7 | 6 | Lab 5: outbox and CDC | Zero-loss proof across restarts; P2 starts |
| 8 | 7 | Lab 6: saga | Failure-path test matrix |
| 9 | 8 | Event sourcing | Projection rebuild timing |
| 10 | 9 | Lab 7: retry ladder and DLQ | Replay of 50,000 messages; P2 due |
| 11 | 10 | Lab 8: lag autoscaling | Recovery-time plot |
| 12 | 11 | Lab 9: schemas and tracing | CI schema gate; end-to-end trace; P3 design review |
| 13 | 11 | Async testing | Chaos test suite |
| 14 | — | P3 integration | P3 demo and write-up |
| 15 | Review and exam | — | Written exam and live failure-analysis exam |

## Working with AI in this course

- **Use AI for:** boilerplate producers, consumers and Testcontainers setups; explaining broker configuration options; generating load and chaos scripts; drafting AsyncAPI documents and schema definitions; summarizing long consumer logs during debugging.
- **Do without AI (drills):** placing acks and commits relative to side effects and naming the resulting guarantee; designing compensations; choosing partition keys; the idempotent-consumer lab; the live failure-analysis exam, where you explain what a broken system did from its logs and metrics.
- **Verify AI output by:** crash testing: kill producers, consumers, brokers and the database at random points 100+ times and check invariants (no lost events, no duplicate effects, per-key order preserved). Read the broker docs for every configuration value the assistant chose. Check that every consumer is idempotent by replaying its input twice.
- **Where AI still fails here (show it yourself):** ask an assistant for "a service that saves an order and publishes an event to Kafka" and check whether it writes to the database and then publishes with no outbox. Ask for "exactly-once processing from Kafka into Postgres" and check whether it relies on Kafka transactions, which do not cover the database. Ask for an SQS consumer and check the visibility timeout against the processing time. Run each one under your crash harness and record the lost or duplicated events.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–9 | 30% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Written exam (semantics, Kafka internals, sagas, outbox) | 20% |
| Live failure-analysis exam (no AI) | 15% |

**Mastery gate:** you pass when you can, without AI help, (a) look at a consumer's code and broker configuration and state its exact delivery guarantee, then find the line that would lose or duplicate a message; (b) implement a transactional outbox and an idempotent consumer that survive 200 random crash points with zero lost and zero duplicated effects; and (c) explain, from logs and lag graphs alone, why a provided system fell 2 hours behind and what you would change.

## Industry reality

- **Apache Kafka 4.0** (18 March 2025) was the first release without ZooKeeper, and made the KIP-848 rebalance protocol generally available. **Kafka 4.2** declared share groups production-ready, and **Kafka 4.3** shipped on 22 May 2026.
- **RabbitMQ 4.0** removed classic queue mirroring after years of deprecation; replicated data now uses quorum queues or streams. RabbitMQ 4.3 (April 2026) is the current series.
- **Amazon SQS** supports messages up to 1 MiB, retention up to 14 days, visibility timeouts up to 12 hours, and fair queues for multi-tenant standard queues.
- **Uber** published its ladder of Kafka retry topics and dead-letter queues in 2018, a pattern now widely copied. **PhonePe's** TStore uses Kafka as a write-ahead log for payment records (see CS211).
- **Debezium** (3.x) ships an outbox event router that turns outbox rows into topic messages keyed by aggregate ID.

Interview questions from this course:

1. **"How do you make sure an order event is published if and only if the order is saved?"** A strong answer explains why dual writes fail, then covers the transactional outbox with a polling relay or CDC, ordering by aggregate key, relay crash behaviour, and idempotent consumers downstream.
2. **"How do you get exactly-once processing from Kafka into a database?"** Cover the boundary of Kafka transactions, idempotent writes or an inbox table, storing offsets in the same database transaction, and why "exactly once" means exactly-once effects.
3. **"Consumer lag is growing. Walk me through it."** Cover lag in time vs messages, processing time per message, downstream slowness, rebalances, poison messages, the partition-count ceiling, and short-term vs long-term fixes.
4. **"Design a booking saga: payment succeeds but the seat is gone. What happens?"** Cover orchestration vs choreography, compensation (refund), pivot steps, timeouts, idempotency of every step, user-visible states, and how you test each path.
5. **"Queue or log for these: sending emails, order history for analytics, rider location updates?"** Cover replay needs, ordering, fan-out to many consumers, retention, per-message acknowledgement, and the operational cost of each system.

## Resources (free first)

- **Documentation:** [Apache Kafka docs](https://kafka.apache.org/documentation/); [RabbitMQ quorum queues](https://www.rabbitmq.com/docs/quorum-queues) and [streams](https://www.rabbitmq.com/docs/streams); [Amazon SQS FIFO exactly-once processing](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html), [fair queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fair-queues.html) and [message quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html); [NATS JetStream](https://docs.nats.io/nats-concepts/jetstream); [Debezium outbox event router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html); [CloudEvents](https://cloudevents.io/); [KEDA](https://keda.sh/); [River](https://riverqueue.com/) (Postgres-backed jobs for Go).
- **Patterns:** microservices.io on the [transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html) and [sagas](https://microservices.io/patterns/data/saga.html); Martin Fowler on [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) and [CQRS](https://martinfowler.com/bliki/CQRS.html).
- **Papers and essays:** Garcia-Molina and Salem, [Sagas](https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf) (SIGMOD 1987); Kleppmann, [Turning the database inside-out](https://martin.kleppmann.com/2015/11/05/database-inside-out-at-oredev.html) (2015); Confluent, [Exactly-once semantics are possible](https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/) (2017); Jay Kreps, *The Log* (LinkedIn Engineering, 2013; the original page is offline, so read an archived copy).
- **Engineering write-ups:** Uber, [Building Reliable Reprocessing and Dead Letter Queues with Apache Kafka](https://www.uber.com/blog/reliable-reprocessing/) (2018); Slack, [Scaling Slack's Job Queue](https://slack.engineering/scaling-slacks-job-queue/).
- **Paid, worth it:** Kleppmann and Riccomini, *Designing Data-Intensive Applications*, 2nd edition (2026), chapters on streams; Chris Richardson, *Microservices Patterns* (Manning).

## Sources

All checked 12 Oct 2026.

- Apache Kafka 4.0.0 release announcement (18 Mar 2025): https://kafka.apache.org/blog/2025/03/18/apache-kafka-4.0.0-release-announcement/ ; 4.2.0 (Feb 2026, share groups production-ready): https://kafka.apache.org/blog/2026/02/17/apache-kafka-4.2.0-release-announcement/ ; 4.3.0 (22 May 2026): https://kafka.apache.org/blog/2026/05/22/apache-kafka-4.3.0-release-announcement/
- RabbitMQ release information (4.3.0 on 23 Apr 2026): https://www.rabbitmq.com/release-information ; classic mirroring removed in 4.0 (release notes): https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.0.1
- Amazon SQS message quotas (1 MiB, 14 days, 12 h visibility): https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html
- Debezium 3.x outbox event router: https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html
- Uber, reliable reprocessing (16 Feb 2018): https://www.uber.com/blog/reliable-reprocessing/
- Zerodha, 1.5 million contract notes in under 25 minutes (5 Feb 2024): https://zerodha.com/z-connect/updates/1-5-million-contract-notes-sent-in-less-than-25-minutes
- PhonePe TStore (Aug 2024), via [CS211 sources](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md)

_Last reviewed: 2026-10_
