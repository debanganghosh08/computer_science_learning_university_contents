# MLE402 · Labs and projects

Use PyTorch (DDP, FSDP2, DTensor, Distributed Checkpoint), DeepSpeed for comparison, and Slurm or Kubernetes for scheduling. Most labs need 2–8 GPUs for a few hours; correctness work can run on CPU processes with the `gloo` backend. Record GPU type, interconnect, software versions and cost with every result. Budget your GPU hours before you start: every lab has a planned cost.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Estimates, MFU and collectives | 6ND estimates and a cost sheet in USD and INR; tokens/s and MFU for a small GPT on one GPU; ring all-reduce implemented with send/recv and compared with NCCL across 4 tensor sizes | Estimate vs measurement table; MFU calculation; correctness test; predicted vs measured all-reduce times | 7 h (2 weeks) |
| 2 · DDP and large batches | DDP on 2–4 GPUs; bucket-size sweep; linear LR scaling with and without warm-up; `DistributedSampler` epoch test | Scaling efficiency plot; warm-up comparison; exactly-once sampling proof | 4 h |
| 3 · Memory and mixed precision | Predict then measure peak memory; fp32 vs bf16 vs fp16; activation-checkpointing policies; audit an assistant's memory estimate line by line | Memory table (predicted vs measured); the audited AI estimate with corrections | 4 h |
| 4 · FSDP2 and ZeRO | Wrap a transformer with FSDP2; compare with DDP and DeepSpeed ZeRO stages 1–3 and CPU offload | Memory and throughput per configuration; a decision table | 5 h |
| 5 · Tensor and pipeline parallelism | A 2-way tensor-parallel MLP and attention block; a 4-stage pipeline with GPipe and 1F1B schedules; compose a 2D DeviceMesh | Output-equivalence tests; bubble fraction measured vs predicted | 6 h (2 weeks) |
| 6 · Distributed GBDT and sharded embeddings | XGBoost on Dask with 4 workers; a DLRM-style model with TorchRec table-wise vs row-wise sharding on Criteo samples | Speed-up curves; throughput by sharding plan | 4 h |
| 7 · Input pipelines and resumption | Convert data to WebDataset or MosaicML Streaming shards; fix a starved loader; resume mid-epoch | GPU idle time before/after; no-repeat/no-skip proof | 4 h |
| 8 · Checkpoints, failures and hangs | DCP save on 4 ranks and load on 2; async save; injected worker crash with elastic restart; a planted hang to diagnose | Resume proofs; recovery time; the hang's root cause from logs | 5 h |
| 9 · Slurm and Kubernetes | A multi-node `sbatch` script (course cluster or local Slurm container); a gang-scheduled job with Kueue or Volcano on `kind`; the same job on Ray Train | Job definitions; screenshots or logs of successful runs | 4 h |
| 10 · Profiling and MFU | PyTorch profiler and Nsight Systems traces; `torch.compile`, fused optimiser and FlashAttention; communication tuning | Top-3 time sinks before/after; MFU gain with each change attributed | 5 h |

## Projects

### P1 · A training plan you can defend (L1, ~6 hours)

**Real-world inspiration.** Before a large run, teams write a plan with a memory budget, a parallelism layout and a cost estimate; the Llama 3 paper and the Hugging Face Ultra-Scale Playbook show the reasoning behind such plans. Compute choices now include hyperscalers, GPU clouds (an 8×H100 machine at about $3.99 per GPU-hour on Lambda, October 2026) and, in India, subsidised IndiaAI capacity (38,000+ GPUs at ₹65 per hour, PIB, February 2026).

**What to build.** A 4–5 page training plan for a 1B-parameter decoder trained on 20B tokens with 2,048-token sequences, covering memory per GPU, parallelism layout, expected MFU, wall-clock time, checkpoint interval, expected failures and total cost on two compute options. Then validate the plan at small scale (for example 125M parameters on 1–2 GPUs).

**Acceptance criteria**
- The memory budget lists parameters, gradients, optimiser states and activations, with and without activation checkpointing.
- Time and cost estimates are within 2× of the measured small-scale run when scaled by your stated assumptions.
- The checkpoint interval is derived from an assumed failure rate and the cost of saving.
- Both compute options are compared in USD and INR, including storage and expected failed-run overhead.
- Every assumption is listed with its source or measurement.

**Stretch goals.** A sensitivity analysis (MFU ± 10 points, price ± 30%); a Chinchilla-style alternative plan with a smaller model trained on more tokens.

**What it proves to an employer.** You can plan compute before spending it, which managers of GPU budgets value highly.

### P2 · Fault-tolerant sharded training (L2, ~15 hours)

**Real-world inspiration.** Llama 3's 54-day snapshot saw 466 interruptions, yet effective training time stayed above 90% thanks to automation (Meta, 2024). PyTorch's Distributed Checkpoint supports parallel and asynchronous saves and resharding at load time.

**What to build.** Take a GPT-style model of 125M–350M parameters from single-GPU training to FSDP2 on 2–8 GPUs (or CPU processes for correctness, plus at least one real multi-GPU run), with bf16, activation checkpointing, sharded data loading with resumable state, asynchronous DCP checkpoints and elastic restarts.

**Acceptance criteria**
- The first 200 steps of the sharded run match the single-GPU loss curve within a documented tolerance (same global batch and seed).
- Killing a random worker mid-run triggers automatic recovery; total lost time is reported and is below one checkpoint interval plus restart time.
- A checkpoint saved on 4 ranks resumes on 2 ranks (and vice versa) with matching loss on the next 50 steps.
- Data resumption is exact: a test proves no sample is repeated or skipped across a restart.
- Peak memory, tokens/s and MFU are reported for DDP vs FSDP2 (with and without checkpointing).
- A README documents how to launch with `torchrun` and with Slurm or Kubernetes.

**Stretch goals.** Add 2-way tensor parallelism with a 2D DeviceMesh; compare against DeepSpeed ZeRO-3 on the same model.

**What it proves to an employer.** You can run training jobs that survive the failures that are normal at scale, and you can prove it.

### P3 · Scaling study and MFU optimisation (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** The modded-nanogpt speedrun turned GPT-2-small training into a public optimisation race: the main track's record fell from 45 minutes (May 2024 baseline) to under 40 seconds on 8×H100 (August 2026), through better optimisers, kernels and systems work. TorchTitan reported gains of 65% from 1D parallelism improvements and further gains from 2D and 3D layouts on H100 clusters (2024).

**What to build.** Choose one track. **LLM track:** train a GPT-2-small-class model to a fixed validation-loss target on FineWeb or another open corpus. **Recommender track:** train a DLRM-style model with sharded embeddings on Criteo data to a fixed log-loss target. In either track, run a scaling study from 1 to at least 8 GPUs (or the most you can access), compare at least three layouts, and optimise MFU or throughput step by step.

**Acceptance criteria**
- The target metric is reached; time-to-target and cost-to-target are reported for every configuration.
- Strong- and weak-scaling plots from 1 to N GPUs with efficiency percentages; at least one drop in efficiency is explained with profiler evidence.
- At least three layouts compared (for example DDP, FSDP2, FSDP2 + tensor parallelism; or table-wise vs row-wise vs hybrid embedding sharding).
- MFU (or examples/s for the recommender track) improves by at least 10 points (or 30%) over your own baseline, with an ablation attributing the gain to each change.
- Fault injection: one injected failure during the final run, with recovery documented.
- A training report (6–8 pages) a stranger could rerun: environment, commands, job files, layout, metrics, failures, cost and lessons.

**Stretch goals.** FP8 training on supported hardware with a loss comparison; context parallelism for long sequences; submit a reproducible result to a public leaderboard or speedrun if your hardware matches its rules.

**What it proves to an employer.** You can make expensive hardware productive and show your work, the core skill of ML infrastructure and research-engineering roles.

## Feeds into

- [MLE501 Frontier Seminar](../../year_5/MLE501_frontier_seminar_ml_research_engineering/README.md): scaling studies and reproductions at research standard.
- [MLE403 Ranking and Recommendation](../MLE403_ranking_and_recommendation_systems_at_scale/README.md): sharded embeddings and large-batch training for recommenders.
- [MLE404 Efficient Inference](../MLE404_efficient_inference_quantization_distillation/README.md): profiling and roofline thinking carry over to serving.
- [OV04 MLOps and ML Platform Engineering](../../../../04_overlaps/OV04_mlops_ml_platform/README.md): cluster scheduling and quotas for shared ML platforms.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): a scaling or efficiency study is a strong thesis topic.
