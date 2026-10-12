# CLD404 · AI Infrastructure in the Cloud: GPUs, Inference and Managed AI

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [CLD304](../../year_3/CLD304_cloud_networking_vpcs_dns_load_balancing/README.md) | [OV04 MLOps and ML Platform Engineering](../../../../04_overlaps/OV04_mlops_ml_platform/README.md), [CLD501](../../year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md) |

Part of the [Cloud Engineering major](../../README.md). Strongly recommended: [CLD303](../../year_3/CLD303_containers_and_kubernetes/README.md) (GPU workloads run mostly on Kubernetes or Slurm) and [CLD305](../../year_3/CLD305_cloud_storage_and_managed_databases/README.md). Parallel-training algorithms are taught in [MLE402](../../../machine_learning_engineering/year_4/MLE402_distributed_training_and_large_scale_ml/README.md), and model-level inference optimisation (quantisation, distillation, compilers) in [MLE404](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md). This course is the infrastructure underneath: accelerators, capacity, networks, storage, schedulers, serving systems, managed platforms and cost.

## Why this course matters now

AI is now the main force behind cloud growth: Synergy Research attributes the 43% year-on-year growth in Q2 2026 cloud infrastructure spending primarily to generative AI ([Synergy, July 2026](https://www.srgresearch.com/articles/q2-cloud-market-passes-143-billion-highest-growth-rate-in-eight-years)). The hardware changes every year: AWS's P6-B300 instances carry eight Blackwell Ultra GPUs with 2,144 GB of HBM3e and 6.4 Tbps of network bandwidth ([AWS](https://aws.amazon.com/ec2/instance-types/p6/)); a Trainium3 UltraServer links 144 chips ([AWS, December 2025](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)); a Google Ironwood superpod links 9,216 TPUs ([Google Cloud](https://docs.cloud.google.com/tpu/docs/tpu7x)). In India, the IndiaAI compute portal offers access to 38,000 GPUs and 1,050 TPUs at subsidised rates below ₹100 an hour ([PIB, February 2026](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc2026210784401.pdf)).

The hard problems are not writing a training script. They are getting capacity at all, keeping thousands of GPUs busy when hardware fails constantly (Meta reported 419 unexpected interruptions in 54 days while training Llama 3 on up to 16,000 H100 GPUs, about 78% from hardware ([arXiv 2407.21783](https://arxiv.org/abs/2407.21783))), feeding data fast enough, and serving models at a cost per token the business can survive. Managed platforms keep renaming themselves (Azure AI Foundry became Microsoft Foundry in November 2025; Vertex AI became the Gemini Enterprise Agent Platform in April 2026), so engineers who understand the layers underneath stay useful through every rebrand.

## Learning outcomes

By the end you can:

1. **Explain** why AI workloads are bound by memory bandwidth, interconnect and data movement, and **estimate** compute, memory and time for a training run or an inference service.
2. **Compare** GPUs, TPUs and Trainium/Inferentia on performance, memory, interconnect, software ecosystem and lock-in, and **choose** instances on AWS, Azure and Google Cloud.
3. **Secure capacity** using quotas, capacity blocks, Dynamic Workload Scheduler, reservations and Spot, and **plan** for scarcity.
4. **Design** cluster networks (NVLink, InfiniBand, RoCE, EFA, ICI) and storage paths (Lustre, object storage with FUSE or Mountpoint, checkpoints) for training.
5. **Operate** GPU clusters with Slurm or Kubernetes (DRA, gang scheduling, Kueue), with health checks, auto-resume and checkpointing that achieve high effective training time.
6. **Deploy** LLM inference with vLLM or SGLang behind an inference-aware gateway, and **tune** time-to-first-token, inter-token latency and throughput.
7. **Use** managed AI platforms (Amazon Bedrock, Microsoft Foundry, Gemini Enterprise Agent Platform) with quotas, private networking, residency controls and provisioned throughput.
8. **Calculate and reduce** cost per million tokens and cost per training run, and **decide** between self-hosting and managed APIs.

## Chapters and lessons

### Chapter 1 · What makes AI infrastructure different (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The roofline | FLOPs versus memory bandwidth, arithmetic intensity, why decode is memory-bound and prefill compute-bound | Place matrix multiply, attention prefill and decode on a roofline for one GPU |
| 1.2 Sizing training | Parameters, tokens, FLOPs ≈ 6 × parameters × tokens; memory for weights, gradients and optimizer states; data, tensor and pipeline parallelism in outline | Estimate GPU-days and memory for a 7B and a 70B model |
| 1.3 Sizing inference | Weights, KV cache per token, batch size, concurrency; why context length drives memory | Compute KV-cache memory for 100 concurrent 8K-token chats |
| 1.4 The AI infrastructure stack | Accelerator, node, scale-up domain, scale-out network, storage, scheduler, framework, serving layer, platform | Draw the stack for a real announced cluster from public specs |

**Check your understanding:** (1) Why does adding GPUs not speed up decode for a single user? (2) Why is optimizer state often larger than the model? (3) What dominates memory for long-context serving?

### Chapter 2 · Accelerators (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 NVIDIA generations | H100, H200, B200, B300 (Blackwell Ultra), GB200 and GB300 rack-scale NVLink domains; HBM capacity and bandwidth; FP8 and FP4 | Build a comparison table from vendor datasheets |
| 2.2 Google TPUs | v5e, v5p, Trillium (v6e), Ironwood (TPU7x: 192 GiB HBM per chip, 9,216-chip superpods, 3D torus ICI); XLA and JAX | Run a small JAX job on a free TPU runtime and read the profile |
| 2.3 AWS silicon | Trainium2, Trainium3 (144 chips per UltraServer, 144 GB HBM3e per chip), Inferentia2; Neuron SDK | Port a small PyTorch model to Neuron (or study the porting guide) and list the friction |
| 2.4 Choosing silicon | Performance per dollar, availability, software maturity, portability, lock-in | Write a silicon decision for a start-up training a 3B Indic-language model |

**Check your understanding:** (1) Why does a bigger NVLink domain change model-parallel design? (2) What does moving to TPUs or Trainium cost in engineering time? (3) When is an older GPU the better buy?

### Chapter 3 · Capacity, instances and quotas (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Instance families | AWS P5/P5e/P5en, P6-B200, P6-B300, P6e UltraServers, G6/G6e, Trn2/Trn3, Inf2; Azure ND H100 v5, ND H200 v5, ND GB200 v6 and NC series; Google A3, A4, A4X, G4 and TPU slices | Map one training and one inference need to each provider |
| 3.2 Quotas | vCPU-based GPU quotas, per-region limits, model API quotas (tokens and requests per minute); requesting increases with evidence | Write a quota request with a usage justification |
| 3.3 Getting capacity | On-demand, EC2 Capacity Blocks for ML, Google Dynamic Workload Scheduler (flex-start and calendar mode), capacity reservations, Spot GPUs; regional availability, including India regions | Compare cost and lead time of four ways to get 32 GPUs for 72 hours |
| 3.4 Sovereign and subsidised compute | IndiaAI compute portal (38,000 GPUs and 1,050 TPUs below ₹100 an hour, February 2026), Indian GPU clouds, residency trade-offs | Assess eligibility and fit of the portal for an academic project |

**Check your understanding:** (1) Why can a quota approval still leave you without GPUs? (2) When are capacity blocks worth their premium over Spot? (3) What does a subsidised GPU hour not include?

### Chapter 4 · Networks for training (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Collectives | All-reduce, all-gather, reduce-scatter; ring and tree algorithms; NCCL; bandwidth and latency terms | Benchmark all-reduce with `nccl-tests` on two GPUs (or simulate) and fit the cost model |
| 4.2 Scale-up versus scale-out | NVLink/NVSwitch inside a node or rack versus the cluster network; why rack-scale systems change parallelism | Decide which parallelism goes on NVLink and which on the network |
| 4.3 InfiniBand, RoCE and EFA | RDMA, GPUDirect RDMA, congestion control; Meta's RoCE training networks (SIGCOMM 2024); AWS EFA (3,200 Gbps on P5 and P6-B200, 6,400 Gbps on P6-B300); Azure InfiniBand; Google ICI and Jupiter | Compare three providers' published training network designs |
| 4.4 Placement | Cluster placement groups, UltraClusters, compact placement policies, topology-aware scheduling | Show the bandwidth difference between packed and spread placement |

**Check your understanding:** (1) Why does one slow link slow the whole all-reduce? (2) What does RDMA remove from the data path? (3) Why must schedulers know the network topology?

### Chapter 5 · Storage and data for AI (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Feeding accelerators | Data-loader throughput, sharded datasets (WebDataset, Parquet), prefetching, GPU starvation | Measure GPU idle time from a slow data loader and fix it |
| 5.2 Parallel file systems | FSx for Lustre, Google Managed Lustre, Azure Managed Lustre; when object storage is enough (Mountpoint for S3, Cloud Storage FUSE, S3 Express One Zone) | Compare read throughput for one dataset on object storage and Lustre |
| 5.3 Checkpointing | Checkpoint size (weights plus optimizer state), async and sharded checkpoints, frequency versus failure rate | Compute an optimal checkpoint interval and measure checkpoint stall time |
| 5.4 Inference storage | Model weight loading speed, image streaming, KV-cache tiering to CPU memory and storage | Cut a model server's cold start by caching weights locally |

**Check your understanding:** (1) Why can a cheaper storage tier waste more money in idle GPU time? (2) What decides checkpoint frequency? (3) Why does model-load time matter for autoscaling?

### Chapter 6 · Orchestrating GPU clusters (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Slurm in the cloud | Partitions, gang allocation, SageMaker HyperPod, Google Cluster Toolkit, Azure CycleCloud | Run a two-node job on a small Slurm cluster |
| 6.2 Kubernetes for AI | GPU device plugins, Dynamic Resource Allocation (stable since v1.34), gang scheduling with Workload/PodGroup (beta in v1.37), Kueue, JobSet, KubeRay | Queue three jobs with Kueue quotas and watch preemption |
| 6.3 Scale | EKS clusters up to 100,000 nodes; the CNCF Kubernetes AI Conformance programme (31 certified platforms by July 2026) | Check a managed platform's conformance claims against the requirement list |
| 6.4 Sharing GPUs | MIG, time-slicing, MPS, fractional GPUs for inference and notebooks | Partition one GPU with MIG (or simulate) and run three workloads |

**Check your understanding:** (1) Why does a training job need all-or-nothing scheduling? (2) When is Slurm a better fit than Kubernetes? (3) What does MIG isolate that time-slicing does not?

### Chapter 7 · Reliability at scale (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Failure is normal | Llama 3's 466 interruptions in 54 days (419 unexpected, 58.7% GPU-related) and above 90% effective training time | Compute expected failures per day for clusters of 1,000 and 16,000 GPUs |
| 7.2 Detection and remediation | GPU health checks (DCGM), XID errors, NCCL timeouts, straggler detection, automatic node replacement | Inject a failed node and auto-resume from checkpoint |
| 7.3 Effective training time | Goodput, checkpoint and restart overheads, hot spares | Measure goodput for your lab run and improve it |

**Check your understanding:** (1) Why do failures grow with cluster size even if each GPU is reliable? (2) What is the cost of a too-long checkpoint interval? (3) How do hot spares change restart time?

### Chapter 8 · Serving LLMs at scale (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Inference mechanics | Prefill and decode, KV cache, continuous batching, PagedAttention (vLLM), prefix caching, speculative decoding in outline | Serve a small open model with vLLM and measure TTFT and inter-token latency |
| 8.2 Serving engines | vLLM, SGLang, TensorRT-LLM; NVIDIA Dynamo; disaggregated prefill and decode (DistServe) | Compare two engines on throughput at a fixed latency target |
| 8.3 Kubernetes-native serving | KServe (CNCF incubating), the Gateway API Inference Extension for model- and load-aware routing, llm-d's KV-cache-aware scheduling, LoRA adapter serving | Route requests by prefix-cache affinity and measure the hit rate |
| 8.4 Autoscaling inference | Scaling on queue depth and KV-cache use rather than CPU, scale-to-zero trade-offs, warm pools | Autoscale a model server on pending requests |
| 8.5 SLOs for AI services | TTFT, time per output token, throughput, error and refusal rates; load testing with realistic prompt distributions | Write SLOs and a load test for a chatbot |

**Check your understanding:** (1) Why does continuous batching raise throughput without hurting most users? (2) Why route requests by prefix? (3) Why is CPU utilisation a bad autoscaling signal for LLM servers?

### Chapter 9 · Managed AI platforms (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 The three platforms | Amazon Bedrock (including AgentCore), Microsoft Foundry (formerly Azure AI Foundry), Gemini Enterprise Agent Platform (formerly Vertex AI); model catalogues, fine-tuning, agents | Call the same model family through two platforms and compare features |
| 9.2 Quotas and throughput | Tokens and requests per minute, provisioned throughput, batch APIs, cross-region inference and its residency implications | Load-test until you hit the quota and design around it |
| 9.3 Private and compliant access | Private endpoints, VPC Service Controls, data-use terms, logging, India-region model availability | Call a model with no public internet path and log every request |
| 9.4 Build or buy | Managed APIs versus self-hosting on cost, latency, control, residency and lock-in | Write the decision for three products |

**Check your understanding:** (1) What does cross-region inference do to a residency promise? (2) When is provisioned throughput worth paying for? (3) Why do platform renames matter little to a well-designed architecture?

### Chapter 10 · Cost per token and per run (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Self-hosted cost per token | Cost per million tokens = hourly price ÷ (tokens per second × 3,600) × 1,000,000; utilisation, batch size, model size and quantisation as levers | Compute cost per million tokens for your vLLM deployment at three loads |
| 10.2 Prices move | AWS cut P5 on-demand prices by up to 45% in June 2025; capacity blocks; Spot; commitments | Recompute your model under three price scenarios |
| 10.3 Comparing with APIs | Input, output and cached-token prices; hidden costs (egress, logging, idle GPUs) | Find the crossover volume for self-hosting |

**Check your understanding:** (1) Why does cost per token fall with batch size until latency SLOs break? (2) Which hidden cost most often reverses a self-hosting decision? (3) How does a 45% price cut change your crossover point?

### Chapter 11 · Security and operations for AI infrastructure (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Protecting models and data | Weight theft, egress control, secrets, signed model artefacts, multi-tenant isolation; confidential GPUs in outline (CLD501) | Lock down a model-serving namespace and prove weights cannot leave |
| 11.2 GPU observability | DCGM exporter, GPU and memory utilisation, SM occupancy, power, XID errors; per-tenant usage | Build a GPU dashboard and alert on a stuck job |
| 11.3 Capacity planning | Forecasting token demand, headroom, multi-region inference failover | Plan capacity for a festival-season traffic spike |
| 11.4 AI agents operating AI infrastructure | Incident agents reading GPU telemetry; limits on what they may change | Compare an agent's diagnosis of a slow training job with yours |

**Check your understanding:** (1) Why is "GPU utilisation 100%" not proof the GPU is doing useful work? (2) What is the blast radius of a stolen model-serving credential? (3) Which operations should an agent never perform on a training cluster?

### Chapter 12 · Capstone integration (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Putting it together | From capacity request to production endpoint with SLOs, costs and runbooks | Present P3 with live load test and cost dashboard |

**Check your understanding:** (1) What is the first thing that fails in your design at 10× load? (2) What is your plan if GPUs are unavailable in your region for a week? (3) Which number tells leadership the system is healthy?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: sizing and roofline | Estimates sheet |
| 2 | 2 | Lab 2: accelerator comparison and TPU job | Profile and table |
| 3 | 3 | Lab 3: capacity options and quotas | Options memo; P1 starts |
| 4 | 4 | Lab 4: collectives benchmark | Cost model fit; P1 due |
| 5 | 5 | Lab 5: data loading and checkpoints | GPU idle fixed |
| 6 | 6 | Lab 6: Slurm and Kueue | Queued jobs; P2 starts |
| 7 | 7 | Lab 7: failure injection and auto-resume | Goodput report |
| 8 | 8 | Lab 8: vLLM serving and SLOs | TTFT/ITL baseline |
| 9 | 8 | Lab 9: inference gateway and autoscaling | Cache-aware routing; P2 due |
| 10 | 9 | Lab 10: managed platforms and quotas | Comparison |
| 11 | 10 | Cost-per-token model | Crossover chart; P3 starts |
| 12 | 11 | Security and GPU dashboards | Hardened namespace |
| 13 | 11 | Capacity plan | Plan and failover test |
| 14 | 12 | P3 completion | Live demo |
| 15 | Review and exam | — | Written exam and design oral |

## Working with AI in this course

- **Use AI for:** reading long hardware datasheets and summarising them (then checking numbers against the source), generating serving configurations and Kubernetes manifests, writing load-test scripts with realistic prompt distributions, explaining NCCL and DCGM output. Named tools: Claude Code, GitHub Copilot, Amazon Q Developer, Gemini Cloud Assist, AWS DevOps Agent.
- **Do without AI (drills):** the sizing estimates in Chapter 1, the cost-per-token arithmetic, checkpoint-interval calculations, and the design oral.
- **Verify AI output by:** checking every hardware and price figure against the provider's instance page for the exact region; benchmarking configurations rather than trusting claimed throughput; confirming model and feature availability in your India region on the provider's regional list; load-testing before accepting any autoscaling advice.
- **Where AI still fails here (show it):** assistants mix up GPU generations and memory sizes, quote instance types not offered in Mumbai or Hyderabad, use stale platform names, and suggest CPU-based autoscaling for LLM servers. Ask one to size a 70B model deployment and check its KV-cache arithmetic; record errors for your P3 report.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Written exam (sizing, networks, storage, serving, cost) | 20% |
| Design oral | 10% |

**Mastery gate:** you pass when you can, without AI help, (a) size the GPUs, memory, network and storage for an unseen training or serving brief within 30% of a reference answer and explain each number; (b) deploy an open model behind an inference gateway that meets stated TTFT and inter-token latency targets under a load test, with autoscaling; and (c) compute cost per million tokens for your deployment and the crossover volume against a managed API.

## Industry reality

AI infrastructure engineers sit at the most capacity-constrained point in the industry: they negotiate GPU capacity, run clusters where hardware failure is routine, and own the cost per token that decides whether AI products make money. Amazon EKS supports clusters with up to 800,000 NVIDIA GPUs or 1.6 million Trainium chips in a single cluster ([AWS, July 2025](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-eks-100000-worker-nodes-per-cluster/)). In India, the IndiaAI Mission, Indian GPU clouds and new hyperscaler investment are creating domestic demand for these skills, including for Indic-language model work.

Interview questions from this course:

1. **"How many GPUs do we need to serve a 70B model to 1,000 concurrent users?"** Cover weight memory by precision, KV cache per token and context length, batch size, throughput per GPU from benchmarks, latency targets, headroom and redundancy.
2. **"Our training job's GPUs show 40% utilisation. Investigate."** Cover data-loader starvation, storage throughput, network collectives and stragglers, checkpoint stalls, small batch sizes, and how to profile each.
3. **"We cannot get H100s in our region for a month. What are our options?"** Cover other regions and residency, capacity blocks, DWS, other accelerators (TPU, Trainium) and porting cost, smaller models, managed APIs, and Spot with checkpointing.
4. **"Self-host or use a managed model API?"** Cover cost per token at expected volume, utilisation risk, latency, data control and residency, operational burden, model choice and lock-in.
5. **"Design autoscaling for an LLM inference service."** Cover signals (queue depth, KV-cache use, TTFT), model-load time and warm pools, cache-aware routing, scale-to-zero trade-offs, and SLO-based policies.

## Resources (free first)

- **Provider docs:** [Amazon EC2 P6 instances](https://aws.amazon.com/ec2/instance-types/p6/), [Trn3 UltraServers](https://aws.amazon.com/ec2/instance-types/trn3/), [Elastic Fabric Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html), [Google Cloud TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x), [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview), [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry), [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html).
- **Open source:** [vLLM](https://docs.vllm.ai/), [SGLang](https://docs.sglang.ai/), [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo), [KServe](https://kserve.github.io/website/), [llm-d](https://llm-d.ai/), [Gateway API Inference Extension](https://gateway-api-inference-extension.sigs.k8s.io/), [Kueue](https://kueue.sigs.k8s.io/), [nccl-tests](https://github.com/NVIDIA/nccl-tests).
- **Papers:** [Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180) (vLLM, SOSP 2023); [DistServe](https://arxiv.org/abs/2401.09670) (disaggregated prefill and decode); [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) (infrastructure and reliability sections); [RoCE networks for distributed AI training at scale](https://engineering.fb.com/2024/08/05/data-center-engineering/roce-network-distributed-ai-training-at-scale/) (Meta, SIGCOMM 2024); [TPU v4](https://arxiv.org/abs/2304.01433) (ISCA 2023).
- **Courses:** Stanford [CS336 Language Modeling from Scratch](https://stanford-cs336.github.io/) (systems lectures); [The Ultra-Scale Playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook) (Hugging Face, free).
- **India:** [IndiaAI compute portal](https://indiaai.gov.in/) and the PIB explainer on subsidised compute.
- **Practising without a big bill:** do sizing, roofline and cost labs on paper; run small models (1–3B parameters, quantised) with vLLM on a single free-tier or low-cost GPU, free notebook GPUs or TPUs, or on CPU for functional tests; use simulated collectives where GPUs are unavailable; book GPU time in short, scripted windows and shut down automatically with a timer; eligible students and researchers can apply for IndiaAI subsidised compute.
- **Paid, worth it:** *AI Engineering* (Chip Huyen, O'Reilly, 2025) for the product context of these systems.

## Sources

All checked 12 Oct 2026.
- [Synergy Research Q2 2026](https://www.srgresearch.com/articles/q2-cloud-market-passes-143-billion-highest-growth-rate-in-eight-years) (30 Jul 2026).
- [Amazon EC2 P6 instances](https://aws.amazon.com/ec2/instance-types/p6/) (P6-B300: 8 GPUs, 2,144 GB HBM3e, 6.4 Tbps); [Trn3 UltraServers announcement](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/) (Dec 2025) and [product page](https://aws.amazon.com/ec2/instance-types/trn3/).
- [Google Cloud TPU7x (Ironwood) docs](https://docs.cloud.google.com/tpu/docs/tpu7x) and [3 things to know about Ironwood](https://blog.google/products/google-cloud/ironwood-google-tpu-things-to-know/).
- [PIB explainer, February 2026](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc2026210784401.pdf) (38,000 GPUs, 1,050 TPUs, under ₹100/h) and [PIB, 17 Feb 2026](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2229171) (20,000 more GPUs announced).
- [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) (Jul 2024).
- [Microsoft Foundry overview](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry) (naming history); [Introducing Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform) and [release notes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes) (22 Apr 2026).
- [EKS 100,000 nodes](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-eks-100000-worker-nodes-per-cluster/) (Jul 2025).
- [Kubernetes v1.34 DRA GA](https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/); [Kubernetes v1.37](https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/); [CNCF AI Conformance](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/) and [July 2026 update](https://www.cncf.io/blog/2026/07/23/the-future-of-ai-is-community-driven-and-open/).
- [KServe joins CNCF incubation](https://www.cncf.io/blog/2025/11/11/kserve-becomes-a-cncf-incubating-project/); [llm-d contributed to CNCF](https://www.redhat.com/en/blog/why-were-contributing-llm-d-cncf-standardizing-future-ai).
- [AWS GPU price reduction](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/) (Jun 2025).

_Last reviewed: 2026-10_
