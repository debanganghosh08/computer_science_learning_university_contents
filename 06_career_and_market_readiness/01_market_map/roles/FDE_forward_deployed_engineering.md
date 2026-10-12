# FDE · Forward Deployed Engineering: roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [Forward Deployed Engineering major](../../../03_majors/forward_deployed_engineering/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

A forward deployed engineer (FDE) is a software engineer who works inside a customer's organisation, or very close to it, to make a product (today usually an AI product) work on the customer's real data, systems and processes.

| Level | Common titles |
|---|---|
| Entry | Forward Deployed Software Engineer (New Grad or Internship), Deployment Strategist (New Grad), Solutions Engineer, Deployment Engineer |
| Mid | Forward Deployed Engineer, Forward Deployed Software Engineer, Applied AI Engineer, Customer Engineer |
| Senior | Senior FDE, Applied AI Architect, Solutions Architect, Deployment Strategist |
| Leadership | Manager, Forward Deployed Engineering; Head of Deployment; Field CTO |

Related titles differ in emphasis: **solutions engineers** support sales with demos and proofs of concept; **FDEs** build and ship production systems for a specific customer; **deployment strategists** focus on the customer's problem and process.

## What the work looks like day to day

- Run discovery with the customer: who does the work today, what data exists, what "better" means (FDE302).
- Integrate quickly with what the customer has: REST and SOAP APIs, legacy databases, single sign-on (SAML, OIDC), file drops, data connectors (FDE303).
- Model the customer's data and business objects so an AI system can use them (FDE401).
- Deploy AI workflows inside enterprise constraints: security reviews, data residency, approvals (FDE304).
- Debug in environments you do not control: proxies, firewalls, odd identity setups (FDE402).
- Demo, write design documents, and run workshops (FDE305).
- Feed repeated patterns back to the product team so the next deployment is faster (FDE501).

## Demand signals

**No official statistics or reliable market-wide posting counts exist for this title.** What can be verified:

- **Job-board snapshot, 12 Oct 2026.** OpenAI listed 26 roles titled "Forward Deployed Engineer", split by industry (healthcare, legal, financial services) and city (San Francisco, New York, Seattle, London, Munich, Madrid), plus 66 "Applied AI" roles. Palantir listed 79 forward-deployed postings (43 distinct titles, including new-graduate and internship roles). Anthropic listed a Forward Deployed Engineer role, a forward-deployed engineering manager role and 47 "Applied AI" roles ([OpenAI careers](https://openai.com/careers), [Palantir careers](https://www.palantir.com/careers/), [Anthropic careers](https://www.anthropic.com/jobs)). A listing can repeat across locations; treat this as a snapshot, not a trend.
- **India.** The same snapshot showed India-based Applied AI Architect roles in Bengaluru and Mumbai (Anthropic) and Applied AI Engineer and Architect roles in Delhi plus a partner deployment role in Bengaluru (OpenAI) ([Anthropic careers](https://www.anthropic.com/jobs), [OpenAI careers](https://openai.com/careers)).
- **The deployment gap.** 88% of organisations use AI, but AI agent deployment is "in the single digits across nearly all business functions" ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)). Closing that gap inside each customer is this role's purpose.
- **Business model shift.** Indian tech providers are moving "away from FTE delivery to outcome-based, risk-sharing constructs" ([NASSCOM 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026)). Outcome-based contracts reward engineers who can deliver results inside client environments (**analysis**).
- **Employer intentions.** 78% of leaders were considering hiring for AI-specific roles ([Microsoft Work Trend Index 2025](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born)).

## How AI is changing the role

**Automated or mostly automated.** Integration boilerplate (API clients, data mappers), first-draft scripts and SQL, documentation, and demo scaffolding.

**Augmented.** Understanding an unfamiliar customer codebase or schema quickly; prototyping several approaches in a day; writing evaluation sets from customer examples.

**Growing in value.**

- Discovery: finding the real problem behind the request.
- Trust: customers grant access to sensitive systems to people, not tools.
- Navigating security reviews, compliance and procurement.
- Judging when an AI workflow is good enough to go live, with evidence.
- Communicating trade-offs, cost and return on investment (FDE403).

**Analysis.** AI makes it fast to build a prototype, which moves the bottleneck to everything around the code: understanding the customer, getting access, handling messy data and earning trust. This is why AI companies are hiring forward-deployed engineers at the same time as AI writes more code.

## Pay (indicative)

**No reliable public salary data exists for the FDE title.** Closest proxies:

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Software developers | Median $135,980; 90th $214,670 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm) |
| US | Computer systems analysts (bridge business needs and IT) | Median $105,850 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/computer-systems-analysts.htm) |
| India | Solutions Architect (usually more senior than entry FDE) | Average base ₹28.5 lakh; base range ₹9.9–40 lakh (664 profiles, Jul 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Solutions_Architect/Salary) |
| India | Solution Architect | Median total pay ₹46.0 lakh (373 submissions) | Self-reported, mostly product companies | [Levels.fyi](https://www.levels.fyi/t/solution-architect/locations/india) |

## The hiring loop

Typical loop (varies by company; not standardised):

1. Coding round: practical problems more than puzzles; sometimes AI-assisted.
2. Build or integration exercise: connect to an unfamiliar API or dataset and produce something working in limited time.
3. Customer scenario: an interviewer plays a customer with a vague goal. You ask questions, break the problem down and propose a plan. Interviewers score structure and communication.
4. System design under real-world constraints: legacy systems, security review, limited access.
5. Written communication: a short design note or summary for a customer.
6. Behavioural: ambiguity, travel, ownership, handling a difficult stakeholder.

See [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- Fast, careful integration engineering (APIs, auth, data).
- Data modelling across messy sources.
- Debugging in unfamiliar environments.
- Discovery interviewing and requirements writing.
- Clear demos, documents and workshops.
- Learning a new industry's vocabulary and rules quickly.
- Security and compliance awareness.

## Adjacent roles and transitions

- **AI engineering** ([AIE](AIE_ai_engineering.md)).
- **Backend and integration engineering** ([BE](BE_backend_engineering.md)).
- **Data analysis and data engineering** for data-heavy deployments ([DAN](DAN_data_analysis.md), [DEN](DEN_data_engineering.md)).
- **Solutions architecture and product management.**
- **Founder path**: FDEs see the same customer problem many times, which is a common origin of startups (FDE501, LCH502).

## Sources

All checked October 2026.

- Job boards on 12 Oct 2026 (listing counts; may repeat across locations): https://openai.com/careers ; https://www.palantir.com/careers/ ; https://www.anthropic.com/jobs
- Stanford HAI, AI Index 2026. https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- NASSCOM, Strategic Review 2026. https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026
- Microsoft, 2025 Work Trend Index (23 Apr 2025). https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born
- BLS, Occupational Outlook Handbook: Software Developers; Computer Systems Analysts (2025–35; May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm ; https://www.bls.gov/ooh/computer-and-information-technology/computer-systems-analysts.htm
- Payscale India: Solutions Architect; Levels.fyi India: Solution Architect (self-reported; 12 Oct 2026). https://www.payscale.com/research/IN/Job=Solutions_Architect/Salary ; https://www.levels.fyi/t/solution-architect/locations/india

_Last reviewed: 2026-10_
