# CSG303 · Distributed Systems II: Consensus, Replication and Scale

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L3 → L4 | [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md), [CS216](../../../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md); draws on [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) | [CSG403](../../year_4/CSG403_quantum_computing_for_computer_scientists/README.md) (catalog sequence); recommended for [CSG401](../../year_4/CSG401_formal_methods_and_program_verification/README.md); electives [SWE401](../../../software_engineering/year_4/SWE401_large_scale_system_design/README.md), [BE401](../../../backend_engineering/year_4/BE401_payments_grade_systems_transactions_idempotency/README.md); supports [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Computer Science (Theory, Systems and Research) major](../../README.md). CS212 gave you clocks, replication basics, consistency models, a working Raft, coordination services, sharding and a first contact with TLA+ and Jepsen. This course goes to the depth that infrastructure teams and systems researchers work at: why consensus is possible at all, Paxos and Raft as proofs rather than recipes, Byzantine fault tolerance, CRDTs for collaboration, distributed transactions from Percolator to Spanner and Calvin, and the specification and testing methods used to find bugs before customers do. The last two weeks are a papers seminar.

## Why this course matters now

Consensus and replication sit under almost every critical system, and their failures are subtle. In November 2020 a partially failed network switch let some etcd nodes see each other while others could not, and the Raft cluster behind a Cloudflare control plane churned through elections, causing an outage that Cloudflare called "a Byzantine failure in the real world" ([Cloudflare](https://blog.cloudflare.com/a-byzantine-failure-in-the-real-world/)). Jepsen found that PostgreSQL 12.3's SERIALIZABLE isolation allowed G2-item anomalies ([Jepsen, 2020](https://jepsen.io/analyses/postgresql-12.3)). Amazon S3 moved to strong read-after-write consistency in December 2020 ([AWS](https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-s3-now-delivers-strong-read-after-write-consistency-automatically-for-all-applications/)), and AWS describes using TLA+, the P language, property-based testing, fault injection and deterministic simulation to keep such systems correct ([Brooker and Desai, CACM, Jun 2025](https://cacm.acm.org/practice/systems-correctness-practices-at-amazon-web-services/)). AI assistants can produce a plausible Raft or CRDT implementation in minutes, but in a June 2026 evaluation the best of 30 models wrote semantically correct TLA+ only 8.6% of the time ([arXiv 2606.05792](https://arxiv.org/abs/2606.05792)). The people these teams hire can state the invariant, write the specification, build the fault-injection harness, and read the counterexample.

## Learning outcomes

By the end you can:

1. **Prove** why consensus needs 2f+1 replicas for crash faults and 3f+1 for Byzantine faults, and **explain** FLP's bivalence argument and how failure detectors and partial synchrony escape it.
2. **Implement** Multi-Paxos and **compare** it with Raft, Viewstamped Replication, Flexible Paxos and EPaxos on quorum structure, latency and failure behaviour.
3. **Harden** a Raft implementation with PreVote, CheckQuorum, leader leases, read index, learners and joint-consensus reconfiguration, and **reproduce** a partial-partition failure.
4. **Explain and simulate** PBFT and HotStuff, and **decide** when Byzantine fault tolerance is worth its cost.
5. **Design** state-based, operation-based and delta CRDTs, including a sequence CRDT for text, and **prove** convergence.
6. **Implement** distributed transactions (2PC over consensus, Percolator-style, Calvin-style deterministic ordering) and **identify** isolation anomalies such as write skew with Elle.
7. **Specify** protocols in TLA+ (safety, liveness, refinement) and P, and **model-check** them to find seeded bugs.
8. **Build** a Jepsen-style harness and a deterministic simulator, and **use** them to find bugs in your own and others' systems.
9. **Read, critique and present** systems papers to a research standard.

## Chapters and lessons

### Chapter 1 · The theory of agreement (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 FLP, properly | Bivalent configurations; the proof structure, not just the statement | Write the FLP proof outline in your own words; identify the step a timeout breaks |
| 1.2 Quorums and lower bounds | Why 2f+1 for crash faults; quorum intersection; Byzantine 3f+1 by the indistinguishability argument | Prove that 3 replicas cannot tolerate 1 Byzantine fault |
| 1.3 Escaping impossibility | Partial synchrony (Dwork–Lynch–Stockmeyer); failure detectors (◇S); randomized consensus (Ben-Or, idea) | Classify Raft, PBFT and a randomized protocol by how they escape FLP |
| 1.4 Consensus numbers | Herlihy's wait-free hierarchy: registers (1), test-and-set (2), compare-and-swap (∞) | Show why test-and-set cannot solve 3-process consensus (sketch) |

**Check your understanding:** (1) Which property, safety or liveness, does a consensus protocol give up during asynchrony, and why that one? (2) Why does Byzantine agreement need more replicas than crash agreement? (3) What does compare-and-swap's infinite consensus number mean for lock-free data structures?

### Chapter 2 · Paxos as a proof (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Single-decree Paxos, invariants first | The safety invariant; why acceptors promise; the proof by induction on ballots | Lab 1: write single-decree Paxos in TLA+/PlusCal and model-check it with TLC |
| 2.2 Multi-Paxos | Stable leaders, slots, phase-1 batching, gaps and no-ops; Paxos Made Moderately Complex | Lab 2: implement Multi-Paxos in Go or Rust with the CS212 test style |
| 2.3 Flexible Paxos | Only phase-1 and phase-2 quorums must intersect (Howard et al., 2016) | Model-check a 5-node configuration with phase-2 quorums of size 2 |
| 2.4 Fast and leaderless variants | Fast Paxos (bigger quorums, fewer round trips); EPaxos (dependency tracking, commutative commands) | Compute commit latency for 3 geo-placements under Multi-Paxos vs EPaxos |
| 2.5 Viewstamped Replication and Raft | VR Revisited (view changes, recovery); "Paxos vs Raft" (Howard and Mortier, 2020): the same algorithm with different leader election | Write a mapping table: Raft term ↔ Paxos ballot ↔ VR view |

**Check your understanding:** (1) In Multi-Paxos, why must a new leader run phase 1 for all open slots? (2) What does Flexible Paxos buy, and what risk does it shift to leader election? (3) Why can EPaxos commit in one round trip for commuting commands but not for conflicting ones?

### Chapter 3 · Raft in production (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Liveness under partial partitions | PreVote and CheckQuorum (Raft thesis §9.6); the Cloudflare 2020 incident | Lab 3: reproduce leader churn under an asymmetric partition, then fix it with PreVote and CheckQuorum |
| 3.2 Fast reads | Read index, leader leases and their clock assumptions, follower reads | Measure read latency for log reads, read index and leases; break leases with clock skew |
| 3.3 Reconfiguration | Joint consensus vs single-server changes; the 2015 single-server bug and its fix; learners (non-voting members) | Model-check single-server membership change in TLA+ (start from raft.tla) |
| 3.4 Performance | Batching, pipelining, parallel disk and network writes, Multi-Raft (TiKV, CockroachDB ranges) | Benchmark throughput with batching on and off |
| 3.5 Reading production code | etcd's `raft` library: `Ready` loop, storage interface, progress tracking | Trace one proposal through the etcd raft code and draw the sequence |

**Check your understanding:** (1) Why does PreVote stop a partitioned node from disrupting a healthy leader? (2) What exactly must be true about clocks for a lease read to be linearizable? (3) Why do learners make adding a node safer?

### Chapter 4 · Byzantine fault tolerance (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 PBFT | Pre-prepare, prepare, commit; certificates of 2f+1; view change; O(n²) messages | Lab 4: simulate PBFT with one equivocating replica; show safety holds |
| 4.2 Authentication | MACs vs signatures; threshold signatures; why authenticators matter for view changes | Count signature verifications per request for n = 4, 16, 64 |
| 4.3 HotStuff and chained BFT | Linear view change, three-chain commit, pipelining; DiemBFT lineage; Tendermint/CometBFT | Compare message complexity of PBFT and HotStuff in your simulator |
| 4.4 DAG-based BFT | Narwhal (data dissemination) and Bullshark (ordering) separation | Summarise why separating dissemination from ordering raises throughput |
| 4.5 When BFT is worth it | Permissioned vs open membership; software bugs as Byzantine faults; cost per decision | Write a one-page recommendation for an illustrative inter-bank settlement network |

**Check your understanding:** (1) Why is 2f+1 the certificate size when n = 3f+1? (2) Why does HotStuff's linear view change matter as n grows? (3) Would BFT have helped in the Cloudflare 2020 incident? Argue both sides.

### Chapter 5 · CRDTs and local-first collaboration (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The algebra | Join-semilattices; state-based (CvRDT) vs operation-based (CmRDT) vs delta CRDTs; strong eventual consistency | Prove a PN-counter converges using the semilattice laws |
| 5.2 Sets, maps and registers | OR-set, LWW and multi-value registers, nested maps; causal delivery requirements | Implement an OR-map and test with random delivery orders |
| 5.3 Sequence CRDTs | RGA, Logoot; the interleaving anomaly; Fugue (Weidner and Kleppmann) | Lab 5: implement a text CRDT and replay a real editing trace |
| 5.4 JSON documents and local-first | Automerge and Yjs; the local-first software ideals (Ink & Switch); sync protocols | Build a two-peer sync over WebSocket and a simulated offline period |
| 5.5 Verified CRDTs and limits | Strong eventual consistency proved in Isabelle (Gomes et al.); invariants CRDTs cannot keep (uniqueness, non-negative balance) | Show a bank balance going negative under concurrent CRDT withdrawals |

**Check your understanding:** (1) Why are commutativity, associativity and idempotence each needed for state-based merge? (2) Why does concurrent typing at the same position produce interleaved text in some sequence CRDTs? (3) Which application invariants need coordination no matter how clever the CRDT is?

### Chapter 6 · Isolation and distributed transactions (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Isolation, precisely | Adya's anomalies (G0, G1, G2), snapshot isolation and write skew, serializable snapshot isolation | Produce write skew in PostgreSQL under REPEATABLE READ, then prevent it with SERIALIZABLE |
| 6.2 Checking histories | Elle: inferring dependency cycles from observed histories | Lab 6: run Elle on histories from your store and from a real database |
| 6.3 Atomic commit | 2PC's blocking problem; 2PC over Paxos/Raft groups; parallel commits (CockroachDB) | Model-check 2PC in TLA+; find the blocking scenario |
| 6.4 Percolator | Snapshot-isolated transactions on Bigtable with a timestamp oracle and primary locks | Implement Percolator-style transactions on your KV store |
| 6.5 Spanner and TrueTime | External consistency, commit wait, lock-free read-only transactions | Compute commit wait for ε = 1, 7 and 100 ms; discuss the throughput cost |
| 6.6 Calvin and deterministic databases | Sequencing first, then deterministic execution without 2PC; FoundationDB's optimistic resolver | Lab 7: a Calvin-style sequencer layer; compare abort rates with Percolator under contention |

**Check your understanding:** (1) Why is snapshot isolation not serializable, and why do many systems still choose it? (2) What does Calvin give up to avoid 2PC? (3) Why does Spanner need bounded clock uncertainty while CockroachDB can run with hybrid logical clocks?

### Chapter 7 · Replication for storage at scale (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Chain replication and CRAQ | Strong consistency with reads from any replica | Measure read throughput of chain vs CRAQ in a simulator |
| 7.2 Quorum storage | Amazon Aurora: 6 copies across 3 zones, write quorum 4, read quorum 3; log-is-the-database | Prove the Aurora quorums intersect and tolerate an AZ+1 failure |
| 7.3 Managed databases in the open | DynamoDB's 2022 paper: Multi-Paxos per partition, adaptive capacity; Kafka KRaft and in-sync replicas | Extract three design decisions from the DynamoDB paper and their reasons |
| 7.4 Erasure coding | Reed–Solomon basics, repair bandwidth, when to replicate and when to code | Compute storage overhead and repair traffic for 3× replication vs RS(10,4) |
| 7.5 Tail latency | "The Tail at Scale": hedged and tied requests; fan-out amplification | Simulate p99 for fan-out 100 with and without hedging |

**Check your understanding:** (1) Why does Aurora replicate the log and not pages? (2) When is erasure coding a bad idea despite its lower storage cost? (3) Why does hedging reduce p99 but increase load?

### Chapter 8 · Geo-distribution and weak consistency (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Causal consistency | COPS and causal+; dependency tracking cost; session guarantees | Implement causal reads with version vectors across three simulated regions |
| 8.2 Tunable consistency | Azure Cosmos DB's five levels (strong, bounded staleness, session, consistent prefix, eventual) | Map each level to a guarantee from CS212's consistency map |
| 8.3 Placement | Leader placement, follower reads, regional failover; latency arithmetic with real inter-region round trips | Choose replica placement for users in Mumbai, Singapore and Frankfurt; compute commit latency |
| 8.4 Cells and blast radius | Cell-based architecture, shuffle sharding, static stability | Design a cell layout that limits a bad deploy to 5% of users |

**Check your understanding:** (1) Why is causal consistency the strongest model that stays available under partition? (2) What does "bounded staleness" bound, and who has to pay to keep the bound? (3) Why is a leader in the wrong region a latency bug for every write?

### Chapter 9 · Specification and verification (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 TLA+ in depth | Actions, invariants, temporal properties, fairness, liveness checking; state-space explosion and symmetry | Lab 8: check liveness of your Paxos spec under weak fairness |
| 9.2 Refinement | Refinement mappings: showing Multi-Paxos implements a replicated log | Write a refinement mapping for a toy protocol |
| 9.3 Other checkers | Apalache (symbolic, SMT-based); the P language for state machines; model-based testing from specs | Lab 9: model a Raft client protocol in P and find a seeded bug |
| 9.4 Verified distributed systems | IronFleet, Verdi; lightweight formal methods in Amazon S3's ShardStore (SOSP 2021) | Read the ShardStore paper's evaluation and list what each method caught |
| 9.5 Industrial practice | AWS's 2015 and 2025 CACM reports; where formal methods pay for themselves | Write a one-page proposal to specify one component of P3 |

**Check your understanding:** (1) What does model checking a 3-node configuration prove about a 5-node cluster, and what does it not? (2) Why do refinement proofs scale better than checking the implementation directly? (3) When is a lightweight method (property tests against a model) a better investment than a full proof?

### Chapter 10 · Testing distributed systems for real (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Jepsen methodology | Generators, nemeses (partitions, clock skew, crashes, pauses), checkers; reading published analyses | Lab 10: a Jepsen-style harness in your language of choice for your P3 store |
| 10.2 Deterministic simulation | FoundationDB's simulator; TigerBeetle's VOPR; Antithesis's deterministic hypervisor | Make your store run under a seeded simulator; replay a failure from its seed |
| 10.3 Property-based and model-based tests | Linearizability checking with Porcupine; random operation sequences against a model | Shrink a failing history to its minimal form |
| 10.4 Debugging from evidence | Per-node logs, causal timelines, visualising message traces | Turn 10,000 log lines into a per-term timeline with a script |

**Check your understanding:** (1) Why do bugs found by deterministic simulation stay fixed while flaky-test bugs return? (2) What does a Jepsen "valid? false" tell you, and what does "valid? true" not tell you? (3) Which fault does your harness not inject, and what bug could hide there?

### Chapter 11 · Papers seminar (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 How to read a systems paper | Problem, assumptions, mechanism, evaluation, what is not measured; Keshav's three-pass method | Write a one-page structured review of one paper |
| 11.2 Presenting | A 20-minute talk with one key figure, a reproduction of one claim, and three questions | Present one paper from the list below |
| 11.3 Reviewing | Writing a fair, specific review; separating "I don't like it" from "this is wrong" | Review a classmate's presentation in conference-review format |
| 11.4 Seminar list | PBFT (1999), Chain replication (2004), Percolator (2010), Spanner (2012), Calvin (2012), EPaxos (2013), Raft (2014), Flexible Paxos (2016), Aurora (2017), HotStuff (2019), Elle (2020), FoundationDB (2021), ShardStore (2021), Narwhal/Bullshark (2022), DynamoDB (2022), Fugue (2023) | Each student presents one, reproduces one figure or claim where feasible, and leads the discussion |

**Check your understanding:** (1) What is the weakest assumption in the paper you presented? (2) Which experiment would you add to the evaluation, and what result would change your mind? (3) Which idea in the list has aged best, and why?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lower-bound proofs (AI off) | Proof set |
| 2 | 2 | Lab 1 · Paxos in TLA+ | Model-checked spec; **P1 starts** |
| 3 | 2 | Lab 2 · Multi-Paxos | Tests passing 200 runs |
| 4 | 3 | Lab 3 · Raft under partial partitions | Churn reproduced and fixed; **P1 due** |
| 5 | 4 | Lab 4 · PBFT simulator | Equivocation experiment |
| 6 | 5 | Lab 5 · Text CRDT | Convergence tests; **P2 starts** |
| 7 | 6 | Lab 6 · Elle on real histories | Anomaly report; mid-term (AI off) |
| 8 | 6 | Lab 7 · Percolator vs Calvin | Abort-rate comparison |
| 9 | 7 | Storage quorums and tail latency | **P2 due** |
| 10 | 8 | Causal geo-replication | P3 design review |
| 11 | 9 | Lab 8 · Liveness in TLA+ | — |
| 12 | 9–10 | Labs 9–10 · P model and Jepsen harness | Seeded bug found |
| 13 | 11 | Papers seminar | Presentation and review |
| 14 | 11 | Papers seminar | **P3 due** |
| 15 | Review | Protocol oral | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** first-pass summaries of papers (then check every claim against the paper's text); explaining unfamiliar code in etcd, CometBFT or Automerge; generating nemesis schedules, workload generators and log-analysis scripts; drafting TLA+ or P that you then model-check and correct; acting as a hostile reviewer of your paper review.
- **Do without AI (drills):** the lower-bound and quorum proofs; hand-simulating Paxos, PBFT and Raft traces; deciding whether a given log state is safe; finding anomalies in a printed history; the core protocol code in Labs 2, 3 and 7; the mid-term, final and protocol oral.
- **Verify AI output by:** model-checking any AI-drafted specification and then mutating it (drop a guard, enlarge a quorum) to confirm the checker catches the bug; running implementations under your harness with partitions, pauses and clock skew for hundreds of seeds; checking histories with Porcupine or Elle; tracing every claimed guarantee back to an invariant.
- **Where AI still fails here (show it):** the 2026 TLA+ study measured 8.6% semantic correctness for the best model. In Lab 1 and Lab 8 you will ask an assistant to specify a protocol from an English description, model-check the result, and record each error (missing fairness, wrong quorum, an invariant that is trivially true). In Lab 5, ask for a sequence CRDT and test it for convergence and interleaving; generated versions commonly converge on simple tests and fail under concurrent inserts at the same position. Keep the failing traces.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Papers seminar (presentation, review, reproduction) | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + protocol oral | 15% |

**Mastery gate.** You pass when you can, with AI off: (1) given a printed Paxos, Raft or PBFT trace, decide whether a value is chosen, whether the state is safe, and what each node does next; (2) show write skew in a history and name the isolation level that forbids it; (3) explain, on a whiteboard, why Byzantine consensus needs 3f+1 replicas; and (4) using your own harness, find a bug seeded by the examiner in a replicated store within 60 minutes and explain it from the evidence.

## Industry reality

Raft runs in etcd, TiKV, CockroachDB and Kafka's KRaft; Multi-Paxos in DynamoDB (per its 2022 paper) and Spanner; BFT protocols in permissioned ledgers and blockchains (CometBFT, the HotStuff family); CRDTs in collaborative editors and local-first apps (Automerge, Yjs); deterministic simulation at FoundationDB, TigerBeetle and Antithesis's customers; TLA+ and P at AWS. In India, the scale of UPI makes reconciliation, idempotency and consistency daily concerns for payment companies (see [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md)); their internal protocols are not public, so any design of them here is illustrative.

**Interview questions from this course**

1. *Why does Byzantine consensus need 3f+1 replicas?* Strong answer: quorums of 2f+1 must intersect in at least f+1 nodes so at least one honest node is in both; the indistinguishability argument for n = 3f; certificates; cost in messages and signatures.
2. *How can a Raft cluster serve linearizable reads without writing to the log?* Strong answer: read index with a heartbeat round to confirm leadership; leases and their clock-drift assumptions; follower reads with read index; what breaks under clock skew or a GC pause.
3. *Design collaborative editing for a document product.* Strong answer: OT vs CRDT trade-offs; a sequence CRDT and the interleaving problem; presence and cursors; offline edits and sync; server role; invariants that need coordination (permissions, comments on deleted text).
4. *How do Spanner and Calvin each avoid anomalies across shards, and what does each cost?* Strong answer: Spanner's 2PC over Paxos with TrueTime commit wait for external consistency; Calvin's global sequencing and deterministic execution with no 2PC but needing read/write sets in advance; latency and contention trade-offs.
5. *Your database vendor claims serializability. How would you check?* Strong answer: Jepsen-style workloads with partitions, crashes and clock faults; history checking with Elle for G0–G2 anomalies; checking the claim per operation type; reproducing with seeds; reading the vendor's own Jepsen report critically.

## Resources (free first)

- **Courses and notes:** [MIT 6.5840](https://pdos.csail.mit.edu/6.824/) (continue from CS212); [MIT 6.852J Distributed Algorithms (OCW)](https://ocw.mit.edu/courses/6-852j-distributed-algorithms-fall-2009/); [Cornell CS 6410 Advanced Systems](https://www.cs.cornell.edu/courses/cs6410/2019fa/); Kleppmann's [Cambridge notes](https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/dist-sys-notes.pdf); van Steen and Tanenbaum, [Distributed Systems, 4th ed.](https://www.distributed-systems.net/index.php/books/ds4/) (free digital copy).
- **Blogs worth following:** [Decentralized Thoughts](https://decentralizedthoughts.github.io/) (BFT, explained by researchers); [Murat Demirbas's paper summaries](https://muratbuffalo.blogspot.com/); [Jepsen analyses](https://jepsen.io/analyses).
- **Consensus papers:** [Viewstamped Replication Revisited](https://dspace.mit.edu/handle/1721.1/71763); [Raft PhD thesis](https://web.stanford.edu/~ouster/cgi-bin/papers/OngaroPhD.pdf); [Flexible Paxos](https://arxiv.org/abs/1608.06696); [EPaxos](https://www.cs.cmu.edu/~dga/papers/epaxos-sosp2013.pdf); [Paxos vs Raft](https://arxiv.org/abs/2004.05074); [PBFT](https://css.csail.mit.edu/6.824/2014/papers/castro-practicalbft.pdf); [HotStuff](https://arxiv.org/abs/1803.05069); [Narwhal and Tusk](https://arxiv.org/abs/2105.11827); [Bullshark](https://arxiv.org/abs/2201.05677); [Wait-free synchronization](https://cs.brown.edu/~mph/Herlihy91/p124-herlihy.pdf).
- **Replication, CRDTs and transactions:** [Chain replication](https://www.cs.cornell.edu/home/rvr/Papers/OSDI04.pdf); [Local-first software](https://www.inkandswitch.com/local-first/); [Fugue](https://arxiv.org/abs/2305.00583); [Verifying strong eventual consistency](https://arxiv.org/abs/1707.01747); [Percolator](https://research.google/pubs/large-scale-incremental-processing-using-distributed-transactions-and-notifications/); [Calvin](http://cs.yale.edu/homes/thomson/publications/calvin-sigmod12.pdf); [CockroachDB parallel commits](https://www.cockroachlabs.com/blog/parallel-commits/); [FoundationDB](https://www.foundationdb.org/files/fdb-paper.pdf); [Aurora](https://www.amazon.science/publications/amazon-aurora-design-considerations-for-high-throughput-cloud-native-relational-databases); [DynamoDB (ATC 2022)](https://www.usenix.org/conference/atc22/presentation/elhemali); [COPS](https://www.cs.cmu.edu/~dga/papers/cops-sosp2011.pdf); [The Tail at Scale](https://research.google/pubs/the-tail-at-scale/); [Cosmos DB consistency levels](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels).
- **Verification and testing:** [Specifying Systems (free)](https://lamport.azurewebsites.net/tla/book.html); [Lamport's TLA+ video course](https://lamport.azurewebsites.net/video/videos.html); [Learn TLA+](https://learntla.com/); [raft.tla](https://github.com/ongardie/raft.tla); [Apalache](https://apalache-mc.org/); [P language](https://p-org.github.io/P/); [Elle](https://arxiv.org/abs/2003.10554) ([code](https://github.com/jepsen-io/elle)); [ShardStore (SOSP 2021)](https://www.amazon.science/publications/using-lightweight-formal-methods-to-validate-a-key-value-storage-node-in-amazon-s3); [IronFleet](https://www.microsoft.com/en-us/research/publication/ironfleet-proving-practical-distributed-systems-correct/); [Antithesis](https://antithesis.com/).
- **Code to read:** [etcd raft](https://github.com/etcd-io/raft), [CometBFT docs](https://docs.cometbft.com/), [Automerge](https://automerge.org/), [Yjs docs](https://docs.yjs.dev/), [editing-trace benchmark](https://github.com/automerge/automerge-perf).
- **Paid, worth it:** Kleppmann and Riccomini, *Designing Data-Intensive Applications*, 2nd ed. (O'Reilly, 2026); Cachin, Guerraoui and Rodrigues, *Introduction to Reliable and Secure Distributed Programming*.

## Sources

All checked 12 Oct 2026.

- Cloudflare, "A Byzantine failure in the real world" (Nov 2020) — https://blog.cloudflare.com/a-byzantine-failure-in-the-real-world/
- Jepsen, "PostgreSQL 12.3" (2020) — https://jepsen.io/analyses/postgresql-12.3
- AWS, "Amazon S3 now delivers strong read-after-write consistency" (Dec 2020) — https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-s3-now-delivers-strong-read-after-write-consistency-automatically-for-all-applications/
- Brooker and Desai, "Systems Correctness Practices at Amazon Web Services", *CACM* 68(6), Jun 2025 — https://cacm.acm.org/practice/systems-correctness-practices-at-amazon-web-services/ ; Newcombe et al., "How Amazon Web Services Uses Formal Methods" (CACM 2015) — https://www.amazon.science/publications/how-amazon-web-services-uses-formal-methods
- "Can LLMs Write Correct TLA+ Specifications?" (arXiv 2606.05792, Jun 2026) — https://arxiv.org/abs/2606.05792
- Elhemali et al., "Amazon DynamoDB: A Scalable, Predictably Performant, and Fully Managed NoSQL Database Service" (USENIX ATC 2022) — https://www.usenix.org/conference/atc22/presentation/elhemali
- Verbitski et al., "Amazon Aurora" (SIGMOD 2017) — https://www.amazon.science/publications/amazon-aurora-design-considerations-for-high-throughput-cloud-native-relational-databases
- Bornholt et al., "Using Lightweight Formal Methods to Validate a Key-Value Storage Node in Amazon S3" (SOSP 2021) — https://www.amazon.science/publications/using-lightweight-formal-methods-to-validate-a-key-value-storage-node-in-amazon-s3

_Last reviewed: 2026-10_
