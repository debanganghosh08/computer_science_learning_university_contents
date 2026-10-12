# DLR301 · Neural Networks from Scratch: Autograd and Backpropagation

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS206](../../../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md) | [DLR401](../../year_4/DLR401_large_language_models_pretraining_fine_tuning/README.md); taken alongside [DLR302](../DLR302_computer_vision_from_cnns_to_vision_transformers/README.md) and [DLR303](../DLR303_sequence_models_and_transformers/README.md); prepares for [DLR304](../DLR304_training_deep_networks_optimization/README.md) and [DLR404](../../year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md) |

## Why this course matters now

Every deep learning system, from a crop-disease classifier to a frontier language model, is trained by the same machine: a tensor library that records operations and runs reverse-mode automatic differentiation. PyTorch builds this graph dynamically on every forward pass (Paszke et al., 2019), and Karpathy's llm.c trains GPT-2 in plain C/CUDA with every backward pass written by hand. Coding assistants such as Claude Code, Cursor and GitHub Copilot now produce a working training script in seconds. The dangerous bugs are the silent ones: a softmax over the wrong axis, a bias gradient that is not summed over the batch, a model left in training mode during evaluation. These still produce a loss curve that goes down. On METR's RE-Bench, the best agents beat human experts at 2-hour budgets, but experts scored twice as high when both had 32 hours (Wijk et al., 2024). The long, careful debugging is still where people win. The AI Index 2026 also cites a study in which heavy AI reliance while learning led to "learning penalties". So this course has you build the machine yourself before you rely on it. CS206 and CS214 built a scalar autograd engine. Here you build a tensor engine with broadcasting, stable numerics, modules and optimizers, then map every piece onto PyTorch's internals.

## Learning outcomes

By the end you can:

1. **Implement** a tensor autograd engine (NumPy backend) with broadcasting, reductions, indexing and matrix multiplication, and **prove** each gradient correct with float64 finite-difference checks.
2. **Derive** vector–Jacobian products by hand for matmul, softmax, log-softmax cross-entropy, layer and batch normalisation, and embedding lookup.
3. **Explain** why each initialisation (Glorot, He, scaled residual) preserves signal variance, and **measure** activation and gradient statistics layer by layer.
4. **Write** numerically stable kernels (log-sum-exp, fused cross-entropy, BCE with logits), and **show** the failure of the naive versions.
5. **Use** PyTorch autograd internals: `grad_fn`, saved tensors, hooks, custom `autograd.Function`, `torch.func.vmap`/`grad`, higher-order gradients and anomaly detection.
6. **Predict** and **measure** the memory of backpropagation, and **reduce** it with activation checkpointing.
7. **Debug** a broken training run systematically: loss at initialisation, overfitting one batch, gradient-norm tracking, and finding bugs by bisection.
8. **Audit** AI-generated model code with gradient checks, shape tests and controlled experiments.

## Chapters and lessons

### Chapter 1 · Tensors and how they live in memory (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Shapes, dtypes and devices | Scalars to n-d arrays; float32, float64, bfloat16, int64; CPU vs GPU memory | Predict `dtype` and shape of 15 expressions, then check in NumPy and PyTorch |
| 1.2 Strides and views | A tensor is a pointer, a shape and strides; `transpose`, `reshape`, `view`, slicing without copies; contiguity | Implement `transpose` and slicing by editing strides only; verify with `np.lib.stride_tricks.as_strided` |
| 1.3 Broadcasting | The trailing-dimension rule; why `(N,)` minus `(N,1)` silently becomes `(N,N)` | Find the broadcasting bug in 5 short snippets |
| 1.4 Einsum as a language | Index notation for batched matmul, outer products, traces and attention scores | Rewrite 8 loops as single `einsum` calls; time both |

**Check your understanding:** Why can `transpose` be free while `reshape` sometimes must copy? A loss computed as `((pred - y)**2).mean()` is 100× too large; which broadcasting mistake is likely? When does an einsum hide an O(n³) cost?

### Chapter 2 · The chain rule for tensors (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Jacobians and VJPs | Why backprop never builds a Jacobian; the vector–Jacobian product as the unit of work | Derive VJPs for `add`, `mul`, `exp`, `log`, `sum`, `mean` |
| 2.2 The shape rule | The gradient has the shape of its input; broadcast in the forward means sum in the backward | Derive the backward of broadcasting add and multiply |
| 2.3 Matmul and reductions | `dA = dC Bᵀ`, `dB = Aᵀ dC`; max/argmax gradients; `keepdims` | Verify matmul VJPs on random shapes |
| 2.4 Gradient checking | Central differences, float64, relative error, step size trade-off, kinks at ReLU | Write `gradcheck(f, inputs)` used for the rest of the course |

**Check your understanding:** Why is reverse mode efficient for a scalar loss and forward mode for one input with many outputs? Your gradient check fails only near zero for ReLU; is the backward wrong? Why must gradient checks run in float64?

### Chapter 3 · Building a tensor autograd engine (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 The `Tensor` class | Data, gradient, parents, backward closure; leaf vs intermediate tensors | Engine skeleton with `+`, `*`, `@`, `sum` |
| 3.2 Topological order | DFS ordering of the graph; one backward sweep; why a recursive version hits Python's recursion limit | Iterative topological sort on a 10,000-node graph |
| 3.3 Accumulation | A tensor used twice receives the sum of gradients; zeroing gradients between steps | Write the test that catches overwriting instead of accumulating |
| 3.4 Control | `no_grad`, `detach`, `requires_grad`, freeing the graph after backward | Show memory growing when the graph is never freed |

**Check your understanding:** What breaks if two branches overwrite rather than add their gradients? Why does a detached tensor stop gradient flow, and when do you want that (targets, EMA teachers)? What exactly can be freed after `backward()`?

### Chapter 4 · The operator library and numerics (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Shape operators | `reshape`, `transpose`, `getitem`, `concat`, `stack` and their backward passes (scatter-add for indexing) | Gradcheck all shape ops |
| 4.2 Stable softmax | Subtract the max; log-sum-exp; `log_softmax` | Show `exp(1000)` overflow; fix it |
| 4.3 Fused cross-entropy | Gradient `softmax(z) − onehot(y)`, scaled by 1/N; why fusing saves memory and avoids `log(0)` | Compare composed vs fused cross-entropy at logits of ±50 |
| 4.4 Sigmoid and BCE with logits | `log(1+e^x)` computed safely (softplus) | Reproduce a NaN from naive BCE; fix it |
| 4.5 Precision | float32 machine epsilon, bfloat16's 8-bit mantissa, cancellation in variance computation | Compute variance three ways in bfloat16; explain the error |

**Check your understanding:** Why does every framework expose cross-entropy on logits rather than on probabilities? Which operations are safe in bfloat16 and which need float32 accumulation? Why is `x[idx] += g` the wrong backward for indexing when `idx` has duplicates?

### Chapter 5 · Modules, parameters and optimizers (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The module tree | `Module`, `Parameter`, `parameters()`, `state_dict`, train/eval flags | Build `Linear`, `Sequential`, `ReLU`, `Dropout` |
| 5.2 Optimizers | SGD, momentum, Adam with bias correction, decoupled weight decay (AdamW) | Implement all four; match `torch.optim` updates to 1e-6 |
| 5.3 Data loading | Shuffling, batching, the last partial batch, deterministic seeds | Data loader with reproducible shuffles |
| 5.4 The training loop | Forward, loss, zero grad, backward, step; evaluation loop without gradients | Train an MLP on MNIST to ≥ 97% test accuracy with your own engine |

**Check your understanding:** Why does Adam need bias correction in the first steps? What goes wrong if dropout stays active during evaluation? Why should evaluation run under `no_grad` even though it would be "correct" without it?

### Chapter 6 · Activations and initialisation (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Activation functions | Sigmoid and tanh saturation; ReLU, leaky ReLU, GELU (Hendrycks and Gimpel, 2016), SiLU | Plot each and its derivative; count dead ReLUs after training |
| 6.2 Variance propagation | Var(out) = fan_in · Var(w) · Var(in); forward and backward conditions | Derive the condition for a linear layer |
| 6.3 Glorot and He | Glorot and Bengio (2010) for tanh; He et al. (2015) for ReLU | 50-layer MLP: activation std per layer under 4 initialisations |
| 6.4 Residual connections | Why `x + f(x)` keeps gradients alive; scaling residual branches by 1/√(2L) | Train 20-layer MLPs with and without residuals |
| 6.5 Watching a network | Histograms of activations, gradients and update-to-weight ratios (~1e-3 as a rule of thumb) | A dashboard that flags saturation and dead units |

**Check your understanding:** Why does N(0, 1) initialisation explode a deep ReLU net while N(0, 2/fan_in) does not? Why is a zero-initialised hidden layer a problem but a zero-initialised last residual layer can be a good idea? What does an update-to-weight ratio of 1e-1 tell you?

### Chapter 7 · Losses and output layers as probability models (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Losses as likelihoods | MSE as Gaussian negative log-likelihood; cross-entropy as categorical; BCE for multi-label | Derive each from its likelihood |
| 7.2 Expected loss at initialisation | A C-class classifier should start near −log(1/C) | Detect a bad output initialisation from the first loss value |
| 7.3 Label smoothing and focal loss | Over-confidence, class imbalance (focal loss, Lin et al., 2017) | Train with and without smoothing; compare confidence histograms |
| 7.4 Calibration | Reliability diagrams, expected calibration error, temperature scaling | Calibrate your MNIST model; report ECE before and after |

**Check your understanding:** Your 10-class model's first loss is 9.7; what is wrong? Why does temperature scaling leave accuracy unchanged? When is MSE on logits a bad idea for classification?

### Chapter 8 · Backpropagation by hand (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 A two-layer MLP | Forward cache; backward in matrix form; bias gradients as batch sums | Manual NumPy backward matched to autograd |
| 8.2 Embeddings | Lookup as one-hot matmul; scatter-add of gradients | Character-level MLP with manual embedding gradients |
| 8.3 Batch normalisation backward | The full derivation; the compact form; train vs eval statistics | Manual batchnorm backward to relative error < 1e-6 |
| 8.4 Cross-entropy and tanh | Composing the full chain end to end | "Backprop ninja": the whole network by hand, every tensor checked |

**Check your understanding:** Why does the batchnorm gradient depend on every example in the batch? Where does the 1/N in the cross-entropy gradient come from, and what happens with gradient accumulation if you forget it? What changes in the embedding backward when one token appears twice in a batch?

### Chapter 9 · Inside PyTorch autograd (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Define-by-run graphs | `grad_fn`, `next_functions`, saved tensors, `retain_graph` | Walk the graph of a small model and print it |
| 9.2 In-place operations | Version counters; the "modified by an inplace operation" error | Trigger and fix the error three ways |
| 9.3 Custom functions | `torch.autograd.Function` with `forward`/`backward`, `ctx.save_for_backward`, `gradcheck` | A fused SiLU-multiply with a hand-written backward |
| 9.4 Higher-order and functional autodiff | `create_graph=True`, gradient penalties, `torch.func.grad`, `vmap`, `jacrev` | Per-example gradient norms with `vmap` |
| 9.5 Hooks and anomaly mode | Tensor and module hooks; `torch.autograd.detect_anomaly` | Find the op that first produces a NaN |

**Check your understanding:** Why does PyTorch refuse some in-place operations but not others? When is `retain_graph=True` a bug rather than a fix? How would you compute the gradient of a gradient norm, and what does it cost?

### Chapter 10 · Memory and speed of backpropagation (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 What backward saves | Activations kept for each op; activation memory ∝ batch × depth × width | Predict peak memory of an MLP; measure it with `torch.cuda.max_memory_allocated` |
| 10.2 Activation checkpointing | Recompute instead of store (Chen et al., 2016); the √n segment trade-off | `torch.utils.checkpoint` on a 32-layer MLP; plot memory and time |
| 10.3 Profiling | `torch.profiler`, CPU vs GPU time, synchronisation when timing | Profile one training step and name the top 3 ops |
| 10.4 `torch.compile` | Graph capture, fusion, recompilation; when it helps | Compare eager vs compiled throughput on a Colab T4 |

**Check your understanding:** Why does memory, not compute, usually limit batch size? Why does timing GPU code without synchronisation give wrong numbers? What does activation checkpointing cost in compute, and why is it worth it?

### Chapter 11 · PyTorch fluency and reproducible experiments (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Porting | Your engine's MLP to idiomatic PyTorch: `Dataset`, `DataLoader`, `nn.Module` | Same seed and initialisation, same loss curve in both |
| 11.2 Devices and mixed precision | `.to(device)`, pinned memory, `torch.autocast` with bfloat16 | Measure speed and accuracy change on a T4 |
| 11.3 Determinism | Seeds, cuDNN flags, non-deterministic ops; seed-to-seed variance | Run 5 seeds; report mean ± standard deviation |
| 11.4 Checkpoints and logging | Saving model, optimizer and RNG state; resuming exactly; TensorBoard or Weights & Biases | Kill and resume a run; prove the curves match |
| 11.5 Testing models | Shape tests, overfit-one-batch test, gradient-flow test, invariance tests | A pytest suite for your model |

**Check your understanding:** Why is a single run's accuracy not evidence that a change helped? What state, beyond weights, must a checkpoint hold to resume exactly? Which model bugs does an overfit-one-batch test catch, and which does it miss?

### Chapter 12 · Debugging neural networks (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 A training recipe | Karpathy's "A Recipe for Training Neural Networks" (2019): become one with the data, simple baselines, overfit, regularise, tune | Apply the recipe to a new dataset and log every step |
| 12.2 Silent bugs | Wrong softmax axis, label shuffling, data leakage, train/eval mode, wrong loss reduction, frozen layers | Bug hunt: 10 scripts, one planted bug each |
| 12.3 Reading loss curves | Plateaus, spikes, divergence, train/validation gaps | Diagnose 8 curves from logs only |
| 12.4 Bisection | Shrinking a failing run to a minimal reproduction | Reduce a failing 300-line script to under 40 lines |

**Check your understanding:** A model reaches 99% training accuracy and 10% validation accuracy on balanced 10-class data; list three causes and the check for each. Why should you look at raw data before tuning any hyperparameter? How do you tell an optimisation problem from a data problem?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Strides and broadcasting | Broadcasting bug report |
| 2 | 2 | Lab 2 · Gradcheck harness | VJP derivation sheet |
| 3 | 3 | Lab 3 · Engine core | Engine passes 20 gradchecks |
| 4 | 4 | Lab 4 · Stable operators | **P1 due** |
| 5 | 5 | Lab 5 · Mini-framework on MNIST | ≥ 97% test accuracy |
| 6 | 6 | Lab 6 · Initialisation zoo | Activation-statistics report |
| 7 | 7 | Lab 7 · Calibration | Reliability diagrams |
| 8 | 8 | Lab 8 · Backprop ninja | Mid-term (AI off) |
| 9 | 9 | Lab 9 · PyTorch internals | Custom `Function` passing `gradcheck` |
| 10 | 10 | Lab 9 (cont.) | **P2 due** |
| 11 | 11 | Lab 10 · Reproducibility | 5-seed report |
| 12 | 11 | Lab 10 (cont.) | Model test suite |
| 13 | 12 | Bug hunt | Bug-hunt write-up |
| 14 | 12 | Project studio | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating random test shapes and property-based tests (Hypothesis) for your operators; explaining PyTorch error messages; plotting dashboards; reviewing your derivations after you finish them; porting engine code to idiomatic PyTorch. Claude, ChatGPT and Gemini explain well; Claude Code, Cursor or GitHub Copilot can scaffold test suites.
- **Do without AI (drills):** every VJP derivation; the engine core (Chapter 3); the manual backward pass (Chapter 8); weekly 30-minute "derive and implement one operator" drills; both exams. You cannot audit a gradient you cannot derive.
- **Verify AI output by:** (1) float64 `gradcheck` on random shapes including size-1 and broadcast dimensions; (2) matching PyTorch outputs and gradients to 1e-6 relative error; (3) checking the loss at initialisation against −log(1/C); (4) overfitting one batch to near-zero loss; (5) running two seeds before believing any improvement.
- **Where AI still fails here:** keep a failure log. Ask an assistant for the backward of a broadcasting operation, of indexing with repeated indices, or of batch normalisation, then run your gradcheck and record what fails and why. Also log runs where AI-written training code trains but measures the wrong thing (evaluation in training mode, a leaked split). These failures are quiet, which is exactly why they need tests rather than trust. The evidence you collect becomes part of P3.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10, auto-graded tests plus short write-ups) | 25% |
| Projects P1–P3 | 30% |
| Derivation write-ups (Chapters 2, 4, 8) | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) and oral defence of P3 | 25% |

**Mastery gate.** You pass when you can, with AI tools off: (1) write from an empty file, in 90 minutes, a tensor autograd engine supporting broadcasting add and multiply, matmul, ReLU, sum and fused log-softmax cross-entropy that passes float64 gradient checks; (2) derive the batch-normalisation backward pass on paper and check it numerically; (3) find three planted bugs in an unfamiliar 200-line PyTorch training script within 30 minutes and explain how each one would show up in the metrics.

## Industry reality

Reverse-mode autodiff is the engine behind PyTorch (Paszke et al., 2019), JAX and TensorFlow; Baydin et al. (2018) survey the techniques. Hand-written backward passes are still used where performance matters: llm.c implements GPT-2 training in C/CUDA with explicit backward kernels, and fused operations with custom backward passes are standard in high-performance training code (see [DLR404](../../year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md)). Research-engineer interviews often include implementing or debugging a model component under time pressure ([DLR market page](../../../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md)).

**Interview questions from this course**

1. *Derive the gradient of mean cross-entropy with respect to the logits.* Strong answer: reaches (softmax(z) − onehot(y)) / N; explains the log-sum-exp trick and why frameworks fuse softmax with the loss; mentions label smoothing changing the target.
2. *Implement forward and backward for a two-layer MLP in NumPy.* Strong answer: states every shape; caches forward values; sums the bias gradient over the batch; handles the ReLU mask; adds a finite-difference check without being asked.
3. *Your loss became NaN at step 2,000. What do you do?* Strong answer: reproduces with a fixed seed; logs gradient norms and the step before; checks data for inf/NaN, learning rate, `log(0)` and fp16 overflow; uses anomaly detection or hooks to find the first bad op; applies a fix and explains why it works rather than adding gradient clipping blindly.
4. *Why does backprop cost about the same as the forward pass, and where does its memory go?* Strong answer: one VJP per op at a constant factor of the forward cost; activations saved for the backward pass dominate memory; checkpointing trades roughly one extra forward pass for √n memory.
5. *A 50-layer ReLU network does not train. Why might that be, and how do you fix it?* Strong answer: variance explosion or vanishing under the wrong initialisation; He initialisation; residual connections with scaled branches; normalisation; shows how to measure per-layer activation std to confirm.

## Resources (free first)

- **Primary course material:** Stanford CS231n (Spring 2026) notes on backpropagation and neural networks — https://cs231n.stanford.edu/ ; Andrej Karpathy, *Neural Networks: Zero to Hero* (micrograd; makemore part 4, "Becoming a backprop ninja") — https://karpathy.ai/zero-to-hero.html
- **Build-your-own-framework courses:** MiniTorch (Cornell Tech) — https://minitorch.github.io/ ; CMU 10-414/714 Deep Learning Systems ("needle") — https://dlsyscourse.org/
- **Textbooks:** Simon Prince, *Understanding Deep Learning* (MIT Press, 2023; free PDF) — https://udlbook.github.io/udlbook/ ; Zhang et al., *Dive into Deep Learning* — https://d2l.ai/ ; Goodfellow, Bengio and Courville, *Deep Learning* — https://www.deeplearningbook.org/
- **Documentation:** PyTorch autograd mechanics — https://docs.pytorch.org/docs/stable/notes/autograd.html ; PyTorch tutorials — https://pytorch.org/tutorials/ ; profiler recipe — https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html
- **Reference code:** micrograd — https://github.com/karpathy/micrograd ; tinygrad — https://github.com/tinygrad/tinygrad ; llm.c — https://github.com/karpathy/llm.c
- **Papers:** Baydin et al., "Automatic differentiation in machine learning: a survey" — https://arxiv.org/abs/1502.05767 ; Glorot and Bengio (2010) — https://proceedings.mlr.press/v9/glorot10a.html ; He et al. (2015) — https://arxiv.org/abs/1502.01852 ; Chen et al., "Training Deep Nets with Sublinear Memory Cost" — https://arxiv.org/abs/1604.06174
- **Guides:** Karpathy, "A Recipe for Training Neural Networks" — https://karpathy.github.io/2019/04/25/recipe/
- **Compute (free):** every lab runs on a CPU or a single free GPU. Google Colab's free tier gives notebooks of at most 12 hours with usage limits that "fluctuate" and are not published — https://research.google.com/colaboratory/faq.html. Kaggle notebooks offer free P100 or 2× T4 GPUs with a weekly GPU quota shown in your account settings, and sessions of up to 12 hours — https://www.kaggle.com/docs/notebooks.

## Sources

- Paszke et al., "PyTorch: An Imperative Style, High-Performance Deep Learning Library" (NeurIPS 2019) — https://arxiv.org/abs/1912.01703 (checked 2026-10)
- Wijk et al., "RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts" (arXiv 2411.15114, Nov 2024) — https://arxiv.org/abs/2411.15114 (checked 2026-10)
- Stanford HAI, *AI Index Report 2026* (learning-penalties study, as summarised on the DLR market page) — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf (checked 2026-10)
- llm.c repository — https://github.com/karpathy/llm.c (checked 2026-10)
- Hendrycks and Gimpel, "Gaussian Error Linear Units (GELUs)" — https://arxiv.org/abs/1606.08415 ; Lin et al., "Focal Loss for Dense Object Detection" — https://arxiv.org/abs/1708.02002 (checked 2026-10)
- Google Colab FAQ — https://research.google.com/colaboratory/faq.html ; Kaggle notebook documentation — https://www.kaggle.com/docs/notebooks (checked 2026-10; Kaggle's weekly quota floats and is not published as a fixed number)

_Last reviewed: 2026-10_
