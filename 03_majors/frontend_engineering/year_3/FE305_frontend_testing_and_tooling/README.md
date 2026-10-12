# FE305 · Frontend Testing and Tooling

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [FND114](../../../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [FE401](../../year_4/FE401_full_stack_frameworks_rendering_data_fetching/README.md), [FE404](../../year_4/FE404_frontend_system_design_at_scale/README.md), [IND401](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) |

Part of the [Frontend Engineering major](../../README.md). CS205 taught test design, code review and CI in general. This course applies them to the browser, where tests must deal with rendering, timing, networks, real devices, visual output and a fast-moving toolchain. It pairs with [QAE302](../../../software_quality_test_engineering/year_3/QAE302_test_automation_engineering_ui_and_api/README.md) for students who lean towards quality engineering.

## Why this course matters now

Frontend tooling was rebuilt in native languages in 2025–2026:
- **Vite 8** (March 2026) replaced its esbuild-plus-Rollup pair with Rolldown, a single Rust bundler. Linear reported production builds dropping from 46 s to 6 s in testing.
- **Next.js 16** made Turbopack its default bundler.
- **TypeScript 7.0** (July 2026) type-checks 8–12× faster, but it has no stable programmatic API yet, so linters still run against TypeScript 6.

Testing moved too. Vitest 5 (September 2026) fails unawaited assertions and adds a trace viewer to Browser Mode. Playwright now bundles its MCP server and ships test agents that plan, generate and repair tests. AI writes tests quickly, but a test that passes for the wrong reason is worse than no test. DORA's 2025 research found AI adoption still negatively related to delivery stability. The npm ecosystem is also a target: in September 2025 a self-replicating worm, Shai-Hulud, compromised more than 500 packages and stole developer credentials (CISA). The skill this course builds is owning the quality pipeline: deciding what to test, proving that tests catch real bugs, and keeping builds fast and dependencies trustworthy.

## Learning outcomes

By the end you can:

1. **Design** a test strategy for a frontend product, choosing what to verify at unit, component, integration, end-to-end, visual and accessibility levels, and **justify** it by risk and cost.
2. **Write** behaviour-focused tests with Vitest 5 and Testing Library, controlling network (MSW), time (fake timers, Temporal mocking) and randomness.
3. **Test** in real browsers with Vitest Browser Mode and Playwright, and **eliminate** flakiness by fixing root causes rather than adding retries.
4. **Measure** test-suite strength with mutation testing and property-based tests, and **review** AI-generated tests for false confidence.
5. **Explain** how bundlers work (module graph, transforms, chunking, tree shaking, source maps), and **diagnose** a bloated bundle.
6. **Configure** the toolchain (TypeScript 7 with a TypeScript 6 API for tools, ESLint 10 or Biome or Oxlint, formatting, dead-code detection) and **defend** the supply chain.
7. **Structure** a monorepo with workspaces, task graphs and remote caching, and **version** packages with changesets.
8. **Build** a CI/CD pipeline with preview deployments, performance, accessibility and visual gates, release automation and source-mapped error monitoring.

## Chapters and lessons

### Chapter 1 · Test strategy and economics (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What tests are for | Confidence per minute of runtime and per hour of maintenance; risk-based testing; the pyramid vs the "testing trophy" | Write a test strategy for a checkout flow with a budgeted runtime |
| 1.2 Test doubles | Fakes, stubs, mocks and spies; over-mocking; testing behaviour at boundaries | Rewrite 10 mock-heavy tests as boundary tests |
| 1.3 Flakiness as a cost | Causes (timing, shared state, order, network, animations), quarantine policy, flake budgets | Classify 20 historical flaky failures by root cause |
| 1.4 Coverage honestly | Line vs branch coverage; what 100% coverage does not prove | Find a bug in code with 100% line coverage |

**Check your understanding:** Why can more end-to-end tests make a team slower and less safe? When is a mock the right choice? What does a coverage number tell a manager, and what does it hide?

### Chapter 2 · Unit and component tests (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Vitest 5 | Config and projects (nested projects inherit the root config), `vi.when`, `clearMocks` default, unawaited assertions now fail, `expect.poll` | Port a Jest 30 suite to Vitest 5; list behaviour changes |
| 2.2 Testing Library | Guiding principles; queries by role and accessible name; `user-event` vs `fireEvent` | Rewrite 15 class-name-based tests to role-based queries |
| 2.3 Async UI | `findBy*`, waiting for disappearance, avoiding arbitrary sleeps | Remove every `setTimeout` from a test suite with no new flakes |
| 2.4 Type tests | `expectTypeOf`, testing public library types (link to FE301) | Add type tests to a component library's public API |

**Check your understanding:** Why are role-based queries more robust and also an accessibility check? What does "test behaviour, not implementation" mean for a component with internal state? Why did Vitest 5 make unawaited async assertions fail?

### Chapter 3 · Controlling network, time and randomness (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Network mocking | MSW 3 handlers shared by tests, Storybook and local development; contract drift | One set of handlers used in unit, component and E2E tests |
| 3.2 Time | Fake timers, debounced inputs, `Temporal` mocking in Vitest 5, time zones (IST vs UTC bugs) | Test a "booking closes at 23:59 IST" banner across time zones |
| 3.3 Randomness and IDs | Seeded randomness, deterministic IDs, snapshot stability | Make a flaky snapshot suite deterministic |
| 3.4 Contracts | Validating mocks against OpenAPI schemas (FE301 P3) so mocks cannot drift from the API | Fail CI when a mock returns a field the API removed |

**Check your understanding:** Why are hand-written mocks a source of false confidence? What date bug appears only between 00:00 and 05:30 IST? How do you keep mocks honest as the backend changes?

### Chapter 4 · Testing in real browsers (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 jsdom vs real browsers | What jsdom does not implement (layout, focus, scrolling, CSS); when it is good enough | List 10 bugs jsdom tests cannot catch; reproduce 3 |
| 4.2 Vitest Browser Mode | Playwright provider, strict locators, ARIA errors on failure, trace view (Vitest 5) | Move 20 component tests to Browser Mode; compare runtime |
| 4.3 Storybook 10 tests | Stories as test cases, interaction tests, accessibility per story | Turn 15 stories into interaction tests |
| 4.4 Cross-browser | Chromium, Firefox and WebKit engines in Playwright; real Safari and real Android caveats | Run the suite on three engines; triage engine-specific failures |

**Check your understanding:** When is a real-browser component test worth its extra runtime? Why does WebKit in Playwright not equal Safari on an iPhone? Why should a story and a test share one source?

### Chapter 5 · End-to-end with Playwright (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Locators and auto-waiting | Role locators, `locator.within()` (1.64), web-first assertions; why `waitForTimeout` is a smell | Write 10 E2E tests with zero explicit waits |
| 5.2 Fixtures and isolation | Test isolation, fixtures, authentication state reuse, seeded test data, named test locks (1.63) | Run the suite in parallel with 8 workers and zero cross-test interference |
| 5.3 Network and devices | Route interception, offline, geolocation, device emulation, passkeys via the WebAuthn credentials API (1.61) | Test a passkey login and an offline banner |
| 5.4 Debugging failures | Traces, videos, aria and screen snapshots in traces, retries vs root cause | Diagnose 5 failing CI runs from traces only |
| 5.5 Scaling | Sharding, `--shuffle` (1.64) to expose order dependence, test impact analysis | Cut suite wall time by 60% with shards; find two order-dependent tests |

**Check your understanding:** Why do retries hide bugs as well as flakes? What is the right level of test data setup for E2E (UI, API or database), and why? How does shuffling test order expose hidden coupling?

### Chapter 6 · Visual and accessibility regression (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Screenshot testing | `toHaveScreenshot`, thresholds, anti-aliasing and font rendering differences, baselines per platform | Stabilise a visual suite across Linux CI and macOS laptops |
| 6.2 Hosted review | Chromatic and similar services: review workflows, cost, when to self-host | Compare a hosted run with a self-hosted run for 50 stories |
| 6.3 Accessibility automation | `@axe-core/playwright`, axe in Storybook, ARIA snapshots for structure; their limits | Gate CI on axe and ARIA snapshots; document what remains manual |
| 6.4 What not to snapshot | Brittle full-page snapshots, dynamic content, ads | Replace 10 brittle snapshots with targeted ones |

**Check your understanding:** Why do visual tests fail on CI but pass locally, and how do you fix that properly? What does an ARIA snapshot catch that axe does not? When is a full-page screenshot test worth keeping?

### Chapter 7 · Testing AI-written code (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Mutation testing | StrykerJS: mutants, mutation score, equivalent mutants; what it reveals about weak assertions | Raise a module's mutation score from 45% to 80% |
| 7.2 Property-based testing | fast-check: generators, shrinking, invariants for formatters, parsers and reducers | Find a bug in a date-range picker with a property test |
| 7.3 Test agents | Playwright's planner, generator and healer agents; Playwright MCP; reviewing what they produce | Generate 10 E2E tests with agents; measure how many catch planted bugs |
| 7.4 Reviewing generated tests | Smells: assertion-free tests, tests mirroring the implementation, over-mocking, snapshot-only tests, "healed" tests that hide regressions | Review 20 AI-written tests; keep, fix or delete each with a reason |

**Check your understanding:** Why can a test-repair agent turn a real regression into a green build? What does a mutation score measure that coverage does not? Which code deserves property tests first?

### Chapter 8 · Build tools and bundlers (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 How bundlers work | Module graph, resolution, transforms (Oxc, SWC, Babel), chunking, scope hoisting, tree shaking, `sideEffects` | Build a 200-line toy bundler that resolves, transforms and concatenates ES modules (no AI) |
| 8.2 Vite 8 and Rolldown | Dev server with native ESM, HMR, production builds with Rolldown, plugin compatibility | Upgrade a Vite 6 app to Vite 8; record build times and differences |
| 8.3 Other bundlers | Turbopack (Next.js default), Rspack, esbuild; when the framework decides for you | Build the same app with two bundlers; compare output and timings |
| 8.4 Diagnosing bundles | Bundle analysers, duplicate dependencies, barrel-file costs, polyfills, source maps | Cut a bundle by 35% and explain every saved kilobyte |
| 8.5 Builds you can trust | Deterministic builds, lockfiles, environment variables in client bundles, secrets that leak | Find a planted secret in a production bundle; add a CI check that blocks it |

**Check your understanding:** Why do barrel files (`index.ts` re-exports) slow down builds and bloat bundles? What does `sideEffects: false` promise, and what breaks if it lies? Why does a dev server not need to bundle, while production does?

### Chapter 9 · Code-quality toolchain and supply chain (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Type checking at speed | TypeScript 7 `tsc` in CI, project references, `@typescript/typescript6` for tools needing the API | Halve CI type-check time; keep typescript-eslint working |
| 9.2 Linters and formatters | ESLint 10 flat config with typescript-eslint, Biome 2, Oxlint; Prettier vs oxfmt; picking one and enforcing it | Compare lint time and rule coverage of ESLint and Oxlint on one repository |
| 9.3 Dead code and dependencies | knip for unused files, exports and dependencies; dependency update automation | Remove all unused dependencies found by knip; prove the build still works |
| 9.4 Supply-chain defence | Lockfiles, pinned versions, npm provenance, phishing-resistant MFA, a minimum release age before installing new versions (pnpm's `minimumReleaseAge`), install scripts; lessons from Shai-Hulud | Write and apply a dependency policy; show it would have delayed a just-published malicious version |

**Check your understanding:** Why does a minimum release age reduce supply-chain risk, and what does it cost? Why might a team run Oxlint and ESLint together? What did CISA recommend after Shai-Hulud, and which of those steps can CI enforce?

### Chapter 10 · Monorepos (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Workspaces | pnpm workspaces, internal packages, `workspace:` protocol, TypeScript project references | Split an app into 2 apps and 3 packages |
| 10.2 Task graphs and caching | Turborepo 2 and Nx: task dependencies, affected builds, local and remote caches, cache keys | Make a cached CI re-run finish in under 1 minute |
| 10.3 Versioning and publishing | changesets, independent vs fixed versioning, changelogs, provenance | Release two packages with generated changelogs |
| 10.4 Boundaries and ownership | Module boundary rules, CODEOWNERS, dependency constraints | Block an app from importing another app's internals |

**Check your understanding:** What makes a remote cache unsafe (wrong cache keys, environment leaks)? When is a monorepo the wrong choice? Why do internal packages need versioning discipline even when they are never published?

### Chapter 11 · CI/CD for frontends (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Pipelines | GitHub Actions stages, caching, parallel jobs, required checks, merge queues | Build a pipeline under 8 minutes for a 5-package monorepo |
| 11.2 Preview deployments | One URL per pull request, seeded data, E2E against previews | Run Playwright against each PR's preview |
| 11.3 Quality gates | Lighthouse CI and `size-limit` budgets, axe, visual tests, type and lint checks | Block a PR that fails any gate; document the override process |
| 11.4 Release and observe | Semantic releases, feature flags, canary rollout, Sentry with uploaded source maps, release health | Ship, detect and roll back a planted bad release |
| 11.5 Agents in the loop | `AGENTS.md`-style repository instructions, Chrome DevTools MCP and Playwright MCP so agents can check their own UI changes, and CI as the final judge | Let an agent fix 3 issues; record which ones CI rejected and why |

**Check your understanding:** Why should every check that matters be automated and required? What makes a canary release meaningful for a frontend? Why is CI, not the agent's own report, the arbiter of an agent's change?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Test strategy | Strategy document with runtime budget |
| 2 | 2 | Lab 2 · Vitest and Testing Library | Ported, role-based suite |
| 3 | 3 | Lab 3 · Network and time | Shared MSW handlers; time-zone tests; **P1 starts** |
| 4 | 4 | Lab 4 · Real browsers | Browser Mode migration report |
| 5 | 5 | Lab 5 · Playwright E2E | Zero-wait suite; **P1 due** |
| 6 | 5 | Lab 5 (cont.) | Sharded, shuffled, traced |
| 7 | 6 | Lab 6 · Visual and accessibility | Stable visual suite; mid-term (AI off) |
| 8 | 7 | Lab 7 · Mutation and agents | Mutation score report; agent test review |
| 9 | 8 | Lab 8 · Toy bundler (no AI) | Working bundler; **P2 due** |
| 10 | 8 | Lab 8 (cont.) · Vite 8 upgrade | Bundle-diet report |
| 11 | 9 | Lab 9 · Toolchain and supply chain | Dependency policy applied |
| 12 | 10 | Lab 10 · Monorepo | Cached CI; **P3 starts** |
| 13 | 11 | Pipeline and previews | Gated pipeline |
| 14 | 11 | Release and rollback | **P3 due** |
| 15 | Review | P3 defence | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating test cases from a written behaviour list; drafting Playwright tests with the planner and generator agents; writing CI YAML; migrating test syntax (Jest to Vitest); explaining a failing trace.
- **Do without AI (drills):** the test strategy; the toy bundler; the root-cause diagnosis of flaky tests from traces; the mid-term (design tests for a spec on paper) and final.
- **Verify AI output by:** mutation testing (a generated test that kills no mutants is decoration); running each new test against a deliberately broken build (it must fail); reading diffs from healer agents line by line; checking every config option against the tool's current documentation, because Vite 8, Vitest 5, ESLint 10 and TypeScript 7 changed many options in 2026.
- **Where AI still fails here (collect your own evidence):** log generated tests that assert on implementation details, mock the unit under test, use fixed sleeps, update snapshots to match a bug, or pass without any assertion. Log every "healed" locator that hid a real regression, and every outdated config key suggested from older versions. The log is part of P3.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 20% |
| Mid-term (AI off) | 10% |
| Final (AI off, 3 h) and P3 defence | 20% |

**Mastery gate.** You pass when you can, with AI off, in 3 hours, take an untested feature with a planted set of 10 bugs and:
1. write a test suite that catches at least 8 of the bugs, across unit, component and E2E levels;
2. reach a mutation score of at least 70% on the core module;
3. explain from a CI trace why one provided E2E test is flaky, and fix the cause.

## Industry reality

Frontend engineers own their own tests and pipelines in most product companies; dedicated quality engineers increasingly build the platform rather than write every test (see the [QAE market page](../../../../06_career_and_market_readiness/01_market_map/roles/QAE_software_quality_test_engineering.md)). Vite 8's announcement lists production-build reductions reported by Linear, Ramp, Mercedes-Benz.io and Beehiiv. The Next.js team described using an agent to research a backlog while maintainers reviewed its findings, closing 1,462 issues in a month (September 2026). That is a picture of agents doing the bulk work and humans owning the judgement. Supply-chain hygiene became a hiring topic after Shai-Hulud.

**Interview questions from this course**

1. *How do you decide what to cover with unit, integration and end-to-end tests for a checkout?* A strong answer is risk-based: unit tests for pricing and validation, component and integration tests for form behaviour with mocked network, and a few E2E tests for money paths on previews. It sets a runtime budget and explains what is deliberately not tested.
2. *Our E2E suite fails 5% of the time. What do you do?* A strong answer measures the flake rate per test and quarantines with an owner. It finds root causes in traces (timing, shared data, animations, order dependence) and fixes them with web-first assertions, isolation and seeded data. It treats retries as a temporary measure only.
3. *Why is our bundle 2 MB, and how would you fix it?* A strong answer uses an analyser to find duplicates, large dependencies, barrel imports and polyfills. It applies route-level splitting and tree-shaking fixes (`sideEffects`), sets a budget in CI and verifies the result in production.
4. *How would you protect our frontend from a compromised npm package?* A strong answer covers lockfiles and pinned versions, a minimum release age, provenance, disabling install scripts where possible, phishing-resistant MFA, least-privilege CI tokens, and dependency review. It cites Shai-Hulud as the threat model.
5. *An AI wrote 40 tests for this module, and coverage is 95%. Are we safe?* A strong answer says not necessarily. It runs mutation testing, checks the assertions, breaks the code deliberately, and looks for over-mocking and snapshot-only tests.

## Resources (free first)

- **Testing:** [Vitest guide](https://vitest.dev/guide/browser/) and [visual regression testing](https://vitest.dev/guide/browser/visual-regression-testing); [Testing Library guiding principles](https://testing-library.com/docs/guiding-principles/); Kent C. Dodds, [The testing trophy](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications); [Playwright docs](https://playwright.dev/docs/release-notes), [test agents](https://playwright.dev/docs/test-agents) and [ARIA snapshots](https://playwright.dev/docs/aria-snapshots); [Storybook docs](https://storybook.js.org/docs); [StrykerJS](https://stryker-mutator.io/docs/stryker-js/introduction/); [fast-check](https://fast-check.dev/); [@axe-core/playwright](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/playwright).
- **Build and tooling:** [Vite 8 announcement](https://vite.dev/blog/announcing-vite8); [Rolldown](https://rolldown.rs/); [Oxc linter](https://oxc.rs/docs/guide/usage/linter); [Biome](https://biomejs.dev/); [ESLint](https://eslint.org/docs/latest/); [knip](https://knip.dev/); [size-limit](https://github.com/ai/size-limit).
- **Monorepos and release:** [Turborepo](https://turborepo.com/docs); [Nx](https://nx.dev/getting-started/intro); [changesets](https://github.com/changesets/changesets); [pnpm settings](https://pnpm.io/settings).
- **CI, release, agents:** [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci); [Sentry JavaScript](https://docs.sentry.io/platforms/javascript/); [AGENTS.md](https://agents.md/); [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp).
- **Security:** [CISA alert on the npm supply-chain compromise](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem).

## Sources

All checked 12 Oct 2026.

- Vite, "Announcing Vite 8" (12 Mar 2026; Rolldown; reported build reductions) — https://vite.dev/blog/announcing-vite8
- Vitest, "Announcing Vitest 5.0" (3 Sep 2026) — https://vitest.dev/blog/vitest-5
- Playwright release notes (1.61–1.64; test agents since 1.56) — https://playwright.dev/docs/release-notes
- Microsoft, Announcing TypeScript 7.0 (8 Jul 2026) — https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/
- Next.js 16 (21 Oct 2025, Turbopack default) — https://nextjs.org/blog/next-16 · Next.js blog (Sep 2026 post on closing 1,462 issues with an agent) — https://nextjs.org/blog
- CISA, "Widespread Supply Chain Compromise Impacting npm Ecosystem" (23 Sep 2025) — https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem
- Google Cloud / DORA 2025 report announcement — https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- npm registry versions on 12 Oct 2026: vite 8.3.4, vitest 5.0.3, @playwright/test 1.64.0, jest 30.5.2, eslint 10.12.0, @biomejs/biome 2.5.15, oxlint 1.87.0, storybook 10.6.1, msw 3.0.3, turbo 2.11.7, nx 23.3.0 — https://registry.npmjs.org/

_Last reviewed: 2026-10_
