# DAN · Data Analysis and Analytics: roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [Data Analysis major](../../../03_majors/data_analysis/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

| Level | Common titles |
|---|---|
| Entry | Data Analyst, Junior Business Analyst, MIS Analyst, Reporting Analyst |
| Mid | Business Intelligence (BI) Analyst, Product Analyst, Marketing Analyst, Analytics Engineer |
| Senior | Senior Analyst, Analytics Lead, Senior Analytics Engineer |
| Leadership | Analytics Manager, Head of Analytics, Director of Decision Science |

"MIS" (management information systems) analyst is a common Indian title for reporting-focused work.

## What the work looks like day to day

- Turn a business question ("why did repeat orders fall in Pune?") into a precise, answerable query.
- Write SQL against a warehouse, check the result for errors, and join it to the right definitions (DAN301).
- Define metrics carefully: what counts as an "active user", a "conversion", a "churned" customer (DAN305).
- Build dashboards that people actually use, and retire the ones they do not (DAN303).
- Read A/B test results and say whether the effect is real (DAN302).
- Model data with dbt and a semantic layer so numbers match across teams (DAN304).
- Present findings and a recommendation to non-technical decision-makers.

## Demand signals

**No official US occupation is called "data analyst".** The closest signals:

- **Global employer survey.** "Data Analysts and Scientists" are among the 15 fastest-growing jobs to 2030, and "Big Data Specialists" are first ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).
- **US projections (proxy).** Operations research analysts +12% from 2025 to 2035 ([BLS](https://www.bls.gov/ooh/math/operations-research-analysts.htm)); data scientists +35% ([BLS](https://www.bls.gov/ooh/math/data-scientists.htm)).
- **US postings are weak.** Indeed's "Data & Analytics" postings index was 63.1 on 2 Oct 2026 (1 Feb 2020 = 100), slightly up from 58.5 a year earlier but far below the 2022 peak of 202.7. The UK index was 51.0 and Germany's 75.0 ([Indeed Hiring Lab data](https://github.com/hiring-lab/job_postings_tracker)).
- **India.** No strong public demand data for analysts in India was found. Employers in India expect Big Data Specialists to be among their fastest-growing roles ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).

**Analysis.** Long-term projections are positive, but current postings are weak. Analyst roles that only produce reports are the most exposed; roles that own metrics, experiments and decisions are holding up better.

## How AI is changing the role

**Automated or mostly automated.** First-draft SQL from a question (text-to-SQL), chart generation, dashboard summaries, cleaning scripts, and routine weekly reports. SQL was 6% of queries in Claude Code ([Anthropic, Apr 2025](https://www.anthropic.com/research/impact-software-development)).

**Augmented.** Exploratory analysis, anomaly explanation, writing narratives, translating between SQL dialects.

**Growing in value.**

- Knowing whether a generated query is right. Text-to-SQL fails quietly: wrong joins, double counting, wrong time zones, filters on the wrong definition (DAN401).
- Metric design and governance: a single agreed definition of each business number (DAN404).
- Experiment design and causal reasoning: telling correlation from cause (DAN501).
- Domain knowledge: finance, marketing, operations, healthcare (DAN403).
- Communicating a decision, not just a chart.

**Analysis.** When anyone can ask a chatbot for a chart, the analyst's value shifts to being the person whose numbers are trusted. That requires data modelling, statistics and the business context that a model does not have.

## Pay (indicative)

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Operations research analysts (closest official occupation) | Median $88,940; 10th $57,060; 90th $159,910 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/math/operations-research-analysts.htm) |
| India | Data Analyst | Average base ₹5.8 lakh; base range ₹2.9–10 lakh; under 1 year ≈₹4.1 lakh total (2,389 profiles, Jul 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Data_Analyst/Salary) |
| India | Business Intelligence (BI) Analyst | Average base ₹6.8 lakh (177 profiles, Jun 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Business_Intelligence_%28BI%29_Analyst/Salary) |

## The hiring loop

Typical loop (varies by company):

1. SQL test, live or take-home: joins, aggregation, window functions, deduplication.
2. Statistics basics: distributions, confidence intervals, A/B test interpretation, common pitfalls (peeking, multiple comparisons).
3. Case study: "daily orders dropped 8% yesterday; how do you investigate?" Interviewers check your structure and the questions you ask.
4. Dashboard or presentation round: present an analysis to a mixed audience.
5. Behavioural: a time your analysis changed a decision, or was wrong.

Expect at least one round where AI tools are not allowed, because SQL fluency is the baseline. See [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- SQL depth, including query plans and performance basics.
- Statistics and experiment design.
- Data modelling for analytics (dimensional models, dbt).
- Metric definition and documentation.
- Business domain knowledge.
- Clear visual and written communication.
- Healthy scepticism towards AI-generated queries and numbers.

## Adjacent roles and transitions

- **Analytics engineering and data engineering**: overlap OV06 ([DEN](DEN_data_engineering.md)).
- **Data science**: add modelling and causal inference ([DSC](DSC_data_science.md)).
- **Product management or strategy**: analysts who know the business well often move here.
- **Forward deployed engineering**: data-heavy customer deployments ([FDE](FDE_forward_deployed_engineering.md)).

## Sources

All checked October 2026.

- WEF, Future of Jobs Report 2025. https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- BLS, Occupational Outlook Handbook: Operations Research Analysts; Data Scientists (2025–35; May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/math/operations-research-analysts.htm ; https://www.bls.gov/ooh/math/data-scientists.htm
- Indeed Hiring Lab, job postings tracker (to 2 Oct 2026). https://github.com/hiring-lab/job_postings_tracker
- Anthropic, AI's impact on software development (28 Apr 2025). https://www.anthropic.com/research/impact-software-development
- Payscale India: Data Analyst; Business Intelligence (BI) Analyst (self-reported; 12 Oct 2026). https://www.payscale.com/research/IN/Job=Data_Analyst/Salary ; https://www.payscale.com/research/IN/Job=Business_Intelligence_%28BI%29_Analyst/Salary

_Last reviewed: 2026-10_
