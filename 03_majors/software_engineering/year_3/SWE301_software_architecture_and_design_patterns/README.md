# SWE301 · Software Architecture and Design Patterns

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L4 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) | [SWE401](../../year_4/SWE401_large_scale_system_design/README.md), then [SWE501](../../year_5/SWE501_frontier_seminar_agentic_software_engineering/README.md); recommended before [SWE402](../../year_4/SWE402_legacy_modernization_and_refactoring_with_ai/README.md) and [IND401](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) |

## Why this course matters now

Architecture is the set of decisions that are expensive to change: where the boundaries are, which parts may depend on which, how data and events flow, and which quality (latency, availability, changeability, cost) wins when two collide. Coding agents such as Claude Code, OpenAI Codex, Cursor and GitHub Copilot now write much of the code inside those boundaries, and Google's DORA 2025 research describes AI as "an amplifier, magnifying an organization's existing strengths and weaknesses". Agents will happily draft a C4 diagram, an ADR or a "clean architecture" skeleton in seconds, and they reach for the patterns they saw most in training data, whether or not the forces in your system call for them. What still needs a skilled human is knowing the forces: which change is likely, which failure is unacceptable, what the team can operate, and which decision is a one-way door. CS205 introduced modules, a few patterns, hexagonal design, C4 and ADRs. This course makes you able to design, document, measure and defend an architecture, and to enforce it so that neither people nor agents erode it.

## Learning outcomes

By the end you can:

1. **Elicit** quality-attribute scenarios (stimulus, environment, response, measure) and **rank** them in a utility tree.
2. **Apply** and **reject** the Gang of Four patterns that still matter, and **explain** which ones a modern language feature replaces.
3. **Design** a domain model with aggregates, value objects and bounded contexts, and **draw** a context map with anti-corruption layers.
4. **Compare** layered, hexagonal, clean, onion and vertical-slice architectures on one codebase, with measured test cost and change cost.
5. **Build** a modular monolith whose boundaries are **enforced** in CI (ArchUnit, Spring Modulith, import-linter or dependency-cruiser), and **decide** with evidence whether to extract a service.
6. **Design** event-driven flows (notification, event-carried state, event sourcing, CQRS, sagas, outbox) and **name** the consistency each gives the user.
7. **Document** an architecture with C4 diagrams as code, an arc42 skeleton and ADRs that survive review.
8. **Run** an ATAM-lite evaluation and **produce** risks, sensitivity points and trade-off points.
9. **Measure** coupling and cohesion (Ca, Ce, instability, abstractness, distance from the main sequence, LCOM4, change coupling from Git) and **act** on the numbers.
10. **Set up** architecture guardrails that keep coding agents inside the design, and **measure** how often they would have broken it.

## Chapters and lessons

### Chapter 1 · What architecture is, and what it is for (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Structures and views | Module, component-and-connector and allocation views (Bass, Clements and Kazman); architecture as "the decisions that are hard to change" | Describe one app you use in three views on one page |
| 1.2 Quality attributes | ISO/IEC 25010:2023 qualities; six-part quality-attribute scenarios; why "fast" and "scalable" are not requirements | Write 8 scenarios for a UPI-style payment app, each with a number |
| 1.3 Architecturally significant requirements | Which requirements shape structure (regulation, peak load, team count); constraints vs drivers | Sort 20 requirements of a clinic-booking system into ASR / not ASR, defend 3 |
| 1.4 Reversibility and Conway's law | One-way and two-way doors (Amazon's 2015 and 2016 shareholder letters); Conway (1968) and the inverse Conway manoeuvre | Map a real org chart (an open-source foundation's team list) to its repo structure |

**Check your understanding:** Why is "the system must be scalable" not a usable requirement, and what would you replace it with? Which of your 8 scenarios would change the architecture if its number changed by 10×? When does Conway's law become a design tool rather than a warning?

### Chapter 2 · Design patterns that still matter (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Patterns as forces, not recipes | Intent, forces and consequences; Norvig's 1996 finding that 16 of the 23 GoF patterns are "invisible or simpler" in dynamic languages | For 6 patterns, write the language feature (first-class functions, sum types, closures) that replaces it |
| 2.2 Creational | Factory method, abstract factory, builder; dependency injection replacing singletons; why global state hurts testing and agents alike | Remove a singleton from a legacy module; show the test that became possible |
| 2.3 Structural | Adapter, decorator, facade, proxy, composite; decorator vs middleware chains | Wrap a payment gateway client with retry, timeout and logging decorators |
| 2.4 Behavioural | Strategy, observer, command, state, chain of responsibility, template method vs composition | Model a UPI collect request's lifecycle as a state machine; prove no illegal transition with a property test |
| 2.5 Visitor vs pattern matching | Double dispatch; the expression problem; sealed types and exhaustive `switch` in Java 21+, Kotlin and TypeScript discriminated unions | Implement an expression evaluator both ways; add one new operation and one new node; count files touched |
| 2.6 Pattern overuse | Speculative generality, interface-for-one-implementation, "enterprise FizzBuzz"; the cost of indirection | Ask a coding agent to "make this extensible"; delete every abstraction that has one user and measure lines removed |

**Check your understanding:** Which GoF patterns become unnecessary when functions are values, and which still earn their keep? Why does exhaustive pattern matching change the visitor trade-off? How would you show a teammate that a pattern was added too early?

### Chapter 3 · Domain modelling and enterprise patterns (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Organising domain logic | Transaction script, table module, domain model (Fowler, *PoEAA*); when each wins | Rewrite one feature from transaction script to domain model; compare test count and size |
| 3.2 Persistence patterns | Repository, unit of work, data mapper vs active record; the ORM leak | Find 3 places where an ORM entity leaks into an API response in an open-source app |
| 3.3 DDD tactical design | Entities, value objects, aggregates as consistency boundaries, domain events | Design the `Order` aggregate of a food-delivery app; list every invariant it protects |
| 3.4 DDD strategic design | Bounded contexts, ubiquitous language, context maps (customer–supplier, conformist, anti-corruption layer) | EventStorming session for a train-ticket booking flow; produce a context map |

**Check your understanding:** Why should an aggregate be small, and what goes wrong with an aggregate that spans the whole order history? When is active record the right choice? What does an anti-corruption layer protect you from when you integrate with a government or partner API?

### Chapter 4 · Layered, hexagonal, clean and vertical-slice architectures (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Layers and the dependency rule | Strict vs relaxed layering; dependency inversion at layer boundaries | Draw the actual dependency graph of a layered app; find the rule violations |
| 4.2 Hexagonal in depth | Driving vs driven ports, primary and secondary adapters (Cockburn, 2005); where transactions and authorisation live | Add a CLI and an HTTP adapter to the same core with zero core changes |
| 4.3 Clean and onion | Entities, use cases, interface adapters; what they add over hexagonal; criticism for CRUD-heavy apps | Measure files touched for one feature in a clean vs a plain layered version of the same app |
| 4.4 Vertical slices | Organising by feature instead of layer; duplication as a price worth paying | Restructure 3 features into slices; compare review diff size for a change |
| 4.5 Testing through the architecture | Testing at the port; fakes for driven adapters; contract tests on adapters | Write the use-case tests with in-memory adapters; keep the suite under 5 seconds |

**Check your understanding:** What does the dependency rule buy you in a codebase that agents edit daily? When is hexagonal architecture pure overhead? Why do vertical slices often make pull requests smaller?

### Chapter 5 · Modular monoliths and the microservices decision (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Modules with real boundaries | Public API per module, internal packages, no shared tables; Shopify's componentisation and Packwerk | Split a monolith into 4 modules with explicit public interfaces |
| 5.2 Enforcing boundaries | ArchUnit (Java), Spring Modulith, import-linter (Python), dependency-cruiser (TypeScript), Packwerk (Ruby) | Add a failing CI rule; prove it blocks a cross-module import |
| 5.3 Monolith first, and when to split | Fowler's "MonolithFirst" and "Microservice Prerequisites"; independent deployability, team autonomy, scaling profile | Score 3 split candidates against the prerequisites; argue for at most one |
| 5.4 The distributed monolith | Synchronous call chains, shared databases, lock-step deploys; availability multiplies (0.999⁵) | Compute end-to-end availability of a 5-hop call chain; redesign it |

**Check your understanding:** What does a module boundary give you that a service boundary also gives, at a fraction of the cost? Which signals in your Git history say a split is overdue? Why does a shared database make two services one system?

### Chapter 6 · Event-driven architecture (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Four meanings of "event-driven" | Event notification, event-carried state transfer, event sourcing, CQRS (Fowler, 2017) | Classify 5 real systems' event use into the four kinds |
| 6.2 Choreography vs orchestration | Sagas, compensations, process managers; visibility vs coupling | Implement an order saga both ways; inject a failure in step 3 |
| 6.3 The outbox and idempotent consumers | Dual-write problem; transactional outbox; inbox/dedup; at-least-once reality | Show a lost event without an outbox; fix it; prove with a crash test |
| 6.4 Asynchronous protocols in the wild | ONDC's Beckn-based API, where every request (`search`) is answered by a callback (`on_search`) | Read ONDC's published spec; draw the sequence for a search-to-confirm flow |
| 6.5 Consistency the user sees | Read-your-writes, pending states in the UI, schema evolution of events | Design the UI states for a payment that is "processing" for 30 seconds |

Queues, brokers and stream processing mechanics are taught in [BE304](../../../backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md); this chapter is about the design choices.

**Check your understanding:** Why does event sourcing make some questions easy (audit) and others hard (ad hoc queries)? What breaks if a consumer is not idempotent? When is choreography the wrong choice?

### Chapter 7 · Documenting architecture (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 C4 in depth | Context, container, component and code levels; dynamic and deployment diagrams; notation rules | Model an app in Structurizr DSL; render all levels from one model |
| 7.2 Diagrams as code | Structurizr, Mermaid, PlantUML; keeping diagrams in the repo and in review | Add a CI step that fails when the model references a deleted component |
| 7.3 arc42 | The 12 sections; which to fill for a small team | Write sections 1, 3, 4, 9 and 10 for P2 |
| 7.4 ADRs that last | Nygard format and MADR; status, consequences, "superseded by"; decision logs for agents | Write 4 ADRs; have a peer reverse one and supersede it properly |
| 7.5 Architecture context for agents | Architecture notes in `AGENTS.md`/`CLAUDE.md`; module maps; which rules belong in tests instead of prose | Compare an agent's output on 5 tasks with and without the module map |

**Check your understanding:** What does a C4 container diagram show that a cloud architecture diagram does not? Why is an ADR with no "consequences" section nearly useless? Which architecture rules should be prose and which should be executable?

### Chapter 8 · Trade-off analysis (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Utility trees | Ranking scenarios by business value and technical risk | Build a utility tree with stakeholders (classmates role-playing product, ops, security) |
| 8.2 ATAM-lite | Approaches, sensitivity points, trade-off points, risks and non-risks (SEI's ATAM, cut to one day) | Run ATAM-lite on another team's P2 design; deliver a 2-page report |
| 8.3 Cost and benefit | CBAM idea; cost of delay; build vs buy vs adopt open source | Price two options for search (managed vs self-hosted) for 3 years |
| 8.4 Spikes and prototypes | Retiring the riskiest assumption first; throwaway vs evolutionary prototypes | Time-box a 4-hour spike to test one risky assumption; report the number |
| 8.5 Fitness functions | Automated checks for architectural qualities (latency budgets, dependency rules, bundle size) | Add three fitness functions to CI for P2 |

**Check your understanding:** What is the difference between a sensitivity point and a trade-off point? Why do weighted decision matrices so often confirm the option the author already liked? Which quality attributes can you turn into a CI check, and which cannot be?

### Chapter 9 · Measuring structure (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Package metrics | Afferent (Ca) and efferent (Ce) coupling; instability I = Ce/(Ca + Ce); abstractness A; distance D = \|A + I − 1\| (Robert Martin) | Compute I, A and D for every package in a 50k-line Java repo; plot the main sequence |
| 9.2 Cohesion | LCOM4, cohesion as "things that change together"; god classes | Find the 5 least cohesive classes; propose splits |
| 9.3 Connascence | Static (name, type, meaning, position, algorithm) and dynamic (execution, timing, value, identity); strength, locality, degree | Rank 10 couplings in a codebase by connascence strength |
| 9.4 Change coupling and hotspots | Mining Git: files that change together, churn × complexity (Tornhill's code-maat) | Run code-maat on a real repo; find the top 3 hotspots and one hidden coupling |
| 9.5 Cycles and layering checks | Package cycles, cycle breaking by inversion or extraction | Break one package cycle; prove with the tool |

**Check your understanding:** Why is a package with I = 0 and A = 0 painful to change? What does change coupling reveal that static analysis cannot? When would you accept a known metric violation?

### Chapter 10 · Architecture when agents write the code (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Why boundaries help agents | Small modules mean small context and small diffs; DORA's AI capabilities include strong version control, small batches and quality internal platforms | Give an agent the same feature in a tangled and a modular version; compare diff size and test failures |
| 10.2 Guardrails over guidance | Executable rules (ArchUnit, import-linter), CODEOWNERS on module APIs, hooks that run checks before an agent's commit | Add a pre-commit hook that runs the boundary tests; watch an agent hit it |
| 10.3 AI as design sparring partner | Asking for 3 alternatives and the strongest case against your design; checking claims against docs | Run a design critique with two different models; list what each missed |
| 10.4 Measuring erosion | Boundary violations per 100 agent PRs; duplicate abstractions; dead interfaces | Replay 20 agent-made changes; count violations caught and missed |

**Check your understanding:** Why is "the agent read our architecture doc" weaker evidence than "the agent's PR passed the boundary tests"? Which kinds of erosion do metrics catch late? How would you decide which modules agents may change without a human architect's review?

### Chapter 11 · Evolving an architecture (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Technical debt, honestly | Fowler's debt quadrant; interest as extra effort per change, measured from hotspots | Estimate the interest on one hotspot in hours per month |
| 11.2 Changing structure safely | Branch by abstraction, parallel change (expand–migrate–contract), feature toggles for structure | Replace a persistence layer behind an abstraction without a long-lived branch |
| 11.3 Architecture reviews | Review checklists, lightweight review boards, design-doc review etiquette | Review two classmates' P3 designs; write actionable findings |
| 11.4 Presenting a decision | One-page decision memo; stating what you are giving up | Present P3 in 10 minutes to a panel that pushes back |

**Check your understanding:** Why is "rewrite it" usually a worse plan than branch by abstraction? What evidence would make you stop a planned extraction halfway? How do you present a trade-off so that a non-engineer can make the call?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Quality-attribute scenarios | Scenario set |
| 2 | 2 | Lab 2 · Patterns and their replacements | — |
| 3 | 2 | Lab 2 (cont.) | **P1 due** |
| 4 | 3 | Lab 3 · Domain model and context map | Context map |
| 5 | 4 | Lab 4 · One feature, four architectures | — |
| 6 | 5 | Lab 5 · Boundaries enforced in CI | — |
| 7 | 6 | Lab 6 · Saga and outbox | Mid-term (AI off): patterns and scenarios |
| 8 | 7 | Lab 7 · C4 as code and ADRs | — |
| 9 | 8 | Lab 8 · ATAM-lite workshop | — |
| 10 | 8 | Lab 8 (cont.) | **P2 due** + ATAM report |
| 11 | 9 | Lab 9 · Metrics and Git mining | Metrics report |
| 12 | 10 | Lab 10 · Agents vs guardrails | — |
| 13 | 11 | P3 build | — |
| 14 | 11 | P3 review panel | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating alternative designs and the strongest argument against your own; drafting ADRs and arc42 sections from your notes; producing Structurizr or Mermaid models from existing code (then correcting them); writing ArchUnit, import-linter or dependency-cruiser rules; summarising Git history for hotspots. Claude Code, OpenAI Codex, Cursor and GitHub Copilot can all read a repository and do this.
- **Do without AI (drills):** quality-attribute scenarios and utility trees; identifying patterns from unfamiliar code; whiteboard C4 sketches in 15 minutes; ATAM-lite trade-off points; the mid-term and final. Architecture judgement is what you are training.
- **Verify AI output by:** executing the boundary rules rather than trusting a diagram; checking every claimed framework feature (Spring Modulith annotations, ArchUnit APIs) against the official docs and a compiling example; recomputing coupling metrics yourself on a sample; asking whether each proposed abstraction has at least two real users.
- **Where AI still fails here (you will collect your own evidence):** in Lab 2 and Lab 10 you log every case where an agent (a) added an interface or factory with one implementation, (b) proposed microservices without being asked about team size or load, (c) drew a diagram that contradicts the code, or (d) imported across a module boundary to finish a task faster. Bring the log to the oral defence; it is graded on accuracy, not on how many failures you found.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| P1 | 10% |
| P2 (with ATAM report) | 20% |
| P3 (with panel review) | 25% |
| Mid-term (AI off) | 5% |
| Final exam (AI off) + oral defence | 20% |

**Mastery gate.** You pass when you can: (1) take an unfamiliar open-source codebase of about 30,000 lines and, in one working day, deliver C4 context, container and component diagrams that match the code, three ADRs that reconstruct real decisions, a coupling report with the three worst hotspots, and boundary rules that run in CI; (2) in a 90-minute AI-off exam, write a utility tree for a case you have not seen, propose two architectures, and name at least two trade-off points and three risks a reviewer agrees with; (3) defend one decision for 10 minutes against a panel arguing for the opposite.

## Industry reality

Where this is used (public sources): Shopify documented moving its Rails monolith to a componentised modular monolith and released Packwerk to enforce boundaries ([Shopify Engineering, 2019](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) and [2020](https://shopify.engineering/shopify-monolith)). Spring Modulith exists because Java teams wanted verifiable module boundaries inside one deployable. ONDC publishes an open, callback-based (asynchronous) protocol for Indian digital commerce ([ONDC on GitHub](https://github.com/ONDC-Official)). The C4 model and ADRs are now standard design-review artefacts. Architecture decisions also surface in the low-level and high-level design rounds of Indian and global interview loops ([SWE market page](../../../../06_career_and_market_readiness/01_market_map/roles/SWE_software_engineering.md)).

**Interview questions from this course**

1. *Monolith or microservices for a 6-engineer startup building a clinic-booking product?* Strong answer: modular monolith with enforced boundaries; names the prerequisites for microservices (independent deploys, team autonomy, ops maturity); says what signal would trigger the first extraction; mentions shared-database and synchronous-chain traps.
2. *Explain hexagonal architecture with an example, and when you would not use it.* Strong answer: driving and driven ports with concrete adapters (HTTP, CLI, Postgres, payment gateway); testing through ports with fakes; admits overhead for thin CRUD apps.
3. *How do you keep an order service and an inventory service consistent without distributed transactions?* Strong answer: saga with compensations, outbox for reliable publishing, idempotent consumers, a visible "pending" state for users, reconciliation job; compares choreography and orchestration.
4. *Which design patterns do you actually use, and which do you avoid?* Strong answer: strategy, adapter, decorator, state and builder with real examples; says which patterns language features replace (functions, sealed types); gives an example of removing an unnecessary abstraction.
5. *How would you know your architecture is eroding?* Strong answer: executable boundary rules in CI, cycle counts, change coupling and hotspot trends from Git, review latency on core modules, and violation rates in agent-generated PRs; acts on trends, not single numbers.

## Resources (free first)

- **Models and templates:** C4 model — https://c4model.com/ ; Structurizr — https://docs.structurizr.com/ ; arc42 — https://arc42.org/ ; Michael Nygard, "Documenting Architecture Decisions" — https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions ; MADR — https://adr.github.io/madr/
- **Articles:** Martin Fowler on event-driven — https://martinfowler.com/articles/201701-event-driven.html ; MonolithFirst — https://martinfowler.com/bliki/MonolithFirst.html ; Microservice Prerequisites — https://martinfowler.com/bliki/MicroservicePrerequisites.html ; Technical Debt Quadrant — https://martinfowler.com/bliki/TechnicalDebtQuadrant.html ; Alistair Cockburn, Hexagonal Architecture — https://alistair.cockburn.us/hexagonal-architecture/ ; Robert C. Martin, "The Clean Architecture" (2012) — https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html ; Peter Norvig, "Design Patterns in Dynamic Languages" (1996) — https://norvig.com/design-patterns/
- **Pattern catalogues:** Refactoring.Guru design patterns — https://refactoring.guru/design-patterns ; Microsoft Azure Architecture Center cloud design patterns — https://learn.microsoft.com/en-us/azure/architecture/patterns/ ; microservices.io — https://microservices.io/patterns/ ; DDD Crew (EventStorming, context mapping) — https://github.com/ddd-crew
- **Tools:** ArchUnit — https://www.archunit.org/ ; Spring Modulith — https://spring.io/projects/spring-modulith ; import-linter — https://import-linter.readthedocs.io/ ; dependency-cruiser — https://github.com/sverweij/dependency-cruiser ; Packwerk — https://github.com/Shopify/packwerk ; code-maat — https://github.com/adamtornhill/code-maat
- **Course:** MIT 6.031 Software Construction readings — https://web.mit.edu/6.031/
- **Paid, optional:** Bass, Clements and Kazman, *Software Architecture in Practice* (4th ed.); Richards and Ford, *Fundamentals of Software Architecture*; Gamma et al., *Design Patterns* (1994); Fowler, *Patterns of Enterprise Application Architecture*; Evans, *Domain-Driven Design*; Khononov, *Learning Domain-Driven Design*; Tornhill, *Your Code as a Crime Scene*.

## Sources

- Google Cloud, "Announcing the 2025 DORA report" (24 Sep 2025) — https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report ; DORA 2025 report page — https://dora.dev/research/2025/dora-report/ (checked 2026-10)
- Google Cloud, "Introducing DORA's inaugural AI Capabilities Model" (24 Sep 2025) — https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model (checked 2026-10)
- Peter Norvig, "Design Patterns in Dynamic Languages" (1996) — https://norvig.com/design-patterns/ (checked 2026-10)
- Shopify Engineering, "Deconstructing the Monolith" (2019) — https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity ; "Under Deconstruction: The State of Shopify's Monolith" (2020) — https://shopify.engineering/shopify-monolith (checked 2026-10)
- ONDC official specifications on GitHub — https://github.com/ONDC-Official (checked 2026-10)
- Amazon, 2016 Letter to Shareholders ("Many decisions are reversible, two-way doors", referring back to the 2015 letter) — https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders ; 2015 letter (PDF) — https://s2.q4cdn.com/299287126/files/doc_financials/annual/2015-Letter-to-Shareholders.PDF (checked 2026-10)
- Melvin Conway, "How Do Committees Invent?" (1968) — http://www.melconway.com/Home/Committees_Paper.html (checked 2026-10)
- ISO/IEC 25010:2023, product quality model — https://www.iso.org/standard/78176.html (checked 2026-10)

_Last reviewed: 2026-10_
