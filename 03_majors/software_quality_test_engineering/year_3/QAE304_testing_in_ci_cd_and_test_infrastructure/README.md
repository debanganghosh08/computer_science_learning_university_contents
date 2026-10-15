# QAE304 · Testing in CI/CD and Test Infrastructure

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md); uses [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) and [QAE302](../QAE302_test_automation_engineering_ui_and_api/README.md) | [QAE404](../../year_4/QAE404_quality_engineering_leadership_and_metrics/README.md); feeds overlap [OV03 DevSecOps](../../../../04_overlaps/OV03_devsecops/README.md) |

Part of the [Software Quality and Test Engineering major](../../README.md). CS205 set up a first CI pipeline with quality gates. This course treats the test pipeline as a product with users (developers), a latency budget (feedback time), a reliability target (flaky rate) and a cost: the work of test-infrastructure and developer-productivity teams.

## Why this course matters now

AI coding tools raised the volume of changes; DORA's 2025 research found AI adoption positively related to throughput but negatively related to delivery stability. DORA now tracks five delivery metrics (change lead time, deployment frequency, failed deployment recovery time, change fail rate and deployment rework rate), and the test pipeline drives most of them. Running every test on every change stops scaling: Meta's predictive test selection reported catching over 99.9% of faulty changes while roughly halving testing infrastructure cost. Flakiness destroys trust: Google found 84% of observed pass-to-fail transitions in CI involved a flaky test. Tools exist for every piece (sharding in Playwright, pytest-xdist, Bazel caching, merge queues, Allure Report, ephemeral Kubernetes environments, LLM failure triage), but someone must design the system that combines them, measure it and keep it honest. That is the test infrastructure engineer.

## Learning outcomes

By the end you can:

1. **Design** a layered test portfolio (pyramid, trophy or Google test sizes) for a given architecture and **justify** what runs per commit, per merge, nightly and per release.
2. **Build** CI pipelines with matrices, caching, artefacts, pinned dependencies and least-privilege secrets on GitHub Actions or GitLab CI.
3. **Cut** feedback time with parallel workers and balanced sharding, and **measure** the result as p50/p95 pipeline duration.
4. **Provision** ephemeral, seeded environments per pull request and **tear them down** reliably.
5. **Implement** test impact analysis and **measure** its selection rate and missed-failure rate on real history.
6. **Run** a flaky-test programme: detection, scoring, quarantine with owners and deadlines, and fixes.
7. **Produce** test reports and analytics (JUnit XML, Allure, traces) that developers open and act on.
8. **Design** quality gates (tests, diff coverage, diff mutation, lint, types, SAST, dependencies, performance, accessibility, contracts) with known false-positive rates and audited overrides.
9. **Evaluate** AI pipeline tools (failure triage, flaky classification, auto-fix agents) by precision and recall, and **guard** against agents editing tests to pass.

## Chapters and lessons

### Chapter 1 · Test infrastructure as a product (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Feedback economics | Cost of delay per minute of CI, context switching, batch size; DORA's five metrics | Compute the yearly engineer-hours lost to a 30-minute pipeline for a 50-person team (illustrative) |
| 1.2 Portfolio shapes | Cohn's pyramid, Fowler's practical pyramid, Dodds's testing trophy, Google's small/medium/large test sizes | Classify an open-source project's tests by size; time each class |
| 1.3 Hermeticity | Tests that depend only on declared inputs; network, clock and data isolation | Make 5 non-hermetic tests hermetic |
| 1.4 Users and SLOs of a pipeline | Developer feedback SLOs (p95 PR feedback time), flaky-rate SLO, availability of CI | Write SLOs for your course pipeline |

**Check your understanding:** Why is a 40-minute pipeline a design problem, not only a hardware problem? When is the testing trophy a better shape than the pyramid? Why does hermeticity matter more as parallelism grows?

### Chapter 2 · CI fundamentals for test engineers (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Pipelines | GitHub Actions workflows, jobs, needs, matrices; GitLab CI stages; Jenkins pipelines for legacy estates | Same pipeline in GitHub Actions and GitLab CI |
| 2.2 Reproducibility | Containers for test runners, lockfiles, pinned actions by commit SHA, browser versions | Reproduce a CI failure locally with the same container image |
| 2.3 Caching and artefacts | Dependency caches, build caches, artefact retention, cache poisoning risks | Cut install time by ≥ 50% with caching; show the cache-key design |
| 2.4 Secrets and permissions | Least-privilege tokens, OIDC to cloud, secrets in forked pull requests; GitHub Actions hardening guide | Audit a workflow; remove 3 excess permissions |

**Check your understanding:** Why pin actions by SHA rather than tag? What makes a cache key correct? Why are pull requests from forks dangerous for secrets?

### Chapter 3 · Speed: parallelism and sharding (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Worker parallelism | pytest-xdist, Playwright workers, JUnit parallel execution; isolation prerequisites | Run a suite at 1, 2, 4 and 8 workers; plot speed-up |
| 3.2 Sharding | Playwright `--shard` and blob reports merged with `merge-reports`; matrix shards | Shard a suite 4 ways and merge one HTML report |
| 3.3 Balancing | Duration-based splitting from history; the slowest shard sets the pace; Amdahl's law for suites | Balance shards to within 15% of each other |
| 3.4 Fail fast | Ordering by failure likelihood, `maxfail`, early smoke stages | Reorder stages; measure time to first failure on 20 broken commits |

**Check your understanding:** Why does doubling shards rarely halve wall-clock time? What breaks when tests share a database under parallelism? Why measure time to first failure separately from total time?

### Chapter 4 · Test environments (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Environment strategy | Local, ephemeral per-PR, shared staging, production; drift and its symptoms | Map where each test layer should run |
| 4.2 Ephemeral environments | Docker Compose or kind + Helm per pull request; seeded databases; preview URLs | Spin up a full app per PR in under 5 minutes |
| 4.3 Data and dependencies | Seed scripts, snapshots, Testcontainers, service virtualisation for third parties | Seed realistic synthetic data; virtualise a payment gateway |
| 4.4 Migrations | Testing database migrations (expand and contract / parallel change), rollback scripts, data backfills | Test a column rename with zero downtime across two releases |
| 4.5 Cost and teardown | Time-to-live, garbage collection, cost per environment-hour | Prove 100% teardown over 50 PRs |

**Check your understanding:** Why do shared staging environments produce flaky end-to-end tests? What makes a migration test convincing? How do you stop forgotten preview environments from running up a bill?

### Chapter 5 · Test selection and impact analysis (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Static selection | Build-graph selection (Bazel test targets), module ownership maps, Playwright `--only-changed` | Select tests from the dependency graph for 50 historical commits |
| 5.2 Coverage-based selection | Per-test coverage maps; staleness; changes outside code (config, data, infrastructure) | Build a coverage map; measure misses on history |
| 5.3 Predictive selection | Meta's learned model (over 95% of individual failures and over 99.9% of faulty changes reported, about half the cost) | Train a simple classifier on file-test failure history |
| 5.4 Safety nets | Full runs nightly and before release; measuring escaped failures; when not to select | Design the safety net and its alerting |

**Check your understanding:** Why does coverage-based selection miss failures caused by configuration changes? What is the cost of one missed failure compared with one extra test run? Why still run everything nightly?

### Chapter 6 · Flaky-test management at scale (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Detection | Rerun-on-failure signals, history-based flakiness scores, scheduled repeat runs | Compute flakiness scores from 30 days of CI history |
| 6.2 Quarantine policy | Owners, deadlines, ticket automation, maximum quarantine size, exit criteria | Write and automate a quarantine policy |
| 6.3 Root causes at scale | Clustering failures by error signature; infrastructure vs test vs product causes | Cluster 200 failures into causes |
| 6.4 Culture | Retries that hide bugs, "just rerun it" habits, flakiness budgets per team | Present a flakiness report to a mock engineering team |

**Check your understanding:** Why is an automatic silent retry dangerous? What should happen to a quarantined test after its deadline? How do you tell a flaky test from a flaky product?

### Chapter 7 · Reporting and test analytics (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Formats | JUnit XML as the common currency; Playwright HTML and blob reports; traces as artefacts | Normalise three tools' outputs into JUnit XML |
| 7.2 Allure Report | Steps, attachments, categories, history and trends; Allure 2 vs the Allure 3 rewrite | Publish an Allure report with history from CI |
| 7.3 Analytics | Slowest tests, most flaky, failure rate by owner, duration trends | Build a dashboard from 30 days of results |
| 7.4 Reports people read | Failure summaries in pull requests with the trace link and owner | Ship a PR comment bot that links the failing trace |

**Check your understanding:** What does a developer need in the first 10 seconds after a red build? Which test metric would you show a director, and which would you hide? Why keep history in reports?

### Chapter 8 · Quality gates (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 What to gate | Tests, diff coverage, mutation on changed lines, lint and types, SAST, dependency checks, performance budgets, accessibility smoke, contract `can-i-deploy` | Draft the gate list for a payments service |
| 8.2 Gate design | False-positive rate, time cost, override rules with audit trail | Measure the false-positive rate of 3 gates over 50 PRs |
| 8.3 Branch protection and merge queues | Required checks, merge queues that test the merged result, batch merging | Show a semantic conflict that passes per-branch CI and fails in the merge queue |
| 8.4 Diff-based mutation | Mutation testing on changed lines only, as in Google's code-review integration | Add diff mutation to PRs with a time budget |

**Check your understanding:** Why should a gate's false-positive rate be measured before it becomes required? What does a merge queue guarantee that "green on my branch" does not? Why run mutation only on changed lines?

### Chapter 9 · Release safety (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Deployment pipelines | Build once, promote the same artefact; environment-specific configuration | Promote one image through 3 environments |
| 9.2 Post-deploy checks | Smoke tests, synthetic transactions, automatic rollback triggers | Roll back automatically on a failed smoke test |
| 9.3 Flags and progressive delivery | Feature flags (OpenFeature), canaries and their test implications (deeper in QAE404) | Test both sides of a flag in CI |
| 9.4 Configuration as code under test | Validating configuration and data pushes before rollout (lesson of the 2024 CrowdStrike incident) | Add schema and staged-rollout checks to a config pipeline |

**Check your understanding:** Why build an artefact once? How many flag combinations must you test, and how do you choose? Why does configuration need the same tests as code?

### Chapter 10 · Scale and cost (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Caching at scale | Remote build and test caching (Bazel), cache-hit rates, correctness risks | Measure cache-hit rate and time saved on 20 commits |
| 10.2 Runner fleets | Self-hosted and autoscaled runners, ephemeral runners, isolation | Run tests on an autoscaled runner pool in kind |
| 10.3 Cost accounting | Cost per pipeline, per PR, per team; idle environments | Build a monthly cost report for the course pipeline |
| 10.4 Pipeline observability | Tracing pipelines (OpenTelemetry CI/CD semantic conventions), p95 durations, queue time | Trace a pipeline run; find the slowest step |

**Check your understanding:** When can a test cache return a wrong "pass"? Why does queue time matter as much as run time? Which cost would you cut first?

### Chapter 11 · AI in the pipeline (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Failure triage | LLM summaries of logs and traces; clustering; owner routing | Evaluate an LLM triage prompt on 50 labelled failures (precision, recall) |
| 11.2 Flaky classification | Classifying failures as flaky, product bug or infrastructure; cost of each error type | Compare an LLM classifier with a history-based score |
| 11.3 Auto-fix agents | Agents that propose fixes for red builds; protected test paths; budgets; human approval | Run an agent on 5 planted failures with tests write-protected; log every attempt to edit tests |
| 11.4 AI-selected tests | Learned selection vs graph selection; auditing misses | Compare an LLM's "which tests to run" with your Chapter 5 selector |

**Check your understanding:** Which AI triage error is worse for your team, false "flaky" or false "product bug"? Why must test files be protected from fix agents? What evidence would make you trust learned test selection?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Test sizes and hermeticity | — |
| 2 | 2 | Lab 2 · Reproducible, hardened pipeline | — |
| 3 | 3 | Lab 3 · Workers, shards and balance | — |
| 4 | 4 | Lab 4 · Ephemeral environment per PR | **P1 due** |
| 5 | 4 | Lab 5 · Migrations and teardown | — |
| 6 | 5 | Lab 6 · Test impact analysis on history | — |
| 7 | 6 | Lab 7 · Flaky scoring and quarantine | Mid-term (AI off) |
| 8 | 7 | Lab 8 · Allure and PR failure bot | — |
| 9 | 8 | Lab 9 · Gates and merge queue | **P2 due** |
| 10 | 9 | Release safety drills | — |
| 11 | 10 | Lab 10 · Cache and cost | — |
| 12 | 11 | AI triage evaluation | Evaluation report |
| 13 | 11 | Fix-agent experiment | — |
| 14 | — | P3 | **P3 due** |
| 15 | Review | P3 demo | Final exam (AI off): pipeline design and diagnosis |

## Working with AI in this course

- **Use AI for:** drafting workflow YAML and Helm values; writing scripts that parse JUnit XML; summarising long CI logs; clustering failures; first drafts of dashboards. Tools: GitHub Copilot (including its code review and agents), Claude Code, Codex, Cursor, GitLab Duo, plus LLM APIs for triage experiments.
- **Do without AI (drills):** the portfolio design (what runs where), the quarantine policy, gate selection, reading a failing pipeline from raw logs, the mid-term and the final.
- **Verify AI output by:** running generated workflows on a fork with a deliberately failing step; checking permissions and secrets in every generated workflow; measuring triage and classification tools against a labelled set; diffing any agent change for edits under `tests/`; never letting an AI tool mark a test as flaky without history.
- **Where AI still fails here (show it):** your logs must record generated workflows with excessive permissions or unpinned actions, plausible but wrong log summaries, product bugs classified as flaky, and fix agents that weakened or skipped tests. The Lab 11 experiments are graded on their measurement quality.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| P1, P2, P3 | 10%, 20%, 25% |
| Mid-term (AI off) | 5% |
| Final exam (AI off) + P3 demo | 20% |

**Mastery gate.** You pass when you can: (1) take an existing repository with a 40-minute serial test run and, in two days, bring p95 pull-request feedback under 12 minutes with sharding, caching and selection, with a measured missed-failure rate of zero on 100 replayed historical commits that had failures; (2) run a flaky-test programme that reduces a provided suite's flaky rate by at least 80% with every quarantined test owned and dated; (3) with AI off, diagnose 3 broken pipelines (cache, permissions, environment drift) within 45 minutes.

## Industry reality

Test infrastructure and developer-productivity teams exist at most large product companies, and SDETs are increasingly expected to own pipelines rather than only tests (see the [market page](../../../../06_career_and_market_readiness/01_market_map/roles/QAE_software_quality_test_engineering.md)). Public practice: Google's test sizes and hermetic testing (*Software Engineering at Google*); Google's flaky-test data (2016); Meta's predictive test selection (2018–2019); DORA's metrics guide (updated January 2026); GitHub's merge queue; Bazel's remote caching.

**Interview questions from this course**

1. *Our PR pipeline takes 45 minutes. Fix it.* Strong answer: measure first (critical path, queue time, slowest tests, cache hits); parallelise and balance shards; move checks to cheaper layers; test selection with a nightly safety net; ephemeral environments; set a feedback SLO and track p95.
2. *How do you handle flaky tests across 40 teams?* Strong answer: detection from history and scheduled reruns; flakiness scores; quarantine with owners and deadlines; no silent retries; clustering causes; team budgets and visible metrics; fixing infrastructure causes centrally.
3. *What quality gates would you require for a payments service?* Strong answer: unit and contract tests, diff coverage or diff mutation, types and lint, SAST and dependency checks, migration tests, performance budget on key paths, can-i-deploy; measured false positives; audited overrides; merge queue.
4. *Explain test impact analysis and its risks.* Strong answer: graph-, coverage- or ML-based selection; misses from configuration, data and non-code changes; stale maps; safety nets; measuring escaped failures; the cost trade-off.
5. *An AI agent now fixes failing builds automatically. What controls do you add?* Strong answer: protected test paths and hooks, human approval, budget limits, evidence in the PR, metrics on accepted vs reverted fixes, never auto-merge, audit logs.

## Resources (free first)

- **Books and guides:** *Software Engineering at Google*, chapters 11 (Testing Overview), 14 (Larger Testing) and 23 (Continuous Integration) — https://abseil.io/resources/swe-book/html/ch11.html , https://abseil.io/resources/swe-book/html/ch14.html , https://abseil.io/resources/swe-book/html/ch23.html ; Martin Fowler, "Continuous Integration" — https://martinfowler.com/articles/continuousIntegration.html ; "The Practical Test Pyramid" — https://martinfowler.com/articles/practical-test-pyramid.html ; Kent C. Dodds, testing trophy — https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications ; Google Testing Blog, "Test Sizes" (2010) — https://testing.googleblog.com/2010/12/test-sizes.html ; DORA metrics guide — https://dora.dev/guides/dora-metrics/
- **Tools:** GitHub Actions matrices — https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs ; security hardening — https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions ; merge queue — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue ; GitLab CI — https://docs.gitlab.com/ci/ ; Playwright sharding — https://playwright.dev/docs/test-sharding ; pytest-xdist — https://pytest-xdist.readthedocs.io/ ; Bazel test encyclopedia — https://bazel.build/reference/test-encyclopedia and remote caching — https://bazel.build/remote/caching ; Allure Report — https://allurereport.org/docs/ ; kind — https://kind.sigs.k8s.io/ ; Helm — https://helm.sh/docs/ ; OpenTelemetry CI/CD semantic conventions — https://opentelemetry.io/docs/specs/semconv/cicd/
- **Papers and posts:** Machalica et al., "Predictive Test Selection" (arXiv 1810.05286) — https://arxiv.org/abs/1810.05286 and Meta's post — https://engineering.fb.com/2018/11/21/developer-tools/predictive-test-selection/ ; Google flaky tests (2016) — https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html ; Petrović et al., "Practical Mutation Testing at Scale" — https://arxiv.org/abs/2102.11378
- **Paid, optional:** Humble and Farley, *Continuous Delivery*.

## Sources

All checked 12 Oct 2026.

- DORA, "DORA's software delivery performance metrics" (five metrics; updated 5 Jan 2026) — https://dora.dev/guides/dora-metrics/
- Google Cloud, "Announcing the 2025 DORA report" (24 Sep 2025) — https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- Machalica, Samylkin, Porth, Chandra, "Predictive Test Selection" (arXiv 1810.05286; camera-ready May 2019) — https://arxiv.org/abs/1810.05286
- John Micco, "Flaky Tests at Google and How We Mitigate Them" (27 May 2016) — https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html
- Playwright release notes (`--only-changed` since 1.46) — https://playwright.dev/docs/release-notes
- Versions on 12 Oct 2026: pytest-xdist 3.8.0, allure-pytest 2.16.2 (PyPI); allure-commandline 2.46.1 (npm); Allure 3 repository — https://github.com/allure-framework/allure3
- CrowdStrike, Channel File 291 Root Cause Analysis (6 Aug 2024) — https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf

_Last reviewed: 2026-10_
