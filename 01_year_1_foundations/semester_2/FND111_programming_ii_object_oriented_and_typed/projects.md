# FND111 · Labs and projects

Every lab and project is done in one Git repository with a GitHub Actions matrix that builds the Java (JDK 25, Maven or Gradle) and TypeScript (Node.js 24, `tsc --strict`) halves on every push. "Green" means compile, tests, linters and the mutation threshold all pass in CI, not only on your laptop.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Two toolchains, one CI | Set up JDK 25 + Maven/Gradle + JUnit 6 and Node 24 + strict TypeScript + Vitest 5; one workflow runs both suites | Repo link, green badge, a README with one-line run commands | 4 h |
| 2 · Payment state machine | Model `Initiated → Pending → Success / Failed(reason) → Reversed` as a sealed interface with pattern-matching `switch` and as a discriminated union with `assertNever`; adding `Disputed` must break compilation in both | Code, tests, and the compiler errors you got when one case was missing | 4 h |
| 3 · Breaking equality | Corrupt a `HashSet` with a mutable key; write `equals` without `hashCode` and watch `HashMap` fail; show that a JavaScript `Map` keys objects by reference; fix each | A bug report per failure (reproduction, cause, fix) plus regression tests | 3 h |
| 4 · Composition refactor | Turn a 6-subclass `Notifier` hierarchy (SMS, email, WhatsApp × retry/no-retry) into composed parts without changing behaviour | Before/after class diagrams, untouched tests still green, class count before and after | 4 h |
| 5 · Generics | Build `LruCache<K, V>`, `Result<T, E>` and a type-safe `pick(obj, keys)`; answer a 10-item variance quiz with code | Code, tests, a one-page explanation of PECS with your own example | 5 h |
| 6 · Error design | Import 100,000 synthetic UPI-style transaction rows with 1% seeded bad rows; report every bad row by line and reason; prove files close when parsing throws | Code, the error report, a test that fails if a resource leaks | 4 h |
| 7 · Collections and Unicode | Word and character frequencies over mixed Hindi–English text; grapheme-correct counts with `Intl.Segmenter` and `BreakIterator` | Code, a timing table for three collection choices, the justification | 4 h |
| 8 · Mutation testing | Run PIT and StrykerJS on Labs 5–6; raise the mutation score to at least 80% | Before/after mutation reports and a list of the surviving mutants you killed | 5 h |
| 9 · Codebase safari | Build Spring PetClinic or another project of 50,000+ lines; trace one request end to end; open a docs or test PR | One-page code map, PR link, a log of every AI claim about the code marked confirmed or false | 6 h |
| 10 · AI refactor with a verification log | Characterization tests first, then an agent-driven refactor of a legacy module in small steps | The diff, test and mutation reports, and a log table: suggestion, accepted or rejected, evidence | 6 h |

## Projects

### P1 · Gilded Rose rescue, twice (L1, ~6 hours)

**Real-world inspiration.** The [Gilded Rose refactoring kata](https://github.com/emilybache/GildedRose-Refactoring-Kata) is a widely used legacy-code exercise with Java and TypeScript versions: untested nested conditionals, plus a new requirement ("Conjured" items) that cannot be added safely until the code is under test.

**What to build.** In both Java and TypeScript: approval (characterization) tests for the original code, a refactor to polymorphism or a rule table, then the Conjured feature.

**Acceptance criteria**
- Characterization tests cover 30 simulated days for every item type and pass against the original, unmodified code.
- After the refactor, the same tests pass unchanged, and no method has cyclomatic complexity above 5 (PMD for Java, the ESLint `complexity` rule for TypeScript).
- Conjured items degrade twice as fast, with at least 6 dedicated tests that include the boundaries (quality 0, sell-in 0, quality 50).
- Mutation score of at least 80% in both languages.
- At least 10 small commits, each one green in CI.

**Stretch goals.** Repeat the refactor from the original code with an AI agent; compare the two diffs and the time taken, and record one thing the agent did well and one thing it got wrong.

**What it proves to an employer.** You can change code you did not write without breaking it, which is most of the job.

### P2 · Seat reservation engine (L2, ~15 hours, Java)

**Real-world inspiration.** Indian Railways tickets move between confirmed, RAC (Reservation Against Cancellation) and waitlisted states, and cinema apps hold seats for a few minutes before they expire. This project is an illustrative model of those ideas, not of any real system.

**What to build.** A Java library with a small CLI. Trains have coaches and berths; a journey covers a segment of a route (station *i* to station *j*). Bookings are sealed types: `Confirmed(berth)`, `Rac(n)`, `Waitlisted(n)`, `Cancelled`. A cancellation promotes RAC to confirmed and waitlist to RAC in first-come order. Seat holds expire after N minutes through an injected `Clock`. Quota rules (general, ladies, senior citizen) are strategies.

**Acceptance criteria**
- Every `switch` over booking states has no `default` branch; the README shows the compile errors produced by adding a new state.
- A jqwik property test generates 10,000 random booking and cancellation sequences and never finds one berth sold to two passengers on overlapping segments; promotion order is always first-come.
- Hold expiry is tested with a fixed `Clock`; no test calls `Thread.sleep`.
- Line coverage of at least 90% and mutation score of at least 75%; `mvn verify` finishes in under 60 seconds with zero Checkstyle violations against the Google style configuration.
- The README has a class diagram and three design decisions, each with the alternative you rejected and why.

**Stretch goals.** Port the domain core to TypeScript with shared JSON test fixtures. Add a 32-thread booking test with `ExecutorService` and make it pass with locks (a preview of [CS203](../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md)). Persist bookings to SQLite (see [FND115](../FND115_databases_i_data_modeling_and_sql/README.md)).

**What it proves to an employer.** You can turn messy business rules into types and invariants and test them with properties, which is what low-level design and machine-coding rounds look for.

### P3 · Typed payments SDK twins: Java and TypeScript (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Payment companies ship official client libraries in many languages, for example Stripe's [stripe-java](https://github.com/stripe/stripe-java) and [stripe-node](https://github.com/stripe/stripe-node) and Razorpay's [razorpay-java](https://github.com/razorpay/razorpay-java) and [razorpay-node](https://github.com/razorpay/razorpay-node). Stripe documents [idempotent requests](https://docs.stripe.com/api/idempotent_requests) so that a retried payment is never charged twice, and [signed webhooks](https://docs.stripe.com/webhooks).

**What to build.** Write an OpenAPI spec for a small mock payments API (create payment, fetch, list with pagination, refund, webhooks) and serve it locally with [Prism](https://github.com/stoplightio/prism) or your own small server. Then build two SDKs with the same design:
- typed models, with money as integer minor units (paise);
- an error taxonomy as a sealed hierarchy in Java and a discriminated union in TypeScript;
- retries with exponential backoff and jitter, only for safe or idempotency-keyed requests;
- idempotency keys, timeouts, and pagination iterators;
- webhook signature verification (HMAC-SHA256 with constant-time comparison).

**Acceptance criteria**
- A shared contract suite of at least 40 JSON fixtures (request → expected result or typed error) runs against both SDKs, and both pass 100%.
- Fault injection: with the mock returning 30% transient 503 errors and random timeouts, 1,000 create-payment calls produce exactly 1,000 payments and zero duplicates.
- Webhook verification rejects tampered bodies and timestamps older than 5 minutes, with tests for both.
- There is no `any` in the TypeScript public API (`@typescript-eslint/no-explicit-any` set to error) and no raw types in the Java public API. Every public member has Javadoc or TSDoc, and generated API docs are published with GitHub Pages.
- Mutation score of at least 70% in both SDKs; CI runs on JDK 25 and Node 24.
- An AI verification log: at least one large refactor done with an AI agent, behind characterization tests, with diff-review notes and at least one rejected suggestion and the reason.
- The README has a quickstart of 10 lines or fewer per language, semantic versioning and a CHANGELOG.

**Stretch goals.** Generate models with [OpenAPI Generator](https://openapi-generator.tech/) and write up the trade-offs against your hand-written ones. Add [OpenTelemetry](https://opentelemetry.io/docs/) tracing hooks. Package with `mvn install` and `npm pack`, and consume both packages from a separate sample app.

**What it proves to an employer.** You can design a public API that other developers depend on, in two type systems, with the reliability rules that money-moving systems require: retries, idempotency and verified webhooks. It also proves you can use AI on real code and show the evidence that the result is correct.

## Feeds into

- [CS205 Software Engineering I](../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md): design, testing and team workflow build directly on Chapters 8–11 and P3.
- [CS216 Programming Languages, Compilers and Interpreters](../../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md): you will implement the kind of type checker whose behaviour you learned here.
- [CS202 Computer Architecture and Systems Programming in C](../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md): C removes the safety nets you relied on here, and you see what they cost.
- [MOB301 Android with Kotlin](../../../03_majors/mobile_engineering/year_3/MOB301_android_with_kotlin_and_jetpack_compose/README.md) and the mobile major: Kotlin runs on the JVM with the same type ideas.
- [SWE302 Low-Level Design](../../../03_majors/software_engineering/year_3/SWE302_low_level_design_and_clean_code_at_scale/README.md), [SWE304 AI-Assisted Software Engineering](../../../03_majors/software_engineering/year_3/SWE304_ai_assisted_software_engineering_agents/README.md) and [SWE402 Legacy Modernization and Refactoring with AI](../../../03_majors/software_engineering/year_4/SWE402_legacy_modernization_and_refactoring_with_ai/README.md) extend Lab 10 and P1 to whole systems.
- [FND112 Data Structures and Algorithms I](../FND112_data_structures_and_algorithms_i/README.md) uses your Java and testing setup from this term.
