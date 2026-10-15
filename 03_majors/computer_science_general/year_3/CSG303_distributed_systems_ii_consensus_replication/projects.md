# CSG303 · Labs and projects

Implementation work is in Go or Rust. Every protocol lab is tested under injected faults (message loss, reordering, duplication, partitions including asymmetric ones, crashes, pauses and clock skew) for many seeds, and every failure must be replayable from its seed. Specifications are in TLA+ (TLC or Apalache) or P. Hand-simulation parts are AI-off.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Paxos in TLA+ | Single-decree Paxos in PlusCal or TLA+; check agreement with TLC for 3 acceptors and 2 proposers; then ask an assistant for a spec from prose and grade it | Spec, TLC output, three mutations that TLC catches, graded AI spec with its errors | 5 h |
| 2 · Multi-Paxos | Multi-Paxos with stable leader, slots, no-op filling and catch-up | Tests passing 200 seeded runs with partitions; latency per command | 7 h |
| 3 · Raft under partial partitions | Extend your CS212 Raft (or etcd raft) with PreVote, CheckQuorum, read index and leases | Reproduction of leader churn under an asymmetric partition, before/after election counts, lease-read failure under injected clock skew | 6 h |
| 4 · PBFT simulator | n = 4 and n = 7 with one or two equivocating replicas and a faulty primary (view change) | Safety checks across 1,000 runs; message and signature counts vs HotStuff-style linear view change | 6 h |
| 5 · Text CRDT | RGA or Fugue with causal delivery; replay a real editing trace | Convergence results under 10⁵ random interleavings; interleaving test; ask-an-assistant comparison | 6 h |
| 6 · Elle on real histories | Append and read-write register workloads against PostgreSQL at two isolation levels and against your own store | Elle reports with each anomaly explained in plain words | 4 h |
| 7 · Percolator vs Calvin | Two transaction layers on the same sharded KV store; contention workloads (uniform and Zipf) | Throughput, latency and abort-rate plots; a paragraph on why each wins where it wins | 7 h |
| 8 · Liveness in TLA+ | Add fairness and check that a value is eventually chosen; show a liveness counterexample without fairness | Spec, TLC output, explanation of the lasso-shaped counterexample | 4 h |
| 9 · P model | Model a client–server retry protocol (or Raft client sessions) in P; find a seeded bug | P model, the failing trace, the fix | 4 h |
| 10 · Jepsen-style harness | Generator, nemesis and checker for your P3 store, plus a deterministic simulation mode | Harness code, a seeded bug found and replayed, run statistics | 6 h |

## Projects

### P1 · Model-checking consensus variants (L1, ~6 hours)

**Real-world inspiration:** AWS engineers report finding subtle design bugs with TLA+ before code was written (CACM 2015 and 2025); Flexible Paxos showed that the quorum rules most systems use are stronger than needed.

**What to build:** a TLA+ specification of Multi-Paxos (bounded to 3 slots) with configurable phase-1 and phase-2 quorum systems, and a short report on which quorum configurations are safe.

**Acceptance criteria:**
- TLC checks agreement and validity for majority quorums with 3 and 5 acceptors (state counts reported).
- Flexible quorums (for example |Q1| = 4, |Q2| = 2 with 5 acceptors) pass; a non-intersecting configuration fails, with the counterexample trace explained step by step.
- Three seeded bugs (acceptor forgets its promise; leader skips phase 1 for one slot; acceptor accepts a lower ballot) are each caught, with the shortest trace.
- The report states the bounds you checked and what the result does and does not prove about unbounded systems.

**Stretch goals:** check the same properties with Apalache; add a refinement mapping to an abstract "chosen log" specification.

**What it proves to an employer:** you can turn a protocol into a checkable specification, a skill that infrastructure and database teams ask about directly.

### P2 · A collaborative text-editing CRDT (L2, ~15 hours)

**Real-world inspiration:** collaborative editors and local-first apps (Automerge, Yjs and others) rely on sequence CRDTs; research has shown that some designs interleave concurrent insertions badly (Fugue, 2023).

**What to build:** a Rust or TypeScript library implementing a sequence CRDT (Fugue or RGA) with insert, delete and causal delivery; a binary or JSON encoding; a small sync server and two browser or terminal clients that edit offline and merge.

**Acceptance criteria:**
- Property-based tests: all replicas converge after 10⁵ randomly generated concurrent sessions with random delivery orders and duplicate messages.
- An interleaving test: two users typing words concurrently at the same position never produce interleaved characters (or, for RGA, the anomaly is demonstrated and documented).
- Replaying the public editing trace (about 260,000 operations from the automerge-perf repository) produces the correct final text; time and peak memory reported and compared with Yjs or Automerge on the same machine.
- An offline scenario: a client edits for 1,000 operations while disconnected and merges correctly on reconnect.
- A two-page note proving (or arguing carefully) convergence from the algebraic properties of your merge.

**Stretch goals:** rich-text marks; garbage collection of tombstones with a causal-stability check; a TLA+ or Isabelle check of convergence for small cases.

**What it proves to an employer:** you can build correct replicated data structures for real-time collaboration, a growing niche in product and developer-tool companies.

### P3 · A geo-replicated transactional key-value store, tested like a vendor would be (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Spanner, CockroachDB, TiDB/TiKV and FoundationDB combine replication groups with distributed transactions, and Jepsen analyses regularly find anomalies in such systems. The deployment below is an **illustrative scenario**: one store serving users from three regions (for example Mumbai, Singapore and Frankfurt), simulated on your machine with network delay injection.

**What to build:** a sharded store with one Raft (or Multi-Paxos) group per shard, a transaction layer offering serializable isolation (2PC over consensus groups, Percolator-style, or Calvin-style; justify your choice), linearizable single-key reads, a TLA+ specification of the commit protocol, and the Jepsen-style harness from Lab 10.

**Acceptance criteria:**
- Elle reports no anomalies across 50 runs of 10 minutes each with partitions, crashes, pauses and clock skew of up to 500 ms (state your clock assumption and enforce it).
- Two bugs seeded by a classmate (from a list of plausible ones) are both found by your harness or your model checker, and replayed from seed.
- The TLA+ commit specification is model-checked for 2 shards and 2 concurrent transactions, with atomicity and isolation invariants.
- Measurements with injected inter-region delays (`tc netem` or your simulator): throughput and p50/p99 latency for single-shard and cross-shard transactions under low and high contention, with leader placement choices explained.
- Behaviour under a full regional failure is demonstrated: which operations stop, which continue, and why that matches your design.
- An 8-page report in paper format, including a threats-to-validity section and a comparison with one published system.

**Stretch goals:** lock-free read-only transactions at a snapshot timestamp; follower reads with bounded staleness; online re-sharding during a test run without anomalies.

**What it proves to an employer or lab:** you can build, specify and break a distributed database the way the best infrastructure teams and testing firms do. This is the strongest single artifact for database-kernel and distributed-systems roles.

## Feeds into

- [CSG401 Formal Methods and Program Verification](../../year_4/CSG401_formal_methods_and_program_verification/README.md): refinement, liveness and proof of P3's commit protocol.
- [CSG403 Quantum Computing for Computer Scientists](../../year_4/CSG403_quantum_computing_for_computer_scientists/README.md): the catalog sequence; quantum error correction is another replication-against-faults story.
- [SWE401 Large-Scale System Design](../../../software_engineering/year_4/SWE401_large_scale_system_design/README.md) and [BE401 Payments-Grade Systems](../../../backend_engineering/year_4/BE401_payments_grade_systems_transactions_idempotency/README.md): electives that apply these mechanisms to product systems.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and the [CSG flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/CSG_computer_science_general.md): P3 is its systems core.
