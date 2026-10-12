# CS206 · Mathematics for Machine Learning

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 2 · 3 | 4 (≈ 120 hours) | L1 → L3 | [FND113](../../../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md), [FND116](../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | [CS214](../../semester_4/CS214_machine_learning_foundations/README.md), [DLR301](../../../03_majors/deep_learning/year_3/DLR301_neural_networks_from_scratch_autograd/README.md), [DLR303](../../../03_majors/deep_learning/year_3/DLR303_sequence_models_and_transformers/README.md), [DLR304](../../../03_majors/deep_learning/year_3/DLR304_training_deep_networks_optimization/README.md) |

## Why this course matters now

Every model in production, from a fraud score to a large language model, is a function of matrices trained by following gradients of a likelihood-based loss. The mathematics shows up directly in today's tools: LoRA fine-tuning adapts a model by learning a low-rank update to its weight matrices (Hu et al., 2021); language models are compared by perplexity, the exponential of cross-entropy; and optimisers keep evolving: AdamW remains a standard choice, while Moonshot AI trained Kimi K2, a 1-trillion-parameter mixture-of-experts model, on 15.5 trillion tokens with MuonClip, a variant of the Muon optimiser that orthogonalises matrix updates (2025). AI systems are now strong at mathematics: an advanced Gemini Deep Think scored 35 of 42 at the 2025 International Mathematical Olympiad, gold-medal standard. Derivations are therefore cheap to obtain. What stays valuable is choosing the right formulation, spotting the silent assumption (independence, convexity, Gaussian noise), and checking every result numerically before a training run burns a week of GPU time.

## Learning outcomes

By the end you can:

1. **Explain** data, models and embeddings geometrically (span, rank, projections, norms), and **write** shape-correct, vectorised NumPy.
2. **Solve** least-squares problems by normal equations, QR and the pseudoinverse, and **diagnose** ill-conditioning.
3. **Compute** and **interpret** eigendecompositions and the SVD, and **apply** them to PCA, low-rank compression and PageRank.
4. **Derive** gradients and Jacobians of matrix expressions and ML losses, and **verify** them with finite differences.
5. **Implement** reverse-mode automatic differentiation and **explain** why backpropagation is cheap.
6. **Manipulate** multivariate Gaussians (marginals, conditionals, sampling) and **use** Monte Carlo estimates with error bars.
7. **Derive** MLE and MAP estimators for standard models, and **show** that L2 and L1 regularisation are Gaussian and Laplace priors.
8. **Explain** entropy, cross-entropy, KL divergence, mutual information and perplexity, and **compute** them on real data.
9. **Recognise** convex problems, **apply** KKT conditions, and **model** problems in CVXPY.
10. **Implement** and **compare** gradient descent, momentum, SGD, Adam and AdamW, and **explain** their behaviour through conditioning and noise.

## Chapters and lessons

### Chapter 1 · Vectors, matrices and the geometry of data (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Spaces and rank | Span, basis, linear independence, rank; data as vectors (pixels, features, embeddings) | Find the rank of a feature matrix with hidden duplicate columns; explain multicollinearity |
| 1.2 Matrices as maps | Composition, inverse, determinant as volume scaling, the four fundamental subspaces | Animate 2×2 transformations on a grid in NumPy and matplotlib |
| 1.3 Shapes and vectorisation | Broadcasting, batch dimensions, `einsum`, row vs column conventions | Rewrite 10 Python loops as `einsum`; add shape assertions |
| 1.4 Norms and similarity | L1, L2, L∞, Frobenius norms; dot product and cosine similarity; nearest-neighbour search | Cosine nearest neighbours over a provided sentence-embedding matrix |

**Check your understanding:** Why does a feature matrix with rank less than its column count break ordinary least squares? Why is cosine similarity preferred over Euclidean distance for many embeddings? What does a zero determinant say about the information a transformation destroys?

### Chapter 2 · Orthogonality, projections and least squares (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Orthogonality | Inner products, orthonormal bases, Gram–Schmidt, QR decomposition | Classical vs modified Gram–Schmidt; measure loss of orthogonality |
| 2.2 Projections | Projection onto a subspace, projection matrices, residuals | Project 3-D data onto a plane; plot residuals |
| 2.3 Least squares | Normal equations, QR solution, pseudoinverse; linear regression as projection | Fit one dataset three ways; compare answers and run times |
| 2.4 Conditioning | Condition number, floating-point error, ridge regularisation as a fix | Solve Hilbert-matrix systems; plot error against condition number |

**Check your understanding:** Why is solving the normal equations less stable than QR? What does the residual of a least-squares fit have to be orthogonal to, and why? How does adding λI improve conditioning, and what does it cost?

### Chapter 3 · Eigenvalues and positive definite matrices (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Eigen-decomposition | Eigenvalues and eigenvectors, diagonalisation, defective matrices | 2×2 and 3×3 by hand; check with `numpy.linalg.eig` |
| 3.2 Symmetric and PSD matrices | Spectral theorem, quadratic forms, positive (semi)definite matrices, covariance, Cholesky | Prove a sample covariance is PSD; test definiteness with Cholesky |
| 3.3 Power iteration and PageRank | Markov chains, stationary distributions, damping factor | PageRank on a public link graph (e.g., a SNAP dataset) |
| 3.4 Linear dynamics | Aᵏ through eigenvalues; stability of linear recurrences | Predict from eigenvalues whether an iterated map explodes or decays; confirm |

**Check your understanding:** Why are the eigenvectors of a symmetric matrix orthogonal, and why does that matter for PCA? What does the second-largest eigenvalue tell you about how fast power iteration converges? Why must a valid covariance matrix be PSD?

### Chapter 4 · SVD, PCA and low-rank structure (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The SVD | Rotate–scale–rotate geometry; link to the eigen-decomposition of AᵀA; singular values and rank | SVD of a 2×2 by hand; verify numerically |
| 4.2 Best low-rank approximation | Eckart–Young theorem; truncated SVD; reconstruction error | Compress an image at ranks 5–100; plot error vs storage |
| 4.3 PCA | Centring, principal components via SVD, explained variance, whitening; pitfalls (scaling, outliers, non-linear structure) | PCA on Fashion-MNIST; 2-D map; reconstruction from k components |
| 4.4 Low rank in modern ML | Matrix-factorisation recommenders (Netflix Prize era); LoRA's update ΔW = BA; randomised SVD (Halko, Martinsson and Tropp) | Count LoRA parameters for a 4096×4096 layer at ranks 8 and 16; implement randomised SVD and compare with full SVD |

**Check your understanding:** Why does PCA on unscaled features mostly find the feature with the largest units? What does Eckart–Young guarantee that a random projection does not? Why can a rank-8 update adapt a large model at all?

### Chapter 5 · Matrix calculus (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Derivatives as linear maps | Gradient, Jacobian, Hessian; the differential view df = f′(x)[dx]; layout conventions | Derive gradients of 5 scalar functions of vectors |
| 5.2 Matrix identities | Gradients of xᵀAx, ‖Ax − b‖², tr(AXB), log det X; chain rule for compositions | Derive each, then check numerically |
| 5.3 Loss functions | Stable log-sum-exp, softmax, cross-entropy (gradient = softmax − one-hot), logistic loss | Show overflow in naive softmax; fix it with log-sum-exp |
| 5.4 Gradient checking | Central differences, relative error, step-size choice, `torch.autograd.gradcheck` | Build a checker; catch 3 planted gradient bugs |

**Check your understanding:** Why is the gradient of ‖Ax − b‖² equal to 2Aᵀ(Ax − b) and not 2(Ax − b)ᵀA, and when does the difference matter in code? Why does a central difference beat a forward difference? Why do frameworks compute softmax and cross-entropy together?

### Chapter 6 · Automatic differentiation (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Computational graphs | Forward vs reverse mode; their costs for n inputs and m outputs | Reverse pass by hand on a 6-node graph |
| 6.2 VJPs and JVPs | Vector–Jacobian and Jacobian–vector products; backpropagation as reverse mode | VJP rules for add, multiply, matmul, `tanh`, sum |
| 6.3 A micro autograd engine | Topological ordering, gradient accumulation, broadcasting rules | Train a 2-layer MLP with your own engine |
| 6.4 AD in frameworks | PyTorch autograd; JAX `grad`, `vmap`, `jit`; activation memory and checkpointing | Match your gradients to PyTorch within 10⁻⁶ |

**Check your understanding:** Why does reverse mode win for a loss with millions of parameters and one output? Where does the memory cost of backpropagation come from? Why must gradients be accumulated, not overwritten, when a value is used twice?

### Chapter 7 · Probability II (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Random vectors | Joint, marginal and conditional distributions; independence; Bayes' rule | Base-rate problem: compute, then confirm by simulation |
| 7.2 Linear transformations | E[Ax + b] and Cov(Ax) = AΣAᵀ | Verify both by simulation for a 3-D example |
| 7.3 Multivariate Gaussians | Density, Mahalanobis distance, conditioning and marginalising, sampling with Cholesky | Sample correlated Gaussians; condition on one coordinate and check against simulation |
| 7.4 Limits and Monte Carlo | Law of large numbers, central limit theorem, Hoeffding's bound (intuition); Monte Carlo estimates and importance sampling | CLT for a skewed distribution; estimate a tail probability with and without importance sampling |

**Check your understanding:** Why is the conditional of a Gaussian still Gaussian, and why does its variance not depend on the observed value? Why does averaging a minibatch of gradients give a useful estimate of the full gradient? When does importance sampling make an estimate worse?

### Chapter 8 · Estimation: MLE, MAP and Bayesian basics (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Maximum likelihood | Likelihood vs probability; MLE for Bernoulli, Gaussian, Poisson | Derive and code each; confirm with `scipy.optimize` |
| 8.2 MLE for models | Gaussian noise ⇒ least squares; Bernoulli labels ⇒ logistic loss (cross-entropy) | Logistic regression by gradient descent from scratch vs scikit-learn |
| 8.3 MAP and regularisation | Gaussian prior ⇒ L2 (ridge); Laplace prior ⇒ L1 (lasso); sparsity | Show the equivalence numerically; plot coefficient paths |
| 8.4 Bayesian updating | Conjugate priors (Beta–Bernoulli), posterior predictive, credible intervals | Bayesian A/B test on two click-through datasets |
| 8.5 Estimator quality | Bias, variance, consistency, the bias–variance decomposition | Decompose the error of polynomial fits by simulation |

**Check your understanding:** Why does the MLE of a Gaussian's variance divide by n rather than n − 1, and is that a problem? Why does an L1 penalty produce exact zeros while L2 does not? When would you prefer a posterior distribution over a point estimate?

### Chapter 9 · Information theory (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Entropy | Surprise, entropy, its link to optimal codes (see Huffman coding in [CS201](../CS201_algorithms_and_complexity/README.md)) | Character entropy of English and Hindi text; compare with `gzip` ratios |
| 9.2 Cross-entropy and KL | Definitions, Gibbs' inequality via Jensen, asymmetry; forward vs reverse KL | Fit one Gaussian to a bimodal distribution by forward and by reverse KL |
| 9.3 Mutual information | Definition, data-processing inequality, use in feature selection | Mutual information between features and labels in a public dataset |
| 9.4 Perplexity | Cross-entropy loss as average code length; bits per token; perplexity for language models | Perplexity of unigram vs bigram character models on held-out text |

**Check your understanding:** Why does minimising cross-entropy to data equal maximising likelihood? Why does reverse KL pick one mode while forward KL spreads across both? What does a perplexity of 20 mean in words?

### Chapter 10 · Convex optimisation (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Convex sets and functions | Definitions, first- and second-order tests, operations that preserve convexity, strong convexity | Prove or disprove convexity for 6 losses |
| 10.2 Optimality and duality | Lagrangian, KKT conditions, weak and strong duality; the SVM dual | Solve a small constrained problem by KKT on paper |
| 10.3 Modelling | Linear and quadratic programmes; disciplined convex programming in CVXPY | Mean–variance portfolio with a budget constraint in CVXPY |
| 10.4 Non-smooth problems | Subgradients, proximal operators, soft-thresholding, ISTA | Lasso by ISTA; compare with CVXPY's answer |

**Check your understanding:** Why is every local minimum of a convex function global? What does a non-zero Lagrange multiplier tell you about its constraint? Why is training a neural network not a convex problem even when its loss function is convex in the outputs?

### Chapter 11 · Gradient descent and its variants (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Gradient descent | L-smoothness, step size 1/L, rates for convex and strongly convex functions, the condition number | GD on quadratics with κ = 10, 100, 1000; plot convergence |
| 11.2 Momentum | Heavy-ball and Nesterov acceleration | Iterations to tolerance with and without momentum |
| 11.3 Stochastic gradient descent | Minibatch noise, batch size, learning-rate schedules (step, cosine, warm-up) | SGD on logistic regression across batch sizes and schedules |
| 11.4 Adaptive methods | AdaGrad, RMSProp, Adam (with bias correction), AdamW's decoupled weight decay | Implement Adam and AdamW; compare on a small MLP |
| 11.5 Beyond first order | Newton's method, L-BFGS; Muon's orthogonalised updates for matrix parameters (Newton–Schulz iteration) | Newton vs GD on logistic regression; implement the Newton–Schulz step on random matrices and check orthogonality |

**Check your understanding:** Why does a large condition number make gradient descent zig-zag, and how does momentum help? Why does Adam need bias correction in early steps? Why is L2 regularisation inside Adam not the same as AdamW's weight decay?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Shapes and linear maps | — |
| 2 | 2 | Lab 2 · Least squares and conditioning | — |
| 3 | 3 | Lab 3 · PageRank by power iteration | — |
| 4 | 4 | Lab 4 · SVD compression and PCA | — |
| 5 | 4 | — | **P1 due** |
| 6 | 5 | Lab 5 · Gradient checker (incl. AI derivations) | — |
| 7 | 6 | Lab 6 · Micro autograd | Mid-term (AI off) |
| 8 | 7 | Lab 7 · Gaussians and Monte Carlo | — |
| 9 | 8 | Lab 8 · MLE, MAP and Bayesian A/B | — |
| 10 | 8–9 | — | **P2 due** |
| 11 | 9 | Lab 9 · Entropy and perplexity | — |
| 12 | 10 | Lab 10 · CVXPY and ISTA | — |
| 13 | 11 | Optimiser zoo (part of P3) | — |
| 14 | 11 | — | **P3 due** |
| 15 | Review | P3 presentation | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** step-by-step derivations you then check; alternative intuitions for a concept; translating formulas into NumPy, PyTorch or JAX; generating practice problems with worked answers; summarising a paper's method section. Claude, ChatGPT and Gemini all handle this level of mathematics; SymPy and Wolfram Alpha are useful symbolic cross-checks.
- **Do without AI (drills):** derive gradients, MLEs and KKT conditions by hand; compute 2×2 eigendecompositions and SVDs; prove convexity; reason about shapes before running code. The mid-term and final exam are AI-off.
- **Verify AI output by:** finite-difference gradient checks; shape assertions in code; Monte Carlo simulation for any probability claim; comparison with `numpy.linalg`, SciPy or framework autograd; limiting cases (n = 1, σ → 0, λ → ∞) that must give a known answer.
- **Where AI still fails here:** competition-level results show these models are strong, so the errors you meet are subtle: a transposed Jacobian, a dropped 1/n, a missing constraint, an independence or convexity assumption made silently. In Lab 5 you gradient-check every derivation an assistant gives you and keep a log of which ones fail and why; that log is part of your grade.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 30% |

**Mastery gate.** You pass when you can, without AI: (1) derive the gradient of a new composite loss (for example softmax cross-entropy with L2 regularisation over a linear layer), implement it, and pass a finite-difference check on the first try or find your own error within 15 minutes; (2) explain PCA through the SVD on a whiteboard, including when it misleads; (3) derive an MLE and its MAP counterpart for a model you have not seen; (4) predict from the condition number how gradient descent and momentum will behave on a quadratic, then confirm it.

## Industry reality

Where this is used (public sources): LoRA's low-rank updates for fine-tuning large models (Hu et al., 2021); Adam (Kingma and Ba, 2014) and AdamW (Loshchilov and Hutter, 2017) as standard training optimisers; Muon's orthogonalised updates (Jordan, 2024) scaled to Kimi K2 as MuonClip (Moonshot AI, 2025); matrix factorisation for recommendations, popularised by the Netflix Prize (Koren, Bell and Volinsky, 2009); PageRank as the stationary distribution of a random walk (Brin and Page, 1998). ML engineers, data scientists, research engineers and quantitative analysts are tested on this material.

**Interview questions from this course**

1. *Derive the gradient of the logistic-regression loss.* Strong answer: σ′(z) = σ(z)(1 − σ(z)); gradient Xᵀ(σ(Xw) − y)/n; notes convexity, adds the L2 term, and mentions numerical stability.
2. *Explain PCA. When would it mislead you?* Strong answer: SVD of centred (and usually standardised) data; components maximise variance; explained-variance ratio; misleads when variance is not relevance, with unscaled features, outliers or non-linear structure.
3. *Why does Adam use bias correction, and why use AdamW instead of L2 regularisation in Adam?* Strong answer: moment estimates start at zero and are biased early; with adaptive scaling, an L2 term is rescaled per parameter, while AdamW decouples weight decay from the gradient step.
4. *How are MLE, cross-entropy and KL divergence related?* Strong answer: maximising average log-likelihood equals minimising cross-entropy between the empirical distribution and the model, which equals minimising KL(data ‖ model) up to the data's entropy, a constant.
5. *Training loss becomes NaN after 200 steps. What do you check?* Strong answer: learning rate and warm-up; overflow in exp or log (use log-sum-exp); division by zero; exploding gradients (norms, clipping); mixed-precision overflow; bad data; reproduce on a small batch and gradient-check.

## Resources (free first)

- **Primary text:** Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (free PDF) — https://mml-book.github.io/
- **Linear algebra:** MIT 18.06 Linear Algebra (Strang, OCW) — https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ ; MIT 18.065 Matrix Methods in Data Analysis, Signal Processing and Machine Learning — https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/ ; 3Blue1Brown, Essence of Linear Algebra — https://www.3blue1brown.com/topics/linear-algebra ; NPTEL Essential Mathematics for Machine Learning (IIT Roorkee) — https://nptel.ac.in/courses/111107137
- **Matrix calculus:** MIT 18.S096 Matrix Calculus for Machine Learning and Beyond (OCW) — https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/ ; Bright, Edelman and Johnson, lecture notes (arXiv 2501.14787) — https://arxiv.org/abs/2501.14787 ; *The Matrix Cookbook* — https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf
- **Optimisation:** Boyd and Vandenberghe, *Convex Optimization* (free PDF) — https://web.stanford.edu/~boyd/cvxbook/ ; Stanford EE364a — https://web.stanford.edu/class/ee364a/ ; CVXPY — https://www.cvxpy.org/
- **Probability and information:** David MacKay, *Information Theory, Inference, and Learning Algorithms* (free) — https://www.inference.org.uk/itila/book.html ; Christopher Bishop, *Pattern Recognition and Machine Learning* (free PDF) — https://www.microsoft.com/en-us/research/people/cmbishop/prml-book/
- **Deep-learning maths:** Goodfellow, Bengio and Courville, *Deep Learning*, chapters 2–4 (free online) — https://www.deeplearningbook.org/ ; *Dive into Deep Learning* — https://d2l.ai/
- **Autodiff:** micrograd — https://github.com/karpathy/micrograd ; PyTorch autograd — https://docs.pytorch.org/docs/stable/autograd.html ; JAX autodiff cookbook — https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html ; SymPy — https://www.sympy.org/
- **Paid, optional:** Gilbert Strang, *Linear Algebra and Learning from Data*.

## Sources

- Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models" (arXiv 2106.09685, 2021) — https://arxiv.org/abs/2106.09685 (checked 2026-10)
- Kimi Team (Moonshot AI), "Kimi K2: Open Agentic Intelligence" (arXiv 2507.20534, Jul 2025) — https://arxiv.org/abs/2507.20534 (checked 2026-10)
- Keller Jordan, "Muon: An optimizer for hidden layers in neural networks" (Dec 2024) — https://kellerjordan.github.io/posts/muon/ (checked 2026-10)
- Google DeepMind, "Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the International Mathematical Olympiad" (21 Jul 2025) — https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/ (checked 2026-10)
- Kingma and Ba, "Adam: A Method for Stochastic Optimization" (arXiv 1412.6980) — https://arxiv.org/abs/1412.6980 ; Loshchilov and Hutter, "Decoupled Weight Decay Regularization" (arXiv 1711.05101) — https://arxiv.org/abs/1711.05101 (checked 2026-10)
- Halko, Martinsson and Tropp, "Finding structure with randomness" (arXiv 0909.4061) — https://arxiv.org/abs/0909.4061 (checked 2026-10)
- Koren, Bell and Volinsky, "Matrix Factorization Techniques for Recommender Systems", *IEEE Computer* (2009) — https://ieeexplore.ieee.org/document/5197422 (checked 2026-10)
- Brin and Page, "The Anatomy of a Large-Scale Hypertextual Web Search Engine" (1998) — http://infolab.stanford.edu/~backrub/google.html (checked 2026-10)

_Last reviewed: 2026-10_
