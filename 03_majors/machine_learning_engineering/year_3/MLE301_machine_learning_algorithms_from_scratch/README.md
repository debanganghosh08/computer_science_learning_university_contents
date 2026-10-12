# MLE301 · Machine Learning Algorithms from Scratch

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L4 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [MLE401](../../year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md), [MLE305](../MLE305_applied_ml_tabular_vision_and_text/README.md), [MLE403](../../year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md), [DLR301](../../../deep_learning/year_3/DLR301_neural_networks_from_scratch_autograd/README.md) |

## Why this course matters now

Most production ML outside language and vision is still classical: logistic regression for scorecards and click prediction, gradient-boosted trees for fraud, risk, pricing and ranking. On medium-sized tabular data, tree-based models still beat deep networks in a careful 45-dataset benchmark (Grinsztajn et al., 2022). Coding assistants such as GitHub Copilot, Claude Code and Cursor now write a k-means or a decision tree in seconds, so typing the algorithm is no longer the skill. The skill is knowing what the library is actually doing. For example, scikit-learn's `LogisticRegression` applies L2 regularisation by default (`C=1.0`), so its coefficients are not the textbook maximum-likelihood estimate that `statsmodels` reports. The engineer who can explain that gap, derive XGBoost's split gain, and predict when k-means will fail is the one trusted to debug a model that misbehaves in production.

## Learning outcomes

By the end you can:

1. **Implement** 12 classical algorithms in vectorised NumPy and **verify** each against scikit-learn, XGBoost or LightGBM within a stated numerical tolerance.
2. **Derive** the loss, gradient and update rule of linear, logistic and softmax regression, SVMs, GMMs and a two-layer network, and **check** every derivation numerically.
3. **Explain** why a library's result differs from yours (regularisation conventions, intercept handling, tie-breaking, initialisation) and **reproduce** the library's exact behaviour on purpose.
4. **Derive** the second-order split gain used by XGBoost and **implement** a histogram-based gradient-boosting library.
5. **Compare** algorithms by time and memory complexity, measure both, and **predict** which one fits a given data size and shape.
6. **Diagnose** failure modes: non-convergence, ill-conditioning, collapsed GMM components, impurity-importance bias, the curse of dimensionality.
7. **Design** a test harness (reference comparison, property-based tests, gradient checks) that catches the subtle bugs AI-generated ML code contains.
8. **Benchmark** estimators fairly across many datasets with repeated cross-validation and a corrected significance test.

## Chapters and lessons

### Chapter 1 · The from-scratch toolkit (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Vectorised NumPy | Broadcasting, `einsum`, memory layout, avoiding Python loops; float32 vs float64 | Rewrite a loop-based pairwise-distance function; measure a 100× speed-up |
| 1.2 The estimator contract | scikit-learn's `fit` / `predict` / `get_params` API, `random_state`, input validation | Write a `MeanRegressor` that passes `check_estimator` |
| 1.3 Tolerances and references | Absolute vs relative error, `np.testing.assert_allclose`, when exact equality is impossible | Write a tolerance policy for your course library |
| 1.4 Property-based testing | Hypothesis strategies for random matrices, invariants (permutation invariance, scaling) | A property test that any regressor's predictions are invariant to row order |

**Check your understanding:** Why can two correct implementations of the same algorithm disagree in the 7th decimal place? Which invariants should every classifier satisfy, whatever its algorithm? Why is matching a reference on one dataset weak evidence?

### Chapter 2 · Linear regression and gradient descent (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Closed form | Normal equations vs QR vs `lstsq`; why the explicit inverse is unstable | Fit California Housing three ways; compare errors and run time |
| 2.2 Gradient descent | Batch, mini-batch and stochastic GD; learning rate from the Lipschitz constant | Plot loss curves for 4 learning rates; find the divergence threshold |
| 2.3 Scaling and conditioning | Standardisation, condition number, why unscaled features make GD zig-zag | Show iterations-to-converge before and after scaling |
| 2.4 Ridge and lasso | L2 closed form; lasso by coordinate descent with soft-thresholding; elastic net | Match `Ridge` and `Lasso` coefficient paths within 10⁻⁵ |
| 2.5 Diagnostics | Residual plots, leverage, heteroscedasticity, multicollinearity (VIF) | Explain an absurd coefficient caused by two collinear features |

**Check your understanding:** Why does lasso produce exact zeros while ridge does not? When is SGD preferable to a closed-form solve? Why must the scaler be fitted only on training data?

### Chapter 3 · Logistic and softmax regression (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 From likelihood to loss | Bernoulli likelihood, cross-entropy, convexity, the gradient Xᵀ(σ(Xw) − y) | Derive and gradient-check by finite differences |
| 3.2 Numerical stability | Stable sigmoid, log-sum-exp, clipping log(0) | Make a naive implementation overflow; fix it |
| 3.3 Newton and IRLS | Hessian XᵀSX, iteratively reweighted least squares; L-BFGS via `scipy.optimize` | Converge in under 10 Newton steps; compare with GD |
| 3.4 Library conventions | `C` vs λ, `l1_ratio` (replaces `penalty` from scikit-learn 1.8), `liblinear` regularising the intercept, class weights | Reproduce `statsmodels` Logit with `C=np.inf`; explain the gap at `C=1.0` |
| 3.5 Softmax regression | Multinomial vs one-vs-rest, the softmax Jacobian | Classify Fashion-MNIST; match `LogisticRegression` accuracy within 0.5 points |

**Check your understanding:** Why does perfectly separable data make unregularised logistic regression diverge? Why does Newton's method converge in few iterations yet scale badly with feature count? What does a class weight do to the loss?

### Chapter 4 · k-nearest neighbours and Naive Bayes (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 k-NN | Distance metrics, majority vs distance-weighted votes, choosing k by validation | Brute-force k-NN; match `KNeighborsClassifier` predictions exactly |
| 4.2 Search structures | KD-trees, ball trees; why they degrade in high dimensions | Time brute force vs KD-tree at d = 2, 10, 50, 200 |
| 4.3 Curse of dimensionality | Distance concentration; why approximate nearest-neighbour search (HNSW) exists | Plot max/min distance ratio vs dimension |
| 4.4 Naive Bayes | Gaussian, multinomial and Bernoulli variants; Laplace smoothing; log-space sums | Multinomial NB on the UCI SMS Spam Collection vs `MultinomialNB` |
| 4.5 Why "naive" works | Ranking vs calibrated probabilities under correlated features | Show NB's accuracy is good but its probabilities are overconfident |

**Check your understanding:** Why does k-NN need feature scaling while Naive Bayes does not? Why does a KD-tree lose to brute force in 200 dimensions? Why can a model with wrong independence assumptions still classify well?

### Chapter 5 · Support vector machines (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Maximum margin | Hard and soft margin, hinge loss, the role of C | Plot margins for C = 0.01, 1, 100 |
| 5.2 Primal by SGD | Pegasos (Shalev-Shwartz et al.) for linear SVMs | Match `LinearSVC` accuracy on a text dataset |
| 5.3 The dual and kernels | Lagrangian dual, support vectors, kernel trick, RBF and polynomial kernels | Show only support vectors carry non-zero α |
| 5.4 SMO | Platt's sequential minimal optimisation (simplified version) | Simplified SMO with RBF on 2-D moons; compare support vectors with `SVC` |
| 5.5 Cost and alternatives | O(n²) kernel memory; random Fourier features as an approximation | Time `SVC` vs `LinearSVC` vs RFF + linear model as n grows |

**Check your understanding:** Why do kernel SVMs struggle beyond about 100,000 rows? How do logistic regression and a linear SVM differ in loss and output? What happens to the support-vector count as C grows?

### Chapter 6 · Decision trees (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 CART | Recursive binary splitting; Gini, entropy and MSE criteria | Grow a tree on Titanic-style data by hand for two levels |
| 6.2 Fast split search | Sorting once per feature, prefix sums, thresholds at midpoints, O(n log n) per feature | Implement the scan; profile it |
| 6.3 Stopping and pruning | `max_depth`, `min_samples_leaf`, cost-complexity pruning (α path) | Reproduce scikit-learn's `ccp_alpha` path |
| 6.4 Categories and missing values | One-hot vs ordinal vs partition splits; missing-value routing | Compare three categorical encodings on one dataset |
| 6.5 Instability | High variance, sensitivity to small data changes | Retrain on 20 bootstrap samples; count distinct root splits |

**Check your understanding:** Why is a single deep tree a low-bias, high-variance model? Why does the midpoint threshold convention matter when comparing with scikit-learn? Why is greedy splitting not globally optimal?

### Chapter 7 · Bagging and random forests (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Bagging | Bootstrap, variance reduction ρσ² + (1 − ρ)σ²/B (ESL §15.2) | Measure prediction variance vs number of trees |
| 7.2 Random forests | Feature subsampling (`max_features`) to decorrelate trees (Breiman, 2001) | Measure average tree correlation vs `max_features` |
| 7.3 Out-of-bag error | OOB estimates as free validation | Compare OOB error with 5-fold CV |
| 7.4 Importance | Impurity importance bias toward high-cardinality features (Strobl et al., 2007); permutation importance | Add a random ID column; watch impurity importance rank it highly |
| 7.5 Extra-trees | Random thresholds, speed vs accuracy | Benchmark against your random forest |

**Check your understanding:** Why does adding trees never increase a random forest's variance but can stop helping? Why does `max_features` matter more than tree count? Why is permutation importance computed on held-out data?

### Chapter 8 · Gradient boosting and its industrial engines (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Functional gradient descent | Friedman (2001): fitting trees to negative gradients; squared loss = residual fitting | Boosting with stumps on 1-D data; animate the fit |
| 8.2 Shrinkage and subsampling | Learning rate vs tree count, stochastic gradient boosting, early stopping | Plot validation loss for 3 learning rates |
| 8.3 Second-order boosting | XGBoost's regularised objective γT + ½λ‖w‖², leaf weight −G/(H + λ), split gain | Derive the gain on paper; check with a 6-row example |
| 8.4 Histogram methods | Feature binning, gradient histograms, histogram subtraction | Implement histogram split search; compare speed with exact search |
| 8.5 LightGBM and CatBoost | Leaf-wise growth, GOSS and EFB (Ke et al., 2017); ordered boosting, ordered target statistics, oblivious trees (Prokhorenkova et al.) | Train all three on one dataset; explain differences in depth and speed |
| 8.6 XGBoost systems tricks | Sparsity-aware split finding, weighted quantile sketch, column blocks and cache-aware access (Chen and Guestrin, 2016) | Profile your library vs XGBoost `tree_method="hist"`; name the bottleneck |

**Check your understanding:** Why does XGBoost need the Hessian when gradient boosting with squared loss does not? Why can leaf-wise growth overfit small data? What is "prediction shift", and how does ordered boosting avoid it?

### Chapter 9 · k-means and Gaussian mixtures (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Lloyd's algorithm | Objective, convergence to a local optimum, empty clusters | Implement; show two seeds giving different solutions |
| 9.2 k-means++ | D² seeding and its O(log k) guarantee (Arthur and Vassilvitskii, 2007) | Compare inertia over 50 seeds: random vs k-means++ |
| 9.3 Choosing k | Elbow, silhouette, stability; mini-batch k-means | Pick k on a customer-segmentation dataset and defend it |
| 9.4 EM for GMMs | E-step responsibilities, M-step updates, log-likelihood monotonicity (Dempster et al., 1977) | Implement full-covariance GMM; check monotone likelihood |
| 9.5 Failure modes | Collapsing components, covariance regularisation, BIC | Trigger a singular covariance; fix with `reg_covar` |

**Check your understanding:** Why does k-means fail on concentric rings? Why is k-means a special case of EM? Why must EM's log-likelihood never decrease, and what does it mean if yours does?

### Chapter 10 · PCA and representation (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 PCA by SVD | Centring, components, explained variance, sign ambiguity | Match `PCA` components up to sign |
| 10.2 Randomised SVD | Halko–Martinsson–Tropp, when it is worth it | Time full vs randomised SVD on a 50,000 × 2,000 matrix |
| 10.3 PCA in pipelines | Whitening, PCA before k-NN, information lost | Accuracy of k-NN vs number of components |
| 10.4 Non-linear views | Kernel PCA; t-SNE and UMAP as visualisations, not analysis (Wattenberg et al., Distill 2016) | Show a t-SNE "cluster" created by perplexity alone |

**Check your understanding:** Why must data be centred before PCA? When does PCA discard exactly the signal you need? Why should cluster sizes in a t-SNE plot not be interpreted?

### Chapter 11 · A neural network from scratch (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Forward and backward | Two-layer MLP, ReLU, softmax cross-entropy, backpropagation by hand | Gradient-check every parameter tensor |
| 11.2 Initialisation | Xavier and He initialisation; dead ReLUs | Show training stalls with all-zero and too-large initialisation |
| 11.3 Optimisers | Mini-batch SGD, momentum, Adam | Match `MLPClassifier` accuracy on Fashion-MNIST within 1 point |
| 11.4 Regularisation | Weight decay, early stopping, dropout | Plot train/validation curves with and without each |

**Check your understanding:** Why does symmetric initialisation make every hidden unit learn the same thing? Why do networks still lose to boosted trees on many tabular tasks? What does your MLP need that logistic regression does not?

### Chapter 12 · Engineering and benchmarking your library (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Library design | Base classes, parameter validation, `check_estimator`, pipelines | Make 8 of your estimators pass `check_estimator` |
| 12.2 Performance | Profiling with `cProfile` and `line_profiler`, memory, optional Numba | Bring your slowest estimator within 10× of scikit-learn |
| 12.3 Fair benchmarks | OpenML-CC18 tasks, repeated cross-validation, Nadeau–Bengio corrected t-test | Benchmark 4 classifiers on 15 datasets |
| 12.4 Choosing an algorithm | No-free-lunch, data size, interpretability, latency, update cost | Write a one-page decision guide with evidence from your benchmark |

**Check your understanding:** Why does an ordinary paired t-test over CV folds overstate significance? Which of your algorithms can be updated online, and which must retrain from scratch? Why is "best average rank" not the same as "best for my problem"?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Test harness | — |
| 2 | 2 | Lab 2 · Linear models | — |
| 3 | 3 | Lab 3 · Logistic regression and library conventions | **P1 due** |
| 4 | 4 | Lab 4 · k-NN and Naive Bayes | — |
| 5 | 5 | Lab 5 · SVMs | — |
| 6 | 6 | Lab 6 · CART | — |
| 7 | 7 | Lab 7 · Random forests and importance | Mid-term (AI off) |
| 8 | 8 | Lab 8 · Histogram GBDT (part 1) | — |
| 9 | 8 | Lab 8 · Histogram GBDT (part 2) | **P2 due** |
| 10 | 9 | Lab 9 · k-means++ and GMMs | — |
| 11 | 10 | Lab 10 · PCA and MLP (part 1) | — |
| 12 | 11 | Lab 10 · PCA and MLP (part 2) | — |
| 13 | 12 | Library hardening (P3) | — |
| 14 | 12 | Benchmark study (P3) | **P3 due** |
| 15 | Review | P3 presentation | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** a first draft of boilerplate (estimator classes, plotting, data loading); explaining a library's source code (for example scikit-learn's `_tree.pyx` or LightGBM's histogram code); generating adversarial test cases; reviewing your derivations. GitHub Copilot, Claude Code, Cursor, ChatGPT and Gemini all handle this.
- **Do without AI (drills):** derive the logistic gradient, the ridge closed form, the GMM M-step and the XGBoost gain; write k-means++, CART split search and backpropagation from a blank file. The mid-term and final are AI-off, and the mastery gate is timed.
- **Verify AI output by:** comparison with a reference library on several seeded datasets; finite-difference gradient checks; property tests (permutation invariance, scaling equivariance, monotone EM likelihood); a known-answer toy case (two points, one feature); reading the code for hidden imports of the library you are meant to replace.
- **Where AI still fails here:** generated "from scratch" code quietly calling `sklearn`; softmax without log-sum-exp; PCA without centring; tree thresholds at sample values instead of midpoints; regularisation conventions mixed up (λ vs `C`, a penalised intercept); scalers fitted on the full dataset. Every lab includes an **AI bug log**: each bug you found in assistant code, the test that caught it, and the fix. The log is graded.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10, including AI bug logs) | 25% |
| Projects P1–P3 | 40% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 25% |

**Mastery gate.** You pass when you can, without AI and within 90 minutes: (1) implement k-means++ and L2-regularised logistic regression in NumPy and match scikit-learn on a provided dataset (centroids by inertia within 1%, coefficients within 10⁻⁴); (2) derive the XGBoost leaf weight and split gain on paper and compute them for a 6-row example; (3) given a library model that disagrees with a textbook answer (a default penalty, an intercept convention, a random seed), find and explain the cause.

## Industry reality

Gradient-boosted trees and linear models are the workhorses of tabular ML. Facebook's ads team reported that feeding boosted-tree leaf indices into logistic regression beat either model alone (He et al., 2014). XGBoost (Chen and Guestrin, 2016) and LightGBM (Ke et al., 2017) are standard in industry and in data-science competitions, and scikit-learn (Pedregosa et al., 2011) is the reference API that most tooling copies. Chip Huyen's free *Machine Learning Interviews* book gives a full chapter of its 200+ interview questions to ML algorithms, including classical methods, which is the material of this course.

**Interview questions from this course**

1. *Derive the split gain XGBoost uses.* Strong answer: second-order Taylor expansion of the loss; optimal leaf weight −G/(H + λ); gain = ½[G_L²/(H_L + λ) + G_R²/(H_R + λ) − (G_L + G_R)²/(H_L + H_R + λ)] − γ; explains what λ and γ do.
2. *Why does a random forest generalise better than one deep tree?* Strong answer: averaging reduces variance; the variance formula with correlation ρ; feature subsampling lowers ρ; bias stays about the same; OOB error as a check.
3. *Implement k-means. Does it always converge? To what?* Strong answer: correct vectorised code; converges because each step cannot increase inertia and there are finitely many partitions; only to a local optimum; k-means++ seeding; empty-cluster handling.
4. *Your logistic regression coefficients differ from a colleague's. Why?* Strong answer: regularisation default and strength, intercept penalisation, feature scaling, solver tolerance, class weights, separable data; how to reproduce each.
5. *When would you choose Naive Bayes, k-NN, an SVM or boosted trees?* Strong answer: data size and dimension, training and inference cost, need for probabilities (and calibration), interpretability, online updates; backed by complexity numbers, not slogans.

## Resources (free first)

- **Primary notes:** Stanford CS229 lecture notes — https://cs229.stanford.edu/main_notes.pdf ; course site — https://cs229.stanford.edu/
- **Textbooks:** Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning* (free PDF) — https://hastie.su.domains/ElemStatLearn/ ; James et al., *An Introduction to Statistical Learning* (Python edition, free) — https://www.statlearning.com/ ; Murphy, *Probabilistic Machine Learning: An Introduction* — https://probml.github.io/pml-book/book1.html ; Bishop, *Pattern Recognition and Machine Learning* — https://www.microsoft.com/en-us/research/people/cmbishop/prml-book/
- **Video course:** NPTEL Introduction to Machine Learning (IIT Madras) — https://nptel.ac.in/courses/106106139
- **Library documentation:** scikit-learn user guide — https://scikit-learn.org/stable/user_guide.html ; developing estimators — https://scikit-learn.org/stable/developers/develop.html ; XGBoost "Introduction to Boosted Trees" — https://xgboost.readthedocs.io/en/stable/tutorials/model.html ; LightGBM features — https://lightgbm.readthedocs.io/en/stable/Features.html ; CatBoost algorithm — https://catboost.ai/docs/en/concepts/algorithm-main-stages
- **Papers:** Friedman (2001) — https://doi.org/10.1214/aos/1013203451 ; Breiman (2001) — https://link.springer.com/article/10.1023/A:1010933404324 ; Chen and Guestrin (2016) — https://arxiv.org/abs/1603.02754 ; Ke et al. (2017) — https://proceedings.neurips.cc/paper_files/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html ; Prokhorenkova et al. (CatBoost) — https://arxiv.org/abs/1706.09516 ; Arthur and Vassilvitskii (2007) — https://theory.stanford.edu/~sergei/papers/kMeansPP-soda.pdf ; Platt (1998), SMO — https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-14.pdf ; Pegasos — https://www.cs.huji.ac.il/~shais/papers/ShalevSiSrCo10.pdf ; Strobl et al. (2007) — https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-8-25
- **Benchmarking:** OpenML-CC18 (Bischl et al.) — https://arxiv.org/abs/1708.03731 ; Nadeau and Bengio (2003) — https://link.springer.com/article/10.1023/A:1024068626366
- **Testing:** Hypothesis — https://hypothesis.readthedocs.io/
- **Visualisation caveats:** "How to Use t-SNE Effectively" (Distill) — https://distill.pub/2016/misread-tsne/

## Sources

- Grinsztajn, Oyallon and Varoquaux, "Why do tree-based models still outperform deep learning on tabular data?" (NeurIPS 2022 Datasets and Benchmarks; arXiv 2207.08815) — https://arxiv.org/abs/2207.08815 (checked 2026-10)
- scikit-learn 1.9.1 `LogisticRegression` documentation: "regularization is applied by default", `C=1.0`, `penalty` deprecated in 1.8 in favour of `l1_ratio` — https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html (checked 2026-10)
- `statsmodels` Logit (unpenalised maximum likelihood) — https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.Logit.html (checked 2026-10)
- He et al., "Practical Lessons from Predicting Clicks on Ads at Facebook" (ADKDD 2014) — https://quinonero.net/Publications/predicting-clicks-facebook.pdf (checked 2026-10)
- Pedregosa et al., "Scikit-learn: Machine Learning in Python", JMLR 12 (2011) — https://www.jmlr.org/papers/v12/pedregosa11a.html (checked 2026-10)
- Chip Huyen, *Machine Learning Interviews* (2021) — https://huyenchip.com/ml-interviews-book/ (checked 2026-10)
- Library versions on PyPI: scikit-learn 1.9.1 (Sep 2026), XGBoost 3.4.1 (Aug 2026), LightGBM 4.7.0 (Jul 2026), CatBoost 1.2.10 (Feb 2026), NumPy 2.5.4 (Oct 2026) — https://pypi.org/ (checked 2026-10)
- Papers listed under Resources (checked 2026-10)

_Last reviewed: 2026-10_
