# MLE402 · Distributed Training and Large-Scale ML

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [MLE302](../../year_3/MLE302_machine_learning_system_design/README.md) (and comfort with PyTorch from [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md)) | [MLE501](../../year_5/MLE501_frontier_seminar_ml_research_engineering/README.md), [MLE403](../MLE403_ranking_and_recommendation_systems_at_scale/README.md), [OV04](../../../../04_overlaps/OV04_mlops_ml_platform/README.md), [DLR404](../../../deep_learning/year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md) |

## Why this course matters now

Training is now a distributed-systems problem. Meta trained Llama 3 405B on up to 16,384 H100 GPUs using four kinds of parallelism at once; during a 54-day snapshot the job was interrupted 466 times, 419 of them unexpectedly, with about 78% of unexpected interruptions attributed to confirmed or suspected hardware issues, yet the team kept effective training time above 90% (Llama 3 paper, 2024). Compute is also expensive and increasingly available to students: an 8×H100 machine rents for about $3.99 per GPU-hour on Lambda (October 2026), and India's IndiaAI Mission reported 38,000+ GPUs at a subsidised ₹65 per hour (PIB, February 2026). Coding assistants generate FSDP or DeepSpeed configs on request. Knowing why a run achieves 25% model FLOPs utilisation instead of 45%, which parallelism layout fits a model and a network, why a job hangs at step 9,000, and whether a checkpoint can be resumed on a different number of GPUs is what separates an engineer who wastes a cluster from one who uses it well.

## Learning outcomes

By the end you can:

1. **Estimate** the compute (≈ 6 × parameters × tokens for dense transformers), memory, communication volume, time and cost of a training run before launching it.
2. **Explain** collective operations (all-reduce, all-gather, reduce-scatter, all-to-all) and **compute** their cost on a given interconnect.
3. **Implement** data parallelism with gradient bucketing and overlap, and **scale** batch size with learning-rate warm-up.
4. **Account** for every byte of GPU memory and **reduce** it with mixed precision, activation checkpointing and sharding (ZeRO, FSDP2).
5. **Apply** tensor, pipeline, sequence, context and expert parallelism, and **choose** a multi-dimensional layout for a model and cluster.
6. **Train** large classic and recommender models: distributed gradient boosting and sharded embedding tables.
7. **Build** input pipelines and checkpointing that survive failures and resume deterministically, including on a different world size.
8. **Run** jobs on Slurm and Kubernetes (Kueue or Volcano) and **debug** hangs, stragglers and NCCL errors.
9. **Profile** and **improve** model FLOPs utilisation (MFU), and **report** cost per run.

## Chapters and lessons

### Chapter 1 · Measuring scale (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 FLOPs and time | 6ND for dense transformers; forward vs backward cost; tokens per second | Estimate training time for a 1B-parameter model on 20B tokens on 8 GPUs |
| 1.2 Utilisation | Model FLOPs utilisation vs hardware FLOPs utilisation (PaLM paper definitions) | Measure MFU of a small GPT on one GPU |
| 1.3 The roofline | Compute-bound vs memory-bound vs overhead-bound (Horace He, "Making Deep Learning Go Brrrr") | Classify 5 operations by arithmetic intensity |
| 1.4 Scaling laws and budgets | Compute-optimal training: parameters and tokens scale together (Chinchilla, 2022) | Choose model size and token count for a fixed GPU-hour budget |
| 1.5 Cost | GPU-hour prices (cloud, IndiaAI), utilisation, failed runs, storage | Cost sheet in dollars and rupees for your plan |

**Check your understanding:** Why is backward roughly twice the cost of forward? Why does an MFU of 40% count as good? Why can a "cheaper" GPU make a run more expensive?

### Chapter 2 · Hardware and collectives (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Inside a node | HBM capacity and bandwidth, NVLink/NVSwitch, PCIe | Compute how long it takes to move 10 GB over NVLink vs PCIe |
| 2.2 Between nodes | InfiniBand and RoCE, topology, oversubscription | Read a cluster spec sheet and predict the bottleneck |
| 2.3 Collectives | All-reduce, all-gather, reduce-scatter, broadcast, all-to-all; ring and tree algorithms | Implement ring all-reduce with `torch.distributed` send/recv; verify against NCCL |
| 2.4 Cost models | Ring all-reduce moves ≈ 2(n−1)/n × the data; latency vs bandwidth terms | Predict and measure all-reduce time for 4 tensor sizes |

**Check your understanding:** Why is all-reduce often implemented as reduce-scatter followed by all-gather? Why do small messages scale badly? What happens to a ring when one link is slow?

### Chapter 3 · Data parallelism (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 DDP | Replicated model, gradient all-reduce, bucketing, overlap with backward | Train with DDP on 2–4 GPUs (or CPU processes); measure scaling |
| 3.2 Launching | `torchrun`, ranks, rendezvous, environment variables, elastic ranges | Launch on 2 nodes (or simulated nodes) with `torchrun` |
| 3.3 Large batches | Linear scaling rule and warm-up (Goyal et al., 2017); gradient accumulation | Reproduce warm-up's effect on a large-batch run |
| 3.4 Determinism and sampling | `DistributedSampler`, epoch seeding, uneven last batches | Prove every sample is seen exactly once per epoch |

**Check your understanding:** Why does DDP overlap communication with the backward pass? When does gradient accumulation equal a bigger batch, and when not? What breaks if each rank shuffles with the same seed?

### Chapter 4 · Where memory goes (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The memory budget | Parameters, gradients, optimiser states (16 bytes per parameter for mixed-precision Adam, per the ZeRO paper), activations, fragmentation | Predict then measure peak memory for 3 model sizes |
| 4.2 Mixed precision | FP16 with loss scaling (Micikevicius et al., 2017), bf16, FP8 formats E4M3/E5M2 (2022) | Train in fp32, bf16 and fp16; compare speed, memory, loss |
| 4.3 Activation checkpointing | Recompute instead of store (Chen et al., 2016: 48 GB → 7 GB for ~30% more runtime on their example) | Find the checkpointing policy that fits a model on one GPU |
| 4.4 Memory profiling | PyTorch memory snapshots and the profiler | Find and fix a memory leak from storing loss tensors |

**Check your understanding:** Why does Adam triple the memory of plain SGD? Why is bf16 easier to train with than fp16? Which layers are best to checkpoint?

### Chapter 5 · Sharded data parallelism (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 ZeRO | Stage 1 shards optimiser states, stage 2 adds gradients, stage 3 adds parameters (Rajbhandari et al., 2019) | Compute per-GPU memory for each stage for a 7B model on 8 GPUs |
| 5.2 FSDP2 | `fully_shard`, DTensor per-parameter sharding, prefetching, reshard-after-forward | Wrap a transformer with FSDP2; compare memory and speed with DDP |
| 5.3 DeepSpeed | ZeRO configs, offload to CPU and NVMe (ZeRO-Infinity) | Fit a model that does not fit with DDP; measure the slowdown of offload |
| 5.4 Choosing | DDP vs FSDP vs ZeRO stages vs offload by model size and network | Decision table for 4 scenarios |

**Check your understanding:** What extra communication does ZeRO-3 add, and when is it worth it? Why does offloading help memory but hurt throughput? Why shard per parameter rather than per flat buffer?

### Chapter 6 · Model parallelism (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Tensor parallelism | Column- and row-parallel linear layers, attention heads across GPUs (Megatron-LM, 2019) | Implement a 2-way tensor-parallel MLP; check outputs match |
| 6.2 Pipeline parallelism | Micro-batches and bubbles (GPipe), 1F1B (PipeDream), interleaved schedules (Narayanan et al., 2021) | Compute bubble fraction for 4 stages and 8, 16, 32 micro-batches |
| 6.3 Sequence and context parallelism | Sequence parallelism for activations (Korthikanti et al., 2022); Ring Attention; DeepSpeed-Ulysses | Explain which one you need for 128K-token sequences |
| 6.4 Expert parallelism | Mixture-of-experts routing, all-to-all traffic, load balancing | Profile all-to-all cost in a toy MoE layer |
| 6.5 Composing dimensions | DeviceMesh; 2D/3D/4D layouts; TorchTitan's measured gains; Llama 3's [TP, CP, PP, DP] ordering | Choose a layout for a 70B model on 64 GPUs across 8 nodes; justify it |

**Check your understanding:** Why is tensor parallelism usually kept inside a node? What shrinks the pipeline bubble, and what does it cost? Why does Llama 3 place tensor parallelism innermost?

### Chapter 7 · Large-scale classic and recommender training (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Distributed gradient boosting | Histogram aggregation across workers in XGBoost and LightGBM (Dask, Spark, Ray) | Train XGBoost on Dask across 4 workers; measure speed-up |
| 7.2 Embedding tables | Billions of rows; model-parallel embeddings with data-parallel MLPs (DLRM, 2019) | Compute embedding memory for 100 M users × 128 dims |
| 7.3 Sharding embeddings | Table-wise, row-wise and column-wise sharding; TorchRec | Shard a DLRM-style model 3 ways; compare throughput |
| 7.4 When not to distribute | Sampling, smaller models, single big machines | Show a single-node job beating a badly configured cluster |

**Check your understanding:** Why are recommendation models often memory-bound in embeddings, not compute-bound in MLPs? Why can row-wise sharding create hot spots? When is one large machine better than a cluster?

### Chapter 8 · Input pipelines (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Starvation | Measuring GPU idle time due to data loading | Profile a job with a slow loader; fix it |
| 8.2 Sharded formats | WebDataset tar shards, MosaicML Streaming, pre-tokenised arrays | Convert a dataset to shards; compare throughput |
| 8.3 Deterministic resumption | Saving loader state; resuming mid-epoch without repeating data | Kill and resume; prove no sample is repeated or skipped |
| 8.4 Remote storage | Object storage throughput, caching, prefetching | Measure throughput from local disk vs object storage |

**Check your understanding:** How do you tell a data-loading bottleneck from a compute bottleneck? Why does resuming mid-epoch need loader state? Why shard data into many files?

### Chapter 9 · Checkpointing and fault tolerance (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Distributed checkpoints | PyTorch Distributed Checkpoint (DCP): parallel save, load-time resharding, async save | Save on 4 ranks, resume on 2 |
| 9.2 Failure at scale | Llama 3's interruption statistics; mean time between failures as cluster size grows | Compute expected interruptions for 1,000 GPUs over 30 days from a given per-GPU failure rate |
| 9.3 Elastic training | `torchrun --max-restarts`, elastic node ranges, health checks | Inject a worker crash; recover automatically |
| 9.4 Hangs and stragglers | NCCL timeouts, debugging hangs, straggler detection, silent data corruption checks | Diagnose a planted hang from logs |
| 9.5 Checkpoint frequency | Cost of saving vs cost of lost work | Choose an interval that minimises expected lost time |

**Check your understanding:** Why does failure become routine at 10,000 GPUs? Why must checkpoints be loadable on a different world size? How do you tell a hang from a slow step?

### Chapter 10 · Clusters and scheduling (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Slurm | `sbatch`, `srun`, partitions, generic resources (GPUs), job arrays | Submit a multi-node job script (on a course cluster or a local Slurm container) |
| 10.2 Kubernetes for training | Gang scheduling with Kueue or Volcano, quotas, preemption | Run a 2-worker job with gang scheduling on `kind` |
| 10.3 Ray Train | Distributed training as a library; fault tolerance; integration with tuning | Port your DDP job to Ray Train |
| 10.4 Shared clusters | Fair share, priorities, spot capacity, the IndiaAI compute portal | Write a usage policy for a 64-GPU university cluster |

**Check your understanding:** Why does a distributed job need gang scheduling? What does preemption mean for checkpoint frequency? When is Slurm a better fit than Kubernetes?

### Chapter 11 · Performance engineering and cost (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Profiling | PyTorch profiler and Nsight Systems traces; reading kernel timelines | Find the top 3 time sinks in a training step |
| 11.2 Compilation and kernels | `torch.compile` for training, fused optimisers, FlashAttention | Measure the speed-up from compile and fused attention |
| 11.3 Communication tuning | Bucket sizes, overlap, NCCL settings, hierarchical collectives | Raise MFU by 10 points on a fixed setup |
| 11.4 Cost reporting | Cost per run, cost per point of metric, idle cost, carbon | A one-page cost report for your P3 run |

**Check your understanding:** Why might `torch.compile` speed up one model and not another? What is the cheapest way to raise MFU on a communication-bound job? Why report cost per useful run, not per hour?

### Chapter 12 · Scaling studies (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Weak and strong scaling | Fixed total vs fixed per-GPU work; efficiency curves | Strong- and weak-scaling plots from 1 to 8 GPUs |
| 12.2 Reading playbooks | The Hugging Face Ultra-Scale Playbook (4,100+ distributed experiments); Google DeepMind's "How to Scale Your Model" | Reproduce one playbook result at small scale |
| 12.3 Writing a training report | Setup, layout, MFU, failures, cost, lessons | Write P3's report |
| 12.4 Planning the next scale-up | Turning measured scaling curves into a plan for 10× more compute; the risks of extrapolating | Write a one-page scale-up proposal with a cost range |

**Check your understanding:** Why does strong scaling eventually stop helping? What does a sudden efficiency drop at 2 nodes suggest? What must a training report contain for someone else to rerun it?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Estimates and MFU | — |
| 2 | 2 | Lab 1 (continued): ring all-reduce | — |
| 3 | 3 | Lab 2 · DDP and large batches | **P1 due** |
| 4 | 4 | Lab 3 · Memory and mixed precision | — |
| 5 | 5 | Lab 4 · FSDP2 and ZeRO | — |
| 6 | 6 | Lab 5 · Tensor and pipeline parallelism | — |
| 7 | 6 | Lab 5 (continued): layouts | Mid-term (AI off) |
| 8 | 7 | Lab 6 · Distributed GBDT and sharded embeddings | **P2 due** |
| 9 | 8 | Lab 7 · Input pipelines and resumption | — |
| 10 | 9 | Lab 8 · Checkpoints, failures and hangs | — |
| 11 | 10 | Lab 9 · Slurm and Kubernetes | — |
| 12 | 11 | Lab 10 · Profiling and MFU | — |
| 13 | 12 | Scaling study (P3) | — |
| 14 | 12 | Training report (P3) | **P3 due** |
| 15 | Review | P3 presentation | Final exam (AI off) |

Labs need 2–8 GPUs for a few hours each. Where a university cluster is not available, use cloud credits, the IndiaAI compute portal (where eligible) or free notebook GPUs, and simulate multi-GPU runs with several CPU processes using the `gloo` backend for correctness work.

## Working with AI in this course

- **Use AI for:** first drafts of launch scripts, FSDP or DeepSpeed configs and Slurm job files; explaining NCCL error messages and profiler traces; converting single-GPU code to DDP; summarising parallelism papers.
- **Do without AI (drills):** the memory budget for a model and optimiser; collective communication costs; bubble fractions; choosing a parallelism layout; expected failures and checkpoint intervals. The mid-term and final are AI-off.
- **Verify AI output by:** checking that sharded and unsharded runs produce matching losses for the first steps; measuring memory and MFU instead of trusting claims; resuming from a checkpoint on a different world size; running the planted-failure tests; comparing config keys with the current documentation (FSDP2 replaced FSDP1's API; DeepSpeed and Megatron-Core options change between releases).
- **Where AI still fails here:** assistants mix FSDP1 and FSDP2 APIs; generate configs that are valid but slow (no overlap, wrong bucket sizes, checkpointing everything); forget `DistributedSampler.set_epoch`; and misstate memory arithmetic (counting fp16 weights but forgetting fp32 master weights and optimiser states). Lab 3 asks you to audit an assistant's memory estimate line by line.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 45% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 20% |

**Mastery gate.** You pass when you can: (1) without AI, given a model size, sequence length, cluster and budget, produce a memory plan, a parallelism layout and a time-and-cost estimate within 2× of a measured run; (2) take a single-GPU training script to a multi-GPU sharded run that matches the single-GPU loss curve, survives a killed worker, and resumes on a different number of GPUs; (3) raise the MFU of a provided baseline by at least 10 points and explain each change.

## Industry reality

Distributed training is run by ML engineers, research engineers and ML infrastructure teams at AI labs, large product companies and cloud providers. Public reports describe the practice: Llama 3's 4D parallelism and failure statistics (Meta, 2024); TorchTitan's measured gains from composing parallelism (PyTorch team, 2024); Megatron-LM training a 1-trillion-parameter model at 502 PFLOP/s on 3,072 GPUs (Narayanan et al., 2021). Recommendation companies train huge embedding models (DLRM). In India, the IndiaAI Mission's subsidised compute (38,000+ GPUs reported in March 2026, with a ₹10,372 crore outlay) is widening access for start-ups and researchers.

**Interview questions from this course**

1. *A 7B model with Adam does not fit on 8 × 80 GB GPUs with DDP. What do you do?* Strong answer: memory arithmetic (weights, gradients, optimiser states, activations); FSDP/ZeRO-3; activation checkpointing; bf16; offload as last resort; the communication cost of each.
2. *Explain tensor vs pipeline vs data parallelism and when to combine them.* Strong answer: what each splits; communication patterns and volumes; TP within a node; PP across nodes with micro-batches; DP or FSDP outermost; context parallelism for long sequences.
3. *Your 64-GPU job is 40% slower than expected. How do you investigate?* Strong answer: profile one step; check data loading, communication overlap, stragglers, network topology, batch size per GPU; measure MFU; compare with a single-node baseline.
4. *How do you make training robust to failures?* Strong answer: sharded async checkpoints, resharding on load, elastic restarts, deterministic data resumption, health checks, hang detection, choosing checkpoint frequency from failure rates.
5. *How would you estimate the cost of training a model?* Strong answer: 6ND FLOPs, achievable MFU, GPU count and price, overhead for failures and evaluations, storage and egress; a range, not a point.

## Resources (free first)

- **Playbooks and books:** Hugging Face, *The Ultra-Scale Playbook* — https://huggingface.co/spaces/nanotron/ultrascale-playbook ; Google DeepMind, *How to Scale Your Model* — https://jax-ml.github.io/scaling-book/ ; Horace He, "Making Deep Learning Go Brrrr From First Principles" — https://horace.io/brrr_intro.html
- **Courses:** Stanford CS336 Language Modeling from Scratch — https://cs336.stanford.edu/ ; CMU Deep Learning Systems — https://dlsyscourse.org/ ; CMU Machine Learning Systems — https://mlsyscourse.org/
- **PyTorch:** DDP notes — https://docs.pytorch.org/docs/stable/notes/ddp.html ; FSDP2 `fully_shard` — https://docs.pytorch.org/docs/stable/distributed.fsdp.fully_shard.html ; DTensor — https://docs.pytorch.org/docs/stable/distributed.tensor.html ; `torchrun` — https://docs.pytorch.org/docs/stable/elastic/run.html ; Distributed Checkpoint — https://docs.pytorch.org/docs/stable/distributed.checkpoint.html ; profiler — https://docs.pytorch.org/docs/stable/profiler.html ; TorchTitan — https://github.com/pytorch/torchtitan ; TorchRec — https://github.com/pytorch/torchrec
- **Other frameworks:** DeepSpeed ZeRO tutorial — https://www.deepspeed.ai/tutorials/zero/ ; Megatron-LM / Megatron-Core — https://github.com/NVIDIA/Megatron-LM ; Hugging Face Accelerate — https://huggingface.co/docs/accelerate/index ; Ray Train — https://docs.ray.io/en/latest/train/train.html ; XGBoost with Dask — https://xgboost.readthedocs.io/en/stable/tutorials/dask.html
- **Infrastructure:** NCCL — https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/index.html ; Nsight Systems — https://docs.nvidia.com/nsight-systems/ ; Slurm — https://slurm.schedmd.com/documentation.html ; Kueue — https://kueue.sigs.k8s.io/ ; Volcano — https://volcano.sh/en/ ; WebDataset — https://github.com/webdataset/webdataset ; MosaicML Streaming — https://docs.mosaicml.com/projects/streaming/en/stable/ ; IndiaAI compute portal — https://compute.indiaai.gov.in
- **Code to read:** nanoGPT — https://github.com/karpathy/nanoGPT ; modded-nanogpt — https://github.com/KellerJordan/modded-nanogpt

## Sources

- Llama Team (Meta), "The Llama 3 Herd of Models" (arXiv 2407.21783, 2024): up to 16K H100 GPUs; 4D parallelism ordered [TP, CP, PP, DP]; 466 interruptions in a 54-day snapshot, 419 unexpected, ~78% hardware-related; >90% effective training time; BF16 MFU 38–43% — https://arxiv.org/abs/2407.21783 (checked 2026-10)
- Lambda pricing (H100 SXM 8× at $3.99/GPU-hr, read 12 Oct 2026) — https://lambda.ai/pricing ; PIB backgrounder on IndiaAI (17 Feb 2026: 38,000+ GPUs at ₹65 per hour) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2229397 ; PIB Lok Sabha reply (25 Mar 2026) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2245069 (checked 2026-10)
- Chowdhery et al., PaLM (MFU definition; 46.2% MFU) — https://arxiv.org/abs/2204.02311 ; Hoffmann et al., Chinchilla — https://arxiv.org/abs/2203.15556 ; Goyal et al., large-minibatch SGD — https://arxiv.org/abs/1706.02677 (checked 2026-10)
- Rajbhandari et al., ZeRO — https://arxiv.org/abs/1910.02054 ; ZeRO-Infinity — https://arxiv.org/abs/2104.07857 ; Shoeybi et al., Megatron-LM — https://arxiv.org/abs/1909.08053 ; Narayanan et al., PTD-P (502 PFLOP/s on 3,072 GPUs) — https://arxiv.org/abs/2104.04473 ; Huang et al., GPipe — https://arxiv.org/abs/1811.06965 ; Harlap et al., PipeDream — https://arxiv.org/abs/1806.03377 ; Korthikanti et al. — https://arxiv.org/abs/2205.05198 ; Jacobs et al., DeepSpeed-Ulysses — https://arxiv.org/abs/2309.14509 ; Liu et al., Ring Attention — https://arxiv.org/abs/2310.01889 ; Liang et al., TorchTitan — https://arxiv.org/abs/2410.06511 (checked 2026-10)
- Micikevicius et al., mixed precision — https://arxiv.org/abs/1710.03740 ; Micikevicius et al., FP8 formats — https://arxiv.org/abs/2209.05433 ; Kalamkar et al., bfloat16 — https://arxiv.org/abs/1905.12322 ; Chen et al., gradient checkpointing — https://arxiv.org/abs/1604.06174 ; Naumov et al., DLRM — https://arxiv.org/abs/1906.00091 (checked 2026-10)
- Versions on PyPI (checked 2026-10): PyTorch 2.14.1, DeepSpeed 0.19.7, Megatron-Core 0.19.2, TorchTitan 0.3.0, Ray 2.59.0, Accelerate 1.15.0

_Last reviewed: 2026-10_
