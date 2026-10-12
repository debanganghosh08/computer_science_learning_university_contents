# SWE302 · Labs and projects

Use Java 21+ or TypeScript (strict mode) for the labs; Go or Python are accepted for P1. All LLD labs require runnable code with tests, not diagrams alone. Labs 3 and 5 and both mock rounds are AI-off and timed. In other labs, agents are allowed, but every agent-written line must survive your review, and you log what you changed.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Value objects, invariants and types | Replace primitives in a provided order module with `Money` (integer paise), `PinCode`, `PhoneNumber`, `DateRange`; then model payment states with sealed types / discriminated unions so that 4 listed illegal states cannot compile | Diff; at least 5 bugs the compiler or constructors now reject, each with a test; 4 snippets that fail to compile, with the errors | 7 h |
| 2 · SOLID and its costs | Refactor `InvoiceService` by actor; add a new GST rule through an extension point; then argue whether the extension point was worth it | Before/after code, files touched for the new rule, and a 300-word verdict | 5 h |
| 3 · Parking lot, timed (AI off) | 60-minute LLD with code: multi-gate, multiple spot types, pluggable fee strategies | Code, 10+ tests, a concurrency test with 1,000 simultaneous arrivals and zero double allocation | 2 h |
| 4 · Rate limiters and caches | Five rate-limiting algorithms; O(1) LFU cache with TTL | Property tests against reference models (10,000 random operations each); JMH results at 1, 8 and 64 threads | 6 h |
| 5 · Splitwise and elevator (AI off for the design) | Splitwise with equal/exact/percentage splits and greedy simplification; 4-car elevator simulation with LOOK scheduling | Tests showing splits always sum to the total; elevator average and p95 wait under a morning-rush trace | 6 h |
| 6 · Seat locking under contention | Seat hold/confirm/expire with three strategies (row lock, optimistic version, conditional update) on Postgres | 10 runs × 1,000 clients for 100 seats: zero double bookings, plus throughput and p99 per strategy | 5 h |
| 7 · Gilded Rose in small steps | Characterisation tests first, then refactor in at least 25 green-to-green commits | Commit history, final design, and the list of refactorings used by name | 4 h |
| 8 · Metrics vs human judgement | Score 10 snippets with cyclomatic and cognitive complexity; collect readability ratings from 8 classmates | Correlation table and a paragraph on where metrics and humans disagree | 3 h |
| 9 · AI-PR review gauntlet | Split a 1,200-line branch into stacked changes; then review 6 agent-written PRs (planted issues) yourself, then with two AI reviewers | The stacked changes; your findings, each tool's findings, and a confusion matrix against the answer key | 5 h |
| 10 · Codemod vs agent | Replace a deprecated API across an open-source repo with OpenRewrite/jscodeshift and separately with a coding agent | Correctness (compile + tests), review time and error count for each approach | 5 h |

## Projects

### P1 · LLD kata pack (L1, ~6 hours)

**Real-world inspiration:** machine-coding rounds in Indian product-company interviews, and the internal libraries every company ends up writing (rate limiting, caching, notifications).

**What to build:** three timed solutions, each done in a single sitting with no AI: (a) a vending machine as a state machine, (b) a notification dispatcher with channel strategies (SMS, email, push) and retries, (c) a snake-and-ladder or cab-allocation game engine. Then one untimed revision pass per solution.

**Acceptance criteria:**
- Each timed solution compiles and runs from a single command, with at least 8 tests, completed within 90 minutes (screen recording or commit timestamps as evidence).
- The revision pass lists every change and the smell it removed.
- No mutable global state; every external effect (clock, randomness, I/O) is injected.
- A peer can add one new requirement to each solution (given by the instructor) by touching at most 3 files.

**Stretch goals:** redo one kata in a second language and compare; record a 10-minute "interview narration" for one solution.

**What it proves to an employer:** you produce clean, extensible, tested code under time pressure, which is exactly what LLD rounds measure.

### P2 · Group-expense service with exact money (L2, ~15 hours)

**Real-world inspiration:** Splitwise-style apps and the group-split features inside Indian payment apps. All business numbers are an **illustrative scenario**.

**What to build:** a service (HTTP or CLI) for groups, expenses, splits (equal, exact, percentage, shares), balances, settlement suggestions and settlement recording. Money is stored in integer paise with a documented rounding rule. Include an audit log of every balance change and a simplification module with a greedy algorithm and an exact algorithm for small groups.

**Acceptance criteria:**
- Conservation invariant: across 100,000 randomly generated operations (property-based test), the sum of all balances in a group is always exactly zero.
- Splits always sum to the expense total; the rounding remainder goes to a deterministic member (documented and tested).
- Greedy simplification uses at most n−1 transfers; for groups of up to 12 members, a report compares greedy with the exact minimum on 500 random groups.
- Concurrent expense additions to the same group (100 threads × 100 expenses) produce correct balances.
- Cognitive complexity of every function ≤ 15 (enforced in CI); duplication below 3% (jscpd or PMD CPD).
- Design doc (2 pages) with class diagram, state diagram for a settlement, and 3 ADRs.

**Stretch goals:** multi-currency with fixed exchange snapshots; an export that reconciles against a bank statement CSV.

**What it proves to an employer:** you can model money correctly, prove invariants with tests, and keep code quality measurable.

### P3 · Code-health programme for a real open-source codebase (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** platform and developer-experience teams at large companies run code-health work: style automation, codemods, review policies and quality ratchets. Google's large-scale change process is described in *Software Engineering at Google*.

**What to build:** choose an active open-source project (at least 50,000 lines, at least 20 contributors in the last year; get maintainer interest in an issue first). Deliver:
1. A code-health baseline: complexity distribution, duplication, hotspots (churn × complexity), review latency from PR data.
2. Two real improvements submitted upstream: one refactoring of a hotspot with characterisation tests, and one codemod-driven mechanical change (for example replacing a deprecated API).
3. A review and agent policy proposal for the project: PR size guidance, evidence requirements for AI-generated PRs, and a ratchet for one metric, with a working CI configuration on your fork.
4. An agent experiment: the same 5 small issues done by you and by a coding agent under your review; record time, defects found in review, and rework.

**Acceptance criteria:**
- Baseline report reproducible from one script; numbers match a second run within 1%.
- At least one upstream PR merged, or a maintainer's written review addressed in full (link included).
- The hotspot refactor keeps behaviour: characterisation tests pass before and after, and mutation score on the refactored code does not drop.
- The codemod runs on the full repository, compiles, passes the test suite, and its diff is split into reviewable shards of at most 400 lines.
- The agent experiment reports medians with the raw data and states its limitations (sample size, task selection).

**Stretch goals:** get the ratchet adopted upstream; write a blog post on what the agent got wrong and how review caught it.

**What it proves to an employer:** you can improve a large codebase you do not own, through the social process of open source, with measurements. That is senior-engineer behaviour.

## Feeds into

- [SWE402 Legacy Modernization and Refactoring with AI](../../year_4/SWE402_legacy_modernization_and_refactoring_with_ai/README.md): characterisation tests, codemods and the agent-vs-codemod comparison at migration scale.
- [SWE304 AI-Assisted Software Engineering](../SWE304_ai_assisted_software_engineering_agents/README.md): the review policy from P3 becomes part of a team agent workflow.
- [CAR301](../../../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) and [CAR401](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): P1 and the mock rounds are your LLD interview preparation; P3's upstream PRs count as open-source portfolio work.
