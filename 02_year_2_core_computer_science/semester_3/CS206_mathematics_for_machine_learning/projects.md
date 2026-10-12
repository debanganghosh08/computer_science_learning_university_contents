# CS206 · Labs and projects

Work in Python with NumPy, SciPy and matplotlib in Jupyter or plain scripts; PyTorch or JAX is used only as a reference to check your own implementations. Every derivation you submit comes with a numerical check.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Shapes and linear maps | Visualise 2×2 maps on a grid; rewrite 10 loop-based computations with broadcasting and `einsum`; find rank deficiency in a feature matrix | Notebook with plots, shape assertions and timing comparisons | 3 h |
| 2 · Least squares and conditioning | Fit a public regression dataset by normal equations, QR and `lstsq`; solve Hilbert systems of growing size | Error vs condition-number plot; a paragraph on when each solver is safe | 4 h |
| 3 · PageRank by power iteration | Build the transition matrix of a public web graph from the Stanford SNAP collection; run power iteration with damping | Top-20 pages, convergence plot, and the effect of the damping factor on convergence speed | 4 h |
| 4 · SVD compression and PCA | Compress images by truncated SVD; run PCA on Fashion-MNIST with and without standardisation | Error-vs-rank curves, 2-D PCA map, explained-variance table | 5 h |
| 5 · Gradient checker | Build a central-difference checker; derive gradients for 8 losses by hand; ask an AI assistant for the same derivations and check them all | Checker code, your derivations, and a log of every AI derivation that failed and why | 4 h |
| 6 · Micro autograd | Scalar reverse-mode engine; train a tiny MLP on a 2-D classification task | Engine, tests against PyTorch, decision-boundary plot | 6 h |
| 7 · Gaussians and Monte Carlo | Sample correlated Gaussians via Cholesky; verify conditioning formulas; estimate a rare-event probability with importance sampling | Plots, analytical vs simulated values, variance comparison | 4 h |
| 8 · MLE, MAP and Bayesian A/B | MLE for three distributions; ridge and lasso as MAP; a Beta–Bernoulli A/B test | Derivations, code, coefficient paths, posterior plots with a decision rule | 5 h |
| 9 · Entropy and perplexity | Character entropy of English and Hindi text; unigram and bigram character models with smoothing; perplexity on held-out text | Entropy table, `gzip` comparison, perplexity results and interpretation | 4 h |
| 10 · CVXPY and ISTA | A portfolio QP in CVXPY; lasso by ISTA compared with CVXPY's solution | Code, KKT check of the CVXPY solution, convergence plot for ISTA | 4 h |

## Projects

### P1 · PCA explorer on faces (L1, ~6 hours)

**Real-world inspiration.** "Eigenfaces" (Turk and Pentland, 1991) used PCA for face recognition; today PCA is the first tool for visualising embeddings and compressing features. This project uses the small Olivetti faces research dataset bundled with scikit-learn.

**What to build.** PCA from scratch through the SVD of centred data: components, explained variance, reconstructions from k components, and nearest-neighbour recognition in PCA space.

**Acceptance criteria**
- Your top 20 components match scikit-learn's up to sign (absolute cosine similarity above 0.999 for each).
- Explained-variance ratios match scikit-learn's within 10⁻⁶.
- Reconstruction-error-vs-k plot, and recognition accuracy on a held-out split compared with nearest-neighbour on raw pixels.
- A one-page explanation of why component signs are arbitrary and why centring matters, with a demonstration of what goes wrong without centring.

**Stretch goals.** Randomised SVD and its speed-accuracy trade-off; PCA on a modern sentence-embedding matrix with a plot of the first two components.

**What it proves to an employer.** You understand what the most common dimensionality-reduction tool actually computes and can check your work against a reference.

### P2 · An autograd engine and a network trained from scratch (L2, ~15 hours)

**Real-world inspiration.** PyTorch autograd and JAX compute gradients for every modern model by reverse-mode automatic differentiation; micrograd showed the core fits in a few hundred lines.

**What to build.** A tensor-level reverse-mode autodiff library in NumPy supporting add, multiply, matmul, broadcasting, sum and mean, exp and log, `tanh` and ReLU, and a fused, numerically stable softmax cross-entropy. Add SGD, momentum, Adam and AdamW optimisers, then train an MLP on Fashion-MNIST.

**Acceptance criteria**
- Gradients match PyTorch within 10⁻⁶ relative error on 200 randomly generated computation graphs, including broadcasting cases.
- Your Adam and AdamW match `torch.optim` parameter values step for step within 10⁻⁶ for 100 steps on the same problem.
- A 2-layer MLP reaches at least 85% test accuracy on Fashion-MNIST using only your library.
- No Python loops over batch elements; the README reports time per epoch and peak memory.
- A short write-up derives the softmax cross-entropy gradient and explains why the fused version is stable.

**Stretch goals.** Forward-mode JVPs; gradient checkpointing with a measured memory saving; a learning-rate warm-up and cosine schedule study.

**What it proves to an employer.** You know what happens inside `loss.backward()` and `optimizer.step()`, which is what lets you debug training rather than restart it.

### P3 · A recommender system from first principles (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** The Netflix Prize (2006–2009) made matrix factorisation the standard approach to rating prediction (Koren, Bell and Volinsky, 2009); streaming and e-commerce platforms still use low-rank embeddings for recommendations. This project uses the public MovieLens dataset from GroupLens.

**What to build.** A reproducible pipeline on MovieLens (1M, or 25M for the stretch): bias-only baselines; truncated SVD on an imputed matrix; regularised matrix factorisation trained two ways, by SGD and by alternating least squares (each ALS step is a ridge regression you derive in Chapter 2); a MAP interpretation of the objective; a rank study; and evaluation by test RMSE and recall@10.

**Acceptance criteria**
- One command reproduces every number from the raw download, with fixed seeds and a documented split.
- Regularised matrix factorisation beats the bias-only baseline on test RMSE; results reported as mean ± standard deviation over 3 seeds.
- SGD and ALS reach objective values within 1% of each other; convergence is plotted against both iterations and wall-clock time.
- The report derives the ALS update and the SGD gradient, and both are verified numerically.
- A rank study over k ∈ {2, 5, 10, 20, 50, 100} with train and test curves, explained through bias and variance.
- The report states the probabilistic model (Gaussian noise, Gaussian priors on factors) behind the regularised objective and interprets λ in those terms.
- A limitations section covering cold start, popularity bias and fairness to niche items.

**Stretch goals.** Implicit-feedback ALS with confidence weights; randomised SVD to speed up initialisation; a "more like this" demo using item-embedding cosine similarity.

**What it proves to an employer.** You can take a real ML problem from linear algebra, probability and optimisation through to a measured, reproducible result, and explain every design choice. ML engineering, data science and research-engineering teams look for exactly this.

## Feeds into

- [CS214 Machine Learning Foundations](../../semester_4/CS214_machine_learning_foundations/README.md): every model there uses Chapters 2, 4, 8 and 11.
- The Deep Learning major: [DLR301 Neural Networks from Scratch](../../../03_majors/deep_learning/year_3/DLR301_neural_networks_from_scratch_autograd/README.md) builds on P2; [DLR304 Training Deep Networks](../../../03_majors/deep_learning/year_3/DLR304_training_deep_networks_optimization/README.md) extends Chapter 11; [DLR303 Sequence Models and Transformers](../../../03_majors/deep_learning/year_3/DLR303_sequence_models_and_transformers/README.md) and [DLR305 Generative Models](../../../03_majors/deep_learning/year_3/DLR305_generative_models_vaes_gans_and_diffusion/README.md) rely on Chapters 7–9.
- [DSC301 Statistical Inference and Modeling](../../../03_majors/data_science/year_3/DSC301_statistical_inference_and_modeling/README.md): Chapter 8 in depth.
- [OV11 AI for Science and Research Engineering](../../../04_overlaps/OV11_ai_for_science_research_engineering/README.md): optimisation and linear algebra at research depth.
