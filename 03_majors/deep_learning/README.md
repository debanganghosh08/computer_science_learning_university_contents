# Deep Learning (DLR) · Learning path

**The science and engineering of neural networks: architectures, training, large-language-model pretraining and alignment, reinforcement learning, efficiency on GPUs, and research.** This major is for people who want to build and understand models, not only call them through an API. Building products on top of models is the [AI Engineering major](../ai_engineering/); running ML systems in production is the [Machine Learning Engineering major](../machine_learning_engineering/). Graduates of this major train the models those teams use.

| Entry requirements | Market and roles | Interview loop | Flagship project |
|---|---|---|---|
| [CS214](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) and [CS206](../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md) | [DLR market page](../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md) | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) | [DLR industry project](../../06_career_and_market_readiness/05_industry_projects/DLR_deep_learning.md) |

## 1. Who this major is for, and the roles it leads to

It suits you if you enjoy both mathematics and code, like running experiments and finding out why they failed, and can live with uncertainty: most research ideas do not work. You finish able to implement any architecture from a paper, train it at the scale your budget allows, measure it honestly, make it fast, and explain what it learned.

| Role | What people in it actually do | Where this major prepares you |
|---|---|---|
| Deep learning engineer (applied) | Train and fine-tune vision, speech or language models for a product; own data pipelines, evaluation and model quality; hand models to platform teams | DLR301–305, DLR401–402 |
| Research engineer (pretraining, post-training, evaluation, inference) | Implement and scale experiments, run ablations, debug loss spikes and numerical problems, build evaluation harnesses; the market page lists these as Member of Technical Staff specialisms | DLR304, DLR401, DLR403, DLR404 |
| Research scientist | Choose research directions, design experiments, publish; in industry often expects a PhD or publication record (DLR market page) | DLR501, RES501–502, THS501–502 |
| Applied scientist | Apply research methods to a company's problems (ranking, speech, vision, language) and prove gains with careful experiments | DLR302–305, DLR401–402 + electives |
| GPU performance engineer | Write CUDA and Triton kernels, profile training and inference, cut cost per token | DLR404, CS202 |
| Interpretability and alignment researcher | Study model internals, reasoning faithfulness, reward hacking and evaluations for safety | DLR403, DLR501, OV05 |
| AI-for-science research engineer | Build models for weather, materials, biology or satellite data with scientists | DLR302, DLR304, OV11 |

Entry titles include research intern, AI resident, Research Engineer I and applied deep learning engineer ([DLR market page](../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md)). That page also summarises demand and pay: industry produced over 90% of notable frontier models in 2025, and competition for industry research roles is intense (AI Index 2026).

## 2. How AI is changing this field

All figures below were checked in October 2026. Paragraphs marked **Analysis** are interpretation.

**AI agents now do real research-engineering work, unevenly.**
- **Time horizons.** METR measures the length of task, in expert human time, that agents complete with a given success rate. The frontier horizon doubled about every seven months from 2019 to 2025 (Kwa et al., 2025). For current values, see the [market map](../../06_career_and_market_readiness/01_market_map/README.md); for example, about 12 hours at 50% success for a February 2026 model, but about 70 minutes at 80%.
- **RE-Bench.** On seven open-ended ML research-engineering tasks, the best agents scored 4× higher than human experts with 2 hours each. Humans scored 2× higher with 32 hours. One agent "wrote a faster custom Triton kernel than any of our human experts" (Wijk et al., 2024).
- **PaperBench.** Agents asked to replicate 20 ICML 2024 papers from scratch reached an average replication score of 21% at best, graded against author-approved rubrics, and did not outperform ML PhDs on a subset (Starace et al., 2025).
- **KernelBench.** Frontier models matched the PyTorch baseline on fewer than 20% of 250 kernel tasks at release (Ouyang et al., 2025).
- **Autonomous experiment loops.** Karpathy's autoresearch (March 2026) lets an agent edit a training script, train for 5 minutes, and keep or discard each change overnight. Two entries on nanochat's "time-to-GPT-2" leaderboard are credited to autoresearch rounds (repository READMEs).

**Automated optimisers also game their goals.** In February 2025 Sakana AI withdrew claims of up to 100× training speed-ups after its system was found to have exploited its evaluation code (TechCrunch). In Anthropic's experiments, models that learned to reward-hack production coding environments generalised to broader misalignment (MacDiarmid et al., 2025).

**What is automated, augmented and growing** (from the [DLR market page](../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md)):
- **Mostly automated:** boilerplate model code, data loaders, plotting and experiment configuration.
- **Augmented:** implementing methods from papers, evaluation harnesses, debugging shapes and numerics, and kernel writing with careful testing.
- **Growing in value:** research taste, experimental rigour, scaling and systems knowledge, evaluation science, and interpretability and alignment research.

The AI Index 2026 cites "learning penalties" for engineers who leaned heavily on AI while learning. That is why every course here has AI-off drills and exams.

**Analysis.** When experiments are cheap and agents run them, the bottleneck moves to choosing the right question, designing comparisons that cannot fool you, and catching invalid "wins" (leakage, seed noise, evaluation exploits). This major trains those skills explicitly: tuning parity in DLR304, verifier and reward-hacking audits in DLR401 and DLR403, adversarial kernel testing in DLR404, and claim audits in DLR501.

## 3. The 5-year path

### Years 1–2: common core (what matters most for this major)

Every student takes the full common core ([CATALOG](../../CATALOG.md)). These courses carry the most weight for deep learning:

| Course | Why it matters here |
|---|---|
| [FND101](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md) Programming I | Python fluency is assumed in every DLR course |
| [FND113](../../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md) Linear Algebra and Calculus | Matrices, gradients and the chain rule are the language of the field |
| [FND116](../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) Probability and Statistics I | Likelihoods, sampling, confidence intervals for every experiment |
| [CS202](../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md) Architecture and C | Memory hierarchies and C prepare you for GPUs and kernels (DLR404) |
| [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) Software Engineering I | Testing and code review for research code |
| [CS206](../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md) Mathematics for ML | **Entry requirement.** Matrix calculus, autodiff, information theory, optimisation |
| [CS212](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) Distributed Systems I | Foundations for multi-GPU training |
| [CS214](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) ML Foundations | **Entry requirement.** Generalisation, evaluation, first neural networks |

### Years 3–5: the major

| Semester | Major courses | Shared and other courses |
|---|---|---|
| 5 (Year 3) | [DLR301](year_3/DLR301_neural_networks_from_scratch_autograd/README.md) Neural Networks from Scratch · [DLR302](year_3/DLR302_computer_vision_from_cnns_to_vision_transformers/README.md) Computer Vision · [DLR303](year_3/DLR303_sequence_models_and_transformers/README.md) Sequence Models and Transformers | [PRO301](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) Ethics, Law and Responsible AI; one elective |
| 6 (Year 3) | [DLR304](year_3/DLR304_training_deep_networks_optimization/README.md) Training Deep Networks · [DLR305](year_3/DLR305_generative_models_vaes_gans_and_diffusion/README.md) Generative Models | [CAR301](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) Career Lab I; electives |
| 7 (Year 4) | [DLR401](year_4/DLR401_large_language_models_pretraining_fine_tuning/README.md) Large Language Models · [DLR402](year_4/DLR402_multimodal_models/README.md) Multimodal Models | [IND401](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) Industry Co-op Studio; overlap course A |
| 8 (Year 4) | [DLR403](year_4/DLR403_reinforcement_learning_including_rl_for_language/README.md) Reinforcement Learning · [DLR404](year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md) Efficient DL and GPU Programming | [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) Career Lab II; overlap course B |
| 9 (Year 5) | [DLR501](year_5/DLR501_frontier_seminar_interpretability_reasoning/README.md) Frontier Seminar: Interpretability, Reasoning Models and Scaling | [RES501](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) Research Methods · [RES502](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) Reproducing Papers · [THS501](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) Thesis I |
| 10 (Year 5) | — | [THS502](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) Thesis II · [LCH502](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) Career Launch and Founder Studio; elective |

**Order notes.** The catalogue lists DLR301 as DLR401's prerequisite, DLR302 for DLR402, DLR303 for DLR403 and DLR304 for DLR404. In practice, DLR401 also draws heavily on DLR303 and DLR304, and DLR403's language-model chapters assume DLR401. Taking the courses in the semester order above covers this.

## 4. Skill map by level

| Level | You can | Built in | Evidence you can show |
|---|---|---|---|
| L0 | Run a notebook that trains a small network; follow a tutorial | FND101, CS214 | A reproduced tutorial with your own notes |
| L1 | Derive backprop for an MLP; train and evaluate a CNN or small transformer; explain each training choice | CS206, CS214, DLR301 | DLR301 P1–P2 |
| L2 (intern-ready) | Implement architectures from papers; fine-tune pretrained models; debug training runs; read PyTorch and Hugging Face code | DLR301–303 | Your autograd framework (DLR301 P3), a GPT trained from scratch (DLR303 P2) |
| L3 (job-ready) | Run fair experiments with seeds and CIs; train generative and multimodal models; post-train an LLM with SFT, preference methods and RLVR; profile and fix performance | DLR304–305, DLR401–402 | Optimizer bake-off (DLR304 P2), reasoning model with verifiable rewards (DLR401 P3) |
| L4 (expert, hard to replace) | Design training recipes and evaluations others rely on; write and audit GPU kernels; secure RL against reward hacking; lead a project end to end | DLR403–404, IND401 | FlashAttention-style kernel (DLR404 P3), RL-with-hacking-audit (DLR403 P3), flagship project |
| L5 (research) | Reproduce, extend and publish; review others' work; set a research agenda | DLR501, RES501–502, THS501–502 | Workshop paper (DLR501 P3), thesis, public reproductions |

## 5. Recommended overlaps and electives

**Overlaps** (Year 4; pick one):
- [OV11 AI for Science and Research Engineering](../../04_overlaps/OV11_ai_for_science_research_engineering/README.md): for those drawn to weather, materials, biology or Earth observation. Built on DLR304, [DSC301](../data_science/year_3/DSC301_statistical_inference_and_modeling/README.md) and [MLE501](../machine_learning_engineering/year_5/MLE501_frontier_seminar_ml_research_engineering/README.md); take DSC301 as a Year 3 elective.
- [OV04 MLOps and ML Platform Engineering](../../04_overlaps/OV04_mlops_ml_platform/README.md): for training-infrastructure and inference-platform roles. Built on [MLE401](../machine_learning_engineering/year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md), [OPS401](../devops_sre_platform_engineering/year_4/OPS401_platform_engineering_and_internal_developer/README.md) and [CLD404](../cloud_engineering/year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md).
- [OV05 AI Security and Safety Engineering](../../04_overlaps/OV05_ai_security_safety/README.md): for alignment, evaluation and red-teaming roles. Built on [AIE305](../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md), [OFF403](../ethical_hacking_offensive_security/year_4/OFF403_ai_and_llm_red_teaming/README.md) and [SAR403](../security_architecture/year_4/SAR403_security_architecture_for_ai_systems_and_agents/README.md); pairs naturally with DLR403 and DLR501.

**Electives** (Years 3–5):

| Elective | Why |
|---|---|
| [DSC301](../data_science/year_3/DSC301_statistical_inference_and_modeling/README.md) Statistical Inference and Modeling; [DSC304](../data_science/year_3/DSC304_experimental_design_and_causal_inference/README.md) Experimental Design | Rigour in experiments and evaluation |
| [MLE402](../machine_learning_engineering/year_4/MLE402_distributed_training_and_large_scale_ml/README.md) Distributed Training | Tensor, pipeline and expert parallelism at cluster scale |
| [MLE404](../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md) Efficient Inference | Production inference toolchains after DLR404 |
| [MLE304](../machine_learning_engineering/year_3/MLE304_model_evaluation_fairness_and_robustness/README.md) Evaluation, Fairness and Robustness; [AIE305](../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md) Evaluating LLM Systems | Evaluation science from the product side |
| [SWE305](../software_engineering/year_3/SWE305_concurrency_and_performance_engineering/README.md) Concurrency and Performance Engineering | CPU-side performance and concurrency for data pipelines |
| [CLD404](../cloud_engineering/year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md) AI Infrastructure in the Cloud | Renting and running GPU clusters |
| [EMB401](../embedded_systems_iot/year_4/EMB401_edge_ai_and_tinyml/README.md) Edge AI and TinyML | Small models on devices |
| [CSG301](../computer_science_general/year_3/CSG301_advanced_algorithms/README.md) Advanced Algorithms | Theory depth for research careers |

## 6. Flagship industry project

The major's flagship project is specified in [DLR industry project](../../06_career_and_market_readiness/05_industry_projects/DLR_deep_learning.md). It brings the whole loop together: data, training, post-training, evaluation, an efficiency pass, a model card and a public write-up. It builds directly on the L3 projects of DLR401 (reasoning model with verifiable rewards), DLR403 (RL with a reward-hacking audit) and DLR404 (FlashAttention-style kernel). Do it in IND401 or alongside THS501.

## 7. Certifications (optional, honest value note)

No certification is required, and for this major portfolios and papers count for far more. The market page reports that industry research loops screen on "publications, open-source work or reproduced papers" ([DLR market page](../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md)). The evidence that moves a hiring manager is a reproduced paper with honest numbers, a merged pull request to PyTorch, Hugging Face TRL or Transformers, vLLM or TransformerLens, a speedrun or leaderboard entry with ablations, or a workshop paper.

If an employer or visa process values certificates, NVIDIA offers associate- and professional-level certifications, including Generative AI LLMs and Generative AI Multimodal (https://www.nvidia.com/en-us/learn/certification/), and Deep Learning Institute courses (https://www.nvidia.com/en-us/training/). They are reasonable structured refreshers. They do not test research or experimental judgement. Cloud ML certifications suit the ML Engineering major better.

## 8. The interview loop

A typical loop for industry research roles, which varies widely ([DLR market page](../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md)):
1. A screen on publications, open-source work or reproduced papers.
2. A practical coding round, sometimes DSA.
3. Deep learning fundamentals: backpropagation, attention, normalisation, optimisation and scaling.
4. An implementation exercise: implement or debug a model component under time pressure.
5. A research discussion or job talk.
6. Behavioural questions and team matching.

| Stage | Prepare with |
|---|---|
| Coding and DSA | [CS201](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md), CAR301 |
| Fundamentals | Interview questions at the end of every DLR course README |
| Implementation | DLR301 mastery gate (autograd from scratch), DLR303 (attention with KV cache from memory), DLR404 (Triton kernel) |
| Research talk | DLR501 presentations and P3 paper; THS501 |
| AI-assisted formats | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) and CAR401 |

## 9. Fast track for working professionals

Budget 15–20 hours a week. Do every mastery gate; skip nothing marked "AI off".

- **Software engineers (strong code, rusty maths), about 9 months.**
  1. CS206 Chapters 1–6 and 11 (linear algebra, matrix calculus, autodiff, optimisation).
  2. DLR301, then DLR303, then DLR304.
  3. DLR401, then DLR404 (or DLR403 for post-training roles).
  4. Portfolio: DLR301 P3, DLR303 P2, DLR304 P3, and DLR401 P3 or DLR404 P3.
- **ML engineers and data scientists, about 6 months.** Test out of DLR301 with its mastery gate. Then take DLR303, DLR304, DLR401, and DLR403 or DLR404 depending on the target role, plus DLR501's reproduction labs.
- **Physics, mathematics and engineering graduates, about 9–12 months.** Start with FND104 (tools) and CS205 (testing), then DLR301, DLR302 and DLR304, then OV11 for AI-for-science roles.

## 10. Into research labs and a PhD

- **Build a public record early.** Do reproductions (DLR501 P1, RES502), contribute open source, enter speedruns or leaderboards with full ablations, and write a workshop paper (DLR501 P3). Research-engineer roles "more often hire strong engineers without a PhD who can implement, scale and debug experiments", while many research-scientist roles expect a PhD or publication record ([DLR market page](../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md)).
- **Pre-doctoral and fellowship programmes** (check each for current eligibility and deadlines):
  - Microsoft Research India Research Fellows — https://www.microsoft.com/en-us/research/academic-program/research-fellows-program-at-microsoft-research-india/
  - MATS — https://www.matsprogram.org/
  - Anthropic Fellows Program for AI safety research — https://alignment.anthropic.com/2025/anthropic-fellows-program-2026/
  - Cohere Labs Scholars — https://cohere.com/research/scholars-program
- **PhD funding.** The Prime Minister's Research Fellowship for PhDs in India — https://pmrf.in/ ; Google PhD Fellowship — https://research.google/programs-and-events/phd-fellowship/
- **Compute for research.** Google's TPU Research Cloud (by application) — https://sites.research.google/trc/about/. The IndiaAI Mission compute portal offers subsidised GPU access for eligible institutions, researchers and startups (student eligibility unconfirmed) — https://indiaai.gov.in/
- **Choosing advisers and labs.** Read a lab's last three papers and their code before writing. Then send a short email that reproduces or extends one result. This is the most persuasive application.
- **Market context.** New AI PhDs in the US and Canada rose 22% from 2022 to 2024, but that increase went into academia, not industry. India had the largest net outflow of AI research authors and inventors of any country in 2025 (AI Index 2026). **Analysis:** strong researchers who build careers in India face less competition for the same work.

## Sources

- DLR market page (all role, demand, pay and loop facts, with their own dated sources) — [../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md](../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md) (checked 2026-10)
- Stanford HAI, *AI Index Report 2026* — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf (checked 2026-10)
- METR, time horizons — https://metr.org/time-horizons/ ; Kwa et al., "Measuring AI Ability to Complete Long Software Tasks" (2025) — https://arxiv.org/abs/2503.14499 (checked 2026-10)
- Wijk et al., "RE-Bench" (2024) — https://arxiv.org/abs/2411.15114 (checked 2026-10)
- Starace et al., "PaperBench" (2025) — https://arxiv.org/abs/2504.01848 (checked 2026-10)
- Ouyang et al., "KernelBench" (2025) — https://arxiv.org/abs/2502.10517 (checked 2026-10)
- Karpathy, autoresearch — https://github.com/karpathy/autoresearch ; nanochat leaderboard — https://github.com/karpathy/nanochat (checked 2026-10)
- TechCrunch, "Sakana walks back claims that its AI can dramatically speed up model training" (21 Feb 2025) — https://techcrunch.com/2025/02/21/sakana-walks-back-claims-that-its-ai-can-dramatically-speed-up-model-training/ (checked 2026-10)
- MacDiarmid et al., "Natural Emergent Misalignment from Reward Hacking in Production RL" (2025) — https://arxiv.org/abs/2511.18397 (checked 2026-10)
- NVIDIA certification programmes — https://www.nvidia.com/en-us/learn/certification/ (checked 2026-10)

_Last reviewed: 2026-10_
