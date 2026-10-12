# MLE305 · Applied ML: Tabular, Vision and Text

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L4 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [MLE401](../../year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md), [MLE403](../../year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md), [MLE404](../../year_4/MLE404_efficient_inference_quantization_distillation/README.md), [IND401](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) |

## Why this course matters now

Applied ML is the daily work of turning a messy dataset into a model that holds up on data it has never seen. AI agents now do much of the mechanical part. On OpenAI's MLE-bench (75 Kaggle competitions), the best agent reached a medal in 17% of competitions in October 2024; by February 2026 the top entry reached 64%. The same leaderboard lists one 78% result separately, because that system used test-set feedback, which is leakage. Pretrained models have also raised the floor: frozen DINOv3 image features, sentence embeddings, and tabular foundation models such as TabPFN (Hollmann et al., *Nature*, 2025) give strong baselines in minutes. What still needs a skilled engineer is everything an agent cannot check by itself: a validation split that mirrors deployment, leaks found before they reach production, labels you can trust, and an honest answer to "is this better, and by how much?"

## Learning outcomes

By the end you can:

1. **Design** a validation scheme (random, stratified, grouped, time-based) that matches how the model will be used, and **detect** train/test mismatch with adversarial validation.
2. **Find and fix** the main leakage types (target, temporal, group, preprocessing and duplicate leakage) in your own code and in AI-generated code.
3. **Build** strong tabular baselines with gradient-boosted trees, out-of-fold target encoding, tuning and ensembling, and **compare** them with AutoML and tabular foundation models.
4. **Apply** transfer learning in vision (linear probe, fine-tuning, augmentation) and **choose** between them by data size and domain gap.
5. **Build** text classifiers from TF-IDF baselines to fine-tuned transformer encoders, including multilingual and code-mixed (Hinglish) text.
6. **Measure and repair** label quality with confident learning and near-duplicate detection.
7. **Use** LLMs and zero-shot models as baselines or weak labellers, and **measure** their agreement with a human gold set before trusting them.
8. **Run** error analysis by slice, explain predictions with SHAP or attribution methods, and **write** an ablation-backed solution report.

## Chapters and lessons

### Chapter 1 · Validation that mirrors reality (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The applied loop | Problem → metric → split → baseline → error analysis → iterate; an experiment log from day 1 | Write the plan for a churn problem before touching data |
| 1.2 Split design | Random, stratified, `GroupKFold`, `TimeSeriesSplit`, purged gaps; "how will this model be used?" | Pick and defend splits for 5 dataset stories |
| 1.3 Adversarial validation | Train a classifier to tell train from test; what an AUC of 0.5 vs 0.9 means | Run it on a Kaggle train/test pair; find the shifting features |
| 1.4 Trusting the score | Variance across seeds and folds, overfitting the validation set by repeated tuning | Measure the spread of 20 runs; set a "real improvement" threshold |

**Check your understanding:** Why is a random split wrong for a model that will score next month's transactions? What does an adversarial-validation AUC of 0.95 tell you to do? Why can 200 tuning runs make your validation score optimistic?

### Chapter 2 · Leakage hunting (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 A taxonomy | Target leakage, train–test contamination, temporal leakage, group leakage (Kaufman et al., 2012) | Classify 10 real leak descriptions |
| 2.2 Preprocessing leakage | Scaling, imputation, feature selection or target encoding fitted outside the CV fold; scikit-learn `Pipeline` and `ColumnTransformer` | Show a 5-point AUC inflation from feature selection outside CV |
| 2.3 Duplicate and near-duplicate leakage | The same user, patient, product or image on both sides of a split | Find near-duplicate images across splits with embeddings |
| 2.4 Suspicious signals | Too-good features, IDs and row order that encode the label, future timestamps | Leak audit of a provided notebook; write a leak report |
| 2.5 Leakage in agent output | Agents and assistants that fit on all data or peek at test labels; MLE-bench's separately listed test-feedback result | Review 3 AI-generated pipelines and mark every leak |

**Check your understanding:** Why is feature selection on the full dataset leakage even if the model never sees test labels? How can a hospital-ID feature leak the label? Why is "the model is suspiciously good" a bug report?

### Chapter 3 · Tabular data and features (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Data types and missingness | MCAR, MAR and MNAR; missing indicators; why trees handle NaN natively | Compare imputation strategies; measure the value of the missing flag |
| 3.2 Categorical encodings | One-hot, ordinal, frequency, hashing; out-of-fold target encoding with smoothing; CatBoost's ordered statistics | Leak-free target encoder vs naive version on a high-cardinality column |
| 3.3 Aggregations and time | Group-by statistics, lags and windows computed only from the past, date parts | Customer-level aggregates on a transactions table without future leakage |
| 3.4 Fast data work | Polars lazy queries, Parquet, memory-aware dtypes | Rewrite a slow pandas feature job in Polars; measure speed and memory |

**Check your understanding:** Why does naive target encoding overfit on rare categories? When is a missing value itself the most predictive feature? Why must a rolling mean exclude the current row?

### Chapter 4 · Strong tabular baselines (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 GBDT in practice | LightGBM, XGBoost and CatBoost defaults; early stopping on a validation fold; seed averaging | Three libraries on one dataset with identical CV |
| 4.2 Tuning | Random search vs TPE (Optuna); which 4–5 hyperparameters matter; budgets | Tune with a fixed 50-trial budget; report the gain over defaults with error bars |
| 4.3 Foundation models and AutoML | TabPFN for small and medium tables (check licence terms); AutoGluon as a ceiling estimate | Compare TabPFN, AutoGluon and your tuned GBDT on 3 OpenML datasets |
| 4.4 When deep tabular helps | Evidence that trees still win on medium-sized data (Grinsztajn et al., 2022); where embeddings of text or images change that | Write a one-page model-choice note with evidence |
| 4.5 Ensembling | Blending, stacking with out-of-fold predictions, rank averaging | Stack 3 models; prove the stack uses no in-fold predictions |

**Check your understanding:** Why does early stopping need its own validation data inside each fold? When is AutoML's result a ceiling and when is it a trap? Why do diverse models ensemble better than five copies of the best one?

### Chapter 5 · Imbalance and decisions (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Imbalanced metrics | PR-AUC vs ROC-AUC, recall at fixed precision | Report both on a 1:500 fraud dataset; explain the difference |
| 5.2 Weights vs resampling | Class weights, undersampling, SMOTE and why resampling before the split leaks | Compare 3 approaches inside correct CV |
| 5.3 Thresholds by cost | Expected cost, choosing the operating point, capacity limits (review queues) | Pick a threshold for a team that can review 200 cases a day |
| 5.4 Case: card fraud | The IEEE-CIS Fraud Detection competition (Vesta, 2019): time split, user identification, feature engineering | Reproduce a time-split baseline and a late submission |

**Check your understanding:** Why can ROC-AUC look excellent when the model is useless at the top of the list? Why does oversampling before splitting inflate scores? Who should choose the decision threshold?

### Chapter 6 · Vision: transfer learning (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Pretrained backbones | CNNs vs ViTs (Dosovitskiy et al., 2020); timm model zoo; input resolution and normalisation | Load 3 backbones; compare accuracy, latency and parameters |
| 6.2 Linear probe first | Frozen features (DINOv2, DINOv3) + logistic regression as the baseline | Linear probe on a 2,000-image dataset in under 10 minutes |
| 6.3 Fine-tuning | Discriminative learning rates, gradual unfreezing, warm-up, mixed precision | Fine-tune and beat the linear probe; report the cost |
| 6.4 Augmentation | Flips, crops, RandAugment, mixup and CutMix; augmentations that break labels | Ablate 4 augmentations; find one that hurts |
| 6.5 Small data and domain gap | When pretrained features transfer and when they do not (medical, satellite, documents) | Probe vs fine-tune on an out-of-domain dataset |

**Check your understanding:** Why does a linear probe sometimes beat fine-tuning with 500 images? Which augmentation is wrong for digit or text images? Why must the backbone learning rate be lower than the head's?

### Chapter 7 · Data-centric vision (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Label noise | Test-set label errors in popular benchmarks (Northcutt et al., 2021); confident learning with cleanlab | Find and review the 50 most suspicious labels in a dataset |
| 7.2 Deduplication | Perceptual hashes and embedding similarity; leakage across splits | Deduplicate before splitting; re-measure accuracy |
| 7.3 Error analysis | Confusion by class, slices by device, lighting or source | Build an error gallery; rank fixes by expected gain |
| 7.4 Attribution | Grad-CAM and integrated gradients (Captum); their limits | Show a model using a watermark or background as a shortcut |

**Check your understanding:** Why can fixing 2% of labels matter more than a bigger model? Why does deduplication usually lower your score? What can a saliency map not prove?

### Chapter 8 · Text: classical baselines (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Tokens and n-grams | Word and character n-grams, TF-IDF, sublinear term frequency | TF-IDF + logistic regression on SMS spam |
| 8.2 Linear models for text | Logistic regression and linear SVM on sparse features; NB-SVM | Beat a naive transformer baseline on a small dataset |
| 8.3 Multilingual and code-mixed text | Character n-grams for Hinglish and transliterated text; script normalisation | Classify a Hindi–English code-mixed set; compare word vs char features |
| 8.4 Interpretability | Top-weighted n-grams, error inspection | Find a spurious n-gram the model depends on |

**Check your understanding:** Why are character n-grams robust to spelling variation? Why do sparse linear models remain strong on short texts? What does a top feature like a phone-number pattern tell you?

### Chapter 9 · Text: embeddings and fine-tuning (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Sentence embeddings | Sentence-BERT (Reimers and Gurevych, 2019); choosing models with the MTEB leaderboard (Muennighoff et al.) | Embeddings + logistic regression vs TF-IDF |
| 9.2 Fine-tuning encoders | BERT-style encoders and ModernBERT (2024); Hugging Face Transformers training loop | Fine-tune a small encoder; compare cost and accuracy |
| 9.3 Few-shot | SetFit (Tunstall et al., 2022) with 8–64 labels per class | Learning curve: 8, 32, 128, all labels |
| 9.4 Indian languages | AI4Bharat models and datasets (IndicBERT, IndicSentiment) | Sentiment in two Indian languages; compare multilingual vs Indic-specific encoders |
| 9.5 Long and noisy text | Truncation strategies, chunk-and-pool, label noise in text | Classify long support tickets; measure truncation loss |

**Check your understanding:** Why do frozen embeddings plus a linear head often match fine-tuning with little data? What does an MTEB score not tell you about your domain? Why might a multilingual model underperform on Hinglish?

### Chapter 10 · Zero-shot models and LLM labelling (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Zero-shot vision | CLIP (Radford et al., 2021) and SigLIP 2 (2025) prompts as classifiers | Zero-shot vs linear probe on the same dataset |
| 10.2 LLMs as baselines | Zero- and few-shot classification with an LLM; cost and latency per 1,000 items | Compare an LLM baseline with your fine-tuned encoder on accuracy, cost and p95 latency |
| 10.3 LLMs as labellers | Weak labels, agreement with a human gold set (Cohen's κ), disagreement review | Label 2,000 items with an LLM; measure κ on a 200-item gold set |
| 10.4 Distillation into small models | Train a small model on verified LLM labels for cheap, fast serving | Distil and report the accuracy gap and the speed-up |

**Check your understanding:** Why must LLM labels be checked against a human gold set before training on them? When is an LLM call per item the right production choice? What bias can a zero-shot prompt introduce?

### Chapter 11 · Error analysis and the solution report (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 SHAP and its limits | Shapley values (Lundberg and Lee, 2017), TreeSHAP, correlated features | Explain 5 predictions; show a misleading attribution under correlation |
| 11.2 Slice analysis | Error by segment, minimum slice sizes, confidence intervals | Find the worst 3 slices of your P2 model |
| 11.3 Ablations | One change at a time, seeds, error bars | Ablation table for P3 |
| 11.4 Reproducibility | Locked environments, seeds, data hashes, one-command runs | Reproduce a classmate's result from their repo |
| 11.5 The write-up | Competition-style solution reports: what worked, what did not, why | Write P3's report |

**Check your understanding:** Why can SHAP split credit arbitrarily between correlated features? Why is an improvement smaller than seed variance not an improvement? What must a solution report include for someone else to reproduce it?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Split design and adversarial validation | — |
| 2 | 2 | Lab 2 · Leakage hunt | **P1 due** |
| 3 | 3 | Lab 3 · Features and target encoding | — |
| 4 | 4 | Lab 4 · GBDT, TabPFN and AutoGluon | — |
| 5 | 4–5 | Lab 5 · Stacking and imbalance | — |
| 6 | 6 | Lab 6 · Linear probe vs fine-tuning | **P2 due** |
| 7 | 6 | Lab 6 (continued) | Mid-term (AI off) |
| 8 | 7 | Lab 7 · Label noise and deduplication | — |
| 9 | 8 | Lab 8 · TF-IDF and code-mixed text | — |
| 10 | 9 | Lab 9 · Embeddings, fine-tuning and Indic text | — |
| 11 | 9 | Lab 9 (continued) | — |
| 12 | 10 | Lab 10 · LLM labelling and distillation | — |
| 13 | 11 | Error analysis and ablations (P3) | — |
| 14 | 11 | Solution report (P3) | **P3 due** |
| 15 | Review | P3 presentation | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** first drafts of training scripts and feature code; running many experiments with a coding agent (Claude Code, OpenAI Codex, Gemini CLI) or an open-source ML agent such as AIDE or MLE-STAR; summarising competition write-ups; generating hypotheses for error analysis. Treat an agent's best run as a strong baseline to beat honestly, not as the answer.
- **Do without AI (drills):** design a split from a one-paragraph dataset story; spot leaks in printed code; compute PR-AUC and expected cost by hand from a small table; read a confusion matrix and propose the next experiment. The mid-term and final are AI-off.
- **Verify AI output by:** checking every `fit` call happens inside the CV fold; adversarial validation; re-running with 3 seeds; an ablation for every claimed gain; comparing an agent's validation score with a hidden holdout you never showed it; human review of LLM labels against a gold set.
- **Where AI still fails here:** the leakage patterns in Chapter 2 appear routinely in generated pipelines (scaler or encoder fitted on all data, random split on time-ordered data, duplicates across folds). Agents optimise the number they are shown, so a leaked or mis-specified validation set produces confident, wrong progress; MLE-bench's maintainers had to list a test-feedback result separately for this reason. In Lab 2 you collect and classify every leak you find in assistant-written code.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 40% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 25% |

**Mastery gate.** You pass when you can: (1) given a new dataset and its deployment story, design and justify a validation scheme in 15 minutes without AI; (2) find at least 4 of 5 planted leaks in an unfamiliar pipeline within 45 minutes; (3) show a model whose hidden-holdout score is within its own cross-validation error bars, with an ablation table explaining every gain over a baseline.

## Industry reality

Applied ML engineers build and improve models for fraud, credit risk, search, catalogue quality, content moderation and document processing. Fraud data has the shape of the IEEE-CIS competition (time-ordered, heavily imbalanced, entity-linked); credit-default data has the shape of Home Credit's competition (many related tables, aggregation features). Large companies increasingly start from pretrained backbones and embeddings (DINOv3, sentence-transformers, multilingual encoders from AI4Bharat for Indian languages) rather than training from scratch. Agents now do much of the mechanical work (MLE-bench), which moves the human contribution to validation design, data quality and judgement.

**Interview questions from this course**

1. *Your validation AUC is 0.94 but production AUC is 0.71. What do you check?* Strong answer: leakage (target, temporal, preprocessing, duplicates); split mismatch; adversarial validation for drift; tuning overfit to one validation set; feature availability at serving time; label definition changes.
2. *How do you encode a categorical feature with 50,000 values?* Strong answer: out-of-fold target encoding with smoothing, frequency or hashing, learned embeddings, CatBoost ordered statistics; rare-category handling; the leakage risk and how to test for it.
3. *You have 2,000 labelled images. Fine-tune or linear probe?* Strong answer: probe first as the baseline; domain gap; augmentation; learning-rate choices; the cost of fine-tuning; measuring both with error bars.
4. *Build a classifier for support tickets in English, Hindi and Hinglish.* Strong answer: TF-IDF with character n-grams baseline; multilingual or Indic encoders; label quality; class imbalance; an LLM zero-shot baseline with cost and latency; slice metrics by language.
5. *Fraud is 0.2% of transactions. How do you train and evaluate?* Strong answer: time-based split; PR-AUC and recall at the review team's capacity; class weights; no resampling before the split; threshold by expected cost; calibration if scores feed rules.

## Resources (free first)

- **Courses:** fast.ai Practical Deep Learning — https://course.fast.ai/ ; Kaggle Learn (including Data Leakage) — https://www.kaggle.com/learn ; Stanford CS229 — https://cs229.stanford.edu/
- **Validation and leakage:** scikit-learn "Common pitfalls" — https://scikit-learn.org/stable/common_pitfalls.html ; cross-validation guide — https://scikit-learn.org/stable/modules/cross_validation.html ; Rachel Thomas, "How (and why) to create a good validation set" — https://www.fast.ai/posts/2017-11-13-validation-sets.html ; Kaufman et al., "Leakage in Data Mining" (2012) — https://www.cs.umb.edu/~ding/history/470_670_fall_2011/papers/cs670_Tran_PreferredPaper_LeakingInDataMining.pdf
- **Tabular:** LightGBM — https://github.com/microsoft/LightGBM ; Optuna — https://optuna.readthedocs.io/en/stable/ ; AutoGluon Tabular — https://auto.gluon.ai/stable/tutorials/tabular/index.html ; TabPFN — https://github.com/PriorLabs/TabPFN ; Polars — https://docs.pola.rs/
- **Vision:** timm — https://huggingface.co/docs/timm/index ; torchvision models — https://docs.pytorch.org/vision/stable/models.html ; DINOv3 — https://github.com/facebookresearch/dinov3 ; cleanlab — https://github.com/cleanlab/cleanlab ; Captum — https://captum.ai/tutorials/
- **Text:** Sentence Transformers — https://sbert.net/ ; MTEB leaderboard — https://huggingface.co/spaces/mteb/leaderboard ; Hugging Face Transformers — https://huggingface.co/docs/transformers/index ; SetFit — https://github.com/huggingface/setfit ; AI4Bharat — https://huggingface.co/ai4bharat
- **Competitions and datasets:** IEEE-CIS Fraud Detection — https://www.kaggle.com/competitions/ieee-fraud-detection ; Home Credit Default Risk — https://www.kaggle.com/competitions/home-credit-default-risk ; Shopee Price Match Guarantee — https://www.kaggle.com/competitions/shopee-product-matching ; IndicSentiment — https://huggingface.co/datasets/ai4bharat/IndicSentiment
- **Agents for comparison:** AIDE — https://github.com/WecoAI/aideml ; MLE-bench — https://github.com/openai/mle-bench

## Sources

- Chan et al., "MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering" (arXiv 2410.07095, Oct 2024): o1-preview with AIDE reached at least bronze in 16.9% of 75 competitions — https://arxiv.org/abs/2410.07095 (checked 2026-10)
- MLE-bench leaderboard (README): top entry Famou-Agent 2.0 + Gemini-3-Pro-Preview, 64.44% ± 1.18% any medal (23 Feb 2026); a 77.78% ensemble listed separately because it used test-set feedback; submissions paused April 2026 — https://github.com/openai/mle-bench (checked 2026-10)
- Hollmann et al., "Accurate predictions on small data with a tabular foundation model", *Nature* (Jan 2025) — https://www.nature.com/articles/s41586-024-08328-6 ; TabPFN repository (TabPFN-3.5 default; up to 1,000,000 rows and 20,000 features; weights under non-commercial licences) — https://github.com/PriorLabs/TabPFN (checked 2026-10)
- Siméoni et al., "DINOv3" (arXiv 2508.10104, Aug 2025) — https://arxiv.org/abs/2508.10104 ; Oquab et al., "DINOv2" — https://arxiv.org/abs/2304.07193 (checked 2026-10)
- Grinsztajn, Oyallon and Varoquaux (2022) — https://arxiv.org/abs/2207.08815 (checked 2026-10)
- Northcutt, Athalye and Mueller, "Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks" (2021) — https://arxiv.org/abs/2103.14749 (checked 2026-10)
- Dosovitskiy et al. (ViT) — https://arxiv.org/abs/2010.11929 ; Radford et al. (CLIP) — https://arxiv.org/abs/2103.00020 ; Tschannen et al. (SigLIP 2) — https://arxiv.org/abs/2502.14786 ; Reimers and Gurevych (Sentence-BERT) — https://arxiv.org/abs/1908.10084 ; Muennighoff et al. (MTEB) — https://arxiv.org/abs/2210.07316 ; Warner et al. (ModernBERT) — https://arxiv.org/abs/2412.13663 ; Tunstall et al. (SetFit) — https://arxiv.org/abs/2209.11055 ; Lundberg and Lee (SHAP) — https://arxiv.org/abs/1705.07874 ; Zhang et al. (mixup) — https://arxiv.org/abs/1710.09412 ; Yun et al. (CutMix) — https://arxiv.org/abs/1905.04899 ; Cubuk et al. (RandAugment) — https://arxiv.org/abs/1909.13719 (all checked 2026-10)
- Library versions on PyPI (checked 2026-10): PyTorch 2.14.1, Transformers 5.19.0, sentence-transformers 6.1.0, timm 1.0.30, AutoGluon 1.6.3, Optuna 5.0.0, tabpfn 9.1.0 — https://pypi.org/

_Last reviewed: 2026-10_
