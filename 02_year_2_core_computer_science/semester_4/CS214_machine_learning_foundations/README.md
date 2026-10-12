# CS214 · Machine Learning Foundations

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 2 · 4 | 4 (≈ 120 hours) | L1 → L3 | [CS206](../../semester_3/CS206_mathematics_for_machine_learning/README.md), [FND101](../../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md) | [MLE301](../../../03_majors/machine_learning_engineering/year_3/MLE301_machine_learning_algorithms_from_scratch/README.md), [DSC302](../../../03_majors/data_science/year_3/DSC302_applied_machine_learning_for_data_scientists/README.md), [DSC305](../../../03_majors/data_science/year_3/DSC305_feature_engineering_and_model_evaluation/README.md), [DLR301](../../../03_majors/deep_learning/year_3/DLR301_neural_networks_from_scratch_autograd/README.md), [AIE301](../../../03_majors/ai_engineering/year_3/AIE301_llm_fundamentals_for_engineers/README.md), [MLE304](../../../03_majors/machine_learning_engineering/year_3/MLE304_model_evaluation_fairness_and_robustness/README.md) |

Part of [Year 2 · Core Computer Science](../../README.md). It uses the linear algebra, calculus, probability and optimization from [CS206](../../semester_3/CS206_mathematics_for_machine_learning/README.md) constantly.

## Why this course matters now

Large language models get the headlines, but much of the machine learning that runs businesses is still classical: credit scoring, fraud flags, delivery-time estimates, demand forecasts, churn models. On tabular data, gradient-boosted trees still dominate. In the 2024 *State of Machine Learning Competitions* report, LightGBM, CatBoost and XGBoost appeared in 16, 13 and 8 winning solutions respectively. Tabular foundation models such as TabPFN (*Nature*, 2025) are new challengers. LLMs add zero-shot classifiers and embeddings as features. They also make it easier than ever to produce a model that looks good and is wrong. The Princeton leakage project lists 41 papers across 30 fields that found leakage errors affecting 648 papers. Notebook assistants (Jupyter AI, GitHub Copilot and others) will write a full scikit-learn pipeline on request. What they cannot do for you is frame the problem, choose a split that matches reality, spot leakage, pick a metric that reflects the cost of mistakes, and decide whether an LLM, a gradient-boosted tree or a rule is the right tool.

## Learning outcomes

By the end you can:

1. **Frame** a business question as an ML problem (unit of prediction, target, decision, cost of errors) and **build** a baseline before any model.
2. **Derive and implement** linear and logistic regression with gradient descent in NumPy, and **match** scikit-learn's results.
3. **Explain** bias–variance, **diagnose** under- and overfitting with learning curves, and **apply** L1, L2 and early stopping.
4. **Design** an evaluation protocol (group, time-series or stratified splits; nested cross-validation) and **detect** the main leakage types.
5. **Train, tune and interpret** trees, random forests and gradient boosting, and **explain** why they win on tabular data.
6. **Use** k-means, PCA and anomaly detection, and **judge** when their output means something.
7. **Implement** backpropagation for a small MLP and **train** a network in PyTorch.
8. **Compare** a classical model with an LLM-based approach on accuracy, calibration, cost, latency and privacy, and **recommend** one with evidence.
9. **Document** a model with a model card and a reproducible experiment record.

## Chapters and lessons

### Chapter 1 · Framing, data and baselines (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The ML landscape | Supervised, unsupervised, self-supervised and reinforcement learning; where LLMs sit | Classify ten product features by learning type |
| 1.2 Framing a problem | Unit of prediction, label definition, when a prediction is made, the decision it drives, the cost of errors | Frame "predict late food deliveries" for a delivery platform (illustrative) |
| 1.3 Baselines and the two cultures | Majority-class, mean and rule baselines; prediction vs explanation (Breiman, 2001) | Build three baselines for a dataset before any model |
| 1.4 The scikit-learn API | Estimators, `fit`/`predict`/`transform`, `Pipeline`, `ColumnTransformer` | Build an end-to-end pipeline on the UCI Adult dataset |

**Check your understanding:** (1) Why must you know *when* a prediction is made before you choose features? (2) A model beats the baseline by 0.3% accuracy: what else do you need to know? (3) When is a hand-written rule better than a model?

### Chapter 2 · Linear regression and gradient descent (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Least squares | Model, loss, normal equations, geometric view as projection | Solve with normal equations in NumPy |
| 2.2 Gradient descent | Batch, stochastic and mini-batch GD; learning rate; convergence; feature scaling | Implement GD and plot loss curves for three learning rates |
| 2.3 Features and non-linearity | Polynomial features, interactions, one-hot encoding | Fit housing prices with polynomial features and watch overfitting appear |
| 2.4 Regression metrics and residuals | MSE, RMSE, MAE, R², residual plots, heteroscedasticity | Diagnose a model from its residual plot |

**Check your understanding:** (1) Why does unscaled data slow gradient descent? (2) When would you prefer MAE to RMSE? (3) Why can R² go negative on a test set?

### Chapter 3 · Logistic regression and classification metrics (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Logistic regression | Sigmoid, log-loss, its gradient, softmax for many classes | Derive the gradient by hand, implement it, and check it numerically |
| 3.2 Confusion-matrix metrics | Precision, recall, F1, specificity; base rates | Compute all metrics by hand for a fraud example with a 0.5% fraud rate |
| 3.3 Ranking metrics | ROC-AUC vs PR-AUC; why PR-AUC suits rare positives | Plot both curves for an imbalanced dataset and explain the difference |
| 3.4 Thresholds and calibration | Cost-based thresholds, reliability diagrams, Platt and isotonic calibration | Choose a threshold from a cost matrix and calibrate a model |

**Check your understanding:** (1) Why is 99% accuracy meaningless for fraud detection at a 0.5% base rate? (2) When does a calibrated probability matter more than ranking quality? (3) Why can two models with the same AUC lead to very different business outcomes?

### Chapter 4 · Generalization, regularization and model selection (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Bias and variance | Decomposition of expected error, learning curves, validation curves | Diagnose four models from their learning curves |
| 4.2 Regularization | L2 (ridge), L1 (lasso), elastic net; geometry of sparsity; early stopping | Show L1 driving coefficients to zero on 100 noisy features |
| 4.3 Cross-validation | k-fold, stratified, group and time-series splits; nested CV for honest tuning | Compare plain and nested CV scores on a small dataset |
| 4.4 Hyperparameter search | Grid, random and Bayesian search (Optuna); search budgets | Tune a model three ways with the same budget and compare |
| 4.5 Beyond the classical picture | Double descent in overparameterized models (Belkin et al., 2019) | Reproduce a double-descent curve with random features |

**Check your understanding:** (1) Why does tuning on the test set make its score optimistic? (2) When does more data help, and when does a bigger model help? (3) Why does L1 produce sparse solutions and L2 does not?

### Chapter 5 · Honest evaluation and data leakage (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Leakage taxonomy | Target leakage, train–test contamination, preprocessing on all data, temporal leakage, duplicate and group leakage (Kapoor and Narayanan, 2023) | Find the leaks in five planted notebooks |
| 5.2 Pipelines as protection | Fitting transformers only on training folds; scikit-learn's "common pitfalls" guide | Reproduce the scikit-learn demo where feature selection on all data inflates accuracy on random labels, then fix it |
| 5.3 Splits that match reality | Time-based splits, grouping by user, patient or store; the shuffled-label sanity test | Re-evaluate a model with a group split and explain the drop |
| 5.4 Uncertainty in results | Bootstrap confidence intervals, paired comparisons, multiple-comparison traps | Report two models' scores with 95% intervals |
| 5.5 Distribution shift | Covariate shift, label shift, concept drift; slice-based evaluation | Evaluate one model on three city slices and on a later time window |

**Check your understanding:** (1) Why is a model that scores 0.99 on day one usually a leakage alarm, not a celebration? (2) Why must a hospital model split by patient rather than by visit? (3) What does a shuffled-label test detect?

### Chapter 6 · Trees and ensembles (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Decision trees | CART, Gini and entropy, depth and pruning, variance of single trees | Implement a decision tree from scratch for classification |
| 6.2 Bagging and random forests | Bootstrap aggregation, feature subsampling, out-of-bag error (Breiman, 2001) | Compare a tree, a forest and OOB vs CV error |
| 6.3 Gradient boosting | Additive models on residuals and gradients; shrinkage; histogram binning; XGBoost, LightGBM, CatBoost (categorical handling) | Tune LightGBM with early stopping and compare all three libraries |
| 6.4 Why trees win on tabular data | Irregular target functions, many uninformative features, and why rotation-invariant MLPs suffer on tabular columns (Grinsztajn et al., 2022); TabPFN as a challenger | Compare GBDT, an MLP and TabPFN on a small table |
| 6.5 Interpretation | Impurity vs permutation importance, partial dependence, SHAP values; their failure modes | Show impurity importance favoring a high-cardinality noise feature |

**Check your understanding:** (1) Why does bagging reduce variance but not bias? (2) Why does boosting need a learning rate and early stopping? (3) Why can a feature importance chart mislead a business decision?

### Chapter 7 · Margins, kernels and neighbours (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Support vector machines | Maximum margin, hinge loss, soft margin `C` | Visualize decision boundaries as `C` changes |
| 7.2 The kernel trick | RBF and polynomial kernels, `gamma`, cost on large datasets | Fit a non-linear boundary on concentric circles |
| 7.3 k-nearest neighbours | Distance metrics, scaling, the curse of dimensionality | Measure how k-NN accuracy decays as noise dimensions are added |
| 7.4 Naive Bayes for text | Bag-of-words, TF-IDF, multinomial NB as a strong text baseline | Build a spam baseline in 20 lines |

**Check your understanding:** (1) Why do SVMs need feature scaling? (2) Why do neighbours stop being "near" in high dimensions? (3) Why is Naive Bayes a good baseline despite its false independence assumption?

### Chapter 8 · Unsupervised learning (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 k-means | Lloyd's algorithm, k-means++, inertia, silhouette, choosing k; failure on non-spherical clusters | Implement k-means from scratch and compare with scikit-learn |
| 8.2 Other clustering | Hierarchical clustering, DBSCAN, Gaussian mixtures in outline | Cluster the same data three ways and justify one |
| 8.3 PCA | Covariance, eigenvectors and SVD, explained variance, reconstruction error | Implement PCA with SVD and compress image patches |
| 8.4 Visualization and anomalies | t-SNE and UMAP for visualization only; isolation forest | Find anomalies in a transaction log and explain three of them |

**Check your understanding:** (1) Why can k-means always "find" clusters, even in uniform noise? (2) Why should you not read distances off a t-SNE plot? (3) Why must data be centred before PCA?

### Chapter 9 · Features, messy data and fairness (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Missing data and encodings | Imputation strategies, missingness indicators, one-hot vs target encoding (fit inside folds) | Compare three encodings for a high-cardinality "city" feature |
| 9.2 Text, dates and aggregates | TF-IDF, date parts, cyclical encoding, time-windowed aggregates without peeking into the future | Build features for a delivery-time model with strict time cut-offs |
| 9.3 Imbalanced data | Class weights, resampling, threshold moving; why resampling distorts calibration | Compare three fixes on a 1%-positive dataset |
| 9.4 Fairness basics | Group metrics (demographic parity, equalized odds), trade-offs, Fairlearn | Audit a loan-approval model across groups and report the trade-off |

**Check your understanding:** (1) Why must target encoding be fitted within cross-validation folds? (2) Why does oversampling change predicted probabilities? (3) Why can't you satisfy every fairness metric at once?

### Chapter 10 · Neural networks (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 From perceptron to MLP | Neurons, activations (ReLU, sigmoid, GELU), universal approximation in words | Train an MLP on a 2-D toy problem and watch the boundary bend |
| 10.2 Backpropagation | Computational graphs, chain rule, reverse-mode autodiff (micrograd) | Build a scalar autograd engine and train a tiny MLP with it |
| 10.3 Training in PyTorch | Tensors, `nn.Module`, loss, optimizers (SGD with momentum, Adam), data loaders | Train Fashion-MNIST to above 88% test accuracy |
| 10.4 Training well | Initialization, batch size, learning-rate schedules, dropout, weight decay, early stopping | Run an ablation of four regularizers and report the effects |
| 10.5 Representations | Learned features, embeddings, transfer learning in outline | Use a pretrained image model as a feature extractor plus logistic regression |

**Check your understanding:** (1) Why does backprop cost about the same as a forward pass? (2) Why do networks rarely beat gradient boosting on small tabular datasets? (3) What does a training loss falling while validation loss rises tell you, and what do you do next?

### Chapter 11 · Where LLMs fit, and shipping a responsible model (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 From features to foundation models | Self-supervised pretraining, transformers in one picture ("Attention Is All You Need", 2017), instruction tuning and RLHF (InstructGPT, 2022) | Explain the pipeline from raw text to a chat model in one page |
| 11.2 Scaling, briefly | Kaplan et al. (2020) and Chinchilla (2022): loss vs parameters, data and compute | Read both abstracts and state what Chinchilla changed |
| 11.3 LLMs inside classical ML | Sentence embeddings as features; zero- and few-shot classification; LLM-assisted labeling | Classify support tickets three ways: TF-IDF + logistic regression, embeddings + logistic regression, zero-shot LLM |
| 11.4 Choosing the tool | Accuracy, calibration, cost per 1,000 predictions, latency, privacy, data residency, drift | Write a decision memo for the ticket task |
| 11.5 Reproducibility and documentation | Seeds and environment pinning, experiment tracking (MLflow), model cards (Mitchell et al., 2019) | Write a model card for your best model |

**Check your understanding:** (1) When is a zero-shot LLM a better first model than a trained classifier? (2) Why can't you trust an LLM's self-reported confidence as a probability without checking calibration? (3) Why does sending customer text to a third-party API raise legal questions under India's DPDP Act?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: baselines and pipeline | Baseline report |
| 2 | 2 | Lab 2: linear regression from scratch | Matches scikit-learn |
| 3 | 3 | Lab 3: logistic regression and metrics | Gradient check, threshold memo |
| 4 | 4 | Lab 4: CV and tuning | Nested CV comparison; P1 due |
| 5 | 5 | Lab 5: leakage hunt | Five leaks found and fixed |
| 6 | 6 | Lab 6: trees from scratch | Tree implementation |
| 7 | 6 | Lab 6: boosting | GBDT vs forest vs TabPFN table; P2 starts |
| 8 | 7 | Kernels and k-NN exercises | Boundary plots |
| 9 | 8 | Lab 7: k-means and PCA from scratch | Matches scikit-learn |
| 10 | 9 | Lab 8: features and fairness | Fairness audit; P2 due |
| 11 | 10 | Lab 9: micrograd | Working autograd |
| 12 | 10 | Lab 9: PyTorch | Fashion-MNIST results; P3 design review |
| 13 | 11 | Lab 10: classical vs LLM | Three-way comparison |
| 14 | 11 | P3 completion | P3 memo and model card |
| 15 | Review and exam | — | Written exam, derivation oral |

## Working with AI in this course

- **Use AI for:** exploratory plots and data-cleaning code; boilerplate pipelines; explaining library errors and parameters; generating synthetic datasets for experiments; a second reviewer that you ask to look for leakage (then check every claim yourself).
- **Do without AI (drills):** deriving gradients for linear and logistic regression; implementing linear regression, logistic regression, k-means, PCA, a decision tree and micrograd in NumPy; computing precision, recall and F1 by hand from a confusion matrix; drawing the split strategy for a dataset before writing code.
- **Verify AI output by:** matching from-scratch implementations to scikit-learn within 1e-4; running the shuffled-label test (scores must fall to chance); confirming every transformer sits inside the pipeline and the split respects groups and time; touching the test set exactly once and recording when; reporting confidence intervals, not single numbers.
- **Where AI still fails here:** leakage is subtle enough that published peer-reviewed work gets it wrong (the 648 affected papers above). Test any assistant's pipeline for a grouped or time-ordered dataset yourself: check whether it used a group or time split and fitted preprocessing inside folds, and record what you find. LLM zero-shot classifiers also need calibration and slice checks before their scores mean anything.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 30% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Written exam (derivations, metric reasoning, leakage spotting) | 20% |
| Oral: derive and explain a model on the whiteboard | 10% |

**Mastery gate:** you pass when you can, without AI help, (a) derive the gradient of the logistic loss and implement logistic regression that matches scikit-learn; (b) take an unseen dataset and a stated decision, and within three hours deliver a leakage-free pipeline, a justified split, a baseline, a tuned gradient-boosting model, calibrated probabilities, a cost-based threshold and confidence intervals; and (c) find at least four of five leaks planted in a colleague's notebook.

## Industry reality

Gradient-boosted trees remain the default on tabular data in competitions (ML Contests, 2024), and Airbnb has published how it moved search ranking from boosted trees to neural networks (KDD 2019). India's AI ecosystem gives learners real data:

- **AIKosh:** the IndiaAI platform listed over 16,000 datasets and 361 models in October 2026.
- **data.gov.in:** publishes open government data.
- **AI4Bharat (IIT Madras):** releases open datasets and models for Indian languages.

Interview questions from this course:

1. **"Explain the bias–variance trade-off with an example."** Cover the error decomposition, a high-bias linear model vs a high-variance deep tree, how learning curves show which you have, and the specific fixes for each.
2. **"Our fraud model has 99% accuracy. Is it good?"** Cover the base rate, the confusion matrix, precision/recall and PR-AUC, the cost of false negatives vs false positives, and threshold choice.
3. **"How do you prevent data leakage?"** Name concrete leak types, pipelines fitted inside folds, group and time splits, auditing features for "known only after the event", and suspicion of scores that are too good.
4. **"When would you use gradient boosting, a neural network, or an LLM?"** Tabular means GBDT first. Images, audio and text at scale mean neural networks. Few labels, text and fast iteration favour an LLM or embeddings, weighed against cost, latency, privacy and calibration. Always compare against a baseline.
5. **"L1 vs L2 regularization: what's the difference, and when does L1 help?"** Cover the constraint geometry (diamond vs circle), sparsity and feature selection, behavior with correlated features, and elastic net.

## Resources (free first)

- **Courses:**
  - [Stanford CS229](https://cs229.stanford.edu/) ([main notes](https://cs229.stanford.edu/main_notes.pdf), [2018 lectures](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU))
  - NPTEL [Introduction to Machine Learning](https://nptel.ac.in/courses/106106139) (Prof. Balaraman Ravindran, IIT Madras)
  - [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
  - [Kaggle Learn](https://www.kaggle.com/learn)
- **Books (free online):**
  - [ISLP](https://www.statlearning.com/) (primary text)
  - [The Elements of Statistical Learning](https://hastie.su.domains/ElemStatLearn/)
  - Murphy, [Probabilistic Machine Learning: An Introduction](https://probml.github.io/pml-book/book1.html)
  - Bishop, [Pattern Recognition and Machine Learning](https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/)
  - [Dive into Deep Learning](https://d2l.ai/)
- **Neural networks:** Karpathy, [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) and [micrograd](https://github.com/karpathy/micrograd); [3Blue1Brown neural networks](https://www.3blue1brown.com/topics/neural-networks); [PyTorch tutorials](https://pytorch.org/tutorials/).
- **Documentation:** [scikit-learn](https://scikit-learn.org/stable/) (incl. [common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)), [XGBoost](https://xgboost.readthedocs.io/), [LightGBM](https://lightgbm.readthedocs.io/), [CatBoost](https://catboost.ai/docs/), [Optuna](https://optuna.org/), [Fairlearn](https://fairlearn.org/), [SHAP](https://shap.readthedocs.io/), [MLflow](https://mlflow.org/docs/latest/), [Sentence Transformers](https://sbert.net/).
- **Papers:**
  - [Leakage and the reproducibility crisis](https://reproducible.cs.princeton.edu/)
  - [Why do tree-based models still outperform deep learning on tabular data?](https://arxiv.org/abs/2207.08815)
  - [TabPFN (Nature 2025)](https://www.nature.com/articles/s41586-024-08328-6)
  - [XGBoost](https://arxiv.org/abs/1603.02754)
  - [Random Forests](https://link.springer.com/article/10.1023/A:1010933404324)
  - [Statistical Modeling: The Two Cultures](https://projecteuclid.org/journals/statistical-science/volume-16/issue-3/Statistical-Modeling--The-Two-Cultures-with-comments-and-a/10.1214/ss/1009213726.full)
  - [Model Cards](https://arxiv.org/abs/1810.03993)
  - [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
  - [Scaling Laws](https://arxiv.org/abs/2001.08361)
  - [Chinchilla](https://arxiv.org/abs/2203.15556)
  - [InstructGPT](https://arxiv.org/abs/2203.02155)
  - [Applying Deep Learning to Airbnb Search](https://arxiv.org/abs/1810.09591)
- **Data (India and global):** [AIKosh](https://aikosh.indiaai.gov.in/), [data.gov.in](https://www.data.gov.in/), [AI4Bharat](https://ai4bharat.iitm.ac.in/), [UCI Adult](https://archive.ics.uci.edu/dataset/2/adult).

## Sources

All checked 12 Oct 2026.
- [scikit-learn 1.9.1 documentation](https://scikit-learn.org/stable/) (release September 2026).
- [ML Contests: State of Machine Learning Competitions 2024](https://mlcontests.com/state-of-machine-learning-competitions-2024/): GBDT counts in winning solutions.
- [Princeton: Leakage and the reproducibility crisis in ML-based science](https://reproducible.cs.princeton.edu/): 41 papers, 30 fields, 648 affected papers.
- [TabPFN, Nature 2025](https://www.nature.com/articles/s41586-024-08328-6).
- [Jupyter AI documentation](https://jupyter-ai.readthedocs.io/).
- [AIKosh](https://aikosh.indiaai.gov.in/) dataset and model counts; [AI4Bharat](https://ai4bharat.iitm.ac.in/).
- [Airbnb, Applying Deep Learning to Airbnb Search](https://arxiv.org/abs/1810.09591) (KDD 2019).

_Last reviewed: 2026-10_
