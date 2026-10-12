# FND113 · Labs and projects

All work is done in Python with NumPy (SciPy and matplotlib where stated) in Jupyter notebooks or scripts kept under Git. Every numerical claim must be backed by a check: `np.allclose` against a library routine, a gradient check, or a convergence plot. Paper-and-pencil derivations are submitted as scans or typed LaTeX/Markdown, and must be your own.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · NumPy and vectors | Broadcasting drills; cosine-similarity search over 200 short documents | Notebook with a vectorised search and timings for the loop and vectorised versions | 3 h |
| 2 · Matrix multiplication | Triple-loop multiplication vs `@` for n = 100 to 1,000; adjacency-matrix powers on a small graph | Timing plot, path counts checked against a brute-force count | 3 h |
| 3 · Transformations | Animate the unit square under rotation, shear, reflection and projection; rotate about an arbitrary point with homogeneous coordinates | Animation and a written explanation of composition order | 4 h |
| 4 · Elimination and conditioning | Gaussian elimination with partial pivoting; Hilbert matrices up to n = 14 | Solver with tests against `np.linalg.solve`; an error vs condition-number plot | 5 h |
| 5 · Least squares | Rainfall trend fit with residual analysis; polynomial overfitting; QR vs normal equations | Notebook with plots and a short interpretation | 4 h |
| 6 · PageRank | Power iteration on a toy web and a SNAP graph; effect of the damping factor | Converged ranks and iteration counts against damping | 4 h |
| 7 · SVD | Grayscale image compression at several ranks | An error and storage vs k plot, with images | 3 h |
| 8 · Numerical derivatives | Forward and central differences across h = 10⁻¹ to 10⁻¹⁶; Newton's method | Error-vs-h log-log plot with the V shape explained | 3 h |
| 9 · Gradients and checks | Contour plots with gradient fields; a `grad_check` utility; three matrix-calculus identities verified | Utility with tests, and plots | 4 h |
| 10 · Optimiser experiments | Gradient descent, momentum and Adam on an elongated quadratic and on linear regression | Path plots for each learning rate, and the divergence threshold compared with 2/λ_max | 5 h |

## Projects

### P1 · Image transformer from scratch (L1, ~6 hours)

**Real-world inspiration.** Every image editor, map viewer and game engine applies affine transforms. [LearnOpenGL's transformations chapter](https://learnopengl.com/Getting-started/Transformations) shows the same matrices driving real-time graphics.

**What to build.** A NumPy-only module and CLI that apply rotation about any point, scaling, shear, reflection and translation to an image. It uses inverse mapping and bilinear interpolation, and a `compose()` function builds one 3×3 matrix from a list of steps.

**Acceptance criteria**
- `compose(T, inverse(T))` equals the identity matrix within 1e-12 for 100 random transforms.
- Four 90° rotations reproduce the original image exactly.
- Inverse mapping leaves no unfilled pixels inside the transformed region, checked on 20 random transforms.
- The output is within a mean absolute error of 1.0 (on 0–255) of [`scipy.ndimage.affine_transform`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.affine_transform.html) with `order=1`, after you document how you matched its coordinate conventions.
- A 1-megapixel image transforms in under 1 second, with no per-pixel Python loops.
- The README shows "scale then rotate" and "rotate then scale" side by side and explains the difference with matrices.

**Common pitfalls.**
- Forward mapping (pushing source pixels to the output), which leaves holes.
- Mixing (row, column) with (x, y), which flips the direction of rotation.
- Rotating about the image corner when you meant its centre.

**Stretch goals.** A perspective (homography) warp from four point pairs, found by solving an 8×8 linear system: straighten a photo of a document.

**What it proves to an employer.** You can turn matrix mathematics into fast, correct, tested code.

### P2 · Ranking and compression with eigenvectors and the SVD (L2, ~15 hours)

**Real-world inspiration.** PageRank ranked the early Google web as the principal eigenvector of a link matrix ([Brin and Page, 1998](https://snap.stanford.edu/class/cs224w-readings/Brin98Anatomy.pdf)). Low-rank approximations underlie image compression and classic recommender systems.

**What to build**
- **(a) PageRank** with damping on the [SNAP web-Google graph](https://snap.stanford.edu/data/web-Google.html), using [`scipy.sparse`](https://docs.scipy.org/doc/scipy/reference/sparse.html) and handling dangling nodes correctly.
- **(b) SVD** low-rank approximation of images, and of the [MovieLens 100K](https://grouplens.org/datasets/movielens/) rating matrix (respect its [usage licence](https://files.grouplens.org/datasets/movielens/ml-100k-README.txt)).

**Acceptance criteria**
- **Subgraph check.** On a 1,000-node subgraph, power iteration matches the normalised principal eigenvector from `np.linalg.eig` to an L1 distance below 1e-8.
- **Full graph.** It runs in under 2 minutes and 4 GB of RAM (state your hardware), and the ranks sum to 1 within 1e-10.
- **Damping study.** Iteration counts for damping 0.5, 0.85 and 0.95 are reported and explained through the eigenvalue gap.
- **SVD theory check.** The squared Frobenius error of each rank-k image approximation equals the sum of the discarded σᵢ² to within 1e-8 (relative). This confirms the Eckart–Young theorem numerically.
- **MovieLens.** With 10% of ratings held out, report the RMSE of rank-k reconstructions (with mean imputation) for k = 2 to 50 against user-mean and global-mean baselines. Discuss why missing data makes plain SVD a weak recommender.
- **Report.** A report of at most 4 pages explains each result in linear-algebra terms.

**Common pitfalls.**
- Dangling nodes leaking probability mass, so the ranks no longer sum to 1.
- Building a dense matrix for the full graph, which cannot fit in memory.
- Comparing eigenvectors without normalising their sign and scale.
- Treating missing ratings as zeros.

**Stretch goals.** Personalised PageRank from a seed set; [randomised SVD](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html) timed against a full SVD.

**What it proves to an employer.** You can run linear algebra at real scale with sparse data, and explain the results instead of just reporting them.

### P3 · A tiny autodiff engine and a model trained from scratch (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** [PyTorch autograd](https://pytorch.org/docs/stable/autograd.html) and [JAX](https://docs.jax.dev/en/latest/automatic-differentiation.html) implement reverse-mode automatic differentiation. Karpathy's [micrograd](https://github.com/karpathy/micrograd) shows the core fits in a few hundred lines.

**What to build.** A NumPy `Tensor` class with reverse-mode autodiff.
- **Operations:** `+`, `−`, `×`, `÷`, `matmul`, `sum`, `mean`, `exp`, `log`, `tanh`, `relu` and a stable `log_softmax`, all with broadcasting-aware gradients.
- **Optimisers:** SGD with momentum, and Adam.
- **Models to train:** linear regression, logistic regression, and a two-layer MLP on scikit-learn's built-in [digits dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html) (8×8 images, no download needed).

**Acceptance criteria**
- **Gradient checks.** Every operation passes `grad_check` with relative error below 1e-6 in float64 on 100 random inputs, including broadcasting cases.
- **Linear regression.** Training through the engine matches `np.linalg.lstsq` to 1e-4.
- **MLP.** At least 95% test accuracy on digits with a fixed seed and a stratified 80/20 split, with training and test curves plotted.
- **Stability.** `log_softmax` and cross-entropy return finite values for logits of ±1,000, with tests.
- **Learning-rate study.** Five learning rates, with divergence explained by the curvature of the loss.
- **Write-up.** At most 6 pages: the computational graph, your own derivations for the `matmul` and softmax-cross-entropy gradients, and your design decisions.

**Option B (graphics track).** A NumPy software renderer that loads an OBJ mesh and applies model, view and projection matrices. It culls back faces with cross-product normals, uses a z-buffer, and shades faces with flat and Gouraud shading. It meets these targets:
- it renders a provided mesh from three camera poses with fewer than 1% of pixels differing from reference images;
- it renders 100,000 triangles in under 5 seconds.

Inspiration: [tinyrenderer](https://github.com/ssloy/tinyrenderer) and [Scratchapixel](https://www.scratchapixel.com/).

**Common pitfalls.**
- Forgetting to reset gradients between optimisation steps.
- Wrong gradients for broadcast operations: you must sum over the broadcast axes.
- Running gradient checks in float32, which is too imprecise to tell a bug from rounding.
- In-place updates on arrays that alias another tensor's storage.

**Stretch goals.** A convolution operation with checked gradients; mini-batch data loading; for Option B, texture mapping with perspective-correct interpolation.

**What it proves to an employer.** You understand what deep-learning frameworks, or graphics pipelines, do underneath, and you verify numerical code rigorously. Both are rare at the intern level.

## Feeds into

- [CS206 Mathematics for Machine Learning](../../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md): eigen-decomposition, SVD, matrix calculus and optimisation continue directly.
- [CS214 Machine Learning Foundations](../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md): least squares, gradient descent and logistic regression become ML models.
- [DLR301 Neural Networks from Scratch: Autograd and Backpropagation](../../../03_majors/deep_learning/year_3/DLR301_neural_networks_from_scratch_autograd/README.md) and [MLE301 Machine Learning Algorithms from Scratch](../../../03_majors/machine_learning_engineering/year_3/MLE301_machine_learning_algorithms_from_scratch/README.md) extend P3.
- [CSG304 Computer Graphics](../../../03_majors/computer_science_general/year_3/CSG304_computer_graphics/README.md) extends Chapter 3 and P3 Option B.
- [FND116 Probability and Statistics I](../FND116_probability_and_statistics_i/README.md) uses integrals and Monte Carlo from Chapter 8.
