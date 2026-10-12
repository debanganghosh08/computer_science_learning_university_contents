# CS212 · Labs and projects

Labs are in Go, following the public handouts of [MIT 6.5840](https://pdos.csail.mit.edu/6.824/schedule.html) where noted. Run every test many times, always with `go test -race`, because a distributed bug that shows up once in 200 runs is still a bug. Keep lab solutions in a private repository so the labs stay useful for others. Labs 6 and 7 (Raft) are done without coding agents.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · RPC and at-most-once KV | Go warm-up (a concurrent crawler), then a key/value server whose `Put` is applied at most once over a lossy network (MIT Lab 2) | Code passing the tests 50 times in a row, and a note on how duplicate detection state is bounded | 7 h |
| 2 · Causal broadcast | Vector clocks and a causal-delivery layer for a group chat of 5 processes with random delays | Code, plus a test that fails if any message is delivered before one it causally depends on | 5 h |
| 3 · SWIM-lite membership | Ping, indirect ping-req, suspicion and gossip dissemination for 20 simulated nodes | A plot of detection time vs false-positive rate for three timeout settings | 5 h |
| 4 · Quorums and CRDTs | A simulator for N/R/W quorum reads and writes under node failure; a G-counter and an OR-set | Simulator results table, and convergence tests under random message reordering | 6 h |
| 5 · Linearizability checking | Record client histories from Lab 1 and check them with Porcupine; inject a stale-read bug and find it | The annotated counterexample visualization and a paragraph explaining it | 3 h |
| 6 · Raft: election and log | Leader election and log replication (MIT Lab 3A–3B) | Tests passing 100 times in a row with `-race`, and a per-term event timeline from your logs | 14 h |
| 7 · Raft: persistence and snapshots | Persist state, survive crash-restart, compact with `InstallSnapshot` (MIT Lab 3C–3D) | Tests passing 200 times in a row with `-race` | 12 h |
| 8 · Leases and fencing | Leader election with etcd leases and compare-and-swap; show a zombie leader corrupting a store without fencing, then prevent it with fencing tokens | Demo script and a failure log before and after the fix | 4 h |
| 9 · MapReduce | A coordinator and workers that complete word count and an inverted index despite crashed and slow workers (MIT Lab 1) | Code passing the crash tests, and a note on how you handle stragglers | 8 h |
| 10 · Model checking and simulation | A TLA+ (or PlusCal) spec of a two-process lock or a primary-backup protocol, checked with TLC; make your Raft tests replayable from a random seed | The spec, the TLC output including one invariant violation you fixed, and a seed that reproduces a past failure | 6 h |

## Projects

### P1 · Exactly-once payment effects over an unreliable network (L1, ~6 hours)

**Real-world inspiration:** Razorpay makes idempotency keys mandatory on payouts, and warns that retrying with a *new* key while the first payout is processing can pay twice ([Razorpay docs](https://razorpay.com/docs/api/x/payout-idempotency/)). The AWS Builders' Library explains why retries without jitter and budgets overload recovering services ([Timeouts, retries, and backoff with jitter](https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter)).

**What to build:**
- a small payment service with an idempotency-key table;
- a client library with timeouts, exponential backoff with full jitter and a retry budget;
- a fault-injecting proxy between the two.

**Acceptance criteria:**
- Send 10,000 payments through the proxy while it drops 20% of requests, drops 20% of responses *after* the server committed, and delays 5% by 2 seconds. The result must have zero duplicate charges, zero lost acknowledged payments, and a definite final status for every request.
- With the server down for 60 seconds, the request rate arriving at the server stays at or below 1.1× normal traffic. Measure it and plot it.
- Reusing a key with a different payload is rejected with an explicit error.
- A histogram shows attempts per request.

**Stretch goals:** key expiry with a TTL and safe clean-up; deadline propagation from client to database; a circuit breaker with half-open probing.

**What it proves to an employer:** you build backends that stay correct when the network misbehaves, which is the first thing fintech and e-commerce teams test for.

### P2 · Linearizable key-value store on your own Raft (L2, ~15 hours)

**Real-world inspiration:** etcd, which stores Kubernetes cluster state, is built on Raft ([etcd](https://etcd.io/)). Kafka 4.0 replaced ZooKeeper with its own Raft-based KRaft quorum ([Kafka 4.0](https://kafka.apache.org/blog/2025/03/18/apache-kafka-4.0.0-release-announcement/)).

**What to build:** a replicated KV service (`Get`, `Put`, `Append`) on your Raft from Labs 6–7, with client request deduplication that survives snapshots, leader redirection and snapshot-based log compaction (MIT Lab 4 equivalent).

**Acceptance criteria:**
- Your Raft passes its full test suite 500 consecutive times with `-race`.
- Histories from 50 randomized runs (partitions, crashes, unreliable network) all pass a Porcupine linearizability check.
- Duplicate client requests are applied exactly once, including across snapshot and restart.
- Persisted Raft state never exceeds 8× the snapshot threshold.
- You report commit latency (p50, p99) for 3-node and 5-node clusters, and the median time to elect a new leader after the leader is killed (target under 1 second with 150–300 ms election timeouts).

**Stretch goals:** read-index reads without appending to the log; Pre-Vote to stop disruptive candidates; leadership transfer.

**What it proves to an employer:** you can implement consensus correctly and prove it with a checker. Few people with two years of study can show this.

### P3 · Sharded, replicated store with live resharding and a Jepsen-style report (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:**
- TiKV runs many independent Raft groups, one per data range ([TiKV](https://tikv.org/)).
- Notion moved to 480 logical shards so it could rebalance without re-keying ([Notion](https://www.notion.com/blog/sharding-postgres-at-notion)).
- Jepsen's public analyses set the bar for how to report correctness testing ([Jepsen](https://jepsen.io/analyses)).
- A food-delivery platform's order store, partitioned by city and rebalanced before festival peaks, is an *illustrative scenario* you can use for the workload.

**What to build:**
- a shard controller, itself replicated on Raft;
- several replica groups;
- client-side routing with configuration caching;
- shard migration with handoff and garbage collection (MIT Lab 5 equivalent);
- a nemesis harness that partitions, crashes and pauses nodes and skews clocks;
- a written report in the style of a Jepsen analysis.

**Acceptance criteria:**
- **Safety under migration:** move 10 shards between groups under continuous load while killing a random leader every 5 seconds. There must be zero lost acknowledged writes and zero duplicates, and every run must pass per-key linearizability checks.
- **Availability:** shards that are not moving keep serving with p99 latency within 2× of baseline during migrations.
- **Scaling:** throughput with 2 groups is at least 1.6× that of 1 group on a uniform workload. One hot-key run must show where scaling stops, with an explanation.
- **Reproducibility:** every failure found is replayable from a seed.
- **Report:** test design, nemeses, results, and at least two real bugs you found and fixed, each with the offending history.

**Stretch goals:** a TLA+ model of shard handoff checked with TLC for 2 groups × 2 shards; cross-shard transactions with 2PC across Raft groups; OpenTelemetry traces across client, controller and groups.

**What it proves to an employer:** you can design, build *and verify* a distributed data system, and write about it with the rigor of a professional correctness report. Systems teams at databases, cloud providers and payment companies read exactly this kind of work.

## Feeds into

- [CSG303 Distributed Systems II](../../../03_majors/computer_science_general/year_3/CSG303_distributed_systems_ii_consensus_replication/README.md): Byzantine faults, Paxos variants, geo-replication.
- [BE304 Asynchronous Systems](../../../03_majors/backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md) and [BE401 Payments-Grade Systems](../../../03_majors/backend_engineering/year_4/BE401_payments_grade_systems_transactions_idempotency/README.md): P1's idempotency work.
- [DEN302 Batch Processing with Spark](../../../03_majors/data_engineering/year_3/DEN302_batch_processing_with_spark/README.md) and [DEN303 Streaming Systems](../../../03_majors/data_engineering/year_3/DEN303_streaming_systems_kafka_and_flink/README.md): the MapReduce-to-Spark lineage.
- [SWE401 Large-Scale System Design](../../../03_majors/software_engineering/year_4/SWE401_large_scale_system_design/README.md) and [CAR401 Career Lab II](../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): system-design interviews draw directly on Chapters 2, 5, 6 and 9.
- [OPS304 Site Reliability Engineering](../../../03_majors/devops_sre_platform_engineering/year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md): post-mortems and overload control.
