# Machine Learning Engineering (MLE)

**Machine learning engineers build the systems that turn data into predictions people rely on, and keep those systems correct, fast and affordable in production.** This major covers the whole path: the algorithms underneath, the design of ML systems, training pipelines and feature stores, evaluation and fairness, applied modelling on tabular, image and text data, MLOps, distributed training, recommendation at scale, efficient inference, and research engineering.

| Entry requirements | Major courses | Overlaps that fit best | Role page | Read next |
|---|---|---|---|---|
| [CS214](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | MLE301–305, MLE401–404, MLE501 | [OV04](../../04_overlaps/OV04_mlops_ml_platform/README.md), [OV09](../../04_overlaps/OV09_edge_ai_secure_iot/README.md), [OV11](../../04_overlaps/OV11_ai_for_science_research_engineering/README.md), [OV05](../../04_overlaps/OV05_ai_security_safety/README.md) | [MLE role page](../../06_career_and_market_readiness/01_market_map/roles/MLE_machine_learning_engineering.md) | [Market map](../../06_career_and_market_readiness/01_market_map/README.md) |

**How this major differs from its neighbours.** [AI Engineering](../ai_engineering/README.md) builds products on top of foundation models (prompts, retrieval, agents). [Deep Learning](../deep_learning/README.md) goes deep into architectures and training large neural networks, including LLM pretraining. [Data Science](../data_science/README.md) focuses on inference, experiments and decisions. Machine learning engineering is the **systems** discipline: making any model, from logistic regression to a trillion-parameter recommender, work reliably at scale.

## 1. Who this major is for, and the roles it leads to

It suits you if you like both mathematics and engineering, enjoy debugging things that fail quietly, and want your work measured by what happens in production.

| Role | What people in it actually do |
|---|---|
| **Machine learning engineer** | Frames problems, builds features and training pipelines, trains and evaluates models, deploys them as services or batch jobs, monitors them and retrains them. The broadest role, and the main target of this major. |
| **Applied scientist / applied ML engineer** | Pushes model quality on a product problem (fraud, search, pricing, ETA, catalogue quality): runs experiments, reads and adapts papers, designs offline and online evaluations. |
| **Ranking and recommendation engineer** | Builds retrieval, ranking and re-ranking for feeds, search, ads and notifications; owns value functions, real-time features and online experiments. |
| **ML platform engineer** | Builds the internal platform other ML teams use: feature stores, experiment tracking, training orchestration, model registries, serving and monitoring. |
| **ML infrastructure engineer (training)** | Runs and optimises large training jobs: parallelism layouts, cluster scheduling, checkpointing, fault tolerance, utilisation and cost. |
| **Inference and performance engineer** | Makes models cheap and fast to serve: quantisation, distillation, compilers, batching, serving engines, CPU and on-device deployment. |
| **MLOps engineer** | Owns CI/CD/CT for models, progressive delivery, monitoring, incident response and governance, often alongside SRE. |
| **Research engineer** | Turns research ideas into reliable experiments, reproduces and extends papers, and builds research infrastructure in labs and research groups. |

Many of these roles also lead to founding: a strong ML engineer can take a narrow, valuable prediction problem (credit risk for a lender, demand forecasting for a retailer, quality inspection for a factory) from data to a product without a large team.

## 2. How AI is changing machine learning engineering

**What the evidence shows (checked October 2026)**

- **Agents now do much of the "Kaggle loop".** On OpenAI's MLE-bench (75 Kaggle competitions), the best agent at launch earned at least a bronze medal in 16.9% of competitions (October 2024). By February 2026, the top leaderboard entry (Famou-Agent 2.0 with Gemini 3 Pro Preview, 24-hour runs) reached 64.4%. A separately listed 77.8% result used test-set feedback, a reminder that agents optimise whatever signal they are given, leaks included. Google's MLE-STAR agent reported medals in 63% of MLE-bench Lite competitions (August 2025). ([MLE-bench paper](https://arxiv.org/abs/2410.07095), [leaderboard](https://github.com/openai/mle-bench), [MLE-STAR](https://research.google/blog/mle-star-a-state-of-the-art-machine-learning-engineering-agents/))
- **Short tasks are automated faster than long ones.** METR's RE-Bench found the best agents scored about 4× higher than human experts with a 2-hour budget, but humans narrowly led at 8 hours and scored about 2× the best agent at 32 hours ([METR, Nov 2024](https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/)). On PaperBench, the best agent averaged a 21.0% replication score on 20 ICML 2024 papers; on a three-paper subset, ML PhDs reached 41.4% in 48 hours against 26.6% for o1 ([PaperBench, Apr 2025](https://arxiv.org/abs/2504.01848)).
- **Strong baselines are now cheap.** Tabular foundation models such as TabPFN (*Nature*, January 2025; TabPFN-3.5 accepts up to 1,000,000 rows and 20,000 features in 2026), frozen image features (DINOv3, August 2025) and sentence embeddings give good models in minutes ([TabPFN](https://github.com/PriorLabs/TabPFN), [DINOv3](https://arxiv.org/abs/2508.10104)).
- **The work is shifting toward systems, evaluation and cost.** Chip Huyen describes AI engineering as "less on modeling and training, and more on model adaptation", with evaluation "a much bigger problem" and inference optimisation more important ([*AI Engineering* excerpt, May 2025](https://newsletter.pragmaticengineer.com/p/the-ai-engineering-stack)). At Uber, the Michelangelo platform grew to more than 5,000 production models and 10 million real-time predictions per second at peak ([Uber, May 2024](https://www.uber.com/blog/from-predictive-to-generative-ai/)).
- **Demand is growing, and skewing senior.** In India, Naukri's JobSpeak index showed AI/ML hiring up 20% year on year in September 2026, against 2% for all white-collar hiring; the increase was +54% for 13–16 years of experience, +28% for 8–12 years and +19% for freshers ([Naukri, Oct 2026](https://www.naukri.com/blog/naukri-jobspeak-october-2026-white-collar-hiring-ai-ml-growth/)). For FY26 as a whole, Naukri reported AI/ML hiring up 45% ([Naukri, Apr 2026](https://www.naukri.com/blog/naukri-jobspeak-march-26-records-a-9-rise-in-white-collar-hiring-as-fy26-closes-at-8-the-strongest-job-growth-in-three-years/)). Global projections and job-posting data are in the [market map](../../06_career_and_market_readiness/01_market_map/README.md).
- **Interviews are changing too.** Canva expects machine-learning candidates to use AI tools in an AI-assisted coding round ([Canva, Jun 2025](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)); Meta told staff some coding candidates may use an AI assistant ([404 Media, Jul 2025](https://www.404media.co/meta-is-going-to-let-job-candidates-use-ai-during-coding-tests/)); others, such as Anthropic, ask for no AI unless stated ([Anthropic](https://www.anthropic.com/candidate-ai-guidance)).

**Analysis: what is being automated, and what grows in value**

| Being automated or commoditised | Growing in value |
|---|---|
| Writing training scripts, feature code, DAGs, Dockerfiles and manifests | Validation design that mirrors deployment; finding leakage before production |
| Hyperparameter search and model selection on a fixed, clean benchmark | Problem framing, metrics tied to decisions, and offline–online alignment |
| Baseline models on standard tabular, image and text tasks | Data quality, labels you can trust, point-in-time-correct features |
| Summarising papers and documentation | Reproducing and extending results; knowing when a gain is real |
| First drafts of design documents | Production ownership: rollouts, monitoring, incidents, retraining policy |
| | Cost and latency engineering for training and inference at scale |
| | Fairness, robustness and regulatory evidence (EU AI Act, RBI guidance) |

The pattern in the evidence is consistent: agents are strong on bounded, well-scored tasks and weaker on long, open-ended work where the scoring signal itself must be designed. This major trains you for the second kind.

## 3. The 5-year path

**Years 1–2: the common core.** Every course matters, but these matter most for this major:

| Year · Semester | Courses that matter most for MLE | Why |
|---|---|---|
| 1 · 1 | [FND101 Programming I (Python)](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md), [FND104 Linux, Shell, Git](../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md), [FND105 AI-Native Learning](../../01_year_1_foundations/semester_1/FND105_ai_native_learning_and_building/README.md) | Python and the command line are daily tools; disciplined AI use starts here |
| 1 · 2 | [FND113 Linear Algebra and Calculus](../../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md), [FND116 Probability and Statistics I](../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md), [FND115 Databases I: SQL](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md), [FND112 DSA I](../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) | The mathematics of every model; SQL for every feature pipeline |
| 2 · 3 | [CS206 Mathematics for ML](../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md), [CS205 Software Engineering I](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS203 Operating Systems](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md), [CS201 Algorithms](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) | Optimisation and probability in depth; testing and design; processes, memory and concurrency for training and serving |
| 2 · 4 | [CS214 ML Foundations](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS212 Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md), [CS215 Cloud and DevOps](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [CS211 Database Internals](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) | The entry gate to the major, plus the systems background for MLOps and distributed training |

**Years 3–5: the major.**

| Year · Semester | Major courses | Shared and other courses |
|---|---|---|
| 3 · 5 | [MLE301 ML Algorithms from Scratch](year_3/MLE301_machine_learning_algorithms_from_scratch/README.md) · [MLE302 ML System Design](year_3/MLE302_machine_learning_system_design/README.md) · [MLE303 Training Pipelines, Feature Stores and Experiment Tracking](year_3/MLE303_training_pipelines_feature_stores_and_experiment/README.md) | [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) |
| 3 · 6 | [MLE304 Model Evaluation, Fairness and Robustness](year_3/MLE304_model_evaluation_fairness_and_robustness/README.md) · [MLE305 Applied ML: Tabular, Vision and Text](year_3/MLE305_applied_ml_tabular_vision_and_text/README.md) | [CAR301 Career Lab I: DSA, Portfolio and Open Source](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) · one elective (see section 5) |
| 4 · 7 | [MLE401 MLOps: Deployment, Monitoring and Retraining](year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md) · [MLE402 Distributed Training and Large-Scale ML](year_4/MLE402_distributed_training_and_large_scale_ml/README.md) | [IND401 Industry Co-op Studio](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) · overlap course A (for example [OV04A ML Platform Engineering](../../04_overlaps/OV04_mlops_ml_platform/OV04A_ml_platform_engineering/README.md)) |
| 4 · 8 | [MLE403 Ranking and Recommendation Systems at Scale](year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md) · [MLE404 Efficient Inference](year_4/MLE404_efficient_inference_quantization_distillation/README.md) | [CAR401 Career Lab II: Interviews, System Design and AI-Driven Assessments](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) · overlap course B (for example [OV04B LLMOps at Scale](../../04_overlaps/OV04_mlops_ml_platform/OV04B_llmops_at_scale/README.md)) |
| 5 · 9 | [MLE501 Frontier Seminar: ML Research Engineering and Reproducing Papers](year_5/MLE501_frontier_seminar_ml_research_engineering/README.md) | [RES501 Research Methods and Scientific Writing](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) · [RES502 Reading, Reproducing and Extending Papers](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) · [THS501 Thesis or Capstone I](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |
| 5 · 10 | — | [THS502 Thesis or Capstone II](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) · [LCH502 Career Launch and Founder Studio](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) · electives or a second overlap |

**How the courses connect.** MLE301 → MLE401 (your library becomes a deployed model); MLE302 → MLE402 (design estimates become cluster plans); MLE303 → MLE403 (feature freshness at recommender scale); MLE304 → MLE404 (slice-level evaluation guards every compression step); MLE401 and MLE403 → MLE501. Each course's `projects.md` lists exactly which later work builds on its projects.

## 4. Skill map by level

| Level | You can… | Evidence that proves it | Where you get it |
|---|---|---|---|
| **L0** Absolute beginner | Run a notebook that trains a model from a tutorial | A reproduced tutorial | FND101 |
| **L1** Foundations | Explain and implement linear models, trees and k-means; compute metrics; write clean Python and SQL | Course projects in FND116, CS206, CS214 | Years 1–2 |
| **L2** Practitioner (intern-ready) | Train and evaluate models on real data with leak-free validation; package a model; use tracking and version control | CS214 projects; MLE301 P1; MLE305 P1 | Year 2 – early Year 3 |
| **L3** Professional (job-ready) | Design an ML system end to end; build point-in-time features and pipelines; deploy with canaries and monitoring; evaluate by slice and fairness; deliver competition-grade applied models | MLE302 P2, MLE303 P2, MLE304 P2, MLE305 P2, MLE401 P2 | Year 3 – Year 4 semester 7 |
| **L4** Expert (senior, hard to replace) | Run ML platforms and large training jobs; build recommenders at scale; cut inference cost several-fold without breaking slices; lead design reviews and incidents | MLE401 P3, MLE402 P3, MLE403 P3, MLE404 P3, IND401 | Year 4 |
| **L5** Research and frontier | Reproduce and extend papers to publication standard; frame open problems; build research infrastructure | MLE501 P3, THS501–502 | Year 5 |

**Mastery gates you must pass on the way:** each course README ends with a concrete gate (for example, MLE305: find 4 of 5 planted leaks in 45 minutes; MLE401: detect and mitigate an unannounced fault in a 45-minute game day; MLE402: take a single-GPU script to a sharded run that survives a killed worker).

## 5. Recommended overlaps and electives

**Overlaps (Year 4).**

| Overlap | Composed of | Why it fits | Roles |
|---|---|---|---|
| [OV04 MLOps and ML Platform Engineering](../../04_overlaps/OV04_mlops_ml_platform/README.md) | MLE401, [OPS401](../devops_sre_platform_engineering/year_4/OPS401_platform_engineering_and_internal_developer/README.md), [CLD404](../cloud_engineering/year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md) | The most direct extension of this major | ML platform engineer, MLOps engineer, LLMOps engineer |
| [OV09 Edge AI and Secure IoT](../../04_overlaps/OV09_edge_ai_secure_iot/README.md) | EMB401, EMB402, MLE404 | Takes MLE404's on-device work to real devices and fleets | Edge ML engineer, on-device inference engineer |
| [OV11 AI for Science and Research Engineering](../../04_overlaps/OV11_ai_for_science_research_engineering/README.md) | DLR304, DSC301, MLE501 | Research-engineering depth for labs and scientific ML; because it requires MLE501, take it in Year 5 semester 10 | Research engineer, scientific ML engineer |
| [OV05 AI Security and Safety Engineering](../../04_overlaps/OV05_ai_security_safety/README.md) | AIE305, OFF403, SAR403 | Robustness, red-teaming and governance for models in production | AI security engineer, ML safety engineer |

**Electives (pick by target role).**

- *Deeper models:* [DLR301 Neural Networks from Scratch](../deep_learning/year_3/DLR301_neural_networks_from_scratch_autograd/README.md), [DLR304 Training Deep Networks](../deep_learning/year_3/DLR304_training_deep_networks_optimization/README.md), [DLR404 Efficient Deep Learning and GPU Programming](../deep_learning/year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md) (pairs with MLE402 and MLE404).
- *Data and decisions:* [DSC304 Experimental Design and Causal Inference](../data_science/year_3/DSC304_experimental_design_and_causal_inference/README.md) (for ranking and experimentation roles), [DSC401 Time Series and Forecasting](../data_science/year_4/DSC401_time_series_analysis_and_forecasting/README.md) (for demand and ETA work).
- *Data platforms:* [DEN303 Streaming Systems: Kafka and Flink](../data_engineering/year_3/DEN303_streaming_systems_kafka_and_flink/README.md), [DEN305 Lakehouse Architecture](../data_engineering/year_3/DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md).
- *LLM-era products:* [AIE303 Retrieval-Augmented Generation and Search](../ai_engineering/year_3/AIE303_retrieval_augmented_generation_and_search/README.md), [AIE305 Evaluating LLM Systems](../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md), [AIE402 Fine-Tuning and Small Models](../ai_engineering/year_4/AIE402_fine_tuning_and_small_models_for_products/README.md).
- *Systems:* [SWE305 Concurrency and Performance Engineering](../software_engineering/year_3/SWE305_concurrency_and_performance_engineering/README.md).

## 6. Flagship industry project

The major's flagship project is specified in [06_career_and_market_readiness/05_industry_projects/MLE_machine_learning_engineering.md](../../06_career_and_market_readiness/05_industry_projects/MLE_machine_learning_engineering.md). It should be the one piece of work you show every employer: a real prediction problem taken from raw data to a monitored production service, with leak-free evaluation, slice and fairness analysis, a canary rollout, drift monitoring, a retraining policy and a cost report. Your course projects are its building blocks: MLE302 P2 or P3 (the design), MLE303 P3 (the pipeline), MLE304 P3 (the evaluation harness), MLE401 P3 (the platform) and MLE404 P2 (the cost reduction).

## 7. Certifications (optional, never required)

Certifications show familiarity with one cloud's ML services; they do not replace a portfolio, and none is required by this curriculum. Status as of October 2026:

| Certification | Status and cost | Honest value note |
|---|---|---|
| [AWS Certified Machine Learning Engineer – Associate](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/) | MLA-C01 ($150) had its last English sitting on 28 Sep 2026; MLA-C02 in beta from 29 Sep 2026 ($75 beta price; adds generative and agentic AI); general availability date not announced | Useful where teams run on SageMaker AI; take C02 once it is generally available |
| [AWS Certified Machine Learning – Specialty](https://aws.amazon.com/certification/certified-machine-learning-specialty/) | Retired; last exam day 31 Mar 2026 | Do not plan for it |
| [Google Cloud Professional Machine Learning Engineer](https://cloud.google.com/learn/certification/machine-learning-engineer) | $200; recommends 3+ years' industry experience; recently updated for Google's move from Vertex AI to Gemini Enterprise Agent Platform | Most relevant cloud ML certification for design-level skills; better taken after Year 4 |
| [Databricks ML Associate](https://www.databricks.com/learn/certification/machine-learning-associate) / [Professional](https://www.databricks.com/learn/certification/machine-learning-professional) | $200 each; valid 2 years | Useful for data-platform-heavy employers and consultancies |
| Microsoft [DP-100](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-scientist/) and AI-102 | Both shown as retired; replaced by [AI-300 Machine Learning Operations Engineer Associate](https://learn.microsoft.com/en-us/credentials/certifications/operationalizing-machine-learning-and-generative-ai-solutions/) and AI-103 | AI-300 maps closely to MLE401; relevant for Azure-centred employers |
| NVIDIA [NCA-GENL](https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-associate/) / [NCP-GENL](https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-professional/) | $125 / $200; whether the professional exam is open for registration is unconfirmed | LLM-focused; relevant mainly for inference and GPU-infrastructure roles |

**Analysis.** For services companies, cloud partners and consulting, a cloud ML certification can help pass résumé filters. For product companies and labs, shipped projects, open-source contributions and a published reproduction carry far more weight.

## 8. The interview loop

The detailed loops, question banks and simulations are in [04_ai_driven_interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/). For ML engineering, expect some combination of these rounds; exact formats vary by company and change often:

| Round | What it tests | Where this major prepares you |
|---|---|---|
| Coding (data structures and algorithms) | Problem solving and clean code, sometimes AI-assisted | FND112, CS201, CAR301 |
| ML coding | Implementing an algorithm or data transformation in Python/NumPy; debugging a training script | MLE301, MLE305 |
| ML fundamentals | Bias–variance, losses, metrics, calibration, regularisation, trees vs neural networks | MLE301, MLE304, CS214 |
| ML system design | Framing, data, features, model, serving, evaluation, monitoring for a product problem; Chip Huyen's *Machine Learning Interviews* notes that almost all companies she spoke to ask at least one such question ([book](https://huyenchip.com/ml-interviews-book/)) | MLE302, MLE403, MLE401 |
| Specialised depth | Distributed training, inference optimisation, ranking, or MLOps, depending on the team | MLE402, MLE404, MLE403, MLE401 |
| Project deep dive and behavioural | Ownership, trade-offs, incidents, collaboration | Every course's P3, IND401 |

Practise both modes: AI-off (whiteboard design, hand derivations) and AI-assisted (finding and fixing problems in AI-generated code, as Canva describes). Each MLE course README lists five interview questions with what a strong answer must cover.

## 9. Fast track for working professionals

Start with the mastery gates: if you can pass a course's gate now, skip the course and do only its P3. Budgets assume 12–15 hours a week.

| You are now… | Take, in order | Skip or skim | Time |
|---|---|---|---|
| **Software or backend engineer** | CS206 chapters 4–8 and 11 → CS214 → MLE301 (chapters 2–3, 6–8) → MLE305 → MLE302 → MLE303 → MLE304 → MLE401 | Most of Years 1–2 systems courses; MLE401's packaging chapters | 9–12 months |
| **Data scientist** | MLE303 → MLE302 → MLE401 → MLE304 (chapters 9–11) → then MLE402, MLE403 or MLE404 by target role | MLE301 (do the mastery gate), MLE305 chapters 1–5 | 6–9 months |
| **Data engineer** | CS206 → CS214 → MLE301 → MLE305 → MLE302 → MLE304 → MLE401 | MLE303 chapters 2–4 and 8 | 9–12 months |
| **DevOps / SRE / platform engineer** | CS214 → MLE302 → MLE303 → MLE401 → MLE402 → MLE404 → [OV04](../../04_overlaps/OV04_mlops_ml_platform/README.md) | MLE305 except chapters 1–2 | 9–12 months |
| **Researcher moving to industry** | MLE302 → MLE303 → MLE401 → MLE304 → MLE404 | MLE301, MLE501 | 5–8 months |

Whatever your route, finish with the flagship industry project and two mock interview loops from [04_ai_driven_interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/).

## Sources

All checked October 2026.

1. Chan et al., "MLE-bench" (arXiv 2410.07095, Oct 2024) — https://arxiv.org/abs/2410.07095 ; MLE-bench leaderboard (top entry 64.44% ± 1.18% any medal, 23 Feb 2026; 77.78% test-feedback result listed separately; submissions paused Apr 2026) — https://github.com/openai/mle-bench
2. Google Research, "MLE-STAR" (1 Aug 2025) — https://research.google/blog/mle-star-a-state-of-the-art-machine-learning-engineering-agents/
3. METR, RE-Bench (22 Nov 2024) — https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/ ; paper — https://arxiv.org/abs/2411.15114
4. Starace et al., "PaperBench" (Apr 2025) — https://arxiv.org/abs/2504.01848
5. Hollmann et al., TabPFN (*Nature*, Jan 2025) — https://www.nature.com/articles/s41586-024-08328-6 ; TabPFN repository — https://github.com/PriorLabs/TabPFN ; DINOv3 (Aug 2025) — https://arxiv.org/abs/2508.10104
6. Chip Huyen, *AI Engineering*, excerpt in The Pragmatic Engineer (20 May 2025) — https://newsletter.pragmaticengineer.com/p/the-ai-engineering-stack ; *Machine Learning Interviews* (2021) — https://huyenchip.com/ml-interviews-book/
7. Uber, "From Predictive to Generative – How Michelangelo Accelerates Uber's AI Journey" (2 May 2024) — https://www.uber.com/blog/from-predictive-to-generative-ai/
8. Naukri JobSpeak, September 2026 (published 6 Oct 2026) — https://www.naukri.com/blog/naukri-jobspeak-october-2026-white-collar-hiring-ai-ml-growth/ ; March 2026 / FY26 (published 6 Apr 2026) — https://www.naukri.com/blog/naukri-jobspeak-march-26-records-a-9-rise-in-white-collar-hiring-as-fy26-closes-at-8-the-strongest-job-growth-in-three-years/
9. Canva, "Yes, You Can Use AI in Our Interviews" (11 Jun 2025) — https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/ ; 404 Media on Meta (29 Jul 2025) — https://www.404media.co/meta-is-going-to-let-job-candidates-use-ai-during-coding-tests/ ; Anthropic candidate AI guidance — https://www.anthropic.com/candidate-ai-guidance
10. Certification pages: AWS MLA — https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/ ; AWS ML Specialty — https://aws.amazon.com/certification/certified-machine-learning-specialty/ ; Google Cloud PMLE — https://cloud.google.com/learn/certification/machine-learning-engineer ; Databricks — https://www.databricks.com/learn/certification/machine-learning-associate and https://www.databricks.com/learn/certification/machine-learning-professional ; Microsoft DP-100 — https://learn.microsoft.com/en-us/credentials/certifications/azure-data-scientist/ ; Microsoft AI-300 — https://learn.microsoft.com/en-us/credentials/certifications/operationalizing-machine-learning-and-generative-ai-solutions/ ; NVIDIA — https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-associate/ and https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-professional/

_Last reviewed: 2026-10_
