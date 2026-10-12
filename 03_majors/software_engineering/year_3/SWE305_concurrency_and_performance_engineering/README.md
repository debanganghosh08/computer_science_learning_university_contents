# SWE305 · Concurrency and Performance Engineering

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L4 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md); recommended [CS202](../../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md), [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md), [SWE303](../SWE303_programming_languages_in_practice_go_rust/README.md) | Recommended before [SWE401](../../year_4/SWE401_large_scale_system_design/README.md) and [SWE403](../../year_4/SWE403_reliability_observability_and_incident/README.md); deeper electives [OPS404](../../../devops_sre_platform_engineering/year_4/OPS404_performance_and_capacity_engineering/README.md), [BE402](../../../backend_engineering/year_4/BE402_scalability_and_performance_caching_sharding/README.md) |

## Why this course matters now

Performance and concurrency bugs are the defects that survive code review, pass tests, and appear only under production load: a lock that serialises a hot path, a cache line bounced between cores, a retry storm, a p99 that triples when one dependency slows down. Dean and Barroso showed in "The Tail at Scale" (2013) that when a request fans out to 100 servers, a 1-in-100 slow response on each server makes 63% of user requests slow. Netflix described a 2022 investigation where cache-line contention between CPU cores (false sharing, and true sharing inside the JVM itself), found only with hardware performance counters, held a JVM service far below its potential; the fix gave roughly a threefold improvement. Coding agents now write a lot of concurrent code and propose optimisations confidently, but concurrency errors depend on interleavings that neither the model nor a normal test run explores, and a performance claim without a measurement is a guess. This course teaches the measurement discipline (benchmarks, profilers, load models), the theory (memory models, queueing, Amdahl), and the tools (ThreadSanitizer, jcstress, loom, flame graphs, eBPF) that make you the engineer who can prove why a system is slow or wrong. CS203 taught threads, locks and deadlock; this course is about doing them fast and correctly at scale.

## Learning outcomes

By the end you can:

1. **State** performance requirements as percentiles under a defined load, and **explain** tail latency, throughput, utilisation and their relationships (Little's law, Amdahl's law, the Universal Scalability Law, M/M/1 queueing).
2. **Benchmark** correctly with JMH, `go test -bench`/benchstat, Criterion and k6 open-model tests, avoiding dead-code elimination, warm-up errors and coordinated omission.
3. **Profile** CPU, off-CPU, allocation and lock time with `perf`, flame graphs, async-profiler, `pprof` and eBPF tools, and **fix** the hot spot with a measured result.
4. **Reason** about memory models (sequential consistency, x86-TSO, ARM's weaker model, acquire/release, Java `volatile`, Go's model) using litmus tests.
5. **Reduce** lock contention (striping, read-mostly structures, sharding, batching), and **implement** basic lock-free structures with safe memory reclamation.
6. **Test** concurrent code systematically with ThreadSanitizer, the Go race detector, jcstress, loom and deterministic simulation.
7. **Build** event-driven servers on epoll or io_uring, and **compare** thread-per-request, event loop and thread-per-core designs with data.
8. **Control** tail latency with bounded queues, load shedding, adaptive concurrency limits, timeouts, retry budgets and hedged requests.
9. **Run** performance as a team practice: regression benchmarks in CI, performance budgets, and written investigation reports.

## Chapters and lessons

### Chapter 1 · Performance as an engineering discipline (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Latency, throughput, percentiles | Why averages lie; p50/p99/p99.9; latency distributions are multi-modal | Plot the latency histogram of a provided service; find its two modes |
| 1.2 The tail at scale | Fan-out amplifies tails (1 − 0.99¹⁰⁰ ≈ 63%) | Simulate fan-out of 1, 10 and 100; compare user-visible p99 |
| 1.3 Laws you will use weekly | Little's law (L = λW), Amdahl's law, Gunther's Universal Scalability Law | Fit USL to throughput measured at 1–32 threads; find the contention and coherency terms |
| 1.4 Methods | Brendan Gregg's USE method (utilisation, saturation, errors); the RED method; "measure first" | Apply USE to a slow VM; write the checklist results |

**Check your understanding:** Why can a change that improves the mean make users unhappier? What does a negative slope in the USL curve tell you physically? Why is "the CPU is at 40%" not evidence that CPU is not the bottleneck?

### Chapter 2 · The hardware underneath (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Caches and cache lines | L1/L2/L3 latencies, 64-byte lines, spatial and temporal locality, prefetching | Traverse a matrix row-wise vs column-wise; explain the gap with `perf stat` cache-miss counts |
| 2.2 False sharing | Coherence traffic (MESI); padding and `@Contended`; Netflix's 2022 case | Reproduce false sharing between two counters; fix with padding; measure |
| 2.3 Branches and SIMD | Branch prediction and misprediction cost; vectorisation | Sorted vs unsorted data in a branchy loop; branchless rewrite |
| 2.4 Data-oriented design | Array of structs vs struct of arrays; pointer chasing; NUMA effects | Convert an object-per-particle simulation to SoA; measure |

**Check your understanding:** Why can two threads that never touch the same variable slow each other down? When does a linked list beat an array in practice, if ever? What hardware counter would you read first for a memory-bound loop?

### Chapter 3 · Benchmarking discipline (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Microbenchmarks | JMH, `testing.B`, Criterion, Google Benchmark; warm-up, dead-code elimination, constant folding, blackholes | Fix 5 broken microbenchmarks across 3 languages |
| 3.2 Statistics for benchmarks | Variance, confidence intervals, benchstat; CPU frequency scaling, turbo and noisy neighbours | Report a 3% improvement with an interval, or show it is noise |
| 3.3 Load-testing models | Closed vs open workload models; coordinated omission (Gil Tene); constant-arrival-rate tests in k6 or wrk2; HdrHistogram | Measure one service with a closed and an open model; explain the p99 difference |
| 3.4 Realistic workloads | Production-like key distributions (Zipf), payload sizes, think time; replaying traces | Benchmark a cache with uniform vs Zipf keys; compare hit rates |

**Check your understanding:** How does a closed-loop load generator hide latency spikes? Why is a benchmark with uniformly random keys optimistic for most caches? What makes a 2% difference believable?

### Chapter 4 · Profiling (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Sampling profilers | `perf record`, stack walking, symbols, frame pointers vs DWARF | Profile a C and a Go program; fix missing frames |
| 4.2 Flame graphs | Reading width and height; differential flame graphs; icicle views | Find the hot path in 3 provided flame graphs; verify with a fix |
| 4.3 Runtime profilers | async-profiler (CPU, allocation, lock and wall-clock modes), JFR, `pprof`, py-spy | Wall-clock profile a service that is slow but not CPU-bound |
| 4.4 Off-CPU and eBPF | Off-CPU analysis; bpftrace and BCC tools (`offcputime`, `runqlat`, `biolatency`) | Find a lock wait and a disk wait with off-CPU flame graphs |
| 4.5 Continuous profiling | Always-on low-overhead profiling (Parca, Grafana Pyroscope); comparing deploys | Compare profiles before and after a planted regression |

**Check your understanding:** Why does a CPU flame graph show nothing useful for a service waiting on a database? What is profiling overhead, and how do sampling profilers keep it low? When would you need frame pointers turned on in production builds?

### Chapter 5 · Memory models (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Why reordering happens | Compiler reordering, store buffers, out-of-order execution | Run the store-buffering litmus test on x86; observe "impossible" results |
| 5.2 Hardware models | Sequential consistency, x86-TSO, ARM's weaker ordering | Run the message-passing litmus test on x86 and ARM (a cloud ARM VM or Apple silicon) |
| 5.3 Language models | C++/Rust atomics (`Relaxed`, `Acquire`, `Release`, `AcqRel`, `SeqCst`); Java `volatile` and `VarHandle`; the Go memory model | Implement a one-shot flag with the weakest correct ordering in Rust; justify it |
| 5.4 Data races vs race conditions | Undefined behaviour in C/C++, defined but surprising in Java and Go; high-level races without data races | Write a race condition with no data race (check-then-act on a concurrent map) |

**Check your understanding:** Why does code that works on x86 fail on ARM? What does an acquire load pair with, and what does the pair guarantee? Why is "use `SeqCst` everywhere" safe but sometimes slow?

### Chapter 6 · Locks under contention (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 How locks work | Futex-based mutexes, spinning then parking, fairness vs throughput | Measure an uncontended vs contended lock acquisition |
| 6.2 Measuring contention | Lock profiling (async-profiler lock mode, Go mutex profile, `perf lock`) | Find the hottest lock in a provided service |
| 6.3 Reducing contention | Lock striping, sharded counters (`LongAdder`), read-copy-update ideas, batching, per-core structures | Replace a global counter and a global map lock; measure scaling to 32 threads |
| 6.4 Reader-writer locks and their traps | Writer starvation; when RW locks are slower than mutexes | Benchmark RW vs plain mutex at 99%, 90% and 50% reads |
| 6.5 Correctness under change | Lock ordering, lock hierarchies, deadlock detection in tests | Add a lock-order checker to a test suite; trigger it |

**Check your understanding:** Why can a fair lock reduce throughput? When does sharding a counter give wrong answers? What is the cheapest way to prove you have a contention problem rather than a CPU problem?

### Chapter 7 · Lock-free basics (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Compare-and-swap | CAS loops, progress guarantees (lock-free, wait-free, obstruction-free) | Lock-free counter and Treiber stack in Rust or Java |
| 7.2 ABA and reclamation | The ABA problem; tagged pointers; hazard pointers; epoch-based reclamation (crossbeam-epoch); RCU in Linux | Reproduce ABA in a test; fix with epochs |
| 7.3 Queues | Michael–Scott queue; single-producer single-consumer ring buffers; the LMAX Disruptor | SPSC ring buffer; measure against a locked queue |
| 7.4 When not to | Complexity, verification cost, and the cases where a well-sharded lock wins | Write a one-page "should we go lock-free?" decision for a provided case |

**Check your understanding:** Why does garbage collection make some lock-free structures easier in Java than in Rust or C++? What does ABA break, concretely? Why might a lock-free queue be slower than a mutex-protected one?

### Chapter 8 · Testing and verifying concurrent code (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Dynamic race detection | ThreadSanitizer, Go race detector: happens-before tracking, overhead, coverage limits | Run TSan on a C++ project and `-race` on a Go project; triage reports |
| 8.2 Stress and litmus testing | jcstress for Java; stress harnesses with random delays | Find a publication bug with jcstress |
| 8.3 Model checking | loom (Rust) explores interleavings exhaustively for small cases | Verify your Chapter 7 queue with loom; find a planted bug |
| 8.4 Deterministic simulation | Single-threaded simulation of a concurrent/distributed system with seeded randomness (FoundationDB, TigerBeetle) | Build a tiny deterministic simulator for a 2-worker job queue; replay a failing seed |
| 8.5 Specifying with TLA+ | Model a concurrent algorithm; check invariants with TLC (Amazon's use of TLA+, CACM 2015) | Specify and check a bounded buffer in TLA+ |

**Check your understanding:** Why does a passing race-detector run not prove absence of races? What does deterministic simulation buy you that stress testing does not? When is a TLA+ model worth its cost?

### Chapter 9 · Async I/O and server architectures (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Blocking vs non-blocking | `select`, `poll`, `epoll`, `kqueue`; edge vs level triggering | Write an epoll echo server in C or Rust |
| 9.2 io_uring | Submission and completion rings; batching syscalls; when it helps | Compare epoll and io_uring file and network throughput |
| 9.3 Runtime designs | Reactor (Node, Netty, Tokio) vs thread-per-request (virtual threads) vs thread-per-core (Seastar) | Same echo service in 3 designs; measure p99 at 50k connections |
| 9.4 Back-pressure | Bounded buffers, flow control, `Retry-After`, pausing reads | Show unbounded memory growth without back-pressure; fix it |

**Check your understanding:** Why does one slow callback hurt every connection in an event loop? When does thread-per-core beat a work-stealing runtime? What is back-pressure, physically, in a TCP server?

### Chapter 10 · Parallelism for throughput (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Work stealing | Fork/join (Java ForkJoinPool), Rayon, Go's scheduler | Parallel merge sort; plot speedup and efficiency to 32 cores |
| 10.2 Granularity and overhead | Task size vs scheduling cost; sequential cut-off | Find the cut-off that maximises speedup |
| 10.3 Vectorisation and batch processing | Auto-vectorisation, SIMD intrinsics basics, columnar processing | Vectorise a checksum or filter; check the generated assembly |
| 10.4 Amdahl in real code | Serial fractions hiding in I/O, allocation and logging | Measure the serial fraction of a "parallel" pipeline; remove one |

**Check your understanding:** Why does doubling cores rarely double throughput? What sets the minimum useful task size? Where do serial fractions hide in typical service code?

### Chapter 11 · Queues, overload and tail latency (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Queueing theory you can use | M/M/1: waiting time grows as 1/(1 − ρ); why 80% utilisation already hurts | Simulate utilisation 50–95%; compare with the formula |
| 11.2 Overload control | Bounded queues, load shedding, priority admission, adaptive concurrency limits (Netflix's concurrency-limits library) | Make a service keep its goodput at 3× offered load |
| 11.3 Timeouts and retries | Deadline propagation, retry budgets, jittered exponential backoff; retry storms (the Google Cloud June 2025 incident lacked randomised backoff during recovery) | Show a retry storm in a 3-service chain; fix with budgets and jitter |
| 11.4 Hedged and tied requests | Hedging after the p95; cancellation of the loser; cost | Add hedging to a fan-out; measure p99 and extra load |
| 11.5 Burst workloads | Flash sales, ticket openings (IRCTC's record is 28,434 tickets booked in one minute, 12 Nov 2022), market opens | Model a 10-second burst with a token bucket and a queue; choose limits |

**Check your understanding:** Why does latency explode before utilisation reaches 100%? What is a retry budget, and why does it protect a recovering service? When does hedging make overall load worse than the latency it saves?

### Chapter 12 · Performance in a team (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Regression testing | Benchmarks in CI with noise-aware thresholds; dedicated runners | Add a benchmark gate that catches a planted 10% regression and ignores noise |
| 12.2 Budgets and ownership | Latency budgets per hop; allocation budgets; who owns the p99 | Write a latency budget for a 4-service request path |
| 12.3 Investigation reports | Hypothesis → measurement → change → result; reproducible notebooks | Write the P3 investigation report |
| 12.4 AI in performance work | Agents that read profiles and propose optimisations; checking every claim with a benchmark | Give an agent a flame graph; accept only changes that survive benchstat |

**Check your understanding:** Why do performance regressions usually arrive as many small slowdowns? How do you set a benchmark threshold that is not noise? What evidence should an agent's "this is 2× faster" claim carry before review?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Percentiles, fan-out and USL | — |
| 2 | 2 | Lab 2 · Caches and false sharing | — |
| 3 | 3 | Lab 3 · Broken benchmarks | **P1 due** |
| 4 | 4 | Lab 4 · Flame graphs and off-CPU | — |
| 5 | 5 | Lab 5 · Litmus tests on x86 and ARM | — |
| 6 | 6 | Lab 6 · Contention | — |
| 7 | 7 | Lab 6 (cont.) · Lock-free with reclamation | Mid-term (AI off) |
| 8 | 8 | Lab 7 · TSan, jcstress, loom, TLA+ | — |
| 9 | 9 | Lab 8 · epoll vs io_uring vs threads | — |
| 10 | 10 | Lab 9 · Parallel speedup | **P2 due** |
| 11 | 11 | Lab 10 · Overload and retries | — |
| 12 | 11 | Lab 10 (cont.) · Bursts and hedging | — |
| 13 | 12 | P3 | — |
| 14 | 12 | P3 | **P3 due** |
| 15 | Review | Oral defence | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining unfamiliar profiler output and hardware counters; drafting benchmark harnesses and load scripts (then fixing their flaws); generating litmus tests and stress harnesses; translating an optimisation idea into another language; reading long GC or `perf` outputs for candidates to investigate.
- **Do without AI (drills):** the Little's law, Amdahl and M/M/1 calculations; reading flame graphs aloud; choosing atomic orderings and justifying them; the mid-term and final. These are the reasoning skills you use to judge every suggestion.
- **Verify AI output by:** a benchmark with confidence intervals for every performance claim; TSan, `-race`, jcstress or loom for every concurrent change; checking assembly for claimed vectorisation; load tests with an open workload model for any latency claim.
- **Where AI still fails here (show it):** in Labs 3, 5 and 6 and in the Chapter 12 agent exercise you log agent output that (a) benchmarks code the compiler deleted, (b) uses `Relaxed` ordering where acquire/release is needed (find it with loom or a litmus test), (c) "optimises" a function that the profile shows is not hot, or (d) fixes a latency problem by adding an unbounded queue. Grade is on the evidence, not the count.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| P1, P2, P3 | 10%, 15%, 25% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can: (1) take a service that misses its p99 target and, within one working day, find the cause with profiles and an open-model load test, fix it, and show the p99 meets target with a reproducible report; (2) find a planted memory-ordering bug in a 300-line lock-free structure using loom, jcstress or TSan within 2 hours; (3) with AI off, compute queueing delays, Amdahl speedups and fan-out tail probabilities for a case you have not seen, and choose overload controls with justification.

## Industry reality

Where this is used (public sources): Google's "The Tail at Scale" (CACM, 2013) shaped how large services handle fan-out latency. Netflix published its hardware-counter investigation of cache-line sharing in a JVM service (2022). Amazon Web Services reported using TLA+ to find subtle bugs in systems such as DynamoDB and S3 (Newcombe et al., CACM 2015). The LMAX exchange's Disruptor processed about 6 million orders per second on a single thread, as described in Fowler's 2011 article. Google Cloud's June 2025 incident report lists missing randomised exponential backoff as a cause of slow recovery in one region.

**Interview questions from this course**

1. *Implement a thread-safe bounded blocking queue.* Strong answer: lock plus two condition variables (or semaphores); handles spurious wake-ups with `while` loops; discusses fairness, timeouts and a lock-free SPSC alternative; tests with many producers and consumers and an invariant check.
2. *Our service got 2× slower after a deploy. Walk me through the investigation.* Strong answer: confirm with metrics and percentiles; compare continuous profiles or flame graphs before and after; check off-CPU time, GC, locks and dependencies; bisect the deploy; fix and confirm with a load test.
3. *What is false sharing and how do you detect it?* Strong answer: independent variables on one cache line cause coherence traffic; detect with hardware counters (`perf c2c`) and a scaling test; fix with padding or per-thread data.
4. *Why is p99 more important than average latency for a service called by many others?* Strong answer: fan-out multiplies tail probability; users experience the slowest dependency; averages hide multi-modal distributions; mentions hedging, timeouts and budgets.
5. *How do you benchmark a change fairly?* Strong answer: realistic workload and open-model load, warm-up, repeated runs with confidence intervals, isolated machine, check for dead-code elimination, compare distributions not single numbers, record the environment.

## Resources (free first)

- **Courses:** MIT 6.172 Performance Engineering of Software Systems (Fall 2018) — https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/ ; CMU 15-418/618 Parallel Computer Architecture and Programming — https://www.cs.cmu.edu/~418/
- **Books (free):** Paul McKenney, *Is Parallel Programming Hard, And, If So, What Can You Do About It?* — https://mirrors.edge.kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.html ; Mara Bos, *Rust Atomics and Locks* — https://marabos.nl/atomics/ ; Ulrich Drepper, "What Every Programmer Should Know About Memory" — https://people.freebsd.org/~lstewart/articles/cpumemory.pdf ; Agner Fog's optimisation manuals — https://www.agner.org/optimize/
- **Methods and tools:** Brendan Gregg on flame graphs — https://www.brendangregg.com/flamegraphs.html and the USE method — https://www.brendangregg.com/usemethod.html ; perf wiki — https://perf.wiki.kernel.org/ ; bpftrace — https://github.com/bpftrace/bpftrace ; async-profiler — https://github.com/async-profiler/async-profiler ; JMH — https://github.com/openjdk/jmh ; jcstress — https://github.com/openjdk/jcstress ; loom — https://github.com/tokio-rs/loom ; ThreadSanitizer — https://clang.llvm.org/docs/ThreadSanitizer.html ; HdrHistogram — https://hdrhistogram.org/ ; k6 — https://grafana.com/docs/k6/latest/ ; Netflix concurrency-limits — https://github.com/Netflix/concurrency-limits ; Jens Axboe, "Efficient IO with io_uring" — https://kernel.dk/io_uring.pdf ; TLA+ — https://lamport.azurewebsites.net/tla/tla.html
- **Papers and articles:** Dean and Barroso, "The Tail at Scale" — https://research.google/pubs/the-tail-at-scale/ ; Newcombe et al., "How Amazon Web Services Uses Formal Methods" — https://cacm.acm.org/research/how-amazon-web-services-uses-formal-methods/ ; Martin Fowler, "The LMAX Architecture" — https://martinfowler.com/articles/lmax.html ; Preshing on Programming (memory ordering) — https://preshing.com/
- **Paid, optional:** Gregg, *Systems Performance* (2nd ed.); Herlihy, Shavit, Luchangco and Spear, *The Art of Multiprocessor Programming* (2nd ed.); Goetz et al., *Java Concurrency in Practice*.

## Sources

- Dean and Barroso, "The Tail at Scale", CACM 56(2), 2013 — https://research.google/pubs/the-tail-at-scale/ (checked 2026-10)
- Netflix Technology Blog, "Seeing through hardware counters: a journey to threefold performance increase" (Nov 2022) — https://netflixtechblog.com/seeing-through-hardware-counters-a-journey-to-threefold-performance-increase-2721924a2822 (checked 2026-10)
- Newcombe et al., CACM 58(4), 2015 — https://cacm.acm.org/research/how-amazon-web-services-uses-formal-methods/ (checked 2026-10)
- Martin Fowler, "The LMAX Architecture" (Jul 2011) — https://martinfowler.com/articles/lmax.html (checked 2026-10)
- Google Cloud, Service Control incident report (12 Jun 2025) — https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW (checked 2026-10)
- IRCTC, Internet Ticketing (record of 28,434 tickets per minute on 12 Nov 2022) — https://www.irctc.com/internet-ticketing.php (checked 2026-10)

_Last reviewed: 2026-10_
