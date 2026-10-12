# QAE · Software Quality and Test Engineering: roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [Software Quality and Test Engineering major](../../../03_majors/software_quality_test_engineering/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

| Level | Common titles |
|---|---|
| Entry | QA Engineer, Test Engineer, Manual Tester, Associate SDET |
| Mid | SDET (Software Development Engineer in Test), Automation Engineer, Performance Test Engineer |
| Senior | Senior SDET, Test Architect, Quality Engineering Lead |
| Leadership | QA Manager, Head of Quality Engineering |

Newer variants: AI evaluation engineer (testing LLM features and agents) and quality engineer for AI-assisted delivery.

## What the work looks like day to day

- Design tests with named techniques: equivalence partitioning, boundary values, decision tables, state transitions (QAE301).
- Automate UI tests (Playwright, Selenium) and API tests, and keep them reliable (QAE302).
- Run load and stress tests and read the latency percentiles (QAE303).
- Wire tests into CI/CD, manage test data and environments, hunt flaky tests (QAE304).
- Test across browsers and mobile devices (QAE305).
- Test security and accessibility basics (QAE403).
- Build evaluation suites for AI features, where the "right answer" is not a single string (QAE402).
- Report quality risk to the team before a release.

## Demand signals

- **US projections.** Software quality assurance analysts and testers: 187,600 jobs, +6% from 2025 to 2035 (+10,600), slower than software developers (+10%) ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm)).
- **AI in QA is early.** "43% of organizations are experimenting with Gen AI in QA, but only 15% have scaled it enterprise-wide". Use of synthetic test data rose from 14% (2024) to 25% (2025). Generative AI was the top-ranked skill for quality engineers (63%), and 58% cited challenges adopting AI-powered tools ([Capgemini World Quality Report 2025–26](https://www.capgemini.com/insights/research-library/world-quality-report-2025-26/)).
- **Stability pressure.** AI adoption is positively related to delivery throughput but negatively related to delivery stability ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)). More code, shipped faster, needs stronger automated checks.
- **India.** No strong public demand data for testers in India specifically was found. NASSCOM's projected shift "from volume to skill mix" in hiring ([NASSCOM 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026)) points to fewer manual-testing roles and more automation and quality-engineering roles (**analysis**).

## How AI is changing the role

**Automated or mostly automated.** Writing test cases from requirements, generating unit and API test code, self-healing UI locators when the page changes (QAE401), synthetic test data, and first-pass bug report summaries.

**Augmented.** Exploratory testing (AI suggests unusual inputs), triaging flaky failures, analysing performance-test results, and test-gap analysis.

**Growing in value.**

- **Test strategy**: deciding what to test, at what level, and what risk remains.
- **Oracles**: knowing what the correct behaviour is, especially when AI generated both the code and the tests. Tests written by the same model that wrote the code can share its blind spots.
- **Testing AI systems**: evaluation sets, graders, statistical pass rates, regression tracking for non-deterministic outputs (QAE402).
- **Property-based testing and fuzzing** to find bugs nobody imagined (QAE501).
- **Quality metrics that leaders trust** (QAE404).

**Analysis.** Manual, script-following testing is the most exposed work in this family. Quality engineering is not: as AI produces more code, independent verification becomes more important, and the skills are shifting from executing tests to designing evidence that software works.

## Pay (indicative)

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Software quality assurance analysts and testers | Median $104,300; 10th $61,440; 90th $167,010 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm) |
| India | Quality Assurance (QA) Engineer | Average base ₹5.6 lakh; base range ₹2.7–10 lakh; under 1 year ≈₹2.9 lakh total (604 profiles, Jun 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Quality_Assurance_%28QA%29_Engineer/Salary) |

SDET roles at product companies are often levelled and paid like software engineering roles; no reliable public source separates them.

## The hiring loop

Typical loop (varies by company):

1. Testing fundamentals: "how would you test this login page / elevator / payment API?" Interviewers look for test-design techniques and risk thinking.
2. Coding for automation: write tests for an API or a function; sometimes a DSA round for SDET roles.
3. Framework design: structure a test automation framework, handle test data and parallel runs.
4. Debugging: a flaky test or a failing pipeline.
5. Behavioural: a bug you caught late, a release you blocked.

See [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- Test design techniques and risk-based prioritisation.
- Programming at a software-engineer level.
- CI/CD and test infrastructure.
- Performance testing and analysis.
- Security and accessibility testing basics.
- Evaluation design for AI systems.
- Clear bug reports and quality reporting.

## Adjacent roles and transitions

- **Software engineering**: SDETs often move into development ([SWE](SWE_software_engineering.md)).
- **DevOps and SRE**: CI/CD and reliability ([OPS](OPS_devops_sre_platform_engineering.md)).
- **Security testing** ([OFF](OFF_ethical_hacking_offensive_security.md)).
- **AI evaluation** ([AIE](AIE_ai_engineering.md)).
- **Frontend and mobile testing** ([FE](FE_frontend_engineering.md), [MOB](MOB_mobile_engineering.md)).

## Sources

All checked October 2026.

- BLS, Occupational Outlook Handbook: Software Developers, Quality Assurance Analysts, and Testers (2025–35; May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm
- Capgemini, World Quality Report 2025–26. https://www.capgemini.com/insights/research-library/world-quality-report-2025-26/
- DORA 2025 (24 Sep 2025). https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- NASSCOM, Strategic Review 2026. https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026
- Payscale India: Quality Assurance (QA) Engineer (self-reported; 12 Oct 2026). https://www.payscale.com/research/IN/Job=Quality_Assurance_%28QA%29_Engineer/Salary

_Last reviewed: 2026-10_
