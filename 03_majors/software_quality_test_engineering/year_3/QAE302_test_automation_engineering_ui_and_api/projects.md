# QAE302 · Labs and projects

All targets run locally (Docker Compose or a local Kubernetes cluster such as kind) unless a public demo explicitly allows automated traffic. Flakiness is always measured, never claimed: "passes N consecutive runs" means N full runs in CI or with `--repeat-each`, with the raw results attached. Every project repository includes a CI workflow, a README that lets a stranger add a test in 10 minutes, and an **AI log** (tool, prompt, what was accepted, what was rejected and why).

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Suite audit | Audit an existing open-source end-to-end suite (or the instructor's legacy suite) for anti-patterns | 10 anti-patterns with file and line, cost, and fix | 2 h |
| 2 · Raw WebDriver and BiDi | Drive a browser with raw WebDriver HTTP calls; capture console and network events with Selenium BiDi | Script, logs, and a half-page comparison of polling vs events | 3 h |
| 3 · Locators and zero-sleep suite | Replace 20 brittle selectors with role-based locators; remove all fixed waits | Before/after diff; 100 runs with `--repeat-each` and zero failures | 4 h |
| 4 · Network, clock and traces | Mock a slow and a failing API with `page.route`; test a 15-minute session timeout with the clock API; debug 3 failures from traces only | Tests, trace files, a diagnosis note per failure | 4 h |
| 5 · One flow, three tools | Implement the same 10 tests in Playwright, Selenium 4 and Cypress | Code, run times, lines of code, flake counts over 50 runs, recommendation memo | 6 h |
| 6 · Patterns refactor | Refactor a flat 30-test suite into component objects, then 5 flows into Screenplay tasks | Both versions; a reviewer's readability scores; your judgement | 4 h |
| 7 · API and Schemathesis | 40 pytest + httpx tests for the RealWorld API; one Newman collection in CI; a Schemathesis run | Suite, JUnit/HTML reports, every Schemathesis failure triaged (bug, spec gap, false alarm) | 5 h |
| 8 · Pact and can-i-deploy | Consumer contract for a small client; provider verification; a broker (Docker) with `can-i-deploy` | Pipeline run that blocks a field rename, and one that passes after the consumer updates | 5 h |
| 9 · Data factory and virtualisation | Builders and factories (Faker `en_IN`), API seeding, Testcontainers PostgreSQL, a WireMock stub with latency and error injection | Factory code, 50 tests passing on 8 parallel workers, test-data policy (1 page) | 5 h |
| 10 · Flake hunt | 10 provided flaky tests across all root-cause families | Deterministic reproduction, root cause, fix and 500 clean runs for at least 7 of them | 6 h |

## Projects

### P1 · Zero-flake Playwright suite for a real app (L1, ~6 hours)

**Real-world inspiration:** teams that adopt Playwright and must keep the first suite trustworthy enough that developers do not learn to ignore it.

**What to build:** 25 Playwright Test tests for a locally run [RealWorld (Conduit)](https://docs.realworld.show/) frontend and backend covering sign-up, login, article create/edit/delete, comments, favourites, follow and pagination, plus 5 negative paths.

**Acceptance criteria:**
- Only role, label, text or test-id locators; zero `waitForTimeout`; lint rule enforces both.
- Login via API and `storageState`, not the UI (except one dedicated login test).
- 200 consecutive runs (`--repeat-each=8` across 25 tests, or CI reruns) with a flaky rate of 0%.
- Full suite under 3 minutes on 4 workers on a laptop; run time reported.
- Traces kept on failure and uploaded as CI artefacts.

**Stretch goals:** run the suite on Chromium, Firefox and WebKit projects and report engine-specific failures.

**What it proves to an employer:** you write UI automation that a team can rely on from day one.

### P2 · API and contract safety net (L2, ~15 hours)

**Real-world inspiration:** service teams that stop breaking each other through consumer-driven contracts instead of one shared, fragile end-to-end environment.

**What to build:** for the RealWorld API (or an approved alternative with an OpenAPI spec), a pytest + httpx suite with schema validation, a Schemathesis property-based run in CI, and Pact contracts for two consumers you write (a web client and a "mobile" client that use different fields), with a Pact Broker and a `can-i-deploy` gate.

**Acceptance criteria:**
- ≥ 80 API tests covering every endpoint's success, validation and auth-failure paths; idempotency and pagination tested where the API supports them.
- Schemathesis runs in CI on every change; every failure is triaged in an issue (bug, spec gap or false positive).
- A demonstration pipeline where a provider change that breaks only the mobile consumer is blocked, while a change that breaks no consumer is allowed.
- API suite runtime under 60 seconds on 4 workers; flaky rate 0% over 100 runs.
- Mutation testing (mutmut or Stryker, depending on the provider's language) on one provider module shows which API tests kill mutants; score reported.

**Stretch goals:** add a message pact for an asynchronous "article published" event; add gRPC or GraphQL tests to a second service.

**What it proves to an employer:** you can protect service boundaries at the cheapest level and explain why it is cheaper than end-to-end tests.

### P3 · Production-grade automation framework for a multi-service app (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** SDET teams that own the shared test framework for many product teams. Target: [.NET eShop](https://github.com/dotnet/eShop), [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo) or one module of [ERPNext](https://github.com/frappe/erpnext), run locally.

**What to build:** a framework with UI (Playwright, page/component objects or Screenplay), API and contract layers; a test-data service (factories, seeding, cleanup); service virtualisation for one external dependency; CI with parallel runs, traces, an HTML or Allure report and a flaky-test detector (nightly repeat runs that flag any test with mixed results). Include 3 deliberately flaky tests injected by a classmate, which you must find and fix.

**Acceptance criteria:**
- ≥ 120 tests across layers, with at least 60% below the UI; each test traces to a risk from your QAE301-style risk register.
- Flaky rate < 0.5% of test executions over 200 full CI runs (attach the raw data), after fixing the 3 injected flaky tests, each with a written root cause.
- 10 planted product bugs (planted by the instructor or a classmate): the suite detects at least 9.
- Full suite under 10 minutes in CI with parallelism; per-layer timing reported.
- A newcomer adds a passing test using only your README in under 15 minutes (recorded).
- AI log: at least 20 AI-generated tests reviewed, with acceptance rate, reasons for rejection, and the number that failed on a broken build.

**Stretch goals:** visual and accessibility smoke checks with thresholds; a Slack- or email-style failure summary that links traces; run the framework against a second app to prove it is reusable.

**What it proves to an employer:** you can design and own the automation framework that a whole engineering organisation depends on, with numbers to show it is fast and trustworthy.

## Feeds into

- [QAE304 Testing in CI/CD and Test Infrastructure](../QAE304_testing_in_ci_cd_and_test_infrastructure/README.md): P3's framework is sharded, selected and gated at scale.
- [QAE305 Mobile and Cross-Browser Testing](../QAE305_mobile_and_cross_browser_testing/README.md): the same patterns on device farms.
- [QAE401 AI in Testing](../../year_4/QAE401_ai_in_testing_generated_tests_self_healing/README.md): the healer experiment and AI log grow into a full evaluation.
- [QAE402 Testing AI Systems](../../year_4/QAE402_testing_ai_systems_evals_and_non_determinism/README.md): API test skills become eval harnesses.
- [QAE flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/QAE_software_quality_test_engineering.md): P3 is its automation layer.
