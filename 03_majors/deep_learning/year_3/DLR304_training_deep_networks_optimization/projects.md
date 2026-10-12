# DLR304 · Labs and projects

Every lab and project ships with a config file per run, logged metrics (loss, gradient norm, learning rate, throughput), at least 3 seeds for any comparison, and a write-up with confidence intervals. Comparisons are invalid without equal tuning budgets; say what budget each method received.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · LR and batch sweeps | Learning-rate range test; 6 batch sizes on CIFAR-10 and a small GPT; gradient-noise-scale estimate | Loss vs examples plots; critical batch size estimate with method | 4 h |
| 2 · Optimizers from scratch, then Muon vs AdamW | SGD+momentum, Adam, AdamW and Lion by hand; then a 20-trial random search for each of AdamW and Muon on a 10–30M GPT | Update equality with `torch.optim` (1e-6); tokens-to-target-loss with 95% CIs and the tuned hyperparameters for both | 10 h |
| 3 · Schedules and WSD branches | Cosine vs linear vs WSD; three cooldown branches from one WSD run | Final-loss table; plot showing a ranking flip between intermediate and final checkpoints | 4 h |
| 4 · Normalisation, logit control and μP | BatchNorm vs GroupNorm at small batch; pre- vs post-norm depth sweep; QK-norm and z-loss on an unstable run; width sweep under standard parameterisation and μP | Stability map (depth × learning rate); optimal learning rate vs width for both parameterisations | 8 h |
| 5 · Double descent and grokking | Epoch-wise double descent with 20% label noise; grokking on modular addition | Curves and the weight-decay ablation for grokking | 4 h |
| 6 · Precision and instabilities | fp16 without loss scaling (fail), with dynamic scaling (fix); simulated FP8 matmul error; a small-scale logit-growth instability | Reproductions with root cause and fix | 4 h |
| 7 · Training clinic | Diagnose 8 broken runs (prepared by classmates with one planted fault each) from logs only | Diagnosis, evidence and fix per run; accuracy is graded | 3 h |
| 8 · Seeds and audited agent experiments | 10-seed variance study; let an AI agent run 20 short experiments on a fixed budget, then re-test its top 3 claims | Minimum detectable effect; table classifying each agent claim as real, noise, unfair comparison or exploit | 5 h |
| 9 · Scaling-law fit | isoFLOP sweep with WSD cooldowns; fit L(N, D) | Fitted law, residuals, bootstrap CIs, a prediction for an unseen run | 6 h |
| 10 · DDP and FSDP | Kaggle 2× T4: DDP scaling efficiency; FSDP to fit a model that DDP cannot | Throughput table; predicted vs measured peak memory (within 15%) | 4 h |

## Projects

### P1 · Loss-curve clinic: a training-failure detector (L1, ~6 hours)

**Real-world inspiration.** Long training runs are watched by people and dashboards; a failure caught in minutes rather than hours saves real money. Google's Deep Learning Tuning Playbook and Karpathy's training recipe both stress reading curves before changing hyperparameters.

**What to build.** Reproduce 6 named failure modes on CIFAR-10 or a small GPT: learning rate too high, missing warmup with Adam, fp16 overflow, evaluation in training mode, unshuffled data, and duplicated data shards. Then write a detector that reads logged metrics (loss, gradient norm, learning rate, update-to-weight ratio, validation loss) and flags each failure with a reason.

**Acceptance criteria**
- Each failure has a signature plot and a one-paragraph mechanism.
- On 12 fresh runs (6 failures and 6 healthy, generated with new seeds and shuffled by a classmate), the detector labels at least 10 correctly, with no healthy run flagged as diverging.
- The detector runs on a JSONL or CSV log file and finishes in under 5 seconds.

**Compute budget.** ≤ 4 GPU-hours for all reproduction and test runs.

**Stretch goals.** Add an "anomalous batch" detector that points to the data batch behind a loss spike.

**What it proves to an employer.** You can watch over expensive runs and turn experience into tooling.

### P2 · An optimizer bake-off you can defend (L2, ~15 hours)

**Real-world inspiration.** Wen et al. (2025) showed that many claimed optimizer speed-ups shrink under equal tuning, and that rankings can flip as the learning rate decays. Meanwhile Muon was adopted in production pretraining (Kimi K2, 2025; DeepSeek-V4, 2026).

**What to build.** Compare AdamW, Muon (with AdamW for non-matrix parameters) and one other optimizer (SOAP, Lion or schedule-free AdamW) on a GPT of 20–60M parameters trained on FineWeb-Edu, at two model sizes and two token budgets.

**Acceptance criteria**
- Each optimizer receives the same hyperparameter search budget (stated in trials and GPU-hours), with the search space documented.
- Final validation loss at matched compute for each cell, over 3 seeds, with 95% confidence intervals; speed-up is reported as tokens-to-target-loss with an interval.
- A plot shows at least one case where intermediate-checkpoint rankings differ from final rankings, or the write-up shows that none occurred.
- Wall-clock overhead per step is measured (Muon's Newton–Schulz iterations are not free).
- Total compute ≤ 15 GPU-hours; every run is reproducible from its config.

**Stretch goals.** Add μP so hyperparameters transfer across the two sizes; test whether the speed-up trend matches the paper's "decreases with scale" finding.

**What it proves to an employer.** You can produce a result a pretraining team would trust, including a negative or modest one.

### P3 · A documented training speedrun (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** modded-nanogpt's community speedrun reduced the time to a fixed FineWeb validation loss on 8×H100 from 45 minutes to under 40 seconds through many small, documented changes, and nanochat runs a "time-to-GPT-2" leaderboard where some March 2026 entries came from AI-agent "autoresearch" rounds (repository READMEs, checked October 2026).

**What to build.** Pick a fixed target (for example, validation loss 3.6 on a fixed FineWeb-Edu slice for a ~30M-parameter model) and a fixed hardware setting (one free T4, or Kaggle's 2× T4). Start from a clean nanoGPT baseline and reduce wall-clock time to the target through changes such as Muon, schedule, architecture tweaks (RoPE, QK-norm, ReLU² or SwiGLU), `torch.compile`, mixed precision and data loading. You may use an AI agent to propose changes, but every change must survive your own ablation.

**Acceptance criteria**
- Final time-to-target is ≤ 70% of the baseline's, both measured over 3 seeds on the same hardware.
- A record table in the style of modded-nanogpt: each change, its isolated effect (with seed spread), and cumulative time.
- A negative-results table with at least 5 changes that did not help, including any agent proposals that failed re-testing.
- The final config reaches the target in every seed; no change touches the evaluation code or validation data.
- Compute ≤ 30 GPU-hours in total, with a log of every run.

**Stretch goals.** Port the final recipe to a 2× larger model and report whether the gains hold; submit an entry or write-up to an open speedrun community.

**What it proves to an employer.** You can make training measurably faster with disciplined ablations, which is the daily work of pretraining and research-engineering teams.

## Feeds into

- [DLR404 Efficient Deep Learning and GPU Programming](../../year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md): profiling, kernels and memory-efficient training build on Chapters 8 and 12.
- [DLR401 Large Language Models](../../year_4/DLR401_large_language_models_pretraining_fine_tuning/README.md): pretraining recipes, schedules and scaling laws at larger scale.
- [OV11 AI for Science and Research Engineering](../../../../04_overlaps/OV11_ai_for_science_research_engineering/README.md): training discipline for scientific models.
- [MLE402 Distributed Training and Large-Scale ML](../../../machine_learning_engineering/year_4/MLE402_distributed_training_and_large_scale_ml/README.md): tensor, pipeline and expert parallelism.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): fair-comparison methodology for reproductions.
