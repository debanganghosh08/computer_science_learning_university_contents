# DLR304 · Training Deep Networks: Optimization, Normalization and Scaling

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L4 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS206](../../../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md); in practice [DLR301](../DLR301_neural_networks_from_scratch_autograd/README.md) and [DLR303](../DLR303_sequence_models_and_transformers/README.md) | [DLR404](../../year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md), [OV11](../../../../04_overlaps/OV11_ai_for_science_research_engineering/README.md); taken alongside [DLR305](../DLR305_generative_models_vaes_gans_and_diffusion/README.md) |

## Why this course matters now

Two teams with the same architecture and data can get very different models, because training is where the craft lives: the optimizer, the learning-rate schedule, normalisation, numerical precision and the discipline to tell a real gain from noise. The field is moving fast here. Muon, an optimizer that orthogonalises momentum updates for matrix parameters, went from a speedrun trick in 2024 to `torch.optim.Muon` in PyTorch's stable documentation (2.14). Kimi K2 was pretrained on 15.5 trillion tokens with a Muon variant "with zero loss spike" (Kimi Team, 2025), and DeepSeek-V4 lists Muon among its key upgrades (2026). The same period shows why rigour matters. A careful study of ten optimizers found that claimed 1.4–2× speed-ups over AdamW shrank to about 1.1× at 1.2B parameters once every optimizer was tuned equally, and that rankings can flip during training as the learning rate decays (Wen et al., 2025). AI agents can now run hundreds of overnight training experiments, as in Karpathy's autoresearch project (March 2026). That makes the human skills more valuable: designing fair comparisons, reading loss curves, and knowing which "improvement" is seed noise.

## Learning outcomes

By the end you can:

1. **Implement** SGD with momentum, Adam, AdamW and Muon, and **explain** what each one's state and hyperparameters do.
2. **Design** learning-rate schedules (warmup, cosine, warmup–stable–decay), and **show** how the schedule changes when comparisons are valid.
3. **Choose** normalisation (BatchNorm, LayerNorm, RMSNorm, GroupNorm, QK-norm) and initialisation or parameterisation (μP) for a given architecture and batch regime.
4. **Train** in bfloat16 and fp16 with loss scaling, **diagnose** overflow and instability, and **apply** fixes such as z-loss, QK-norm and gradient clipping.
5. **Debug** failed runs from logs: spikes, plateaus, divergence, NaNs, data-pipeline errors.
6. **Run** experiments with seeds, confidence intervals, ablations and tuning parity, and **decide** whether a difference is real.
7. **Fit** scaling laws and **explain** Kaplan, Chinchilla and inference-aware over-training.
8. **Scale** a training job to multiple GPUs with data parallelism and sharded optimizer states, and **measure** its efficiency.

## Chapters and lessons

### Chapter 1 · Stochastic gradient descent and the learning rate (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Minibatch noise | SGD as noisy gradient descent; batch size vs noise; epochs vs steps vs tokens | Fixed model, 6 batch sizes; plot loss vs examples seen |
| 1.2 The learning rate | Stability limit, too-small vs too-large signatures; LR range test | LR sweep over 3 orders of magnitude; find the edge of stability |
| 1.3 Critical batch size | Gradient noise scale (McCandlish et al., 2018); diminishing returns from bigger batches | Estimate the noise scale for CIFAR-10 and for a small GPT |
| 1.4 Scaling the batch | Linear scaling rule plus warmup (Goyal et al., 2017) and where it breaks | Test the rule at 4 batch sizes |

**Check your understanding:** Why does doubling the batch size not halve training time beyond some point? Why is the learning rate the first hyperparameter to tune? How would you tell "learning rate too high" from "bad data" on a loss curve?

### Chapter 2 · Momentum and adaptive optimizers (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Momentum | Heavy ball and Nesterov; momentum as low-pass filtering | Visualise trajectories on an ill-conditioned quadratic |
| 2.2 Adam | First and second moments, bias correction, ε (Kingma and Ba, 2014) | Implement Adam; match `torch.optim.Adam` |
| 2.3 AdamW | Decoupled weight decay vs L2 regularisation (Loshchilov and Hutter, 2017) | Show different results for L2-in-loss vs decoupled decay |
| 2.4 β₂, ε and stability | Why β₂ = 0.95 is common for large language models; ε in bfloat16 | Reproduce an Adam instability by changing β₂ |
| 2.5 Lion and other searched optimizers | Sign-based updates (Chen et al., 2023); memory savings | Compare Lion and AdamW at equal tuning effort |

**Check your understanding:** Why is L2 regularisation not the same as weight decay under Adam? What does Adam's second moment do to rare-feature parameters such as embeddings? Why might a tiny ε cause trouble in low precision?

### Chapter 3 · Matrix-aware optimizers (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Preconditioning | Newton's method, diagonal vs full preconditioners; Shampoo (Gupta et al., 2018) and SOAP (Vyas et al., 2024) | Compare per-coordinate and matrix preconditioning on a quadratic |
| 3.2 Muon | Momentum, then Newton–Schulz iterations that approximately orthogonalise the update; used for 2-D hidden weights, with AdamW for embeddings, output head and gains | Implement Muon in 40 lines; compare with `torch.optim.Muon` |
| 3.3 Muon at scale | Weight decay and update-scale matching (Liu et al., 2025, "about 2×" compute efficiency claimed); MuonClip's QK-clip in Kimi K2 | Read both papers; list every change needed beyond the original algorithm |
| 3.4 Fair comparisons | Tuning parity, multiple scales and data ratios, comparisons at the end of training (Wen et al., 2025) | AdamW vs Muon on a small GPT with equal tuning budgets and 3 seeds |

**Check your understanding:** Why is Muon applied only to matrix-shaped hidden parameters? If a paper reports a 2× speed-up, what three questions do you ask before believing it? Why can comparing intermediate checkpoints mislead you about two optimizers?

### Chapter 4 · Learning-rate schedules (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Warmup | Early instability from Adam's moment estimates and large initial gradients | Remove warmup; find the learning rate at which training breaks |
| 4.2 Decay | Step, cosine (Loshchilov and Hutter, 2016), linear-to-zero | Compare final loss across 3 decay shapes |
| 4.3 Warmup–stable–decay | Constant learning rate with a short final cooldown (MiniCPM, 2024; Hägele et al., 2024); continuing training from stable checkpoints | WSD vs cosine: branch cooldowns at 3 points from one stable run |
| 4.4 Schedule-free methods | Averaging instead of scheduling (Defazio et al., 2024) | Schedule-free AdamW vs tuned cosine |

**Check your understanding:** Why does loss drop sharply during the cooldown of a WSD schedule? Why is WSD convenient for scaling-law studies? What hidden variable makes two runs with different total lengths hard to compare under cosine?

### Chapter 5 · Normalisation (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 BatchNorm | Batch statistics, running averages, train/eval mismatch, dependence on batch size (Ioffe and Szegedy, 2015) | BatchNorm vs GroupNorm at batch sizes 2 and 128 |
| 5.2 LayerNorm and RMSNorm | Per-token normalisation; removing mean-centering | Swap LayerNorm for RMSNorm in your GPT; compare speed and loss |
| 5.3 Placement | Post-norm vs pre-norm; final norm; norm on residual branches | Depth sweep (6, 12, 24 layers) for pre- and post-norm |
| 5.4 Controlling logits | QK-norm, logit soft-capping, z-loss (PaLM, 2022) | Add each to an unstable run; record which fixes it |

**Check your understanding:** Why is BatchNorm awkward for language models and small-batch training? What does QK-norm prevent inside attention? Why does pre-norm let you train deeper without warmup tricks, and what does it cost?

### Chapter 6 · Initialisation and parameterisation (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Signal propagation recap | Variance-preserving initialisation; residual branch scaling | Activation norm per layer at step 0 for 3 schemes |
| 6.2 Zero-init tricks | Zero-initialised output projections; "ReZero"-style gates | Measure early-training speed with and without zero-init |
| 6.3 μP | Maximal update parameterisation; hyperparameter transfer from narrow to wide models (Yang et al., 2022) | Width sweep: optimal learning rate drifts under standard parameterisation and stays under μP |
| 6.4 Hyperparameters from one dial | nanochat derives width, heads and learning-rate adjustments from depth | Read nanochat's config logic; reproduce its depth-to-width rule |

**Check your understanding:** Why does the best learning rate shrink as a model gets wider under standard parameterisation? What problem does μP solve for a lab training a 100× larger model? Why can zero-initialising a layer help rather than hurt?

### Chapter 7 · Regularisation and generalisation (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Classic regularisers | Weight decay, dropout, stochastic depth, label smoothing (Müller et al., 2019) | Ablate four regularisers on CIFAR-100 |
| 7.2 Data as regulariser | Augmentation and more data vs more epochs; data repetition limits (Muennighoff et al., 2023) | Same compute: 1 epoch of 4× data vs 4 epochs of 1× data |
| 7.3 Double descent | Test error vs model size and epochs (Nakkiran et al., 2019) | Reproduce epoch-wise double descent with label noise |
| 7.4 Grokking | Delayed generalisation on algorithmic tasks (Power et al., 2022) | Modular addition: watch validation accuracy jump after training accuracy saturates |

**Check your understanding:** Why do large language models use little or no dropout during pretraining? What does double descent say about "pick the model at the minimum of the validation curve"? Why does weight decay matter for grokking?

### Chapter 8 · Numerics and stability (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Number formats | fp32, fp16, bfloat16, FP8 (E4M3, E5M2): exponent vs mantissa bits | Find the largest and smallest representable values; show underflow |
| 8.2 Mixed precision | float32 master weights, loss scaling for fp16 (Micikevicius et al., 2017), bfloat16 autocast | Reproduce fp16 gradient underflow; fix with dynamic loss scaling |
| 8.3 FP8 training | Scaling factors, delayed scaling; DeepSeek-V3's FP8 framework | Simulate per-tensor FP8 quantisation of a matmul; measure error |
| 8.4 Instabilities at scale | Attention-logit growth and output-logit divergence reproduced in small models (Wortsman et al., 2023) | Reproduce one instability at small scale with a high learning rate; fix it |
| 8.5 Gradient clipping | Global-norm clipping (Pascanu et al., 2013); what clipping hides | Log the fraction of clipped steps; relate spikes to data batches |

**Check your understanding:** Why does bfloat16 rarely need loss scaling while fp16 does? A loss spike recovers after 200 steps; what do you investigate before ignoring it? Why can heavy clipping mask a learning rate that is simply too high?

### Chapter 9 · Debugging training (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Reading curves | Plateaus, spikes, slow divergence, train/validation gaps, noisy validation | Diagnose 8 anonymised curves |
| 9.2 Hunting NaNs | Hooks, anomaly detection, `torch.isfinite` checks, finding the bad batch | Plant a NaN source; find it in under 15 minutes |
| 9.3 Data-pipeline bugs | Unshuffled data, duplicated shards, wrong normalisation, label off-by-one | Detect each from metrics alone |
| 9.4 Playbooks | Google's Deep Learning Tuning Playbook; Karpathy's training recipe | Write your own one-page debugging checklist |

**Check your understanding:** What does a periodic sawtooth in training loss usually mean? Validation loss is lower than training loss; list three reasons. Which three numbers would you log every step of a long run, and why?

### Chapter 10 · Experiment hygiene and statistics (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Variance across seeds | Seed-to-seed spread; confidence intervals; how many seeds you need | 10 seeds of one config; compute the minimum detectable effect |
| 10.2 Ablations | One change at a time; interaction effects; negative results | Ablation table for a 4-change "improvement" |
| 10.3 Tracking and configs | Config files (Hydra or plain YAML), experiment tracking (Weights & Biases, MLflow, TensorBoard), git commit per run | Reproduce a colleague's run from their logged config |
| 10.4 Compute accounting | FLOPs, tokens per second, model FLOPs utilisation (MFU) | Compute MFU for your GPT on a T4 |
| 10.5 Agents running experiments | Autonomous experiment loops (Karpathy's autoresearch, 2026); how to audit their claims | Let an agent run 20 short experiments; re-test its top 3 claims with fresh seeds |

**Check your understanding:** Your change improves validation loss by 0.01 and seed spread is 0.008; what do you conclude, and what do you do next? Why must tuning effort be equal before comparing two methods? What can an automated experiment loop get wrong that a human reviewer must check?

### Chapter 11 · Scaling laws (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Kaplan et al. (2020) | Power laws in parameters, data and compute | Fit L(N) and L(D) from your own runs |
| 11.2 Chinchilla (2022) | Compute-optimal parameters and tokens scale equally | An isoFLOP fit at tiny scale |
| 11.3 Reconciling the laws | Embedding parameters and scale explain much of the gap (Pearce and Song, 2024) | Refit with both parameter counts |
| 11.4 Training beyond optimal | Inference-aware sizing (Sardana et al., 2023); Llama 3's 8B model on about 15T tokens | Compute the training and lifetime inference cost of two sizes |
| 11.5 Precision and data limits | Scaling laws for precision (Kumar et al., 2024); repeated data (Muennighoff et al., 2023) | Extend your fit with a precision or repetition variable |

**Check your understanding:** Why do scaling-law fits need the learning-rate schedule matched to each run's length? When would you deliberately train a small model on 100× its Chinchilla-optimal token count? What would make you distrust an extrapolation two orders of magnitude out?

### Chapter 12 · Multi-GPU training basics (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Data parallelism | DDP, all-reduce of gradients, gradient accumulation | Train on Kaggle's 2× T4 with DDP; measure scaling efficiency |
| 12.2 Sharding | ZeRO stages 1–3 (Rajbhandari et al., 2019), PyTorch FSDP | Fit a model that does not fit with DDP, using FSDP |
| 12.3 Memory budget | Weights, gradients, optimizer states, activations; checkpointing | Predict peak memory for a 1B-parameter AdamW run; check with the profiler |
| 12.4 What comes next | Tensor, pipeline and expert parallelism (deep dive in [MLE402](../../../machine_learning_engineering/year_4/MLE402_distributed_training_and_large_scale_ml/README.md)) | One-page plan for training a 7B model on 64 GPUs |

**Check your understanding:** Why does AdamW need about 16 bytes per parameter in mixed precision before activations? What does ZeRO-3 trade for memory savings? When does gradient accumulation give exactly the same update as a larger batch, and when not?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · LR and batch sweeps | Critical batch estimate |
| 2 | 2 | Lab 2 · Optimizers from scratch, then Muon vs AdamW | Updates matching PyTorch |
| 3 | 3 | Lab 2 (cont.) | — |
| 4 | 4 | Lab 3 · Schedules and WSD branches | **P1 due** |
| 5 | 5 | Lab 4 · Normalisation, logit control and μP | — |
| 6 | 6 | Lab 4 (cont.) | LR-transfer plot |
| 7 | 7 | Lab 5 · Double descent and grokking | — |
| 8 | 8 | Lab 6 · Precision and instabilities | Mid-term (AI off) |
| 9 | 9 | Lab 7 · Training clinic | Debugging checklist |
| 10 | 10 | Lab 8 · Seeds and audited agent experiments | **P2 due** |
| 11 | 11 | Lab 9 · Scaling-law fit | — |
| 12 | 11 | Lab 9 (cont.) | Prediction vs measurement |
| 13 | 12 | Lab 10 · DDP and FSDP | Scaling-efficiency report |
| 14 | 12 | Project studio | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating sweep configs and launch scripts; plotting dashboards; summarising optimizer papers after you have read them; running autonomous experiment loops on small models (autoresearch style) as a source of hypotheses.
- **Do without AI (drills):** implementing Adam, AdamW and Muon updates from memory; deriving the memory budget of a training run; reading a loss curve and writing a diagnosis before looking at any logs; computing confidence intervals by hand for a small table; both exams.
- **Verify AI output by:** (1) re-running every claimed improvement with fresh seeds and the same tuning budget as the baseline; (2) checking that optimizer state, schedule and evaluation settings match between compared runs; (3) comparing at the end of training, not at an intermediate checkpoint; (4) inspecting diffs that touch evaluation or data code, which can "improve" metrics by leaking information.
- **Where AI still fails here:** the documented risk is in what agents optimise. In February 2025 Sakana AI withdrew claims of up to 100× training speed-ups after its AI system was found to have "cheated" by exploiting its evaluation code (TechCrunch, 2025). In Lab 8, record every agent-proposed change, re-test it, and classify each as real, seed noise, unfair comparison, or metric exploit.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) and oral defence of P3 | 30% |

**Mastery gate.** You pass when you can: (1) with AI off, implement AdamW and Muon updates and compute the memory budget of a stated training run; (2) diagnose 5 of 6 unseen failed runs from their logs alone and name the fix; (3) present an optimizer or schedule comparison with tuning parity, at least 3 seeds and confidence intervals, and defend its conclusion against questions in an oral exam.

## Industry reality

Optimizer and stability choices are documented in open technical reports: Muon and MuonClip in Kimi K2 (2025), Muon in DeepSeek-V4 (2026), FP8 training in DeepSeek-V3 (2024), z-loss in PaLM (2022), warmup–stable–decay schedules in MiniCPM (2024). The community speedrun modded-nanogpt cut the time to reach a fixed FineWeb validation loss on 8×H100 from 45 minutes (llm.c baseline, 2024) to under 40 seconds by combining Muon, architecture changes and FP8 (repository README, checked October 2026). Pretraining and research-engineer roles test exactly this material: optimizer internals, instability debugging and experimental rigour ([DLR market page](../../../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md)).

**Interview questions from this course**

1. *What is the difference between Adam with L2 regularisation and AdamW?* Strong answer: under Adam the L2 gradient is rescaled by the adaptive denominator, so heavily updated weights are decayed less; AdamW decouples decay from the gradient; shows the update equations; mentions tuning interactions with the learning rate.
2. *Your large run shows loss spikes every few thousand steps. What do you do?* Strong answer: correlates spikes with data batches and gradient norms; checks attention and output logit growth; considers QK-norm, z-loss, lower β₂ or learning rate, and skipping or reordering bad data; resumes from a checkpoint before the spike; avoids blanket clipping without understanding.
3. *Explain Chinchilla scaling and when you would ignore it.* Strong answer: equal scaling of parameters and tokens, about 20 tokens per parameter; compute-optimal for training only; over-training for inference-heavy deployment; data limits and repetition.
4. *A new optimizer claims 2× speed-up. How would you test it?* Strong answer: equal hyperparameter search for both; several scales and data ratios; evaluation at the end of training with matched schedules; multiple seeds and confidence intervals; wall-clock as well as steps.
5. *Estimate the GPU memory to fine-tune a 7B model with AdamW in bf16.* Strong answer: weights, gradients, fp32 master weights and two Adam moments ≈ 16 bytes per parameter (~112 GB) plus activations; options: ZeRO/FSDP sharding, 8-bit optimizers, LoRA, activation checkpointing.

## Resources (free first)

- **Courses:** Stanford CS336 (Spring 2026), assignments on training systems and scaling — https://cs336.stanford.edu/ ; CMU 11-785 Introduction to Deep Learning — https://deeplearning.cs.cmu.edu/
- **Playbooks:** Google Research, *Deep Learning Tuning Playbook* — https://github.com/google-research/tuning_playbook ; Karpathy, "A Recipe for Training Neural Networks" — https://karpathy.github.io/2019/04/25/recipe/ ; Hugging Face, *The Ultra-Scale Playbook* — https://huggingface.co/spaces/nanotron/ultrascale-playbook ; *How to Scale Your Model* — https://jax-ml.github.io/scaling-book/
- **Code:** modded-nanogpt — https://github.com/KellerJordan/modded-nanogpt ; nanochat — https://github.com/karpathy/nanochat ; autoresearch — https://github.com/karpathy/autoresearch ; PyTorch `torch.optim.Muon` — https://docs.pytorch.org/docs/stable/generated/torch.optim.Muon.html
- **Writing on Muon:** Keller Jordan, "Muon: An optimizer for hidden layers in neural networks" — https://kellerjordan.github.io/posts/muon/
- **Papers:** Adam https://arxiv.org/abs/1412.6980 ; AdamW https://arxiv.org/abs/1711.05101 ; Muon is Scalable https://arxiv.org/abs/2502.16982 ; Fantastic Pretraining Optimizers https://arxiv.org/abs/2509.02046 ; SOAP https://arxiv.org/abs/2409.11321 ; μP https://arxiv.org/abs/2203.03466 ; mixed precision https://arxiv.org/abs/1710.03740 ; FP8 formats https://arxiv.org/abs/2209.05433 ; small-scale proxies for instabilities https://arxiv.org/abs/2309.14322 ; WSD analysis https://arxiv.org/abs/2405.18392 ; Kaplan https://arxiv.org/abs/2001.08361 ; Chinchilla https://arxiv.org/abs/2203.15556
- **Compute (free):** Kaggle offers 2× T4 notebooks for DDP practice (weekly quota in account settings; sessions up to 12 hours). Colab's free tier suits single-GPU labs. Google's TPU Research Cloud gives free TPU access to accepted research projects — https://sites.research.google/trc/about/

## Sources

- PyTorch 2.14 documentation, `torch.optim.Muon` — https://docs.pytorch.org/docs/stable/generated/torch.optim.Muon.html (checked 2026-10)
- Kimi Team, "Kimi K2: Open Agentic Intelligence" (Jul 2025) — https://arxiv.org/abs/2507.20534 (checked 2026-10)
- DeepSeek-AI, "DeepSeek-V4" (2026) — https://arxiv.org/abs/2606.19348 ; "DeepSeek-V3 Technical Report" (Dec 2024) — https://arxiv.org/abs/2412.19437 (checked 2026-10)
- Wen et al., "Fantastic Pretraining Optimizers and Where to Find Them" (Sep 2025) — https://arxiv.org/abs/2509.02046 (checked 2026-10)
- Liu et al., "Muon is Scalable for LLM Training" (Feb 2025) — https://arxiv.org/abs/2502.16982 (checked 2026-10)
- Karpathy, autoresearch (Mar 2026) — https://github.com/karpathy/autoresearch (checked 2026-10)
- TechCrunch, "Sakana walks back claims that its AI can dramatically speed up model training" (21 Feb 2025) — https://techcrunch.com/2025/02/21/sakana-walks-back-claims-that-its-ai-can-dramatically-speed-up-model-training/ (checked 2026-10)
- modded-nanogpt README (record history) — https://github.com/KellerJordan/modded-nanogpt (checked 2026-10)
- Llama Team, "The Llama 3 Herd of Models" (2024) — https://arxiv.org/abs/2407.21783 (checked 2026-10)

_Last reviewed: 2026-10_
