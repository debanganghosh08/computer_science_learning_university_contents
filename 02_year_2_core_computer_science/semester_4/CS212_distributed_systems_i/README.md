# CS212 · Distributed Systems I

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 2 · 4 | 4 (≈ 120 hours) | L1 → L3 | [CS203](../../semester_3/CS203_operating_systems/README.md), [CS204](../../semester_3/CS204_computer_networks/README.md) | [CSG303](../../../03_majors/computer_science_general/year_3/CSG303_distributed_systems_ii_consensus_replication/README.md), [BE304](../../../03_majors/backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md), [CLD301](../../../03_majors/cloud_engineering/year_3/CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md), [DEN302](../../../03_majors/data_engineering/year_3/DEN302_batch_processing_with_spark/README.md), [DEN303](../../../03_majors/data_engineering/year_3/DEN303_streaming_systems_kafka_and_flink/README.md), [SWE401](../../../03_majors/software_engineering/year_4/SWE401_large_scale_system_design/README.md) |

Part of [Year 2 · Core Computer Science](../../README.md). Pairs with [CS211 Database Systems Internals](../CS211_database_systems_internals/README.md) (single-node storage and transactions) and [CS215 Cloud and DevOps Foundations](../CS215_cloud_and_devops_foundations/README.md) (where these systems run).

## Why this course matters now

Every non-trivial product is a distributed system: a phone talking to an API, which talks to replicated databases, queues and caches across data centres. Most large outages come from the partial failures this course teaches you to reason about:

- **AWS us-east-1, 19–20 October 2025:** a latent race condition in DynamoDB's DNS automation left a regional endpoint with no DNS records.
- **Cloudflare, 18 November 2025:** a database permissions change doubled a generated configuration file, which then crashed proxies worldwide.
- **Google Cloud, 12 June 2025:** a policy with blank fields crashed Service Control globally.

AI coding assistants can write a gRPC service or a retry loop in seconds. Showing that a protocol is correct under partitions, crashes and clock skew is still a human job. In a June 2026 evaluation of 30 language models writing TLA+ specifications from natural language, the best reached 26.6% syntactic and 8.6% semantic correctness. The engineers who stay valuable can state an invariant, test it with fault injection, and read a linearizability checker's counterexample.

## Learning outcomes

By the end you can:

1. **Explain** system and failure models (asynchronous, partially synchronous; crash-stop, crash-recovery, Byzantine), and **state** what FLP and CAP actually prove.
2. **Implement** RPC clients with timeouts, exponential backoff with jitter, retry budgets and idempotency keys, and **show** exactly-once *effects* under message loss.
3. **Implement** Lamport and vector clocks, and **explain** when you need hybrid logical clocks or TrueTime-style bounded uncertainty.
4. **Implement** Raft (election, log replication, persistence, snapshots) that passes adversarial tests hundreds of times in a row.
5. **Compare** consistency models (linearizable, sequential, causal, read-your-writes, eventual), and **check** a history for linearizability with a tool.
6. **Design** a partitioning and replication scheme with quorums, and **calculate** availability and latency trade-offs (PACELC).
7. **Explain** the lineage from GFS and MapReduce to Spark, and **implement** a fault-tolerant MapReduce.
8. **Test** distributed code with fault injection, deterministic simulation and a small TLA+ model, and **write** a blameless post-mortem of a real outage.

## Chapters and lessons

### Chapter 1 · Models, failures and the network (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What makes systems distributed | Partial failure, no global clock, unbounded delays; the fallacies of distributed computing | List the partial failures possible when a UPI app requests a payment |
| 1.2 System models | Synchronous, asynchronous and partially synchronous timing; crash-stop, crash-recovery, omission and Byzantine faults | Classify five real failures (lost packet, GC pause, disk full, bit flip, malicious node) |
| 1.3 Impossibility results | Two Generals; FLP (1985): no deterministic consensus in a fully asynchronous system with one crash; why real systems still work | Explain FLP in five sentences to a classmate, then have them find the gap |
| 1.4 Go for distributed systems | Goroutines, channels, `sync.Mutex`, `context` deadlines, the race detector | Lab 1 warm-up: concurrent web crawler with a race-free shared map |

**Check your understanding:** (1) Why can't a node tell a crashed peer from a slow one? (2) What extra assumption lets Raft make progress despite FLP? (3) A GC pause of 20 seconds hits a leader: which failure model does that look like to its peers?

### Chapter 2 · Communication: RPC, retries and idempotency (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 RPC | Stubs, serialization (Protocol Buffers), gRPC, HTTP/2 streams; why remote calls are not local calls | Build a gRPC or Go `net/rpc` service and measure p50/p99 latency |
| 2.2 Delivery semantics | At-most-once, at-least-once, exactly-once *effect*; duplicate detection tables | Lab 1: a KV server with at-most-once `Put` over an unreliable network (MIT 6.5840 Lab 2) |
| 2.3 Timeouts and backoff | Choosing timeouts from latency distributions; exponential backoff with jitter; retry budgets (AWS Builders' Library) | Simulate a retry storm, then fix it with jitter and a budget |
| 2.4 Idempotency keys | Client-generated keys, server-side deduplication, key expiry; Razorpay's mandatory payout idempotency keys | Design the idempotency table for a payout API |
| 2.5 Overload and cascading failure | Load shedding, deadline propagation, circuit breakers (Google SRE book chapters 21–22) | Add deadline propagation across three services and show a cascade stopping |

**Check your understanding:** (1) A client times out after the server has committed a payment: what must happen on retry? (2) Why does jitter matter more than the backoff base? (3) If each of 5 layers makes up to 3 attempts, how can one user request become 3⁵ = 243 calls at the bottom, and what stops it?

### Chapter 3 · Time, clocks and ordering (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Physical clocks | Quartz drift, NTP, monotonic vs wall-clock time, why `time.Now()` differences can go negative | Measure clock offset between two machines or VMs |
| 3.2 Logical clocks | Happens-before, Lamport clocks (1978), total order by tie-break | Implement Lamport clocks and order a chat log |
| 3.3 Vector clocks | Detecting concurrency; size costs; version vectors in Dynamo-style stores | Lab 2: causal broadcast with vector clocks |
| 3.4 Hybrid and bounded-uncertainty clocks | Hybrid logical clocks; Spanner's TrueTime and commit wait | Compute commit wait for a given uncertainty interval |
| 3.5 Snapshots and IDs | Chandy–Lamport global snapshots; Snowflake-style IDs; UUIDv7 (RFC 9562) | Generate time-ordered IDs on 10 nodes and test for collisions and ordering |

**Check your understanding:** (1) Why can Lamport timestamps order events but not detect concurrency? (2) What would break in Spanner if the clock-uncertainty bound were violated? (3) Why should a lease expiry use a monotonic clock?

### Chapter 4 · Failure detection, leases and membership (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Failure detectors | Heartbeats, timeouts, completeness vs accuracy, phi-accrual detection | Tune a detector on a recorded latency trace for false positives vs detection time |
| 4.2 Gossip membership | SWIM: indirect probes, suspicion, dissemination | Lab 3: SWIM-lite membership for 20 simulated nodes |
| 4.3 Leases and fencing | Leader leases, clock assumptions, fencing tokens to stop zombie leaders | Show a stale lock-holder corrupting data, then fix it with fencing tokens |
| 4.4 Split brain | Quorums vs majority partitions; why two-node clusters are dangerous | Partition a 2-node and a 3-node cluster and record which can still act safely |

**Check your understanding:** (1) Why is a lock without a fencing token unsafe even with a perfect lock service? (2) What does a shorter heartbeat timeout buy, and what does it cost? (3) Why do consensus clusters use odd sizes?

### Chapter 5 · Replication (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Leader-follower | Synchronous vs asynchronous replication, replication lag, failover and its dangers | Measure lag on a PostgreSQL replica pair under write load |
| 5.2 State machine replication | Deterministic commands, replicated logs, primary-backup vs SMR | Turn a KV store into a replicated state machine on paper |
| 5.3 Leaderless quorums | Dynamo (2007): N, R, W; sloppy quorums, hinted handoff, read repair, Merkle-tree anti-entropy | Compute which R/W settings tolerate one failure with N = 3 and N = 5 |
| 5.4 Multi-leader and conflicts | Last-writer-wins, version vectors, CRDTs (G-counter, OR-set) | Lab 4: implement a G-counter and an OR-set and test convergence |
| 5.5 Chain replication | Head/tail roles, strong consistency with high throughput | Compare chain and primary-backup by message counts per write |

**Check your understanding:** (1) Why can last-writer-wins silently lose data? (2) With N = 3, R = 1, W = 3, what fails when one replica is down? (3) Why do async replicas break read-your-writes, and name two fixes.

### Chapter 6 · Consistency models and CAP (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The model zoo | Linearizability, sequential, causal, PRAM, eventual; session guarantees (Jepsen consistency map) | Place six real systems on the Jepsen map using their docs |
| 6.2 Checking histories | Linearizability checking; Porcupine (Go) | Lab 5: feed recorded histories from your KV server to Porcupine and read a counterexample |
| 6.3 CAP, precisely | Gilbert and Lynch (2002); Brewer's "twelve years later"; why "CP or AP" labels mislead (Kleppmann, 2015) | Rewrite three vendor claims as precise statements |
| 6.4 PACELC | The latency vs consistency trade-off without partitions (Abadi, 2012) | Classify DynamoDB-style, Spanner-style and PostgreSQL-replica setups |

**Check your understanding:** (1) Is a single-leader database with async replicas linearizable? Under what reads? (2) Serializability does not promise real-time order: give an example where a serializable system returns a stale read that a linearizable one could not. (3) What does CAP say about a system with no partitions?

### Chapter 7 · Consensus I: Raft (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Leader election | Terms, randomized timeouts, `RequestVote`, the election restriction | Lab 6 (MIT 3A): elections that survive partitions |
| 7.2 Log replication | `AppendEntries`, consistency check, fast backup, the commit rule for current-term entries | Lab 6 (MIT 3B): replicate and commit under loss and reordering |
| 7.3 Persistence | What must be on stable storage before replying (`currentTerm`, `votedFor`, log) | Lab 7 (MIT 3C): crash-restart tests |
| 7.4 Snapshots and compaction | `InstallSnapshot`, bounded logs | Lab 7 (MIT 3D): snapshots |
| 7.5 A service on Raft | Linearizable reads (read index, leases), duplicate detection, client redirection | P2: a fault-tolerant KV service on your Raft (MIT Lab 4) |
| 7.6 Membership changes | Joint consensus vs single-server changes | Simulate adding two nodes to a 3-node cluster and find the unsafe sequence |

**Check your understanding:** (1) Why can't a leader commit an entry from a previous term by counting replicas alone (Figure 8 of the Raft paper)? (2) What breaks if `votedFor` is not persisted? (3) Why must a leader confirm it is still leader before serving a linearizable read?

### Chapter 8 · Consensus II: Paxos intuition and coordination services (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Single-decree Paxos | Proposers, acceptors, ballots, prepare/promise, accept/accepted ("Paxos Made Simple", 2001) | Hand-simulate two competing proposers and show only one value is chosen |
| 8.2 Multi-Paxos and Raft | Stable leaders, log slots; how Raft maps onto Multi-Paxos | Write a one-page comparison table |
| 8.3 Coordination services | Chubby (2006), ZooKeeper (2010), etcd; locks, leader election, configuration, watches | Lab 8: use etcd's lease plus compare-and-swap to elect a leader among three processes, with fencing tokens |
| 8.4 Consensus in production | Kafka 4.0 (March 2025) runs entirely on KRaft without ZooKeeper; etcd under Kubernetes; Raft groups in TiKV | Read the Kafka 4.0 announcement and list what operators no longer run |

**Check your understanding:** (1) Why do Paxos acceptors promise never to accept lower ballots? (2) What does a coordination service give you that a database row lock does not? (3) Why did removing ZooKeeper simplify Kafka operations?

### Chapter 9 · Partitioning and distributed transactions (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Partitioning schemes | Hash, range, consistent hashing with virtual nodes; hot keys | Measure load imbalance for 1M keys on 10 nodes with and without virtual nodes |
| 9.2 Rebalancing and routing | Shard maps, configuration services, client-side vs proxy routing; migration without downtime | Design a shard migration plan with a cut-over step |
| 9.3 Secondary indexes | Local (scatter-gather) vs global (term-partitioned) indexes | Estimate fan-out for a "orders by restaurant" query under each design |
| 9.4 Sharded KV | Replica groups per shard, configuration changes, shard handoff (MIT Lab 5) | Start P3 design |
| 9.5 Cross-shard transactions | 2PC over consensus groups; Spanner's TrueTime commit; sagas for long workflows | Model a food order (payment, restaurant, rider) as a saga with compensations |

**Check your understanding:** (1) Why does adding one node with naive `hash(key) mod N` move most keys? (2) Why does running 2PC across Raft groups remove 2PC's blocking problem? (3) When is a saga acceptable instead of an atomic transaction?

### Chapter 10 · From MapReduce to Spark (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 GFS and MapReduce | Chunk servers, a single master, re-execution on failure, stragglers and backup tasks (2003, 2004) | Lab 9: MapReduce coordinator and workers that survive worker crashes (MIT 6.5840 Lab 1) |
| 10.2 Spark and lineage | RDDs (2012), lineage-based recovery vs replication, narrow vs wide dependencies, shuffles | Run a word count and a join in Spark 4.x locally and read the DAG in the UI |
| 10.3 Skew and partitioning in practice | Hot keys, salting, broadcast joins, adaptive query execution in Spark | Fix a skewed join with salting or a broadcast join and measure the change in the Spark UI |
| 10.4 Streams | Logs as the source of truth, consumer groups, exactly-once processing in outline | Sketch how a clickstream reaches a dashboard through Kafka |

**Check your understanding:** (1) Why does MapReduce write intermediate results to local disk? (2) When is recomputing from lineage cheaper than replicating data? (3) What makes a shuffle the expensive step?

### Chapter 11 · Verifying and operating distributed systems (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Fault injection and Jepsen | Partitions, clock skew and crashes under load; history checking | Run your Raft KV under a nemesis schedule and check histories |
| 11.2 Deterministic simulation | FoundationDB's simulation testing; TigerBeetle's VOPR; seeded schedulers | Make your Raft tests replayable from a seed |
| 11.3 Formal specification | TLA+ and the TLC model checker; how AWS used formal methods (CACM 2015) | Lab 10: specify and model-check a two-process lock or a tiny replication protocol |
| 11.4 Observability | Distributed tracing (OpenTelemetry), correlation IDs, RED metrics | Trace one request across three services |
| 11.5 Reading post-mortems | The AWS October 2025, Cloudflare November 2025 and Google Cloud June 2025 write-ups | Write a one-page analysis: trigger, latent cause, blast radius, the fix you would add |

**Check your understanding:** (1) Why do distributed bugs disappear when you add logging? (2) What can a model checker prove that 10,000 test runs cannot? (3) In the Cloudflare outage, what kind of validation would have stopped the bad file?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 warm-up: Go concurrency | Race-free crawler |
| 2 | 2 | Lab 1: at-most-once KV | Passing tests; P1 starts |
| 3 | 3 | Lab 2: causal broadcast | Vector-clock tests; P1 due |
| 4 | 4 | Lab 3: SWIM-lite | Detection-time vs false-positive plot |
| 5 | 5 | Lab 4: quorums | Quorum simulator results |
| 6 | 5 | Lab 4: CRDTs | Convergence tests |
| 7 | 6 | Lab 5: linearizability checking | Annotated counterexample |
| 8 | 7 | Lab 6: Raft election and log | Tests passing 100 times in a row; P2 starts |
| 9 | 7 | Lab 7: persistence and snapshots | Tests passing 200 times with `-race` |
| 10 | 8 | Lab 8: leases, fencing, etcd | Election demo; P2 due |
| 11 | 9 | Shard design | P3 design review |
| 12 | 10 | Lab 9: MapReduce | Crash-tolerant MapReduce |
| 13 | 11 | Lab 10: TLA+ and simulation | Model-checked spec, replayable seed |
| 14 | 11 | P3 completion | P3 demo and post-mortem essay |
| 15 | Review and exam | — | Written exam, Raft oral |

## Working with AI in this course

- **Use AI for:** summarizing papers before you read them in full (then check the summary against the paper); generating fault-injection schedules and test scaffolding; explaining Go race-detector reports; producing log-analysis scripts that turn 10,000 lines of Raft debug output into a per-term timeline; drafting TLA+ that you then model-check.
- **Do without AI (drills):** the Raft labs (election, log, persistence); hand-simulating Raft elections and Paxos rounds on paper; quorum overlap arithmetic; drawing vector clocks for a message diagram; explaining Figure 8 of the Raft paper aloud.
- **Verify AI output by:** running test suites hundreds of times with the race detector (a protocol bug may appear once in 200 runs); checking histories with a linearizability checker; model-checking small configurations with TLC; asking for the invariant a piece of code maintains, then writing a test that tries to break it.
- **Where AI still fails here:** in the June 2026 study, the best of 30 language models produced semantically correct TLA+ only 8.6% of the time. You can demonstrate the coding gap yourself: generate a Raft implementation with an assistant, run the 6.5840-style tests 500 times under partitions, and record the failures. Code that looks right but breaks under rare interleavings is the core risk here. The defence is a person who knows the invariants.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (autograded, must pass repeated runs) | 30% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Written exam (models, clocks, quorums, consensus traces) | 20% |
| Raft oral and post-mortem essay | 10% |

**Mastery gate:** you pass when you can, without AI help, (a) run your Raft implementation's full test suite 500 times with the race detector and show zero failures; (b) explain to an examiner, on a whiteboard, why a given Raft log state is or is not safe and what the leader does next; and (c) take a short incident description you have not seen before, then name the consistency or failure-model assumption that broke and propose a mechanism (fencing, idempotency, quorum change, deadline) that would have contained it.

## Industry reality

Raft runs in etcd (the datastore behind Kubernetes), in TiKV's Raft groups, and in Kafka's KRaft mode: Kafka 4.0 (March 2025) is its first release to run entirely without ZooKeeper. AWS engineers have described using TLA+ to find subtle bugs in production designs (CACM 2015). FoundationDB and TigerBeetle test with deterministic simulation. In India, UPI's monthly volumes (published on NPCI's statistics page) make idempotency and reconciliation everyday concerns: Razorpay requires idempotency keys on payouts. Zerodha's engineering blog argues for "common sense" scaling over complex distributed machinery, which is a useful counterweight.

Interview questions from this course:

1. **"A client's payment request times out. What happens when it retries?"** Cover the fact that the server may have committed, idempotency keys and deduplication storage, key expiry, returning the original result, and backoff with jitter.
2. **"Walk me through Raft leader election. Why can't a node with a stale log win?"** Cover terms, randomized timeouts, vote granting, the up-to-date log check (last term, then index), and why committed entries survive.
3. **"Is your database CP or AP?"** Explain why the label is too coarse, define linearizability, say what happens to minority partitions, cover PACELC latency trade-offs, and give per-operation choices.
4. **"Generate unique, roughly time-ordered IDs across 100 servers."** Cover Snowflake-style bit layouts, clock skew and backwards jumps, UUIDv7, per-node sequence counters, and what "roughly" means for ordering guarantees.
5. **"Pick a real outage and explain it."** For example AWS October 2025: a latent race in automation, an empty DNS record, dependency fan-out, retries adding load, and recovery steps. A strong answer separates trigger from root cause and proposes containment (cells, static stability, validation of generated config).

## Resources (free first)

- **Primary course:** [MIT 6.5840 Distributed Systems (Spring 2026)](https://pdos.csail.mit.edu/6.824/) ([schedule and labs](https://pdos.csail.mit.edu/6.824/schedule.html); Labs 1–5 in Go).
- **Lecture notes:** Martin Kleppmann's Cambridge [distributed systems notes](https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/dist-sys-notes.pdf) and [video lectures](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB).
- **India:** NPTEL [Distributed Systems](https://nptel.ac.in/courses/106106168) (Prof. Rajiv Misra).
- **Raft:** [paper](https://www.usenix.org/system/files/conference/atc14/atc14-paper-ongaro.pdf), [raft.github.io](https://raft.github.io/) (visualization), [The Secret Lives of Data](https://thesecretlivesofdata.com/raft/).
- **Papers:**
  - [Time, Clocks, and the Ordering of Events](https://lamport.azurewebsites.net/pubs/time-clocks.pdf)
  - [Paxos Made Simple](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf)
  - [Distributed Snapshots](https://lamport.azurewebsites.net/pubs/chandy.pdf)
  - [Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
  - [GFS](https://research.google/pubs/the-google-file-system/)
  - [MapReduce](https://www.usenix.org/conference/osdi-04/mapreduce-simplified-data-processing-large-clusters)
  - [Spark RDDs](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/zaharia)
  - [Chubby](https://research.google/pubs/the-chubby-lock-service-for-loosely-coupled-distributed-systems/)
  - [ZooKeeper](https://www.usenix.org/conference/usenix-atc-10/zookeeper-wait-free-coordination-internet-scale-systems)
  - [Spanner](https://www.usenix.org/conference/osdi12/technical-sessions/presentation/corbett)
  - [CAP Twelve Years Later](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)
  - [PACELC](https://cs.umd.edu/~abadi/papers/abadi-pacelc.pdf)
- **Practice and patterns:**
  - [Jepsen consistency models](https://jepsen.io/consistency/models) and [analyses](https://jepsen.io/analyses)
  - [Please stop calling databases CP or AP](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html)
  - [Patterns of Distributed Systems](https://martinfowler.com/articles/patterns-of-distributed-systems/)
  - [Timeouts, retries, and backoff with jitter](https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter)
  - Google SRE book: [Handling Overload](https://sre.google/sre-book/handling-overload/), [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
- **Tools:** [Porcupine](https://github.com/anishathalye/porcupine), [TLA+ Foundation](https://foundation.tlapl.us/), [FoundationDB simulation testing](https://apple.github.io/foundationdb/testing.html), [Apache Spark docs](https://spark.apache.org/docs/latest/).
- **Paid, worth it:** *Designing Data-Intensive Applications*, 2nd edition (O'Reilly, March 2026).

## Sources

All checked 12 Oct 2026.
- [MIT 6.5840 Spring 2026](https://pdos.csail.mit.edu/6.824/) and [lab schedule](https://pdos.csail.mit.edu/6.824/schedule.html).
- [AWS summary of the 19–20 Oct 2025 us-east-1 event](https://aws.amazon.com/message/101925/).
- [Cloudflare 18 Nov 2025 outage](https://blog.cloudflare.com/18-november-2025-outage/).
- [Google Cloud 12 Jun 2025 incident report](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW).
- [Can LLMs Write Correct TLA+ Specifications?](https://arxiv.org/abs/2606.05792) (arXiv, 4 Jun 2026): 30 LLMs; up to 26.6% syntactic and 8.6% semantic correctness.
- [Apache Kafka 4.0 release announcement](https://kafka.apache.org/blog/2025/03/18/apache-kafka-4.0.0-release-announcement/) (18 Mar 2025).
- [etcd](https://etcd.io/) and [TiKV](https://tikv.org/) home pages (Raft).
- [How Amazon Web Services uses formal methods](https://www.amazon.science/publications/how-amazon-web-services-uses-formal-methods) (CACM 2015).
- [TigerBeetle safety and VOPR](https://docs.tigerbeetle.com/concepts/safety/).
- [Razorpay payout idempotency](https://razorpay.com/docs/api/x/payout-idempotency/).
- [Zerodha: Scaling with common sense](https://zerodha.tech/blog/scaling-with-common-sense/) (Jun 2020).
- [NPCI UPI product statistics](https://www.npci.org.in/what-we-do/upi/product-statistics) (monthly volumes; the page blocks automated fetching, so no figure is quoted here).
- [RFC 9562 (UUIDs, including version 7)](https://www.rfc-editor.org/rfc/rfc9562).
- [Spark 4.2.0 release](https://spark.apache.org/downloads.html) (Jul 2026).

_Last reviewed: 2026-10_
