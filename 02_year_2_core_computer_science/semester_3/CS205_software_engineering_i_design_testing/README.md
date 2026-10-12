# CS205 · Software Engineering I: Design, Testing and Collaboration

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 2 · 3 | 4 (≈ 120 hours) | L1 → L3 | [FND111](../../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md), [FND104](../../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) | [SWE301](../../../03_majors/software_engineering/year_3/SWE301_software_architecture_and_design_patterns/README.md), [SWE304](../../../03_majors/software_engineering/year_3/SWE304_ai_assisted_software_engineering_agents/README.md), [QAE301](../../../03_majors/software_quality_test_engineering/year_3/QAE301_testing_foundations_and_test_design_techniques/README.md), [IND401](../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md), and every applied major |

## Why this course matters now

Writing code is no longer the bottleneck. Google's 2025 DORA report found that 90% of technology professionals use AI at work and more than 80% believe it has made them more productive, yet 30% have little or no trust in AI-generated code, and higher AI adoption went with higher delivery throughput but lower delivery stability. The Stack Overflow 2025 survey found 66% of developers frustrated by AI answers that are "almost right, but not quite". In METR's 2025 randomised trial, experienced open-source developers took 19% longer with early-2025 AI tools on their own mature repositories while believing they had been 20% faster; METR's February 2026 follow-up reported that newer measurements were unreliable because many developers now refuse to work without AI. The lesson is that AI coding agents (Claude Code, OpenAI Codex, GitHub Copilot, Cursor, Gemini CLI) amplify whatever engineering system they land in. This course builds that system: clear specifications, designs that keep change cheap, tests that act as evidence, reviews that catch what generators miss, and pipelines that make shipping safe.

## Learning outcomes

By the end you can:

1. **Write** requirements as user stories with testable acceptance criteria, and **turn** them into specifications precise enough for a teammate or an AI agent to implement.
2. **Design** modules with low coupling and clear interfaces, and **record** decisions in design docs and architecture decision records (ADRs).
3. **Use** trunk-based Git workflows, small pull requests, `git bisect` and merge queues in a team of 3–5.
4. **Review** code, including AI-generated code, for correctness, design, tests and security, and **give** feedback people act on.
5. **Build** a test suite across the pyramid (unit, integration, contract, end-to-end), and **measure** its strength with mutation testing rather than coverage alone.
6. **Practise** TDD and test-first prompting, and **detect** when an agent weakens tests to make them pass.
7. **Set up** a CI pipeline with quality gates, dependency and supply-chain checks, and safe delivery (feature flags, canary, rollback).
8. **Estimate** with ranges and forecasts, and **run** a small agile process with honest retrospectives and blameless postmortems.
9. **Measure** the effect of AI tools on your own work with a controlled design, and **interpret** published studies critically.

## Chapters and lessons

### Chapter 1 · How software gets built in 2026 (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Programming vs engineering | "Programming integrated over time" (*Software Engineering at Google*); cost of change; Hyrum's law | Mine an open-source repo's history: contributors, age of the oldest surviving line |
| 1.2 Process models | Waterfall, iterative, Scrum, Kanban, Shape Up; which fits regulated, startup and open-source work | Map three real projects to the model they actually use, with evidence |
| 1.3 Measuring delivery | DORA metrics (deployment frequency, lead time, change failure rate, recovery time); the SPACE framework | Compute DORA-style metrics from a public GitHub repo's PRs and releases |
| 1.4 Agents in the loop | What coding agents do (read the repo, plan, edit, run tests, open PRs) and which decisions stay human | Watch an agent close one issue; list every decision you would want to review |

**Check your understanding:** Why does Hyrum's law make "just a small API change" risky? Why can deployment frequency rise while user-visible quality falls? Which of the agent's decisions in 1.4 would you never delegate, and why?

### Chapter 2 · Requirements and specifications (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Eliciting needs | Stakeholders, interviews, observation; functional vs non-functional needs (latency, availability, accessibility, privacy under India's DPDP Act 2023) | Interview a real user (a canteen manager, a club secretary) and write their requirements |
| 2.2 Stories and acceptance criteria | INVEST stories; Given/When/Then (Gherkin); edge cases as criteria | Ten stories with criteria for a campus library app |
| 2.3 Precise specifications | Pre- and postconditions, state machines, API contracts in OpenAPI, examples as specifications | OpenAPI spec for 4 endpoints, linted with Spectral |
| 2.4 Specifications for agents | Spec-driven development (spec → plan → tasks, as in GitHub Spec Kit); `AGENTS.md` context files; ambiguity as the main failure mode | Give an agent a vague and a precise spec for the same feature; diff the results |
| 2.5 Requirement smells | Untestable adjectives ("fast", "easy"), hidden assumptions, missing failure cases | Rewrite 10 smelly requirements as testable ones |

**Check your understanding:** What makes an acceptance criterion testable? Why do non-functional requirements cause more late surprises than functional ones? What does a good spec for an agent contain that a good spec for a senior engineer can leave out?

### Chapter 3 · Design: modules, interfaces and decisions (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Managing complexity | Cohesion, coupling, information hiding (Parnas, 1972), deep vs shallow modules | Split a 1,500-line "god class"; show the dependency graph before and after |
| 3.2 Interfaces and contracts | Abstraction boundaries, dependency inversion, errors as part of the API, immutability | A payment-provider interface with two fake providers behind it |
| 3.3 Everyday patterns | Strategy, adapter, observer, repository, factory, and when a pattern is overkill | Replace a type `switch` with a strategy; argue whether it paid off |
| 3.4 Architecture basics | Layered and hexagonal (ports and adapters) designs; modular monolith vs microservices; C4 diagrams | C4 context and container diagrams for an app you use |
| 3.5 Recording decisions | Design docs, ADRs, RFC-style review | A 2-page design doc and two ADRs for P2 |

**Check your understanding:** Why is a module with a small interface and a large implementation usually better than the reverse? When does splitting into microservices make a system harder to change? What should an ADR record that the code never will?

### Chapter 4 · Version control workflows (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Git internals | Blobs, trees, commits, refs, the commit DAG, the reflog | Recover a "lost" commit after a bad reset |
| 4.2 Branching strategies | Trunk-based development, short-lived branches, feature flags; GitFlow and release branches | Simulate a release plus hotfix in both models; compare effort |
| 4.3 Pull requests and history | Small PRs, rebase vs merge, squash, Conventional Commits, semantic versioning, changelogs | Rewrite a messy branch into 4 clean, reviewable commits |
| 4.4 Repositories at scale | Protected branches, CODEOWNERS, merge queues, signed commits, monorepos; `git bisect run` | Find a planted regression in 500 commits with `git bisect run` |

**Check your understanding:** Why do long-lived branches make merges expensive? What does a merge queue guarantee that "CI passed on my branch" does not? When would you not squash?

### Chapter 5 · Code review (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 What review is for | Google's standard: approve when the change improves overall code health; design, correctness, tests, naming, complexity | Review 3 PRs using Google's reviewer guide |
| 5.2 The human side | Tone, blocking vs non-blocking comments, review latency, PR descriptions, author duties | Rewrite 10 harsh comments into actionable ones |
| 5.3 Reviewing AI-generated changes | Tests as evidence; hallucinated APIs and packages; over-broad diffs; insecure defaults (OWASP Top 10) | Review an agent-written PR with 6 planted issues; find at least 4 |
| 5.4 Automated reviewers | Linters, Semgrep, CodeQL, AI first-pass reviewers (for example GitHub Copilot code review): what each catches and misses | Run Semgrep and an AI reviewer on one PR; compare with your own findings |

**Check your understanding:** Why does review quality drop as PR size grows? What evidence should an AI-generated PR carry before a human reads the code? Which defects do static analysers find reliably, and which need a human?

### Chapter 6 · Testing I: unit tests and test design (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The test pyramid | Unit, integration, end-to-end; speed and cost per layer; the "testing trophy" alternative | Classify an open-source repo's tests and time each layer |
| 6.2 Good unit tests | Arrange–act–assert, one behaviour per test, pytest and JUnit 5 parametrisation, boundary values, equivalence classes | Test a date-range function to full branch coverage |
| 6.3 Test doubles | Stubs, mocks, fakes, spies; dependency injection; the over-mocking trap | Replace mocks of a database with an in-memory fake; compare brittleness after a refactor |
| 6.4 Beyond coverage | Limits of line and branch coverage; mutation testing (mutmut, PIT, Stryker); property-based testing (Hypothesis, jqwik, fast-check) | Raise a module's mutation score; find one bug with a property test |

**Check your understanding:** Why can 100% coverage coexist with a useless test suite? When is a mock better than a fake? What does a surviving mutant tell you?

### Chapter 7 · Testing II: integration, end-to-end and TDD (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Test-driven development | Red–green–refactor, triangulation, outside-in TDD | TDD kata (a rate limiter) with one commit per step |
| 7.2 Test-first prompting | Acceptance tests written first become the agent's specification; protecting test files so the agent cannot weaken them | Repeat the kata with an agent, tests first; record any attempt to edit tests |
| 7.3 Integration and contract tests | Testcontainers with real PostgreSQL and Redis; consumer-driven contracts with Pact; schema tests | Integration suite against a real PostgreSQL container |
| 7.4 End-to-end tests | Playwright, page objects, test data, causes of flakiness (timing, shared state, order), quarantine policy | Make a flaky sign-up test deterministic |
| 7.5 Testing legacy code | Characterisation (golden-master) tests, seams, approval tests | Pin an untested legacy module's behaviour before refactoring it |

**Check your understanding:** Why does TDD tend to produce smaller interfaces? An agent made the tests pass by changing an assertion: how would your process have caught it? Why are contract tests cheaper than end-to-end tests across services?

### Chapter 8 · Continuous integration and delivery (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 CI pipelines | GitHub Actions workflows, jobs, matrices, caching, artefacts; keeping feedback under ~10 minutes | Pipeline: format, lint, type-check, test, coverage, build |
| 8.2 Quality gates | Ruff or ESLint, mypy/pyright or `tsc`, Semgrep, CodeQL, secret scanning | Break each gate on purpose and confirm the pipeline blocks the merge |
| 8.3 Supply chain | Lockfiles, Dependabot or Renovate, SBOMs (CycloneDX, SPDX), SLSA provenance; hallucinated package names ("slopsquatting") | Generate an SBOM; verify every dependency exists and is the one intended |
| 8.4 Delivery | Continuous delivery vs deployment, environments, feature flags, canary releases, rollback | Ship a change behind a flag; roll it back without a redeploy |

**Check your understanding:** Why is a slow CI pipeline a design problem, not only an infrastructure one? What does an SBOM let you answer on the day a vulnerable library is announced? Why is a feature flag also a liability?

### Chapter 9 · Documentation, estimation and planning (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Docs as code | README anatomy; Diátaxis (tutorials, how-to guides, reference, explanation); generated API references; runbooks | Restructure a project's docs into the four Diátaxis types |
| 9.2 Estimation | Cone of uncertainty, relative sizing, planning poker, reference-class forecasting, Monte Carlo forecasts from throughput | Forecast P2's finish date as a range; compare with the actual date |
| 9.3 Agile in practice | Scrum Guide 2020 (roles, events, artefacts); Kanban WIP limits and flow metrics; Little's law | Run two one-week iterations of P2 with WIP limits |
| 9.4 Learning from failure | Blameless postmortems, contributing factors vs root cause, action items that get done | Postmortem for a bug that escaped in P2 |

**Check your understanding:** Why do single-number estimates hide the information managers need? What does Little's law say about cutting work in progress? Why is "human error" never a finished root cause?

### Chapter 10 · AI coding agents across the lifecycle (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 How agents work | The loop (gather context → plan → edit → run tools and tests → repeat); context windows; `AGENTS.md`/`CLAUDE.md`; tools through the Model Context Protocol; permissions and sandboxes | Write an `AGENTS.md` for P2; compare agent results on 5 issues with and without it |
| 10.2 Delegation design | Sizing tasks, spec → plan → tasks, checkpoints, review gates, parallel agents and merge conflicts | Delegate 3 issues in parallel; review and merge them |
| 10.3 Risks | Prompt injection through issues or repo files, secret exposure, insecure code, licence provenance, package hallucination, skill atrophy | Threat-model your agent set-up: what can it read, write and execute? |
| 10.4 Measuring productivity honestly | Randomised trials (GitHub Copilot 2023, Google 2024, METR 2025) and why their results differ; selection effects (METR 2026); perception vs measurement; DORA's "amplifier" finding | Run a small self-experiment on 6 matched tasks with and without an agent; report with uncertainty |

**Check your understanding:** Why might the same tool speed up a greenfield task and slow down work in a mature repository? What would make you distrust a vendor's "55% faster" claim for your team? Which parts of your process would you strengthen before giving agents more autonomy?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Repo archaeology and delivery metrics | — |
| 2 | 2 | Lab 2 · Specs for humans and agents | — |
| 3 | 3 | Lab 3 · Refactor the god class | **P1 due** |
| 4 | 3 | P2 team formation, design doc, ADRs | Design doc |
| 5 | 4 | Lab 4 · Git workflows and bisect | — |
| 6 | 5 | Lab 5 · Review gauntlet (human and AI PRs) | — |
| 7 | 6 | Lab 6 · Unit, mutation and property tests | Mid-term (AI off) |
| 8 | 7 | Lab 7 · TDD with and without an agent | — |
| 9 | 7 | Lab 8 · Integration and end-to-end | — |
| 10 | 8 | Lab 9 · CI/CD pipeline | — |
| 11 | 9 | P2 iteration 1 | Forecast |
| 12 | 9 | P2 iteration 2 | **P2 due** + postmortem |
| 13 | 10 | Lab 10 · Agent delegation and threat model | — |
| 14 | 10 | P3 | **P3 due** |
| 15 | Review | P3 presentation | Final exam (AI off): design + review |

## Working with AI in this course

- **Use AI for:** drafting tests from your acceptance criteria; scaffolding CI workflows; summarising large diffs; generating realistic test data; a first-pass review before human review; first drafts of docs. Tools to know: Claude Code, OpenAI Codex, GitHub Copilot (agent mode, coding agent and code review), Cursor, Gemini CLI, and spec-driven tooling such as GitHub Spec Kit and Kiro.
- **Do without AI (drills):** writing stories and acceptance criteria; the design doc; the first TDD kata; reviewing a PR fully before running any AI reviewer; estimation. Your judgement is what you are training, and the final exam is AI-off.
- **Verify AI output by:** tests written before the code; mutation testing to check that tests actually constrain behaviour; CI quality gates; confirming every new dependency exists, is maintained and is the package you meant; reading the full diff; running the change yourself; Semgrep or CodeQL on the result.
- **Where AI still fails here:** Veracode's 2025 study of 80 security-relevant coding tasks across more than 100 models found OWASP Top 10 vulnerabilities introduced in 45% of test cases. Spracklen et al. (USENIX Security 2025) found code models recommending packages that do not exist, at least 5.2% of the time for commercial models and 21.7% for open models on average, which attackers can exploit by registering those names. METR's 2025 trial shows that time saved writing code can be lost in prompting, waiting and reviewing on complex, mature codebases. In Lab 7 you will also see whether your agent tries to edit tests to make them pass; you record what happened.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| P1 (individual) | 10% |
| P2 (team of 3–5, with peer review) | 25% |
| P3 (individual, portfolio) | 25% |
| Final exam (AI off): spec, design and review tasks | 20% |

**Mastery gate.** You pass when you can: (1) turn a one-paragraph feature request into stories with testable acceptance criteria, a design doc and one ADR, in two hours without AI; (2) review a 400-line PR (human- or AI-written) with 7 planted defects and find at least 5, including the security defect, in 45 minutes; (3) take a repository with no tests and, in one working day, add a CI pipeline and tests that reach a mutation score of at least 60% on its core module.

## Industry reality

Where this is used (public sources): the DORA research programme's delivery metrics and its 2025 report on AI-assisted development; Google's published code-review guide and its book *Software Engineering at Google*; GitHub's open-source Spec Kit for spec-driven development (September 2025); the Linux Foundation's Agentic AI Foundation (December 2025), which now hosts the Model Context Protocol and the `AGENTS.md` convention; ONDC, India's open commerce network, which publishes its protocol specifications openly on GitHub, a large example of specification-first engineering. Every software role, from frontend to ML, works inside this lifecycle.

**Interview questions from this course**

1. *An agent produced a 2,000-line pull request. How do you review it?* Strong answer: ask for it to be split; read the spec and tests first; run it; check new dependencies exist and are intended; look for duplicated logic, swallowed errors and insecure defaults; the reviewer, not the tool, owns the approval.
2. *How do you decide what to test?* Strong answer: risk-based (money, data loss, security first); pyramid balance; boundaries and equivalence classes; property and contract tests where they fit; mutation score as a quality check; avoiding brittle, over-mocked tests.
3. *Trunk-based development or GitFlow for a team of 8 deploying daily?* Strong answer: trunk-based with short-lived branches, feature flags, required CI and a merge queue; GitFlow-style release branches only when supporting several released versions.
4. *Your two-week estimate is now in week three. What do you do?* Strong answer: tell people early; re-forecast from data; cut or re-sequence scope; surface the unknowns that caused the miss; avoid hidden overtime; take the lesson into the next estimate.
5. *Design an interface so the product can switch payment gateways (say, from Razorpay to another provider).* Strong answer: a port with adapters; idempotency keys; a normalised error taxonomy; webhook verification and replay handling; contract tests against fakes; versioning and migration plan.

## Resources (free first)

- **Books:** *Software Engineering at Google* (free online) — https://abseil.io/resources/swe-book ; *Pro Git* (free) — https://git-scm.com/book/en/v2
- **Courses:** MIT 6.031 Software Construction — https://web.mit.edu/6.031/ ; NPTEL Software Engineering (Rajib Mall, IIT Kharagpur) — https://nptel.ac.in/courses/106105182
- **Practice guides:** Google engineering practices (code review) — https://google.github.io/eng-practices/review/ ; Martin Fowler, "The Practical Test Pyramid" — https://martinfowler.com/articles/practical-test-pyramid.html ; Diátaxis — https://diataxis.fr/ ; The Scrum Guide — https://scrumguides.org/scrum-guide.html ; C4 model — https://c4model.com/ ; Michael Nygard, "Documenting Architecture Decisions" — https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- **Research:** DORA — https://dora.dev/ ; Forsgren et al., "The SPACE of Developer Productivity", ACM Queue (2021) — https://queue.acm.org/detail.cfm?id=3454124 ; Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules" (1972) — https://dl.acm.org/doi/10.1145/361598.361623
- **Tools:** Hypothesis — https://hypothesis.readthedocs.io/ ; Testcontainers — https://testcontainers.com/ ; Pact — https://docs.pact.io/ ; Playwright — https://playwright.dev/ ; GitHub Actions — https://docs.github.com/en/actions ; Semgrep — https://semgrep.dev/docs/ ; CodeQL — https://codeql.github.com/ ; SLSA — https://slsa.dev/
- **Agents and specs:** GitHub Spec Kit — https://github.com/github/spec-kit ; AGENTS.md — https://agents.md/ ; Claude Code — https://code.claude.com/docs/en/overview ; OpenAI Codex CLI — https://github.com/openai/codex ; GitHub Copilot — https://docs.github.com/en/copilot ; Gemini CLI — https://github.com/google-gemini/gemini-cli
- **Paid, optional:** John Ousterhout, *A Philosophy of Software Design*; Michael Feathers, *Working Effectively with Legacy Code*; Forsgren, Humble and Kim, *Accelerate*.

## Sources

- Google Cloud, "Announcing the 2025 DORA report" (24 Sep 2025) — https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report ; DORA 2025 report — https://dora.dev/research/2025/dora-report/ (checked 2026-10)
- Stack Overflow Developer Survey 2025, AI section — https://survey.stackoverflow.co/2025/ai (checked 2026-10)
- METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (Jul 2025) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ (checked 2026-10)
- METR, "We are Changing our Developer Productivity Experiment Design" (24 Feb 2026) — https://metr.org/blog/2026-02-24-uplift-update/ (checked 2026-10)
- Peng et al., "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot" (arXiv 2302.06590, 2023) — https://arxiv.org/abs/2302.06590 (checked 2026-10)
- Paradis et al., "How much does AI impact development speed? An enterprise-based randomized controlled trial" (arXiv 2410.12944; ICSE-SEIP 2025) — https://arxiv.org/abs/2410.12944 (checked 2026-10)
- Veracode, "AI-Generated Code Poses Major Security Risks in Nearly Half of All Development Tasks" (press release on the 2025 GenAI Code Security Report, 30 Jul 2025) — https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/ (checked 2026-10)
- Spracklen et al., "We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs", USENIX Security 2025 — https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen (checked 2026-10)
- Linux Foundation, "Linux Foundation Announces the Formation of the Agentic AI Foundation" (9 Dec 2025) — https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation (checked 2026-10)
- ONDC protocol specifications on GitHub — https://github.com/ONDC-Official (checked 2026-10)

_Last reviewed: 2026-10_
