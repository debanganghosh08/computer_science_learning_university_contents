# SWE402 · Legacy Modernization and Refactoring with AI

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [SWE302](../../year_3/SWE302_low_level_design_and_clean_code_at_scale/README.md); recommended [SWE301](../../year_3/SWE301_software_architecture_and_design_patterns/README.md) and [SWE304](../../year_3/SWE304_ai_assisted_software_engineering_agents/README.md) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) capstones; [SWE501](../../year_5/SWE501_frontier_seminar_agentic_software_engineering/README.md) (verification of AI code) |

## Why this course matters now

Most professional software work happens in code that is old, important and poorly tested: banking cores, insurance and telecom billing, government portals, the ten-year-old Rails or Java monolith at a startup that succeeded. Modernizing it was historically slow and risky, so it was postponed. Large language models changed the economics of the mechanical part. Google reported that in one large migration of 32-bit to 64-bit IDs, 80% of the landed code modifications were fully AI-authored and total time fell by an estimated 50%; its JUnit 3 to JUnit 4 migration changed 5,359 files and more than 149,000 lines in three months, with about 87% of AI-generated code committed unchanged. Airbnb moved about 3,500 React test files from Enzyme to React Testing Library in six weeks against a hand estimate of 1.5 years, using validation-and-retry loops rather than clever prompts. Amazon's CEO claimed AI-assisted Java upgrades saved the equivalent of 4,500 developer-years (a company claim, not audited). What did not change: deciding what the old system actually does, proving the new one does the same, moving data without losing it, and rolling out without an outage. This course teaches those disciplines and how to run agents and codemods inside them.

## Learning outcomes

By the end you can:

1. **Assess** a legacy system (code, data, runtime behaviour, people) and **choose** a modernization strategy (retain, rehost, replatform, refactor, rearchitect, replace, retire) with a written case.
2. **Recover** business rules from code with AI help, and **verify** every recovered rule against tests or production evidence.
3. **Pin** existing behaviour with characterization (golden-master) tests and **break** dependencies with seams, sprout and wrap techniques.
4. **Replace** a system incrementally with the strangler fig pattern, event interception and branch by abstraction.
5. **Migrate** data online with expand–contract schema changes, change data capture and verified backfills.
6. **Prove** equivalence with shadow traffic, response diffing, production experiments (Scientist-style) and parity dashboards.
7. **Build** migration pipelines that combine deterministic codemods (OpenRewrite, jscodeshift, ast-grep) with LLM agents, validation gates and retry loops.
8. **Control** risk and **report** progress: rollout plans, kill switches, parity and correctness metrics, decommissioning.

## Chapters and lessons

### Chapter 1 · The economics and options of modernization (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What "legacy" means | Code without tests (Feathers); code that earns money and nobody dares change | List the legacy traits of an open-source project that is 10+ years old |
| 1.2 The rewrite trap | Big-bang rewrites, second-system effect; Joel Spolsky's "Things You Should Never Do" (2000) and its critics | Find a public account of a failed or late rewrite; extract three causes |
| 1.3 The options | Retain, retire, rehost, replatform, repurchase, refactor, rearchitect (cloud-migration guides publish versions of this "Rs" list) | Classify 6 components of a provided system; justify each |
| 1.4 Building the case | Cost of change today (hotspot interest from SWE301), risk, opportunity; how to measure benefit | One-page modernization case for a provided legacy module |

**Check your understanding:** Why do rewrites usually take longer than estimated? When is "retain" the correct decision? What evidence would convince a finance team that refactoring pays back?

### Chapter 2 · Understanding a system nobody fully understands (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Code archaeology | Git history mining, ownership maps, dead code via coverage in production-like runs | Find modules nobody has touched in 3 years and the 5 most-changed files |
| 2.2 Runtime truth | Tracing, logs and request sampling to see what actually executes | Instrument a legacy app; produce a call graph of one business flow |
| 2.3 Business-rule extraction with AI | Asking agents to explain code with line citations; rule catalogues; contradictions between code and documentation | Extract 20 rules from a legacy pricing module; verify each with a test |
| 2.4 Reading COBOL and old Java | COBOL divisions, PIC clauses, packed decimal (COMP-3), copybooks; EJB-era Java patterns | Explain a 300-line COBOL program and its data layout; write the equivalent record type |
| 2.5 People and documents | Interviewing operators and long-tenured engineers; runbooks as evidence | Interview plan and a findings log for a mock stakeholder |

**Check your understanding:** Why is an AI summary of legacy code a hypothesis, not a fact? Which behaviours exist only at runtime and never appear clearly in the code? Why does packed-decimal arithmetic matter when moving from COBOL to Java?

### Chapter 3 · Characterization tests and seams (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Golden-master testing | Approval tests; capturing outputs for many generated inputs; scrubbing timestamps and IDs | Approval tests for the Gilded Rose and a legacy invoice generator |
| 3.2 Seams | Object seams, link seams, preprocessing seams; dependency-breaking techniques | Get a class with a hard-coded database call under test without changing behaviour |
| 3.3 Sprout and wrap | Adding new behaviour beside old code without editing it | Add a discount rule via sprout method; then via wrap class |
| 3.4 Record and replay | Capturing (sanitised) production requests and responses as tests; privacy constraints under India's DPDP Act 2023 | Build a replay harness for an HTTP service with PII scrubbing |
| 3.5 Generated characterization tests | Using agents to generate input sets and approval tests; checking them with mutation testing | Agent-generated golden master; raise its mutation score |

**Check your understanding:** Why does a characterization test assert what the code does, not what it should do? What makes a seam safe to introduce without tests? When would recorded production traffic be illegal or unsafe to use?

### Chapter 4 · Strangler fig and incremental replacement (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The strangler fig | Routing slices of traffic to new code at a facade (Fowler); growing the new around the old | Put a routing proxy in front of a legacy app; move one endpoint |
| 4.2 Legacy displacement patterns | Divert the flow, extract product lines, event interception, transitional architecture, questioning feature parity (Fowler and Thoughtworks) | Map 4 patterns onto a provided monolith's migration plan |
| 4.3 Branch by abstraction | Abstraction layer, two implementations, switch, remove old | Replace a payment client inside the monolith without a long-lived branch |
| 4.4 Anti-corruption layers | Translating the old model so it does not leak into the new one | ACL between a legacy customer model and a new domain model |

**Check your understanding:** Why is "feature parity" often the wrong goal? What makes a slice of functionality a good first candidate to strangle? When does the transitional architecture become permanent by accident?

### Chapter 5 · Moving data without losing it (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Expand–contract schema changes | Add, dual-write, backfill, switch reads, stop old writes, remove | Rename a column on a live table under load with zero errors |
| 5.2 Change data capture | Debezium and logical replication; outbox as an alternative to dual writes | Stream changes from a legacy MySQL to a new Postgres model |
| 5.3 Online schema tools | gh-ost and pt-online-schema-change; locks and replication lag | Run an online migration; monitor lag |
| 5.4 Backfills and parity | Batching, throttling, idempotency; row counts, checksums and sampled deep comparison | Backfill 10 million rows; produce a parity report |

**Check your understanding:** Why are dual writes from application code risky without an outbox or CDC? What does a matching row count fail to prove? How do you roll back a data migration that already took writes?

### Chapter 6 · Proving the new system is equivalent (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Shadow traffic | Mirroring requests to the new system; side-effect isolation | Shadow a read-heavy endpoint; log every difference |
| 6.2 Diffing responses | Noise filtering (timestamps, ordering, float rounding) in the spirit of Twitter's Diffy | Diff old vs new for 100,000 requests; classify differences |
| 6.3 Experiments in production | GitHub's Scientist: run old and new paths, return the old result, record mismatches | Wrap a refactored function with a Scientist-style experiment |
| 6.4 Defining "equivalent" | Exact, semantic, and acceptable differences; sign-off with domain owners | Write an equivalence specification for a tax calculation |
| 6.5 Canaries and parity dashboards | Progressive rollout gated on mismatch rate | Dashboard and an automatic rollback on mismatch rate > 0.1% |

**Check your understanding:** Why must shadow traffic never trigger real side effects, and how do you guarantee it? What mismatch rate would you accept for a payments calculation, and why? Who signs off that a difference is acceptable?

### Chapter 7 · Codemods and deterministic refactoring (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Abstract syntax tree tools | OpenRewrite (Java), jscodeshift and ts-morph (TypeScript), LibCST (Python), ast-grep and Comby (multi-language) | Write a recipe that migrates a deprecated API across a repo |
| 7.2 Composing recipes | Framework upgrade recipes (for example Spring Boot or JUnit upgrades) as sequences of small transforms | Run an OpenRewrite upgrade recipe on an open-source Java app; fix what it misses |
| 7.3 Huge single changes | Stripe converted its codebase from Flow to TypeScript with a codemod in one large change (2022) | Plan a one-shot vs incremental codemod rollout for a 1-million-line repo |
| 7.4 Codemod vs LLM | Determinism, auditability, cost; when patterns are regular vs irregular | For 3 migration tasks, choose codemod, LLM or hybrid; justify |

**Check your understanding:** What can a codemod guarantee that an LLM cannot? Which migrations are too irregular for codemods? Why was a one-shot conversion reasonable for Stripe, and when would it not be?

### Chapter 8 · LLM-driven migrations at scale (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 What the public cases show | Google's migrations (80% AI-authored edits and ~50% time saving for the ID migration; ~87% of generated code committed unchanged for JUnit), Airbnb's test migration (75% of files in the first 4-hour pass, 97% after 4 days on the long tail, fewer than 100 files by hand), Amazon's Java upgrade claims | Compare the three: task type, validation, human effort, what is claimed vs measured |
| 8.2 The pipeline | Shard the work; build context (related files, examples); generate; validate (compile, tests, lint, types); feed errors back; retry; route failures to humans | Build a pipeline that migrates 200 test files between two frameworks |
| 8.3 Sample, tune, sweep | Sampling failures, fixing prompts and context, re-running the long tail (Airbnb's method) | Raise your pipeline's pass rate by 20 points with evidence of what changed it |
| 8.4 Review at scale | Diff sampling, risk-based review, reviewer rotation, ownership approvals | Design the review plan for 5,000 generated changes |
| 8.5 Cost and throughput | Tokens, compute, retries, human minutes per change | Cost per migrated file for your pipeline; compare with a manual estimate |

**Check your understanding:** Why did retrying often beat prompt engineering in Airbnb's migration? What is the danger of a pipeline whose only validation is "tests pass"? How would you audit a vendor's "4,500 developer-years saved" claim?

### Chapter 9 · Language and framework migrations (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Runtime upgrades | Java 8/11/17 to 21/25, Python 3.x, Node LTS; deprecations, behaviour changes, dependency resolution | Upgrade an app from Java 11 to Java 25 with OpenRewrite plus an agent; record every manual fix |
| 9.2 Frontend framework migrations | AngularJS to React, class components to hooks, Enzyme to React Testing Library | Migrate 3 components with an agent behind characterization tests |
| 9.3 COBOL to Java | Decimal semantics, EBCDIC, record layouts, batch scheduling; why line-by-line translation produces unmaintainable Java | Translate one COBOL batch program; prove output equivalence on 10,000 records |
| 9.4 C to Rust | C2Rust's mechanical (mostly `unsafe`) translation; DARPA's TRACTOR programme; LLM-assisted idiomatic translation | Translate a small C library; reduce `unsafe` blocks; fuzz both for equivalence |

**Check your understanding:** Why does mechanically translated code often keep the old design's problems? What breaks when decimal arithmetic becomes `double`? How do you prove a C and a Rust implementation behave the same?

### Chapter 10 · Risk control and rollout (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Migration plans | Phases, exit criteria, rollback points, freeze windows (for example festival-sale or financial-year-end periods) | Write the plan for P3 |
| 10.2 Kill switches and progressive rollout | Flags per slice, percentage rollout, automatic rollback on parity or error metrics | Implement and drill a kill switch |
| 10.3 Measuring progress honestly | Call sites remaining, traffic share on new path, parity rate, incidents, cost | Build a migration burn-down from real data |
| 10.4 Decommissioning | Turning the old system off: data retention, archives, access removal | Decommission checklist for a retired service |

**Check your understanding:** Why do many migrations stall at 90%? Which metric would make you pause a rollout immediately? What must happen before you delete the old system's data?

### Chapter 11 · Running a modernization programme (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Sequencing | By value and risk; hotspots first; dependencies; quick wins that build trust | Sequence 10 modernization items with reasons |
| 11.2 Teams and ownership | Platform vs product team roles; migration guilds; who fixes the long tail | Responsibility matrix for a 3-team migration |
| 11.3 Communicating | Status reports, risks, asks; translating technical progress for leadership | Write a monthly status report for P3 |
| 11.4 Capstone | End-to-end modernization of a real or realistic legacy system | P3 delivery and review |

**Check your understanding:** Why should the first slice be low risk but visible? Who should own the long tail of a migration? What should a status report say when the project is behind?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Options and the case | — |
| 2 | 2 | Lab 2 · Archaeology and rule extraction | — |
| 3 | 3 | Lab 3 · Golden masters and seams | **P1 due** |
| 4 | 4 | Lab 4 · Strangler proxy | — |
| 5 | 5 | Lab 5 · Expand–contract and CDC | — |
| 6 | 6 | Lab 6 · Shadow, diff, Scientist | — |
| 7 | 7 | Lab 7 · Codemods | Mid-term (AI off): read legacy code, write characterization tests |
| 8 | 8 | Lab 8 · LLM migration pipeline | — |
| 9 | 8 | Lab 8 (cont.) · Sample, tune, sweep | **P2 due** |
| 10 | 9 | Lab 9 · COBOL or C translation with equivalence proof | — |
| 11 | 10 | Lab 10 · Kill switches and burn-down | — |
| 12 | 11 | P3 | — |
| 13 | 11 | P3 | — |
| 14 | 11 | P3 review | **P3 due** |
| 15 | Review | Oral defence | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining unfamiliar legacy code with line citations; drafting characterization inputs; bulk mechanical changes inside a validated pipeline; translating between languages behind equivalence tests; summarising migration failures into categories.
- **Do without AI (drills):** reading a legacy module and writing its characterization tests (mid-term); choosing a modernization option; writing the equivalence specification; the rollback plan; the final exam. These are the decisions that make an AI-driven migration safe.
- **Verify AI output by:** characterization tests and mutation testing; compile, type, lint and test gates on every generated change; shadow traffic and diffing; differential fuzzing for translations; sampled human review at a rate set by risk; parity metrics before every rollout step.
- **Where AI still fails here (show it):** in Labs 2, 8 and 9 you log cases where an agent (a) described a business rule that the code does not implement, (b) produced a translation that compiles and passes weak tests but differs on edge inputs (rounding, encodings, overflow), (c) "fixed" a failing test instead of the code, or (d) migrated mechanically while keeping the old design's problems. Google's own report treats time savings as estimates and says it is not a controlled study, so you will also report the limits of your own measurements.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| P1, P2, P3 | 10%, 20%, 25% |
| Mid-term (AI off) | 5% |
| Final exam (AI off) + oral defence | 20% |

**Mastery gate.** You pass when you can: (1) take an untested legacy module (about 2,000 lines) and, with AI off, pin its behaviour with characterization tests reaching at least 70% mutation score in one working day; (2) run a migration of at least 200 files through a validated LLM-plus-codemod pipeline with a documented pass rate, cost and zero unreviewed high-risk changes; (3) move one slice of a live system to new code with shadow traffic showing a mismatch rate below an agreed threshold and a drilled rollback.

## Industry reality

Where this is used (public sources): Google's experience report on AI-assisted internal code migrations ([Nikolov et al., 2025](https://arxiv.org/abs/2501.06972)); Airbnb's Enzyme to React Testing Library migration ([Airbnb Engineering, Mar 2025](https://medium.com/airbnb-engineering/accelerating-large-scale-test-migration-with-llms-9565c208023b)); Amazon's AI-assisted Java upgrades (CEO statement, Aug 2024, as reported by [The Decoder](https://the-decoder.com/amazons-ai-assistant-saves-4500-years-of-development-time-ceo-andy-jassy-says/)); Stripe's Flow-to-TypeScript conversion ([Stripe, 2022](https://stripe.com/blog/migrating-to-typescript)); GitHub's open-source Scientist library for production refactoring experiments; Fowler and Thoughtworks' legacy displacement patterns. Banks, insurers and government departments in India and worldwide run long-lived core systems, and modernization work is a large share of IT services revenue (analysis).

**Interview questions from this course**

1. *You inherit a 200,000-line service with no tests and must add a feature next week. What do you do?* Strong answer: characterization tests around the change area; seams; sprout or wrap the new behaviour; small PRs; no rewrite; plan broader tests later.
2. *How would you migrate a monolith's orders module to a new service without downtime?* Strong answer: strangler facade, data migration via expand–contract or CDC, shadow traffic and diffing, progressive rollout with kill switch, rollback plan, decommissioning.
3. *Your team wants to use an LLM to upgrade 3,000 services from Java 11 to 21. How do you design it?* Strong answer: deterministic recipes first (OpenRewrite), LLM for the irregular remainder, compile/test gates, retry with errors, risk-based human review, metrics per batch, canary deploys.
4. *How do you prove a rewritten tax calculation is correct?* Strong answer: equivalence specification with domain owners, golden-master tests on historical inputs, property-based and differential tests, shadow comparisons in production, explicit handling of rounding.
5. *What are the risks of AI-translating COBOL to Java?* Strong answer: decimal semantics, record layouts and encodings, batch and transaction semantics, unidiomatic output that nobody can maintain, missing business rules, the need for equivalence testing at volume.

## Resources (free first)

- **Patterns:** Martin Fowler, "Strangler Fig Application" — https://martinfowler.com/bliki/StranglerFigApplication.html ; Ian Cartwright, Rob Horn and James Lewis, "Patterns of Legacy Displacement" — https://martinfowler.com/articles/patterns-legacy-displacement/ ; Branch by Abstraction — https://martinfowler.com/bliki/BranchByAbstraction.html ; Parallel Change — https://martinfowler.com/bliki/ParallelChange.html
- **Testing legacy code:** ApprovalTests — https://approvaltests.com/ ; Gilded Rose kata — https://github.com/emilybache/GildedRose-Refactoring-Kata ; GitHub Scientist — https://github.com/github/scientist ; Diffy — https://github.com/opendiffy/diffy
- **Codemods:** OpenRewrite — https://docs.openrewrite.org/ ; jscodeshift — https://github.com/facebook/jscodeshift ; LibCST — https://libcst.readthedocs.io/ ; ast-grep — https://ast-grep.github.io/ ; Comby — https://comby.dev/
- **Data migration:** Debezium — https://debezium.io/documentation/ ; gh-ost — https://github.com/github/gh-ost
- **Translation:** C2Rust — https://github.com/immunant/c2rust ; DARPA TRACTOR — https://www.darpa.mil/research/programs/translating-all-c-to-rust ; GnuCOBOL (to run COBOL locally) — https://gnucobol.sourceforge.io/
- **Case studies:** Google (arXiv 2501.06972), Airbnb, Stripe (links above)
- **Paid, optional:** Feathers, *Working Effectively with Legacy Code*; Fowler, *Refactoring* (2nd ed.); Tornhill, *Software Design X-Rays*.

## Sources

- Nikolov et al., "How is Google using AI for internal code migrations?" (arXiv 2501.06972, 12 Jan 2025) — https://arxiv.org/abs/2501.06972 (checked 2026-10)
- Airbnb Engineering, "Accelerating Large-Scale Test Migration with LLMs" (Mar 2025) — https://medium.com/airbnb-engineering/accelerating-large-scale-test-migration-with-llms-9565c208023b ; InfoQ summary (Mar 2025) — https://www.infoq.com/news/2025/03/airbnb-llm-test-migration/ (checked 2026-10)
- The Decoder, report on Andy Jassy's statement about Amazon Q Java upgrades (Aug 2024) — https://the-decoder.com/amazons-ai-assistant-saves-4500-years-of-development-time-ceo-andy-jassy-says/ (checked 2026-10)
- Stripe, "Migrating millions of lines of code to TypeScript" (2022) — https://stripe.com/blog/migrating-to-typescript (checked 2026-10)
- Joel Spolsky, "Things You Should Never Do, Part I" (Apr 2000) — https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/ (checked 2026-10)

_Last reviewed: 2026-10_
