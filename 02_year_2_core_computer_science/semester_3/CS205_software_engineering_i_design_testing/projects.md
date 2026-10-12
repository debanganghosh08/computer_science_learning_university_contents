# CS205 · Labs and projects

Use Python or TypeScript (Java is fine where a lab says so), Git and GitHub, and one AI coding agent of your choice for the labs that ask for it. Every lab that uses an agent also asks you to record what it did and what you changed.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Repo archaeology and delivery metrics | Mine a public repository: contributors over time, oldest surviving code, PR lead times, release cadence | A notebook with DORA-style metrics and three conclusions you can defend | 3 h |
| 2 · Specs for humans and agents | Write stories, Gherkin criteria and an OpenAPI spec for one feature; give an agent a vague and a precise version | Both specs, both agent results, a diff and a one-page analysis of what ambiguity cost | 4 h |
| 3 · Refactor the god class | Split a provided 1,500-line class into cohesive modules behind clear interfaces, protected by characterisation tests | Before/after dependency graphs, passing tests, an ADR explaining the split | 5 h |
| 4 · Git workflows and bisect | Practise rebase, interactive history clean-up, conflict resolution, reflog recovery and `git bisect run` on a 500-commit repo | Clean branch history, the bisect script, the offending commit and why it broke | 3 h |
| 5 · Review gauntlet | Review 4 PRs (2 human, 2 agent-written) with planted defects, using Google's reviewer guide; then run Semgrep and an AI reviewer | Review comments, a table of defects found by you vs each tool | 4 h |
| 6 · Unit, mutation and property tests | Test a pricing module; measure coverage, then mutation score; add property tests until mutants die | Tests, mutation report before and after, one bug found by a property | 5 h |
| 7 · TDD with and without an agent | Do a rate-limiter kata by TDD by hand; repeat with an agent given only the failing tests, with test files write-protected | Commit-per-step history for both runs; time, defects and any test-tampering attempts | 5 h |
| 8 · Integration and end-to-end | Integration tests with Testcontainers (PostgreSQL); a Pact contract between two services; a Playwright test made deterministic | Passing suites; flake rate over 20 runs before and after your fixes | 5 h |
| 9 · CI/CD pipeline | GitHub Actions: format, lint, type-check, test, Semgrep, SBOM, build; feature-flagged release and rollback | Workflow files, a run under 10 minutes, screenshots of each gate blocking a bad PR | 4 h |
| 10 · Agent delegation and threat model | Delegate 3 issues to agents in parallel with an `AGENTS.md`; threat-model what the agent can read, write and execute | Merged PRs with your review notes; a threat model with mitigations applied | 4 h |

## Projects

### P1 · Test-and-CI rescue (L1, ~6 hours)

**Real-world inspiration.** Most engineering time goes into existing code. Maintainers of small open-source libraries and teams inheriting legacy modules face the same first task: make the code safe to change.

**What to build.** Take the provided untested billing module (an illustrative invoice and tax calculator) or a small open-source library with weak tests. Pin current behaviour with characterisation tests, add focused unit tests, set up CI (lint, type-check, test, coverage) and rewrite the README into Diátaxis sections.

**Acceptance criteria**
- Characterisation tests pass against the original code, proving no behaviour changed.
- Branch coverage of at least 80% and a mutation score of at least 50% on the core module.
- CI runs on every PR in under 5 minutes and blocks merges on failure.
- At least one real defect found and reported (issue or test marked as expected failure), with a minimal reproduction.

**Stretch goals.** Property-based tests for rounding rules; a contribution guide and a PR template.

**What it proves to an employer.** You can walk into an unfamiliar codebase and make it safer to change within a day.

### P2 · Campus food pre-order service, as a team (L2, ~15 hours each, team of 3–5)

**Real-world inspiration.** Food-ordering flows (Swiggy, Zomato) and UPI payment collection are familiar to every Indian student; ONDC publishes open protocol specifications for commerce. The scope here is illustrative and runs on campus scale.

**What to build.** A web API and minimal UI where students pre-order canteen meals for pickup slots with limited capacity; an order state machine (placed → paid → preparing → ready → collected or cancelled); payment through an adapter with a fake provider (or a payment provider's test mode); an admin view for the canteen. The process is assessed as much as the product: stories, design doc and ADRs, trunk-based Git, mandatory review, CI, two one-week iterations, a forecast and a postmortem.

**Acceptance criteria**
- At least 20 stories with acceptance criteria, each traced to at least one automated test.
- Every merged PR has an approving review from another team member and green CI; median PR size under 300 changed lines.
- Mutation score of at least 60% on the domain module; integration tests against a real database container; one Playwright end-to-end test for the golden path with zero flakes over 20 consecutive runs.
- Slot overbooking is impossible: a test fires 50 concurrent orders at a 20-seat slot and exactly 20 succeed.
- `docker compose up` starts the whole system; the README explains how to run and test it.
- Forecast vs actual delivery reported; one blameless postmortem; peer evaluation of each member.

**Stretch goals.** Feature flags with a canary rollout; an accessibility audit with axe; notifications when an order is ready.

**What it proves to an employer.** You can ship in a team with the habits (small PRs, reviews, tests, CI, honest planning) that make teams fast for years, not weeks.

### P3 · Agent-built service, measured (L3, portfolio-grade, ~30 hours, individual)

**Real-world inspiration.** Group expense apps such as Splitwise, and UPI collect requests used to settle them. Teams adopting coding agents must decide, with evidence, where agents help and how to keep quality.

**What to build.** A split-bill ledger API: groups, expenses with uneven splits, balances, a settlement plan that minimises the number of transfers, idempotent payment-request endpoints and an audit log. Build it with a spec-driven agent workflow: specification → plan → tasks (GitHub Spec Kit or your own template), an `AGENTS.md`, tests written first and write-protected, agent implementation, and human review against a checklist. Alongside, run a self-experiment: split 8 comparable tasks at random (coin flip) between "agent" and "manual" and record time, review findings and escaped defects.

**Acceptance criteria**
- A hidden acceptance suite written by a peer from your spec passes at 95% or more.
- Property tests prove that balances in every group always sum to zero and that the settlement plan never uses more than n − 1 transfers for n members.
- Replaying the same payment request 100 times creates exactly one record (idempotency key).
- Mutation score of at least 70% on the balance and settlement module.
- CI includes Semgrep or CodeQL with zero high-severity findings, an SBOM, and a check that every dependency resolves to the intended package.
- The experiment report contains the per-task data, how tasks were randomised, mean and spread for each arm, threats to validity (learning effects, task differences, small sample) and a comparison with published studies (GitHub 2023, Google 2024, METR 2025), ending with a conclusion the data supports.
- Design doc, three ADRs and a 5-minute demo.

**Stretch goals.** Multi-currency with explicit rounding rules; settlement via minimum-cost flow (links to [CS201](../CS201_algorithms_and_complexity/README.md)); a canary deployment.

**What it proves to an employer.** You can use agents to go faster without giving up correctness, and you can measure the trade-off instead of guessing. Teams adopting agents need people who can do both.

## Feeds into

- [SWE301 Software Architecture and Design Patterns](../../../03_majors/software_engineering/year_3/SWE301_software_architecture_and_design_patterns/README.md) and [SWE302 Low-Level Design and Clean Code at Scale](../../../03_majors/software_engineering/year_3/SWE302_low_level_design_and_clean_code_at_scale/README.md): Chapter 3 grows into full architecture and design practice.
- [SWE304 AI-Assisted Software Engineering](../../../03_majors/software_engineering/year_3/SWE304_ai_assisted_software_engineering_agents/README.md): P3's agent workflow and measurement method.
- [QAE301](../../../03_majors/software_quality_test_engineering/year_3/QAE301_testing_foundations_and_test_design_techniques/README.md) and [QAE304](../../../03_majors/software_quality_test_engineering/year_3/QAE304_testing_in_ci_cd_and_test_infrastructure/README.md): Chapters 6–8 in depth.
- [IND401 Industry Co-op Studio](../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): P2's team process is the baseline expected on co-op.
- [CS215 Cloud and DevOps Foundations](../../semester_4/CS215_cloud_and_devops_foundations/README.md): CI/CD extends into deployment and operations.
