# QAE302 · Test Automation Engineering: UI and API

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [QAE402](../../year_4/QAE402_testing_ai_systems_evals_and_non_determinism/README.md); feeds [QAE304](../QAE304_testing_in_ci_cd_and_test_infrastructure/README.md), [QAE305](../QAE305_mobile_and_cross_browser_testing/README.md), [QAE401](../../year_4/QAE401_ai_in_testing_generated_tests_self_healing/README.md) |

Part of the [Software Quality and Test Engineering major](../../README.md). Take it alongside [QAE301](../QAE301_testing_foundations_and_test_design_techniques/README.md): QAE301 decides what to test, this course builds the automation that checks it on every change. Frontend students meet the same tools from the component side in [FE305](../../../frontend_engineering/year_3/FE305_frontend_testing_and_tooling/README.md).

## Why this course matters now

Browser automation changed shape in 2025–2026. Playwright (1.64 on npm in October 2026) ships planner, generator and healer agents since 1.56 and bundles an MCP server since 1.62, so coding agents can open a browser, click through a flow and write the test. Selenium (4.51) is moving its implementation from WebDriver Classic to WebDriver BiDi, the W3C bidirectional protocol (a Working Draft, latest dated 8 October 2026) that its documentation calls the cross-browser replacement for the Chrome DevTools Protocol. Writing a test is now cheap; keeping thousands of them fast, deterministic and meaningful is not. Google reported that about 1.5% of its test runs were flaky and that 84% of the pass-to-fail transitions it observed in CI involved a flaky test. An SDET is valuable for the framework design, test data, contract boundaries and flake diagnosis that keep a suite trustworthy, and for reviewing the tests that agents now produce.

## Learning outcomes

By the end you can:

1. **Explain** how WebDriver Classic, WebDriver BiDi, CDP and Playwright's protocol drive a browser, and **predict** what each makes easy or hard (waits, network control, multiple tabs, iframes).
2. **Build** a Playwright Test suite with role-based locators, web-first assertions, fixtures, projects, authentication state, network mocking and traces, with no fixed sleeps.
3. **Compare** Playwright, Selenium 4 and Cypress on a real suite and **write** a tool recommendation with evidence.
4. **Design** a maintainable framework using page or component objects or the Screenplay pattern, and **justify** the layering.
5. **Test** REST APIs with pytest + httpx, REST Assured and Postman/Newman, including schema validation and property-based API testing (Schemathesis).
6. **Implement** consumer-driven contract tests with Pact and a `can-i-deploy` gate.
7. **Manage** test data with builders, API seeding, containers and service virtualisation, without copying production personal data.
8. **Diagnose** flaky tests from traces and logs to a root cause, and **prevent** the common causes by design.
9. **Review** AI-generated automation for weak locators, missing assertions and hidden waits, and **measure** it against planted bugs.

## Chapters and lessons

### Chapter 1 · Automation strategy and framework architecture (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What to automate | Automation ROI: run frequency, stability, risk, oracle clarity; checks that should stay exploratory | Score 30 test ideas from QAE301 for automation value |
| 1.2 Layers | Test layer, domain/action layer, driver/client layer; test code as production code (review, lint, types) | Draw the layer diagram of an open-source Playwright suite |
| 1.3 Language and runner choice | TypeScript + Playwright Test, Python + pytest, Java + JUnit; parallel runners and fixtures | Same smoke test in two stacks; compare setup and run time |
| 1.4 Anti-patterns | Ice-cream-cone suites, UI tests for API logic, record-and-playback without design, shared accounts | Audit a provided suite; list 10 anti-patterns with fixes |

**Check your understanding:** Why should most business-rule checks run below the UI? What makes a test "cheap to keep" rather than cheap to write? When is a record-and-playback script acceptable?

### Chapter 2 · How browsers are driven (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 WebDriver Classic | W3C WebDriver: HTTP commands, sessions, element references, drivers per browser; why polling waits | Drive a browser with raw WebDriver HTTP calls using `curl` |
| 2.2 WebDriver BiDi and CDP | Event streams (console, network, log), bidirectional messages; CDP as Chromium-specific; Selenium's move to BiDi | Capture console errors with Selenium BiDi; compare with CDP |
| 2.3 Playwright's model | Browser contexts, auto-waiting and actionability checks, patched browser builds vs branded Chrome | Show the actionability checks that fire before a click in a trace |
| 2.4 Cypress's model | Test code running inside the browser's event loop; retry-ability; consequences for multiple tabs and origins | Write the same multi-tab flow in Cypress and Playwright; record the workarounds |

**Check your understanding:** Why does a protocol with events make waiting more reliable than polling? What does "Playwright's WebKit" not guarantee about Safari on an iPhone? Why does Cypress find some cross-origin flows harder?

### Chapter 3 · Playwright in depth (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Locators | `getByRole`, `getByLabel`, `getByTestId`; strictness; why CSS/XPath chains break; accessible names as stable contracts | Replace 20 brittle selectors in a legacy suite |
| 3.2 Assertions and waiting | Web-first assertions (`toHaveText`, `toBeVisible`), auto-retry, timeouts; never `waitForTimeout` | Remove every sleep from a suite and keep it green |
| 3.3 Fixtures and projects | Custom fixtures, worker vs test scope, projects per browser and device, `storageState` for login | Log in once per worker via API; reuse auth across 50 tests |
| 3.4 Network and time | `page.route` mocking and modification, HAR replay, the clock API for timers and dates | Test a "session expires after 15 minutes" banner in under 1 second |
| 3.5 Debugging | Trace viewer, UI mode, HTML report, video; ARIA snapshots (`toMatchAriaSnapshot`) for structure | Diagnose 3 failing tests from traces only |
| 3.6 Visual checks | `toHaveScreenshot`, thresholds, masking dynamic regions, platform-specific baselines | Add visual checks to 5 pages without false failures across 20 runs |

**Check your understanding:** Why are role-based locators also an accessibility check? When should you mock the network in an end-to-end test, and what do you lose? Why do screenshot baselines differ between operating systems?

### Chapter 4 · Selenium, Cypress and choosing a tool (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Selenium 4 | Explicit waits, Selenium Manager, Grid, BiDi features (network interception, log events); language bindings | Port 10 Playwright tests to Selenium (Java or Python) |
| 4.2 Cypress | `cy.intercept`, component testing, retry-ability, time travel; current browser support (check the docs on the day) | Port the same 10 tests to Cypress |
| 4.3 Choosing | Decision matrix: languages, browsers, parallelism, debugging, ecosystem, team skills, licence and vendor services | Write a one-page recommendation for an illustrative team of 12 |
| 4.4 Migration | Strangler migration of a large Selenium suite; running both in CI during transition | Plan the migration of a 2,000-test suite with milestones |

**Check your understanding:** When is Selenium still the right choice in 2026? What would make you pick Cypress for a frontend-heavy team? What is the biggest risk in a "big bang" migration?

### Chapter 5 · Patterns for maintainable suites (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Page and component objects | Fowler's page object; component objects for repeated widgets; assertions outside page objects | Refactor a flat suite into page and component objects |
| 5.2 The Screenplay pattern | Actors, abilities, tasks, interactions, questions (Serenity/JS); composition over inheritance | Re-express 5 flows as Screenplay tasks; compare readability |
| 5.3 Test readability | DAMP over DRY in tests; builders and fluent APIs; naming by behaviour | Peer-review a classmate's suite with a checklist |
| 5.4 Framework hygiene | Linting (eslint-plugin-playwright), type checks, code review rules for tests, ownership | Add lint and type gates that fail on `waitForTimeout` and `.only` |

**Check your understanding:** Why should page objects avoid assertions? When does Screenplay pay off over page objects? Why is duplicated setup sometimes better than a clever helper?

### Chapter 6 · API testing (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 HTTP for testers | Methods, status codes, idempotency (RFC 9110), caching headers, pagination, error formats (RFC 9457 problem details) | Write the expected-behaviour table for 8 endpoints |
| 6.2 pytest + httpx | Fixtures, parametrisation, auth flows (OAuth 2.0, JWT expiry), async clients, response timing | 40 API tests for the RealWorld API |
| 6.3 REST Assured and Newman | Java given/when/then DSL; Postman collections run headless with Newman in CI | Run one collection in Newman with environment files and JUnit output |
| 6.4 Schema and property-based API testing | JSON Schema and OpenAPI validation; Schemathesis generating requests from an OpenAPI spec | Run Schemathesis against your API; triage every failure |
| 6.5 Beyond REST | GraphQL (query depth, partial errors), gRPC (proto contracts, `grpcurl`), webhooks with signature checks | Test one GraphQL and one gRPC endpoint |

**Check your understanding:** Why must a retried `POST /payments` with the same idempotency key not create a second payment, and how do you test it? What does Schemathesis find that hand-written tests rarely do? Why is a 200 response with an error body a bug?

### Chapter 7 · Contract testing (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Why contracts | Consumer-driven contracts (Fowler); contracts vs end-to-end tests across teams | List 5 integration bugs a contract would have caught |
| 7.2 Pact | Consumer tests generate pacts; provider verification; provider states; matchers | Pact between a small consumer you write and the RealWorld API |
| 7.3 Broker and deployment safety | Pact Broker, versions and tags, `can-i-deploy`, webhooks | Block a deploy when the provider renames a field |
| 7.4 Other contract styles | Bi-directional (OpenAPI-based) contracts; message pacts for events; schema registries | Write a message pact for an "order placed" event |

**Check your understanding:** Why are consumer-driven contracts cheaper than a shared end-to-end environment? What does a contract test not prove? Who should own provider states?

### Chapter 8 · Test data and environments (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Data isolation | Per-test data, unique keys, cleanup vs disposable environments; shared-account failures | Make 50 tests safe to run in parallel |
| 8.2 Seeding | Seed through APIs, not the UI; builders and factories; Faker with the `en_IN` locale | Build a data factory for users, orders and addresses |
| 8.3 Containers and virtualisation | Testcontainers; WireMock and Mock Service Worker; Playwright route stubs; when to virtualise a payment gateway | Stub a slow third-party API with injected latency and errors |
| 8.4 Privacy | Masking, subsetting and synthetic data; why copying production personal data into test is a DPDP Rules 2025 risk | Write a test-data policy for an illustrative fintech |

**Check your understanding:** Why does seeding through the UI make suites slow and flaky? When is a virtualised dependency more dangerous than helpful? What makes synthetic data realistic enough?

### Chapter 9 · Flaky tests: diagnosis and prevention (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Definition and cost | Google's definition (pass and fail on the same code); 1.5% of runs, 16% of tests, 84% of pass-to-fail transitions (2016) | Compute your suite's flaky rate from 100 runs |
| 9.2 Root-cause families | Async waits, concurrency, test-order dependence, shared state, time and time zones, randomness, resource leaks, infrastructure | Classify 10 provided flaky tests by family |
| 9.3 Detection | `--repeat-each`, shuffled order (`--shuffle` since 1.64), stress on CPU, trace diffing between pass and fail | Reproduce 3 flaky tests deterministically |
| 9.4 Fix, not retry | Why retries hide bugs; when a quarantine is acceptable (owner, deadline); fixes per family | Fix the 3 tests; prove 500 clean runs |

**Check your understanding:** Why can a flaky test hide a real race condition in the product? When is a retry legitimate? What evidence proves that a flaky test is fixed?

### Chapter 10 · AI-assisted automation (weeks 11–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Agents that write tests | Playwright MCP and test agents (planner, generator, healer); codegen; coding agents with browser access | Generate 15 tests for P3's app with the planner and generator |
| 10.2 Reviewing generated tests | Checklist: locator quality, real assertions, no sleeps, data isolation, traceability to risk | Review 15 generated tests; reject or fix each with a reason |
| 10.3 Measuring them | Plant 10 bugs; count which tests fail; mutation testing of page logic | Compare generated vs hand-designed tests on planted bugs |
| 10.4 Healing with care | When a healer edits a locator vs an assertion; why an automatic fix can turn a regression green | Run the healer on 5 broken tests where 2 are real regressions; record what it does |

**Check your understanding:** Why must a human approve any healer change that touches an assertion? What does a generated test usually get wrong about test data? How would you prove that agent-written tests add value?

### Chapter 11 · Framework capstone (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Documentation | README for contributors, conventions, how to add a test in 10 minutes | Have a classmate add a test using only your README |
| 11.2 Reporting | Playwright HTML report, traces as CI artefacts, Allure Report basics | Publish reports from CI for every run |
| 11.3 Handover | Ownership, flakiness budget, review rules for test changes | Present P3 to a panel |

**Check your understanding:** What would make your framework fail when a new team joins? Which report would a developer actually open after a failure? What is your suite's flakiness budget, and who enforces it?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Suite audit | — |
| 2 | 2 | Lab 2 · Raw WebDriver and BiDi | — |
| 3 | 3 | Lab 3 · Locators and zero-sleep suite | — |
| 4 | 3 | Lab 4 · Network, clock and traces | **P1 due** |
| 5 | 4–5 | Lab 5 · One flow, three tools | Tool recommendation |
| 6 | 5–6 | Lab 6 · Patterns refactor | — |
| 7 | 6 | Lab 7 · API and Schemathesis | Mid-term (AI off) |
| 8 | 7 | Lab 8 · Pact and can-i-deploy | — |
| 9 | 8 | Lab 9 · Data factory and virtualisation | **P2 due** |
| 10 | 9 | Lab 10 · Flake hunt | — |
| 11 | 10 | P3 build | — |
| 12 | 10 | AI generation and review | Review log |
| 13 | 10 | Healer experiment | — |
| 14 | 11 | P3 | **P3 due** |
| 15 | Review | P3 panel | Final exam (AI off): framework design and flake diagnosis |

## Working with AI in this course

- **Use AI for:** first drafts of tests from your QAE301 designs; converting tests between tools; writing data factories and fixtures; explaining an unfamiliar trace; generating Postman collections from an OpenAPI file. Tools: Playwright test agents and MCP server, Claude Code, Codex, GitHub Copilot, Cursor, Chrome DevTools MCP.
- **Do without AI (drills):** the first locator-repair lab, the first API suite, the Pact setup, every flake diagnosis (you must read traces yourself), the framework layer design, the mid-term and the final.
- **Verify AI output by:** running each generated test against a deliberately broken build (it must fail); linting for sleeps, `.only` and CSS-chain selectors; running new tests 100 times with `--repeat-each` before merge; checking assertions verify outcomes (state, data, messages), not just that a page loaded; reading every healer diff.
- **Where AI still fails here (show it):** your Lab and P3 logs must record generated tests that pass on broken builds, brittle selectors, invented test IDs that do not exist in the DOM, hard waits, shared data that breaks parallel runs, and healer edits that weaken assertions. The course grades the evidence, not the tool.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| P1, P2, P3 | 10%, 20%, 25% |
| Mid-term (AI off): API tests and locator repair | 5% |
| Final exam (AI off) + P3 panel | 20% |

**Mastery gate.** You pass when you can: (1) given an unfamiliar web app with an OpenAPI spec, deliver in one working day a Playwright + API suite of 30 tests with API-seeded data that runs in parallel on 4 workers and passes 200 consecutive runs with no flaky result; (2) with AI off, take 5 flaky tests and identify the root-cause family of at least 4 from traces and logs within 60 minutes; (3) show a Pact contract that blocks a breaking provider change in CI.

## Industry reality

UI and API automation is the core of SDET and automation-engineer roles in both product and services companies (see the [market page](../../../../06_career_and_market_readiness/01_market_map/roles/QAE_software_quality_test_engineering.md)). Public practice to study: Google's flaky-test data and mitigation approach (2016); Playwright, Selenium and Cypress are open-source projects with public issue trackers and release notes; Pact is maintained by the open-source Pact Foundation. Framework design and flake diagnosis are standard interview rounds.

**Interview questions from this course**

1. *Playwright or Selenium for a new project?* Strong answer: depends on languages, browsers, team skills and existing grid; explains auto-waiting and contexts vs WebDriver's model and BiDi's arrival; mentions real Safari and mobile needs; proposes a spike measured on real flows.
2. *A UI test fails one run in fifty. Walk me through it.* Strong answer: reproduce with repeats and shuffled order, compare traces of pass and fail, classify the cause (wait, data, order, time, infrastructure), fix the cause, prove with hundreds of clean runs; quarantine only with owner and deadline.
3. *Design an automation framework for a 30-developer product with web, API and two partner integrations.* Strong answer: layers, most checks at API and contract level, a thin UI layer, data factories, parallel isolation, contract tests with partners, reporting, ownership, flakiness budget, CI integration.
4. *How do you test that an API is idempotent?* Strong answer: same request with the same idempotency key returns the same result and creates one resource; concurrent duplicates; different payload with the same key is rejected; expiry of keys; checks the database or ledger, not only the response.
5. *An agent generated 200 Playwright tests overnight. What do you check before merging?* Strong answer: run against a broken build, assertion quality, locator strategy, no sleeps, data isolation, duplicates, traceability to risk, repeat runs for flakiness, and who owns them.

## Resources (free first)

- **Documentation:** Playwright — https://playwright.dev/ (best practices https://playwright.dev/docs/best-practices , test agents https://playwright.dev/docs/test-agents , API testing https://playwright.dev/docs/api-testing , mocking https://playwright.dev/docs/mock ) ; Selenium — https://www.selenium.dev/documentation/ and BiDi https://www.selenium.dev/documentation/webdriver/bidi/ ; Cypress — https://docs.cypress.io/app/get-started/why-cypress ; W3C WebDriver BiDi — https://www.w3.org/TR/webdriver-bidi/
- **API and contracts:** pytest — https://docs.pytest.org/ ; HTTPX — https://www.python-httpx.org/ ; REST Assured — https://rest-assured.io/ ; Newman — https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/ ; Schemathesis — https://schemathesis.readthedocs.io/ ; Pact — https://docs.pact.io/ ; Martin Fowler, "Consumer-Driven Contracts" — https://martinfowler.com/articles/consumerDrivenContracts.html
- **Patterns and data:** Martin Fowler, "PageObject" — https://martinfowler.com/bliki/PageObject.html ; Serenity/JS Screenplay pattern — https://serenity-js.org/handbook/design/screenplay-pattern/ ; Testcontainers — https://testcontainers.com/ ; WireMock — https://wiremock.org/
- **Flakiness:** Google Testing Blog, "Flaky Tests at Google and How We Mitigate Them" — https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html ; Martin Fowler, "Eradicating Non-Determinism in Tests" — https://martinfowler.com/articles/nonDeterminism.html ; Gruber and Fraser, developer survey on flakiness (arXiv 2203.00483) — https://arxiv.org/abs/2203.00483
- **Practice apps:** RealWorld — https://docs.realworld.show/ ; OWASP Juice Shop (rich UI flows; run locally) — https://github.com/juice-shop/juice-shop ; .NET eShop — https://github.com/dotnet/eShop ; Online Boutique — https://github.com/GoogleCloudPlatform/microservices-demo

## Sources

All checked 12 Oct 2026.

- npm registry, latest versions on 12 Oct 2026: @playwright/test 1.64.0, selenium-webdriver 4.51.0, cypress 16.1.1, webdriverio 10.0.2, @pact-foundation/pact 17.1.4, newman 6.2.3 — https://registry.npmjs.org/ ; PyPI: pytest 9.1.1, httpx 0.28.1, schemathesis 4.30.1, selenium 4.51.0 — https://pypi.org/
- Playwright release notes (agents 1.56; bundled MCP 1.62; `--shuffle` 1.64; clock API 1.45) — https://playwright.dev/docs/release-notes
- W3C, WebDriver BiDi, Working Draft (8 Oct 2026) — https://www.w3.org/TR/webdriver-bidi/
- Selenium documentation, "WebDriver BiDi" (implementation moving from Classic to BiDi; CDP support temporary) — https://www.selenium.dev/documentation/webdriver/bidi/
- John Micco, "Flaky Tests at Google and How We Mitigate Them" (27 May 2016) — https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html
- PIB, DPDP Rules notified (14 Nov 2025) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014

_Last reviewed: 2026-10_
