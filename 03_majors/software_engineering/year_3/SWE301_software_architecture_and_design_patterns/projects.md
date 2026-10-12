# SWE301 · Labs and projects

Labs use Java 21+ (Spring Boot with Spring Modulith and ArchUnit) or TypeScript (NestJS or plain Node with dependency-cruiser) or Python (import-linter). Pick one stack for the semester; P1 is stack-neutral. Every lab ends with a short written note: what you decided, what you gave up, and the number that convinced you. Labs 1, 3 and 8 are AI-off. Elsewhere coding agents are allowed, and you must log any agent output you rejected and why.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Quality-attribute scenarios (AI off) | Write 10 six-part scenarios for a UPI-style P2P payment app; rank them in a utility tree | Scenario table with a measurable response for each, plus the top 3 with reasons | 3 h |
| 2 · Patterns and their replacements | Implement strategy, decorator, state and visitor; then replace each with the language feature that makes it smaller (lambdas, sealed types, pattern matching) | Both versions, line counts, and a test showing identical behaviour | 6 h |
| 3 · Domain model and context map (AI off) | EventStorming for a train-ticket booking flow (search, hold, pay, confirm, cancel, refund); define aggregates and bounded contexts | Photo or digital board, aggregate invariants list, context map with relationship types | 4 h |
| 4 · One feature, four architectures | Implement "apply a discount code" in layered, hexagonal, clean and vertical-slice versions of a starter app | Files touched, lines changed, test runtime and test count per version; one-paragraph verdict | 6 h |
| 5 · Boundaries enforced in CI | Split a provided 8,000-line monolith into 4 modules with public APIs; add ArchUnit/Spring Modulith, import-linter or dependency-cruiser rules | A CI run that fails on a planted cross-module import and passes after the fix | 5 h |
| 6 · Saga and outbox | Order → payment → inventory saga with compensations, in choreography and orchestration styles; transactional outbox; idempotent consumer | Crash test (kill the process between DB commit and publish, 100 runs) showing zero lost and zero duplicated effects | 6 h |
| 7 · C4 as code and ADRs | Structurizr DSL model of the Lab 5 system (all four levels plus one dynamic view); 4 ADRs, one superseded | Rendered diagrams, the DSL in the repo, ADRs in MADR format | 4 h |
| 8 · ATAM-lite workshop (AI off) | Evaluate another team's P2 design in a 3-hour session using their utility tree | 2-page report: approaches, sensitivity points, trade-off points, risks, non-risks | 4 h |
| 9 · Metrics and Git mining | Compute Ca, Ce, I, A, D and LCOM4 on a 50k-line open-source Java or TypeScript repo; run code-maat for change coupling and hotspots | Main-sequence plot, top 5 hotspots, one hidden coupling explained from commit history | 5 h |
| 10 · Agents vs guardrails | Give a coding agent 10 change requests on the Lab 5 system, with and without boundary tests in a pre-commit hook | Table: violations attempted, caught, missed; diff sizes; your three rule changes | 5 h |

## Projects

### P1 · Architecture recovery of an open-source application (L1, ~6 hours)

**Real-world inspiration:** engineers joining a team, or consultants starting a modernisation, first reconstruct the architecture nobody wrote down. Pick a mid-sized, actively maintained open-source app (for example Zulip, Mastodon, Plausible Analytics, or the Spring PetClinic microservices sample if you are new to large codebases).

**What to build:** a recovered architecture pack: C4 context and container diagrams, one component diagram for the most-changed container, three ADRs that reconstruct real decisions from commit history, issues or docs (with links as evidence), and a list of five quality-attribute scenarios the system visibly optimises for.

**Acceptance criteria:**
- Every box and arrow in the container diagram is traceable to a file, config or deployment manifest (a table of evidence links).
- Each ADR cites at least two pieces of evidence (commit, issue, PR or doc), and states the alternatives that were available at the time.
- A maintainer-style check: two classmates who have not seen the repo use your pack to locate the code for 5 given features; they succeed on at least 4 within 30 minutes.
- At most 2 pages of prose besides diagrams.

**Stretch goals:** open a documentation PR upstream with one diagram or ADR; compare your diagram with any existing architecture doc in the project and list the drift.

**What it proves to an employer:** you can understand a codebase you did not write, quickly, and leave behind documentation others can use.

### P2 · Modular monolith with enforced boundaries (L2, ~15 hours)

**Real-world inspiration:** Shopify's componentised monolith, and the many Indian startups that run a single deployable for years before splitting. The domain is a clinic and diagnostic-lab booking platform (patients, doctors, slots, lab tests, payments, notifications). Business numbers are an **illustrative scenario**.

**What to build:** a modular monolith with at least 5 modules (identity, scheduling, labs, billing, notifications), each with a public API and private internals; one domain event flow using an outbox; a hexagonal core for scheduling with in-memory and Postgres adapters; ADRs for every boundary decision; Structurizr model; fitness functions in CI.

**Acceptance criteria:**
- Boundary rules run in CI and fail on any cross-module access to internals, any package cycle, or any module reading another module's tables (proved by three planted violations).
- Booking a slot is race-safe: 500 concurrent attempts for 50 slots produce exactly 50 bookings across 10 runs.
- Scheduling use-case tests run against in-memory adapters in under 5 seconds; the same suite also passes against Postgres in Testcontainers.
- The notification flow survives a crash between commit and publish (outbox crash test, 100 runs, zero lost or duplicate notifications).
- At least 6 ADRs and a utility tree with 8 scenarios, each linked to the code or test that addresses it.
- An external team runs Lab 8 (ATAM-lite) on it; you respond to every risk in writing.

**Stretch goals:** extract `notifications` into a separate service with a strangler-style routing switch and show the before/after deploy independence; add a fitness function for p95 latency of the booking endpoint.

**What it proves to an employer:** you can structure a real codebase so a team (and its agents) can change it without breaking it, and you can defend the structure.

### P3 · Architecture under change: evolve a system and measure it (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** platforms that start as one app and must grow new channels and partners, such as Indian commerce sellers joining ONDC's asynchronous network while keeping their existing storefront, or any SaaS adding a public API and a partner integration. Load and team numbers are **illustrative**.

**What to build:** start from your P2 system or a provided seller-catalogue-and-orders monolith. Deliver three evolution steps, each with an ADR and measurements:
1. Add a partner channel that speaks an asynchronous callback protocol modelled on ONDC's `search`/`on_search` pattern, behind an anti-corruption layer.
2. Replace the persistence of one module behind a branch-by-abstraction seam, with no long-lived branch.
3. Decide, with evidence, whether to extract one module as a service; if yes, extract it with strangler routing and contract tests; if no, write the ADR that says what would change your mind.

Run an agent experiment: 15 realistic change requests implemented by a coding agent under your guardrails, all reviewed by you.

**Acceptance criteria:**
- Before/after metrics for each step: instability and distance for touched packages, cycle count, change coupling between modules, test runtime, and files touched per feature (computed by a script in the repo).
- The partner channel handles duplicate and out-of-order callbacks correctly (property-based test with at least 1,000 generated sequences).
- Zero downtime during the persistence switch under a k6 load of 200 requests/s (k6 output included).
- Agent experiment report: violations attempted, blocked by guardrails, and slipped through (with the fix), and median review time per agent PR.
- A 10-minute recorded presentation of the extraction decision, including what you gave up.

**Stretch goals:** publish the fitness-function setup as a reusable template; add an event-sourced audit log for orders and show one question it answers that the CRUD model could not.

**What it proves to an employer:** you can change architecture safely under load, decide with numbers, and keep a codebase healthy when agents write much of the code. This is staff-track evidence.

## Feeds into

- [SWE401 Large-Scale System Design](../../year_4/SWE401_large_scale_system_design/README.md): P2 and P3 boundaries become the service and data boundaries of a large design.
- [SWE402 Legacy Modernization and Refactoring with AI](../../year_4/SWE402_legacy_modernization_and_refactoring_with_ai/README.md): branch by abstraction and strangler routing at production scale.
- [SWE304 AI-Assisted Software Engineering](../SWE304_ai_assisted_software_engineering_agents/README.md): Lab 10 guardrails become part of the team agent workflow.
- [OV02 Cloud-Native Backend](../../../../04_overlaps/OV02_cloud_native_backend/README.md) and the [SWE flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SWE_software_engineering.md): P3 is the architecture core.
