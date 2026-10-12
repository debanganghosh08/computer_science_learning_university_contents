# Software Engineering (SWE) · Learning path

| Code | Years | Entry requirements | Market page | Interview loop |
|---|---|---|---|---|
| SWE | 3–5 (after the common Years 1–2) | [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS201](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) | [SWE roles and market](../../06_career_and_market_readiness/01_market_map/roles/SWE_software_engineering.md) | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) |

This major treats software engineering as a discipline, not a layer of the stack. Backend (BE), frontend (FE) and DevOps/SRE (OPS) majors go deep into one layer. This major teaches what every layer shares: architecture and design, language and runtime judgement, performance and concurrency, large-scale design, modernizing old systems, operating what you ship, and leading other engineers. It also teaches how to do all of that when coding agents write a large share of the code.

## 1. Who this major is for, and the roles it leads to

Choose this major if you want to be the engineer who can be dropped into any codebase, understand it, change it safely and explain the trade-offs. It suits people who like structure, who enjoy reading code as much as writing it, and who want a path to senior, staff or engineering-management roles.

| Role | What people in it actually do | Where this major prepares you |
|---|---|---|
| Software Engineer I / SDE-1 / Associate Engineer / Graduate Engineer Trainee | Deliver well-scoped tickets with review; write tests; fix bugs; learn the codebase | SWE302, SWE304, CAR301 |
| Software Engineer II / SDE-2 | Own features end to end, including design notes, rollout and on-call | SWE301, SWE303, SWE305, SWE403 |
| Senior Software Engineer / SDE-3 | Design components other people build on; review heavily; unblock others; handle the incidents nobody planned for | SWE401, SWE402, SWE403 |
| Staff / Principal Engineer, Architect | Set technical direction across teams; write strategy and RFCs; pick the few decisions that are hard to reverse. Will Larson's four staff archetypes are Tech Lead, Architect, Solver and Right Hand ([StaffEng](https://staffeng.com/guides/staff-archetypes/)) | SWE401, SWE404, SWE501 |
| Tech Lead | Steer one team's technical direction and delivery; plan, estimate, split work between people and agents | SWE404 |
| Engineering Manager | Own people, hiring, delivery and team health; usually reached after senior level | SWE404, LCH502 |
| Product Engineer | Build features end to end with strong product sense; talk to users; measure outcomes | SWE301, SWE304, overlap OV08 |
| Founding Engineer (early-stage startup) | Build the first version alone or with two or three others, choose the stack, then make it survive growth | All of the above, plus LCH502 |
| Developer Productivity / Developer Experience Engineer | Build the internal tools, CI, codemods and agent workflows that make other engineers faster | SWE304, SWE402, electives in OPS |

Titles are not standard. An "SDE-2" at a product company and a "Senior Software Engineer" at a services company can be the same level ([SWE market page](../../06_career_and_market_readiness/01_market_map/roles/SWE_software_engineering.md)).

## 2. How AI coding agents are changing software engineering

All figures below were checked in October 2026. Paragraphs marked **Analysis** are interpretation.

**Adoption is near-universal, trust is conditional.** In the 2026 Stack Overflow survey, 65.9% of respondents use AI coding assistants or coding agents at work; among agent users, the most used are Claude Code (65.5%) and GitHub Copilot (58.7%). Only 6.6% trust AI output for important decisions, and 48.0% trust it only when they can easily verify it ([Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data)). Google's DORA research found 90% of technology professionals use AI at work ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)).

**Capability is rising fast; reliability lags.** METR measures the length of task an agent completes at a given success rate. Claude Opus 4.6 (February 2026) succeeds half the time on tasks that take an expert about 12 hours, but its 80%-reliability horizon is about 70 minutes ([METR data file](https://metr.org/assets/benchmark_results_1_1.yaml)). Benchmarks are also being questioned: in February 2026 OpenAI said it no longer reports SWE-bench Verified, citing contamination and flawed tests, and recommended the harder SWE-bench Pro ([OpenAI](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)).

**Productivity studies disagree, for understandable reasons.**

| Study | Result |
|---|---|
| Field experiments with GitHub Copilot (Cui et al., summarised in the [AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)) | +26% pull requests completed; less experienced developers gained most |
| [METR randomised trial](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) (16 experienced open-source developers, 246 tasks, early 2025) | 19% slower with AI on their own mature repositories, while believing they were 20% faster |
| [METR update](https://metr.org/blog/2026-02-24-uplift-update/) (Feb 2026) | Point estimates of 18% and 4% less time, with intervals that include a slowdown; METR calls it an "unreliable signal" because many developers refused to work without AI |
| [DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) | AI adoption goes with higher delivery throughput but still with lower delivery stability; AI is "an amplifier" of a team's existing strengths and weaknesses |
| [Anthropic Economic Index, Jan 2026](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report) | About 61% of software-development requests to Claude succeed; adjusting for task success "roughly halves" the implied productivity gain |
| [Anthropic internal survey, Dec 2025](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic) (132 staff, self-reported) | Claude used in about 60% of work, +50% self-reported productivity; some engineers reported fewer mentoring conversations and worried about skill atrophy |

**Entry level is where the pressure is.** US software developers aged 22–25 were close to 20% below their late-2022 employment peak by September 2025, while older developers kept growing ([Brynjolfsson, Chandar and Chen, Nov 2025](https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf)). Hiring activity grew 22% for lead developers but 7% for entry level ([HackerRank 2025](https://www.hackerrank.com/reports/developer-skills-report-2025)). The BLS still projects US software developer jobs +10% for 2025–35, against −7% for "computer programmers" whose repetitive tasks are being automated ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm)). In India, NASSCOM expects FY27 hiring "to shift from volume to skill mix" ([NASSCOM 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026)).

**What is being automated:** boilerplate, CRUD endpoints, test scaffolding, routine bug fixes, framework upgrades and large mechanical migrations. Google reported that 80% of the code changes in one large ID-type migration were AI-authored and the total time fell by an estimated 50% ([Nikolov et al., 2025](https://arxiv.org/abs/2501.06972)).

**What grows in value:**

| Skill | Why it compounds | Taught in |
|---|---|---|
| Specification | Ambiguity is the main way agents fail; a precise spec plus acceptance tests is the new unit of delegation | SWE304, SWE302 |
| Review and verification | More code is produced than people write; someone must tell correct from "almost right" | SWE302, SWE304, SWE501 |
| Architecture and boundaries | Agents work inside the structure they find; good boundaries make agent tasks small and checkable | SWE301, SWE401 |
| Performance and concurrency | Hard to verify by reading; AI-written concurrent code fails in ways tests rarely show | SWE305, SWE303 |
| Production ownership | Only 20% of AI users use it for deploying, operating or troubleshooting production ([Stack Overflow, Oct 2026](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)) | SWE403 |
| Leading people and agents | Someone decides what to build, splits it, and owns the result | SWE404 |

**Analysis.** The job is moving from "write the code" to "specify, generate, verify, integrate and own the code". This major keeps AI-off drills in every course because you cannot judge output you could not have produced, and because many interview loops still test fundamentals without AI.

## 3. The 5-year path

### Years 1–2: the common core

Every course in Years 1–2 is required. These matter most for this major:

| Course | Why it matters for SWE |
|---|---|
| [FND111 Programming II (Java and TypeScript)](../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md) | Types, interfaces and objects: the raw material of design |
| [FND112 Data Structures and Algorithms I](../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) and [CS201 Algorithms and Complexity](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) | DSA rounds; reasoning about cost |
| [FND106 Technical Communication](../../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md) | Design docs, reviews and RFCs are writing |
| [CS203 Operating Systems](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) | Threads, locks and memory, needed for SWE305 |
| [CS205 Software Engineering I](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | Entry requirement: specs, testing, review, CI, first contact with agents |
| [CS211 Database Systems Internals](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) and [CS212 Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | Storage, replication and consistency, needed for SWE401 |
| [CS216 Programming Languages, Compilers and Interpreters](../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md) | Runtimes and type systems, needed for SWE303 |

### Years 3–5: the major

| Semester | Major courses | Shared courses | Other |
|---|---|---|---|
| 5 (Year 3) | [SWE301 Software Architecture and Design Patterns](year_3/SWE301_software_architecture_and_design_patterns/README.md) · [SWE302 Low-Level Design and Clean Code at Scale](year_3/SWE302_low_level_design_and_clean_code_at_scale/README.md) · [SWE303 Programming Languages in Practice: Go, Rust and the JVM](year_3/SWE303_programming_languages_in_practice_go_rust/README.md) | [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) | 1 elective |
| 6 (Year 3) | [SWE304 AI-Assisted Software Engineering: Agents in the SDLC](year_3/SWE304_ai_assisted_software_engineering_agents/README.md) · [SWE305 Concurrency and Performance Engineering](year_3/SWE305_concurrency_and_performance_engineering/README.md) | [CAR301 Career Lab I: DSA Mastery, Portfolio and Open Source](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) | 1–2 electives |
| 7 (Year 4) | [SWE401 Large-Scale System Design](year_4/SWE401_large_scale_system_design/README.md) · [SWE402 Legacy Modernization and Refactoring with AI](year_4/SWE402_legacy_modernization_and_refactoring_with_ai/README.md) | [IND401 Industry Co-op Studio](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) | Overlap course A |
| 8 (Year 4) | [SWE403 Reliability, Observability and Incident Engineering for Developers](year_4/SWE403_reliability_observability_and_incident/README.md) · [SWE404 Engineering Leadership and Technical Strategy](year_4/SWE404_engineering_leadership_and_technical_strategy/README.md) | [CAR401 Career Lab II: Interviews, System Design and AI-Driven Assessments](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) | Overlap course B |
| 9 (Year 5) | [SWE501 Frontier Seminar: Agentic Software Engineering and Program Synthesis](year_5/SWE501_frontier_seminar_agentic_software_engineering/README.md) | [RES501 Research Methods](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) · [RES502 Reading, Reproducing and Extending Papers](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) · [THS501 Thesis or Capstone I](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) | — |
| 10 (Year 5) | — | [THS502 Thesis or Capstone II](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) · [LCH502 Career Launch and Founder Studio](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) | Electives |

Course prerequisites inside the major: SWE301 → SWE401; SWE302 → SWE402; SWE303 → SWE403; SWE304 → SWE404; SWE401 + SWE403 → SWE501.

## 4. Skill map by level

| Level | You can… | Mastery gate (do it, don't describe it) |
|---|---|---|
| L0 → L1 (Year 1) | Write small programs in Python, Java and TypeScript; use Git; write SQL | Build and test a 500-line CLI tool with a README and a passing CI run |
| L2 (end of Year 2) | Build a small service with tests and CI; read an open-source codebase; review a pull request | CS205's gate: spec + design doc + ADR in two hours without AI; find 5 of 7 planted defects in a 400-line PR |
| L3 (end of Year 3) | Design modules with enforced boundaries; solve LLD problems; write idiomatic Go or Rust and modern Java; profile and fix a concurrency bug; run a coding agent on a real repo with tests, hooks and review gates | Take an unfamiliar 30,000-line repo: produce its C4 diagrams, find one performance and one concurrency defect with evidence, and ship an agent-assisted feature that passes review and mutation testing |
| L4 (end of Year 4) | Design a system for millions of users with capacity numbers; modernize a legacy module behind a strangler with characterization tests; define SLOs and debug an incident from traces; lead a design review and write strategy | Pass a 60-minute HLD round and a design-doc review by a panel; run a migration where shadow traffic shows zero unexplained diffs for 7 days; lead a game-day incident as incident commander |
| L5 (Year 5) | Read, reproduce and extend agentic software engineering papers; build evaluation harnesses; publish | Reproduce one SWE-bench-style result within stated error, extend it, and submit a workshop-quality paper or a merged contribution to an open benchmark |

## 5. Recommended overlaps and electives

**Overlaps** (Year 4; each has two courses, A in semester 7 and B in semester 8):

| Overlap | Why it fits a software engineer | Composed of |
|---|---|---|
| [OV08 Full-Stack AI Product Engineering](../../04_overlaps/OV08_full_stack_ai_product_engineering/README.md) | Product engineer and founding engineer roles: ship AI features end to end | FE403, BE403, AIE404 |
| [OV02 Cloud-Native Backend](../../04_overlaps/OV02_cloud_native_backend/README.md) | The most common senior SWE job shape: services on Kubernetes and managed cloud | BE301, BE304, CLD303 |
| [OV12 Agent Infrastructure and Platform Engineering](../../04_overlaps/OV12_agent_infrastructure_platform/README.md) | Developer-productivity and platform teams that run coding agents for a whole company | AIE401, OPS403, BE501 |

Take the composing courses you lack as Year 3 electives. OV02's are all Year 3 courses, so it is the easiest fit. OV08 and OV12 list Year 4–5 courses as prerequisites; check the catalog before planning them.

**Electives** (pick 3–5):

- [BE301 API Design](../backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md) and [BE304 Asynchronous Systems](../backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md): the service mechanics SWE301 and SWE401 assume.
- [CSG303 Distributed Systems II](../computer_science_general/year_3/CSG303_distributed_systems_ii_consensus_replication/README.md): before SWE401 if you want infrastructure roles.
- [CSG401 Formal Methods and Program Verification](../computer_science_general/year_4/CSG401_formal_methods_and_program_verification/README.md): strongly recommended before SWE501.
- [AIE304 Tool Use and AI Agents](../ai_engineering/year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md): how agent harnesses work inside, alongside SWE304.
- [QAE401 AI in Testing](../software_quality_test_engineering/year_4/QAE401_ai_in_testing_generated_tests_self_healing/README.md): generated tests and test agents.
- [OPS401 Platform Engineering](../devops_sre_platform_engineering/year_4/OPS401_platform_engineering_and_internal_developer/README.md): golden paths and internal developer platforms.
- [SAR302 Threat Modeling](../security_architecture/year_3/SAR302_threat_modeling/README.md): every senior design review now includes a threat model.
- [FE404 Frontend System Design at Scale](../frontend_engineering/year_4/FE404_frontend_system_design_at_scale/README.md): if you are aiming at product-engineer roles.

## 6. Flagship industry project

The SWE flagship is described in [`05_industry_projects/SWE_software_engineering.md`](../../06_career_and_market_readiness/05_industry_projects/SWE_software_engineering.md). It joins the major's threads into one system that you design, build with coding agents under your own review gates, load-test, operate under SLOs, break on purpose, and document with ADRs, a design doc and postmortems. Its parts come from SWE301 P3 (architecture), SWE304 P1 and P2 (agent workflow), SWE305 P3 (performance), SWE401 P3 (design doc) and SWE403 P3 (reliability). Build it in Year 4 and use it as the centrepiece of your portfolio in CAR401 and LCH502.

## 7. Certifications (optional, never required)

| Certification | Honest value |
|---|---|
| Oracle Certified Professional: Java SE Developer | Proves Java language knowledge. Some Indian services companies and their clients ask for it in staffing (unconfirmed as a general rule). Product companies rarely ask. |
| AWS Certified Developer – Associate or Certified Kubernetes Application Developer (CKAD) | Useful if you aim at cloud-native backend roles (OV02). CKAD is hands-on, so it says more than multiple-choice exams. |
| iSAQB CPSA-Foundation (software architecture) | Recognised mainly in German-speaking Europe. Low signal elsewhere. |
| Scrum or agile certificates | Low signal for engineers. Shipping evidence beats them. |
| Vendor AI-tool certificates (for example GitHub's Copilot certification) | Very low signal. A public repository showing your agent workflow, review gates and measured results says far more. |

**Analysis.** For software engineers, certificates rarely move a hiring decision. A merged open-source contribution, a portfolio project with load-test numbers, and a strong interview performance do.

## 8. The interview loop for this role

A typical loop (details vary by company; see the [market page](../../06_career_and_market_readiness/01_market_map/roles/SWE_software_engineering.md)):

| Round | What is tested | Prepared by |
|---|---|---|
| Online assessment | 2–3 timed DSA problems | CS201, CAR301 |
| Coding (2–3 rounds) | Clean, tested code under time; explaining complexity | CS201, SWE302 |
| Low-level design (common in India) | Classes, interfaces, patterns, concurrency for problems like a parking lot, rate limiter, Splitwise or seat booking | SWE302, SWE301, SWE305 |
| High-level system design (mid-level and above) | Requirements, estimates, storage and caching choices, consistency, failure handling | SWE401, CAR401 |
| AI-assisted coding (growing) | Using an AI tool on a realistic task and catching its mistakes. Canva asks: "Can they identify and fix issues in AI-generated code?" ([Canva, Jun 2025](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)) | SWE304 |
| Behavioural | Ownership, conflict, failure, influence without authority | SWE404, IND401 |

Some employers forbid AI in live interviews ([Anthropic](https://www.anthropic.com/candidate-ai-guidance)), so prepare for both. Simulations and question banks: [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/).

## 9. Fast track for working professionals

For engineers with 1–5 years of experience (for example in a services company) who want product-company, senior or staff roles. Budget 12–15 hours a week for about 12 months.

1. **Placement (week 1).** Attempt the mastery gates of CS201 and CS205. Fill gaps before continuing.
2. **Months 1–3: immediate leverage.** SWE304 (agents with review gates) and SWE302 (LLD and review). Apply both at work from week one.
3. **Months 4–6: design depth.** SWE301 and SWE305. Use your employer's codebase (within its rules) for the architecture-recovery and profiling labs.
4. **Months 7–9: senior signals.** SWE401 and SWE403. Write one real design doc and one real postmortem at work.
5. **Months 10–12: pick one.** SWE402 if your company runs legacy systems; SWE404 if you are moving into tech lead or management; SWE303 if you need a second language.
6. **Throughout.** One CAR301 timed DSA set per week, and one mock interview per fortnight from month 6.

## Sources

All checked October 2026.

- Stack Overflow, 2026 Developer Survey: AI (6 Oct 2026) — https://survey.stackoverflow.co/2026/ai/data ; blog — https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/
- Google Cloud, "Announcing the 2025 DORA report" (24 Sep 2025) — https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- METR, time-horizon data file (v1.1) — https://metr.org/assets/benchmark_results_1_1.yaml ; randomised trial (10 Jul 2025) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ; update (24 Feb 2026) — https://metr.org/blog/2026-02-24-uplift-update/
- OpenAI, "Why we no longer evaluate SWE-bench Verified" (23 Feb 2026) — https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- Stanford HAI, AI Index 2026 — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- Anthropic Economic Index, January 2026 report — https://www.anthropic.com/research/anthropic-economic-index-january-2026-report ; "How AI is transforming work at Anthropic" (2 Dec 2025) — https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- Brynjolfsson, Chandar, Chen, "Canaries in the Coal Mine?" (13 Nov 2025) — https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf
- HackerRank, 2025 Developer Skills Report — https://www.hackerrank.com/reports/developer-skills-report-2025
- US BLS, Occupational Outlook Handbook, Software Developers (2025–35) — https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm
- NASSCOM, Strategic Review 2026 — https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026
- Nikolov et al., "How is Google using AI for internal code migrations?" (arXiv 2501.06972, Jan 2025) — https://arxiv.org/abs/2501.06972
- Will Larson, StaffEng, "Staff archetypes" — https://staffeng.com/guides/staff-archetypes/
- Canva Engineering, "Yes, you can use AI in our interviews" (11 Jun 2025) — https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/ ; Anthropic candidate AI guidance — https://www.anthropic.com/candidate-ai-guidance

_Last reviewed: 2026-10_
