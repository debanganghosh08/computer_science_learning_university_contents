# Data Science (DSC) · Learning path

| Code | Years | Entry requirements | Market page | Interview loop |
|---|---|---|---|---|
| DSC | 3–5 (after the common Years 1–2) | [CS214](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [FND116](../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | [DSC roles and market](../../06_career_and_market_readiness/01_market_map/roles/DSC_data_science.md) | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) |

## 1. Who this major is for

Data science is the work of turning data into decisions when the answer is uncertain. A data scientist asks four questions: what happened, why did it happen, what will happen next, and what should we do about it. The last two questions need statistics, causal reasoning and machine learning, and the answer is only useful if the person who must act on it believes it.

This major is for you if you enjoy probability and statistics, like arguing about evidence, and want your work to change a decision rather than fill a dashboard. It is built on three pillars: **statistical modelling** (DSC301, DSC401, DSC501), **experimentation and causal inference** (DSC304, DSC501), and **applied machine learning for decisions** (DSC302, DSC305, DSC402, DSC403).

How it differs from its neighbours:

| Major | Main question | Typical output | Choose it if you want to |
|---|---|---|---|
| Data Analysis (DAN) | What happened, and for whom? | BI dashboards, metric definitions, dbt models, semantic layers | Own a company's reporting and analytics engineering |
| **Data Science (DSC)** | **Why, what next, and what should we do?** | **Experiments, causal estimates, forecasts, predictive models, decision memos** | **Own the evidence behind product, pricing, risk and policy decisions** |
| Data Engineering (DEN) | How does the data get here, reliably? | Pipelines, lakehouses, streaming systems, data contracts | Build the platform everyone else depends on |
| ML Engineering (MLE) | How does a model run at scale? | Training pipelines, feature stores, serving, MLOps | Build and operate ML systems in production |

The boundaries are porous. A data scientist writes SQL every day (DAN), reads Parquet at scale (DEN) and hands models to engineers (MLE). This major teaches enough of each to collaborate, and goes deepest where those majors stop: inference, causality, forecasting and evaluation.

## 2. Roles this major leads to

| Role | What people in it actually do | Courses that matter most |
|---|---|---|
| Product data scientist (analytics flavour) | Define success metrics, design and read A/B tests, estimate causal effects of launches, size opportunities, advise product managers | DSC301, DSC304, DSC404 |
| Data scientist (modelling flavour) | Build churn, fraud, credit-risk, pricing and propensity models; choose metrics that match the cost of errors; hand models to ML engineers | DSC302, DSC305, DSC404 |
| Decision scientist | Combine forecasts, experiments and optimisation into a recommendation; quantify trade-offs for leadership | DSC304, DSC401, DSC404 |
| Applied scientist | Research-flavoured modelling inside product teams (recommendations, search, forecasting, NLP), often with publications | DSC401–DSC403, DSC501 |
| Forecasting / demand scientist | Forecast demand, supply or load at many levels (store, SKU, city, hour) and turn forecasts into inventory or staffing decisions | DSC401, DSC303 |
| Quantitative analyst / risk modeller | Credit scoring, loss forecasting, model validation and model-risk documentation in banks, NBFCs, insurers and fintechs | DSC301, DSC305, DSC404 |
| Research data scientist | Policy evaluation, public health, economics and science; survey data, field experiments, Bayesian models | DSC301, DSC304, DSC501 |

The seniority ladder (associate data scientist → data scientist → senior/lead → staff/principal) and the split between analytics-focused and modelling-focused data scientists are described on the [market page](../../06_career_and_market_readiness/01_market_map/roles/DSC_data_science.md), with sourced demand and pay figures. Two headline facts from it: the US Bureau of Labor Statistics projects data scientist jobs to grow 35% from 2025 to 2035 (about 24,800 openings a year), while Indeed's US "Data & Analytics" postings index stood at 63.1 on 2 October 2026, below its February 2020 level. Long-run projections and current postings disagree; the market page explains why.

## 3. How AI is changing data science

All facts checked in October 2026.

**Agents can now do much of the modelling on well-specified problems.** OpenAI's MLE-bench measures whether an AI agent can earn a Kaggle medal in 75 real competitions within 24 hours. In October 2024 the best setup (o1-preview with the AIDE scaffold) reached a medal in 16.9% of competitions. By February 2026 the top entry on the main leaderboard reached 64.4%. OpenAI paused new leaderboard submissions in April 2026 while it develops a fairer comparison process ([MLE-bench paper](https://arxiv.org/abs/2410.07095); [leaderboard](https://github.com/openai/mle-bench)).

**Notebook agents write whole analyses.** Google made its Data Science Agent in Colab generally available on 3 March 2025. It generates complete, runnable notebooks from a plain-language goal such as "build and optimize prediction model", and the announcement itself notes that it "may make mistakes" ([Google Developers Blog](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/)). Similar assistants ship inside Jupyter (Jupyter AI), Positron (Posit Assistant), Databricks and every major chat assistant.

**Open-ended analysis is harder for agents than Kaggle.** Kaggle tasks arrive with a fixed metric and a clean target. Real analysis does not. On BLADE, a 2024 benchmark of 12 open research questions with ground truth from expert analysts, language models were "often limited to basic analyses", and agents that could run code improved but stayed "non-optimal" in their analytical decisions ([BLADE](https://arxiv.org/abs/2408.09667)). On DSBench (2024), the best agent solved 34.12% of 466 realistic data-analysis tasks ([DSBench](https://arxiv.org/abs/2409.07703)). These benchmarks are dated, and current models score higher; the gap between closed and open-ended tasks is the durable point.

**Analytic freedom was a problem before AI, and AI makes it cheaper.** In the "Many Analysts, One Data Set" study, 29 teams (61 analysts) answered the same question with the same data. Their effect estimates ranged from 0.89 to 2.93 in odds-ratio units; 20 teams found a significant effect and 9 did not, and neither expertise nor prior beliefs explained the spread ([Silberzahn et al., 2018](https://doi.org/10.1177/2515245917747646)). An agent can now run a hundred such specifications in an afternoon and report the best-looking one.

**Language models replace much custom text labelling.** Zero-shot ChatGPT labels beat crowd workers by about 25 percentage points on average across four annotation datasets, at under $0.003 per label ([Gilardi et al., 2023](https://doi.org/10.1073/pnas.2305016120)). Using those labels for downstream statistics without correction can bias the result; methods such as prediction-powered inference give valid confidence intervals when a small human-labelled set is available ([Angelopoulos et al., 2023](https://doi.org/10.1126/science.adi6000)).

| Mostly automated now | Augmented (a human decides) | Growing in value |
|---|---|---|
| Exploratory-analysis code, plots, baseline models, boilerplate feature engineering, notebook documentation, first-draft SQL and pandas | Model debugging, error analysis, hypothesis generation, report drafting, text analytics with LLM labels, hyperparameter search | Problem framing, causal identification and experiment design, evaluation design (metrics, test sets, leakage), quantifying uncertainty, judging whether an AI-generated analysis is valid, communicating to decision-makers, accountability under privacy law |

**Analysis.** The tasks that used to fill a junior data scientist's week (cleaning, plotting, fitting a baseline) are the ones agents now do well. What remains scarce is judgement about whether the question, the design and the evidence hold up. That is why every course in this major has AI-off drills on inference and design, a verification method for AI output, and a rule that every claimed result must survive a test the analyst did not choose after seeing the data. India adds a further reason to keep humans accountable: the Digital Personal Data Protection Rules, 2025 were notified in November 2025 with an 18-month phased compliance window ([PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014)), so purpose, consent and minimisation become design constraints on every model that uses personal data.

## 4. The 5-year path

### Years 1–2: the common core

Every student takes all of Years 1–2. These courses matter most for this major:

| Course | Why it matters for data science |
|---|---|
| [FND101](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md) Programming I (Python) | Python is the working language of every DSC course |
| [FND106](../../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md) Technical Communication | The decision memo is the main deliverable of the job |
| [FND113](../../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md) Linear Algebra and Calculus | Regression, PCA, matrix factorisation, gradients |
| [FND115](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md) Databases I: SQL | The first screen in most data science interviews |
| [FND116](../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) Probability and Statistics I | Entry requirement; the base of DSC301 and DSC304 |
| [CS206](../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md) Mathematics for ML | Likelihood, optimisation, information theory |
| [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) Software Engineering I | Tests, Git workflows and reviews for analysis code |
| [CS211](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) Database Internals | Why a query or a join is slow (DSC303) |
| [CS214](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) ML Foundations | Entry requirement; leakage, validation, trees, metrics |

### Years 3–5: the major

| Semester | Major courses | Shared courses | Notes |
|---|---|---|---|
| 5 (Y3) | [DSC301](year_3/DSC301_statistical_inference_and_modeling/README.md) Statistical Inference and Modeling · [DSC302](year_3/DSC302_applied_machine_learning_for_data_scientists/README.md) Applied ML for Data Scientists · [DSC303](year_3/DSC303_data_wrangling_at_scale_pandas_polars_and_spark/README.md) Data Wrangling at Scale | [PRO301](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) Ethics, Law and Responsible AI | One elective (see §6) |
| 6 (Y3) | [DSC304](year_3/DSC304_experimental_design_and_causal_inference/README.md) Experimental Design and Causal Inference · [DSC305](year_3/DSC305_feature_engineering_and_model_evaluation/README.md) Feature Engineering and Model Evaluation | [CAR301](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) Career Lab I | One elective; summer internship target |
| 7 (Y4) | [DSC401](year_4/DSC401_time_series_analysis_and_forecasting/README.md) Time Series and Forecasting · [DSC402](year_4/DSC402_nlp_and_text_analytics_with_llms/README.md) NLP and Text Analytics with LLMs | [IND401](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) Industry Co-op Studio | Overlap course A |
| 8 (Y4) | [DSC403](year_4/DSC403_recommender_systems_and_personalization/README.md) Recommender Systems and Personalization · [DSC404](year_4/DSC404_data_science_in_production_deployment_monitoring/README.md) Data Science in Production | [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) Career Lab II | Overlap course B; flagship project |
| 9 (Y5) | [DSC501](year_5/DSC501_frontier_seminar_bayesian_methods_causal_ml/README.md) Frontier Seminar: Bayesian Methods, Causal ML and AI-Assisted Science | [RES501](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) Research Methods · [RES502](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) Reproducing Papers · [THS501](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) Thesis or Capstone I | Choose a thesis (research) or capstone (industry) |
| 10 (Y5) | — | [THS502](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) Thesis or Capstone II · [LCH502](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) Career Launch and Founder Studio | Defend the thesis; launch |

**One project spine runs through the major.** Several P3 projects build on each other: the India district panel from DSC303 supplies covariates to the small-area model in DSC301 (both in semester 5) and is the starting point for the policy evaluation in DSC304; the model from DSC305 and the forecasting system from DSC401 are deployed and monitored in DSC404. By the end of Year 4 you have one connected, public body of work rather than ten unrelated notebooks.

## 5. Skill map by level

| Level | You can… | Evidence that proves it |
|---|---|---|
| L0 · Absolute beginner | Load a CSV, compute a mean, draw a histogram, follow a worked analysis | Reproduce a tutorial notebook end to end |
| L1 · Foundations (end of Year 1) | Write SQL with joins and aggregations; explain sampling variation, confidence intervals and p-values; fit a linear regression and read its output | Answer FND116 problem sets without AI; a short analysis with correct uncertainty |
| L2 · Practitioner (end of Year 2) | Build a validated scikit-learn pipeline, spot common leakage, choose a split that matches deployment, report results with intervals | CS214 projects; an honest baseline that matches a hidden holdout |
| L3 · Professional (end of Year 3) | Design and analyse an A/B test with variance reduction and SRM checks; estimate a causal effect from observational data with a defensible design; build a calibrated, cost-aware model; wrangle hundreds of millions of rows on a laptop | DSC301–DSC305 P3 projects; a decision memo a product manager acted on |
| L4 · Expert (end of Year 4) | Own forecasting, text analytics or personalisation for a business area; design evaluation and monitoring for models in production; lead the analysis of a high-stakes decision and defend it to leadership | DSC401–DSC404 P3 projects; the flagship project; co-op references |
| L5 · Research (Year 5) | Reproduce and extend a methods paper; develop or adapt a Bayesian or causal-ML method; evaluate AI-assisted analysis rigorously | DSC501 replication; thesis; a workshop paper or public preprint |

## 6. Recommended overlaps and electives

You take one overlap specialisation in Year 4 (course A in semester 7, course B in semester 8). Each overlap assumes some background from its composing courses; take one of them as a Year 3 elective.

| Overlap | Why a data scientist takes it | Take as Year 3 elective |
|---|---|---|
| [OV06 Data Platform and Analytics Engineering](../../04_overlaps/OV06_data_platform_analytics_engineering/README.md) | You become the data scientist who can also build the semantic layer and lakehouse your models depend on; common in start-ups and GCCs with small data teams | [DAN304](../data_analysis/year_3/DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md) or [DEN305](../data_engineering/year_3/DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md) |
| [OV07 Privacy Engineering](../../04_overlaps/OV07_privacy_engineering/README.md) | Personal data is the raw material of most models; differential privacy, anonymisation and the DPDP Act are becoming part of the data scientist's job | [SEC305](../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md) (PRO301 is already in your path) |
| [OV10 FinTech Systems Engineering](../../04_overlaps/OV10_fintech_systems_engineering/README.md) | OV10B (Fraud Detection and Risk Systems) is a direct fit for credit, fraud and risk modelling; India's payment scale makes it a large employer | [DEN303](../data_engineering/year_3/DEN303_streaming_systems_kafka_and_flink/README.md) |
| [OV11 AI for Science and Research Engineering](../../04_overlaps/OV11_ai_for_science_research_engineering/README.md) | DSC301 is already one of its components; the natural route to research data science, public health and climate work | [DLR304](../deep_learning/year_3/DLR304_training_deep_networks_optimization/README.md) |

**Electives worth taking** (pick according to the role you want):

- [DAN303](../data_analysis/year_3/DAN303_data_visualization_and_storytelling/README.md) Data Visualization and Storytelling: for product and decision scientists.
- [DAN305](../data_analysis/year_3/DAN305_product_and_business_analytics_metrics_funnels/README.md) Product and Business Analytics: metric trees, funnels and cohorts that DSC304 assumes.
- [DEN302](../data_engineering/year_3/DEN302_batch_processing_with_spark/README.md) Batch Processing with Spark: if your target employer runs Spark at scale.
- [MLE304](../machine_learning_engineering/year_3/MLE304_model_evaluation_fairness_and_robustness/README.md) Model Evaluation, Fairness and Robustness: for modelling-focused roles.
- [MLE401](../machine_learning_engineering/year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md) MLOps: if you want to ship your own models without waiting for an ML engineer.
- [AIE305](../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md) Evaluating LLM Systems: evaluation is where statisticians are most useful in AI engineering.
- [CSG305](../computer_science_general/year_3/CSG305_human_computer_interaction/README.md) Human-Computer Interaction: for experimentation and user-research-heavy roles.

## 7. Flagship industry project

The major's flagship project is specified in [`06_career_and_market_readiness/05_industry_projects/DSC_data_science.md`](../../06_career_and_market_readiness/05_industry_projects/DSC_data_science.md). It is done in semester 8, alongside DSC404, and must show the whole job in one piece of work: a decision framed with a stakeholder, a forecast or model evaluated against the cost of errors, an experiment or a causal design that measures the decision's effect, a deployed and monitored artefact, and a written recommendation with honest uncertainty. The P3 projects of DSC303, DSC304, DSC401, DSC305 and DSC404 are designed as its building blocks.

## 8. Certifications: an honest note

No certification is required for any data science role, and none replaces a public, reproducible portfolio. Data-science-specific vendor certifications have also been unstable:

- Microsoft's Azure Data Scientist Associate certification (exam DP-100) is retired ([Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-scientist/), checked Oct 2026).
- AWS Certified Machine Learning – Specialty is being retired; the last exam date was 31 March 2026, and existing holders stay certified for three years ([AWS](https://aws.amazon.com/certification/certified-machine-learning-specialty/)).

Still available, and useful mainly if your target employer runs that platform: Google Cloud Professional Machine Learning Engineer (US$200 registration fee) ([Google Cloud](https://cloud.google.com/learn/certification/machine-learning-engineer)), AWS Certified Machine Learning Engineer – Associate (US$150) ([AWS](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/)) and Databricks Certified Machine Learning Associate ([Databricks](https://www.databricks.com/learn/certification/machine-learning-associate)). They test platform ML engineering far more than statistics or causal inference. Stronger signals for data science hiring: a replicated published analysis, a well-documented experiment analysis, a forecasting project scored against a public benchmark, and Kaggle or public competition results you can explain line by line.

## 9. The interview loop

The typical loop (from the [market page](../../06_career_and_market_readiness/01_market_map/roles/DSC_data_science.md); it varies by company), with where this curriculum prepares you:

| Stage | What is tested | Prepare with |
|---|---|---|
| 1 · SQL and Python screen | Joins, window functions, aggregation, pandas or Polars fluency, often timed | FND115, DSC303, CAR301 |
| 2 · Statistics and probability | Hypothesis tests, power, bias, Bayes' rule, regression assumptions, "explain a p-value to a PM" | FND116, DSC301 |
| 3 · Machine learning concepts | Bias–variance, regularisation, evaluation metrics, leakage, calibration, imbalanced data | CS214, DSC302, DSC305 |
| 4 · Product or business case | Define success metrics for a feature, design the experiment, handle interference and novelty effects, decide with ambiguous results | DSC304, DSC404, DAN305 (elective) |
| 5 · Take-home analysis | A modelling or analysis exercise with a written report; AI policies differ by employer | DSC302 P1, DSC404 memo labs |
| 6 · Behavioural (often with a product manager) | Influence without authority, handling a result nobody wanted | DSC404 Ch. 7–8, IND401 |

Some employers now allow AI tools in take-homes and ask you to explain every step; others forbid them. Practise both ways. The [AI-driven interviews section](../../06_career_and_market_readiness/04_ai_driven_interviews/) has simulations, and [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) runs mock loops.

## 10. Fast track for working professionals

Each track assumes 12–15 hours a week. Pass each course's mastery gate before moving on; the gates, not the calendar, decide your pace.

| You are… | Skip or skim | Core sequence | Time |
|---|---|---|---|
| A software engineer moving into data science | FND101, FND115, DSC303 (take only its Spark and performance chapters) | FND116 → CS214 → DSC301 → DSC304 → DSC302 → DSC305 → one of DSC401–DSC403 by target role | ~9–11 months |
| A data analyst (SQL and dashboards) moving up | FND115, most of DSC303 | FND116 refresher → CS214 → DSC301 → DSC304 → DSC305 → DSC404 | ~8–10 months |
| A scientist, economist or engineer with strong statistics | FND116, most of DSC301 (do its Bayesian and GLM chapters) | CS214 → DSC303 → DSC302 → DSC305 → DSC304 (online-experiment chapters 4–6) → DSC404 | ~7–9 months |

In every track, finish with one P3 project from your target area plus the DSC404 decision memo. Those two artefacts carry most of the weight in interviews.

## Sources

All checked October 2026.

- US Bureau of Labor Statistics, *Occupational Outlook Handbook: Data Scientists* (2025–35 projections; page modified 27 Aug 2026). https://www.bls.gov/ooh/math/data-scientists.htm
- Indeed Hiring Lab, job postings tracker (to 2 Oct 2026). https://github.com/hiring-lab/job_postings_tracker
- Chan et al., *MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering* (arXiv 2410.07095, Oct 2024; ICLR 2025). https://arxiv.org/abs/2410.07095 ; leaderboard and April 2026 pause notice: https://github.com/openai/mle-bench
- Google Developers Blog, *Data Science Agent in Colab: The future of data analysis with Gemini* (3 Mar 2025). https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/
- Gu et al., *BLADE: Benchmarking Language Model Agents for Data-Driven Science* (arXiv 2408.09667, Aug 2024). https://arxiv.org/abs/2408.09667
- Jing et al., *DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?* (arXiv 2409.07703, Sep 2024). https://arxiv.org/abs/2409.07703
- Silberzahn et al., *Many Analysts, One Data Set*, Advances in Methods and Practices in Psychological Science 1(3), 2018. https://doi.org/10.1177/2515245917747646
- Gilardi, Alizadeh and Kubli, *ChatGPT outperforms crowd workers for text-annotation tasks*, PNAS, 2023. https://doi.org/10.1073/pnas.2305016120
- Angelopoulos et al., *Prediction-powered inference*, Science, 2023. https://doi.org/10.1126/science.adi6000
- Press Information Bureau, *Government notifies DPDP Rules* (Nov 2025). https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014
- Certification pages: Microsoft Learn (Azure Data Scientist Associate, retired) https://learn.microsoft.com/en-us/credentials/certifications/azure-data-scientist/ ; AWS ML Specialty https://aws.amazon.com/certification/certified-machine-learning-specialty/ ; AWS ML Engineer Associate https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/ ; Google Cloud PMLE https://cloud.google.com/learn/certification/machine-learning-engineer ; Databricks ML Associate https://www.databricks.com/learn/certification/machine-learning-associate

_Last reviewed: 2026-10_
