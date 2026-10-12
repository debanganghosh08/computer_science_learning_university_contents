# DSC · Data Science: roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [Data Science major](../../../03_majors/data_science/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

| Level | Common titles |
|---|---|
| Entry | Associate Data Scientist, Data Scientist I, Junior Data Scientist |
| Mid | Data Scientist, Product Data Scientist, Decision Scientist, Applied Scientist |
| Senior | Senior Data Scientist, Lead Data Scientist, Senior Applied Scientist |
| Staff and above | Staff/Principal Data Scientist, Head of Data Science |

The title covers two different jobs. **Analytics-focused data scientists** run experiments, causal analysis and metrics for product decisions. **Modelling-focused data scientists** build predictive models (forecasting, churn, fraud, recommendations) and work with ML engineers to deploy them.

## What the work looks like day to day

- Frame a vague business question as a measurable hypothesis.
- Pull and clean data at scale with SQL, pandas, Polars or Spark (DSC303).
- Design experiments and estimate causal effects when experiments are impossible (DSC304).
- Build and evaluate models; choose metrics that match the business cost of errors (DSC305).
- Forecast demand, revenue or load (DSC401).
- Use LLMs for text analytics: classification, extraction, summarisation, with evaluation (DSC402).
- Hand models to production, monitor them, and explain results to decision-makers (DSC404).

## Demand signals

- **US projections.** Data scientists: 275,600 jobs in 2025, projected +35% to 2035 (+95,400), about 24,800 openings a year. BLS links growth to "demand for data-driven decisions" and to firms that "continue to integrate artificial intelligence (AI)-based systems into their workflows" ([BLS](https://www.bls.gov/ooh/math/data-scientists.htm)).
- **Global employer survey.** "Data Analysts and Scientists" are among the 15 fastest-growing jobs to 2030, and "AI and big data" is the fastest-growing skill ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).
- **But current postings are weak.** Indeed's US "Data & Analytics" postings index was 63.1 on 2 Oct 2026 (1 Feb 2020 = 100) ([Indeed Hiring Lab data](https://github.com/hiring-lab/job_postings_tracker)). Ten-year projections and today's postings point in different directions; see the [market map](../README.md#10-where-sources-disagree).
- **India.** Employers in India expect Big Data Specialists and AI and ML Specialists to be among their fastest-growing roles ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)). India's AI talent concentration rose 120% between 2019 and 2025 ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)).

## How AI is changing the role

**Automated or mostly automated.** Exploratory-analysis code, plotting, baseline models with standard libraries, feature-engineering boilerplate, notebook documentation, and literature summaries.

**Augmented.** Model debugging, hypothesis generation, writing analysis reports, and text analytics. Large language models now replace many custom NLP models for classification and extraction, but they need evaluation sets and error analysis (DSC402).

**Growing in value.**

- Problem framing: deciding which question is worth answering.
- Causal inference and experiment design. AI tools readily produce correlations that look like answers.
- Evaluation: choosing metrics, building test sets, detecting leakage, quantifying uncertainty.
- Statistical judgement about whether a model or an AI-generated analysis is valid.
- Communication of uncertainty to decision-makers.

**Analysis.** The data science tasks that are easiest to automate are the ones that used to fill a junior data scientist's week: cleaning, plotting, fitting a baseline. What remains is the part that needs statistical maturity and business context. Expect entry-level candidates to be judged on reasoning, not on how many libraries they know.

## Pay (indicative)

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Data scientists | Median $120,230; 10th $67,240; 90th $199,130 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/math/data-scientists.htm) |
| India | Data Scientist | Average base ₹10.2 lakh; base range ₹3.1–20 lakh; under 1 year ≈₹6.0 lakh total (1,267 profiles, Jul 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Data_Scientist/Salary) |
| India | Data Scientist | Median total pay ₹30.1 lakh; 25th ₹18.7 lakh; 90th ₹63.1 lakh (1,064 submissions, Oct 2026) | Self-reported, mostly product companies | [Levels.fyi](https://www.levels.fyi/t/data-scientist/locations/india) |

## The hiring loop

Typical loop (varies by company):

1. SQL and Python screen: data manipulation, joins, aggregation.
2. Statistics and probability: hypothesis tests, power, bias, Bayes' rule, regression assumptions.
3. Machine learning concepts: bias–variance, regularisation, evaluation metrics, leakage.
4. Product or business case: define success metrics for a feature and design an experiment.
5. Take-home analysis or modelling exercise with a written report.
6. Behavioural, often with a product manager.

AI policies vary for take-homes; some employers allow AI and ask you to explain every step, others forbid it. See [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- Probability and statistical inference.
- Causal inference: experiments, difference-in-differences, instrumental variables, regression discontinuity.
- Model evaluation and error analysis.
- SQL and scalable data processing.
- Domain knowledge in one industry.
- Writing and presenting with honest uncertainty.

## Adjacent roles and transitions

- **Data analysis** ([DAN](DAN_data_analysis.md)).
- **Machine learning engineering**: take models to production ([MLE](MLE_machine_learning_engineering.md)).
- **Data engineering** ([DEN](DEN_data_engineering.md)).
- **AI engineering**: evaluation of LLM systems is a natural fit for statisticians ([AIE](AIE_ai_engineering.md)).
- **AI for science and research**: overlap OV11 ([DLR](DLR_deep_learning.md)).

## Sources

All checked October 2026.

- BLS, Occupational Outlook Handbook: Data Scientists (2025–35; May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/math/data-scientists.htm
- WEF, Future of Jobs Report 2025. https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- Indeed Hiring Lab, job postings tracker (to 2 Oct 2026). https://github.com/hiring-lab/job_postings_tracker
- Stanford HAI, AI Index 2026. https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- Payscale India and Levels.fyi India, Data Scientist (self-reported; 12 Oct 2026). https://www.payscale.com/research/IN/Job=Data_Scientist/Salary ; https://www.levels.fyi/t/data-scientist/locations/india

_Last reviewed: 2026-10_
