# DSC305 · Feature Engineering and Model Evaluation

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) (assumes [DSC302](../DSC302_applied_machine_learning_for_data_scientists/README.md) from semester 5) | [DSC401](../../year_4/DSC401_time_series_analysis_and_forecasting/README.md), [DSC403](../../year_4/DSC403_recommender_systems_and_personalization/README.md), [DSC404](../../year_4/DSC404_data_science_in_production_deployment_monitoring/README.md), [OV10B](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10B_fraud_detection_and_risk_systems/README.md) |

Part of the [Data Science major](../../README.md). The ML Engineering major's [MLE304](../../../machine_learning_engineering/year_3/MLE304_model_evaluation_fairness_and_robustness/README.md) covers robustness and fairness testing of deployed systems; this course focuses on what goes into a model and how to judge it against the cost of being wrong.

## Why this course matters now

On tabular problems, the features and the evaluation decide most of the outcome, and both fail silently. A feature computed with a few hours of future data, or a target encoding fitted on the full table, inflates every offline score; Kapoor and Narayanan (2023) found leakage across 17 scientific fields. Common fixes for rare events backfire: in a simulation and clinical case study, random undersampling, oversampling and SMOTE produced strongly miscalibrated risk models without improving the area under the ROC curve, and simply moving the threshold gave similar sensitivity–specificity balance (van den Goorbergh et al., 2022). Feature generation is now partly automated: AutoGluon builds features and stacks models, sentence-transformer and LLM embeddings turn any text column into hundreds of features in minutes, and LLM-based methods such as CAAFE propose new features from a dataset's description (Hollmann et al., 2023). The human job is to make sure every feature was knowable at prediction time, that the metric reflects what an error costs, and that the probabilities mean what they claim.

## Learning outcomes

By the end you can:

1. **Draw** a feature timeline for any prediction and **build** point-in-time-correct features with as-of joins.
2. **Choose and implement** encodings for numeric, categorical (including very high-cardinality), temporal, geographic, text and embedding inputs, and **justify** each for the model family.
3. **Prevent** target leakage in encodings and aggregates with cross-fitting, and **prove** it with tests.
4. **Select** features with methods that stay honest under cross-validation, and **measure** the stability of the selection.
5. **Translate** a business cost structure into a metric, an operating point and an expected cost with uncertainty.
6. **Evaluate** probabilistic predictions with proper scoring rules and reliability diagrams, and **recalibrate** with Platt, isotonic or temperature scaling.
7. **Handle** imbalanced data with weights and thresholds rather than resampling by default, and **evaluate** with precision–recall curves and intervals.
8. **Compare** models with paired statistical tests and **explain** how repeated use of a holdout overfits it.
9. **Write** an evaluation report that a risk reviewer can audit, including slices, calibration and stability over time.

## Chapters and lessons

### Chapter 1 · Features as hypotheses, in time (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What a feature encodes | A feature is a hypothesis about the world; signal, noise and proxies | List 20 candidate features for a delivery-delay model and tag each by hypothesis |
| 1.2 The feature timeline | Prediction time, data availability lags, label window; drawing it for every model | Draw timelines for credit, churn and ETA models |
| 1.3 Point-in-time correctness | As-of joins, snapshot tables, late-arriving data; feature stores as the industrial answer (see [MLE303](../../../machine_learning_engineering/year_3/MLE303_training_pipelines_feature_stores_and_experiment/README.md)) | Rebuild three leaky aggregates as point-in-time features |
| 1.4 Training–serving skew | Same definition, different code paths; how features drift between notebook and production | Find the skew between a batch and a "live" feature implementation |

**Check your understanding:** (1) A "number of complaints" feature is updated nightly. What value should a 10 a.m. prediction see? (2) Why can a feature be legal at training time and impossible at serving time? (3) What does a feature store guarantee, and what does it not?

### Chapter 2 · Numeric features (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Scale and shape | Standardisation, log, Box-Cox, Yeo-Johnson, winsorising; what trees ignore and linear models need | Compare transformations for a skewed income feature in a GLM and a GBDT |
| 2.2 Binning | Equal-width, quantile, supervised binning; information loss vs robustness; credit-scorecard bins | Bin a feature three ways and compare stability across years |
| 2.3 Splines and interactions | Natural splines, pairwise interactions, ratios and differences from domain knowledge | Build "debt-to-income" and "price relative to category median" features |
| 2.4 Aggregates | Group statistics, rolling windows, counts and recency; leakage through group statistics | Create customer-level aggregates with strict time cut-offs |

**Check your understanding:** (1) Why can binning improve a model's stability even if it lowers its training score? (2) When does a ratio feature help a tree that already has both components? (3) What leaks if a group mean includes the current row's target?

### Chapter 3 · Categorical features and target encoding (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 One-hot, ordinal and hashing | Dimensionality, collisions, unseen categories | Hash a 50,000-level feature and measure collision impact |
| 3.2 Target encoding done safely | Smoothing toward the prior, cross-fitting (scikit-learn `TargetEncoder`), CatBoost's ordered target statistics (Prokhorenkova et al., 2018) | Show the leak from naive target encoding, then remove it |
| 3.3 Hierarchies and rare levels | Pincode → district → state backoff; grouping rare categories | Build a hierarchical encoding for location and compare it with flat encoding |
| 3.4 Entity embeddings | Learned embeddings for categories in neural nets; reusing them in trees | Train embeddings for merchant IDs and use them in LightGBM |

**Check your understanding:** (1) Why does naive target encoding overfit most on rare categories? (2) How does hierarchical backoff help new pincodes? (3) When would you prefer hashing to target encoding?

### Chapter 4 · Time, calendar and geography (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Calendar features | Day of week, month, cyclical encoding, Indian holidays and festivals whose dates move each year (Diwali, Eid), paydays and fiscal-year ends | Build a holiday table for five years and measure its effect on daily demand |
| 4.2 Lags and windows | Lags, rolling statistics, exponentially weighted features; gaps between data and prediction | Generate lag features that respect a 2-day data delay |
| 4.3 Recency, frequency, tenure | RFM features; time since last event; censoring | Build RFM features for an e-commerce log |
| 4.4 Geographic features | Distances, H3 cells, spatial aggregates, spatial leakage across folds | Show spatial leakage with random vs spatial-block CV |

**Check your understanding:** (1) Why is month-of-year a poor proxy for Diwali? (2) What breaks if lag features are computed on the full series before the split? (3) Why can neighbouring H3 cells leak information across folds?

### Chapter 5 · Text, image and embedding features (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Classical text features | Counts, TF-IDF, character n-grams, length and punctuation features | Add TF-IDF of complaint text to a churn model |
| 5.2 Pretrained embeddings | Sentence-transformers, multilingual models, choosing with MTEB; dimensionality reduction | Compare three embedding models as features for the same target |
| 5.3 LLM-derived features | Asking an LLM to extract attributes (product type, sentiment, intent) as structured fields; cost, latency and validation | Extract 3 attributes from 1,000 product titles and check them against 100 hand labels |
| 5.4 Leakage through text and embeddings | Text written after the outcome (resolution notes), embeddings of near-duplicate records | Find a leaking text field in a support-ticket dataset |

**Check your understanding:** (1) When are 768 embedding dimensions worse than 20 TF-IDF features? (2) How do you validate an LLM-extracted feature before using it? (3) Why can embeddings make duplicate-record leakage harder to spot?

### Chapter 6 · Missing data and data quality as features (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Why values are missing | MCAR, MAR, MNAR in operational data; missingness as signal | Test whether missingness predicts the target |
| 6.2 Imputation inside the pipeline | Simple, iterative and model-based imputation fitted on training folds only; indicators | Compare four strategies under CV |
| 6.3 Quality flags | Outlier flags, impossible values, source-system indicators | Add quality flags and measure their effect |
| 6.4 When missingness will change | Process changes that alter missingness in production | Simulate a form change that removes a field and measure damage |

**Check your understanding:** (1) Why can "income missing" be one of the strongest features? (2) What goes wrong if the imputer sees validation rows? (3) How would you protect a model from a field becoming optional?

### Chapter 7 · Leakage forensics and feature selection (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Leakage forensics | Single-feature AUCs, timestamps vs prediction time, proxies of the label, the eight leakage types | Investigate a model that is "too good" and find the cause |
| 7.2 Filter, wrapper and embedded selection | Correlation and mutual information filters; recursive elimination; L1 and tree-based selection | Run three methods and compare chosen sets |
| 7.3 Selection inside CV | Why selection outside CV inflates scores (the scikit-learn random-labels demonstration) | Reproduce the inflation on random labels, then fix it |
| 7.4 Stability selection | Selection frequency across resamples; reporting unstable features | Report which features survive 80% of bootstrap resamples |

**Check your understanding:** (1) A feature has AUC 0.98 alone. List three explanations. (2) Why must selection happen inside each fold? (3) What does an unstable selected set tell a stakeholder?

### Chapter 8 · Metrics tied to business cost (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 The cost matrix | Expected cost; cost-sensitive thresholds (Elkan, 2001); asymmetric errors | Derive the optimal threshold for a fraud and a medical-screening case |
| 8.2 Capacity and ranking metrics | Precision@k, recall at fixed review volume, lift; ROC vs precision–recall (Davis and Goadrich, 2006; Saito and Rehmsmeier, 2015) | Evaluate two models at a 500-alerts-a-day capacity |
| 8.3 Regression losses | MAE vs RMSE vs MAPE (and its failure near zero), pinball loss for quantiles, asymmetric losses | Choose a loss for delivery-time promises where lateness costs 3× earliness |
| 8.4 Metric choice and gaming | Goodhart's law; proxy metrics; metrics that reward the wrong model | Construct a model that wins on accuracy and loses money |
| 8.5 Expected business impact | Turning a metric difference into money with intervals | Estimate the monthly savings of model B over A with a bootstrap |

**Check your understanding:** (1) Why is accuracy meaningless at a 0.5% positive rate? (2) When is ROC-AUC the right metric? (3) Why does MAPE favour models that under-forecast?

### Chapter 9 · Probabilities: calibration and proper scoring (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Proper scoring rules | Log loss and Brier score; why they reward honest probabilities (Gneiting and Raftery, 2007) | Show a miscalibrated model beating a calibrated one on AUC but losing on log loss |
| 9.2 Reliability diagrams and their limits | Binning choices, expected calibration error and its pitfalls | Plot reliability with bootstrap bands |
| 9.3 Recalibration | Platt scaling, isotonic regression, temperature scaling; calibration sets (Niculescu-Mizil and Caruana, 2005) | Recalibrate a GBDT and a resampled model |
| 9.4 Calibration over time and slices | Base-rate shift, recalibration on recent data, calibration by group | Detect and fix calibration drift across two years |
| 9.5 Prediction intervals | Quantile models and conformal prediction (Angelopoulos and Bates) | Produce 90% intervals for delivery times and check coverage |

**Check your understanding:** (1) Why does undersampling the majority class inflate predicted probabilities? (2) When is isotonic calibration risky? (3) What does conformal coverage guarantee, and under what assumption?

### Chapter 10 · Imbalanced data (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 What imbalance does and doesn't do | Base rates; the real problem is few positives, not the ratio | Learning curve on positives: how many do you need? |
| 10.2 Weights, thresholds and resampling | Class weights vs threshold moving vs SMOTE; the calibration cost (van den Goorbergh et al., 2022) | Reproduce the calibration damage of resampling, then avoid it |
| 10.3 Evaluating with few positives | Intervals on recall and precision; stratified and repeated CV | Report recall with a 95% interval from 40 positives |
| 10.4 Getting more positives | Active learning and targeted labelling; rare-event sampling with weights | Simulate active labelling for a fraud review queue |

**Check your understanding:** (1) Why is "balance the classes" not a goal in itself? (2) How do you correct probabilities after case–control sampling? (3) What does a recall estimate from 40 positives really tell you?

### Chapter 11 · Comparing models honestly (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Paired comparisons | Paired bootstrap, McNemar's test, corrected repeated CV tests | Decide whether a new model's gain is real |
| 11.2 Holdout reuse | Overfitting to a test set through repeated submissions; Kaggle public vs private leaderboards | Simulate 200 submissions against one holdout and measure optimism |
| 11.3 Temporal and slice robustness | Out-of-time evaluation, performance by vintage and segment | Evaluate a credit model by origination year |
| 11.4 Evaluation reports | Structure: data, splits, metrics, calibration, slices, stability, limitations | Write the evaluation section for P3 |

**Check your understanding:** (1) Why do you need paired tests when two models are scored on the same rows? (2) How does repeated holdout use bias your final estimate? (3) Which slice results belong in the main report?

### Chapter 12 · Automated and AI-generated features (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 AutoML feature generation | What AutoGluon and similar tools generate and how they validate it | Inspect AutoGluon's generated features and validation splits |
| 12.2 LLM-proposed features | CAAFE-style generation from dataset descriptions; semantic plausibility vs real gain | Ask an LLM for 20 features; keep only those that survive CV and the timeline test |
| 12.3 Auditing generated features | Timeline check, leakage scan, stability, cost | Audit a supplied generated-feature set and reject the leaky ones |
| 12.4 Feature cost and governance | Compute, latency and data-licensing cost per feature; documentation; retiring features nobody needs | Price every feature in your P3 model and drop those that do not pay for themselves |

**Check your understanding:** (1) Why is "plausible" not evidence for a feature? (2) Which test catches a generated feature that peeks at the future? (3) When is a feature not worth its compute or latency?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Point-in-time features | Feature timelines |
| 2 | 2 | Lab 1 (cont.): Numeric transforms and aggregates | — |
| 3 | 3 | Lab 2 · Encoding bake-off | — |
| 4 | 4 | Lab 3 · Calendars and spatial CV | **P1 due** |
| 5 | 5 | Lab 4 · Embedding and LLM features | — |
| 6 | 6 | Lab 4 (cont.): Missingness | — |
| 7 | 7 | Lab 5 · Leakage forensics | Mid-term (AI off) |
| 8 | 8 | Lab 6 · Cost curves | — |
| 9 | 8–9 | Lab 7 · Calibration | — |
| 10 | 9 | Lab 7 (cont.) and conformal intervals | **P2 due** |
| 11 | 10 | Lab 8 · Imbalance without resampling | — |
| 12 | 11 | Lab 9 · Paired tests and holdout reuse | P3 checkpoint |
| 13 | 11 | Evaluation report clinic | — |
| 14 | 12 | Lab 10 · Audit generated features | **P3 due** |
| 15 | Review | Evaluation defence | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating candidate features from domain descriptions; writing as-of joins and rolling-window code; boilerplate for encoders, calibration and plots; summarising evaluation tables. Tools: Claude Code, GitHub Copilot, ChatGPT, Gemini in Colab, AutoGluon's feature generation and LLM-based generators such as CAAFE.
- **Do without AI (drills):** drawing the feature timeline; deriving cost-optimal thresholds; reading a reliability diagram; deciding which metric matches a cost structure; the leakage forensics in Lab 5. The mid-term and final are AI-off.
- **Verify AI output by:** (1) the timeline test: every feature's source timestamp must precede prediction time minus the data delay; (2) a shuffled-label run (scores must fall to chance); (3) cross-fitted versions of any target-dependent feature; (4) reliability diagrams and proper scores, not just AUC; (5) out-of-time evaluation.
- **Where AI still fails here:** an LLM proposing features cannot see your data pipeline's timing, so plausible-sounding features can be impossible at prediction time; CAAFE-style methods keep a feature only if it improves validation scores, which is exactly why the validation must be leak-free. In Lab 10 you will measure how many assistant-proposed features fail the timeline test or add nothing out of time.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 40% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + evaluation defence | 25% |

**Mastery gate.** You pass when you can: (1) given an unseen dataset and a prediction time, build a point-in-time-correct feature set that passes a hidden leakage audit; (2) AI off, convert a stated cost structure into a metric and operating point, and compute expected cost with an interval; (3) diagnose and fix miscalibration in a supplied model, and explain to a reviewer why the original probabilities could not be used for pricing.

## Industry reality

Credit, insurance, fraud and logistics models are judged on calibrated probabilities and cost-weighted errors, not on accuracy. A main purpose of feature stores is to make point-in-time correctness and training–serving consistency routine (covered in MLE303). Mortgage and consumer-credit modelling is evaluated by vintage, because economic conditions shift default rates; the Freddie Mac Single-Family Loan-Level Dataset, which includes loans through the 2008 crisis, is a public way to experience this. Public competitions show the cost of holdout reuse: Kaggle separates public and private leaderboards for this reason.

**Interview questions from this course**

1. *How would you encode a pincode feature for a delivery model?* Strong answer: high cardinality; hierarchical backoff (pincode → district → state); cross-fitted target encoding with smoothing; handling unseen pincodes; spatial leakage in CV; geographic features as an alternative.
2. *Fraud is 0.1% of transactions. Which metric do you optimise?* Strong answer: not accuracy; precision–recall and recall at the review team's capacity; expected cost with chargeback and review costs; intervals because positives are few; calibration if probabilities feed a decision engine.
3. *Should we use SMOTE?* Strong answer: usually not by default; it distorts calibration without improving discrimination in many settings (van den Goorbergh et al., 2022); prefer class weights or threshold moving; if resampling, correct probabilities afterwards.
4. *Our model's probabilities feed pricing. How do you evaluate it?* Strong answer: proper scoring rules (log loss, Brier), reliability diagrams by segment and over time, recalibration on recent data, monitoring base-rate shifts.
5. *Model A has higher AUC; model B has lower log loss. Which do you deploy?* Strong answer: depends on use; ranking for a fixed-capacity queue favours AUC or precision@k; probability-driven decisions favour log loss and calibration; check both at the operating point with paired tests.

## Resources (free first)

- **Texts:** Kuhn and Johnson, *Feature Engineering and Selection* (free online) — https://bookdown.org/max/FES/ ; Molnar, *Interpretable Machine Learning* — https://christophm.github.io/interpretable-ml-book/ ; Angelopoulos and Bates, *A Gentle Introduction to Conformal Prediction* — https://arxiv.org/abs/2107.07511
- **Documentation:** scikit-learn preprocessing and `TargetEncoder` — https://scikit-learn.org/stable/modules/preprocessing.html ; scikit-learn probability calibration — https://scikit-learn.org/stable/modules/calibration.html ; scikit-learn common pitfalls — https://scikit-learn.org/stable/common_pitfalls.html ; Sentence-Transformers — https://sbert.net/ ; MTEB leaderboard — https://huggingface.co/spaces/mteb/leaderboard ; AutoGluon — https://auto.gluon.ai/ ; H3 — https://h3geo.org/
- **Papers:** van den Goorbergh et al. — https://doi.org/10.1093/jamia/ocac093 ; Niculescu-Mizil and Caruana — https://doi.org/10.1145/1102351.1102430 ; Gneiting and Raftery — https://doi.org/10.1198/016214506000001437 ; Saito and Rehmsmeier — https://doi.org/10.1371/journal.pone.0118432 ; Elkan, cost-sensitive learning — https://cseweb.ucsd.edu/~elkan/rescale.pdf ; Prokhorenkova et al., CatBoost — https://arxiv.org/abs/1706.09516 ; Hollmann et al., CAAFE — https://arxiv.org/abs/2305.03403
- **Data:** Freddie Mac Single-Family Loan-Level Dataset (free registration) — https://www.freddiemac.com/research/datasets/sf-loanlevel-dataset ; Amazon.com Employee Access Challenge (Kaggle) — https://www.kaggle.com/c/amazon-employee-access-challenge ; NYC TLC trip records — https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- **Courses:** Kaggle Learn Feature Engineering — https://www.kaggle.com/learn

## Sources

- Kapoor and Narayanan, *Patterns* (2023) — https://doi.org/10.1016/j.patter.2023.100804 (checked 2026-10)
- van den Goorbergh et al., "The harm of class imbalance corrections for risk prediction models", *JAMIA* (2022) — https://doi.org/10.1093/jamia/ocac093 (checked 2026-10)
- Hollmann, Müller and Hutter, CAAFE (arXiv 2305.03403, NeurIPS 2023) — https://arxiv.org/abs/2305.03403 (checked 2026-10)
- Davis and Goadrich (2006) — https://doi.org/10.1145/1143844.1143874 ; Saito and Rehmsmeier (2015) — https://doi.org/10.1371/journal.pone.0118432 ; Niculescu-Mizil and Caruana (2005) — https://doi.org/10.1145/1102351.1102430 ; Gneiting and Raftery (2007) — https://doi.org/10.1198/016214506000001437 (checked 2026-10)
- Elkan, "The Foundations of Cost-Sensitive Learning", IJCAI 2001 — https://cseweb.ucsd.edu/~elkan/rescale.pdf (checked 2026-10)
- Prokhorenkova et al., "CatBoost: unbiased boosting with categorical features" (arXiv 1706.09516) — https://arxiv.org/abs/1706.09516 (checked 2026-10)
- Freddie Mac, Single-Family Loan-Level Dataset — https://www.freddiemac.com/research/datasets/sf-loanlevel-dataset (checked 2026-10)

_Last reviewed: 2026-10_
