# CS214 · Labs and projects

All work is in Python with NumPy, pandas, scikit-learn and PyTorch, in Jupyter or plain scripts. Every result you report needs: the split you used and why, a baseline, a confidence interval, and a single command that reproduces it. Labs 2, 3, 6 (the tree part), 7 and 9 (the micrograd part) are "from scratch" labs and are done without AI assistance.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Baselines and pipelines | Frame a task on UCI Adult; build majority, rule and logistic baselines inside a `Pipeline` with `ColumnTransformer` | Framing note (unit, target, prediction time, cost of errors) and a baseline table | 3 h |
| 2 · Linear regression from scratch | Normal equations and mini-batch gradient descent in NumPy; scaling; polynomial features | Code matching scikit-learn coefficients within 1e-4, plus loss curves for three learning rates | 4 h |
| 3 · Logistic regression and metrics | Derive and implement logistic regression; confusion-matrix metrics; ROC vs PR curves; calibration and cost-based thresholds | Gradient check under 1e-6 relative error, plus a threshold memo for a 0.5%-positive problem | 5 h |
| 4 · Validation and tuning | k-fold vs group vs time-series CV; nested CV; grid vs random vs Optuna search at an equal budget | A table comparing plain and nested CV estimates, and the search comparison | 4 h |
| 5 · Leakage hunt | Five notebooks with planted leaks (preprocessing, target, temporal, group, duplicate); reproduce scikit-learn's random-label feature-selection demo | Each leak found, explained and fixed, with before-and-after scores | 4 h |
| 6 · Trees and boosting | CART from scratch; then random forest, XGBoost, LightGBM, CatBoost and TabPFN on two tabular datasets | Tree code; a comparison table with confidence intervals; a permutation-importance vs impurity-importance plot | 8 h |
| 7 · k-means and PCA from scratch | k-means++ with Lloyd's algorithm; PCA via SVD; image-patch compression; isolation forest on transactions | Code matching scikit-learn (inertia within 1%, explained variance within 1e-6) and three explained anomalies | 5 h |
| 8 · Features and fairness | Target encoding within folds, time-windowed aggregates, imbalance fixes; a Fairlearn audit of a loan model | Encoding comparison and a fairness report with the trade-off stated | 5 h |
| 9 · Neural networks | Build a micrograd-style autograd engine and train an MLP with it; then PyTorch on Fashion-MNIST | Autograd tests, plus Fashion-MNIST test accuracy above 88% and a four-way regularization ablation | 8 h |
| 10 · Classical vs LLM | Ticket classification with TF-IDF + logistic regression, embeddings + logistic regression, and a zero-shot LLM | Accuracy, macro-F1, latency and cost table, and a half-page decision note | 5 h |

## Projects

### P1 · NumPy ML toolkit with tests (L1, ~6 hours)

**Real-world inspiration:** scikit-learn's estimator API (`fit`, `predict`, `transform`), which most of the Python ML ecosystem copies, and Karpathy's [micrograd](https://github.com/karpathy/micrograd), which shows how far a small, correct implementation can teach.

**What to build:** a tiny library with `LinearRegression` (normal equations and mini-batch GD), `LogisticRegression` (GD with L2), `KMeans` (k-means++ initialization) and `PCA` (SVD), all following the estimator API.

**Acceptance criteria:**
- **Accuracy against scikit-learn:**
  - coefficients within 1e-4 relative error on three datasets, with matched regularization;
  - PCA explained-variance ratios within 1e-6;
  - k-means inertia within 1% when both start from the same initial centres.
- **Gradients:** a numerical gradient check for the logistic loss with relative error below 1e-6.
- **Tests:** at least 25 unit tests running in CI on every push.
- **Derivations:** a README with the derivations in Markdown math.

**Stretch goals:** Newton's method for logistic regression; softmax regression; making one estimator pass scikit-learn's `check_estimator`.

**What it proves to an employer:** you understand the algorithms beneath the library calls well enough to implement and test them. That is what "from scratch" interview rounds and debugging production models both demand.

### P2 · A leakage-proof model tied to a real decision (L2, ~15 hours)

**Real-world inspiration:** delivery apps show customers a promised delivery time, and lenders decide who gets credit. Both are decisions where errors have unequal costs. Leakage that makes such models look better than they are is common enough that the Princeton project lists 648 affected papers ([reproducible.cs.princeton.edu](https://reproducible.cs.princeton.edu/)).

**What to build:** choose a public dataset with a real decision attached. Options are UCI Adult, a public credit-default dataset, or a dataset from [data.gov.in](https://www.data.gov.in/) or [AIKosh](https://aikosh.indiaai.gov.in/). Build the full path: framing, split design, baseline, logistic regression, gradient boosting, calibration, threshold, slice analysis and a model card.

**Acceptance criteria:**
- **Framing:** a written note covering the decision, unit of prediction, prediction time, available features at that time, and a cost matrix.
- **Split and sanity check:** the split (group, time or stratified) is justified and passes a shuffled-label test, scoring chance ± 2 percentage points.
- **Model comparison:** the gradient-boosting model's gain over the baseline is reported with a 95% bootstrap confidence interval.
- **Calibration:** expected calibration error on the test set is ≤ 0.05 after calibration, or the write-up explains why not.
- **Threshold:** chosen from the cost matrix, with the expected cost per 1,000 decisions reported against the baseline.
- **Slices:** metrics for at least three groups (for example region or age band), using Fairlearn, with the trade-off you chose stated plainly.
- **Test-set discipline:** the test set is scored exactly once. Commit a hash of the test predictions with a timestamp.
- **Reproducibility:** a model card and a one-command run with fixed seeds and a pinned environment.

**Stretch goals:** monotonic constraints in LightGBM where domain logic demands them; SHAP explanations for five individual decisions with caveats; a simulated drift scenario and how your monitoring would catch it.

**What it proves to an employer:** that your numbers can be trusted. Data science and ML teams value this above any single algorithm skill.

### P3 · Classical ML vs LLMs for Indian-language support-ticket routing (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Indian consumer apps receive support messages in English, Hindi and code-mixed Hinglish. Routing them to the right team quickly is a real cost and quality problem (*illustrative scenario*). Open Indian-language resources from [AI4Bharat](https://ai4bharat.iitm.ac.in/) and datasets on [AIKosh](https://aikosh.indiaai.gov.in/) make the problem workable. The trade-offs mirror those every team now faces when choosing between a trained model and an LLM call.

**What to build:**
- **Data:** a labelled dataset of at least 2,000 tickets across 6–10 routing classes, from a public source or built by you with written annotation guidelines. Use only synthetic or anonymized text, with no personal data.
- **Systems:** at least four, compared head-to-head: TF-IDF + logistic regression; multilingual sentence embeddings + logistic regression or GBDT; a zero- or few-shot LLM (an API or a local open model); and one of (a) a fine-tuned small transformer or (b) LLM-labelled data distilled into a small classifier.

**Acceptance criteria:**
- **Frozen test set:** at least 500 tickets, labelled before any system is built, and never included in prompts or few-shot examples (a script checks this).
- **Annotation quality:** if you built the data, at least 200 items are double-annotated and Cohen's kappa is reported.
- **Per-system metrics:** macro-F1 with a 95% bootstrap CI, per-language F1, calibration error (after calibration where possible), p95 latency, and cost per 1,000 tickets computed from measured tokens and dated published prices.
- **Robustness:** results on a held-out code-mixed slice and on 100 typo-perturbed tickets.
- **Error analysis:** 50 errors from each of the two best systems, grouped into categories with examples.
- **Decision memo:** at most two pages, recommending one system (or a cascade) for a stated budget and latency target. It covers privacy and where customer text is processed, with reference to India's DPDP Act.
- **Reproducibility:** one-command reruns; pinned prompts, model names and versions; an experiment log (MLflow or similar); a model card for the chosen system.

**Stretch goals:** a cascade (cheap model first, LLM only on low-confidence items) with a cost-vs-accuracy curve; active learning that measurably reduces the labels needed; deployment as a small API with drift monitoring.

**What it proves to an employer:** AI-era judgement. You can decide with evidence when an LLM is worth its cost and risk and when a small classical model is better, and you can defend the choice to engineers, product owners and legal teams.

## Feeds into

- [MLE301 Machine Learning Algorithms from Scratch](../../../03_majors/machine_learning_engineering/year_3/MLE301_machine_learning_algorithms_from_scratch/README.md) (P1 is the starting point), [MLE302 ML System Design](../../../03_majors/machine_learning_engineering/year_3/MLE302_machine_learning_system_design/README.md) and [MLE304 Model Evaluation, Fairness and Robustness](../../../03_majors/machine_learning_engineering/year_3/MLE304_model_evaluation_fairness_and_robustness/README.md).
- [DSC302 Applied ML for Data Scientists](../../../03_majors/data_science/year_3/DSC302_applied_machine_learning_for_data_scientists/README.md) and [DSC305 Feature Engineering and Model Evaluation](../../../03_majors/data_science/year_3/DSC305_feature_engineering_and_model_evaluation/README.md) (P2's evaluation discipline).
- [DLR301 Neural Networks from Scratch](../../../03_majors/deep_learning/year_3/DLR301_neural_networks_from_scratch_autograd/README.md) and [DLR303 Sequence Models and Transformers](../../../03_majors/deep_learning/year_3/DLR303_sequence_models_and_transformers/README.md).
- [AIE301 LLM Fundamentals for Engineers](../../../03_majors/ai_engineering/year_3/AIE301_llm_fundamentals_for_engineers/README.md) and [AIE305 Evaluating LLM Systems](../../../03_majors/ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md) (P3's comparison method).
- [OV04A ML Platform Engineering](../../../04_overlaps/OV04_mlops_ml_platform/OV04A_ml_platform_engineering/README.md).
