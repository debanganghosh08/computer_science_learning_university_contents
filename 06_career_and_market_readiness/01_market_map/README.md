# The CS and IT job market map (late 2026)

| Covers | Markets | Figures checked | Read next |
|---|---|---|---|
| 20 role families, one page each | India and global (most hard data is from the US, UK and Germany) | October 2026 | [AI impact matrix](ai_impact_matrix.md) · [Role pages](#11-role-pages) · [AI-driven interviews](../04_ai_driven_interviews/) |

This page describes the computer science and IT job market as of October 2026. It covers what AI coding assistants and agents changed, where hiring is weak, where it is growing, what employers now screen for, and which skills keep their value. Every number links to its source, and every source was checked in October 2026. When sources disagree, both are shown. Paragraphs marked **Analysis** are interpretation, not measurement.

Two words used throughout:

- **Automation**: the AI does the task and a human accepts or rejects the result.
- **Augmentation**: a human does the task faster or better with AI help, and stays in the loop.

## 1. The short version

1. **AI coding tools are now standard equipment.** In the 2026 Stack Overflow survey, 65.9% of respondents use AI coding assistants or coding agents at work, and 73% of those use them daily ([Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data)). Google's DORA research found 90% of technology professionals use AI at work ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)).
2. **Trust is conditional.** 48.0% trust AI output only when they can easily verify it, and 6.6% trust it for important decisions ([Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data)).
3. **Capability is rising fast, reliability less so.** On METR's software tasks, Claude Opus 4.6 (February 2026) succeeds half the time on tasks that take a human expert about 12 hours, but at 80% reliability its horizon is about 70 minutes ([METR data file](https://metr.org/assets/benchmark_results_1_1.yaml)).
4. **Entry level is where the pressure is.** By September 2025, US employment of software developers aged 22–25 was close to 20% below its late-2022 peak, while older developers kept growing ([Brynjolfsson, Chandar and Chen, Nov 2025](https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf)). Recent US computer science graduates had 7.0% unemployment in 2024, against 4.2% for all majors ([New York Fed](https://www.newyorkfed.org/research/college-labor-market)).
5. **The wider labour market is not (yet) broadly disrupted.** The Yale Budget Lab found no "discernible disruption" in the US occupational mix since ChatGPT's release ([Yale Budget Lab, Oct 2025](https://budgetlab.yale.edu/research/evaluating-impact-ai-labor-market-current-state-affairs)). US software development job postings are recovering: 78.3 on 2 October 2026 (1 February 2020 = 100), up from 64.3 a year earlier ([Indeed Hiring Lab data](https://github.com/hiring-lab/job_postings_tracker)).
6. **Growth is concentrated.** AI and machine learning, data, security, and roles that put AI into production are growing. The US Bureau of Labor Statistics (BLS) projects data scientists +35%, information security analysts +21% and computer and information research scientists +22% for 2025–35, against −7% for computer programmers ([BLS OOH](https://www.bls.gov/ooh/computer-and-information-technology/home.htm)).
7. **India is shifting from headcount to skill mix.** Direct tech-sector employment is projected at about 6 million in FY26 (+2.3%, net +135,000). NASSCOM expects FY27 hiring "to shift from volume to skill mix" as AI productivity gains are passed to clients ([NASSCOM Strategic Review 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026)).

## 2. What changed with AI coding assistants and agents

### 2.1 Adoption

| Measure | Figure | Source |
|---|---|---|
| Use AI coding assistants or coding agents at work | 65.9% (n = 17,464) | [Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data) |
| Use AI agents or automated workflows at work | 26.2% | same |
| Do not use AI tools at work | 17.2% | same |
| Most-used coding agents among agent users | Claude Code 65.5%, GitHub Copilot 58.7% | same |
| Using or planning to use AI tools (previous year) | 84% (2025) | [Stack Overflow 2025](https://survey.stackoverflow.co/2025/ai) |
| Technology professionals using AI at work | 90% (≈5,000 respondents) | [DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) |
| New GitHub developers using Copilot in their first week | 80% | [GitHub Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) |
| Surveyed organisations using AI | 88% in 2025; generative AI in at least one business function at 70%; AI agent deployment "in the single digits across nearly all business functions" | [Stanford AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) |

What developers use AI for matters more than whether they use it. In 2026, 67% of AI users generate code in familiar areas and 61% debug with it, but only 20% use it for "deploying, operating, or troubleshooting production systems" ([Stack Overflow blog, 6 Oct 2026](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)).

### 2.2 What the tools can do, and how reliably

[METR](https://metr.org/time-horizons/) measures a model's **time horizon**: the length of task (measured by how long a human expert takes) that an AI agent completes with a given success rate. The tasks are mostly software engineering, machine learning and cybersecurity tasks with automatic scoring.

| Model (release) | 50% time horizon | 80% time horizon |
|---|---|---|
| GPT-4 (Mar 2023) | ≈4 minutes | <1 minute |
| Claude 3.7 Sonnet (Feb 2025) | ≈60 minutes | ≈12 minutes |
| o3 (Apr 2025) | ≈2.0 hours | ≈30 minutes |
| GPT-5 (Aug 2025) | ≈3.4 hours | ≈38 minutes |
| GPT-5.2 (Dec 2025) | ≈5.9 hours | ≈66 minutes |
| Claude Opus 4.6 (Feb 2026) | ≈12 hours (95% interval ≈5–61 hours) | ≈70 minutes |

Source: METR-Horizon-v1.1 data file ([metr.org/assets/benchmark_results_1_1.yaml](https://metr.org/assets/benchmark_results_1_1.yaml)), checked October 2026. Earlier METR publications used an older task suite and report different values for the same models (for example, about 50 minutes for Claude 3.7 Sonnet in the [original paper](https://arxiv.org/abs/2503.14499)).

How to read it:

- **The trend is steep.** The original paper estimated the 50% horizon doubling about every seven months since 2019 ([arXiv 2503.14499](https://arxiv.org/abs/2503.14499)). The current data file estimates about 129 days (roughly four months) for models since 2023.
- **Reliability lags capability.** The 80% horizon is roughly four to ten times shorter than the 50% horizon. A tool that fails half the time on long tasks still needs a person who can tell success from failure.
- **METR's own limits.** METR says "measurements above 16 hrs are unreliable" with its current tasks, and that the results do not imply AI can automate most jobs, because real work is messier and often cannot be scored automatically ([METR](https://metr.org/time-horizons/)). An early preview model measured in spring 2026 (Claude Mythos Preview) scored about 17 hours at 50%, already past the reliable range, which is why this page quotes the February 2026 figure.
- **Benchmarks tell a similar story.** On SWE-bench Verified (fixing real GitHub issues), the top models were clustered in the low-to-mid 70s as of February 2026, led by about 76.8% under a standard agent setup ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)).
- **Real usage is less reliable than benchmarks.** Anthropic estimated that about 61% of software-development requests to Claude succeed, and that adjusting for task success "roughly halves" the implied productivity gains ([Anthropic Economic Index, Jan 2026](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)).

### 2.3 Productivity: what controlled studies found

| Study | Who and what | Result |
|---|---|---|
| Field experiments summarised in the [AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) (Cui et al., 2025) | Developers using GitHub Copilot in field experiments | 26% more pull requests completed; across studies, less experienced workers tended to gain most |
| [METR randomised trial](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) (data Feb–Jun 2025) | 16 experienced open-source developers, 246 tasks in their own repositories | Tasks took 19% longer with AI. Developers expected a 24% speed-up and afterwards believed they had been 20% faster |
| [METR update](https://metr.org/blog/2026-02-24-uplift-update/) (Feb 2026, data from Aug 2025) | 57 developers, 800+ tasks, agentic tools | Point estimates of 18% and 4% less time, with confidence intervals that include a slowdown. METR calls this an "unreliable signal": 30–50% of developers withheld tasks they did not want to do without AI. METR believes developers are "more sped up" in early 2026 than in early 2025 |
| [DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) | ≈5,000 technology professionals (survey) | AI adoption is positively related to delivery throughput but still negatively related to delivery stability. "AI doesn't fix a team; it amplifies what's already there" |
| Learning study cited in the [AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) (Shen and Tamkin, 2025) | Software engineers learning with heavy AI reliance | No measurable speed gain and "learning penalties" |

**Analysis.** The gains are real for well-defined tasks, for less experienced people, and for teams that already test, review and deploy well. They are smaller, or negative, for experts working in large codebases they know deeply, and stability suffers when review and testing do not keep up. This is why this curriculum keeps "drills without AI" and "verify AI output" in every course.

### 2.4 What companies say (claims, not measurements)

| Company | Statement | Source |
|---|---|---|
| Google | "more than a quarter of all new code at Google is generated by AI, then reviewed and accepted by engineers" (29 Oct 2024) | [Google blog](https://blog.google/inside-google/message-ceo/alphabet-earnings-q3-2024/) |
| Microsoft | "I'd say maybe 20%, 30% of the code that is inside of our repos today and some of our projects are probably all written by software" (Satya Nadella, 29 Apr 2025) | [CNBC](https://www.cnbc.com/2025/04/29/satya-nadella-says-as-much-as-30percent-of-microsoft-code-is-written-by-ai.html) |
| Salesforce | On customer support headcount: "I've reduced it from 9,000 heads to about 5,000, because I need less heads" (Marc Benioff, reported 2 Sept 2025) | [CNBC](https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html) |
| Amazon | AI "will reduce our total corporate workforce" over the next few years (Andy Jassy memo, 17 Jun 2025). About 14,000 corporate roles cut on 28 Oct 2025, framed around fewer layers and faster AI-era execution, while hiring continues "in key strategic areas" | [Jassy memo](https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-on-generative-ai) · [Amazon, Oct 2025](https://www.aboutamazon.com/news/company-news/amazon-workforce-reduction) |
| Shopify | Employees must show why AI cannot do a job before asking for more headcount (April 2025 memo, as reported) | [CNBC](https://www.cnbc.com/2025/04/29/satya-nadella-says-as-much-as-30percent-of-microsoft-code-is-written-by-ai.html) |

Read these carefully. "Share of code written by AI" has no standard definition (accepted autocomplete characters, lines, or merged pull requests), the figures are not audited, and executives speak to investors. They show direction and intent, not measured productivity.

## 3. Entry-level hiring: what the data shows

| Evidence | What it says | Source |
|---|---|---|
| US payroll data (ADP), millions of workers | Ages 22–25 in the most AI-exposed jobs: 16% relative employment decline after controlling for firm-level shocks. Software developers aged 22–25: close to 20% below the late-2022 peak by Sept 2025. Older workers stable or growing. Declines are concentrated where AI **automates** tasks, not where it **augments** them. Employment adjusted, not wages | [Canaries in the Coal Mine, Nov 2025](https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf) |
| US recent graduates by major (2024 data, released Feb 2026) | Computer engineering 7.8% and computer science 7.0% unemployment, against 4.2% for all majors. But underemployment is low (15.8% and 19.1% against 39.4%) and early-career median wages are high ($90,000 and $87,000 against $58,000) | [New York Fed](https://www.newyorkfed.org/research/college-labor-market) ([data](https://www.newyorkfed.org/medialibrary/research/interactives/data/college-labor-market/college-labor-outcomes-by-major-data.csv)) |
| Hiring activity on a large assessment platform | Year-on-year hiring: lead developers +22%, senior +19%, junior +9%, entry-level +7% ("nearly flat") | [HackerRank 2025](https://www.hackerrank.com/reports/developer-skills-report-2025) |
| Security teams | 31% of security teams had no entry-level professionals (2024) | [ISC2 2024](https://www.isc2.org/Insights/2024/09/Employers-Must-Act-Cybersecurity-Workforce-Growth-Stalls-as-Skills-Gaps-Widen) |
| Students reacting | US undergraduate enrolment in computer science as a major fell 11% from 2024 to 2025 | [AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) |
| Counter-evidence | Overall US occupational mix shows no "discernible disruption" since ChatGPT; the faster change in occupational mix predates generative AI | [Yale Budget Lab, Oct 2025](https://budgetlab.yale.edu/research/evaluating-impact-ai-labor-market-current-state-affairs) |
| Timing | US software development postings peaked at 233.8 in Feb 2022, nine months **before** ChatGPT launched, fell to 61.1 in May 2025, and stood at 78.3 on 2 Oct 2026 | [Indeed Hiring Lab data](https://github.com/hiring-lab/job_postings_tracker) |

**Analysis.** The junior squeeze has more than one cause. Postings started falling before generative AI, so the post-2021 hiring boom and its correction explain part of it. The payroll study controls for firm-level shocks and still finds a drop for young workers in AI-exposed occupations, so AI is a measured contributor, not just a headline. The authors' explanation is useful for learners: AI substitutes most for **codified** knowledge (the "book-learning" a graduate brings) and least for **tacit** knowledge (judgement built by doing real work). The practical response is to acquire tacit knowledge earlier: internships, open-source maintenance, operating something real, and reviewing other people's code.

## 4. Which tasks are being automated, and which are augmented

What usage data shows:

- Software development is the largest single use of Claude. Computer and mathematical tasks were 34% of Claude.ai conversations in November 2025 and nearly half of API traffic. The single most common task, "modifying software to correct errors", was 6% of all usage ([Anthropic, Jan 2026](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)).
- In Claude Code, an agentic coding tool, 79% of conversations were automation, against 49% on the Claude.ai chat interface. JavaScript/TypeScript (31%) and HTML/CSS (28%) dominated, and Anthropic noted that "jobs that center on making simple applications and user interfaces may face disruption from AI systems sooner" ([Anthropic, Apr 2025](https://www.anthropic.com/research/impact-software-development)).
- Business (API) use is mostly automation: 77% in August 2025 ([Anthropic, Sept 2025](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report)).

What official projections say (US, 2025–35, [BLS OOH](https://www.bls.gov/ooh/computer-and-information-technology/home.htm)):

- Computer programmers: −7%, mainly because companies use technologies, including AI, "to automate repetitive programming tasks".
- Network and computer systems administrators: −4%, as tasks shift to DevOps-focused developers and network-as-a-service providers, and routine work is automated.
- Computer support specialists: −3%.
- Web developers: "increasing use of artificial intelligence (AI) for web development may soften the employment growth".
- Database administrators: fewer needed "as many companies operate in the cloud", while database architects grow as firms adopt AI to process data.

| Mostly automated now | AI augments (human decides) | Still human-led |
|---|---|---|
| Boilerplate and CRUD code, simple UI components, unit-test scaffolding, syntax and API lookup, first-draft SQL, routine config and scripts, ticket summaries, first-pass log reading | Debugging, refactoring, code review, test design, data exploration, alert triage, documentation, migration of legacy code | Deciding what to build, system design and trade-offs, production ownership and incident command, security and risk sign-off, customer and stakeholder work, evaluating whether AI output is correct |

The table is **analysis** built from the sources in this section and the [AI impact matrix](ai_impact_matrix.md), which breaks it down for all 20 role families.

## 5. Which roles are growing

**Employer expectations (global).** The World Economic Forum's survey of over 1,000 employers lists the fastest-growing jobs to 2030 (by percentage). The technology ones are Big Data Specialists, FinTech Engineers, AI and Machine Learning Specialists, Software and Applications Developers, Security Management Specialists, Data Warehousing Specialists, UI and UX Designers, Internet of Things Specialists, Data Analysts and Scientists, Information Security Analysts and DevOps Engineers ([WEF Future of Jobs 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)). The same survey expects 170 million jobs created and 92 million displaced worldwide by 2030 (net +78 million), and 39% of workers' core skills to change.

**Official US projections, 2025–35** ([BLS OOH](https://www.bls.gov/ooh/computer-and-information-technology/home.htm), pages updated 27 Aug 2026; median pay for May 2025):

| Occupation | Jobs (2025) | Projected change | Median pay |
|---|---|---|---|
| [Data scientists](https://www.bls.gov/ooh/math/data-scientists.htm) | 275,600 | +35% | $120,230 |
| [Computer and information research scientists](https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm) | 38,600 | +22% | $140,300 |
| [Information security analysts](https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm) | 192,900 | +21% | $129,180 |
| [Operations research analysts](https://www.bls.gov/ooh/math/operations-research-analysts.htm) | 113,100 | +12% | $88,940 |
| [Software developers](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm) | 1,717,800 | +10% | $135,980 |
| [Computer hardware engineers](https://www.bls.gov/ooh/architecture-and-engineering/computer-hardware-engineers.htm) | 76,100 | +9% | $161,740 |
| [Computer network architects](https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm) | 181,800 | +8% | $134,050 |
| [Computer systems analysts](https://www.bls.gov/ooh/computer-and-information-technology/computer-systems-analysts.htm) | 544,400 | +8% | $105,850 |
| [Software QA analysts and testers](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm) | 187,600 | +6% | $104,300 |
| [Web developers and digital designers](https://www.bls.gov/ooh/computer-and-information-technology/web-developers.htm) | 220,100 | +5% | $99,520 |
| [Database administrators and architects](https://www.bls.gov/ooh/computer-and-information-technology/database-administrators.htm) | 144,500 | +4% | $126,760 |
| [Computer support specialists](https://www.bls.gov/ooh/computer-and-information-technology/computer-support-specialists.htm) | 903,100 | −3% | $62,890 |
| [Network and computer systems administrators](https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm) | 323,600 | −4% | $99,130 |
| [Computer programmers](https://www.bls.gov/ooh/computer-and-information-technology/computer-programmers.htm) | 110,800 | −7% | $100,390 |

**What job postings ask for.** In the US, 2.6% of all job postings required AI skills in 2025 (Singapore led with 4.69%). Mentions of generative AI skills in US AI postings grew 111% from 2024 to 2025, and postings mentioning AI agents and agentic systems rose sharply while the share mentioning ChatGPT, chatbots or conversational AI declined. The fastest-growing skills in AI postings were about running systems at scale: AWS (+1,358% against a decade earlier), scalability (+733%) and workflow management (+818%) ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)).

**New role types.** 78% of leaders surveyed by Microsoft were considering AI-specific roles; among managers, 35% were considering hiring AI trainers and 32% AI agent specialists ([Work Trend Index 2025](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born)). Forward-deployed engineering, where engineers build and deploy AI inside customer organisations, is visible on major AI companies' job boards. On 12 October 2026, OpenAI listed 26 roles with "Forward Deployed Engineer" in the title and 66 "Applied AI" roles, Anthropic listed 47 "Applied AI" roles (including India-based Applied AI Architect roles in Bengaluru and Mumbai), and Palantir listed 79 forward-deployed postings ([OpenAI careers](https://openai.com/careers), [Anthropic careers](https://www.anthropic.com/jobs), [Palantir careers](https://www.palantir.com/careers/)). This is a one-day snapshot of three employers, not a market-wide trend.

**Security.** AI was the most-cited skills need (41%), followed by cloud security (36%), in the 2025 ISC2 study of 16,029 professionals. But 24% of respondents reported layoffs and 39% hiring freezes, and ISC2 stopped estimating a "workforce gap" that year ([ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study)). The demand is for specific skills, not for any security certificate holder.

**Hardware and the physical world.** Connected IoT devices are expected to grow from 18.5 billion (2024) to 39 billion in 2030 ([IoT Analytics](https://iot-analytics.com/number-connected-iot-devices/)). US electrical engineering postings stood at 152.0 on Indeed's index in October 2026, well above their February 2020 level, while software development was at 78.3 ([Indeed Hiring Lab data](https://github.com/hiring-lab/job_postings_tracker)).

**Other markets.** Postings are weaker outside the US. On 2 October 2026, Indeed's software development index was 61.3 in the UK and 48.3 in Germany (Germany's lowest since at least 2023) ([Indeed Hiring Lab data](https://github.com/hiring-lab/job_postings_tracker)).

## 6. India

| Measure | Figure | Source |
|---|---|---|
| Tech industry revenue | $283 bn in FY25 (+5.1%); expected to cross $315 bn in FY26 | [NASSCOM 2025](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2025), [NASSCOM 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026) |
| Tech workforce | 5.80 million in FY25 (net +126,000); ~6 million projected for FY26 (+2.3%, net +135,000) | same |
| Direction of hiring | Providers moving "away from FTE delivery to outcome-based, risk-sharing constructs". FY27: hiring "to shift from volume to skill mix" | [NASSCOM 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026) |
| Developers on GitHub | 21.9 million (2025), +5.2 million in the year; projected 57.5 million by 2030, "poised to overtake the US" | [Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) |
| Fastest-growing roles expected by employers in India | Big Data Specialists, AI and ML Specialists, Security Management Specialists | [WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf) |
| Skills-based hiring | 30% of employers in India plan to remove degree requirements (19% globally); 35% expect semiconductors and computing technologies to transform their operations | same |
| AI talent | AI talent concentration among LinkedIn members 1.01% in 2025, up 120% since 2019. India also had the largest net outflow of AI research authors and inventors of any country in 2025 | [AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) |
| How Indians use AI | 7.2% of global Claude.ai use; "coding tasks are over half of all usage in India versus roughly a third of all usage globally" | [Anthropic, Sept 2025](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) |
| Security workforce | Top skills needs: AI 52%, cloud security 43%, application security 38%. "Skills shortages have overtaken staffing shortages" | [ISC2 India, Sept 2026](https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai) |

**Pay depends on which source you read.** For "software engineer" in India, Levels.fyi shows a median total compensation of ₹30.6 lakh (21,909 self-reported salaries, mostly product companies and multinationals) ([Levels.fyi](https://www.levels.fyi/t/software-engineer/locations/india)). Payscale shows an average base salary of ₹8.1 lakh (4,950 profiles across the whole market) ([Payscale](https://www.payscale.com/research/IN/Job=Software_Engineer/Salary)). Both are honest; they measure different populations (product firms against everyone) and different pay (total compensation against base). The role pages show both where available.

**Analysis.** The traditional Indian services model is priced by headcount (full-time equivalents). When AI makes each engineer more productive and clients capture the gain, as NASSCOM describes, firms need fewer people for the same contract, and the people they keep must cover more of the work: design, integration, testing, domain knowledge and client communication. Global capability centres (GCCs) and product companies are where depth pays most, which matches the large gap between the two salary sources above.

## 7. What hiring managers now screen for

Evidence:

- **Some employers require AI in interviews.** Canva "now expect[s] Backend, Machine Learning and Frontend engineering candidates to use AI tools" and replaced its computer science fundamentals screen with an AI-assisted coding interview. It evaluates how candidates break down ambiguous problems, when they use AI, and "Can they identify and fix issues in AI-generated code?" ([Canva, Jun 2025](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)).
- **Others forbid it.** Anthropic's candidate guidance says take-home assessments are done without AI unless stated, and live interviews are "all you–no AI assistance unless we indicate otherwise" ([Anthropic](https://www.anthropic.com/candidate-ai-guidance)).
- **Assessment integrity is a live problem.** 76% of developers say AI makes gaming assessments easier, and tech leaders rank assessment relevance as their top concern ([HackerRank 2025](https://www.hackerrank.com/reports/developer-skills-report-2025)).
- **Skills employers rank highest.** Analytical thinking is the most sought-after core skill. AI and big data, networks and cybersecurity, and technological literacy are the fastest-growing, alongside creative thinking, resilience and curiosity ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).
- **Managing agents is becoming a job skill.** Microsoft describes the "agent boss": "someone who builds, delegates to, and manages agents to amplify their impact" ([Work Trend Index 2025](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born)).

**Analysis: what a strong candidate shows in 2026.**

1. **Fundamentals without AI.** You can write, read and debug code, SQL and shell by hand under time pressure. Many loops still test this.
2. **Verification.** You can tell whether AI output is right: you write tests, read diffs critically and know the failure modes.
3. **Decomposition.** You turn an ambiguous request into a plan, a design and checkable steps.
4. **System thinking.** You discuss trade-offs: consistency, latency, cost, security, failure modes.
5. **Production ownership.** You have run something real and handled something breaking.
6. **Communication.** You write a clear design note and explain a decision to a non-specialist.
7. **Evidence.** You show shipped work with measurable results, not a list of courses.

The [AI-driven interviews section](../04_ai_driven_interviews/) covers each loop in detail, with simulations.

## 8. Skills that compound and skills being commoditised

This table is **analysis**. The evidence column shows what each judgement is based on.

| Skills that compound (grow in value) | Why | Evidence |
|---|---|---|
| Debugging and reading unfamiliar code | AI produces more code than people write; someone must understand it when it breaks | 66% frustrated by "almost right" AI output ([SO 2025](https://survey.stackoverflow.co/2025/ai)); METR 80% horizons |
| System design and failure analysis | Hardest to score automatically, so least automated | METR caveats; Canva interview criteria |
| Operating production systems | Only 20% of AI users use it in production operations; AI adoption still hurts stability | [SO 2026 blog](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/); [DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) |
| Security thinking and AI security | AI is the top security skills need globally and in India | [ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study) |
| Evaluating AI systems (evals, testing non-deterministic output) | Task success is ~61% for software requests; someone must measure it | [Anthropic, Jan 2026](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report) |
| Data modelling and data infrastructure | AI needs clean, governed data; database architects grow while administrators shrink | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/database-administrators.htm) |
| Domain knowledge and customer work | Tacit knowledge is what AI substitutes least | [Canaries](https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf) |
| Maths and statistics for ML | Needed to judge models, not just call them | BLS data scientists +35% |

| Skills being commoditised | Why | Evidence |
|---|---|---|
| Boilerplate, CRUD endpoints, simple UI components | Most-automated coding work | [Anthropic, Apr 2025](https://www.anthropic.com/research/impact-software-development) |
| Routine programming from a full specification | Projected decline | BLS computer programmers −7% |
| Syntax and API recall | Assistants answer instantly | 69.3% use AI to generate code in familiar areas ([SO 2026](https://survey.stackoverflow.co/2026/ai/data)) |
| Routine system administration and first-line support | Automation and managed services | BLS −4% and −3% |
| Simple, well-specified tasks of under an hour | Inside the 80% reliability horizon of current models | [METR data](https://metr.org/assets/benchmark_results_1_1.yaml) |

Commoditised does not mean worthless. You still need these skills to check AI output and to pass interviews; they just no longer set you apart.

## 9. How to read this market without panic

1. **Separate the cycle from the trend.** US software postings peaked in February 2022 and fell before ChatGPT existed. Part of the drop was a correction after a hiring boom. Ask what part of a change is cyclical before blaming AI.
2. **Separate claims from measurements.** CEO statements about "share of code" are not audited. Randomised trials and payroll data are slower but more reliable. When they disagree, trust the measurement and note the claim.
3. **Check who is counted.** A salary median from big-tech employees and one from the whole market can differ by four times. A survey of AI enthusiasts overstates adoption. Read the sample before the number.
4. **Look at levels, not only changes.** The BLS still projects about 174,700 more US software developer jobs from 2025 to 2035, on a base of about 1.7 million. A slower-growing field can still hire many people.
5. **Watch reliability, not just capability.** A 12-hour 50% horizon and a 70-minute 80% horizon describe the same model. Employers pay people for the gap.
6. **Treat the junior squeeze as information.** It shows which rung of the ladder AI removes first: codified, checkable tasks. Climb past it by building judgement early through internships, open source, production work and code review.
7. **Remember supply responds too.** US computer science enrolment fell 11% from 2024 to 2025 ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)). Fewer graduates in four years may ease competition (**analysis**, low confidence).
8. **Re-check twice a year.** Sources refresh on known schedules: Indeed postings daily; New York Fed graduate data quarterly (February, May, August, November); BLS OOH yearly (late summer); Stack Overflow survey yearly; NASSCOM Strategic Review every February; Stanford AI Index each spring; WEF Future of Jobs every two to three years.

## 10. Where sources disagree

| Question | One view | Other view | Why they differ |
|---|---|---|---|
| Is AI hurting entry-level jobs? | Yes, in exposed occupations: −16% relative for ages 22–25 ([Canaries](https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf)) | No broad disruption in the occupational mix ([Yale](https://budgetlab.yale.edu/research/evaluating-impact-ai-labor-market-current-state-affairs)) | Narrow slice (young, exposed) against the whole economy; different data (payroll against household survey) |
| Do AI tools make developers faster? | +26% pull requests ([AI Index summary of Cui et al.](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)) | 19% slower for experts in familiar repositories ([METR 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)) | Experience level, codebase familiarity, task type and tool generation; METR's 2026 update leans towards speed-up but is weak evidence |
| Is AI use mostly automation? | Automation exceeded augmentation for the first time in Aug 2025 data ([Anthropic, Sept 2025](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report)) | Augmentation back to 52% against 45% automation in Nov 2025 data ([Anthropic, Jan 2026](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)) | Shifting mix of users and products; API (business) use stays about three-quarters automation |
| How good are models at real coding? | Highlights say SWE-bench Verified rose "to near 100% of meeting the human baseline" | The same report shows top scores around 76.8% in Feb 2026 ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)) | Relative-to-baseline wording against raw score; quote the raw score |
| When did junior developer employment fall? | AI Index highlights: "fallen nearly 20% from 2024" | AI Index body and the source paper: close to 20% below the late-2022 peak by Sept 2025 | Use the source paper's wording |
| Are data jobs growing? | BLS projects data scientists +35% (2025–35) | US Data and Analytics postings at 63.1, below the Feb 2020 level ([Indeed](https://github.com/hiring-lab/job_postings_tracker)) | Ten-year projection against current postings; the job title "data scientist" is narrower than the posting category |
| Is there a security talent shortage? | 59% report critical or significant skills needs | 24% saw layoffs and 39% hiring freezes; ISC2 stopped estimating the gap ([ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study)) | Shortage of specific skills (AI, cloud security) alongside tight budgets |
| What does an Indian software engineer earn? | ₹30.6 lakh median total pay ([Levels.fyi](https://www.levels.fyi/t/software-engineer/locations/india)) | ₹8.1 lakh average base ([Payscale](https://www.payscale.com/research/IN/Job=Software_Engineer/Salary)) | Different employers and pay definitions |

## 11. Role pages

| Code | Role family | Market page | Learning path |
|---|---|---|---|
| CSG | Computer Science (Theory, Systems and Research) | [CSG](roles/CSG_computer_science_general.md) | [path](../../03_majors/computer_science_general/README.md) |
| SWE | Software Engineering | [SWE](roles/SWE_software_engineering.md) | [path](../../03_majors/software_engineering/README.md) |
| BE | Backend Engineering | [BE](roles/BE_backend_engineering.md) | [path](../../03_majors/backend_engineering/README.md) |
| FE | Frontend Engineering | [FE](roles/FE_frontend_engineering.md) | [path](../../03_majors/frontend_engineering/README.md) |
| MOB | Mobile Engineering | [MOB](roles/MOB_mobile_engineering.md) | [path](../../03_majors/mobile_engineering/README.md) |
| CLD | Cloud Engineering | [CLD](roles/CLD_cloud_engineering.md) | [path](../../03_majors/cloud_engineering/README.md) |
| OPS | DevOps, SRE and Platform Engineering | [OPS](roles/OPS_devops_sre_platform_engineering.md) | [path](../../03_majors/devops_sre_platform_engineering/README.md) |
| SEC | Cybersecurity: Defense, Operations and Governance | [SEC](roles/SEC_cybersecurity_defense.md) | [path](../../03_majors/cybersecurity_defense/README.md) |
| OFF | Ethical Hacking and Offensive Security | [OFF](roles/OFF_ethical_hacking_offensive_security.md) | [path](../../03_majors/ethical_hacking_offensive_security/README.md) |
| SAR | Security Architecture | [SAR](roles/SAR_security_architecture.md) | [path](../../03_majors/security_architecture/README.md) |
| DAN | Data Analysis and Analytics | [DAN](roles/DAN_data_analysis.md) | [path](../../03_majors/data_analysis/README.md) |
| DSC | Data Science | [DSC](roles/DSC_data_science.md) | [path](../../03_majors/data_science/README.md) |
| DEN | Data Engineering | [DEN](roles/DEN_data_engineering.md) | [path](../../03_majors/data_engineering/README.md) |
| MLE | Machine Learning Engineering | [MLE](roles/MLE_machine_learning_engineering.md) | [path](../../03_majors/machine_learning_engineering/README.md) |
| DLR | Deep Learning | [DLR](roles/DLR_deep_learning.md) | [path](../../03_majors/deep_learning/README.md) |
| AIE | AI Engineering: LLM Applications and Agents | [AIE](roles/AIE_ai_engineering.md) | [path](../../03_majors/ai_engineering/README.md) |
| FDE | Forward Deployed Engineering | [FDE](roles/FDE_forward_deployed_engineering.md) | [path](../../03_majors/forward_deployed_engineering/README.md) |
| EMB | Embedded Systems and IoT | [EMB](roles/EMB_embedded_systems_iot.md) | [path](../../03_majors/embedded_systems_iot/README.md) |
| QAE | Software Quality and Test Engineering | [QAE](roles/QAE_software_quality_test_engineering.md) | [path](../../03_majors/software_quality_test_engineering/README.md) |
| NET | IT Infrastructure and Network Engineering | [NET](roles/NET_it_infrastructure_networking.md) | [path](../../03_majors/it_infrastructure_networking/README.md) |

## Sources

All checked October 2026.

1. Stack Overflow. *2026 Developer Survey: AI* (results published 6 Oct 2026). https://survey.stackoverflow.co/2026/ai/data and blog https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/
2. Stack Overflow. *2025 Developer Survey: AI*. https://survey.stackoverflow.co/2025/ai
3. Google Cloud / DORA. *Announcing the 2025 DORA report* (24 Sep 2025). https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
4. GitHub. *Octoverse 2025* (28 Oct 2025, updated 28 Feb 2026). https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
5. Stanford HAI. *AI Index Report 2026*. https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
6. METR. *Time horizons* (page updated 8 Sep 2026) https://metr.org/time-horizons/ ; data file https://metr.org/assets/benchmark_results_1_1.yaml ; Kwa et al., *Measuring AI Ability to Complete Long Tasks* (Mar 2025, v4 Jul 2026) https://arxiv.org/abs/2503.14499
7. METR. *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* (10 Jul 2025). https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ; update (24 Feb 2026) https://metr.org/blog/2026-02-24-uplift-update/
8. Anthropic. *Economic Index* reports: software development (28 Apr 2025) https://www.anthropic.com/research/impact-software-development ; September 2025 report https://www.anthropic.com/research/anthropic-economic-index-september-2025-report ; January 2026 report https://www.anthropic.com/research/anthropic-economic-index-january-2026-report
9. Brynjolfsson, Chandar, Chen. *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence* (version 13 Nov 2025). https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf
10. Yale Budget Lab. *Evaluating the Impact of AI on the Labor Market: Current State of Affairs* (1 Oct 2025). https://budgetlab.yale.edu/research/evaluating-impact-ai-labor-market-current-state-affairs
11. Federal Reserve Bank of New York. *The Labor Market for Recent College Graduates* (quarterly update 6 Aug 2026; outcomes by major released 4 Feb 2026, 2024 data). https://www.newyorkfed.org/research/college-labor-market
12. Indeed Hiring Lab. *Job postings tracker* data (through 2 Oct 2026). https://github.com/hiring-lab/job_postings_tracker
13. US Bureau of Labor Statistics. *Occupational Outlook Handbook* (2025–35 projections, May 2025 pay; pages modified 27 Aug 2026). https://www.bls.gov/ooh/computer-and-information-technology/home.htm
14. World Economic Forum. *Future of Jobs Report 2025* (Jan 2025). https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
15. Microsoft. *2025 Work Trend Index: The Year the Frontier Firm Is Born* (23 Apr 2025). https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born
16. NASSCOM. *Technology Sector in India: Strategic Review 2025* and *2026* (key findings pages). https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2025 ; https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026
17. ISC2. *2024 Cybersecurity Workforce Study* (11 Sep 2024) https://www.isc2.org/Insights/2024/09/Employers-Must-Act-Cybersecurity-Workforce-Growth-Stalls-as-Skills-Gaps-Widen ; *2025 Cybersecurity Workforce Study* (4 Dec 2025) https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study ; *India's Cybersecurity Workforce* (24 Sep 2026) https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai
18. HackerRank. *2025 Developer Skills Report*. https://www.hackerrank.com/reports/developer-skills-report-2025
19. Canva Engineering. *Yes, you can use AI in our interviews* (11 Jun 2025). https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/
20. Anthropic. *Guidance on candidates' AI usage*. https://www.anthropic.com/candidate-ai-guidance
21. Company statements: Google (29 Oct 2024) https://blog.google/inside-google/message-ceo/alphabet-earnings-q3-2024/ ; CNBC on Microsoft (29 Apr 2025) https://www.cnbc.com/2025/04/29/satya-nadella-says-as-much-as-30percent-of-microsoft-code-is-written-by-ai.html ; CNBC on Salesforce (2 Sep 2025) https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html ; Amazon (17 Jun 2025) https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-on-generative-ai and (28 Oct 2025) https://www.aboutamazon.com/news/company-news/amazon-workforce-reduction
22. IoT Analytics. *Number of connected IoT devices* (28 Oct 2025). https://iot-analytics.com/number-connected-iot-devices/
23. Job boards on 12 Oct 2026 (counts of listings, which may repeat across locations): OpenAI https://openai.com/careers ; Anthropic https://www.anthropic.com/jobs ; Palantir https://www.palantir.com/careers/
24. Salary aggregators (self-reported; checked 12 Oct 2026): Levels.fyi https://www.levels.fyi/t/software-engineer/locations/india ; Payscale https://www.payscale.com/research/IN/Job=Software_Engineer/Salary

_Last reviewed: 2026-10_
