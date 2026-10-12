# DSC501 · Frontier Seminar: Bayesian Methods, Causal ML and AI-Assisted Science

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [DSC401](../../year_4/DSC401_time_series_analysis_and_forecasting/README.md), [DSC403](../../year_4/DSC403_recommender_systems_and_personalization/README.md) (builds directly on [DSC301](../../year_3/DSC301_statistical_inference_and_modeling/README.md) and [DSC304](../../year_3/DSC304_experimental_design_and_causal_inference/README.md)) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) (taken alongside), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

Part of the [Data Science major](../../README.md). A seminar: each week pairs two or three papers with a hands-on replication sprint. Students present papers, critique them and extend one result into a research-grade project.

## Why this course matters now

Three research fronts are changing what a senior data scientist does. **Bayesian workflow** has matured from "fit a model" into a disciplined loop of prior checks, computation diagnostics, model comparison and criticism (Gelman et al., 2020), supported by PyMC, Stan and NumPyro. **Causal machine learning** combines flexible prediction with valid inference: double/debiased machine learning (Chernozhukov et al., 2018) and generalized random forests (Wager and Athey, 2018; Athey, Tibshirani and Wager, 2019) estimate effects and their heterogeneity with confidence intervals, and policy-learning methods turn them into targeting rules. **AI-assisted science** is moving fast: Google's AI co-scientist (February 2025) is a multi-agent system built with Gemini 2.0 to generate hypotheses and research proposals; the AI Scientist-v2 (April 2025) submitted three fully autonomous papers to an ICLR workshop and one scored above the average human acceptance threshold; on MLE-bench the best agents medal in about 64% of Kaggle competitions. Yet on DiscoveryBench, a 2024 benchmark of 264 data-driven discovery tasks from published papers, the best system scored only 25%, and BLADE found models "often limited to basic analyses". Meanwhile, LLM-generated labels and "silicon samples" of simulated survey respondents (Argyle et al., 2023) raise new questions about valid inference. The researcher who can tell a real finding from a well-written artefact, with or without AI help, is the one who will matter.

## Learning outcomes

By the end you can:

1. **Run** a full Bayesian workflow (prior predictive checks, simulation-based calibration, HMC diagnostics, posterior predictive checks, LOO model comparison) and **report** it to publication standard.
2. **Fit** hierarchical models at scale in PyMC, Stan (CmdStanPy or brms) and NumPyro, and **diagnose** and fix computational problems such as divergences with reparameterisation.
3. **Derive and implement** double/debiased machine learning with cross-fitting, and **explain** Neyman orthogonality and when DML fails.
4. **Estimate and evaluate** heterogeneous treatment effects with causal forests and meta-learners, and **learn** a treatment policy with valid evaluation (RATE, policy value).
5. **Apply** conformal and prediction-powered methods for distribution-free uncertainty, including for counterfactuals and model-generated labels.
6. **Evaluate** AI research agents and data-science agents on a benchmark you design, with measured failure modes.
7. **Read, reproduce and critique** methods papers, and **write** a paper-style report with code and data that others can rerun.

## Chapters and lessons

### Chapter 1 · The Bayesian workflow (weeks 1–2)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Workflow as a loop | Gelman et al. (2020): model building, checking, expansion and comparison as one process | Map your DSC301 P3 analysis onto the workflow and list missing steps |
| 1.2 Priors that mean something | Weakly informative priors, prior predictive simulation, units and scales | Reject two default priors by prior predictive checks |
| 1.3 Simulation-based calibration | Checking that inference recovers parameters (Talts et al., 2018) | Run SBC on a hierarchical model and interpret rank histograms |
| 1.4 Diagnostics | Rank-normalised R-hat and ESS (Vehtari et al., 2021), divergences, energy plots | Diagnose and fix a model with divergences |
| 1.5 Model comparison | PSIS-LOO and its diagnostics (Vehtari, Gelman and Gabry, 2017); stacking | Compare three models with LOO and explain Pareto-k warnings |

**Check your understanding:** (1) What does SBC test that posterior predictive checks do not? (2) Why are divergences a sign of bias, not just inefficiency? (3) When should you stack models instead of selecting one?

### Chapter 2 · Probabilistic programming in practice (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Three languages | PyMC, Stan (via CmdStanPy or brms) and NumPyro (JAX): model syntax, samplers, speed | Write one hierarchical model in all three and compare run times |
| 2.2 Reparameterisation | Centred vs non-centred parameterisations; funnels | Remove a funnel with a non-centred parameterisation |
| 2.3 Scaling up | Variational inference and its failure modes; GPU sampling with JAX; when approximations are acceptable | Compare ADVI and NUTS posteriors on the same model |
| 2.4 Reporting | ArviZ summaries, plots and a reproducible appendix | Produce a publication-style appendix |

**Check your understanding:** (1) Why can a variational posterior be confidently wrong? (2) What does a funnel look like in a trace? (3) What must a Bayesian appendix contain for replication?

### Chapter 3 · Hierarchical models for decisions (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Many groups | Partial pooling for thousands of SKUs, stores or districts | Fit a hierarchical demand model over a DSC401 hierarchy |
| 3.2 MRP | Multilevel regression and post-stratification for survey estimates | Estimate a state-level quantity from a non-representative sample |
| 3.3 Bayesian experimentation | Hierarchical shrinkage across many A/B tests; decision rules with expected loss | Re-analyse 50 simulated experiments with shrinkage |
| 3.4 Marketing mix models | Bayesian MMM with adstock and saturation (Google's Meridian, PyMC-Marketing); priors from experiments; identifiability limits | Fit a small MMM on simulated data and show which effects it cannot identify |

**Check your understanding:** (1) Why does shrinkage reduce false "wins" across many experiments? (2) What does MRP need to be true about the post-stratification table? (3) How does an expected-loss rule differ from a significance rule?

### Chapter 4 · Double/debiased machine learning (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The problem | Regularisation bias when ML estimates nuisance functions; why naive plug-in fails | Simulate plug-in bias in a partially linear model |
| 4.2 Orthogonality and cross-fitting | Neyman-orthogonal scores, sample splitting, valid confidence intervals (Chernozhukov et al., 2018) | Implement DML from scratch and match the DoubleML package |
| 4.3 Applications | Partially linear, interactive and IV models; the 401(k) eligibility example | Replicate the 401(k) analysis with DoubleML |
| 4.4 When DML fails | Poor overlap, weak nuisance models, unmeasured confounding; sensitivity analysis | Break DML with limited overlap and show the interval |

**Check your understanding:** (1) Why does cross-fitting matter even with a good learner? (2) What does orthogonality buy you? (3) Which assumption does DML not relax?

### Chapter 5 · Heterogeneous effects and policy learning (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Causal forests | Honest trees, local moment equations, confidence intervals (Wager and Athey, 2018; GRF) | Fit a causal forest with `grf` or EconML on an experiment |
| 5.2 Meta-learners revisited | S-, T-, X-, R- and DR-learners; when each works | Compare five learners on semi-synthetic data with known effects |
| 5.3 Evaluating CATE models | Rank-weighted average treatment effect (Yadlowsky et al.); calibration tests | Compute RATE for two CATE models |
| 5.4 Policy learning | Learning treatment rules with doubly robust scores (Athey and Wager, 2021); budgets | Learn and evaluate a budget-constrained policy on DSC304 P2 data |

**Check your understanding:** (1) Why can't you validate CATE predictions with ordinary accuracy? (2) What does "honest" mean in a causal tree? (3) Why might the best policy ignore the largest predicted effects?

### Chapter 6 · Distribution-free uncertainty (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Conformal prediction | Split conformal, conformalised quantile regression, coverage guarantees and their assumptions | Add conformal intervals to a DSC401 forecaster and test coverage under shift |
| 6.2 Conformal for counterfactuals | Intervals for individual treatment effects (Lei and Candès, 2021) | Build counterfactual intervals on an experiment |
| 6.3 Prediction-powered inference and its extensions | Valid inference with ML predictions plus a small labelled set | Apply PPI to a regression coefficient |
| 6.4 Calibration and sharpness | Evaluating predictive distributions with proper scoring rules; Bayesian vs conformal intervals | Compare the calibration and width of Bayesian and conformal intervals on one forecaster |

**Check your understanding:** (1) What does conformal coverage not guarantee? (2) Why are individual treatment-effect intervals so wide? (3) When does PPI give no gain over the labelled data alone?

### Chapter 7 · Long-term effects, surrogates and transportability (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Surrogate indices | Estimating long-term effects from short-term outcomes (Athey et al.) | Build a surrogate index for long-term retention in simulation |
| 7.2 Transportability | Generalising experiment results to new populations | Re-weight an experiment to a different city's population |
| 7.3 Interference revisited | Recent designs for networks and marketplaces | Present one recent paper and its assumptions |
| 7.4 Combining experiments and observational data | Using a small RCT with a large observational dataset for precision or generalisation; what each source must assume | Replicate the simulation study of one recent paper on data fusion |

**Check your understanding:** (1) What must be true for a surrogate index to be valid? (2) Why might an effect in Bengaluru not transport to Patna? (3) Which interference assumption is hardest to test?

### Chapter 8 · AI-assisted science and data-science agents (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Research agents | AI co-scientist (2025), the AI Scientist and AI Scientist-v2; what they automate and how they were evaluated | Critique one system's evaluation design |
| 8.2 Benchmarks for analysis | MLE-bench, DSBench, BLADE, DiscoveryBench: task design, scoring, contamination | Design five benchmark tasks from your own past projects |
| 8.3 Running agents on your tasks | Agent scaffolds, budgets, logging, failure taxonomies | Run two agents on your tasks and classify every failure |
| 8.4 Analytic flexibility and multiverses | Many analysts (Silberzahn et al., 2018); multiverse analysis; agents as forking-path generators | Run a 100-specification multiverse with an agent and summarise honestly |

**Check your understanding:** (1) Why is "passed peer review at a workshop" weak evidence of scientific value? (2) What makes an analysis task hard to score automatically? (3) How should a team report results when an agent explored hundreds of specifications?

### Chapter 9 · Inference with AI-generated data (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Model labels as measurements | Measurement error, PPI and design-based supervised learning (Egami et al.) | Compare naive and corrected estimates on DSC402 P3 data |
| 9.2 Silicon samples | LLMs simulating survey respondents (Argyle et al., 2023); validity questions | Compare LLM-simulated answers with real survey margins and discuss |
| 9.3 Synthetic data | Synthetic tabular data for privacy and augmentation; what inference it supports | Fit the same model on real and synthetic data and compare intervals |
| 9.4 Disclosing AI use in analyses | What to report: tools, prompts, explored specifications, verification steps | Write the AI-use disclosure for your P3 |

**Check your understanding:** (1) What can simulated respondents not tell you? (2) Why can synthetic data give misleadingly narrow intervals? (3) When is a model label acceptable as a measurement?

### Chapter 10 · Open problems and research practice (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Open problems | Causal discovery reliability; uncertainty in foundation models for tables and time series; valid inference after agentic exploration; long-term and network effects | Write a two-page research proposal on one open problem |
| 10.2 Reproducibility | Pre-registration, open code and data, computational reproducibility checks | Have a classmate reproduce your P3 results from scratch |
| 10.3 Writing and reviewing | Paper structure, related work, honest limitations; reviewing to conference standards | Review two classmates' P3 papers |
| 10.4 Research careers | PhD programmes, research engineering, applied science and policy research: what each values and how to show it | Map your P3 to two target roles and list the evidence each expects |

**Check your understanding:** (1) Which open problem matters most for your intended career, and why? (2) What would make your P3 result fail to replicate? (3) What makes a review useful to authors?

## Weekly rhythm

| Week | Chapter | Papers and sprint | Deliverable |
|---|---|---|---|
| 1 | 1 | Bayesian workflow; SBC | Paper presentation 1 |
| 2 | 1–2 | R-hat, LOO; PyMC/Stan/NumPyro sprint | — |
| 3 | 2 | Reparameterisation and VI | **P1 due** |
| 4 | 3 | MRP; Bayesian experimentation | — |
| 5 | 4 | DML from scratch | — |
| 6 | 4–5 | 401(k) replication; causal forests | — |
| 7 | 5 | RATE; policy learning | **P2 due** |
| 8 | 6 | Conformal, counterfactual intervals, PPI | P3 proposal |
| 9 | 7 | Surrogates and transportability | — |
| 10 | 8 | Research agents and benchmarks | — |
| 11 | 8 | Agent evaluation sprint; multiverse | — |
| 12 | 9 | AI-generated data and inference | P3 draft |
| 13 | 10 | Open problems; reproduction swap | — |
| 14 | 10 | Peer review | **P3 due** |
| 15 | Review | Seminar conference: P3 talks | Oral examination |

## Working with AI in this course

- **Use AI for:** literature search and paper summaries (always checked against the paper); translating models between PyMC, Stan and NumPyro; scaffolding simulations; running agents as objects of study; editing prose. Claude, ChatGPT, Gemini (including Deep Research modes), Claude Code and GitHub Copilot are all appropriate.
- **Do without AI (drills):** derivations (orthogonal scores, IPW and DR estimators, conformal coverage); reading diagnostics; the oral examination; peer reviews (written by you, then optionally compared with an AI review).
- **Verify AI output by:** (1) SBC or fake-data recovery for every new model; (2) checking every cited paper exists and says what is claimed, with page or section; (3) reproducing agent results from logs; (4) comparing at least two estimators with different assumptions.
- **Where AI still fails here:** published benchmarks put open-ended discovery far below closed tasks (DiscoveryBench best system 25% in 2024; MLE-bench medals about 64% by February 2026). Chapter 8 makes measuring this your job: you will build a small benchmark from your own projects and publish a failure taxonomy for at least two agents.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Paper presentations and critiques (3) | 15% |
| Replication sprints (weekly) | 15% |
| Projects P1–P3 | 50% |
| Peer reviews | 5% |
| Oral examination | 15% |

**Mastery gate.** You pass when you can: (1) reproduce a published methods result from its description and code, and explain any discrepancy; (2) take an unseen causal or Bayesian problem from question to a defensible estimate with full diagnostics, AI off for the design and derivations; (3) present a research-grade P3 that a classmate reproduces from scratch and that would be credible as a workshop submission or preprint.

## Industry reality

Bayesian hierarchical models are used where data are sparse across many groups, such as experimentation, marketing measurement and forecasting; open-source tools such as PyMC, Stan and NumPyro are maintained by active communities with industry users. Causal ML is used for targeting and personalization, and its main libraries (EconML from Microsoft Research's ALICE project, now under PyWhy; DoubleML; GRF) are open source. AI research agents are an active area at Google, Sakana AI and many labs; their evaluation is unsettled, which is why this seminar treats them as objects of study as well as tools.

**Interview questions from this course** (research and senior data scientist roles)

1. *Your Bayesian model shows divergences. What do you do?* Strong answer: treats them as a sign of biased inference; checks geometry (funnels), reparameterises (non-centred), tightens priors with prior predictive checks, increases adapt delta only as a diagnostic; confirms with SBC.
2. *Explain double machine learning to an engineer.* Strong answer: predict outcome and treatment from controls with any ML model, use residuals from out-of-fold predictions, regress residual on residual; orthogonality removes first-order bias from nuisance errors; cross-fitting avoids overfitting bias; confounding assumptions remain.
3. *How would you decide whom to target with a costly retention offer?* Strong answer: randomised data if possible; CATE with causal forests or DR-learners; evaluate with RATE or policy value on held-out data; budget constraint; monitor and re-test.
4. *An AI agent produced an analysis with a striking result. How do you evaluate it?* Strong answer: reproduce from logs; check how many specifications were explored; pre-registered confirmation on new data; inspect data handling; sensitivity analysis; treat as a hypothesis until confirmed.
5. *Can we replace a survey with LLM-simulated respondents?* Strong answer: explains what silicon samples can and cannot represent; validation against real margins and subgroups; risk of stereotypes; possible use for questionnaire piloting, not for estimates; legal and ethical constraints.

## Resources (free first)

- **Texts:** Gelman et al., *Bayesian Data Analysis*, 3rd ed. (free PDF) — https://sites.stat.columbia.edu/gelman/book/ ; Gelman et al., "Bayesian Workflow" — https://arxiv.org/abs/2011.01808 ; Chernozhukov et al., *Applied Causal Inference Powered by ML and AI* — https://causalml-book.org/ ; Statistical Rethinking 2025 lectures — https://github.com/rmcelreath/stat_rethinking_2025 ; Angelopoulos and Bates, conformal prediction — https://arxiv.org/abs/2107.07511
- **Software:** PyMC — https://www.pymc.io/ ; Stan — https://mc-stan.org/ ; CmdStanPy — https://mc-stan.org/cmdstanpy/ ; brms — https://paulbuerkner.com/brms/ ; NumPyro — https://num.pyro.ai/ ; ArviZ — https://python.arviz.org/ ; DoubleML — https://docs.doubleml.org/ ; EconML — https://github.com/py-why/EconML ; GRF — https://grf-labs.github.io/grf/ ; Meridian (Bayesian MMM) — https://github.com/google/meridian ; PyMC-Marketing — https://github.com/pymc-labs/pymc-marketing
- **Bayesian papers:** Talts et al., SBC — https://arxiv.org/abs/1804.06788 ; Vehtari et al., R-hat — https://arxiv.org/abs/1903.08008 ; Vehtari, Gelman and Gabry, LOO — https://arxiv.org/abs/1507.04544
- **Causal ML papers:** Chernozhukov et al., DML — https://arxiv.org/abs/1608.00060 ; Wager and Athey — https://doi.org/10.1080/01621459.2017.1319839 ; Athey, Tibshirani and Wager, GRF — https://doi.org/10.1214/18-AOS1709 ; Künzel et al. — https://doi.org/10.1073/pnas.1804597116 ; Athey and Wager, policy learning — https://doi.org/10.3982/ECTA15732 ; Yadlowsky et al., RATE — https://arxiv.org/abs/2111.07966 ; Lei and Candès — https://arxiv.org/abs/2006.06138 ; Athey et al., surrogate index — https://arxiv.org/abs/1603.09326
- **AI-assisted science:** Google AI co-scientist — https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/ ; Lu et al., The AI Scientist — https://arxiv.org/abs/2408.06292 ; Yamada et al., The AI Scientist-v2 — https://arxiv.org/abs/2504.08066 ; MLE-bench — https://github.com/openai/mle-bench ; BLADE — https://arxiv.org/abs/2408.09667 ; DiscoveryBench — https://arxiv.org/abs/2407.01725 ; Argyle et al., silicon samples — https://doi.org/10.1017/pan.2023.2 ; Egami et al. — https://arxiv.org/abs/2306.04746
- **Data:** DoubleML 401(k) data — https://docs.doubleml.org/stable/api/generated/doubleml.datasets.fetch_401K.html ; Criteo Uplift — https://ai.criteo.com/criteo-uplift-prediction-dataset/ ; NFHS-5 (DHS) — https://dhsprogram.com/methodology/survey/survey-display-541.cfm

## Sources

- Gelman et al., "Bayesian Workflow" (arXiv 2011.01808, 2020) — https://arxiv.org/abs/2011.01808 (checked 2026-10)
- Chernozhukov et al., "Double/debiased machine learning", *The Econometrics Journal* (2018) — https://doi.org/10.1111/ectj.12097 (checked 2026-10)
- Wager and Athey, *JASA* (2018) — https://doi.org/10.1080/01621459.2017.1319839 ; Athey, Tibshirani and Wager, *Annals of Statistics* (2019) — https://doi.org/10.1214/18-AOS1709 ; Athey and Wager, *Econometrica* (2021) — https://doi.org/10.3982/ECTA15732 (checked 2026-10)
- Google Research blog, "Accelerating scientific breakthroughs with an AI co-scientist" (19 Feb 2025) — https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/ (checked 2026-10)
- Yamada et al., "The AI Scientist-v2" (arXiv 2504.08066, Apr 2025) — https://arxiv.org/abs/2504.08066 (checked 2026-10)
- OpenAI, MLE-bench leaderboard (top main-leaderboard entry 64.44%, Feb 2026; submissions paused Apr 2026) — https://github.com/openai/mle-bench (checked 2026-10)
- Majumder et al., "DiscoveryBench" (arXiv 2407.01725, 2024) — https://arxiv.org/abs/2407.01725 ; Gu et al., "BLADE" (arXiv 2408.09667, 2024) — https://arxiv.org/abs/2408.09667 (checked 2026-10)
- Argyle et al., "Out of One, Many", *Political Analysis* (2023) — https://doi.org/10.1017/pan.2023.2 (checked 2026-10)
- Silberzahn et al., "Many Analysts, One Data Set" (2018) — https://doi.org/10.1177/2515245917747646 (checked 2026-10)
- PyPI release pages (PyMC 6.3, NumPyro 0.22, ArviZ 1.3, DoubleML 0.11, EconML 0.17; Jul–Sep 2026) — https://pypi.org/ (checked 2026-10)

_Last reviewed: 2026-10_
