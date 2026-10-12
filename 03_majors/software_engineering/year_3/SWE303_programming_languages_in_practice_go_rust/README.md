# SWE303 · Programming Languages in Practice: Go, Rust and the JVM

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L4 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md); recommended [CS216](../../../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md) and [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) | [SWE403](../../year_4/SWE403_reliability_observability_and_incident/README.md); pairs with [SWE305](../SWE305_concurrency_and_performance_engineering/README.md) |

## Why this course matters now

Most production backends, infrastructure and developer tools run on one of three families: Go (Kubernetes, Docker, Terraform), Rust (a growing share of Android, Cloudflare's Pingora proxy, AWS Firecracker) or the JVM (Java and Kotlin services at banks, e-commerce and large tech companies). Each makes different promises about memory, concurrency and failure, and those promises decide your latency tail, your security bugs and your on-call nights. Google reported in November 2025 that memory-safety vulnerabilities fell below 20% of Android's total for the first time, with Rust code showing roughly a 1,000× lower memory-safety vulnerability density than Android's C and C++, a 4× lower rollback rate, and about 25% less time in code review. Coding agents write fluent Go, Java and Rust, but the runtime semantics are where they and their users go wrong: goroutine leaks, data races, `unwrap()` in a hot path, `Arc<Mutex<…>>` everywhere, virtual threads pinned or starved. This course makes you productive in all three, able to read and debug their runtimes, and able to choose between them with evidence instead of fashion.

## Learning outcomes

By the end you can:

1. **Compare** the memory-management and concurrency models of Go, Rust and the JVM, and **predict** how each behaves under load, in a container and during failure.
2. **Write** idiomatic, tested Go: small interfaces, errors as values, `context` cancellation, `errgroup`, and race-free concurrency verified with `-race`.
3. **Write** idiomatic Rust: ownership and borrowing without fighting the compiler, `Result`-based errors, traits and generics, and async code on Tokio that is cancellation-safe.
4. **Explain** the Java Memory Model (happens-before, `volatile`, final fields) and **tune** a JVM service's garbage collector with evidence from GC logs and JFR.
5. **Use** virtual threads, scoped values and structured concurrency correctly, and **diagnose** pinning and resource starvation.
6. **Profile** each runtime (`pprof` and the execution tracer, `perf`/`cargo flamegraph`, async-profiler and JFR) and **fix** the hot spot.
7. **Build** interop across languages: cgo, Rust FFI with `bindgen`/`cbindgen`, PyO3 extensions, Java's Foreign Function and Memory API, and gRPC.
8. **Choose** a language for a component with a written decision covering latency, memory, safety, team skills, hiring and operations.

## Chapters and lessons

### Chapter 1 · Languages as engineering decisions (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Runtime models | Ahead-of-time native code, managed runtimes with JIT, interpreters; startup, peak performance and footprint | Measure startup time, RSS and peak throughput of a "hello HTTP" in Go, Rust and Java 25 |
| 1.2 Memory-management spectrum | Manual, ownership, reference counting, tracing GC; pause vs throughput trade-offs | Allocate 10⁷ small objects in each; plot latency of a concurrent request stream |
| 1.3 Concurrency models | OS threads, goroutines (M:N), async/await state machines, virtual threads | Run 100,000 concurrent sleeping tasks in each model; record memory |
| 1.4 Case studies | Discord moving a service from Go to Rust over GC latency spikes (2020); Android's Rust adoption data (2025); Uber's study of data races in 46 million lines of Go (PLDI 2022) | Write a one-page brief per case: problem, evidence, decision, what you would ask |

**Check your understanding:** Why can a language with a faster benchmark lose in production? What evidence did Discord use, and what would have made it insufficient? Why did Uber find so many data races in a language with channels?

### Chapter 2 · Go I: the language and its idioms (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Types and interfaces | Structs, methods, implicit interface satisfaction; small interfaces (`io.Reader`); accept interfaces, return structs | Implement a streaming CSV-to-JSON converter on `io.Reader`/`io.Writer` |
| 2.2 Errors as values | Wrapping with `%w`, `errors.Is`/`errors.As`, sentinel vs typed errors | Add context to every error path in a provided service; test with `errors.Is` |
| 2.3 Generics | Type parameters and constraints (Go 1.18); generic methods (new in Go 1.27, Aug 2026) | Write a generic LRU cache; compare with an `any`-based version |
| 2.4 Tooling | Modules, `go vet`, staticcheck, table-driven tests, fuzzing with `go test -fuzz`, `go fix` modernizers | Fuzz a URL parser until you find a crash or prove 10 minutes without one |

**Check your understanding:** Why does Go encourage interfaces defined by the consumer? When is a sentinel error the wrong design? What did generics fix in Go, and what did they not?

### Chapter 3 · Go II: concurrency (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Goroutines, channels and `select` | Unbuffered vs buffered channels; ownership of closing; fan-out/fan-in; pipelines | Build a 3-stage pipeline with cancellation |
| 3.2 Context and cancellation | `context.Context` propagation, deadlines, `errgroup` | Cancel all in-flight work when one of 10 fetches fails |
| 3.3 The Go memory model | Happens-before (2022 revision); `sync`, `sync/atomic`; why "benign" races are not | Write a data race; catch it with `go test -race`; fix it two ways |
| 3.4 Leaks and deterministic tests | Goroutine leaks; the `goroutineleak` profile (generally available in Go 1.27); `testing/synctest` for time-dependent code | Find 3 planted leaks with the profile; make a flaky timeout test deterministic with `synctest` |

**Check your understanding:** Who should close a channel, and what happens if two goroutines try? Why is a map read concurrently with a write a crash risk, not just a stale read? What does `context` cancellation not do for you automatically?

### Chapter 4 · Go III: the runtime in production (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The scheduler | G, M and P; work stealing; `GOMAXPROCS` and container CPU limits (container-aware since Go 1.25) | Show throttling with a CPU limit and a wrong `GOMAXPROCS` on an older Go; fix it |
| 4.2 Garbage collection | Concurrent mark-sweep; `GOGC` and `GOMEMLIMIT`; the Green Tea collector (default since Go 1.26) | Tune `GOMEMLIMIT` to stop an OOM kill in a 512 MB container |
| 4.3 Escape analysis and allocation | `-gcflags=-m`; reducing allocations in hot paths; `sync.Pool` | Cut allocations per request by half in a JSON handler; prove with benchmarks |
| 4.4 Profiling and tracing | `pprof` CPU/heap/mutex/block profiles; `go tool trace` | Diagnose a provided latency regression from a trace alone |

**Check your understanding:** Why does a Go service in a container with a 2-CPU limit misbehave if the runtime thinks it has 64 CPUs? What does `GOMEMLIMIT` trade? When does `sync.Pool` make things worse?

### Chapter 5 · Rust I: ownership and borrowing (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Ownership and moves | Single owner, `Drop`, move semantics; `Copy` vs `Clone` | Port a 200-line Python script; explain every compiler error you hit |
| 5.2 Borrowing | Shared XOR mutable references; non-lexical lifetimes; slices; `String` vs `&str` | Implement a tokenizer that returns `&str` slices into its input |
| 5.3 Lifetimes | Elision rules; lifetimes in structs; when to own instead of borrow | Fix 10 lifetime errors from a kata set without adding `.clone()` |
| 5.4 Patterns that fight the borrow checker | Graphs, self-references, observer patterns; arenas and indices as the Rust answer | Build a graph with an arena and `usize` indices; compare with `Rc<RefCell<…>>` |

**Check your understanding:** What class of bugs does "shared XOR mutable" rule out at compile time? Why is sprinkling `.clone()` a smell? When is `Rc<RefCell<T>>` the honest choice?

### Chapter 6 · Rust II: types, traits and errors (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Enums and pattern matching | Sum types; exhaustive `match`; `Option` and `Result` | Model an HTTP request parser's states as an enum |
| 6.2 Traits and generics | Static dispatch (monomorphisation) vs trait objects (`dyn Trait`); associated types; iterator adaptors as zero-cost abstractions | Benchmark generic vs `dyn` dispatch on a hot loop |
| 6.3 Error handling | `?`, `thiserror` for libraries, `anyhow` for applications; panics vs errors; Cloudflare's 18 Nov 2025 outage, where `unwrap()` on an unexpected error turned a bad config file into a global panic | Remove every `unwrap()` from a provided service; justify any that remain |
| 6.4 Smart pointers and thread safety | `Box`, `Rc`, `Arc`, `RefCell`, `Mutex`, `RwLock`; `Send` and `Sync` | Make a single-threaded cache thread-safe; explain each compiler error |

**Check your understanding:** Why did a Rust service with no memory bugs still take down traffic in November 2025? When should a library return an error and when should it panic? What do `Send` and `Sync` guarantee, and what do they not?

### Chapter 7 · Rust III: async and unsafe (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Futures as state machines | `Future`, `poll`, wakers, `Pin`; why async Rust needs an executor | Hand-write a tiny executor that runs two futures |
| 7.2 Tokio in practice | Tasks, `spawn_blocking`, channels, `select!`; async functions in traits (stable since Rust 1.75) | Build an async TCP echo server; measure 10,000 connections |
| 7.3 Cancellation and blocking | Cancellation safety in `select!`; blocking calls inside async code; back-pressure | Reproduce a lost-message bug caused by a cancelled future; fix it |
| 7.4 Unsafe and tooling | What `unsafe` permits; invariants you must uphold; Miri; the 2024 edition (Rust 1.85, Feb 2025) | Find the undefined behaviour in a provided `unsafe` block with Miri |

**Check your understanding:** Why does dropping a future cancel it, and why is that dangerous inside `select!`? What happens to a Tokio worker thread when you call blocking file I/O? What must be true for an `unsafe` block to be sound?

### Chapter 8 · JVM I: bytecode, JIT and the memory model (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 From source to machine code | Class loading, bytecode (`javap`), interpreter, tiered JIT (C1/C2), deoptimisation | Watch a method get compiled with `-XX:+PrintCompilation`; trigger a deopt |
| 8.2 Modern Java | Records, sealed types, pattern matching for `switch`; compact source files and instance main methods (JDK 25) | Rewrite a visitor-based evaluator with sealed types and `switch` patterns |
| 8.3 The Java Memory Model | Happens-before, `volatile`, `final` field semantics, safe publication; JLS chapter 17 | Reproduce an unsafe-publication bug with jcstress; fix it |
| 8.4 Benchmarking the JVM | JMH; dead-code elimination, constant folding, warm-up | Fix three broken micro-benchmarks |

**Check your understanding:** Why can a JVM benchmark without JMH report a loop as free? What does `volatile` guarantee that a plain field does not? Why does a JIT need to deoptimise?

### Chapter 9 · JVM II: garbage collection (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Generational collection | Weak generational hypothesis; young and old generations; allocation rate vs promotion rate | Read GC logs of a service; compute both rates |
| 9.2 G1, ZGC and Shenandoah | G1 regions and pause targets; generational ZGC (default ZGC mode since JDK 23); generational Shenandoah (JDK 25) | Run one service under G1 and generational ZGC; compare p99 and CPU |
| 9.3 Memory footprint | Compact object headers (JEP 519, JDK 25); heap sizing in containers (`MaxRAMPercentage`) | Measure heap savings from compact headers on an object-heavy workload |
| 9.4 JFR and diagnosis | Java Flight Recorder events, allocation profiling, JFR CPU-time profiling (experimental, JDK 25) | Find an allocation hot spot with JFR; fix and measure |

**Check your understanding:** Why does a low-pause collector usually cost more CPU? What does a rising promotion rate warn you about? Why do JVMs in containers need explicit memory settings?

### Chapter 10 · JVM III: virtual threads and structured concurrency (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Virtual threads | JEP 444 (JDK 21): mounting, unmounting and carrier threads; thread-per-request again | Convert a thread-pool HTTP client fan-out to virtual threads; measure |
| 10.2 Pinning and starvation | `synchronized` pinning before JEP 491 (fixed in JDK 24); native frames still pin; pooled resources (DB connections) as the real limit | Reproduce pinning on JDK 21, show it gone on JDK 25; then starve a connection pool |
| 10.3 Scoped values and structured concurrency | Scoped values (final in JDK 25, JEP 506); structured concurrency (still preview in JDK 25) | Replace `ThreadLocal` request context with a scoped value |
| 10.4 Choosing a JDK | LTS vs feature releases (JDK 25 is the current LTS; JDK 27 shipped on 15 Sep 2026); upgrade strategy | Write an upgrade plan from JDK 17 to 25 for a service, with risks |

**Check your understanding:** Why do virtual threads not make CPU-bound code faster? What does a database connection pool of 20 mean for 100,000 virtual threads? Why is structured concurrency about failure handling more than speed?

### Chapter 11 · Interoperability (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 The C ABI | Calling conventions, ownership across the boundary, who frees memory | Expose a Rust function with `cbindgen`; call it from C |
| 11.2 Go and Rust interop | cgo costs (baseline overhead about 30% lower in Go 1.26) and pitfalls; `bindgen` for C libraries | Measure cgo call overhead; batch calls to amortise it |
| 11.3 Rust inside Python | PyO3 and maturin; why tools like Ruff, uv and `pydantic-core` are written in Rust | Speed up a Python hot function with a PyO3 extension; measure |
| 11.4 JVM interop | JNI vs the Foreign Function and Memory API (JEP 454, final in JDK 22) | Call a C library from Java with FFM; compare code size with JNI |
| 11.5 Process-level interop | gRPC and Protocol Buffers; WebAssembly components (WASI 0.2) as a sandboxed plugin boundary | Same service called from Go, Rust and Java clients via gRPC |

**Check your understanding:** Why is an FFI boundary also a security and memory-ownership boundary? When is a separate process with gRPC better than in-process FFI? What does batching do to cgo overhead, and why?

### Chapter 12 · Choosing and migrating (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 A decision framework | Latency and memory needs, safety requirements, team skills, hiring market, ecosystem, operations | Write a language decision record for a payment-tokenisation component |
| 12.2 Memory safety as policy | CISA's "Case for Memory Safe Roadmaps" (Dec 2023); incremental adoption (new code in Rust first, as in Android) | Draft a memory-safety roadmap for a C++ codebase |
| 12.3 AI and translation | Agents translating Go ↔ Rust ↔ Java; why idiomatic translation needs tests and a human; C-to-Rust research (link to SWE402) | Have an agent port a 500-line Go module to Rust; review and fix it |
| 12.4 Capstone | The same service in all three languages, measured | P3 build, benchmark and report |

**Check your understanding:** What would make you choose Java over Rust for a latency-sensitive service? Why does "new code in memory-safe languages" reduce vulnerabilities faster than rewriting old code? What does an agent's translation usually get wrong about error handling and ownership?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Three runtimes, one workload | Case briefs |
| 2 | 2 | Lab 2 · Idiomatic Go | — |
| 3 | 3 | Lab 3 · Races and leaks | — |
| 4 | 4 | Lab 3 (cont.) · Go in a container | **P1 due** |
| 5 | 5 | Lab 4 · Borrow-checker kata | — |
| 6 | 6 | Lab 5 · No `unwrap()` | — |
| 7 | 7 | Lab 6 · Async Rust and cancellation | Mid-term (AI off): Go + Rust reading and fixing |
| 8 | 8 | Lab 7 · JMM and JMH | — |
| 9 | 9 | Lab 8 · GC shoot-out | — |
| 10 | 10 | Lab 9 · Virtual threads under load | **P2 due** |
| 11 | 11 | Lab 10 · Interop | — |
| 12 | 12 | Decision records | — |
| 13 | 12 | P3 | — |
| 14 | 12 | P3 | **P3 due** |
| 15 | Review | Oral defence | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** translating idioms you know into a language you are learning ("what is the idiomatic Go version of this Java stream?"); explaining compiler errors (especially Rust's); generating test inputs and benchmarks; drafting FFI glue; summarising GC logs and JFR recordings (then checking the numbers).
- **Do without AI (drills):** the borrow-checker kata (Lab 4); reading and explaining compiler errors aloud; the Go race and leak hunt (Lab 3); all exams. Your goal is a mental model of each runtime, and you only build it by struggling with it.
- **Verify AI output by:** `go test -race` and the `goroutineleak` profile on every Go change; `cargo clippy`, Miri and a grep for `unwrap`/`expect`/`clone` on every Rust change; jcstress for any lock-free Java; benchmarks with JMH, `go test -bench` or Criterion before accepting any performance claim; checking each JEP, Go release note or Rust feature the AI cites against the official page.
- **Where AI still fails here (show it):** Microsoft researchers reported a peak accuracy of roughly 74% for an LLM-based tool fixing real Rust compilation errors, so even the best configuration left about a quarter unresolved ([RustAssistant, 2023](https://arxiv.org/abs/2308.05177)). In Labs 3, 5 and 9 you log agent output that compiles but (a) leaks goroutines, (b) races, (c) uses `unwrap()` on fallible I/O, (d) blocks inside async code, or (e) wraps every field in `Arc<Mutex<…>>`.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| P1, P2, P3 | 10%, 15%, 25% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence | 20% |

**Mastery gate.** You pass when you can: (1) with AI off, find and fix a planted data race and a goroutine leak in a 1,500-line Go service, and a cancellation bug in a Tokio service, within 2 hours; (2) take a JVM service with a p99 latency problem and, from GC logs, JFR and an async-profiler flame graph, name the cause and cut p99 by at least 30%; (3) write and defend a one-page language decision for a component you have not seen.

## Industry reality

Where this is used (public sources): Kubernetes, Docker and Terraform are written in Go. Uber's Go monorepo held about 46 million lines when it reported over 2,000 data races found and over 1,000 fixed ([Chabbi and Ramanathan, PLDI 2022](https://arxiv.org/abs/2204.00764)). Zerodha's open-source mailing-list manager listmonk is written in Go. Android, Cloudflare's Pingora proxy and AWS Firecracker use Rust. JDK 25 (Sept 2025) is the current long-term-support Java release, and JDK 27 shipped on 15 September 2026.

**Interview questions from this course**

1. *How do goroutines differ from OS threads and from Java virtual threads?* Strong answer: M:N scheduling with growable stacks; preemption; virtual threads mount on carrier threads; both make blocking cheap but neither helps CPU-bound work; mentions pinning and resource limits.
2. *Explain Rust's borrow checker to someone who knows Java.* Strong answer: ownership and moves; shared XOR mutable references; lifetimes as scopes the compiler checks; what bugs this prevents (use-after-free, data races) and what it does not (logic bugs, panics, deadlocks).
3. *A Java service's p99 latency doubles every few minutes. How do you investigate?* Strong answer: correlate with GC logs and JFR; check allocation and promotion rates, heap sizing in the container, safepoints; try generational ZGC; confirm with a load test and flame graph before and after.
4. *When would you pick Go, Rust or Java for a new service?* Strong answer: names concrete criteria (tail-latency budget, memory, safety exposure, team skills, ecosystem, hiring); gives an example of each; acknowledges that the team's existing operational tooling often decides.
5. *What happens when you call a blocking function inside async Rust or Node code?* Strong answer: it blocks the executor thread and starves other tasks; use `spawn_blocking` or a dedicated pool; detect it with runtime metrics or tokio-console.

## Resources (free first)

- **Go:** A Tour of Go — https://go.dev/tour/ ; Effective Go — https://go.dev/doc/effective_go ; The Go Memory Model — https://go.dev/ref/mem ; Go 1.26 and 1.27 release notes — https://go.dev/doc/go1.26 , https://go.dev/doc/go1.27 ; Uber Go style guide — https://github.com/uber-go/guide
- **Rust:** *The Rust Programming Language* — https://doc.rust-lang.org/book/ ; Rustlings — https://github.com/rust-lang/rustlings ; Async Book — https://rust-lang.github.io/async-book/ ; Tokio tutorial — https://tokio.rs/tokio/tutorial ; The Rustonomicon — https://doc.rust-lang.org/nomicon/ ; Mara Bos, *Rust Atomics and Locks* (free online) — https://marabos.nl/atomics/
- **JVM:** dev.java learning — https://dev.java/learn/ ; JLS chapter 17 (threads and locks) — https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html ; Aleksey Shipilëv, JVM Anatomy Quarks — https://shipilev.net/jvm/anatomy-quarks/ ; JDK 25 JEP list — https://openjdk.org/projects/jdk/25/ ; JMH — https://github.com/openjdk/jmh ; jcstress — https://github.com/openjdk/jcstress ; async-profiler — https://github.com/async-profiler/async-profiler
- **Interop:** PyO3 — https://pyo3.rs/ ; JEP 454 (FFM API) — https://openjdk.org/jeps/454 ; gRPC — https://grpc.io/docs/
- **Practice:** Exercism Go, Rust and Java tracks — https://exercism.org/
- **Paid, optional:** Donovan and Kernighan, *The Go Programming Language*; Blandy, Orendorff and Tindall, *Programming Rust*; Gjengset, *Rust for Rustaceans*; Goetz et al., *Java Concurrency in Practice*.

## Sources

- Google, "Rust in Android: move fast and fix things" (13 Nov 2025) — https://blog.google/security/rust-in-android-move-fast-fix-things/ (checked 2026-10)
- Discord, "Why Discord is switching from Go to Rust" (Feb 2020) — https://discord.com/blog/why-discord-is-switching-from-go-to-rust (checked 2026-10)
- Chabbi and Ramanathan, "A Study of Real-World Data Races in Golang" (PLDI 2022, arXiv 2204.00764) — https://arxiv.org/abs/2204.00764 (checked 2026-10)
- Cloudflare, "Cloudflare outage on November 18, 2025" — https://blog.cloudflare.com/18-november-2025-outage/ (checked 2026-10)
- Go release history and notes (Go 1.25 Aug 2025, 1.26 Feb 2026, 1.27 Aug 2026) — https://go.dev/doc/devel/release (checked 2026-10)
- OpenJDK, JDK 25 (GA 16 Sep 2025) and JDK release list (JDK 27 GA 15 Sep 2026) — https://openjdk.org/projects/jdk/25/ , https://openjdk.org/projects/jdk/ (checked 2026-10)
- JEP 444 (Virtual Threads), JEP 491 (Synchronize Virtual Threads without Pinning), JEP 474 (ZGC generational mode by default) — https://openjdk.org/jeps/444 , https://openjdk.org/jeps/491 , https://openjdk.org/jeps/474 (checked 2026-10)
- Deligiannis et al., "Fixing Rust Compilation Errors using LLMs" (arXiv 2308.05177, 2023) — https://arxiv.org/abs/2308.05177 (checked 2026-10)
- CISA et al., "The Case for Memory Safe Roadmaps" (Dec 2023) — https://www.cisa.gov/resources-tools/resources/case-memory-safe-roadmaps (checked 2026-10)
- Cloudflare, "How we built Pingora" (Sep 2022) — https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/ (checked 2026-10)
- listmonk (Zerodha) — https://github.com/knadh/listmonk (checked 2026-10)

_Last reviewed: 2026-10_
