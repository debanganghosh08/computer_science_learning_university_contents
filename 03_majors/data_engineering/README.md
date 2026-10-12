# Data Engineering (DEN) · Learning path

| Code | Entry requirements | Years | Market page | Interview loop |
|---|---|---|---|---|
| DEN | [CS211](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [CS212](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | 3–5 (after the common Years 1–2) | [DEN roles and market](../../06_career_and_market_readiness/01_market_map/roles/DEN_data_engineering.md) | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) |

Data engineering is the infrastructure side of data. Data engineers build the systems that collect, model, move, store, check and govern data so that analysts, applications, ML models and AI assistants can trust it. This major covers six areas:

- **Modelling and warehousing:** dimensional models and warehouse internals.
- **Processing:** batch with Spark, streaming with Kafka and Flink.
- **Orchestration:** scheduling, backfills and pipeline reliability.
- **Lakehouses:** Parquet, Iceberg and Delta.
- **Quality, platforms and governance:** data quality and contracts, cloud data platforms, governance and privacy.
- **Data for AI:** unstructured-data pipelines, embeddings and retrieval indexes.

It is not the analytics major: dashboards, metrics and analytics engineering in depth live in [Data Analysis (DAN)](../data_analysis/README.md). It is also not the ML major: model training and serving live in [Machine Learning Engineering (MLE)](../machine_learning_engineering/README.md). The three meet in the overlaps listed below.

## 1. Who this major is for, and the roles it leads to

It suits people who like building systems that other people depend on, care about correctness more than demos, and enjoy both SQL and distributed systems. Typical roles:

| Role | What people in it actually do |
|---|---|
| **Data engineer** | Builds and runs ingestion, transformation and serving pipelines. Models data (star schemas, slowly changing dimensions), tunes Spark and warehouse jobs, handles retries, backfills and late data, and is on call when a pipeline breaks |
| **Analytics engineer** | Turns raw data into tested, documented, well-modelled tables and metrics with dbt and SQL. Sits between data engineering and analysis ([OV06](../../04_overlaps/OV06_data_platform_analytics_engineering/README.md) is the bridge) |
| **Data platform engineer** | Builds the platform other data teams use: lakehouse tables and catalogs, orchestration, compute, access control, cost governance, self-service tooling |
| **Streaming engineer** | Runs Kafka, Flink and CDC pipelines with ordering, exactly-once and state guarantees for payments, logistics, fraud and real-time products |
| **AI data engineer** | Builds document ingestion, parsing, chunking, embedding and retrieval-index pipelines for AI systems, plus training and evaluation datasets, with freshness, permissions and erasure handled. The market page lists this as a newer title |
| **ML data engineer** | Builds feature pipelines and training data with point-in-time correctness; works closely with ML engineers ([OV04](../../04_overlaps/OV04_mlops_ml_platform/README.md)) |
| **Data architect / Staff data engineer** | Designs the organisation's data architecture, sets standards for modelling, contracts, governance and platforms, and leads migrations |
| **Privacy and data-governance engineer** | Turns privacy law (India's DPDP Act and Rules, GDPR) and sector rules (RBI, UIDAI) into lineage, access, masking, retention and erasure controls ([OV07](../../04_overlaps/OV07_privacy_engineering/README.md)) |

Seniority ladder (from the [market page](../../06_career_and_market_readiness/01_market_map/roles/DEN_data_engineering.md)): Data Engineer I or Associate → Data Engineer, Analytics Engineer, Streaming Engineer → Senior, Data Platform Engineer, Lead → Staff or Principal, Data Architect, Head of Data Platform.

**Demand and pay (sourced, October 2026).**

- **Growth:** the WEF's employer survey ranks Big Data Specialists as the fastest-growing job to 2030 by percentage, and Data Warehousing Specialists sixth. It also lists Big Data Specialists among India's fastest-growing roles.
- **US projections:** BLS expects database architects to grow faster than database administrators, as organisations adopting AI need people to design and secure their data systems.
- **India pay:** Payscale reports an average base salary of ₹9.7 lakh for data engineers (range ₹4.1–20 lakh; 1,284 self-reported profiles, July 2026).
- **US pay:** the closest official US occupation, database architects, had a median of $139,500 (May 2025).
- **Postings:** the broad US "Data & Analytics" postings index stood at 63.1 on 2 October 2026 (February 2020 = 100). That category mixes analysts and engineers, so treat it as a rough signal.

## 2. How AI is changing data engineering

**What is being automated.** First-draft SQL transformations, dbt model scaffolding, schema mapping, pipeline boilerplate, table and column documentation, and simple data-quality tests (market page). Vendors are building this into platforms:

- **BigQuery:** Google says its Data Engineering Agent, which builds and modifies pipelines from natural language, has been generally available since April 2026.
- **dbt:** dbt v2 is a Rust rewrite that statically analyses every model before it runs and ships agent skills. It arrived as Fivetran and dbt Labs completed their merger on 1 June 2026, which they framed around "data infrastructure for trusted AI agents".
- **DuckDB:** its CLI gained an agent mode in October 2026.
- **Stream processing:** Flink CDC 3.7 calls language models inside pipelines.

**How good the automation is.** The evidence is mixed, so check it yourself:

| Measure | Result | Source |
|---|---|---|
| Text-to-SQL on curated databases (BIRD) | Best ≈ 83% execution accuracy vs human ≈ 93% (Sept 2026) | [BIRD](https://bird-bench.github.io/) |
| Agents completing real dbt projects (Spider 2.0-DBT leaderboard) | Top entry 65.6 (self-reported leaderboard, Oct 2026) | [Spider 2.0](https://spider2-sql.github.io/) |
| End-to-end ELT pipelines built by agents (ELT-Bench) | Best agent tested built 3.9% of required data models correctly (Apr 2025; newer models score higher on related leaderboards) | [arXiv 2504.04808](https://arxiv.org/abs/2504.04808) |
| Developers using AI in production operations | 20% of AI users use it for "deploying, operating, or troubleshooting production systems" | [Stack Overflow, Oct 2026](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/) |

**What grows in value** (market page, with this major's courses):

- Data modelling that makes numbers correct and queries cheap ([DEN301](year_3/DEN301_data_modeling_and_warehousing/README.md)).
- Correctness under failure: idempotency, deduplication, late data, schema evolution ([DEN302](year_3/DEN302_batch_processing_with_spark/README.md)–[DEN304](year_3/DEN304_orchestration_and_pipelines_airflow_and_dagster/README.md)).
- Contracts and quality ownership between teams ([DEN401](year_4/DEN401_data_quality_observability_and_data_contracts/README.md)).
- Cost engineering on cloud platforms ([DEN402](year_4/DEN402_cloud_data_platforms_snowflake_bigquery/README.md)).
- Unstructured-data pipelines for AI ([DEN403](year_4/DEN403_data_engineering_for_ai_unstructured_data/README.md)).
- Governance and privacy ([DEN404](year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md)).

In US AI-related job postings, the fastest-growing skills were about running systems at scale: AWS, scalability and workflow management (AI Index 2026).

**What stays human.** Deciding the grain of a table and what a "customer" means. Choosing what to test and what to page on. Agreeing contracts between teams. Signing off on privacy and access. Owning incidents and restatements. Judging whether an agent's pipeline is correct under retries and backfills. **Analysis:** every AI feature depends on data that is fresh, correct, permitted and well described. As companies move AI from demos to production, the bottleneck is often the data layer, which is why every course in this major includes AI-off drills, verification methods and logs of AI failures you collect yourself.

## 3. The 5-year path

**Years 1–2 (common core).** Every course matters, but these matter most for data engineering:

| Course | Why it matters here |
|---|---|
| [FND101](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md) Programming I (Python) | Python is the main pipeline language |
| [FND104](../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) Linux, Shell, Git | Every pipeline runs on Linux and ships through Git |
| [FND112](../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) Data Structures and Algorithms I | Hashing, sorting and trees under every engine |
| [FND115](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md) Databases I: Modeling and SQL | SQL is the language of the job |
| [FND116](../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) Probability and Statistics I | Anomaly detection, sampling and data-quality monitoring |
| [CS201](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) Algorithms and Complexity | Joins, sketches, deduplication and cost reasoning |
| [CS203](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) Operating Systems | Memory, I/O and processes behind Spark and Kafka |
| [CS204](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md) Computer Networks | Shuffles, replication and cross-zone costs |
| [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) Software Engineering I | Testing and code review for pipelines |
| [CS211](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) Database Systems Internals | **Entry requirement.** Storage, indexes, execution, MVCC, WAL |
| [CS212](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) Distributed Systems I | **Entry requirement.** Replication, consensus, partitioning, MapReduce to Spark |
| [CS215](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) Cloud and DevOps Foundations | Object storage, containers, IaC for data platforms |
| [CS213](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) Security Foundations | Access control and encryption for DEN404 |
| [CS214](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) ML Foundations | Enough ML to serve ML and AI teams well |

**Years 3–5.** Full-time load is six 4-credit courses per semester. Slots marked "elective" are chosen from Section 5.

| Year · Semester | Major courses | Shared and other courses |
|---|---|---|
| 3 · 5 | [DEN301](year_3/DEN301_data_modeling_and_warehousing/README.md) Data Modeling and Warehousing · [DEN302](year_3/DEN302_batch_processing_with_spark/README.md) Batch Processing with Spark · [DEN303](year_3/DEN303_streaming_systems_kafka_and_flink/README.md) Streaming Systems: Kafka and Flink | [PRO301](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) Professional Practice: Ethics, Law and Responsible AI · 2 electives |
| 3 · 6 | [DEN304](year_3/DEN304_orchestration_and_pipelines_airflow_and_dagster/README.md) Orchestration and Pipelines · [DEN305](year_3/DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md) Lakehouse Architecture | [CAR301](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) Career Lab I · 3 electives |
| 4 · 7 | [DEN401](year_4/DEN401_data_quality_observability_and_data_contracts/README.md) Data Quality, Observability and Data Contracts · [DEN402](year_4/DEN402_cloud_data_platforms_snowflake_bigquery/README.md) Cloud Data Platforms | Overlap course A · [IND401](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) Industry Co-op Studio · 1–2 electives |
| 4 · 8 | [DEN403](year_4/DEN403_data_engineering_for_ai_unstructured_data/README.md) Data Engineering for AI · [DEN404](year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md) Data Governance, Lineage and Privacy Engineering | Overlap course B · [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) Career Lab II · 1–2 electives |
| 5 · 9 | [DEN501](year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md) Frontier Seminar: Real-Time AI Data Systems and Query Engine Internals | [RES501](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) Research Methods · [RES502](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) Reading, Reproducing and Extending Papers · [THS501](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) Thesis or Capstone I |
| 5 · 10 | — | [THS502](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) Thesis or Capstone II · [LCH502](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) Career Launch and Founder Studio |

Course dependencies inside the major: DEN301 → DEN401; DEN302 → DEN402; DEN303 → DEN403; DEN304 → DEN404; DEN401 and DEN403 → DEN501. DEN305 is the entry requirement for the OV06 overlap.

## 4. Skill map

| Level | What you can do | Where you get it | Gate |
|---|---|---|---|
| **L0** Absolute beginner | Run a query someone else wrote; follow a tutorial pipeline | FND101, FND115 | Load a CSV into PostgreSQL and answer 5 questions in SQL |
| **L1** Foundations | Write joins, aggregations and window functions; script a file-to-database load in Python; use Git and the shell | Year 1 | Solve 10 SQL problems AI-off in 60 minutes |
| **L2** Practitioner (intern-ready) | Explain how a database stores and executes a query; reason about replication and partitioning; build a small idempotent batch pipeline with tests | Year 2 (CS211, CS212) | Build and explain a re-runnable daily pipeline with reconciliation |
| **L3** Professional (job-ready) | Model a business process; build batch, streaming and orchestrated pipelines that survive retries, late data and backfills; run a lakehouse; tune Spark from the UI | Year 3 (DEN301–305), co-op | The mastery gates of DEN301–305, for example a 5× Spark speed-up from evidence and a Flink job that matches batch after 20 crashes |
| **L4** Expert (hard to replace) | Design platforms others build on: contracts across teams, observability with low false alarms, cost programmes with proof, AI data pipelines with freshness and permissions, privacy controls that survive audits; lead incidents | Year 4 (DEN401–404), overlap, IND401 | Lead a simulated data incident to restatement; prove an erasure across every store; cut a platform bill by 30% with SLOs intact |
| **L5** Research and frontier | Read, reproduce and extend data-systems research; contribute to engines; create new methods | Year 5 (DEN501, RES501–502, thesis) | A reproduced result and an extension paper with a rerunnable artefact |

## 5. Recommended overlaps and electives

**Overlaps (Year 4, choose one).** Each overlap lists required courses from other majors. Plan the electives in Year 3 so that you have them.

| Overlap | Why it fits | Courses it needs | Plan for it by |
|---|---|---|---|
| [OV06 Data Platform and Analytics Engineering](../../04_overlaps/OV06_data_platform_analytics_engineering/README.md) | The most common next step: platform plus analytics engineering, semantic layers and self-serve analytics with AI | DEN305, [DAN304](../data_analysis/year_3/DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md), [CLD305](../cloud_engineering/year_3/CLD305_cloud_storage_and_managed_databases/README.md) | Taking DAN304 and CLD305 as semester-6 electives |
| [OV07 Privacy Engineering](../../04_overlaps/OV07_privacy_engineering/README.md) | DPDP and GDPR duties land on data platforms; privacy-enhancing technologies and law in practice | DEN404, [SEC305](../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md), PRO301 | Taking SEC305 as a semester-6 elective. DEN404 is in semester 8, so check the overlap page for sequencing |
| [OV04 MLOps and ML Platform Engineering](../../04_overlaps/OV04_mlops_ml_platform/README.md) | Feature pipelines, training data and model platforms | [MLE401](../machine_learning_engineering/year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md), [OPS401](../devops_sre_platform_engineering/year_4/OPS401_platform_engineering_and_internal_developer/README.md), [CLD404](../cloud_engineering/year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md) | The heaviest prerequisites. Realistic only with extra semesters or prior ML and ops experience |
| [OV10 FinTech Systems Engineering](../../04_overlaps/OV10_fintech_systems_engineering/README.md) | Payments, ledgers, fraud and risk; India's UPI ecosystem needs streaming and reconciliation skills | DEN303, [BE401](../backend_engineering/year_4/BE401_payments_grade_systems_transactions_idempotency/README.md), SEC305 | Taking SEC305 in semester 6 and BE401 as a semester-7 elective (BE401 requires BE301) |

**Electives (Years 3–4).**

- **Analytics engineering:** [DAN304](../data_analysis/year_3/DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md) Analytics Engineering.
- **Cloud:** [CLD305](../cloud_engineering/year_3/CLD305_cloud_storage_and_managed_databases/README.md) Cloud Storage and Managed Databases; [CLD302](../cloud_engineering/year_3/CLD302_infrastructure_as_code_terraform_opentofu/README.md) Infrastructure as Code; [CLD403](../cloud_engineering/year_4/CLD403_finops_and_cloud_cost_engineering/README.md) FinOps and Cloud Cost Engineering.
- **Backend:** [BE304](../backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md) Asynchronous Systems.
- **ML and AI:** [MLE303](../machine_learning_engineering/year_3/MLE303_training_pipelines_feature_stores_and_experiment/README.md) Training Pipelines and Feature Stores; [AIE303](../ai_engineering/year_3/AIE303_retrieval_augmented_generation_and_search/README.md) Retrieval-Augmented Generation and Search.
- **Governance and security:** [SEC305](../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md) Governance, Risk and Compliance.
- **Operations and performance:** [OPS303](../devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md) Observability; [SWE305](../software_engineering/year_3/SWE305_concurrency_and_performance_engineering/README.md) Concurrency and Performance Engineering.
- **Distributed systems:** [CSG303](../computer_science_general/year_3/CSG303_distributed_systems_ii_consensus_replication/README.md) Distributed Systems II.

## 6. Flagship industry project

The major's flagship project is described in [`06_career_and_market_readiness/05_industry_projects/DEN_data_engineering.md`](../../06_career_and_market_readiness/05_industry_projects/DEN_data_engineering.md). The P3 projects in this major are built to combine into it:

- the streaming payment-risk system (DEN303);
- the operated streaming CDC lakehouse with erasure (DEN305);
- the deadline-bound orchestration platform (DEN304);
- the contract-driven quality platform (DEN401);
- the cost programme and migration (DEN402);
- the AI data platform with freshness and permissions (DEN403);
- the DPDP-ready governance controls (DEN404).

Together they form one portfolio system that an employer can run, break and inspect.

## 7. Certifications worth considering

Certifications are optional. They help with HR screens, consulting and partner firms (which often need certified staff for vendor partnerships), and with learning a platform's details. They never replace a portfolio. Pick at most one or two that match your target employers' stack. Details checked October 2026:

| Certification | Format and cost | Honest value note |
|---|---|---|
| [Databricks Certified Data Engineer Associate](https://www.databricks.com/learn/certification/data-engineer-associate) | 45 scored questions, 90 minutes, $200, valid 2 years; topics include ingestion, transformation, Lakeflow Jobs, CI/CD, governance | Useful if you target Databricks shops. The [Professional](https://www.databricks.com/learn/certification/data-engineer-professional) level carries more weight with experienced hiring managers |
| [SnowPro Core (COF-C03) and SnowPro Advanced: Data Engineer (DEA-C02)](https://learn.snowflake.com/en/certifications/) | $175 (Core) and $375 (Advanced); 20% regional discount for exams delivered in India | Core proves platform literacy; the Advanced exam is the data-engineering signal. Most valuable at Snowflake partners |
| [Google Cloud Professional Data Engineer](https://cloud.google.com/learn/certification/data-engineer) | 2 hours, 40–50 questions, $200, valid 2 years; Google recommends 3+ years of experience | A recognised broad credential. Hard for a student without real projects; better after your co-op |
| [AWS Certified Data Engineer – Associate](https://aws.amazon.com/certification/certified-data-engineer-associate/) | 130 minutes, $150, valid 3 years | Good value where AWS is the default cloud, which is common in Indian startups |
| [Microsoft Certified: Fabric Data Engineer Associate (DP-700)](https://learn.microsoft.com/en-us/credentials/certifications/fabric-data-engineer-associate/) | 100 minutes; free online renewal; English version updated 19 Oct 2026 | Useful in Microsoft-centred enterprises and services firms. Check the updated study guide first |

## 8. The interview loop

A typical data-engineering loop, from the [market page](../../06_career_and_market_readiness/01_market_map/roles/DEN_data_engineering.md), with where this major prepares you:

| Round | What is tested | Prepared by |
|---|---|---|
| SQL | Window functions, deduplication, sessionisation, slowly changing dimensions, NULL traps, often timed and AI-off | FND115, DEN301 (Chapter 9 drills) |
| Coding (Python, sometimes Scala or Java) | Data structures, parsing files and streams, idempotent logic | FND101, CS201, CAR301 |
| Data modelling | Design the warehouse for an e-commerce, ride-hailing or payments business: grain, facts, dimensions, history | DEN301 (Chapter 11 mock interviews) |
| Pipeline system design | Design a streaming payments pipeline or a daily batch with backfills: idempotency, late data, quality checks, cost, monitoring | DEN303, DEN304, DEN401, DEN402; CAR401 |
| Spark and distributed processing | Stages and shuffles, skew, join strategies, reading the Spark UI, when not to use Spark | DEN302 |
| Behavioural | A data incident you handled; a stakeholder who disagreed with a number | DEN401 incident drills, IND401 |

Some employers now allow or require AI tools in interviews, and others forbid them. The [AI-driven interviews section](../../06_career_and_market_readiness/04_ai_driven_interviews/) covers both formats with simulations. Practise every round both ways.

## 9. Fast track for working professionals

Take the placement checks in [`00_start_here/`](../../00_start_here/) first. Then choose the route that matches your background (part-time pace, about 15–25 hours a week):

| You are… | Skip or skim | Core route (in order) | Approximate time |
|---|---|---|---|
| **A software or backend engineer** | Years 1–2 except CS211 and CS212 if your database and distributed-systems depth is thin | DEN301 → DEN302 → DEN304 → DEN303 → DEN305 → DEN401 → DEN402 | 2–3 semesters part-time |
| **A data analyst or BI developer** | FND115 and parts of DEN301 | CS211 → CS212 → DEN301 (Chapters 6–9) → DEN302 → DEN304 → DEN305 → DEN401 | 3 semesters part-time |
| **A DBA or ETL developer** (SSIS, Informatica, PL/SQL) | CS211, most of DEN301 | CS212 → DEN302 → DEN305 → DEN304 → DEN402 → DEN401 | 2–3 semesters part-time |
| **An ML or AI engineer needing data skills** | CS214 and parts of DEN403 | CS211 → DEN301 → DEN303 → DEN305 → DEN403 → DEN404 | 2–3 semesters part-time |

On every route, do the P3 of each course you take: the projects, not the reading, are what employers check. Then add DEN403 and DEN404, because AI data pipelines and privacy controls are where demand is moving (market page). Use the DEN mastery gates as your exit tests.

## Sources

All checked October 2026. Market figures are reused from the [DEN market page](../../06_career_and_market_readiness/01_market_map/roles/DEN_data_engineering.md), which lists full citations.

- World Economic Forum, *Future of Jobs Report 2025*. https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- US BLS, *Occupational Outlook Handbook*: Database Administrators and Architects (2025–35; May 2025 pay). https://www.bls.gov/ooh/computer-and-information-technology/database-administrators.htm
- Stanford HAI, *AI Index 2026*. https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- Payscale India, Data Engineer (self-reported; checked 12 Oct 2026). https://www.payscale.com/research/IN/Job=Data_Engineer/Salary
- Indeed Hiring Lab, job postings tracker (to 2 Oct 2026). https://github.com/hiring-lab/job_postings_tracker
- Stack Overflow, 2026 Developer Survey results (6 Oct 2026). https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/
- BIRD leaderboard. https://bird-bench.github.io/ ; Spider 2.0 leaderboards. https://spider2-sql.github.io/ ; ELT-Bench (arXiv 2504.04808). https://arxiv.org/abs/2504.04808
- Google Cloud, BigQuery Data Engineering Agent documentation. https://docs.cloud.google.com/bigquery/docs/data-engineering-agent-pipelines
- dbt, "Upgrading to v2". https://docs.getdbt.com/docs/dbt-versions/dbt-upgrade/upgrading-to-v2 ; Fivetran, merger completion (1 Jun 2026). https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents
- DuckDB news (CLI agent mode, 9 Oct 2026). https://duckdb.org/news/ ; Apache Flink posts (Flink CDC 3.7.0). https://flink.apache.org/posts/
- Certification pages as linked in Section 7 (Databricks, Snowflake, Google Cloud, AWS, Microsoft), checked October 2026.

_Last reviewed: 2026-10_
