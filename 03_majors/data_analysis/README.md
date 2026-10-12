# DAN · Data Analysis and Analytics: learning path

| Code | Entry requirements | Major courses | Market and roles | Flagship project | Interview loop |
|---|---|---|---|---|---|
| DAN | [FND115](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md), [FND116](../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | 10 (DAN301–305, DAN401–404, DAN501) | [DAN role page](../../06_career_and_market_readiness/01_market_map/roles/DAN_data_analysis.md) | [DAN industry project](../../06_career_and_market_readiness/05_industry_projects/DAN_data_analysis.md) | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) |

This major trains people whose analysis changes business decisions. It covers SQL at depth, statistics and experiments for business, visualisation and written argument, analytics engineering, product and domain analytics, forecasting, governance and privacy, and the evaluation of AI tools that now draft much of the routine work. Building machine-learning models is the focus of [Data Science](../data_science/README.md), and building pipelines and platforms is the focus of [Data Engineering](../data_engineering/README.md). This major owns the layer where data becomes a number someone trusts and a decision someone makes.

## 1. Who this major is for, and the roles it leads to

It suits people who like questions more than tools: why did something change, is the effect real, what should we do. You need comfort with numbers, patience for detail, and the willingness to explain things to people who are not technical. Many strong analysts come from commerce, economics and engineering backgrounds alike (see the fast track in Section 9).

| Role | What people in it actually do | Courses that matter most |
|---|---|---|
| Data analyst | Turn business questions into SQL, check results, build reports and recommendations | DAN301, DAN302, DAN303 |
| MIS / reporting analyst | Own recurring management reports, often in Excel and BI tools; a common entry title in India | DAN301, DAN303, DAN404 |
| Business analyst (data) | Analyse processes and performance for a business unit. In Indian IT services the same title often means a requirements analyst, so read the job description | DAN305, DAN303, DAN403 |
| Product analyst | Define product metrics, run funnels, cohorts and experiments, partner with product managers | DAN305, DAN302, DAN301 |
| BI analyst / developer | Build semantic models and dashboards in Power BI, Tableau or Looker; manage access and performance | DAN303, DAN304, DAN404 |
| Analytics engineer | Model data with dbt, test it, define metrics in a semantic layer, run CI for analytics code | DAN304, DAN301, DAN404 |
| Marketing / growth analyst | Attribution, incrementality tests, marketing mix models, CAC and LTV | DAN403, DAN302, DAN305 |
| Finance / FP&A analyst | Variance analysis, budgets, driver-based forecasts, unit economics, board packs | DAN403, DAN402, DAN305 |
| Risk / credit analyst | Vintage curves, roll rates, approval strategy, monitoring of lending and payments | DAN403, DAN302, DAN404 |
| Operations / supply-chain analyst | Delivery, inventory and capacity analytics; forecasts feeding orders and staffing | DAN402, DAN403, DAN301 |
| Health and public-policy analyst | Survey and administrative data, programme evaluation, briefs for officials | DAN403, DAN302, DAN404 |
| Decision scientist / analytics lead | Causal analysis, decision models, governance of metrics and AI answers, leading a team | DAN501, DAN404, DAN401 |

The seniority ladder runs from data analyst and MIS analyst, through BI, product and analytics-engineering roles, to senior analyst, analytics lead, head of analytics and director of decision science ([role page](../../06_career_and_market_readiness/01_market_map/roles/DAN_data_analysis.md)).

**Pay and demand (indicative, checked October 2026).**

- **India.** Payscale reports an average base salary of ₹5.8 lakh for data analysts (self-reported, July 2026) and ₹6.8 lakh for BI analysts (June 2026).
- **US.** Operations research analysts, the closest official US occupation, had a median of $88,940 in May 2025, with employment projected to grow 12% from 2025 to 2035 (BLS).
- **Global.** The World Economic Forum lists "Data Analysts and Scientists" among the 15 fastest-growing jobs to 2030.
- **Postings now.** Indeed's US "Data & Analytics" postings index stood at 63.1 on 2 October 2026, against 100 in February 2020.

**Analysis.** Long-run demand looks positive, but entry-level competition is real. Report-only roles are the most exposed. Roles that own metrics, experiments and decisions are holding up better.

## 2. How AI is changing analysis

All facts below were checked in October 2026.

- **Adoption is high.** In dbt Labs' 2025 survey of 459 practitioners, 80% used AI in their daily work, up from 30% a year earlier. Poor data quality was still the most-cited challenge (over 56%), and increasing trust in data remained the top objective.
- **Every analytics tool now has a natural-language interface.**
  - Power BI's report Copilot pane is generally available.
  - Looker's Conversational Analytics is grounded in LookML.
  - Snowflake's Cortex Analyst works over semantic views and verified queries.
  - Databricks offers Genie One, Genie Agents and Genie Code.
  - Tableau Pulse writes metric insights in plain language.
- **Vendors document the limits themselves.**
  - Microsoft says that without a prepared semantic model, Copilot "can misinterpret the data and return generic or inaccurate results". Questions not about the model are answered from the LLM's general knowledge.
  - Looker's agent does not support forecasting, correlation or anomaly questions.
  - Cortex Analyst cannot reuse earlier query results in a conversation.
- **Benchmarks show progress and a persistent gap.**
  - On BIRD, the best text-to-SQL system scores 82.95% execution accuracy against 92.96% for human experts.
  - On Spider 2.0's enterprise tasks, the original paper's best model solved 17.1%. Leaderboard entries now report 96.70 on the Snowflake setting but 65.6 on dbt-project tasks.
  - When systems must ask clarifying questions (BIRD-Interact), GPT-5 solved 8.67% to 17.00% of tasks.
  - On DABstep's multi-step analysis tasks, the best agent solved 14.55% of the hard ones.
  - On CharXiv chart reasoning, GPT-4o scored 47.1% against 80.5% for humans.
- **Context decides accuracy.**
  - GPT-4 answered 16% of enterprise questions correctly over raw SQL schemas and 54% over a knowledge-graph representation of the same data (Sequeda et al., 2023).
  - Uber's QueryGPT moved to curated domain "workspaces" because plain retrieval lost accuracy as tables were added. Uber reports query-writing time falling from about 10 minutes to about 3, and says hallucinated tables were not fully solved (2024).
- **AI features can also disappear.** Excel's preview `COPILOT()` worksheet function stopped working on 14 September 2026; cells that recalculate now return `#NAME?`.

| Automated or mostly automated | Augmented | Growing in value (and where this major teaches it) |
|---|---|---|
| First-draft SQL and formulas, chart generation, routine report summaries, dialect translation, cleaning scripts, documentation drafts | Exploratory analysis, anomaly explanation, dashboard building, narrative writing, forecasting code, model scaffolding in dbt | Knowing whether an answer is right (DAN301, DAN401); metric design and definitions (DAN305, DAN404); semantic layers that make AI answers consistent (DAN304); experiment design and causal reasoning (DAN302, DAN501); domain knowledge (DAN403); decision-ready communication (DAN303); governance of personal data and AI use (DAN404) |

**Analysis.** When anyone can ask a chatbot for a chart, the analyst's value moves to being the person whose numbers are trusted. That requires owning definitions, verifying answers and understanding the business. Every course in this major therefore has AI-off drills, a verification method and documented AI failure modes.

## 3. The 5-year path

### Years 1–2: common core (what matters most for this major)

| Year · Semester | Courses | Priority for DAN |
|---|---|---|
| 1 · 1 | [FND101](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md) Python, FND102, FND103, [FND104](../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) Git, [FND105](../../01_year_1_foundations/semester_1/FND105_ai_native_learning_and_building/README.md) AI-native learning, [FND106](../../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md) communication | **Highest:** FND101, FND104, FND106 (analysts live by Python, Git and writing) |
| 1 · 2 | FND111, FND112, FND113, FND114, [FND115](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md) SQL, [FND116](../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) statistics | **Highest:** FND115 and FND116 (the entry requirements) |
| 2 · 3 | CS201, CS202, CS203, CS204, [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) testing and collaboration, [CS206](../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md) maths for ML | **High:** CS205 (tests, reviews, CI used in DAN304); CS206 (regression and optimisation) |
| 2 · 4 | [CS211](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) database internals, CS212, [CS213](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) security, [CS214](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) ML foundations, [CS215](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) cloud, CS216 | **High:** CS211 (query performance), CS214 (forecasting and uplift models), CS213 (needed for PRO301 and privacy work) |

### Years 3–5: major, shared courses and specialisation

A full-time load is six 4-credit courses per semester. Courses in bold are required for this major.

| Year · Semester | Major courses | Shared courses | Overlap and electives (pick to fill six) |
|---|---|---|---|
| 3 · 5 | **[DAN301](year_3/DAN301_spreadsheets_to_sql_analytical_querying_in_depth/README.md)** Spreadsheets to SQL · **[DAN302](year_3/DAN302_business_statistics_and_experimentation/README.md)** Business statistics and experimentation · **[DAN303](year_3/DAN303_data_visualization_and_storytelling/README.md)** Visualisation and storytelling | **[PRO301](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md)** Ethics, law and responsible AI | [DEN301](../data_engineering/year_3/DEN301_data_modeling_and_warehousing/README.md) Data modelling and warehousing; [DSC303](../data_science/year_3/DSC303_data_wrangling_at_scale_pandas_polars_and_spark/README.md) Data wrangling at scale |
| 3 · 6 | **[DAN304](year_3/DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md)** Analytics engineering · **[DAN305](year_3/DAN305_product_and_business_analytics_metrics_funnels/README.md)** Product and business analytics | **[CAR301](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md)** Career Lab I | For OV06: [DEN305](../data_engineering/year_3/DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md) and [CLD305](../cloud_engineering/year_3/CLD305_cloud_storage_and_managed_databases/README.md). Otherwise: [DSC304](../data_science/year_3/DSC304_experimental_design_and_causal_inference/README.md) causal inference; [SEC305](../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md) GRC |
| 4 · 7 | **[DAN401](year_4/DAN401_ai_augmented_analytics_text_to_sql_copilots/README.md)** AI-augmented analytics · **[DAN402](year_4/DAN402_forecasting_for_business_decisions/README.md)** Forecasting for business decisions | **[IND401](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md)** Industry co-op studio | Overlap course A (recommended [OV06A](../../04_overlaps/OV06_data_platform_analytics_engineering/OV06A_building_a_modern_data_platform/README.md)); [AIE302](../ai_engineering/year_3/AIE302_prompt_and_context_engineering/README.md) prompt and context engineering; [DEN401](../data_engineering/year_4/DEN401_data_quality_observability_and_data_contracts/README.md) data quality and contracts (needs DEN301) |
| 4 · 8 | **[DAN403](year_4/DAN403_domain_analytics_finance_marketing_operations/README.md)** Domain analytics · **[DAN404](year_4/DAN404_data_governance_quality_and_privacy_for_analysts/README.md)** Governance, quality and privacy | **[CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md)** Career Lab II | Overlap course B (recommended [OV06B](../../04_overlaps/OV06_data_platform_analytics_engineering/OV06B_semantic_layers_and_self_serve_analytics_with_ai/README.md)); one domain elective |
| 5 · 9 | **[DAN501](year_5/DAN501_frontier_seminar_decision_intelligence/README.md)** Frontier seminar: decision intelligence and causal analytics | **[RES501](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md)** Research methods · **[RES502](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md)** Reproducing papers · **[THS501](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md)** Thesis or capstone I | Electives, for example [DSC501](../data_science/year_5/DSC501_frontier_seminar_bayesian_methods_causal_ml/README.md) Bayesian methods and causal ML |
| 5 · 10 | — | **[THS502](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md)** Thesis or capstone II · **[LCH502](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md)** Career launch and founder studio | Electives or a full-time internship |

Prerequisite chain inside the major: DAN301 → DAN401; DAN302 → DAN402; DAN303 → DAN403; DAN304 → DAN404; DAN401 + DAN403 → DAN501. Taking DAN301 before DAN304 is strongly recommended even though the catalogue only requires FND115 and FND116.

## 4. Skill map by level

| Level | Data and SQL | Statistics and causality | Communication | Modelling and engineering | Business and domain | Working with AI |
|---|---|---|---|---|---|---|
| **L0** Absolute beginner | Sorts and filters a spreadsheet | Reads an average and a percentage | Copies a chart template | — | Knows what revenue and cost are | Asks a chatbot for a formula |
| **L1** Foundations | Joins, aggregates and simple windows in SQL; PivotTables; lookups (FND115) | Distributions, intervals, a basic A/B test (FND116) | Chooses a sensible chart; writes a clear paragraph | Understands tables, keys and grain | Reads a P&L and a funnel | Checks AI SQL against a known answer |
| **L2** Intern-ready | Cohorts, funnels, sessions, recursive CTEs in a warehouse dialect; Power Query (DAN301) | Ratio metrics, CUPED, SRM checks, regression for analysts (DAN302) | A dashboard and a one-page memo that a manager acts on (DAN303) | Builds a tested dbt star schema (DAN304) | Metric trees, LTV and CAC, unit economics (DAN305) | Uses copilots with a written verification checklist |
| **L3** Job-ready | Tested, linted, cost-aware SQL that reviewers trust | Designs and reads experiments; spots paradoxes and confounding | Presents to executives; defends numbers under challenge | Incremental models, semantic layers, CI and data diffs | Owns a metric set and diagnoses drops quickly | Builds a gold-set evaluation of an AI tool (DAN401) |
| **L4** Expert, hard to replace | Designs the analytics data model for a company | Chooses quasi-experimental designs; forecasts with honest uncertainty (DAN402) | Shapes leadership decisions with written argument | Governs metrics, quality, access and privacy (DAN404) | Deep in one domain: finance, marketing, operations or health (DAN403) | Ships a guarded, measured, auditable AI analytics assistant |
| **L5** Research and frontier | Builds new evaluation datasets and methods | Reproduces and extends causal and decision-science research (DAN501) | Publishes and teaches | Creates new tools or standards | Opens new problem areas (for example, Indian public data) | Advances the evaluation of data agents |

Each course's README states a concrete mastery gate. The major's overall gate is the flagship project in Section 6.

## 5. Recommended overlaps and electives

- **[OV06 Data Platform and Analytics Engineering](../../04_overlaps/OV06_data_platform_analytics_engineering/README.md)** (recommended for most students). It is composed of DEN305, DAN304 and CLD305, so take DEN305 and CLD305 as Year 3 Semester 6 electives. OV06A builds the platform under your models; OV06B builds governed self-serve analytics with AI on top of the semantic layer. It leads to analytics-engineering and BI-platform roles.
- **[OV07 Privacy Engineering](../../04_overlaps/OV07_privacy_engineering/README.md)**, for students heading to banking, insurance, health or regulated product companies. It is composed of DEN404, SEC305 and PRO301. Check the catalogue for scheduling, because DEN404 runs in Semester 8. DAN404 covers the analyst-side material.
- **[OV10 FinTech Systems Engineering](../../04_overlaps/OV10_fintech_systems_engineering/README.md)**, for students aiming at payments, lending and risk analytics who are willing to take backend and streaming courses. It is composed of BE401, SEC305 and DEN303, which carry their own prerequisites (BE301, CS211, CS212, CS213). Most DAN students reach fintech roles through DAN403's lending and payments chapters instead.
- **Electives by goal.**
  - Data science: [DSC304](../data_science/year_3/DSC304_experimental_design_and_causal_inference/README.md), [DSC303](../data_science/year_3/DSC303_data_wrangling_at_scale_pandas_polars_and_spark/README.md).
  - Data engineering: [DEN301](../data_engineering/year_3/DEN301_data_modeling_and_warehousing/README.md), [DEN401](../data_engineering/year_4/DEN401_data_quality_observability_and_data_contracts/README.md).
  - AI products: [AIE302](../ai_engineering/year_3/AIE302_prompt_and_context_engineering/README.md), [OV08B](../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08B_product_analytics_and_growth_for_ai_apps/README.md).
  - Governance: [SEC305](../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md).

## 6. Flagship industry project

The brief is in [06_career_and_market_readiness/05_industry_projects/DAN_data_analysis.md](../../06_career_and_market_readiness/05_industry_projects/DAN_data_analysis.md). Each part of it builds on a portfolio project from this major:

- a tested dimensional model with a semantic layer (DAN304 P3);
- an experiment designed for a marketplace (DAN302 P3);
- a unit-economics model and decision memo (DAN305 P3);
- a forecast turned into an inventory or staffing decision (DAN402 P3);
- an evaluated, guarded AI analytics assistant (DAN401 P3);
- a governance layer covering definitions, quality, access and DPDP duties (DAN404 P3).

Completing the flagship project end to end, and defending it to a panel, is the clearest proof that a graduate of this major is job-ready at L3.

## 7. Certifications worth having (optional)

No certification is required, and none replaces a portfolio and a live SQL round. Some help with résumé screening in specific stacks.

| Certification | Provider facts (checked Oct 2026) | Honest value | When |
|---|---|---|---|
| Google Data Analytics Professional Certificate | Coursera; nine courses; about 6 months at 10 hours a week; spreadsheets, SQL, Tableau and R, with added AI content; over 3.8 million enrolled | A structured start for career-changers. Weak signal for employers who test SQL directly, because so many people hold it | Before or during DAN301 if you are new to analysis |
| Microsoft Certified: Power BI Data Analyst Associate (PL-300) | 100-minute proctored exam; covers preparing, modelling, visualising and analysing data and managing and securing Power BI; free online renewal every 12 months; price set by country | Useful where employers run Microsoft stacks; proves Power Query and DAX basics | After DAN303 |
| Microsoft Certified: Fabric Analytics Engineer Associate (DP-600) | Semantic models, data preparation and solution maintenance in Fabric; SQL, KQL and DAX; English version due to be updated on 19 Oct 2026 | Relevant for analytics engineers in Microsoft Fabric organisations | After DAN304 |
| Salesforce Certified Tableau Data Analyst | Delivered through Salesforce Trailhead; no prerequisites; about 6 months of Tableau experience recommended | Useful for Tableau-heavy employers; check exam details on Trailhead before booking | After DAN303 |
| dbt Analytics Engineering Certification | US$200 per attempt; online proctored; valid for two years | Signals dbt competence, but a public, tested dbt project signals more | After DAN304 |

**Analysis.** In interviews, a candidate who can write a correct cohort query live, explain a test result and walk through a public portfolio project outperforms a candidate with certificates alone. Certificates matter most when a recruiter screens résumés by keyword for a specific tool.

## 8. The interview loop

A typical analyst loop, with variations by company:

1. **Online assessment.** Timed SQL, sometimes with spreadsheet tasks, aptitude or statistics questions. Prepared by DAN301 and FND116.
2. **Live SQL round, usually AI off.** Joins, windows, deduplication, cohorts, top-N with ties, and explaining a query's grain. Prepared by DAN301's timed rounds.
3. **Statistics and experiments.** p-values, intervals, power, SRM, peeking, Simpson's paradox. Prepared by DAN302.
4. **Case study or product sense.** "Orders fell 8% yesterday", "pick a north-star metric", "should we launch?" Prepared by DAN305 and DAN403.
5. **Guesstimate.** Market sizing with stated assumptions, for example "how many UPI QR codes are there at kirana stores in Pune?". These are common in Indian analyst loops, especially at startups and consulting-style analytics firms (based on candidate reports; not a measured share).
6. **Take-home, dashboard critique or presentation.** Build, critique or present an analysis to a mixed panel. Prepared by DAN303 and the P3 projects.
7. **Behavioural and hiring manager.** A time your analysis changed a decision, or was wrong.

Some companies now allow AI tools in take-homes and then probe whether you understand and can defend the output; live rounds are usually AI-off. Be ready to explain how you verified any AI-assisted work, with the checklists from DAN401. Question banks and simulations are in [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/).

**A guesstimate structure that works.** Restate the question and the unit. Choose a decomposition (population → households → stores, or demand side vs supply side). State each assumption with a range. Compute a low, base and high case, sanity-check against any public number you know, and say what data would narrow the range.

## 9. Fast tracks

**Commerce, BBA, B.Com and economics graduates (no CS background), about 10–12 months at 20–25 hours a week.**

| Phase | Weeks | Study | Portfolio output |
|---|---|---|---|
| 1 · Foundations | 1–8 | [FND101](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md) chapters 1–3, 7 and 8 (Python basics, collections, files and real data); FND115 chapters 1–3 and 7–8; FND116 chapters 1, 6 and 9–11 | Small SQL and statistics exercises |
| 2 · Core tools | 9–20 | DAN301 (all), DAN303 | DAN301 P1 and P2; DAN303 P2 |
| 3 · Analysis that decides | 21–32 | DAN302, DAN305 | DAN305 P3 (your commerce background is an advantage here) |
| 4 · Specialise | 33–44 | DAN403 (finance track if you know accounting) and DAN401 chapters 1–5, or DAN304 for analytics engineering | DAN403 P1 or P3; DAN401 P1 |
| 5 · Interview | 45–48 | Section 8 rounds; timed SQL; mock cases and guesstimates | Two polished portfolio pieces and a one-page résumé |

Gate: pass the DAN301 and DAN303 mastery gates before applying for analyst roles, and the DAN305 gate before product-analyst roles.

**Working professionals.**

- **Software engineers moving into analytics (about 6 months):** DAN302, DAN305, DAN303, then DAN304 and DAN401. Your SQL and Git transfer; the gaps are statistics, metrics and communication.
- **MIS or Excel analysts upgrading (about 6–8 months):** DAN301 chapters 4–11, DAN304, DAN401, then DAN404. Your business context transfers; the gaps are warehouse SQL, testing and modelling.
- **Domain experts (finance, marketing, operations, health):** DAN301 and DAN303 first, then DAN403 in your own domain and DAN302 for evidence standards.

## Sources

All checked October 2026. Market figures are reused from the [DAN role page](../../06_career_and_market_readiness/01_market_map/roles/DAN_data_analysis.md) and its sources.

- Payscale India, Data Analyst and BI Analyst (self-reported; 12 Oct 2026) — https://www.payscale.com/research/IN/Job=Data_Analyst/Salary ; https://www.payscale.com/research/IN/Job=Business_Intelligence_(BI)_Analyst/Salary
- BLS, Operations Research Analysts (2025–35 projections; May 2025 pay) — https://www.bls.gov/ooh/math/operations-research-analysts.htm
- WEF, Future of Jobs Report 2025 — https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- Indeed Hiring Lab, job postings tracker (to 2 Oct 2026) — https://github.com/hiring-lab/job_postings_tracker
- dbt Labs, 2025 State of Analytics Engineering (29 Apr 2025) — https://www.getdbt.com/resources/state-of-analytics-engineering-2025
- Microsoft Learn, Copilot for Power BI overview (updated 24 Aug 2026) — https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
- Google Cloud, Conversational Analytics in Looker (updated 9 Oct 2026) — https://docs.cloud.google.com/looker/docs/conversational-analytics-overview
- Snowflake, Cortex Analyst — https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst · Databricks, Genie (updated 18 Sep 2026) — https://docs.databricks.com/aws/en/genie/ · Tableau Pulse — https://help.tableau.com/current/online/en-us/pulse_intro.htm
- BIRD and BIRD-Interact (updated 9 Oct 2026) — https://bird-bench.github.io/ · Spider 2.0 — https://spider2-sql.github.io/ · DABstep — https://arxiv.org/abs/2506.23719 · CharXiv — https://arxiv.org/abs/2406.18521
- Sequeda, Allemang and Jacob (arXiv 2311.07509, 2023) — https://arxiv.org/abs/2311.07509
- Uber Engineering, QueryGPT (19 Sep 2024) — https://www.uber.com/blog/query-gpt/
- Microsoft Support, COPILOT function — https://support.microsoft.com/en-us/office/copilot-function-5849821b-755d-4030-a38b-9e20be0cbf62
- Coursera, Google Data Analytics Professional Certificate — https://www.coursera.org/professional-certificates/google-data-analytics
- Microsoft Learn, PL-300 — https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/ · DP-600 — https://learn.microsoft.com/en-us/credentials/certifications/fabric-analytics-engineer-associate/
- Salesforce Trailhead, Tableau Data Analyst credential — https://trailhead.salesforce.com/credentials/tableaudataanalyst
- dbt Labs, certifications — https://www.getdbt.com/dbt-certification

_Last reviewed: 2026-10_
