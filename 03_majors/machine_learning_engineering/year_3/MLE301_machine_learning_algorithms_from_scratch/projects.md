# MLE301 · Labs and projects

Work in Python with NumPy and SciPy only for your implementations; scikit-learn, XGBoost, LightGBM and `statsmodels` are used only as references to check against. Every lab ships with tests (pytest plus Hypothesis), fixed seeds, and an **AI bug log**: each bug you found in assistant-written code, the test that caught it, and the fix.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Test harness | A reusable kit: seeded dataset generators, a reference-comparison helper with a written tolerance policy, property tests (row-order invariance, scaling behaviour) | `mlkit/testing.py`, the tolerance policy, 10 passing property tests | 3 h |
| 2 · Linear models | OLS by normal equations, QR and `lstsq`; batch, mini-batch and SGD; ridge closed form; lasso by coordinate descent | Coefficients matching `LinearRegression`, `Ridge` and `Lasso` within 10⁻⁵; learning-rate divergence plot | 4 h |
| 3 · Logistic regression and conventions | GD, Newton/IRLS and L-BFGS fits; reproduce `statsmodels` Logit with `C=np.inf` and scikit-learn's default with `C=1.0`; test `liblinear`'s penalised intercept | A table of the 4 fits with coefficients, iterations and run time, plus a paragraph explaining every difference | 4 h |
| 4 · k-NN and Naive Bayes | Brute-force and KD-tree k-NN; multinomial NB on the UCI SMS Spam Collection | Exact prediction match with scikit-learn; timing plot vs dimension; reliability plot showing NB overconfidence | 4 h |
| 5 · SVMs | Pegasos linear SVM; simplified SMO with an RBF kernel on 2-D moons | Decision-boundary plots; support-vector overlap with `SVC` above 90%; a timing plot as n grows | 5 h |
| 6 · CART | Classification and regression trees with Gini, entropy and MSE; cost-complexity pruning | ≥ 99% prediction agreement with `DecisionTreeClassifier` at fixed depth; your α path vs scikit-learn's | 5 h |
| 7 · Random forests and importance | Bagging, feature subsampling, OOB error, permutation importance | Tree-correlation vs `max_features` plot; a demonstration that impurity importance ranks a random ID column highly and permutation importance does not | 4 h |
| 8 · Histogram GBDT | Second-order boosting with binned features, histogram subtraction, early stopping; squared and logistic loss | Library code; log-loss and wall-clock comparison with XGBoost (`tree_method="hist"`) and LightGBM on a public dataset | 8 h (2 weeks) |
| 9 · k-means++ and GMMs | Lloyd's algorithm with k-means++; full-covariance GMM by EM; BIC model selection | Inertia over 50 seeds (random vs k-means++); a monotone log-likelihood test; BIC curve | 4 h |
| 10 · PCA and an MLP | PCA by SVD and randomised SVD; two-layer MLP with He initialisation and Adam | Components matching `PCA` up to sign; MLP within 1 point of `MLPClassifier` on Fashion-MNIST; gradient-check log | 6 h (2 weeks) |

## Projects

### P1 · A verified linear-models engine (L1, ~6 hours)

**Real-world inspiration.** Logistic regression is still a production baseline for click prediction: Facebook's ads team combined boosted-tree features with a logistic-regression model (He et al., 2014). Illustrative scenario: two teams fit "the same" model on the same data and get different coefficients, because one library regularises by default and the other does not.

**What to build.** A small package with `LinearRegression`, `Ridge`, `Lasso` and `LogisticRegression` (binary and softmax), each with closed-form or Newton solvers where they exist and gradient-descent solvers everywhere, plus a CLI that prints a "convention report" for a given scikit-learn configuration (penalty strength, intercept handling, class weights).

**Acceptance criteria**
- Coefficients match scikit-learn within 10⁻⁴ (relative) on 5 seeded datasets under identical regularisation, and match `statsmodels` Logit when `C=np.inf` on non-separable data.
- Analytic gradients pass a central-difference check with relative error below 10⁻⁶.
- Perfectly separable data triggers a clear warning instead of silent divergence.
- Convergence plots for every solver, with iterations and wall-clock time.
- A one-page README explains every convention difference you found, with a minimal code example for each.

**Stretch goals.** Elastic net; sample weights; standard errors and confidence intervals for the unpenalised logistic model, matched against `statsmodels`.

**What it proves to an employer.** You can explain exactly what a model library does and reconcile two "conflicting" results, which is everyday debugging in ML teams.

### P2 · Tree ensembles from scratch (L2, ~15 hours)

**Real-world inspiration.** Gradient-boosted trees power fraud, risk and ranking models across industry, and XGBoost and LightGBM are among the most used ML libraries. Their speed comes from systems ideas (histograms, sparsity-aware splits, cache-aware layouts) described in their papers (Chen and Guestrin, 2016; Ke et al., 2017).

**What to build.** CART (classification and regression), a random forest with OOB error and permutation importance, and a histogram-based gradient-boosting library with second-order gains, L2 leaf regularisation (λ), minimum split gain (γ), shrinkage, row subsampling and early stopping. Benchmark on 3 OpenML datasets of different shapes (for example: many rows and few features; many categorical features; strong class imbalance).

**Acceptance criteria**
- CART agrees with scikit-learn on at least 99% of test predictions at fixed depth and identical settings.
- Your random forest's mean accuracy over 5 seeds is within 1 percentage point of `RandomForestClassifier` on each dataset.
- Your GBDT's test log-loss is within 3% of XGBoost `tree_method="hist"` with matched hyperparameters (depth, learning rate, rounds, λ, γ, bins).
- Histogram split search is at least 5× faster than your exact split search at 100,000 rows; both timings reported.
- A profile identifies your library's main bottleneck, with a short explanation of how XGBoost or LightGBM avoids it.

**Stretch goals.** Leaf-wise growth with `num_leaves` (LightGBM style); missing-value default directions (XGBoost style); the GBDT-leaves → logistic-regression feature transform from the Facebook paper, with its measured effect on one dataset.

**What it proves to an employer.** You understand the most important model family for tabular data down to the systems level, so you can tune it, debug it and explain it.

### P3 · mini-learn: a tested, benchmarked ML library (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** scikit-learn began in 2007 as a Google Summer of Code project and became the reference API for classical ML (scikit-learn "About us"; Pedregosa et al., 2011). Its estimator checks, documentation and benchmark discipline are what make it trustworthy. Benchmarks such as OpenML-CC18 exist because single-dataset comparisons mislead.

**What to build.** Package your course work into an installable library (`pyproject.toml`) with at least 12 estimators: linear and logistic regression, Naive Bayes, k-NN, linear SVM, CART, random forest, histogram GBDT, k-means, GMM, PCA and an MLP. Add continuous integration (for example GitHub Actions), API documentation, and a benchmark study.

**Acceptance criteria**
- At least 8 estimators pass scikit-learn's `check_estimator` (list any skipped checks with reasons).
- Test coverage of at least 85%; property tests for every estimator; CI runs on every push.
- Benchmark on at least 15 OpenML-CC18 classification tasks with 5×2 repeated cross-validation; report accuracy and log-loss for your 4 strongest classifiers against their scikit-learn, XGBoost or LightGBM equivalents, with a Nadeau–Bengio corrected t-test.
- No estimator is more than 10× slower than its reference at 50,000 rows (or the gap is explained with a profile).
- A written "decision guide" (2–3 pages) recommends algorithms by data size, dimension, latency budget and interpretability, citing your own benchmark numbers.
- The AI bug log from the whole course is included, grouped by bug type.

**Stretch goals.** Numba-accelerated hot loops with measured speed-ups; ONNX export for your linear models and GBDT; a model card for one estimator on one dataset.

**What it proves to an employer.** You can build ML software to library standards: correct, tested, documented, benchmarked honestly and fast enough. That is the evidence hiring managers for ML engineering and ML platform roles look for.

## Feeds into

- [MLE401 MLOps](../../year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md): your packaged library becomes a model you deploy, monitor and retrain.
- [MLE305 Applied ML](../MLE305_applied_ml_tabular_vision_and_text/README.md): the decision guide from P3 is your starting point for tabular baselines.
- [MLE403 Ranking and Recommendation](../../year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md): your GBDT extends to LambdaMART-style learning to rank.
- [MLE304 Evaluation, Fairness and Robustness](../MLE304_model_evaluation_fairness_and_robustness/README.md): the NB overconfidence from Lab 4 returns as calibration.
- [DLR301 Neural Networks from Scratch](../../../deep_learning/year_3/DLR301_neural_networks_from_scratch_autograd/README.md): Chapter 11's MLP grows into a full autograd engine.
- [CAR301 Career Lab I](../../../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md): P3 is a strong open-source portfolio piece.
