# SWE302 · Low-Level Design and Clean Code at Scale

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L4 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) | [SWE402](../../year_4/SWE402_legacy_modernization_and_refactoring_with_ai/README.md); supports [CAR401](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) LLD rounds |

## Why this course matters now

Low-level design (LLD) is the craft of turning a feature into classes, interfaces, state machines and method signatures that stay correct when requirements change and when many people (and agents) edit them. In India, many product-company interview loops include a dedicated LLD or machine-coding round, and system-design rounds assume it ([SWE market page](../../../../06_career_and_market_readiness/01_market_map/roles/SWE_software_engineering.md)). On the job, coding agents (Claude Code, OpenAI Codex, Cursor, GitHub Copilot) now produce working code faster than any person, and AI code reviewers comment on every pull request. That makes two human skills more valuable, not less: modelling a problem so that illegal states cannot exist, and reading a diff fast enough to tell good structure from plausible structure. In the 2026 Stack Overflow survey, only 6.6% of developers trust AI output for important decisions; the rest verify. This course trains the design taste and the review discipline that verification needs, at the scale of codebases with millions of lines and hundreds of contributors.

## Learning outcomes

By the end you can:

1. **Model** a problem as objects, value types and state machines, and **make** illegal states unrepresentable with types.
2. **Apply** SOLID where it pays, **recognise** where it adds cost, and **explain** both with code.
3. **Design** method signatures, error handling (exceptions vs result types) and null handling that callers cannot misuse.
4. **Solve** classic LLD problems (parking lot, rate limiter, Splitwise, elevator, BookMyShow-style seat locking, LRU cache) in 45–90 minutes with working, tested, thread-safe code.
5. **Refactor** with Fowler's catalogue in small, behaviour-preserving steps, and **name** the smell each step removes.
6. **Measure** complexity (cyclomatic, cognitive) and duplication, and **explain** why no metric fully captures readability.
7. **Review** code at scale: stacked changes, review checklists, CODEOWNERS, readability standards, and AI-generated pull requests.
8. **Run** large-scale mechanical changes with codemods (OpenRewrite, jscodeshift) and coding agents, with verification.

## Chapters and lessons

### Chapter 1 · From requirements to an object model (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Responsibilities, not nouns | CRC cards; why "underline the nouns" produces anaemic models; tell-don't-ask | CRC session for a metro smart-card top-up kiosk |
| 1.2 Value objects and entities | Equality by value vs identity; immutability; `record` in Java, `@dataclass(frozen=True)` in Python, `readonly` in TypeScript | Replace 5 primitives (`String phone`, `long paise`) with value objects; count bugs the compiler now catches |
| 1.3 Invariants and encapsulation | Constructors that cannot build invalid objects; private state; defensive copies | Break a `DateRange` class three ways; fix each with encapsulation |
| 1.4 Just-enough UML | Class, sequence and state diagrams for discussion, not documentation | Draw the state diagram of a food-delivery order with 9 states |
| 1.5 Composition over inheritance | Fragile base class; delegation; when inheritance is right (closed hierarchies) | Refactor a 3-level inheritance tree to composition; compare change cost for a new variant |

**Check your understanding:** Why does an object with only getters and setters push logic into every caller? Which bugs disappear when money is a value type instead of a `double`? When is inheritance still the best tool?

### Chapter 2 · SOLID in practice (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Single responsibility | "One reason to change" as "one actor who asks for changes"; cohesion | Split a 600-line `InvoiceService` by actor (finance, tax, notifications) |
| 2.2 Open–closed | Extension points through strategy and plugins; the cost of premature extension points | Add a new tax rule (GST slab change) without editing existing classes, then judge whether it was worth it |
| 2.3 Liskov substitution | Behavioural subtyping; the JDK's "optional operations" (`Collections.unmodifiableList(...).add` throws) as a real violation | Write a contract test suite every `List` implementation must pass; run it on an unmodifiable list |
| 2.4 Interface segregation and dependency inversion | Role interfaces; depending on abstractions the client owns | Shrink a 14-method repository interface into role interfaces |
| 2.5 Where SOLID hurts | Indirection cost; Dan North's CUPID critique; the Ousterhout–Martin debate on function size | Take one position in the debate; defend it with code from this course |

**Check your understanding:** Why is "a class should do one thing" a weaker rule than "one actor per class"? Give a Liskov violation that compiles and passes unit tests. When does dependency inversion make code harder for a newcomer to follow?

### Chapter 3 · Signatures, errors and types (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Parse, don't validate | Turning unchecked input into typed values at the edge (Alexis King, 2019) | Replace scattered `if (pin.length != 6)` checks with a `PinCode` type |
| 3.2 Illegal states unrepresentable | Sum types and sealed hierarchies instead of flags; Java sealed interfaces, TypeScript discriminated unions, Rust enums | Model a payment's states so "refunded but never captured" cannot compile |
| 3.3 Errors as part of the API | Checked vs unchecked exceptions; result types; error taxonomies; never swallowing | Design the error type for a bank-transfer call with retryable and terminal errors |
| 3.4 Null safety | `Optional`, Kotlin nullability, TypeScript `strictNullChecks`; null as a missing case in a sum type | Turn on `strictNullChecks` in a 5k-line TS project; fix and classify the errors |
| 3.5 Designing for the caller | Argument order, boolean parameters, builders, named parameters; API evolution inside a codebase | Rewrite 10 confusing signatures from an open-source repo; justify each |

**Check your understanding:** Why are boolean parameters a design smell? What does a result type force callers to do that an unchecked exception does not? Where should parsing happen in a hexagonal design?

### Chapter 4 · The LLD method (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The 45-minute structure | Clarify scope; list use cases; entities and relationships; class diagram; APIs; key algorithms; concurrency; extensions | Time-boxed walkthrough of a library management system |
| 4.2 Machine-coding rounds | 90–120 minutes, runnable code, tests, in-memory storage; what evaluators look for (separation, extensibility, correctness) | 90-minute snake-and-ladder or cab-booking machine-coding drill |
| 4.3 Parking lot | Spot types, allocation strategy, tickets, fees as strategy, multiple entry gates and concurrent allocation | Implement with a thread-safe allocator; 1,000 concurrent arrivals, no double allocation |
| 4.4 Communicating a design | Narrating trade-offs; when to stop extending | Record yourself; score against a rubric with a peer |

**Check your understanding:** What do you ask in the first five minutes, and why? Where is the concurrency in a parking lot with four gates? Which extension request should you refuse to design for in the first version?

### Chapter 5 · LLD problems I: rate limiter, caches, logging (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Rate limiter | Token bucket, leaky bucket, fixed window, sliding log, sliding window counter; burst vs smoothness; clock injection for tests | Implement all five; property-test that no window exceeds the limit |
| 5.2 Thread-safe rate limiting | Lock per key, `ConcurrentHashMap.compute`, atomic counters; contention | Benchmark 1 vs 64 threads with JMH; explain the curve |
| 5.3 LRU and LFU caches | Hash map + doubly linked list; LFU with frequency buckets in O(1); TTL | O(1) LFU; verify against a slow reference with random operations |
| 5.4 Logging and notification frameworks | Chain of responsibility, observer, async appenders, back-pressure | Logger with levels, sinks and a bounded async queue that drops with a counter |

**Check your understanding:** Which rate-limiting algorithm lets a client send twice the limit at a window edge, and why? Why must a rate limiter take a clock as a dependency? What should a logger do when its queue is full?

### Chapter 6 · LLD problems II: money, elevators and seats (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Splitwise | Expenses, splits (equal, exact, percentage), balances; money in integer paise; rounding rules | Implement with exact split rounding that always sums to the total |
| 6.2 Simplifying debts | Net balances; greedy settlement in at most n−1 transfers; minimum number of transfers is NP-hard (link to [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md)) | Greedy vs exact (bitmask DP for n ≤ 15); measure the gap |
| 6.3 Elevator system | State machine per car; SCAN/LOOK scheduling; dispatching requests across cars; simulation | Simulate 4 cars, 20 floors, morning-rush traffic; report average wait |
| 6.4 Seat booking (BookMyShow-style) | Seat holds with TTL; pessimistic locking (`SELECT … FOR UPDATE`) vs optimistic versioning vs a conditional update; idempotent confirm | 1,000 concurrent clients, 100 seats; prove zero double-booking |
| 6.5 Vending machine and other state machines | State pattern vs transition tables; invalid transitions as errors | Implement with a transition table; generate all paths in tests |

**Check your understanding:** Why is "minimise the number of transfers" a different problem from "settle all debts"? What happens to seat holds when the payment callback arrives after the TTL? Why does a transition table make an elevator easier to test than nested `if` statements?

### Chapter 7 · The refactoring catalogue (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Smells | Long function, feature envy, shotgun surgery, divergent change, primitive obsession, data clumps, speculative generality | Tag 30 smells in a provided legacy module |
| 7.2 Core refactorings | Extract/inline function, move function, introduce parameter object, replace primitive with object, split phase, encapsulate collection | Gilded Rose kata in 25+ green-to-green commits |
| 7.3 Conditionals and polymorphism | Replace conditional with polymorphism; guard clauses; decompose conditional | Remove a 12-branch `switch` on order type |
| 7.4 Tool-driven vs AI-driven refactoring | IDE refactorings are behaviour-preserving by construction; agent refactorings are not; tests as the safety net | Same refactor by IDE and by an agent; diff behaviour with a characterisation test |

**Check your understanding:** Why are small steps faster than big ones in refactoring? Which smell does "shotgun surgery" indicate about module boundaries? What can an IDE refactoring guarantee that an agent cannot?

### Chapter 8 · Readability and complexity metrics (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Cyclomatic complexity | McCabe (1976): independent paths, test-case lower bound | Compute by hand for 5 functions; check with a tool |
| 8.2 Cognitive complexity | SonarSource's 2017 metric: nesting penalties, why `switch` scores lower than nested `if` | Rank 10 functions by both metrics; explain disagreements |
| 8.3 What research says | Buse and Weimer (2010) readability model; Scalabrino et al. (2017) found the metrics they studied captured understandability poorly | Readability survey on 10 snippets with classmates; correlate with metrics |
| 8.4 Duplication and naming | Clone detection (PMD CPD, jscpd); naming as design | Measure duplication before and after an agent-written feature |

**Check your understanding:** Why can a function with low cyclomatic complexity still be hard to read? When should a team gate merges on a metric, and when only report it? What does rising duplication after agent adoption tell you?

### Chapter 9 · Code review at scale (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 What review is really for | Bacchelli and Bird (2013): reviewers expect to find defects but most value is knowledge transfer and alternative solutions; Google's code-review case study (Sadowski et al., 2018) | Classify 50 real review comments from an open-source repo |
| 9.2 Readability as a credential | Google's readability process (*Software Engineering at Google*, ch. 3); style guides as shared memory | Write a 1-page style addendum for your team's language |
| 9.3 Reviewable changes | Stacked diffs (Sapling, Graphite, Gerrit); 200–400 lines per review session; splitting refactors from behaviour changes | Split a 1,200-line branch into 5 stacked, independently reviewable changes |
| 9.4 Review operations | CODEOWNERS, review load balancing, latency targets, comment severity labels | Measure review latency and load from a public repo's PR data |

**Check your understanding:** If most review value is knowledge transfer, what changes when an agent wrote the code? Why separate refactoring from behaviour changes? What review latency target would you set, and what breaks if you miss it?

### Chapter 10 · Reviewing AI-generated code (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Evidence first | PR description, spec link, tests that fail before and pass after, screenshots or traces; reject PRs without evidence | Write an evidence checklist; apply it to 10 agent PRs |
| 10.2 What to look for | Duplicated helpers, swallowed errors, broad `catch`, invented APIs, unnecessary abstractions, tests that assert nothing | Find planted defects in 6 agent-written PRs |
| 10.3 AI reviewers | GitHub Copilot code review, Claude Code's GitHub code review, and similar tools: what they flag and miss | Run two AI reviewers and yourself on the same 5 PRs; build a confusion matrix |
| 10.4 Review policies for teams | Who approves agent PRs; size limits; required tests; "author must explain every line" rule | Draft a review policy for a 10-person team using agents daily |

**Check your understanding:** Why is "the AI reviewer found nothing" weak evidence? Which defect classes did your human review catch that the AI reviewers missed, and vice versa? What should a reviewer do with a 2,000-line agent PR?

### Chapter 11 · Clean code at the scale of thousands of engineers (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Formatters, linters and style guides | Google style guides, Uber Go style guide; automate every rule a machine can check | Configure formatter + linter + pre-commit for a polyglot repo |
| 11.2 Large-scale changes | Google's LSC process and tooling (*Software Engineering at Google*, ch. 22); sharding changes; global approvers | Plan an API rename across 300 call sites as sharded changes |
| 11.3 Codemods | OpenRewrite recipes (Java), jscodeshift and ts-morph (TypeScript), ast-grep (many languages) | Write a codemod that replaces a deprecated logging API; run it on an open-source repo |
| 11.4 Agents for mechanical change | Agent + codemod hybrids; verifying with compilation, tests and diff sampling | Same migration by codemod and by an agent; compare correctness and review time |
| 11.5 Keeping quality from drifting | Ratchets (never let a metric get worse), baseline files, quality dashboards | Add a ratchet on cognitive complexity to CI |

**Check your understanding:** When is a codemod better than an agent, and when is the reverse true? Why does a ratchet work better than a hard threshold on a legacy codebase? What makes a large-scale change safe to approve without reading every file?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Value objects, invariants and types | — |
| 2 | 2 | Lab 2 · SOLID and its costs | — |
| 3 | 3 | Lab 1 (cont.) · Types that forbid bugs | **P1 due** |
| 4 | 4 | Lab 3 · Parking lot, timed | — |
| 5 | 5 | Lab 4 · Rate limiters and caches | — |
| 6 | 6 | Lab 5 · Splitwise and elevator | Mock LLD round 1 |
| 7 | 6 | Lab 6 · Seat locking under contention | Mid-term (AI off): 90-minute machine coding |
| 8 | 7 | Lab 7 · Gilded Rose in small steps | — |
| 9 | 8 | Lab 8 · Metrics vs human judgement | — |
| 10 | 9 | Lab 9 · Stacked changes and review | **P2 due** |
| 11 | 10 | Lab 9 (cont.) · AI-PR review gauntlet | Review policy |
| 12 | 11 | Lab 10 · Codemod vs agent | — |
| 13 | 11 | P3 | Mock LLD round 2 |
| 14 | 11 | P3 | **P3 due** |
| 15 | Review | Oral review of P3 | Final exam (AI off): LLD + review |

## Working with AI in this course

- **Use AI for:** generating random operation sequences and reference implementations for property tests; drafting codemods (then testing them); first-pass review comments; explaining an unfamiliar refactoring; producing a second LLD for comparison after you finish yours.
- **Do without AI (drills):** every timed LLD and machine-coding round; the Gilded Rose kata; CRC sessions; the human review in Lab 9 before any AI reviewer runs; the mid-term and final. Interview LLD rounds are usually AI-off, and your design taste must be your own.
- **Verify AI output by:** characterisation tests before any agent refactor; concurrency tests with many threads and a checked invariant (no double booking, totals conserved); mutation testing on the tests the agent wrote; compiling and running every API the agent claims exists; reading the full diff in stacked pieces.
- **Where AI still fails here (show it, don't assume it):** in Labs 5–6 and 9 you record cases where an agent's design (a) used floating point for money, (b) ignored concurrent access in a booking or allocation path, (c) weakened or deleted a test to make it pass, or (d) refactored in a way that changed behaviour without failing any existing test. Veracode's 2025 study found security flaws in 45% of AI-generated code samples across 80 tasks, so security review stays human-owned.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| P1, P2, P3 | 10%, 15%, 25% |
| Two mock LLD rounds (AI off) | 10% |
| Final exam (AI off): one LLD problem + one 400-line review | 20% |

**Mastery gate.** You pass when you can, with AI off: (1) solve an unseen LLD problem in 90 minutes with runnable code, at least 10 tests and a correct concurrency strategy for its shared state; (2) review a 400-line pull request (agent-written) and find at least 5 of 7 planted issues, including one concurrency bug and one test that asserts nothing, in 45 minutes; (3) refactor a 300-line legacy function to a clean design in green-to-green steps, with every step committed and tests passing.

## Industry reality

Where this is used (public sources): Google's readability certification and large-scale change process are described in *Software Engineering at Google* (free online). Google's code-review guide is public. Uber publishes its Go style guide. OpenRewrite is used for automated Java framework migrations. LLD and machine-coding rounds are a standard part of many SDE loops in India ([SWE market page](../../../../06_career_and_market_readiness/01_market_map/roles/SWE_software_engineering.md)).

**Interview questions from this course**

1. *Design a rate limiter library used by 50 services.* Strong answer: clarifies per-user vs per-key, burst behaviour and accuracy; picks token bucket or sliding window counter with reasons; thread-safe per-key state; injectable clock; memory bounds with eviction; notes the distributed variant (shared store, approximate counters) as a follow-up.
2. *Design BookMyShow seat selection so two users never get the same seat.* Strong answer: seat state machine (available, held, booked); hold with TTL; compares row locks, optimistic versions and conditional updates; idempotent confirm tied to payment; expiry job; a concurrency test with an invariant.
3. *Design Splitwise and simplify debts.* Strong answer: integer money, split strategies with exact rounding, balance ledger; greedy settlement in at most n−1 transfers; says that minimising transfers exactly is NP-hard and when an exact search is affordable.
4. *Show a Liskov substitution violation and how you'd fix it.* Strong answer: a concrete example (unmodifiable collections throwing on `add`, or a subclass that strengthens preconditions); fix by splitting interfaces or composition; contract tests to prevent recurrence.
5. *How would you review a large pull request generated by an agent?* Strong answer: demands evidence and splitting; reads tests and spec first; checks duplication, error handling, invented APIs and concurrency; runs it; the human approver owns the outcome.

## Resources (free first)

- **Books (free):** *Software Engineering at Google* — https://abseil.io/resources/swe-book ; *Game Programming Patterns* (Nystrom) — https://gameprogrammingpatterns.com/
- **Refactoring and smells:** Fowler's refactoring catalogue — https://refactoring.com/catalog/ ; Refactoring.Guru smells and refactorings — https://refactoring.guru/refactoring ; Gilded Rose kata — https://github.com/emilybache/GildedRose-Refactoring-Kata
- **Design essays:** "Parse, don't validate" — https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/ ; Dan North, "CUPID — for joyful coding" — https://dannorth.net/cupid-for-joyful-coding/ ; Ousterhout and Martin's discussion — https://github.com/johnousterhout/aposd-vs-clean-code
- **Review:** Google engineering practices — https://google.github.io/eng-practices/review/ ; Bacchelli and Bird, "Expectations, Outcomes, and Challenges of Modern Code Review" (ICSE 2013) — https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/ ; Sadowski et al., "Modern Code Review: A Case Study at Google" (ICSE-SEIP 2018) — https://research.google/pubs/modern-code-review-a-case-study-at-google/
- **Style guides:** Google — https://google.github.io/styleguide/ ; Uber Go — https://github.com/uber-go/guide
- **Metrics:** SonarSource, *Cognitive Complexity* white paper — https://www.sonarsource.com/docs/CognitiveComplexity.pdf ; jscpd — https://github.com/kucherenko/jscpd
- **Codemods:** OpenRewrite — https://docs.openrewrite.org/ ; jscodeshift — https://github.com/facebook/jscodeshift ; ast-grep — https://ast-grep.github.io/
- **LLD practice:** awesome-low-level-design — https://github.com/ashishps1/awesome-low-level-design
- **Paid, optional:** Fowler, *Refactoring* (2nd ed.); Ousterhout, *A Philosophy of Software Design*; Martin, *Clean Code* (read critically, alongside Ousterhout); Freeman and Robson, *Head First Design Patterns*; McConnell, *Code Complete*.

## Sources

- Stack Overflow, 2026 Developer Survey: AI — https://survey.stackoverflow.co/2026/ai/data (checked 2026-10)
- Veracode, 2025 GenAI Code Security Report press release (30 Jul 2025) — https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/ (checked 2026-10)
- McCabe, "A Complexity Measure", IEEE Transactions on Software Engineering SE-2(4), 1976 — https://doi.org/10.1109/TSE.1976.233837 (checked 2026-10)
- Buse and Weimer, "Learning a Metric for Code Readability", IEEE TSE 36(4), 2010 — https://doi.org/10.1109/TSE.2009.70 (checked 2026-10)
- Scalabrino et al., "Automatically Assessing Code Understandability: How Far Are We?", ASE 2017 — https://doi.org/10.1109/ASE.2017.8115654 (checked 2026-10)
- Java SE `Collection` interface documentation (optional operations) — https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html (checked 2026-10)
- Bacchelli and Bird (2013) and Sadowski et al. (2018), links above (checked 2026-10)

_Last reviewed: 2026-10_
