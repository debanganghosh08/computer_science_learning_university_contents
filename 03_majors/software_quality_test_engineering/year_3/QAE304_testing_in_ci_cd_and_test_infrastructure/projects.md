# QAE304 · Labs and projects

Use GitHub Actions or GitLab CI free tiers, or self-hosted runners on your laptop (kind or Docker). Keep a **pipeline ledger** for every lab: p50 and p95 duration, queue time, flaky rate, cache-hit rate and estimated cost. Claims without ledger data do not count. Never store real credentials in a course repository; use short-lived tokens or OIDC, and never run workflows from untrusted forks with secrets.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Test sizes and hermeticity | Classify an open-source project's tests by Google test size; make 5 non-hermetic tests hermetic (network, clock, filesystem, order) | Classification table with timings; diffs; 100 clean runs of the fixed tests | 3 h |
| 2 · Reproducible, hardened pipeline | Containerised test runner, lockfiles, actions pinned by SHA, least-privilege permissions, cache keys | Workflow, a local reproduction of one CI failure, a permissions audit | 4 h |
| 3 · Workers, shards and balance | Run a suite at 1–8 workers; shard 4 ways with duration-based balancing; merge blob reports | Speed-up plot, shard imbalance before and after, merged report | 4 h |
| 4 · Ephemeral environment per PR | Docker Compose or kind + Helm environment per pull request with seeded synthetic data and a preview URL | Spin-up time over 10 PRs, teardown evidence, cost per environment-hour | 6 h |
| 5 · Migrations and teardown | Expand-and-contract column rename tested across two releases; time-to-live garbage collection | Migration tests, rollback test, 50-PR teardown report | 4 h |
| 6 · Test impact analysis on history | Replay 100 historical commits of an open-source repository with graph- or coverage-based selection | Selection rate, missed failures (with each one explained), time saved | 6 h |
| 7 · Flaky scoring and quarantine | Compute flakiness scores from CI history; automate quarantine with owner issues and deadlines | Scoring script, policy document, bot run log | 5 h |
| 8 · Allure and PR failure bot | Allure Report with history; a bot that comments the failing test, owner and trace link on PRs | Report URL or artefact, 5 example PR comments | 4 h |
| 9 · Gates and merge queue | Required checks; diff coverage and diff mutation gates; a merge queue catching a semantic conflict | Gate list with measured false-positive rates over 50 PRs; the conflict demonstration | 5 h |
| 10 · Cache and cost | Remote cache (Bazel or a build-tool cache) and an autoscaled runner pool in kind | Cache-hit rate, time saved, monthly cost estimate with assumptions | 4 h |

## Projects

### P1 · Fast, sharded pipeline for an existing suite (L1, ~6 hours)

**Real-world inspiration:** the first thing a new SDET is often asked to do: "make CI faster without losing tests".

**What to build:** take your QAE302 P1 suite (or the instructor's 150-test suite). Build a pipeline with a smoke stage, a 3-browser matrix, 4-way sharding, merged HTML and Allure reports, dependency caching and traces as artefacts.

**Acceptance criteria:**
- Wall-clock time reduced by ≥ 60% against the serial baseline, measured as p50 over 10 runs each.
- Slowest shard within 20% of the fastest.
- Time to first failure under 3 minutes on 10 deliberately broken commits.
- Actions pinned by SHA; workflow permissions minimal (audit included).
- One merged report per run that a reviewer can open in one click from the PR.

**Stretch goals:** reproduce the pipeline in GitLab CI and compare durations and configuration size.

**What it proves to an employer:** you can make a test suite fast enough that developers keep running it.

### P2 · Test selection and flaky-test programme for an open-source repository (L2, ~15 hours)

**Real-world inspiration:** Meta's predictive test selection and Google's flaky-test data show that at scale you cannot run everything, and you cannot trust results without managing flakiness.

**What to build:** fork an active open-source project with at least 1,000 tests and CI history (for example a mid-sized Python or TypeScript library; agree the choice with the instructor). Build:
1. A test impact analysis selector (dependency-graph or per-test coverage map, optionally with a learned ranking).
2. A replay harness over at least 200 historical commits.
3. A flakiness detector (scheduled repeat runs plus history) and a quarantine bot that opens owner issues with deadlines.

**Acceptance criteria:**
- Replay reports: average fraction of tests selected, wall-clock saved, and missed failures (a commit where the full suite failed but the selection passed). Target: zero missed faulty commits, or each miss explained with a fix to the selector.
- Selector handles non-code changes (configuration, fixtures, dependency bumps) by falling back to a full run; demonstrated.
- Flaky detector finds every test the instructor made flaky in a hidden branch, with no more than 2 false flags across the suite.
- Quarantine policy enforced by the bot: owner, deadline, automatic escalation; quarantined tests still run and report.
- A 2-page report with the data, threats to validity and a recommendation to the project's maintainers.

**Stretch goals:** offer the flaky-test findings upstream as issues; compare an LLM-based failure classifier with your history-based score on 100 labelled failures.

**What it proves to an employer:** you can cut CI cost and restore trust in test results with measured evidence, which is a core developer-productivity skill.

### P3 · Test platform for a multi-service application (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** internal test platforms that give every pull request its own environment and a single trustworthy verdict. Target: [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo), [.NET eShop](https://github.com/dotnet/eShop) or your QAE302 P3 application.

**What to build:**
- Ephemeral environment per PR on kind (or k3d) with Helm, seeded synthetic data and one virtualised third-party dependency.
- A layered pipeline: lint and types → unit → contract (`can-i-deploy`) → API → sharded UI → performance smoke with a budget (from QAE303) → accessibility smoke.
- Test impact analysis with a nightly full-run safety net.
- Flaky detection and quarantine automation.
- Quality gates with measured false-positive rates and audited overrides.
- A dashboard: PR feedback p50/p95, queue time, flaky rate, cache-hit rate, cost per PR, and the DORA metrics you can compute from the repository.

**Acceptance criteria:**
- Environment ready in under 5 minutes (p95 over 20 PRs) and torn down in 100% of cases.
- PR feedback p95 under 15 minutes for a typical change; full nightly run documented.
- Flaky rate below 0.5% of test executions over 2 weeks of runs, with every quarantined test owned.
- Every gate has a measured false-positive rate; at least one gate tuned after measurement.
- An auto-fix or triage agent experiment with tests write-protected: results reported as precision and recall on planted failures, and every attempt to modify a test logged.
- A runbook so another student can operate the platform for a week; they confirm it in writing.

**Stretch goals:** OpenTelemetry tracing of pipeline runs; a cost-reduction change with before/after numbers.

**What it proves to an employer:** you can build and run the test platform a product organisation ships on, and you can show its speed, reliability and cost.

## Feeds into

- [QAE404 Quality Engineering Leadership and Metrics](../../year_4/QAE404_quality_engineering_leadership_and_metrics/README.md): the dashboard and gates become organisation-level metrics and policy.
- [QAE403 Security and Accessibility Testing](../../year_4/QAE403_security_and_accessibility_testing/README.md): DAST, dependency and accessibility stages plug into this pipeline.
- [OV03 DevSecOps](../../../../04_overlaps/OV03_devsecops/README.md): policy as code and supply-chain gates on the same platform.
- [QAE flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/QAE_software_quality_test_engineering.md): P3 is its infrastructure layer.
