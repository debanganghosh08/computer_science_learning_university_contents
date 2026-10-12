# FND113 · Linear Algebra and Calculus for Computing

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 1 · 2 | 4 (≈ 120 hours) | L0 → L2 | [FND103](../../semester_1/FND103_discrete_mathematics_for_computing/README.md) | [CS206](../../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md), then [CS214](../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) and [CSG304](../../../03_majors/computer_science_general/year_3/CSG304_computer_graphics/README.md) |

## Why this course matters now

Every neural network is trained by gradient descent, with gradients computed by the chain rule (backpropagation, now automated in PyTorch autograd and JAX). Every 3D scene on screen is placed by 4×4 matrices. Google's original search engine ranked pages with PageRank, the principal eigenvector of the web's link matrix, and JPEG images are stored as coefficients of a discrete cosine transform, which is a change of basis. AI models are now strong at mathematics: an advanced Gemini model reached gold-medal standard at the 2025 International Mathematical Olympiad. Yet the GSM-Symbolic study showed that language-model accuracy drops when only the numbers in a problem change, or when an irrelevant sentence is added. You need to own these ideas well enough to set up the problem, read the shapes, and check every answer numerically. This course teaches the mathematics through code, so that each idea ends as something you can run and test.

## Learning outcomes

By the end you can:

1. Compute with vectors and matrices by hand (small cases) and in NumPy (large cases), and explain matrix multiplication as composition of linear maps.
2. Build 2D and 3D transformations, including translation through homogeneous coordinates, and compose them in the right order.
3. Solve linear systems with Gaussian elimination and LU, explain when solutions exist, and measure the effect of conditioning on accuracy.
4. Use rank, bases, orthogonality and projections to fit models by least squares and diagnose redundant features.
5. Interpret eigenvalues, eigenvectors and the SVD geometrically, and apply them to Markov chains, PageRank and low-rank compression.
6. Differentiate single- and multivariable functions, compute gradients, Jacobians and Hessians of common expressions, and check every gradient by finite differences.
7. Explain backpropagation as reverse-mode automatic differentiation, and implement a small autodiff engine that passes gradient checks.
8. Minimise functions with gradient descent and its variants, and predict from the problem's curvature when it will converge, crawl or diverge.
9. Recognise and avoid numerical failure: cancellation, overflow, ill-conditioning and an unstable choice of step size.

## Chapters and lessons

### Chapter 1 · Vectors and NumPy (week 1)

| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Vectors as data | n-tuples and arrows; addition, scaling, linear combinations; a colour, a set of ratings and a word count as vectors | Represent five real objects as vectors and say what each coordinate means |
| 1.2 Dot product and angle | L1 and L2 norms, unit vectors, cosine similarity, projection onto a vector | Rank 10 documents against a query by cosine similarity of word-count vectors |
| 1.3 NumPy arrays | `dtype`, shape, axes, broadcasting rules, vectorisation | Replace four Python loops with vectorised code and time the speed-up |
| 1.4 Floating point for maths | Rounding, catastrophic cancellation, `np.allclose` instead of `==` | Compute a variance two ways and show one losing all its digits |

**Check your understanding:** (1) Why does cosine similarity ignore document length, and when is that a bug? (2) What does broadcasting do with shapes (3, 1) and (4,)? (3) Why must numerical tests use a tolerance?

### Chapter 2 · Matrices and multiplication (week 2)

| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Matrix times vector | A combination of columns, or dot products with rows | Compute three products both ways, by hand and in NumPy |
| 2.2 Matrix times matrix | Composition; associative but not commutative; O(n³) cost of the naive algorithm | Triple-loop multiplication vs NumPy `@` for n = 100 to 1,000; plot both |
| 2.3 Special matrices | Identity, diagonal, symmetric, orthogonal, permutation; adjacency matrices | Show that (A²)ᵢⱼ counts two-step paths in a small graph |
| 2.4 Transpose and shapes | (AB)ᵀ = BᵀAᵀ; shapes as a type system | Predict the shape of 10 expressions before running them |

**Check your understanding:** (1) Why is AB ≠ BA in general, using rotations as the example? (2) What does an entry of A³ mean for a graph? (3) Why is NumPy's `@` so much faster than your triple loop when both do O(n³) work?

### Chapter 3 · Transformations and geometry (week 3)

| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Linear maps in 2D | Scaling, rotation, shear, reflection, projection; the columns show where the basis vectors land | Animate the unit square under six matrices with matplotlib |
| 3.2 Determinants | Area scale factor, orientation, determinant zero means collapse | Predict, then compute, which of five matrices flip orientation |
| 3.3 Homogeneous coordinates | Translation as a 3×3 matrix; composition order | Rotate a shape about a point other than the origin |
| 3.4 3D and the camera | Model, view and projection matrices; the perspective divide | Project a cube's eight corners to 2D and draw its wireframe |

**Check your understanding:** (1) Why can't a 2×2 matrix translate a point? (2) What goes wrong if you translate before you rotate? (3) What does a negative determinant mean for a mesh's triangles?

### Chapter 4 · Linear systems (week 4)

| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Two pictures of Ax = b | Row picture (intersecting lines and planes) vs column picture (combining columns); zero, one or infinitely many solutions | Classify six systems by sketching both pictures |
| 4.2 Elimination and LU | Pivots, back substitution, partial pivoting, LU factorisation | Implement elimination with partial pivoting and match `np.linalg.solve` to 1e-10 |
| 4.3 Solve, don't invert | When an inverse exists; why `solve` beats `inv(A) @ b` in cost and accuracy | Compare time and residual for both on a random 1,000×1,000 system |
| 4.4 Conditioning | Condition number; the Hilbert matrix; losing digits | Solve Hilbert systems for n = 4 to 14 and plot error against condition number |

**Check your understanding:** (1) Why does partial pivoting matter even when no pivot is exactly zero? (2) A system has condition number 10¹². How many correct digits can you expect in float64? (3) When is computing an inverse actually justified?

### Chapter 5 · Vector spaces, orthogonality and least squares (weeks 5–6)

| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Span and basis | Linear independence, basis, dimension, coordinates in a basis | Test whether five feature vectors are independent |
| 5.2 The four subspaces | Column space, null space, rank, the rank–nullity theorem | Find the redundant (collinear) features in a dataset with `matrix_rank` |
| 5.3 Orthogonality | Orthonormal bases, Gram–Schmidt, QR factorisation | Implement Gram–Schmidt, compare it with `np.linalg.qr`, and watch it lose orthogonality |
| 5.4 Projection and least squares | Projection matrices; normal equations; residuals orthogonal to the column space; `lstsq` | Fit a trend line to IMD sub-divisional rainfall (1901–2017) from data.gov.in and plot the residuals |
| 5.5 Overfitting, numerically | Polynomial degree vs train and test error; QR vs normal equations on an ill-conditioned design | Fit degrees 1–10 and plot both errors |

**Check your understanding:** (1) Why is the least-squares residual perpendicular to every column of A? (2) What does a non-trivial null space say about a model's parameters? (3) Why can solving the normal equations lose twice as many digits as QR?

### Chapter 6 · Eigenvalues, eigenvectors and the SVD (weeks 7–8)

| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Eigen-intuition | Directions a matrix only stretches; the 2×2 characteristic polynomial; diagonalisation | Hand-compute three 2×2 cases and check them with `np.linalg.eig` |
| 6.2 Powers and Markov chains | Aᵏ through eigenvalues; a steady state is an eigenvector with eigenvalue 1 | Find a three-state chain's steady state by simulation and by eigenvector |
| 6.3 PageRank and power iteration | The principal eigenvector, damping factor 0.85 (Brin and Page, 1998), convergence set by the eigenvalue gap | Power iteration on a 6-page web, then on a SNAP web graph |
| 6.4 Symmetric matrices | Real eigenvalues, orthogonal eigenvectors (spectral theorem, intuitively); quadratic forms; positive definiteness | Classify four quadratic forms by their eigenvalues and plot their level curves |
| 6.5 The SVD | A = UΣVᵀ; best rank-k approximation; a first look at PCA | Compress a grayscale image at ranks 5, 20 and 50; plot error and storage against k |

**Check your understanding:** (1) Why does repeatedly multiplying by A pull almost any vector toward the dominant eigenvector? (2) What does the damping factor guarantee in PageRank? (3) Why does every matrix have an SVD while not every matrix can be diagonalised?

### Chapter 7 · Derivatives (week 9)

| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Rates and limits | Secant to tangent; the limit idea; continuity | Estimate speed from noisy position samples |
| 7.2 Rules | Power, product, quotient and chain rules; exp and log; derivatives of sigmoid and tanh | Derive σ′(x) = σ(x)(1 − σ(x)) and check it numerically |
| 7.3 Local approximation | Linear approximation and Taylor polynomials | Approximate √x and eˣ; plot the error against the step size |
| 7.4 Numerical derivatives | Forward vs central differences; truncation error vs rounding error; the best step | Log-log plot of error against h for both, and explain the V shape |
| 7.5 Newton's method | Root finding; quadratic convergence; failure cases | Implement Newton's method for √a and count correct digits per step |

**Check your understanding:** (1) Why does making h smaller eventually make a finite-difference estimate worse? (2) Why does Newton's method roughly double the number of correct digits per step near a root? (3) Where does the chain rule appear when you differentiate σ(wx + b)?

### Chapter 8 · Integrals (week 10)

| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Accumulation | Riemann sums, the definite integral, area | Distance travelled from a velocity log |
| 8.2 The fundamental theorem | Antiderivatives of common functions | Check three integrals symbolically with SymPy and numerically |
| 8.3 Numerical integration | Trapezoid and Simpson rules; order of error | Compare errors as n doubles and read off the order from the slope |
| 8.4 Integrals and probability | Densities, probabilities as areas, expectation as an integral; Monte Carlo integration (continued in [FND116](../FND116_probability_and_statistics_i/README.md)) | Estimate π and ∫e^(−x²) dx by Monte Carlo and show the error shrinking like 1/√n |

**Check your understanding:** (1) Why does Simpson's rule beat the trapezoid rule on smooth functions? (2) Why is Monte Carlo slow in one dimension but often the only option in 100? (3) What does the area under a density between a and b mean?

### Chapter 9 · Multivariable calculus (week 11)

| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Partial derivatives | Functions of several variables, level curves, partials | Contour-plot a loss surface and compute its partials |
| 9.2 Gradients | Steepest ascent, perpendicular to level curves; directional derivatives | Draw gradient arrows on the contour plot |
| 9.3 Jacobians, Hessians and matrix calculus | Linearisation in many dimensions; ∇(aᵀx), ∇(xᵀAx), ∇‖Ax − b‖² (MIT 18.S096 style) | Derive ∇‖Ax − b‖² = 2Aᵀ(Ax − b) and confirm it numerically |
| 9.4 Gradient checking | Finite-difference checks and relative error | Write `grad_check(f, grad_f, x)` and use it for the rest of the course |

**Check your understanding:** (1) Why is the gradient perpendicular to level curves? (2) What is the shape of the gradient of a scalar loss with respect to a 3×4 weight matrix? (3) What relative error in a gradient check should make you suspicious?

### Chapter 10 · The chain rule, computational graphs and backpropagation (week 12)

| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Computational graphs | The multivariable chain rule on a graph of operations | Draw the graph of a two-layer network's loss |
| 10.2 Forward vs reverse mode | Why reverse mode wins with many inputs and one output | Count the operations each mode needs on a small graph |
| 10.3 Backpropagation | Reverse-mode automatic differentiation (Rumelhart, Hinton and Williams, 1986); local gradients and accumulation | A scalar autodiff engine of about 100 lines, in the style of micrograd, with every gradient checked |
| 10.4 Vectorised gradients | Gradients of `matmul`, `sum` and elementwise operations; shape rules | Extend the engine to NumPy arrays and check it with `grad_check` |

**Check your understanding:** (1) Why does backpropagation cost about the same as a few forward passes? (2) Why must gradients be accumulated (`+=`) when a value is used twice? (3) What memory does reverse mode need that forward mode does not?

### Chapter 11 · Optimisation (weeks 13–14)

| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Critical points | Minima, maxima, saddles; the Hessian test; convexity, intuitively | Classify the critical points of four functions |
| 11.2 Gradient descent | Learning rate; convergence and divergence on quadratics, tied to eigenvalues and condition number | Plot descent paths on an elongated bowl for three learning rates |
| 11.3 Variants | Mini-batch and stochastic gradient descent, momentum, Adam (intuition) | Fit linear regression on 10⁵ rows with batch and mini-batch descent; compare with `lstsq` |
| 11.4 Numerical stability in ML | Softmax overflow; the log-sum-exp trick; float32 vs float64 | Implement a stable softmax and cross-entropy and test them with logits of ±1,000 |
| 11.5 Constraints | Lagrange multipliers as a geometric picture | Maximise area for a fixed perimeter by hand and with `scipy.optimize` |

**Check your understanding:** (1) Why does gradient descent zig-zag on an elongated bowl, and how does feature scaling help? (2) What is the largest stable learning rate for a quadratic with Hessian H? (3) Why does log-sum-exp give the same answer without overflowing?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · NumPy and vectors | Similarity search notebook |
| 2 | 2 | Lab 2 · Matrix multiplication | Timing plot; paper quiz 1 |
| 3 | 3 | Lab 3 · Transformations | Animated transformations; P1 starts |
| 4 | 4 | Lab 4 · Elimination and conditioning | Solver with tests; P1 due |
| 5–6 | 5 | Lab 5 · Least squares | Rainfall trend and residuals |
| 7–8 | 6 | Lab 6 · PageRank; Lab 7 · SVD | Converged ranks; compression plot; P2 starts |
| 9 | 7 | Lab 8 · Numerical derivatives | Error-vs-h plot |
| 10 | 8 | Monte Carlo integration | P2 due |
| 11 | 9 | Lab 9 · Gradients and checks | `grad_check` utility |
| 12 | 10 | Autodiff engine | Engine passing gradient checks; P3 starts |
| 13–14 | 11 | Lab 10 · Optimiser experiments | Learning-rate study |
| 15 | Review and exam | Written exam (AI off) and P3 demo | P3 due |

Every week also has a 30-minute paper quiz, done without AI.

## Working with AI in this course

- **Use AI for:** a second explanation or picture of an idea after you have worked an example yourself; extra practice problems (verify the answers yourself); turning notation into NumPy code; hints when a derivation is stuck, as long as you finish it yourself.
- **Do without AI (drills):** the weekly paper quiz. It covers elimination on 3×3 systems, 2×2 eigenvalues, chain-rule derivatives, gradients of matrix expressions, and sketching what a matrix does to the unit square. All proofs and derivations in graded work are your own.
- **Verify AI output by:** `np.allclose` against NumPy and SciPy; SymPy (or [SymPy Live](https://live.sympy.org/)) for symbolic results; a finite-difference gradient check for every derivative; plugging random matrices into any claimed identity; checking shapes before values.
- **Where AI still fails here:** the GSM-Symbolic results (above) show that fluent mathematical reasoning can break when the surface of a problem changes. In practice, log the errors you catch: arithmetic slips in long fraction work, sign errors in derivatives, transposes missing from matrix gradients, and convergence claims made without their conditions. A random-matrix check catches most of these in seconds.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Weekly paper quizzes, AI off | 15% |
| Labs (10) | 20% |
| Projects P1 · P2 · P3 | 8% · 12% · 15% |
| Final exam: 2 hours written (AI off) plus 1 hour computational | 30% |

**Mastery gate.** You pass when you can, on paper and without AI:
- row-reduce a 3×3 system;
- find the eigenvalues and eigenvectors of a 2×2 matrix and say what they mean geometrically;
- derive the gradient of the least-squares loss in matrix form.

Then, in NumPy, you implement gradient descent for linear regression that agrees with `np.linalg.lstsq` to four decimal places and passes a gradient check.

## Industry reality

Machine-learning engineers rely on this course daily, even when frameworks hide it: PyTorch autograd and JAX implement reverse-mode differentiation. Graphics and game engines compose model, view and projection matrices for every frame. PageRank was published as an eigenvector computation. JPEG's baseline mode transforms 8×8 blocks with the DCT (ITU-T T.81). Recommendation systems factorise rating matrices. ML, data science, graphics and quantitative interviews test these ideas directly.

**Interview questions from this course**

1. *"What is an eigenvector, and why does power iteration find the dominant one?"* Av = λv; repeated multiplication amplifies the component with the largest |λ|; convergence rate |λ₂/λ₁|; why PageRank adds damping.
2. *"How do you solve Ax = b in code? Why not `inv(A) @ b`?"* LU-based `solve` is cheaper and more accurate; conditioning; `lstsq` or QR for non-square systems; always check the residual.
3. *"Derive the gradient of mean squared error for linear regression and implement gradient descent."* L = (1/n)‖Xw − y‖², ∇L = (2/n)Xᵀ(Xw − y); a step-size limit set by the largest eigenvalue of XᵀX; feature scaling; a stopping rule; comparison with the closed form.
4. *"Explain backpropagation."* A computational graph; local derivatives; reverse accumulation by the chain rule; cost of a small multiple of the forward pass; memory for stored activations; gradient checking.
5. *"What does the SVD give you, and how would you use it?"* UΣVᵀ with ordered singular values; best rank-k approximation; storage k(m + n + 1) instead of mn; image compression and the missing-data problem in recommenders.

## Resources (free first)

- **Linear algebra:** [MIT 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) and [18.06SC](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) (Strang); [3Blue1Brown, Essence of linear algebra](https://www.3blue1brown.com/lessons/vectors); [Immersive Linear Algebra](https://immersivemath.com/ila/index.html); [Hefferon, *Linear Algebra*](https://hefferon.net/linearalgebra/); [Axler, *Linear Algebra Done Right*, 4th ed.](https://linear.axler.net/) (open access, proof-based, for later); [NPTEL Linear Algebra](https://nptel.ac.in/courses/111104137) (IIT Kanpur).
- **Calculus:** [MIT 18.01SC](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) and [18.02SC](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/); [3Blue1Brown, Essence of calculus](https://www.3blue1brown.com/lessons/essence-of-calculus); [OpenStax Calculus, Vol. 1](https://openstax.org/books/calculus-volume-1/pages/preface) to [Vol. 3](https://openstax.org/books/calculus-volume-3/pages/preface); [Strang, *Calculus*](https://ocw.mit.edu/courses/res-18-001-calculus-fall-2023/); [MIT 18.S096 Matrix Calculus for Machine Learning and Beyond](https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/).
- **Bridging to ML and graphics:** [*Mathematics for Machine Learning*](https://mml-book.github.io/) (Deisenroth, Faisal, Ong); [Google ML Crash Course: gradient descent](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent); [CS231n optimisation notes](https://cs231n.github.io/optimization-1/); [micrograd](https://github.com/karpathy/micrograd); [LearnOpenGL: Transformations](https://learnopengl.com/Getting-started/Transformations); [Scratchapixel](https://www.scratchapixel.com/).
- **Tools:** [NumPy](https://numpy.org/doc/stable/) and [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html); [broadcasting rules](https://numpy.org/doc/stable/user/basics.broadcasting.html); [SciPy optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html); [SymPy](https://www.sympy.org/en/index.html); [The Matrix Cookbook](https://www2.imm.dtu.dk/pubdb/edoc/imm3274.pdf); [Jupyter](https://jupyter.org/).

## Sources

All checked 12 Oct 2026.

- Brin and Page, "The Anatomy of a Large-Scale Hypertextual Web Search Engine" (1998), doi:10.1016/S0169-7552(98)00110-X — https://snap.stanford.edu/class/cs224w-readings/Brin98Anatomy.pdf
- ITU-T Recommendation T.81 (JPEG), 1992 — https://www.w3.org/Graphics/JPEG/itu-t81.pdf
- Rumelhart, Hinton and Williams, "Learning representations by back-propagating errors", *Nature* 323 (1986), doi:10.1038/323533a0 — https://www.nature.com/articles/323533a0
- Google DeepMind, Gemini Deep Think at IMO 2025 (21 Jul 2025) — https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/
- Mirzadeh et al., "GSM-Symbolic" (arXiv 2410.05229, revised Aug 2025) — https://arxiv.org/abs/2410.05229
- PyTorch autograd — https://pytorch.org/docs/stable/autograd.html · JAX automatic differentiation — https://docs.jax.dev/en/latest/automatic-differentiation.html
- NumPy releases (2.5 series, 2026) — https://numpy.org/news/ · Python 3.15.0 (Oct 2026) — https://www.python.org/downloads/release/python-3150/
- IMD rainfall data, Open Government Data Platform India — https://data.gov.in/catalog/rainfall-india · SNAP web-Google graph — https://snap.stanford.edu/data/web-Google.html
- ACM/IEEE-CS/AAAI CS2023, Mathematical and Statistical Foundations — https://csed.acm.org/mathematical-and-statistical-foundations/

_Last reviewed: 2026-10_
