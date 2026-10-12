# FE305 · Labs and projects

Every lab has two checks: the tests must pass on a correct build, and they must fail on a provided broken build. A test that cannot fail does not count. Mutation scores come from StrykerJS. The toy bundler and the flaky-test diagnosis are done without AI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Test strategy | Risk-based strategy for a checkout flow with a 6-minute CI runtime budget | Strategy document: risks, levels, what is not tested and why | 3 h |
| 2 · Vitest and Testing Library | Port a Jest 30 suite to Vitest 5; convert to role-based queries | Ported suite; list of behaviour changes; zero class-name queries | 4 h |
| 3 · Network and time | Shared MSW 3 handlers validated against an OpenAPI schema; IST/UTC boundary tests | Handlers reused in 3 test levels; a time-zone bug found and fixed | 4 h |
| 4 · Real browsers | Move 20 tests to Vitest Browser Mode; run Playwright on Chromium, Firefox and WebKit | Runtime comparison; 3 jsdom-invisible bugs reproduced | 4 h |
| 5 · Playwright E2E | 20 tests with zero explicit waits, 8 parallel workers, sharding, `--shuffle` | Green suite over 50 shuffled runs; traces for 5 diagnosed failures | 7 h |
| 6 · Visual and accessibility | Stable screenshots across Linux CI and a laptop; axe and ARIA snapshots as gates | Visual suite with under 1% false positives over 20 runs; gate demonstration | 4 h |
| 7 · Mutation and agents | Raise a module's mutation score from 45% to at least 80%; generate 10 tests with Playwright agents and grade them | Mutation reports; agent-test review table (kept, fixed or deleted, with reasons) | 5 h |
| 8 · Toy bundler (no AI) | Resolve, transform (TypeScript via a library), tree-shake exports and concatenate ES modules | Bundler passing 25 provided fixtures; a one-page design note | 8 h |
| 9 · Toolchain and supply chain | TypeScript 7 type-check plus typescript-eslint on TypeScript 6; knip clean-up; dependency policy | CI time before/after; policy applied (pinned, minimum release age, provenance check, install scripts reviewed) | 4 h |
| 10 · Monorepo | 2 apps and 3 packages with pnpm workspaces, Turborepo or Nx, remote cache, changesets | Cold CI under 8 minutes; cached re-run under 1 minute; a release with changelogs | 5 h |

## Projects

### P1 · Prove a checkout form works (L1, ~6 hours)

**Real-world inspiration:** checkout forms are where small bugs cost money: GST-inclusive totals, PIN-code validation, coupon rules, UPI ID formats and time-limited offers. The form is provided and is an **illustrative scenario** with 12 planted bugs that you are not told about.

**What to build:** a test suite for the provided form (React or Vue), including:
- unit tests for the pricing and validation logic;
- component tests with Testing Library and MSW;
- property-based tests for the price calculator and validators;
- three Playwright E2E tests for the happy path, a declined payment and an expired offer;
- an axe check on every step.

**Acceptance criteria:**
- Your suite catches at least 10 of the 12 planted bugs. Each caught bug has a failing test, a fix and a passing test.
- Mutation score of at least 75% on the pricing module.
- Zero arbitrary waits; the whole suite runs in under 90 s locally.
- The suite passes 30 consecutive runs in random order with no flakes.
- A one-page note lists what the suite does not cover and why that risk is acceptable.

**Stretch goals:** run the same component tests in Vitest Browser Mode and in jsdom, and report which bugs only one of them caught.

**What it proves to an employer:** you write tests that find bugs, not tests that only produce coverage.

### P2 · A fast, trustworthy toolchain from scratch (L2, ~15 hours)

**Real-world inspiration:** Vite 8's announcement reports large build-time reductions at Linear and Ramp after the move to Rolldown. Teams that adopt such tools well also re-examine linting, type checking, caching and dependency policy at the same time.

**What to build:** a monorepo template containing:
- a Vite 8 React app, an Astro or Next.js site, and three shared packages (UI, utilities, API client);
- TypeScript 7 project references, plus typescript-eslint running on the TypeScript 6 API;
- Oxlint and ESLint split by rule type, and a formatter;
- Vitest 5 projects, Playwright E2E and Storybook 10 with interaction tests;
- Turborepo or Nx with a remote cache, changesets, knip, `size-limit`;
- a written dependency policy.

**Acceptance criteria:**
- **Speed:** a cold CI run takes at most 8 minutes. A no-change re-run takes at most 60 s from the cache. Changing one package rebuilds and retests only its dependents (task-graph evidence).
- **Correctness of caching:** a planted environment variable change invalidates the right tasks; a test proves the cache is never reused across different inputs.
- **Gates:** type, lint, unit, E2E, Storybook interaction and bundle-size checks are required. Planted failures of each kind block merge.
- **Supply chain:** lockfile enforced; a minimum release age configured; install scripts allow-listed; provenance verified for published packages; a write-up maps your controls to CISA's Shai-Hulud recommendations.
- **Documentation:** a new contributor clones the repository and gets all checks green locally in under 15 minutes (observed with one tester).

**Stretch goals:** compare Turbopack and Rolldown builds for the same app; add an `AGENTS.md` and measure how often an agent's changes pass CI on the first try.

**What it proves to an employer:** you can own a team's developer experience and build safety, which frontend platform teams hire for.

### P3 · Frontend quality platform with release safety (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** product teams ship many times a day only because preview deployments, automated gates and fast rollback make each release low-risk. The Next.js team's account of agent-assisted issue triage (September 2026) shows the new shape of the work: agents produce many changes, and pipelines and humans decide what merges.

**What to build:** on top of P2, or on an open-source frontend you contribute to, build:
- preview deployments per pull request, with E2E tests against the preview;
- visual regression for all stories, and accessibility gates (axe plus ARIA snapshots on key pages);
- Lighthouse CI and `size-limit` budgets per route;
- flaky-test detection with automatic quarantine and an owner;
- feature-flagged canary releases with error monitoring and uploaded source maps, plus a one-command rollback;
- an experiment with AI test agents and coding agents on 10 real issues, with results measured.

**Acceptance criteria:**
- **Gate effectiveness:** a red-team set of 12 planted regressions (visual, accessibility, performance, functional, bundle size, type) is each blocked before merge, or caught by the canary within 10 minutes and rolled back automatically.
- **Pipeline speed:** median PR pipeline at most 10 minutes over 20 PRs.
- **Flakiness:** the flake rate over 200 pipeline runs is reported per test, and quarantined tests have owners and expiry dates.
- **Observability:** a production error from the canary maps to the original TypeScript line through source maps, with release and commit tags.
- **Agent experiment:** for 10 issues, report the share of agent-produced PRs that passed all gates, the share that passed gates but were wrong on human review, and the gate you added because of one.
- **Upstream contribution (strongly encouraged):** one merged pull request to an open-source testing or build tool (for example Vitest, Playwright, Testing Library, Storybook or Rolldown), or a documented attempt with maintainer feedback.

**Stretch goals:** test-impact analysis that runs only affected E2E tests; a cost report of CI minutes per month with and without caching.

**What it proves to an employer:** you can make fast shipping safe, and you can measure how far agents can be trusted in a real pipeline. Few candidates have that judgement, and it is hard to replace.

## Feeds into

- [FE401 Full-Stack Frameworks](../../year_4/FE401_full_stack_frameworks_rendering_data_fetching/README.md): testing server rendering, caching and authentication.
- [FE404 Frontend System Design at Scale](../../year_4/FE404_frontend_system_design_at_scale/README.md): monorepos, micro-frontends and release governance across many teams.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): the P3 pipeline becomes the default for co-op projects.
- [OPS301 CI/CD Engineering](../../../devops_sre_platform_engineering/year_3/OPS301_ci_cd_engineering/README.md), as an elective for deeper pipeline work.
