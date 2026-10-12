# DLR301 · Labs and projects

Every lab and project ships with code, a test suite (gradient checks in float64 plus comparisons against PyTorch), and a short write-up with measured numbers. Labs 1–8 run on a laptop CPU; Labs 9–10 and P3 use a free Colab or Kaggle GPU.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Strides and broadcasting | Implement `transpose`, slicing and `expand` by editing strides; predict 20 broadcasting results before running them | Code, a table of predictions vs results, one paragraph on the `(N,)` vs `(N,1)` trap | 2 h |
| 2 · Gradcheck harness | A reusable `gradcheck(f, *inputs)` with central differences, relative error and random shapes (including size-1 and broadcast dimensions) | Harness plus tests for 10 hand-derived VJPs | 3 h |
| 3 · Engine core | `Tensor` with graph recording, iterative topological sort, gradient accumulation, `no_grad`, `detach` | Engine passing 20 gradchecks; a test that fails if accumulation is replaced by assignment | 5 h |
| 4 · Stable operators | Naive vs stable softmax, log-softmax, fused cross-entropy, BCE with logits | Overflow/NaN reproductions and fixes; error vs float64 reference for each | 3 h |
| 5 · Mini-framework on MNIST | `Module`, `Linear`, `Dropout`, SGD/momentum/AdamW, data loader; train an MLP | ≥ 97% MNIST test accuracy; optimizer updates matched to `torch.optim` within 1e-6 | 5 h |
| 6 · Initialisation zoo | 50-layer MLPs under N(0,1), Glorot, He and scaled-residual initialisation | Per-layer activation and gradient std plots; dead-unit counts; explanation tied to the variance formula | 4 h |
| 7 · Calibration | Reliability diagram and expected calibration error; temperature scaling on a validation split | ECE before/after, with accuracy shown unchanged | 3 h |
| 8 · Backprop ninja | Manual backward through embedding, linear, batch norm, tanh and cross-entropy | Every intermediate gradient matched to autograd with relative error < 1e-6 | 5 h |
| 9 · PyTorch internals | Custom `autograd.Function` for a fused op; per-example gradient norms with `torch.func.vmap`; trigger and fix an in-place error | Code passing `torch.autograd.gradcheck`; memory and speed comparison of fused vs unfused | 4 h |
| 10 · Reproducibility and bug hunt | 5-seed runs with resume-from-checkpoint; then diagnose 10 scripts with one planted bug each (swapped by a classmate) | Seed-variance table; for each bug: symptom, detection method, fix | 5 h |

## Projects

### P1 · Devanagari handwriting recogniser on your own engine (L1, ~6 hours)

**Real-world inspiration.** Handwritten forms in Indian scripts remain common in post offices, banks and examinations. The Devanagari Handwritten Character Dataset (UCI Machine Learning Repository, https://archive.ics.uci.edu/dataset/389/devanagari+handwritten+character+dataset) provides 92,000 images (32×32) in 46 classes: 36 consonants and 10 digits.

**What to build.** Using only your Lab 3–5 engine (NumPy, no PyTorch), train an MLP on the dataset's 10 digit classes, then on all 46 classes. Include a data loader with a fixed train/validation/test split, AdamW, and an evaluation script.

**Acceptance criteria**
- ≥ 95% test accuracy on the 10 digit classes; the 46-class accuracy is reported honestly whatever it is.
- The first-step loss is within 10% of −log(1/C) for each task, and the README explains why.
- Every operator in the engine passes the Lab 2 gradcheck; the test suite runs in under 60 s on a laptop.
- A confusion matrix and 20 misclassified examples with a one-line hypothesis each.

**Compute budget.** CPU only; training finishes in under 30 minutes on a laptop.

**Stretch goals.** Replace the MLP with a small convolution implemented via `im2col` in your engine; compare with the same model in PyTorch for speed.

**What it proves to an employer.** You understand training from the tensor up and you test numerical code properly.

### P2 · Character-level language model with a hand-checked backward pass (L2, ~15 hours)

**Real-world inspiration.** Bengio et al.'s neural probabilistic language model (JMLR, 2003) introduced learned embeddings for next-token prediction, the direct ancestor of modern LLMs. Transliteration keyboards for Indian languages need models of how words are spelled in Latin script; AI4Bharat's Aksharantar dataset contains 26 million transliteration pairs across 21 Indian languages (Madhani et al., 2022, https://arxiv.org/abs/2205.03018).

**What to build.** A character-level MLP language model (context of 8 characters, embeddings, two hidden layers with batch normalisation) trained on romanised Hindi words from Aksharantar. Implement it twice: (a) with autograd in PyTorch, and (b) with a fully manual backward pass in NumPy that you derive.

**Acceptance criteria**
- Manual and autograd gradients agree for every parameter tensor (relative error < 1e-6 in float64) on 100 random batches.
- Validation negative log-likelihood beats a count-based bigram baseline and a trigram baseline with add-k smoothing, with all three numbers reported.
- Initialisation is justified: activation statistics per layer at step 0 are shown, and tanh saturation is below 5% of units.
- 50 sampled words are shown, with a short analysis of which spelling patterns the model learned and which it did not.
- The full run is reproducible from a seed (two runs give identical losses).

**Compute budget.** CPU only, or under 1 GPU-hour on a free T4.

**Stretch goals.** Add a WaveNet-style hierarchical context; train on Bengali or Tamil romanisations and compare perplexities.

**What it proves to an employer.** You can derive and verify gradients for a real model, which is what implementation interviews for research roles test.

### P3 · A tested mini deep learning framework (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** micrograd, MiniTorch, tinygrad and CMU's needle show that a small, readable framework is the best way to understand PyTorch. Framework teams (PyTorch, JAX, tinygrad) hire people who can reason about autograd, memory and numerical correctness.

**What to build.** Extend your engine into a documented package:
1. at least 30 differentiable operators, including indexing with repeated indices, `einsum` for two-operand contractions, fused log-softmax cross-entropy and layer normalisation;
2. modules, AdamW, a learning-rate schedule and checkpoint save/resume (including optimizer and RNG state);
3. activation checkpointing for `Sequential` blocks;
4. an optional GPU backend through CuPy (or a clear plan for one);
5. a property-based test suite (Hypothesis) that compares every operator's output and gradient with PyTorch;
6. a short "AI failure log" from the course with every case where generated backward code failed your tests.

**Acceptance criteria**
- 1,000 randomly generated property tests pass against PyTorch (forward and gradient, tolerance stated per dtype).
- A 4-layer MLP on Fashion-MNIST trained with your framework ends within 0.5 percentage points of an identical PyTorch model (same initialisation, seed and data order), averaged over 3 seeds.
- Activation checkpointing reduces measured peak memory by ≥ 40% on a 32-layer MLP at a stated batch size, and the extra compute time is reported.
- Resume-from-checkpoint reproduces the uninterrupted loss curve exactly.
- README with architecture diagram, API examples, benchmarks against PyTorch on CPU, and known limitations.

**Compute budget.** Under 4 GPU-hours on a free T4; everything else runs on CPU.

**Stretch goals.** Lazy evaluation with simple kernel fusion (tinygrad style); higher-order gradients; a tiny transformer block trained with your framework (after DLR303 Chapter 4).

**What it proves to an employer.** You can build and test infrastructure that other researchers rely on, and you know where generated code breaks. This is a strong signal for research-engineer and ML-framework roles.

## Feeds into

- [DLR303 Sequence Models and Transformers](../DLR303_sequence_models_and_transformers/README.md): your engine and manual-backward skills are reused to build attention and a GPT.
- [DLR304 Training Deep Networks](../DLR304_training_deep_networks_optimization/README.md): optimizers, initialisation and debugging become a full course.
- [DLR401 Large Language Models](../../year_4/DLR401_large_language_models_pretraining_fine_tuning/README.md): the formal follow-on in the catalogue.
- [DLR404 Efficient Deep Learning and GPU Programming](../../year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md): custom `autograd.Function` plus fused kernels in Triton.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): the testing discipline used to reproduce results.
