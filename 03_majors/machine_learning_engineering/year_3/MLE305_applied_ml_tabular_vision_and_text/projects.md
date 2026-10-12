# MLE305 · Labs and projects

Every lab and project uses one rule: **all preprocessing is fitted inside the validation fold**, and every claimed improvement comes with an ablation and at least 3 seeds. Keep an experiment log (MLflow or a plain CSV) from Lab 1. You may use coding agents for any lab except Lab 2's audit, but you must report the agent's best score next to your own, and both are scored on a hidden holdout the agent never saw.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Split design and adversarial validation | Choose splits for 5 dataset stories; run adversarial validation on a public train/test pair | Split decisions with one-line justifications; the adversarial AUC and the top shifting features | 3 h |
| 2 · Leakage hunt | Audit a provided pipeline with 5 planted leaks (target, temporal, preprocessing, group, duplicate), then audit 3 assistant-generated pipelines | Leak report: location, type, measured score inflation, fix | 4 h |
| 3 · Features and target encoding | Missing-value flags, out-of-fold target encoding, past-only aggregates; a Polars rewrite of a slow pandas job | Encoder with a leakage unit test; speed and memory table | 4 h |
| 4 · GBDT, TabPFN and AutoGluon | LightGBM, XGBoost and CatBoost under identical CV; 50-trial Optuna budget; TabPFN and AutoGluon on 3 OpenML datasets | Results table with mean ± std over seeds; a one-page model-choice note (including licence terms) | 5 h |
| 5 · Stacking and imbalance | Out-of-fold stacking; class weights vs undersampling vs SMOTE inside CV; cost-based threshold | PR curves, the chosen threshold for a 200-cases-a-day review team, and its expected cost | 4 h |
| 6 · Linear probe vs fine-tuning | timm backbones; DINOv3 frozen features + logistic regression; fine-tuning with discriminative learning rates; augmentation ablation | Accuracy, GPU-minutes and latency for each approach; one harmful augmentation explained | 6 h (2 weeks) |
| 7 · Label noise and deduplication | cleanlab on an image dataset; near-duplicate detection across splits with embeddings | 50 reviewed suspect labels (agree/disagree); accuracy before and after deduplication | 4 h |
| 8 · Classical text and code-mixed text | TF-IDF word vs character n-grams; logistic regression and linear SVM; a Hindi–English code-mixed set | Comparison table; the 20 most influential n-grams and one spurious one | 3 h |
| 9 · Embeddings, fine-tuning and Indic text | Sentence embeddings + linear head; a fine-tuned small encoder; SetFit learning curve; IndicSentiment in two languages | Learning curves (8 → all labels); multilingual vs Indic-specific comparison | 6 h (2 weeks) |
| 10 · LLM labelling and distillation | LLM labels for 2,000 items; Cohen's κ against a 200-item human gold set; distil into a small model | κ, confusion between LLM and gold labels, cost per 1,000 items, accuracy and p95 latency of the distilled model | 4 h |

## Projects

### P1 · A leak-proof baseline and leakage audit (L1, ~6 hours)

**Real-world inspiration.** Kaufman et al. (2012) documented leakage in real data-mining competitions and projects, and Kaggle Learn's Data Leakage lesson separates target leakage from train–test contamination using a credit-card application example. A leak that nobody audits survives into production, where the promised accuracy never appears.

**What to build.** For a tabular dataset with a deployment story supplied by your instructor (illustrative scenario: a lender scoring loan applications at the moment of application), build a scikit-learn `Pipeline` baseline and a written leakage audit of the dataset and of one public notebook on the same data.

**Acceptance criteria**
- Every transformer is inside a `Pipeline` or `ColumnTransformer`; a unit test fails if any transformer is fitted on validation rows.
- The audit names at least 4 leakage risks, and for each one measures the score with and without the suspect feature or step.
- The cross-validated score is within 2 standard errors of the instructor's hidden holdout score.
- An adversarial-validation check is included and interpreted.
- One page of findings is written for a non-ML product manager.

**Stretch goals.** A reusable `leakcheck` script that flags features with suspiciously high single-feature AUC, timestamps after the prediction time, and duplicate entities across folds.

**What it proves to an employer.** You do not ship a number you cannot defend, which is the first thing a senior ML engineer checks in a junior's work.

### P2 · Competition-grade fraud model (L2, ~15 hours)

**Real-world inspiration.** The IEEE-CIS Fraud Detection competition (Vesta Corporation with the IEEE Computational Intelligence Society, Kaggle, 2019) released real e-commerce transaction data. It is time-ordered and heavily imbalanced, and the same card holder appears in many transactions without an explicit customer ID, which makes it a realistic test of validation design and entity-level leakage.

**What to build.** A full solution: time-based validation that mirrors the competition's train/test gap, feature engineering (aggregates, frequency and target encodings, entity features), LightGBM and CatBoost models plus one different model family, out-of-fold stacking, and a cost-based operating point. Submit late to Kaggle to get the private-leaderboard score.

**Acceptance criteria**
- The validation scheme is documented and the local score tracks the private-leaderboard score (the gap is reported and explained).
- An ablation table with at least 6 rows, each the mean of 3 seeds, shows what every feature group and model adds.
- The final stack beats your best single model by more than the seed standard deviation, or the report says honestly that it does not.
- A PR curve, recall at a fixed review capacity, and a threshold chosen by an explicit cost assumption.
- The whole pipeline reruns from raw files with one command in under 2 hours on a laptop or free cloud notebook.
- The report lists any agent-generated code that was used and the leaks found in it.

**Stretch goals.** TabPFN on a down-sampled version, compared fairly; SHAP analysis of the top 20 features with a note on correlated-feature attribution; a calibration curve.

**What it proves to an employer.** You can deliver a strong model on hard, realistic tabular data and explain exactly where each point of improvement came from.

### P3 · Multimodal product matching (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Marketplaces must detect when two listings are the same product, for price comparison, duplicate removal and search quality. Shopee's "Price Match Guarantee" competition on Kaggle (2021) released product images and titles grouped by product, scored by F1 per posting.

**What to build.** A matching system that combines image embeddings (a frozen or lightly fine-tuned backbone such as DINOv3 or a CLIP-style model) with text features (TF-IDF with character n-grams and sentence embeddings), nearest-neighbour search, a per-modality and fused threshold, and an error-analysis report. Package it as a function that takes a new listing and returns its matches.

**Acceptance criteria**
- Folds are grouped by product group, so no product appears in both training and validation (explain why a random split leaks here).
- Image-only, text-only and fused results are reported with 3 seeds; the fused system beats both single modalities.
- A late submission records the private-leaderboard F1.
- Matching a new listing against the full catalogue takes under 100 ms at p95 on CPU, measured and reported with hardware details.
- An error gallery of 30 failures grouped into causes (variants, bundles, text-in-image, wrong labels), with one fix implemented and measured.
- A model card states intended use, data, metrics by slice (for example, by title language or category if identifiable), and known failure modes.

**Stretch goals.** An LLM verifier for borderline pairs, with cost per 1,000 pairs and the precision gain measured; distil the fused model into a single small encoder; an approximate-nearest-neighbour index with recall vs latency curves.

**What it proves to an employer.** You can combine pretrained vision and text models into a working product feature, measure it honestly, and reason about latency and cost, which is the job of an applied ML engineer at any marketplace.

## Feeds into

- [MLE401 MLOps](../../year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md): the P2 fraud model is deployed, monitored for drift and retrained.
- [MLE403 Ranking and Recommendation](../../year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md): P3's embedding search becomes candidate generation.
- [MLE404 Efficient Inference](../../year_4/MLE404_efficient_inference_quantization_distillation/README.md): P3's encoders are quantised and distilled.
- [MLE304 Evaluation, Fairness and Robustness](../MLE304_model_evaluation_fairness_and_robustness/README.md): calibration and slice metrics from P2 and P3 go deeper.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): a data-centric study (label noise, leakage, LLM labelling) is a strong capstone topic.
