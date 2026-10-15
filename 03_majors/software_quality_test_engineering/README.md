# Software Quality and Test Engineering (QAE) · Learning path

| Code | Years | Entry requirements | Market page | Interview loop |
|---|---|---|---|---|
| QAE | 3–5 (after the common Years 1–2) | [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [QAE roles and market](../../06_career_and_market_readiness/01_market_map/roles/QAE_software_quality_test_engineering.md) | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/README.md) |

This major trains engineers who produce **evidence that software works**, and who can say exactly how much risk remains when it ships. It is not a "manual testing" track. Graduates write production-grade automation code, design test strategies by risk, build the test infrastructure that lets a company release many times a day, load-test systems before a sale or a ticket rush, test on the phones people actually own, check security and accessibility, and evaluate AI systems whose answers are never exactly the same twice. By Year 5 they work at the frontier of the field: property-based testing, fuzzing and formal verification at industrial scale.

## 1. Who this major is for, and the roles it leads to

Choose this major if you enjoy finding out how things break, if "how do we know?" is your favourite question, and if you want to be the person a team trusts before a release. You must like programming: almost every role below is a software engineering role whose product is confidence.

| Role | What people in it actually do | Where this major prepares you |
|---|---|---|
| QA Engineer / Test Engineer (entry) | Design test cases with named techniques, run exploratory sessions, write clear bug reports, automate regression checks | QAE301, QAE302 |
| SDET (Software Development Engineer in Test) | Write test code and test tools at a developer's standard; review developers' tests; build fixtures, fakes and test data services | QAE302, QAE304, CAR301 |
| Test Automation Engineer / Automation Architect | Design the automation framework (UI, API, contract), keep it fast and non-flaky, choose tools | QAE302, QAE304, QAE305 |
| Performance Engineer | Model real workloads, run load, stress and soak tests, read latency percentiles, find the bottleneck, plan capacity for peak events | QAE303 |
| Mobile and Cross-Browser QA | Test across browser engines, Android and iOS versions, low-end devices and bad networks; run device-farm pipelines | QAE305 |
| Security and Accessibility Test Engineer | Run DAST and dependency scanning on the team's own apps in CI; audit against WCAG 2.2 with tools and screen readers | QAE403 |
| AI Evaluation Engineer | Build golden datasets, graders and statistical eval suites for LLM features and agents; gate prompt and model changes | QAE402, QAE401, overlap OV12 |
| Test Infrastructure / Developer Productivity Engineer | Run the CI test platform: sharding, test selection, flaky-test quarantine, ephemeral environments | QAE304 |
| Quality Engineering Lead, Test Architect, QA Manager, Head of QE | Own quality strategy and metrics, decide release risk, build and coach the QE team, report to leadership | QAE404, LCH502 |
| Founder (testing tools or QE services) | Build a testing product or a specialist QE consultancy | QAE401, QAE501, LCH502 |

Titles follow the [market page](../../06_career_and_market_readiness/01_market_map/roles/QAE_software_quality_test_engineering.md): entry (QA Engineer, Test Engineer, Associate SDET), mid (SDET, Automation Engineer, Performance Test Engineer), senior (Senior SDET, Test Architect, QE Lead) and leadership (QA Manager, Head of QE). The same title can mean very different work: at many product companies an SDET is levelled and paid like a software engineer, while some services roles are mostly manual execution.

## 2. How AI is changing testing

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

**Test generation and repair are now product features.** Playwright 1.56 added three test agents: a *planner* that explores an app and writes a test plan, a *generator* that turns the plan into test files, and a *healer* that runs the suite and repairs failing tests. Since 1.62, Playwright bundles its MCP server so coding agents can drive a browser directly ([Playwright release notes](https://playwright.dev/docs/release-notes)). Commercial tools (for example mabl and Tricentis Testim) and the open-source Healenium project sell or ship "self-healing" locators.

**Industrial evidence exists, with filters.** Meta's TestGen-LLM only kept generated tests that built, passed repeatedly and added coverage: on Instagram Reels and Stories, 75% of generated tests built, 57% passed reliably and 25% increased coverage, and engineers accepted 73% of its recommendations ([Alshahwan et al., FSE 2024](https://arxiv.org/abs/2402.09171)). Meta's later ACH system generates mutants (planted faults) first and then tests that catch them; engineers accepted 73% of its 571 privacy-hardening tests ([Foster et al., 2025](https://arxiv.org/abs/2501.12862)). Google's OSS-Fuzz used LLM-written fuzz targets to add 370,000+ lines of coverage across 272 C/C++ projects and found 26 new vulnerabilities, including CVE-2024-9143 in OpenSSL ([Google, Nov 2024](https://security.googleblog.com/2024/11/leveling-up-fuzzing-finding-more.html)).

**Adoption is broad but shallow.** Capgemini's World Quality Report 2025–26 found 43% of organisations experimenting with generative AI in QA but only 15% having scaled it enterprise-wide; 58% cited challenges adopting AI-powered tools; 60% struggle with secure, scalable test data; use of synthetic test data rose from 14% (2024) to 25% (2025); and generative AI was the top-ranked skill for quality engineers (63%) ([Capgemini](https://www.capgemini.com/insights/research-library/world-quality-report-2025-26/)).

**More code needs more verification.** DORA's 2025 research found AI adoption positively related to delivery throughput but negatively related to delivery stability ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)). When AI writes the code and the tests, the tests can share the code's blind spots: someone independent must decide what "correct" means.

**Manual-only QA is under pressure.** The US Bureau of Labor Statistics projects QA analysts and testers at +6% for 2025–35, against +10% for software developers ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm)). Payroll research found early-career employment declines concentrated in occupations where AI *automates* tasks rather than augments them ([Brynjolfsson, Chandar and Chen, Nov 2025](https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf)), and NASSCOM expects Indian tech hiring to shift "from volume to skill mix" ([NASSCOM 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026)). No public dataset isolates manual-tester jobs, so the following is **analysis**: writing test cases from specifications and executing scripted steps are exactly the tasks the tools above automate. A role made only of those tasks is the most exposed role in this family.

**Testing AI is a new job.** LLM features and agents need evaluation suites, graders and statistics, not single expected strings. Anthropic's engineering guidance (January 2026) distinguishes capability evals from regression evals and *pass@k* (at least one success in k tries) from *pass^k* (all k tries succeed), and recommends starting with 20–50 tasks drawn from real failures ([Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)). Services firms now advertise assurance of "models, agents, decisions, controls, and outcomes" (vendor marketing, [Coforge QE page](https://www.coforge.com/capabilities/quality-engineering)).

| Mostly automated now | Augmented (a human decides) | Growing in value | Taught in |
|---|---|---|---|
| Test cases from specs, unit and API test code, locator repair, synthetic data, first-draft bug summaries | Exploratory testing, flaky-test triage, performance analysis, accessibility audits, test-gap analysis | Test strategy and risk, **oracles** (what "correct" means), AI evaluation, property-based testing and fuzzing, test infrastructure, metrics leaders trust | QAE301 (strategy, oracles), QAE401 (AI tools), QAE402 (AI evals), QAE501 (PBT, fuzzing) |

**Analysis.** The work is moving from *executing* tests to *designing evidence*. Every course in this major makes you use the AI tools, then measure them: mutation scores for generated tests, false-heal rates for self-healing locators, judge-human agreement for LLM graders.

### India context

- **A large services market.** Indian IT services firms sell testing as "quality engineering". Mid-tier Coforge bought the Hyderabad testing specialist Cigniti in stages (54% by December 2024) and announced closure of the acquisition on 30 April 2026 ([Coforge](https://news.coforge.com/newsroom/press-release/coforge-successfully-closes-cigniti-acquisition)). On 12 October 2026, cigniti.com redirected to Coforge's Quality Engineering page. No reliable public headcount for testing roles in India was found (unconfirmed).
- **A testing product built in India.** BrowserStack, a cloud of real browsers and devices, was co-founded in 2011 by Ritesh Arora and Nakul Aggarwal, is headquartered in Mumbai, and raised $200 million at a $4 billion valuation in June 2021 ([Wikipedia](https://en.wikipedia.org/wiki/BrowserStack)). It reports 50,000+ customers in 135+ countries and 3,500+ real devices and browsers ([BrowserStack](https://www.browserstack.com/company)).
- **Android-heavy, low-end-heavy users.** Android held 93.89% of India's mobile OS market in September 2026 ([StatCounter](https://gs.statcounter.com/os-market-share/mobile/india)), which is why QAE305 tests on low-end Android and slow networks.
- **Rules that need test evidence.** SEBI's July 2025 circular requires accessibility audits of regulated entities' digital platforms ([Deque summary](https://www.deque.com/blog/sebi-sets-a-new-standard-for-digital-accessibility-in-finance-in-india/)); the DPDP Rules notified in November 2025 make copying real personal data into test environments a legal risk ([PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014)).
- **Pay.** Payscale's self-reported data (June 2026) puts the average base pay of a QA Engineer in India at ₹5.6 lakh, with a ₹2.7–10 lakh range (see the [market page](../../06_career_and_market_readiness/01_market_map/roles/QAE_software_quality_test_engineering.md) for the source). SDET and quality-engineering roles at product companies are often paid on software engineering bands, but no reliable public source separates them.

## 3. The 5-year path

### Years 1–2: the common core

Every Year 1–2 course is required. These matter most for QAE:

| Course | Why it matters for QAE |
|---|---|
| [FND101 Programming I (Python)](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md) and [FND111 Programming II (Java and TypeScript)](../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md) | Test code is code: pytest, JUnit, TypeScript for Playwright |
| [FND104 Developer's Toolkit](../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) | Shell, Git and CI are where tests run |
| [FND114 Web Foundations](../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md) | HTTP, DOM and accessibility basics behind UI and API testing |
| [FND115 Databases I](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md) | Test data, database assertions, data-quality checks |
| [FND116 Probability and Statistics I](../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | Percentiles, flakiness rates, confidence intervals for evals |
| [FND105 AI-Native Learning and Building](../../01_year_1_foundations/semester_1/FND105_ai_native_learning_and_building/README.md) | First evals with promptfoo or Inspect |
| [CS203 Operating Systems](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) and [CS204 Computer Networks](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md) | Why systems slow down, time out and race: the raw material of QAE303 and flaky-test diagnosis |
| [CS205 Software Engineering I](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | Entry requirement: pyramid, test doubles, TDD, mutation and property testing basics, CI |
| [CS213 Security Foundations](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) | Needed for QAE403 |
| [CS214 Machine Learning Foundations](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) | Needed for QAE402 |
| [CS215 Cloud and DevOps Foundations](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) | Containers and pipelines for QAE304 |

### Years 3–5: the major

| Semester | Major courses | Shared courses | Other |
|---|---|---|---|
| 5 (Year 3) | [QAE301 Testing Foundations and Test Design Techniques](year_3/QAE301_testing_foundations_and_test_design_techniques/README.md) · [QAE302 Test Automation Engineering: UI and API](year_3/QAE302_test_automation_engineering_ui_and_api/README.md) · [QAE303 Performance and Load Testing](year_3/QAE303_performance_and_load_testing/README.md) | [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) | 1 elective |
| 6 (Year 3) | [QAE304 Testing in CI/CD and Test Infrastructure](year_3/QAE304_testing_in_ci_cd_and_test_infrastructure/README.md) · [QAE305 Mobile and Cross-Browser Testing](year_3/QAE305_mobile_and_cross_browser_testing/README.md) | [CAR301 Career Lab I: DSA Mastery, Portfolio and Open Source](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) | 1–2 electives |
| 7 (Year 4) | [QAE401 AI in Testing: Generated Tests, Self-Healing and Test Agents](year_4/QAE401_ai_in_testing_generated_tests_self_healing/README.md) · [QAE402 Testing AI Systems: Evals and Non-Determinism](year_4/QAE402_testing_ai_systems_evals_and_non_determinism/README.md) | [IND401 Industry Co-op Studio](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) | Overlap course A |
| 8 (Year 4) | [QAE403 Security and Accessibility Testing](year_4/QAE403_security_and_accessibility_testing/README.md) · [QAE404 Quality Engineering Leadership and Metrics](year_4/QAE404_quality_engineering_leadership_and_metrics/README.md) | [CAR401 Career Lab II: Interviews, System Design and AI-Driven Assessments](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) | Overlap course B |
| 9 (Year 5) | [QAE501 Frontier Seminar: Property-Based Testing, Fuzzing and Verification at Scale](year_5/QAE501_frontier_seminar_property_based_testing_fuzzing/README.md) | [RES501 Research Methods](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) · [RES502 Reading, Reproducing and Extending Papers](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) · [THS501 Thesis or Capstone I](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) | — |
| 10 (Year 5) | — | [THS502 Thesis or Capstone II](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) · [LCH502 Career Launch and Founder Studio](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) | Electives |

Prerequisites inside the major (from [`catalog.json`](../../catalog.json)): QAE301 → QAE401; QAE302 → QAE402; QAE303 → QAE403; QAE304 → QAE404; QAE401 + QAE403 → QAE501. All Year 3 courses need only CS205.

## 4. Skill map by level

| Level | You can… | Mastery gate (do it, don't describe it) |
|---|---|---|
| L0 → L1 (Year 1) | Program in Python, Java and TypeScript; use Git and the shell; write SQL; explain HTTP | A tested 500-line CLI tool with a README and a passing CI run |
| L2 (end of Year 2) | Write unit, integration and end-to-end tests; use test doubles; run mutation and property tests on small modules | CS205's gate: tests and CI for an untested repository reaching ≥ 60% mutation score on its core module in one day |
| L3 (end of Year 3) | Design tests by risk and named techniques; build a non-flaky UI + API + contract framework; model and run load tests; run tests in parallel in CI; test on real devices and three browser engines | On an unfamiliar web app in one week: a risk-based test plan, a Playwright + API suite with < 0.5% flaky runs over 200 CI runs, a load test with SLO thresholds, and three reproducible bug reports a maintainer accepts |
| L4 (end of Year 4) | Evaluate AI test tools with evidence; build eval suites for LLM features; gate security and accessibility in CI; set quality strategy and metrics for an organisation | Defend a quality strategy for a 40-engineer product to a panel: metrics with baselines, an AI-feature eval with judge-human agreement measured, DAST and WCAG 2.2 AA gates, and a canary policy with automatic rollback |
| L5 (Year 5) | Apply property-based testing, fuzzing and formal specification to real systems; reproduce and extend testing research | Find and report a real bug in an open-source project with a property test or fuzzer, or reproduce a published testing result within stated error and extend it in a workshop-quality paper |

## 5. Recommended overlaps and electives

**Overlaps** (Year 4; course A in semester 7, course B in semester 8):

| Overlap | Why it fits a quality engineer | Composed of |
|---|---|---|
| [OV12 Agent Infrastructure and Platform Engineering](../../04_overlaps/OV12_agent_infrastructure_platform/README.md) | Best fit for AI evaluation roles: its course [OV12B Agent Evaluation and Reliability Engineering](../../04_overlaps/OV12_agent_infrastructure_platform/OV12B_agent_evaluation_and_reliability_engineering/README.md) extends QAE402 to long-running agents | AIE401, OPS403, BE501 |
| [OV05 AI Security and Safety Engineering](../../04_overlaps/OV05_ai_security_safety/README.md) | Defensive red-team suites and guardrail testing for LLM products | AIE305, OFF403, SAR403 |
| [OV03 DevSecOps](../../04_overlaps/OV03_devsecops/README.md) | Security gates, supply-chain checks and policy as code in the pipelines QAE304 builds | OPS301, SAR305, SEC302 |

Take the composing courses you lack as electives. OV03's are Year 3 courses, so it is the easiest fit. OV05's AIE305 is a Year 3 course but OFF403 and SAR403 are Year 4; OV12's are Year 4–5 courses. Check prerequisites in the catalog before planning.

**Electives** (pick 3–5):

- [AIE305 Evaluating LLM Systems](../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md): the AI-engineering view of evals, before QAE402.
- [FE305 Frontend Testing and Tooling](../frontend_engineering/year_3/FE305_frontend_testing_and_tooling/README.md) and [FE303 CSS, Design Systems and Accessibility](../frontend_engineering/year_3/FE303_css_design_systems_and_accessibility/README.md): component testing and accessibility depth.
- [OPS301 CI/CD Engineering](../devops_sre_platform_engineering/year_3/OPS301_ci_cd_engineering/README.md) and [OPS303 Observability](../devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md): the platform under QAE304 and QAE404.
- [SWE305 Concurrency and Performance Engineering](../software_engineering/year_3/SWE305_concurrency_and_performance_engineering/README.md) or [OPS404 Performance and Capacity Engineering](../devops_sre_platform_engineering/year_4/OPS404_performance_and_capacity_engineering/README.md): deeper performance work after QAE303.
- [OPS402 Chaos Engineering and Resilience](../devops_sre_platform_engineering/year_4/OPS402_chaos_engineering_and_resilience/README.md): fault injection as testing.
- [OFF302 Web Application Security Testing](../ethical_hacking_offensive_security/year_3/OFF302_web_application_security_testing/README.md): authorised security testing beyond scanners.
- [MLE304 Model Evaluation, Fairness and Robustness](../machine_learning_engineering/year_3/MLE304_model_evaluation_fairness_and_robustness/README.md): classical ML testing, CheckList, slices.
- [MOB301 Android with Kotlin and Jetpack Compose](../mobile_engineering/year_3/MOB301_android_with_kotlin_and_jetpack_compose/README.md): build what you test in QAE305.
- [CSG401 Formal Methods and Program Verification](../computer_science_general/year_4/CSG401_formal_methods_and_program_verification/README.md): strongly recommended before QAE501.
- [SWE304 AI-Assisted Software Engineering](../software_engineering/year_3/SWE304_ai_assisted_software_engineering_agents/README.md): how coding agents work, before QAE401.

## 6. Flagship industry project

The QAE flagship is described in [`05_industry_projects/QAE_software_quality_test_engineering.md`](../../06_career_and_market_readiness/05_industry_projects/QAE_software_quality_test_engineering.md): a quality programme for a real open-source application (for example [ERPNext](https://github.com/frappe/erpnext)), with bug reports filed upstream. You write a risk-based strategy, build UI, API and contract automation, run workload-modelled load tests, run the suite in CI with sharding and flaky-test quarantine, test on real devices and three browser engines, gate security and accessibility, evaluate any AI feature, and report metrics a maintainer would act on. Its parts come from QAE301 P3 (strategy), QAE302 P3 (framework), QAE303 P2 (load model), QAE304 P3 (infrastructure), QAE403 P3 (security and accessibility gates), QAE402 P3 (evals) and QAE404 P2 (metrics). Build it in Year 4 and defend it in CAR401 and LCH502.

## 7. Certifications (optional, never required)

| Certification | Honest value |
|---|---|
| ISTQB Certified Tester Foundation Level (CTFL) v4.0 | Shared vocabulary for test design and process. Frequently listed in services-company job ads (unconfirmed as a general rule); rarely decisive at product companies. Required before ISTQB specialist exams such as CT-GenAI. Covers much of QAE301 |
| ISTQB Advanced: Test Automation Engineering (CTAL-TAE v2.0), Test Analyst (CTAL-TA v4.0) | Useful for automation-architect and consulting roles where clients ask for certified staff; a working framework on GitHub is stronger evidence |
| ISTQB Performance Testing (CT-PT), Mobile Application Testing (CT-MAT) | Niche; worth it only if your employer pays and your role is in that niche |
| ISTQB AI Testing (CT-AI v2.0) and Testing with Generative AI (CT-GenAI, approved July 2025, minor update v1.1 in 2026) | New, so their hiring signal is unproven (unconfirmed). Read the free syllabi as reading lists for QAE401–402 |
| IAAP certifications (CPACC, WAS) for accessibility | SEBI's 2025 circular refers to IAAP-certified auditors ([Deque summary](https://www.deque.com/blog/sebi-sets-a-new-standard-for-digital-accessibility-in-finance-in-india/)), which gives them real value for accessibility audit work in Indian finance |
| Scrum or agile tester certificates | Low signal for engineers |

ISTQB's current list (Foundation, Advanced, Specialist and Expert levels) is on its [certifications page](https://istqb.org/certifications/). **Analysis:** for SDET and AI-evaluation roles, a public repository with a non-flaky suite, mutation scores and an eval report beats any certificate. All ISTQB syllabi are free to download, so you can learn the material without paying for the exam.

## 8. The interview loop for this role

A typical loop (details vary; see the [market page](../../06_career_and_market_readiness/01_market_map/roles/QAE_software_quality_test_engineering.md)):

| Round | What is tested | Prepared by |
|---|---|---|
| Testing fundamentals | "How would you test this login page, lift, payment API or chatbot?" Interviewers want named techniques, risk ordering and oracles, not a list of random cases | QAE301 |
| Coding for automation | Write tests for an API or a function; sometimes a DSA round for SDET roles | QAE302, CAR301 |
| Framework design | Structure an automation framework: layers, test data, parallel runs, reporting, flakiness policy | QAE302, QAE304 |
| Debugging | A flaky test, a failing pipeline, a p99 regression | QAE302, QAE303, QAE304 |
| AI-era round (growing) | Review AI-generated tests and find what they miss; design an eval for an LLM feature | QAE401, QAE402 |
| Behavioural | A bug you caught late, a release you blocked, a metric you changed | QAE404, IND401 |

Simulations, rubrics and the QAE question bank are in [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/README.md).

## 9. Fast track: manual QA → SDET

For working testers (1–6 years, often manual or record-and-playback) who want SDET, automation-architect or AI-evaluation roles. Budget 12–15 hours a week for about 12 months.

1. **Placement (week 1).** Attempt the mastery gates of [FND101](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md) and [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md). Most manual testers must close a programming gap first: do FND101 and FND111's labs before anything else, AI off.
2. **Months 1–3: automation that lasts.** QAE302 (Playwright, API and contract tests) and the test-design chapters of QAE301. Rebuild one real regression suite from work (within your employer's rules) and measure its flaky rate before and after.
3. **Months 4–6: pipeline and data.** QAE304. Get your suite sharded and running on every pull request, with a quarantine policy and an Allure report your developers actually read.
4. **Months 7–9: pick a specialism.** QAE303 (performance), QAE305 (mobile) or QAE402 (AI evaluation). AI evaluation has the newest demand; performance has the deepest moat.
5. **Months 10–12: prove it.** QAE401 (measure AI test tools with mutation testing) and a public portfolio project modelled on the flagship. Run one mock interview per fortnight from month 6.
6. **Throughout.** One CAR301 timed DSA set per week if you target product-company SDET roles; keep a bug-report portfolio of upstream issues you filed in open-source projects.

## Sources

All checked October 2026.

- Playwright release notes (test agents since 1.56; bundled MCP server since 1.62) — https://playwright.dev/docs/release-notes
- Alshahwan et al., "Automated Unit Test Improvement using Large Language Models at Meta" (arXiv 2402.09171; FSE 2024) — https://arxiv.org/abs/2402.09171
- Foster et al., "Mutation-Guided LLM-based Test Generation at Meta" (arXiv 2501.12862, Jan 2025) — https://arxiv.org/abs/2501.12862
- Google Open Source Security Team, "Leveling Up Fuzzing: Finding more vulnerabilities with AI" (20 Nov 2024) — https://security.googleblog.com/2024/11/leveling-up-fuzzing-finding-more.html
- Capgemini, World Quality Report 2025–26 — https://www.capgemini.com/insights/research-library/world-quality-report-2025-26/
- Google Cloud, "Announcing the 2025 DORA report" (24 Sep 2025) — https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- US BLS, Occupational Outlook Handbook: Software Developers, Quality Assurance Analysts, and Testers (2025–35) — https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm
- Brynjolfsson, Chandar, Chen, "Canaries in the Coal Mine?" (Nov 2025) — https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf
- NASSCOM, Strategic Review 2026 — https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026
- Anthropic, "Demystifying evals for AI agents" (9 Jan 2026) — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Coforge, "Coforge successfully closes Cigniti acquisition" (30 Apr 2026) — https://news.coforge.com/newsroom/press-release/coforge-successfully-closes-cigniti-acquisition ; Coforge Quality Engineering page (cigniti.com redirect target, 12 Oct 2026) — https://www.coforge.com/capabilities/quality-engineering
- BrowserStack company page — https://www.browserstack.com/company ; Wikipedia, BrowserStack (founding, headquarters, 2021 funding) — https://en.wikipedia.org/wiki/BrowserStack
- StatCounter, mobile OS market share India, Sep 2026 — https://gs.statcounter.com/os-market-share/mobile/india
- Deque, summary of SEBI's accessibility circular (31 Jul 2025; revised 29 Aug 2025) — https://www.deque.com/blog/sebi-sets-a-new-standard-for-digital-accessibility-in-finance-in-india/
- PIB, DPDP Rules notified (14 Nov 2025) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014
- ISTQB certifications page — https://istqb.org/certifications/ ; ISTQB CT-GenAI launch — https://istqb.org/istqb-certified-tester-specialist-level-testing-with-generative-ai-ct-genai-press-release/ ; CT-GenAI v1.1 update — https://istqb.org/istqb-announces-minor-update-to-certified-tester-testing-with-generative-ai-ct-genai/

_Last reviewed: 2026-10_
