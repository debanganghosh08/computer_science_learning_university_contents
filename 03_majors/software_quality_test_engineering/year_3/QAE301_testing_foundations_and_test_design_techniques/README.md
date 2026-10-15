# QAE301 · Testing Foundations and Test Design Techniques

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [QAE401](../../year_4/QAE401_ai_in_testing_generated_tests_self_healing/README.md); used by every QAE course, especially [QAE302](../QAE302_test_automation_engineering_ui_and_api/README.md) and [QAE404](../../year_4/QAE404_quality_engineering_leadership_and_metrics/README.md) |

Part of the [Software Quality and Test Engineering major](../../README.md). CS205 taught you to write good unit tests, use test doubles and measure a suite with mutation testing. This course teaches you to decide **what** to test and **why**: how to choose, out of an effectively infinite input space, the few hundred tests that carry the most information about risk.

## Why this course matters now

On 19 July 2024 a CrowdStrike content update crashed about 8.5 million Windows devices. CrowdStrike's root-cause analysis found that a new template type defined 21 input fields while the sensor code supplied 20, that the number of fields was not validated, and that "Template Type testing should cover a wider variety of matching criteria": a boundary and combination case that existing tests did not exercise. AI tools now generate test cases from requirements in seconds (Playwright's planner and generator agents, LLM chat assistants, Meta's TestGen-LLM in industry), but a generator only tests what it is told or what the code already does. It cannot know which failure would cost the company most, which input combinations matter, or what the correct output is when the specification is silent. Those three judgements (risk, coverage and the oracle) are what this course trains, with named techniques you can defend in a review or an interview.

## Learning outcomes

By the end you can:

1. **Run** a product risk analysis with stakeholders and **turn** it into a prioritised, risk-based test strategy.
2. **Derive** test cases with equivalence partitioning, boundary value analysis (2- and 3-value), domain testing, decision tables, cause–effect graphs, state transition testing and pairwise/t-way combinatorial testing, and **justify** each case by the technique that produced it.
3. **Measure** structural coverage (statement, branch, condition, MC/DC) and **use** mutation analysis to judge test adequacy rather than coverage alone.
4. **Choose** oracles (specified, differential, metamorphic, regression, implicit, human) and **explain** the oracle problem for a given system.
5. **Plan and run** session-based exploratory testing with charters, heuristics, notes and debriefs.
6. **Write** bug reports that get fixed, and **separate** severity from priority with evidence.
7. **Write** a one-page test plan and a test summary report that states residual risk honestly.
8. **Compare** AI-generated test suites with technique-derived ones using fault-detection and mutation scores.

## Chapters and lessons

### Chapter 1 · What testing is, and what it cannot do (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Error, fault, failure | The causal chain; why a test only reveals a fault if it reaches the faulty code, infects the program state, propagates the bad state to an output and checks that output (the RIPR model: reachability, infection, propagation, revealability) | For 5 real bug reports, name the error, fault and failure |
| 1.2 Why exhaustive testing is impossible | Input-space arithmetic (a form with 6 fields of 10 classes each = 10⁶ cases); Dijkstra's "testing shows the presence, not the absence of bugs" | Count the input space of a sign-up form; estimate run time at 10 tests/s |
| 1.3 Testing versus checking | Bach and Bolton's distinction: checks are algorithmic confirmations, testing is investigation and learning | Classify 20 activities from a real team as checking or testing |
| 1.4 Quality models and test types | ISO/IEC 25010:2023 product quality characteristics; functional vs non-functional; test levels (unit, integration, system, acceptance) | Map 15 user complaints about a food-delivery app to 25010 characteristics |
| 1.5 The ISTQB vocabulary | CTFL v4.0 terms (test basis, test condition, test case, coverage item) so you can talk with any team | Rewrite a messy test document using precise terms |

**Check your understanding:** Why can a test execute faulty code and still pass? Which ISO 25010 characteristics can an automated check never fully cover? When is "100% of requirements tested" a meaningless statement?

### Chapter 2 · Risk-based testing (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Product risk | Likelihood × impact; technical vs business risk; risk appetite; who owns which risk | Interview a "stakeholder" (instructor role-play) and list 20 risks |
| 2.2 Risk analysis methods | Risk workshops, FMEA-lite (failure mode, effect, detection), heuristic risk catalogues | FMEA table for a wallet top-up flow (illustrative) |
| 2.3 From risk to test effort | Risk levels → test depth, technique choice and automation priority; the Heuristic Test Strategy Model (Bach) | Allocate 80 tester-hours across 12 features by risk; defend the split |
| 2.4 Residual risk | What remains untested, and how to say it to a release manager | One-paragraph residual-risk statement for a mock release |

**Check your understanding:** Why does impact usually matter more than likelihood for payments and health? How should risk-based testing change when a module was written mostly by an AI agent? What makes a residual-risk statement useful rather than defensive?

### Chapter 3 · Equivalence partitioning, boundaries and domains (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Equivalence partitioning | Valid and invalid partitions; one test per partition; why invalid partitions are tested one at a time | Partition a PAN/IFSC-style input validator (format rules from public specs) |
| 3.2 Boundary value analysis | 2-value and 3-value BVA (CTFL v4.0); closed vs open boundaries; off-by-one families | Find 5 seeded boundary bugs in a provided fee calculator |
| 3.3 Domain testing | Multi-variable domains, on- and off-points (Beizer), linear boundaries | Domain tests for "loan eligible if income ≥ 3 × EMI and age 21–60" |
| 3.4 Hard boundaries | Floating point and money (paise, rounding modes), dates (leap years, month ends, IST without daylight saving, UTC conversion), string lengths in bytes vs characters (Devanagari, emoji) | Break a date-range function and a name-length check with Unicode |

**Check your understanding:** Why test invalid partitions separately? Where is the boundary of `amount > 0` for a value stored in paise, and for one stored as a float? Why can a 30-character limit fail on a 12-letter Hindi name?

### Chapter 4 · Decision tables and cause–effect (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Full decision tables | Conditions, actions, rules; 2ⁿ growth; impossible combinations | Table for a ticket-refund policy with 4 conditions |
| 4.2 Collapsing tables | Don't-care entries; when collapsing hides bugs | Collapse the refund table; find the rule it loses |
| 4.3 Cause–effect graphs | Causes, effects, constraints (exclusive, requires, masks) | Build a graph for a discount-coupon engine; derive tests |
| 4.4 MC/DC | Modified condition/decision coverage; why avionics (DO-178C Level A) requires it; n+1 tests for n conditions | MC/DC set for `(a && b) \|\| (c && !d)`; prove each condition's independent effect |

**Check your understanding:** When does a decision table beat equivalence partitioning? Why does MC/DC need only about n+1 tests while full combination needs 2ⁿ? What business rule in a product you use would you model as a table?

### Chapter 5 · State transition and model-based testing (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 State machines | States, events, guards, actions; state tables expose invalid transitions | Model an e-commerce order lifecycle (placed → paid → packed → shipped → delivered, plus cancel and return) |
| 5.2 Coverage criteria | All states, all transitions (0-switch), transition pairs (1-switch), invalid transitions | Derive 0-switch and 1-switch suites; compare counts |
| 5.3 Model-based testing | Generate paths from a model (GraphWalker); random walks vs coverage-driven walks | Generate 200 paths for the order model; run them against a buggy implementation |
| 5.4 Stateful property testing | Hypothesis `RuleBasedStateMachine`: random command sequences checked against a model | Find a seeded "refund after partial cancel" bug with a stateful test |

**Check your understanding:** Why do invalid transitions find so many real bugs? When is a state model too expensive to maintain? What does a stateful property test find that 50 hand-written scenarios miss?

### Chapter 6 · Combinatorial and pairwise testing (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The interaction rule | NIST's finding that most failures are triggered by one or two parameters and progressively fewer by more (1 to 6 observed) | Read the NIST summary; estimate how many failures a 2-way suite should catch |
| 6.2 Covering arrays | Pairwise and t-way coverage; orthogonal arrays vs covering arrays | Hand-build a pairwise set for 4 parameters × 3 values |
| 6.3 Tools and constraints | Microsoft PICT and NIST ACTS; constraints ("Safari only on macOS/iOS"), seeding must-have rows | PICT model of browser × OS × locale × payment method × network |
| 6.4 Configuration testing | Feature flags, locales, device matrices; when 3-way is worth it | Compare 2-way and 3-way on a simulator with planted 3-way faults |

**Check your understanding:** Why can pairwise testing miss a bug that needs three parameters? How do constraints change a covering array's size? Which product decisions would make you pay for 3-way coverage?

### Chapter 7 · Structural coverage and test adequacy (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Coverage criteria | Statement, branch, condition, path; subsumption; `coverage.py` branch mode, JaCoCo | Measure all four on one module; explain the gaps |
| 7.2 Data-flow testing | Definitions and uses; def-use pairs; why loops hide bugs | Find a def-use pair no current test exercises |
| 7.3 Mutation analysis as adequacy | Mutation score, equivalent mutants, mutant sampling; Google's diff-based mutation in code review | Raise a suite's mutation score from baseline by ≥ 20 points |
| 7.4 Coverage as a tool, not a target | Goodhart's law; assertion-free tests with 100% coverage | Write a 100%-coverage suite that kills < 30% of mutants, then fix it |

**Check your understanding:** Why can branch coverage be 100% while condition combinations stay untested? What does a surviving mutant tell you that a coverage report cannot? Why do teams that target coverage percentages get worse tests?

### Chapter 8 · Oracles: knowing the right answer (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 The oracle problem | Barr et al.'s survey (IEEE TSE 2015); why automation without an oracle only finds crashes | List the oracles available for a search engine, a pricing engine and a chatbot |
| 8.2 Derived oracles | Differential testing (two implementations), regression/golden-master oracles, model oracles | Differential-test two JSON parsers on generated input |
| 8.3 Metamorphic relations | Relations between outputs when inputs change (sorting a permuted list, search with an added filter) | Write 5 metamorphic relations for a route-distance service |
| 8.4 Implicit and human oracles | Crashes, sanitizers, timeouts; HICCUPPS consistency heuristics (Bolton) | Use HICCUPPS to argue that a behaviour is a bug with no written spec |

**Check your understanding:** Why does a generated test that asserts the current output risk freezing a bug in place? When are two implementations not independent enough for differential testing? Which metamorphic relation would you trust for a recommendation feed?

### Chapter 9 · Exploratory testing (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Session-based test management | Charters, time-boxed sessions, session sheets, PROOF debriefs (Jonathan and James Bach, 2000) | Three 60-minute sessions on a RealWorld (Conduit) app |
| 9.2 Charters | "Explore *target* with *resources* to discover *information*" (Hendrickson); chartering from risks | Write 10 charters from your Chapter 2 risk list |
| 9.3 Heuristics and tours | SFDIPOT (structure, function, data, interfaces, platform, operations, time); touring heuristics; interruptions, back button, double submit | One session per heuristic family; tally bugs per family |
| 9.4 Tool-assisted exploration | Browser DevTools, network throttling, proxies on your own app, log tailing; AI as an idea generator, not a judge | Pair with an LLM for charter ideas; record which ideas found bugs |
| 9.5 Bug reports and advocacy | Reproduction steps, minimal case, expected vs actual, evidence, impact; severity vs priority; BBST bug advocacy | Rewrite 5 weak public bug reports into ones a maintainer would act on |

**Check your understanding:** Why is exploratory testing not "random clicking"? What makes a session's notes useful to someone who was not there? When should a severe bug get low priority?

### Chapter 10 · Test planning and reporting (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Test plans | ISO/IEC/IEEE 29119-3 plan contents vs a one-page plan; scope, approach, entry and exit criteria, environments, risks | One-page plan for a mobile-recharge feature |
| 10.2 Estimation | Work-breakdown, ratio and three-point estimates; why test estimates fail | Estimate P3; compare with actual hours |
| 10.3 Test data | Partitions as data requirements; synthetic data; why copying production personal data is a DPDP Rules 2025 risk | Generate synthetic Indian addresses and names covering your partitions |
| 10.4 Reporting | Test summary reports; defect trends; "what we did not test"; go/no-go recommendations | Write the summary report for P2 |

**Check your understanding:** What exit criterion would you refuse to sign, and why? Why is "pass rate 98%" useless without a risk breakdown? How do you make synthetic data realistic enough to find bugs?

### Chapter 11 · Test design with and against AI (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 What generators do | LLM test-case generation from requirements; Playwright planner agent; TestGen-LLM's filters (builds, passes repeatedly, adds coverage) | Generate a suite from P1's spec with two different AI tools |
| 11.2 Measuring generated suites | Fault detection on a bug zoo, mutation score, duplicate and vacuous tests, technique coverage | Score AI suites against your technique-derived suite |
| 11.3 Shared blind spots | Tests derived from code inherit its bugs; spec ambiguity propagates; the oracle stays human | Give the AI the buggy code instead of the spec; count bugs it "confirms" |
| 11.4 A combined workflow | Human risk analysis and oracles; AI breadth for partitions and data; review gates | Write your team's rules for accepting AI-generated tests |

**Check your understanding:** Why does an AI test generator that reads the implementation tend to miss specification bugs? Which part of test design gains most from AI breadth? What evidence would make you accept an AI-generated suite into CI?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Input space and quality model | — |
| 2 | 2 | Lab 2 · Risk workshop | Risk register |
| 3 | 3 | Lab 3 · Boundary bug zoo | — |
| 4 | 4 | Lab 4 · Decision tables and MC/DC | **P1 due** |
| 5 | 5 | Lab 5 · State models and stateful tests | — |
| 6 | 6 | Lab 6 · Pairwise with PICT | — |
| 7 | 7 | Lab 7 · Coverage vs mutation | Mid-term (AI off) |
| 8 | 8 | Lab 8 · Differential and metamorphic oracles | — |
| 9 | 9 | Lab 9 · Session-based exploratory testing | — |
| 10 | 9 | P2 sessions | Session sheets |
| 11 | 10 | P2 reporting | **P2 due** |
| 12 | 10 | P3 strategy review | Strategy draft |
| 13 | 11 | Lab 10 · AI vs technique | — |
| 14 | 11 | P3 | **P3 due** |
| 15 | Review | P3 defence | Final exam (AI off): design tests for an unseen spec |

## Working with AI in this course

- **Use AI for:** brainstorming risks and charter ideas after you have written your own list; generating synthetic test data for partitions you defined; drafting PICT models and decision tables from long policy documents (then checking every rule against the source); turning your test design into pytest or Playwright code; summarising session notes. Tools: Claude, ChatGPT or Gemini chat; Claude Code, Codex or Copilot for code; Playwright's planner agent for first-pass plans.
- **Do without AI (drills):** every first derivation with a technique (partitions, boundaries, tables, state models); the risk analysis; the oracle choice; bug reports; the mid-term and final. You cannot judge a generated test design you could not have produced.
- **Verify AI output by:** running generated tests against the bug zoo and mutants (a test that kills nothing is decoration); tracing each generated case back to a technique and a risk; checking every business rule the AI "read" from a document against the document; deleting duplicates and assertion-free tests.
- **Where AI still fails here (show it):** in Lab 10 and Chapter 11 you measure it yourself: suites generated from code that confirm planted bugs, missing invalid-partition and boundary cases, invented business rules, and duplicate tests that inflate counts. In Meta's TestGen-LLM evaluation, 75% of generated test cases built, 57% passed reliably and only 25% increased coverage, which is why every generated test must pass filters before it is trusted.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| P1, P2, P3 | 10%, 20%, 25% |
| Mid-term (AI off): technique application | 5% |
| Final exam (AI off) + P3 defence | 20% |

**Mastery gate.** You pass when you can: (1) given an unseen two-page specification and 90 minutes without AI, produce a risk list and a test design using at least four named techniques that kills at least 85% of a hidden bug zoo of 20 faulty implementations; (2) run a 60-minute exploratory session on an unfamiliar app and return a session sheet and two bug reports that a reviewer can reproduce without asking you a question; (3) write a one-page test summary that names residual risks a release manager can act on.

## Industry reality

Test design is assessed in almost every QA and SDET loop, usually as "how would you test X?" (see the [market page](../../../../06_career_and_market_readiness/01_market_map/roles/QAE_software_quality_test_engineering.md)). Named public practices: Google's book *Software Engineering at Google* devotes chapters to testing culture and unit testing; Google reported that about 1.5% of all its test runs were flaky and that almost 16% of its tests showed some flakiness (2016), a reminder that test design includes designing for determinism; NIST's combinatorial testing research and free ACTS tool underpin pairwise practice; MC/DC is required by DO-178C for the most critical avionics software. The CrowdStrike 2024 analysis is a public case where wider matching-criteria testing and input validation were listed as fixes.

**Interview questions from this course**

1. *How would you test a UPI-style "send money" screen?* Strong answer: clarifies scope and risks first (money loss, double debit, wrong payee); partitions and boundaries for amount (minimum, per-transaction limit, paise rounding); state transitions for pending, success, failure and reversal; idempotency on retry and double tap; network loss mid-flow; accessibility and Hindi labels; names oracles (ledger balance invariants) and says what is out of scope.
2. *What is the difference between boundary value analysis and equivalence partitioning, and when does BVA fail?* Strong answer: partitions group inputs expected to behave alike, BVA probes edges where off-by-one faults cluster; BVA fails when partitions are wrong, when boundaries are hidden (internal limits, byte lengths, float precision) or for unordered domains.
3. *You have 2 days to test a release with 40 changed features. What do you do?* Strong answer: risk analysis with stakeholders, depth by risk, automation for regression, exploratory sessions on new and risky areas, explicit residual-risk statement, no pretence of full coverage.
4. *An AI tool generated 300 tests for our service with 92% line coverage. Are we done?* Strong answer: coverage is not adequacy; check mutation score, assertions, duplicates, whether tests were derived from code (shared blind spots), oracles for business rules, and fault detection on known past bugs.
5. *Write a bug report for a bug you found.* Strong answer: one-line summary with impact, environment, minimal reproducible steps, expected vs actual with evidence, frequency, severity and suggested priority with reasoning, no blame.

## Resources (free first)

- **Courses and books:** NPTEL Software Testing (Prof. Meenakshi D'Souza, IIIT Bangalore) — https://nptel.ac.in/courses/106101163 ; MIT 6.031 testing reading — https://web.mit.edu/6.031/www/sp22/classes/03-testing/ ; *Software Engineering at Google*, chapters 11–12 — https://abseil.io/resources/swe-book/html/ch11.html ; BBST courses (Kaner, Fiedler) — https://bbst.courses/
- **Syllabi and standards:** ISTQB CTFL v4.0 syllabus (free) — https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/ ; ISO/IEC 25010:2023 (catalogue page) — https://www.iso.org/standard/78176.html
- **Exploratory testing:** James Bach, Heuristic Test Strategy Model — https://www.satisfice.com/download/heuristic-test-strategy-model ; Jonathan Bach, Session-Based Test Management — https://www.satisfice.com/download/session-based-test-management ; Michael Bolton, "Testing vs. Checking" — https://www.developsense.com/blog/2009/08/testing-vs-checking/
- **Techniques and tools:** NIST combinatorial testing and ACTS — https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software ; Microsoft PICT — https://github.com/microsoft/pict ; GraphWalker — https://graphwalker.github.io/ ; Hypothesis stateful testing — https://hypothesis.readthedocs.io/en/latest/stateful.html ; coverage.py — https://coverage.readthedocs.io/ ; mutmut — https://mutmut.readthedocs.io/
- **Papers:** Barr et al., "The Oracle Problem in Software Testing: A Survey", IEEE TSE (2015) — https://doi.org/10.1109/TSE.2014.2372785 ; Petrović et al., "Practical Mutation Testing at Scale" (arXiv 2102.11378) — https://arxiv.org/abs/2102.11378
- **Practice apps:** RealWorld (Conduit) — https://docs.realworld.show/ and https://github.com/gothinkster/realworld
- **Paid, optional:** Elisabeth Hendrickson, *Explore It!* (Pragmatic Bookshelf) — https://pragprog.com/titles/ehxta/explore-it/ ; Ammann and Offutt, *Introduction to Software Testing* (Cambridge, 2nd ed.).

## Sources

All checked 12 Oct 2026.

- Microsoft, "Helping our customers through the CrowdStrike outage" (20 Jul 2024; about 8.5 million devices) — https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/
- CrowdStrike, Channel File 291 Incident Root Cause Analysis (6 Aug 2024): field-count validation, matching-criteria testing, Content Validator logic error, staged deployment — https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf
- Alshahwan et al., TestGen-LLM (arXiv 2402.09171; FSE 2024) — https://arxiv.org/abs/2402.09171
- Playwright release notes (test agents since 1.56) — https://playwright.dev/docs/release-notes
- John Micco, "Flaky Tests at Google and How We Mitigate Them" (27 May 2016) — https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html
- NIST, Automated Combinatorial Testing for Software (interaction rule; ACTS 3.3) — https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software
- ISTQB certifications page (CTFL v4.0 current) — https://istqb.org/certifications/
- PIB, DPDP Rules notified (14 Nov 2025) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014

_Last reviewed: 2026-10_
