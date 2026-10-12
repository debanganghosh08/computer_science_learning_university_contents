# CLD404 · Labs and projects

GPU time is the expensive part of this course, so every GPU lab is scripted to start, run and shut itself down, with a hard timer and a budget action. Use small open models (1–8B parameters, quantised where possible), free notebook GPUs or TPUs where they suffice, and CPU mode for functional tests. Eligible students can apply for IndiaAI subsidised compute. The sizing and cost labs are done without AI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Sizing and the roofline (no AI) | Estimate FLOPs, memory and GPU-days for 7B and 70B training runs; KV-cache memory for a chat service; place kernels on a roofline | Worked estimates with every assumption stated | 4 h |
| 2 · Accelerator comparison | Build a datasheet table (HBM, bandwidth, FP8/BF16 FLOPs, interconnect) for five accelerators; run a small JAX job on a TPU runtime and read the profile | Table with sources, profile notes | 4 h |
| 3 · Capacity options | For "32 GPUs for 72 hours next week", compare on-demand, capacity blocks, DWS flex-start or calendar mode, Spot and IndiaAI options on price, lead time and risk | Options memo with a recommendation | 3 h |
| 4 · Collectives | Run `nccl-tests` all-reduce across GPUs (or a simulator if unavailable); fit the latency/bandwidth model; compare packed and spread placement | Benchmark data, fitted model, placement comparison | 4 h |
| 5 · Data loading and checkpoints | Profile a training loop starved by its data loader; fix with sharding and prefetch; measure checkpoint stall and add async checkpointing | GPU idle time before/after; checkpoint stall times | 5 h |
| 6 · Schedulers | Two-node job on Slurm (HyperPod, Cluster Toolkit or local); Kueue with quotas and preemption on a Kubernetes cluster with GPU or simulated devices | Job logs, queue behaviour under contention | 5 h |
| 7 · Failure and auto-resume | Inject a node failure into a multi-GPU job; detect, replace and resume from checkpoint automatically | Goodput calculation and timeline | 4 h |
| 8 · vLLM serving and SLOs | Serve an open model with vLLM; load-test with a realistic prompt-length distribution; measure TTFT, inter-token latency and throughput at three concurrency levels | Results table and SLO proposal | 5 h |
| 9 · Inference gateway and autoscaling | Put two replicas behind an inference-aware gateway (Gateway API Inference Extension or llm-d); autoscale on queue depth; measure prefix-cache hit rate | Routing and scaling evidence | 5 h |
| 10 · Managed platforms and quotas | Call the same model family on two managed platforms through private endpoints; hit and handle quota limits; log every request | Feature and latency comparison, quota-handling code | 4 h |

## Projects

### P1 · A capacity and sizing plan for an Indic-language model (L1, ~6 hours)

**Real-world inspiration:** the IndiaAI Mission funds foundation-model work and offers subsidised GPUs and TPUs ([PIB, February 2026](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc2026210784401.pdf)); Meta's Llama 3 paper documents the compute and reliability realities of large runs ([arXiv 2407.21783](https://arxiv.org/abs/2407.21783)). The team is an *illustrative scenario*: a university lab training a 3B-parameter model on 200 billion tokens of Indian-language text, then serving it to 500 concurrent users.

**What to build:** a written plan covering training compute and memory, parallelism outline, accelerator choice, capacity route (IndiaAI, hyperscaler capacity blocks, Spot), storage and checkpoint plan, expected failures and checkpoint interval, inference sizing, and a cost estimate for each option.

**Acceptance criteria:**
- Every number is derived in the document from stated formulas and sourced specs.
- At least three capacity routes compared on cost, lead time, residency and risk.
- Checkpoint interval justified from an assumed failure rate.
- A reviewer can reproduce your GPU-hour estimate within 10%.
- **Cost ceiling:** US$0.

**Stretch goals:** a TPU and Trainium variant with porting effort estimates.

**What it proves to an employer:** you can turn an AI ambition into a costed, credible infrastructure plan.

### P2 · A resilient small training cluster (L2, ~15 hours)

**Real-world inspiration:** SageMaker HyperPod, Google's Cluster Toolkit and Kubernetes with Kueue all exist because training jobs must survive hardware failures automatically. Llama 3's team reported above 90% effective training time despite 419 unexpected interruptions ([arXiv 2407.21783](https://arxiv.org/abs/2407.21783)).

**What to build:** a 2–4 GPU cluster (Slurm or Kubernetes with Kueue/JobSet) built with IaC, with a shared dataset on Lustre or object storage via FUSE/Mountpoint, health checks, async sharded checkpointing, automatic node replacement and job resubmission, and a goodput dashboard. Fine-tune a small open model as the workload.

**Acceptance criteria:**
- Three injected failures (node kill, simulated GPU error, network partition of one node) each lead to automatic resume from the last checkpoint without human action.
- Goodput (useful training time ÷ wall time) of at least 85% over a 2-hour run that includes the failures.
- GPU utilisation during steady state above 70%, with data-loader idle time under 5%.
- Teardown leaves no running GPU resources (verified by script).
- **Cost ceiling:** US$40; use Spot or capacity blocks where available and the smallest multi-GPU instances.

**Stretch goals:** topology-aware placement with a measured all-reduce gain; a TPU or Trainium variant of the same job.

**What it proves to an employer:** you can keep expensive accelerators doing useful work when things break, the core of ML platform roles.

### P3 · Production LLM inference with SLOs, residency and a cost case (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:**
- vLLM's PagedAttention ([arXiv 2309.06180](https://arxiv.org/abs/2309.06180)) and disaggregated serving ([DistServe](https://arxiv.org/abs/2401.09670)) define modern serving.
- KServe and llm-d brought LLM serving into the CNCF ecosystem in 2025.
- Managed platforms (Amazon Bedrock, Microsoft Foundry, Gemini Enterprise Agent Platform) compete on the same workloads.
- The service is an *illustrative scenario*: a multilingual assistant for a state-government citizen helpline whose data must stay in India, with a 10× spike on results day.

**What to build:**
- a self-hosted path: an open model served by vLLM or SGLang on GPU nodes in an India region, behind an inference-aware gateway with prefix-cache-aware routing, autoscaling on queue depth with warm capacity, private networking only, and GPU observability;
- a managed path: the same assistant on a managed platform restricted to India-region processing with private endpoints, or a documented reason why residency could not be guaranteed;
- an evaluation set in three languages to check that both paths meet a quality bar;
- an SLO document, a load-test suite, a capacity plan for results day, a security review (weights, egress, secrets), and a cost model for both paths.

**Acceptance criteria:**
- **SLOs:** under the steady-state load test, p95 TTFT under 1 second and p95 inter-token latency under 100 ms for prompts up to 2,000 tokens (adjust to your model size and state the hardware).
- **Spike:** a 10× step load for 10 minutes is handled with fewer than 1% failed or queued-out requests, using warm capacity and autoscaling; scaling events are shown on a timeline.
- **Residency:** a check proves that all inference, logs and stored prompts stay in India regions for the self-hosted path; the managed path's residency is documented with the provider's terms.
- **Cost:** measured cost per million tokens at three load levels for the self-hosted path, the managed path's cost at the same volumes, and the crossover volume.
- **Security:** model weights cannot be copied out of the serving namespace (demonstrated), and no public endpoint exists.
- **AI review:** a table of defects found in an assistant-generated serving configuration (resources, autoscaling signal, KV-cache settings, security).
- **Cost ceiling:** US$60 including GPU hours and managed-model usage; schedule short test windows.

**Stretch goals:** disaggregated prefill and decode with NVIDIA Dynamo or llm-d and a measured gain; LoRA adapters per department served from one base model; a confidential-GPU variant (see CLD501).

**What it proves to an employer:** you can run AI in production with measured latency, cost and compliance, which is what AI infrastructure and ML platform teams hire for.

## Feeds into

- [OV04 MLOps and ML Platform Engineering](../../../../04_overlaps/OV04_mlops_ml_platform/README.md): with MLE401 and OPS401.
- [CLD501 Frontier Seminar](../../year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md): confidential computing for AI, sovereign AI and energy.
- [MLE402 Distributed Training](../../../machine_learning_engineering/year_4/MLE402_distributed_training_and_large_scale_ml/README.md) and [MLE404 Efficient Inference](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md).
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): inference cost and goodput studies make strong capstones.
