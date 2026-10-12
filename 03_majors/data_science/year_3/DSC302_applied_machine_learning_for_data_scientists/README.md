# DSC302 · Applied Machine Learning for Data Scientists

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | [DSC402](../../year_4/DSC402_nlp_and_text_analytics_with_llms/README.md), [DSC305](../DSC305_feature_engineering_and_model_evaluation/README.md), [DSC404](../../year_4/DSC404_data_science_in_production_deployment_monitoring/README.md), [OV10B](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10B_fraud_detection_and_risk_systems/README.md) |

Part of the [Data Science major](../../README.md). CS214 taught how the algorithms work. This course teaches how a data scientist uses them to change a decision: framing, baselines, validation that matches reality, interpretation with its limits, and communication. ML systems engineering is covered in the MLE major ([MLE302](../../../machine_learning_engineering/year_3/MLE302_machine_learning_system_design/README.md), [MLE305](../../../machine_learning_engineering/year_3/MLE305_applied_ml_tabular_vision_and_text/README.md)).

## Why this course matters now

Fitting a good model to a well-posed problem is becoming a commodity. On OpenAI's MLE-bench (75 Kaggle competitions, 24 hours per attempt), the best AI agent earned a medal in 16.9% of competitions in October 2024 and the top leaderboard entry reached 64.4% by February 2026. Yet in industry the hard part is rarely the fit. Booking.com analysed about 150 customer-facing models, all validated in randomized controlled trials, and concluded that an iterative, hypothesis-driven process integrated with other disciplines was what made them succeed; one of its lessons is that offline model performance did not reliably predict business gains (Bernardi et al., KDD 2019). In science, Kapoor and Narayanan (2023) found data leakage in 17 fields, affecting 294 papers, sometimes with "wildly overoptimistic conclusions". AutoGluon, TabPFN, the Data Science Agent in Colab and coding agents such as Claude Code and GitHub Copilot will produce a tuned model on request. They will not decide what the label should be, when the prediction is made, which split mimics deployment, what an error costs, or whether a SHAP plot is being read as causation. That is this course.

## Learning outcomes

By the end you can:

1. **Frame** a business question as a prediction task with a decision, an action, a unit, a horizon and a cost of errors, or **argue** that it is not a prediction problem.
2. **Build** a baseline ladder (rule, linear, boosted trees, AutoML/TabPFN) and **report** gains with uncertainty.
3. **Design** validation that mirrors deployment (time, group, entity splits; nested CV) and **estimate** how much a CV score can be trusted.
4. **Find and quantify** leakage in a pipeline, including leakage through label definitions and selection.
5. **Tune** gradient-boosted trees within a fixed budget, using monotone constraints and categorical handling where they help.
6. **Turn** scores into decisions with cost-based thresholds, capacity constraints and decision curves.
7. **Explain** a model with permutation importance, partial dependence, ALE and SHAP, and **demonstrate** where each misleads.
8. **Run** slice-based error analysis with confidence intervals, including fairness metrics.
9. **Audit** an AutoML or agent-generated pipeline and **write** a modelling memo and model card a stakeholder can act on.

## Chapters and lessons

### Chapter 1 · From question to prediction task (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Decision first | Who acts on the prediction, what they do, at what moment; prediction policy problems (Kleinberg et al., 2015) | Write the decision statement for five model requests |
| 1.2 Unit, label and horizon | Defining "churn", "default" or "fraud" precisely; label windows; censoring | Draft three label definitions for churn and show how the positive rate changes |
| 1.3 Prediction vs causal questions | "Who will leave?" vs "who will stay if we call them?"; when a model cannot answer the question asked | Classify ten requests as prediction, causal or descriptive |
| 1.4 When not to use ML | Rules, lookups, simple scores; cost of maintenance and explanation | Write a one-paragraph "no model needed" recommendation |

**Check your understanding:** (1) Why can a perfect churn predictor still waste a retention budget? (2) What breaks if your label uses information available only after the decision time? (3) Name one request that sounds predictive but is causal.

### Chapter 2 · Baselines and benchmarks (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 The baseline ladder | Majority class, business rule, logistic regression, GBDT, AutoML; why each rung exists | Build all rungs on the Bank Marketing data with one CV protocol |
| 2.2 Strong automatic baselines | AutoGluon presets, TabPFN for small tables (Hollmann et al., *Nature* 2025), time budgets | Run both with equal compute and compare to your GBDT |
| 2.3 Reporting gains honestly | Mean ± standard deviation across repeated CV, paired comparisons, practical vs statistical significance | Decide whether a 0.004 AUC gain is real |
| 2.4 Cost of complexity | Latency, retraining, explainability, data dependencies | Estimate the yearly maintenance cost of each rung (illustrative scenario) |

**Check your understanding:** (1) Why should an AutoML result be a baseline rather than the deliverable? (2) When is a rule better than a 2-point AUC gain? (3) How many CV repeats do you need before comparing two models?

### Chapter 3 · Validation design (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Splits that mirror deployment | Time-based, group (customer, store, patient) and entity splits; gap periods | Re-score a model under random vs time split and explain the drop |
| 3.2 What CV estimates | CV estimates average performance over training sets, not your model's; intervals for CV error (Bates, Hastie and Tibshirani, 2023) | Compare naive and nested CV intervals on a small dataset |
| 3.3 Nested CV and tuning bias | Selection on the validation set as overfitting; holdout discipline | Show optimistic bias from tuning without nesting |
| 3.4 Adversarial validation and shift | Train vs test classifiers; covariate shift between periods | Detect the features that drift between two years of data |

**Check your understanding:** (1) Your model is trained monthly. What split mimics that? (2) Why does a random split overstate performance when customers appear many times? (3) What does an adversarial-validation AUC of 0.9 tell you?

### Chapter 4 · Leakage hunting (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The leakage taxonomy | Eight types from Kapoor and Narayanan (2023): target, temporal, preprocessing, duplicates, illegitimate features and more | Classify ten real leakage reports |
| 4.2 Features from the future | Call duration in telemarketing data is known only after the call; post-outcome fields in CRM tables | Remove and quantify the leak in the Bank Marketing data |
| 4.3 Labels that leak | Label defined with the feature window; outcome-dependent sampling; selection (only approved loans have outcomes) | Show how training only on approved applicants distorts default rates |
| 4.4 Model info sheets and leak tests | Pre-deployment checklists; single-feature AUC screens; shuffled-label tests | Write a model info sheet for your P1 model |

**Check your understanding:** (1) Why is "only funded loans have labels" a leakage-like bias even with a perfect time split? (2) What does a single feature with AUC 0.99 usually mean? (3) How does a shuffled-label test catch pipeline leaks?

### Chapter 5 · Gradient-boosted trees in practice (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The parameters that matter | Learning rate and rounds with early stopping, leaves/depth, min data per leaf, subsampling, regularization | Tune LightGBM with a 50-trial Optuna budget and plot importance of hyperparameters |
| 5.2 Categoricals and missing values | Native categorical splits, CatBoost ordered target statistics, missing-value direction | Compare one-hot, native and CatBoost handling on a high-cardinality column |
| 5.3 Constraints | Monotone constraints for price, income or risk features; interaction constraints | Enforce "higher income never raises risk" and measure the cost in AUC |
| 5.4 Why trees win on tables, and when they don't | Grinsztajn et al. (2022); TabPFN and neural tabular models; small vs large data | Compare GBDT, TabPFN and an MLP on three OpenML datasets |
| 5.5 Reproducibility | Seeds, deterministic training, experiment logs (MLflow) | Show score variance from seeds alone |

**Check your understanding:** (1) Why tune the number of rounds with early stopping rather than a grid? (2) What do you lose by adding monotone constraints, and why might a regulator want them? (3) When would you expect TabPFN to beat a tuned GBDT?

### Chapter 6 · Linear and interpretable models still matter (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Regularized GLMs as strong baselines | Elastic net with splines and interactions | Match 95% of GBDT performance with a GLM on one dataset |
| 6.2 Glass-box models | Explainable Boosting Machines (InterpretML), GAMs, scorecards | Fit an EBM and read every shape function |
| 6.3 The case for interpretable models | Rudin (2019): for high-stakes decisions, prefer interpretable models over explaining black boxes | Debate: when is the accuracy cost worth paying? |
| 6.4 Scorecards in credit risk | Points-based scorecards, binning, monotonicity | Convert a logistic model into a 0–1000 point scorecard |

**Check your understanding:** (1) What does an EBM give a reviewer that SHAP on a GBDT does not? (2) When is a 1% AUC loss acceptable? (3) Why do lenders like monotone scorecards?

### Chapter 7 · From probabilities to decisions (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Expected cost and thresholds | Cost matrix; optimal threshold from costs and calibrated probabilities | Pick the threshold for a fraud team that reviews 200 cases a day |
| 7.2 Capacity constraints | Top-k targeting, precision@k, budget curves | Compare threshold rules with fixed-capacity rules |
| 7.3 Decision curves | Net benefit (Vickers and Elkin, 2006) vs "treat all" and "treat none" | Draw decision curves for two readmission models |
| 7.4 Calibration check | Reliability diagrams and Brier score as a sanity check before using probabilities (depth in DSC305) | Detect a miscalibrated model and recalibrate it |

**Check your understanding:** (1) Why can a model with a better AUC give a worse decision? (2) What changes if the review team doubles? (3) Why do you need calibrated probabilities for cost-based thresholds but not for ranking?

### Chapter 8 · Interpretability, with caveats (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Global importance | Impurity vs permutation importance; drop-column importance; correlated features splitting credit | Show permutation importance halving when a feature is duplicated |
| 8.2 Effect plots | Partial dependence, ICE, accumulated local effects (Apley and Zhu) | Find a case where PDP shows an effect that ALE does not |
| 8.3 SHAP | Shapley values, TreeSHAP (Lundberg et al.), local and global views | Explain 20 individual predictions and summarize patterns |
| 8.4 Where SHAP misleads | Interventional vs observational values, correlated features, off-manifold inputs (Kumar et al., 2020; Janzing et al., 2019); SHAP is not causal | Build a dataset where SHAP ranks a non-causal proxy first |
| 8.5 Counterfactual explanations | "What would change the decision?"; actionability and plausibility | Generate counterfactuals for three rejected applicants and judge their feasibility |

**Check your understanding:** (1) A stakeholder wants to raise a feature because its SHAP value is large. What do you say? (2) Why do correlated features make importance unstable? (3) When is a counterfactual explanation misleading?

### Chapter 9 · Error analysis, slices and fairness (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Error analysis | Confusion by segment, residual analysis, error galleries | Group 50 errors into causes and fix the largest |
| 9.2 Slice discovery with uncertainty | Metrics by segment with bootstrap intervals; small-slice noise | Report recall by state with intervals and flag only real gaps |
| 9.3 Fairness metrics | Demographic parity, equalized odds, calibration within groups; incompatibility results; Fairlearn | Audit a credit model across gender and age groups |
| 9.4 Mitigation and trade-offs | Reweighting, thresholds per group, constraints; legal context (see PRO301) | Document the accuracy–fairness trade-off for one mitigation |

**Check your understanding:** (1) Why can every slice look worse than average? (2) Why can't a model satisfy calibration and equalized odds at once in general? (3) Who decides which fairness metric applies?

### Chapter 10 · Unsupervised learning for decisions (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Segmentation that someone uses | Clustering on behaviour, stability across seeds and samples, naming segments honestly | Test whether your segments survive a bootstrap |
| 10.2 Anomaly detection evaluation | Isolation forest, robust z-scores; evaluating without labels; alert budgets | Tune an anomaly detector to a 20-alerts-a-day budget |
| 10.3 Embeddings as features | Pretrained text or image embeddings feeding tabular models (depth in DSC305, DSC402) | Add product-title embeddings to a demand model |
| 10.4 Semi-supervised and weak labels | Pseudo-labelling, label noise, cleanlab | Estimate label noise in a public dataset |

**Check your understanding:** (1) What makes a segmentation actionable? (2) How do you evaluate an anomaly detector with no labels? (3) When does pseudo-labelling hurt?

### Chapter 11 · AutoML and agents as colleagues (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 AutoML in practice | AutoGluon stacking, time budgets, what it does to your validation | Reproduce an AutoGluon leaderboard and inspect its splits |
| 11.2 Agentic modelling | What MLE-bench measures and what it leaves out (framing, label design, deployment cost) | Give an agent the P1 task and compare its pipeline with yours |
| 11.3 Auditing generated pipelines | Fit-on-all-data scalers, target encoding outside folds, test-set peeking, silent row drops | Audit three agent-generated notebooks for leaks |
| 11.4 Experiment tracking | MLflow runs, data versions, seeds; making agent work reproducible | Log every run of P2 and rebuild the best one from the log |

**Check your understanding:** (1) Why does an agent's high validation score need an independent holdout? (2) What parts of P1 could an agent not do without you? (3) How would you detect a silently dropped 10% of rows?

### Chapter 12 · Communicating models (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 The modelling memo | Decision, recommendation, evidence, risks, what would change your mind | Write the memo for P2 in two pages |
| 12.2 Model cards | Intended use, data, metrics by slice, limitations (Mitchell et al., 2019) | Write a model card for P3 |
| 12.3 Showing uncertainty | Intervals on metrics, expected range of business impact, scenario tables | Turn a CV result into a range of expected monthly savings |
| 12.4 Defending a model | Questions from risk, legal and product; answering "why did it reject me?" | Mock review panel on P3 |

**Check your understanding:** (1) What belongs on page one of a modelling memo? (2) Which limitation would you put first in a model card for a credit model? (3) How do you present a model that is only slightly better than the rule?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Framing workshop | Decision statements |
| 2 | 2 | Lab 2 · Baseline ladder | — |
| 3 | 3 | Lab 3 · Validation design | — |
| 4 | 4 | Lab 4 · Leakage hunt | **P1 due** |
| 5 | 5 | Lab 5 · GBDT tuning under budget | — |
| 6 | 5–6 | Lab 5 (cont.): EBM vs GBDT | — |
| 7 | 7 | Lab 6 · Thresholds and decision curves | Mid-term (AI off) |
| 8 | 8 | Lab 7 · Interpretability traps | — |
| 9 | 8 | Lab 7 (cont.) | — |
| 10 | 9 | Lab 8 · Slices and fairness | **P2 due** |
| 11 | 10 | Lab 9 · Segments and anomalies | — |
| 12 | 11 | Lab 10 · Agent pipeline audit | P3 checkpoint |
| 13 | 12 | Memo clinic | Draft model card |
| 14 | 12 | Review panel rehearsal | **P3 due** |
| 15 | Review | Review panel on P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** boilerplate pipelines, Optuna search code, plotting, SHAP and PDP code, first drafts of model cards, and AutoML or agent runs as baselines. Tools: Claude Code, GitHub Copilot, Gemini's Data Science Agent in Colab, ChatGPT, Jupyter AI, AutoGluon and TabPFN.
- **Do without AI (drills):** framing (decision, label, horizon, cost) for every project; the validation design; leakage hunts in Lab 4; choosing thresholds from a cost matrix by hand; explaining any plot aloud. The mid-term and final are AI-off.
- **Verify AI output by:** (1) a hidden holdout the assistant never saw, scored once; (2) a shuffled-label test (the pipeline must drop to chance); (3) reading every `fit` call to confirm it sees only training rows; (4) row-count and key checks before and after each step; (5) reproducing the result from your experiment log.
- **Where AI still fails here:** MLE-bench scores competitions that come with a fixed metric and clean target, so it does not measure framing, label design or deployment fit. Open-ended analysis benchmarks such as BLADE (2024) show weaker analytical decisions. In Lab 10 you will collect your own evidence: list each leak, silent row drop or wrong split you find in agent-generated pipelines, with the score inflation it caused.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 40% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + review panel on P3 | 25% |

**Mastery gate.** You pass when you can: (1) given an unseen tabular problem and a stakeholder brief, produce within 4 hours a framed task, a deployment-matching validation, a baseline ladder and a cost-based operating point whose hidden-holdout score falls within 2 standard errors of your CV estimate; (2) find all leaks in a planted pipeline within 30 minutes, AI off; (3) explain to a non-technical panel what the model's explanations do and do not show.

## Industry reality

Booking.com's 150-model study (Bernardi et al., 2019) is the clearest public account of applied ML judged by RCTs rather than offline metrics. Credit scoring, collections, fraud and insurance pricing commonly use gradient-boosted trees and regularized GLMs, often under monotonicity and interpretability requirements; in the US, banks follow the Federal Reserve's SR 11-7 model-risk guidance, which requires documentation, validation and ongoing monitoring of models. Obermeyer et al. (2019) showed how a health-risk model trained on cost as a proxy for need cut the number of Black patients identified for extra care by more than half, a framing error, not an algorithmic one.

**Interview questions from this course**

1. *Build a model to predict which customers will churn.* Strong answer: asks what action follows and its capacity; defines churn, horizon and decision time; notes that uplift, not churn probability, decides who to contact; proposes a baseline ladder, a time-based split and a cost-based operating point.
2. *Your model has an AUC of 0.97 on a problem where 0.75 is typical. What do you do?* Strong answer: suspects leakage first; runs single-feature AUCs, checks feature timestamps against decision time, duplicates across splits and label construction; shows the corrected score.
3. *Explain SHAP to a product manager, then tell me when it misleads.* Strong answer: average marginal contribution relative to a baseline; local and global uses; correlated features, interventional vs observational choices, proxies, and that SHAP explains the model, not the world.
4. *How would you validate a loan-default model trained on three years of applications?* Strong answer: out-of-time validation by vintage; label maturity windows; selection bias because only approved loans have outcomes (reject inference); stability across periods; calibration by segment.
5. *AutoML beat your model by 1 point. What now?* Strong answer: confirms the comparison used identical splits and no leakage; weighs latency, explainability, maintenance and licence; often adopts AutoML as baseline or ensemble member; reports the gain with an interval and in business terms.

## Resources (free first)

- **Texts:** James et al., *An Introduction to Statistical Learning with Applications in Python* — https://www.statlearning.com/ ; Christoph Molnar, *Interpretable Machine Learning* — https://christophm.github.io/interpretable-ml-book/
- **Courses and tutorials:** Kaggle Learn (Intermediate ML, Feature Engineering, Machine Learning Explainability) — https://www.kaggle.com/learn ; scikit-learn "Common pitfalls and recommended practices" — https://scikit-learn.org/stable/common_pitfalls.html
- **Documentation:** LightGBM — https://lightgbm.readthedocs.io/ ; XGBoost — https://xgboost.readthedocs.io/ ; CatBoost — https://catboost.ai/docs/ ; AutoGluon — https://auto.gluon.ai/ ; TabPFN — https://github.com/PriorLabs/TabPFN ; SHAP — https://shap.readthedocs.io/ ; InterpretML — https://interpret.ml/ ; Fairlearn — https://fairlearn.org/ ; Optuna — https://optuna.org/
- **Papers:** Kapoor and Narayanan, leakage — https://doi.org/10.1016/j.patter.2023.100804 ; Grinsztajn et al. — https://arxiv.org/abs/2207.08815 ; Lundberg and Lee — https://arxiv.org/abs/1705.07874 ; Kumar et al. — https://arxiv.org/abs/2002.11097 ; Rudin — https://doi.org/10.1038/s42256-019-0048-x ; Mitchell et al., model cards — https://arxiv.org/abs/1810.03993
- **Data:** UCI Bank Marketing — https://archive.ics.uci.edu/dataset/222/bank+marketing ; UCI Diabetes 130-US Hospitals — https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008 ; Home Credit Default Risk (Kaggle) — https://www.kaggle.com/c/home-credit-default-risk ; OpenML — https://www.openml.org/
- **Paid, optional:** Kuhn and Johnson, *Applied Predictive Modeling*.

## Sources

- Chan et al., MLE-bench (arXiv 2410.07095) — https://arxiv.org/abs/2410.07095 ; leaderboard — https://github.com/openai/mle-bench (checked 2026-10)
- Bernardi, Mavridis and Estevez, "150 Successful Machine Learning Models: 6 Lessons Learned at Booking.com", KDD 2019 — https://doi.org/10.1145/3292500.3330744 ; summary of the offline-vs-business finding, The Morning Paper (7 Oct 2019) — https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/ (checked 2026-10)
- Kapoor and Narayanan, "Leakage and the reproducibility crisis in machine-learning-based science", *Patterns* (2023) — https://doi.org/10.1016/j.patter.2023.100804 (checked 2026-10)
- Hollmann et al., "Accurate predictions on small data with a tabular foundation model", *Nature* (2025) — https://doi.org/10.1038/s41586-024-08328-6 (checked 2026-10)
- Kleinberg et al., "Prediction Policy Problems", *AER* (2015) — https://doi.org/10.1257/aer.p20151023 ; Bates, Hastie and Tibshirani, "Cross-Validation: What Does It Estimate and How Well Does It Do It?", *JASA* (2023) — https://doi.org/10.1080/01621459.2023.2197686 ; Vickers and Elkin, decision curve analysis (2006) — https://doi.org/10.1177/0272989X06295361 (checked 2026-10)
- Janzing et al. (arXiv 1910.13413) — https://arxiv.org/abs/1910.13413 ; Apley and Zhu, ALE (arXiv 1612.08468) — https://arxiv.org/abs/1612.08468 ; Lundberg et al., TreeSHAP (arXiv 1802.03888) — https://arxiv.org/abs/1802.03888 (checked 2026-10)
- Obermeyer et al., "Dissecting racial bias in an algorithm used to manage the health of populations", *Science* (2019) — https://doi.org/10.1126/science.aax2342 (checked 2026-10)
- Board of Governors of the Federal Reserve System, SR 11-7 Guidance on Model Risk Management (2011) — https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107.htm (checked 2026-10)
- Gu et al., BLADE (arXiv 2408.09667) — https://arxiv.org/abs/2408.09667 (checked 2026-10)

_Last reviewed: 2026-10_
