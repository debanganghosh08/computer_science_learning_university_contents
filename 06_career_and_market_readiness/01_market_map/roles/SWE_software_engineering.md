# SWE · Software Engineering: roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [Software Engineering major](../../../03_majors/software_engineering/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

| Level | Common titles | What changes at this level |
|---|---|---|
| Intern / entry | Software Engineer I, SDE-1, Associate Software Engineer, Graduate Engineer Trainee (Indian services firms) | You deliver well-scoped tickets with review |
| Mid | Software Engineer II, SDE-2, Senior Software Engineer (services firms) | You own features end to end and go on call |
| Senior | Senior Software Engineer, SDE-3, Tech Lead | You design components and unblock others |
| Staff and above | Staff, Principal, Distinguished Engineer, Architect | You set technical direction across teams |
| Management track | Engineering Manager, Director of Engineering | You own people, delivery and hiring |

Titles are not standard across companies. An "SDE-2" at a product company and a "Senior Software Engineer" at a services company can be the same level.

## What the work looks like day to day

- Read a ticket or design note and clarify what "done" means.
- Write code with an AI assistant, then read every line it produced.
- Write and fix tests; keep the build green.
- Review teammates' pull requests, including AI-generated ones.
- Debug failures in staging or production; go on call in rotation.
- Write short design documents and discuss trade-offs.
- Refactor and modernise older code (see SWE402).

## Demand signals

- **US projections.** Software developers: 1,717,800 jobs in 2025, projected +10% (+174,700) to 2035, described as "much faster than average" ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm)).
- **US postings.** Indeed's software development postings index was 78.3 on 2 Oct 2026 (1 Feb 2020 = 100), up from 64.3 a year earlier but far below its February 2022 peak of 233.8 ([Indeed Hiring Lab data](https://github.com/hiring-lab/job_postings_tracker)).
- **Other markets.** The same index was 61.3 in the UK and 48.3 in Germany ([Indeed Hiring Lab data](https://github.com/hiring-lab/job_postings_tracker)).
- **Global employer survey.** "Software and Applications Developers" is the fourth fastest-growing job to 2030 in percentage terms ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).
- **Entry level is weak.** US software developers aged 22–25 were close to 20% below their late-2022 employment peak by Sept 2025 ([Canaries, Nov 2025](https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf)). Recent computer science graduates had 7.0% unemployment in 2024, against 4.2% for all majors, but low underemployment (19.1%) and a high early-career median wage ($87,000) ([New York Fed](https://www.newyorkfed.org/research/college-labor-market)). Hiring activity grew 22% for lead developers but 7% for entry level ([HackerRank 2025](https://www.hackerrank.com/reports/developer-skills-report-2025)).
- **India.** Direct tech employment is projected at about 6 million in FY26 (+2.3%), with FY27 hiring expected "to shift from volume to skill mix" ([NASSCOM 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026)). India had 21.9 million GitHub developers in 2025 ([Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)).

## How AI is changing the role

**What is being automated.** The most common single task people bring to Claude is "modifying software to correct errors" (6% of all usage), and 79% of conversations in the agentic tool Claude Code are automation rather than collaboration ([Anthropic, Jan 2026](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report); [Anthropic, Apr 2025](https://www.anthropic.com/research/impact-software-development)). Google says more than a quarter of its new code is AI-generated and then reviewed by engineers (claim, Oct 2024) ([Google](https://blog.google/inside-google/message-ceo/alphabet-earnings-q3-2024/)). Routine coding from a complete specification is shrinking: BLS projects computer programmers −7% because AI automates "repetitive programming tasks" ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/computer-programmers.htm)).

**What is augmented.** Debugging, refactoring and code review. 61% of AI users debug with it ([Stack Overflow 2026](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)). Measured gains vary: +26% pull requests in field experiments, but 19% slower for experts in their own large repositories in METR's 2025 trial ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf); [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)).

**What grows in value.** Verification and production ownership. Only 6.6% of developers trust AI output for important decisions ([Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data)), and AI adoption is still negatively related to delivery stability ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)).

**Analysis.** The job is moving from "write the code" to "specify, generate, verify, integrate and own the code". Directing agents is part of the job (SWE304). The engineers who gain are those who can judge AI output quickly and who understand the system well enough to know what to ask for.

## Pay (indicative)

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Software developers | Median $135,980; 10th percentile $82,460; 90th $214,670 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm) |
| US | Software developers at software publishers | Median $164,550 (May 2025) | Official survey | same |
| India | Software Engineer | Average base ₹8.1 lakh; base range ₹3.5–20 lakh; under 1 year experience ≈₹5.4 lakh total (4,950 profiles, Jul 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Software_Engineer/Salary) |
| India | Software Engineer | Median total pay ₹30.6 lakh; 25th percentile ₹17.6 lakh; 90th ₹69.9 lakh; Bengaluru median ₹38.7 lakh (21,909 submissions, Oct 2026) | Self-reported, mostly product companies | [Levels.fyi](https://www.levels.fyi/t/software-engineer/locations/india) |

These figures are indicative. The two India sources describe different employers and different pay definitions; see the [market map](../README.md#6-india).

## The hiring loop

A typical loop (it varies by company):

1. Online assessment: two or three data-structures-and-algorithms (DSA) problems, timed.
2. Recruiter or hiring-manager screen.
3. Two to three coding interviews; in India, often one low-level design (LLD) round (classes, interfaces, patterns).
4. System design for mid-level and above.
5. Behavioural interview: ownership, conflict, failure.

AI policies differ. Canva expects candidates to use AI tools in an "AI-Assisted Coding" interview and asks: "Can they identify and fix issues in AI-generated code?" ([Canva](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)). Anthropic allows no AI in live interviews unless stated ([Anthropic](https://www.anthropic.com/candidate-ai-guidance)). Prepare for both. Details: [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- Debugging unfamiliar code from logs, traces and a failing test.
- Design reasoning: interfaces, data models, failure modes, and the cost of change.
- Testing strategy and reading diffs critically.
- Concurrency and performance (SWE305).
- Operating what you build: observability, incidents, rollbacks (SWE403).
- Clear writing: design notes, pull request descriptions, postmortems.
- Domain knowledge in one industry (payments, logistics, healthcare).

## Adjacent roles and transitions

- **Backend, frontend or mobile**: specialise in one layer ([BE](BE_backend_engineering.md), [FE](FE_frontend_engineering.md), [MOB](MOB_mobile_engineering.md)).
- **AI engineering**: add retrieval, agents and evaluation ([AIE](AIE_ai_engineering.md)).
- **Forward deployed engineering**: add customer work ([FDE](FDE_forward_deployed_engineering.md)).
- **DevOps/SRE**: add operations depth ([OPS](OPS_devops_sre_platform_engineering.md)).
- **Quality engineering**: add test architecture ([QAE](QAE_software_quality_test_engineering.md)).
- **Engineering management**: after senior level, through SWE404.

## Sources

All checked October 2026.

- BLS, Occupational Outlook Handbook: Software Developers, QA Analysts and Testers; Computer Programmers (2025–35 projections, May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm ; https://www.bls.gov/ooh/computer-and-information-technology/computer-programmers.htm
- Indeed Hiring Lab, job postings tracker (data to 2 Oct 2026). https://github.com/hiring-lab/job_postings_tracker
- WEF, Future of Jobs Report 2025 (Jan 2025). https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- Brynjolfsson, Chandar, Chen, Canaries in the Coal Mine (13 Nov 2025). https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf
- Federal Reserve Bank of New York, Labor Market for Recent College Graduates (majors data released 4 Feb 2026). https://www.newyorkfed.org/research/college-labor-market
- HackerRank, 2025 Developer Skills Report. https://www.hackerrank.com/reports/developer-skills-report-2025
- NASSCOM, Strategic Review 2026. https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026
- GitHub, Octoverse 2025 (28 Oct 2025). https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- Anthropic Economic Index (28 Apr 2025; 15 Jan 2026). https://www.anthropic.com/research/impact-software-development ; https://www.anthropic.com/research/anthropic-economic-index-january-2026-report
- Google, Q3 2024 earnings remarks (29 Oct 2024). https://blog.google/inside-google/message-ceo/alphabet-earnings-q3-2024/
- Stack Overflow, 2026 Developer Survey (6 Oct 2026). https://survey.stackoverflow.co/2026/ai/data ; https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/
- Stanford HAI, AI Index 2026. https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- METR, early-2025 developer productivity trial (10 Jul 2025). https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- DORA 2025 (24 Sep 2025). https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- Payscale India and Levels.fyi India, Software Engineer (self-reported; checked 12 Oct 2026). https://www.payscale.com/research/IN/Job=Software_Engineer/Salary ; https://www.levels.fyi/t/software-engineer/locations/india
- Canva Engineering (11 Jun 2025). https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/ ; Anthropic candidate AI guidance. https://www.anthropic.com/candidate-ai-guidance

_Last reviewed: 2026-10_
