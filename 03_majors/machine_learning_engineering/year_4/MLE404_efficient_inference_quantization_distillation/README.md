# MLE404 · Efficient Inference: Quantization, Distillation and Compilers

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [MLE304](../../year_3/MLE304_model_evaluation_fairness_and_robustness/README.md) (and serving basics from [MLE401](../MLE401_mlops_deployment_monitoring_and_retraining/README.md)) | [OV09 Edge AI and Secure IoT](../../../../04_overlaps/OV09_edge_ai_secure_iot/README.md), [OV04](../../../../04_overlaps/OV04_mlops_ml_platform/README.md), [MLE501](../../year_5/MLE501_frontier_seminar_ml_research_engineering/README.md) |

## Why this course matters now

Training happens once; inference runs every time a user does anything, so for a widely used model the serving bill keeps growing long after training ends, and it decides whether a product is affordable. Most of the gains come from systems ideas, not new models: continuous batching gave up to 36.9× higher throughput than FasterTransformer on GPT-3 175B (Orca, OSDI 2022); vLLM's PagedAttention added a further 2–4× over FasterTransformer and Orca by nearly eliminating KV-cache waste (SOSP 2023); AWQ's 4-bit weight quantization won the MLSys 2024 best paper award; NVIDIA's NVFP4 format stores weights about 3.5× smaller than FP16 (2025); and DeepSeek released six dense distilled reasoning models from 1.5B to 70B parameters (2025). Runtimes keep moving: ExecuTorch reached 1.0 in October 2025, TensorFlow Lite became LiteRT in 2024, and Triton Inference Server became part of NVIDIA Dynamo in 2025. Assistants will happily produce a quantisation script. Choosing calibration data, proving that the int4 model did not silently fail one language or customer segment, measuring p99 under real load, and knowing which tricks your hardware actually accelerates is the engineering work this course teaches.

## Learning outcomes

By the end you can:

1. **Benchmark** inference correctly (warm-up, synchronisation, load generation, p50/p99, throughput, time-to-first-token and time-per-output-token, cost per 1,000 requests or tokens).
2. **Explain** with the roofline model why LLM decoding is memory-bound and which optimisations help in each regime.
3. **Export and compile** models with `torch.export`, ONNX, `torch.compile`, TensorRT and OpenVINO, and **diagnose** graph breaks and dynamic-shape problems.
4. **Apply** post-training quantisation and quantisation-aware training (int8, int4, FP8, microscaling formats) and **evaluate** accuracy by slice, not only on average.
5. **Quantise** LLMs with GPTQ, AWQ and SmoothQuant-style methods and **compare** them on quality, speed and memory.
6. **Distil** large models into small ones (logit, feature and sequence-level distillation) and **measure** what is lost.
7. **Prune** models (unstructured, structured, 2:4) and **show** when sparsity gives real speed-ups.
8. **Configure** serving engines (vLLM, SGLang, TensorRT-LLM, Dynamo-Triton) with continuous batching, prefix caching and speculative decoding, and **tune** the latency–throughput trade-off.
9. **Deploy** models on CPUs, phones and edge devices (ONNX Runtime, OpenVINO, llama.cpp, ExecuTorch, LiteRT, Core ML).
10. **Choose** an efficient design from an accuracy–latency–cost Pareto frontier and **defend** it.

## Chapters and lessons

### Chapter 1 · Measuring inference (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Metrics | Latency percentiles, throughput, TTFT and TPOT, memory, cost per 1,000 requests or tokens | Define the metrics for a chatbot, a fraud API and a nightly batch job |
| 1.2 Benchmarking pitfalls | Warm-up, CUDA synchronisation, timer placement, batch size 1 vs batched, closed- vs open-loop load | Show a 5× error from a naive GPU timer; fix it |
| 1.3 The roofline for inference | Arithmetic intensity of prefill vs decode; memory bandwidth limits | Predict decode tokens/s from model size and HBM bandwidth; measure |
| 1.4 Industry benchmarks | MLPerf Inference scenarios (offline, server, single-stream) | Map your use case to an MLPerf scenario |

**Check your understanding:** Why is single-token decoding memory-bound? Why does the average latency hide what users feel? Why must a benchmark state the batch size and concurrency?

### Chapter 2 · Export and graphs (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Graph capture | `torch.export` (ahead-of-time, full graph) vs eager; dynamic shapes | Export a vision model and a small transformer |
| 2.2 ONNX | ONNX opsets, export, ONNX Runtime execution providers (CPU, CUDA, TensorRT) | Export to ONNX; verify outputs within tolerance |
| 2.3 Numerical equivalence | Tolerances per dtype; testing exported models against the original | Build an equivalence test suite for exports |
| 2.4 Failure modes | Unsupported ops, data-dependent control flow, graph breaks | Fix 3 export failures in a provided model |

**Check your understanding:** Why does data-dependent control flow break export? What tolerance is reasonable for fp16 vs fp32 outputs? When should you keep a model in eager mode?

### Chapter 3 · Compilers and runtimes (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 `torch.compile` | TorchDynamo capture, TorchInductor code generation with Triton kernels, modes, recompilation | Measure speed-up and compile time for 3 models |
| 3.2 Fusion and CUDA graphs | Operator fusion, kernel-launch overhead, CUDA graphs for small batches | Show launch overhead dominating at batch size 1; fix with CUDA graphs |
| 3.3 TensorRT and OpenVINO | Engine building, precision modes, layer fusion; Intel CPU/GPU/NPU targets | Build a TensorRT engine and an OpenVINO model; compare |
| 3.4 ML compilers | Apache TVM, MLC LLM; portability across hardware | Run a model through MLC LLM on a laptop GPU or WebGPU |

**Check your understanding:** Why can compilation make the first request slow? When does fusion help most? Why might a TensorRT engine need rebuilding after a driver upgrade?

### Chapter 4 · Quantisation fundamentals (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Number formats | fp32, bf16, fp16, int8, int4, FP8 (E4M3, E5M2), microscaling MXFP4 and NVFP4 (16-value blocks with E4M3 scales) | Represent the same tensor in 5 formats; measure error |
| 4.2 Affine quantisation | Scale and zero point, symmetric vs asymmetric, per-tensor vs per-channel vs per-group (Jacob et al., 2018; Nagel et al., 2021) | Implement quantise/dequantise; compare granularities |
| 4.3 PTQ and calibration | Min-max, percentile and MSE calibration; choosing calibration data | Calibrate with in-domain vs out-of-domain data; compare accuracy |
| 4.4 Quantisation-aware training | Fake quantisation, straight-through estimator | Recover accuracy lost by int8 PTQ with QAT |
| 4.5 Outliers | Activation outliers in transformers and mixed-precision decomposition (LLM.int8()) | Find outlier channels in a small LLM |

**Check your understanding:** Why is per-channel weight quantisation more accurate than per-tensor? Why does calibration data from the wrong domain hurt? Why are activations harder to quantise than weights in LLMs?

### Chapter 5 · Quantising classic and vision models (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 int8 CNNs | Static PTQ with ONNX Runtime or TensorRT; fused conv-BN-ReLU | Quantise a ResNet; report speed-up and accuracy |
| 5.2 Encoders | Dynamic quantisation for BERT-style encoders; Hugging Face Optimum | Quantise your MLE305 text classifier |
| 5.3 Slice-level evaluation | Using the MLE304 harness: accuracy by class, language or segment after quantisation | Find a slice that degrades 3× more than average |
| 5.4 When not to quantise | Small models, CPU without int8 support, numerically sensitive outputs | A decision note for 3 deployment targets |

**Check your understanding:** Why can a quantised model lose 0.5% overall but 5% on one class? What hardware feature makes int8 fast on CPUs? Why fuse BatchNorm before quantising?

### Chapter 6 · Quantising LLMs (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Weight-only methods | GPTQ (second-order, 3–4 bits; 175B models in about 4 GPU hours), AWQ (activation-aware scaling) | Quantise a 1–8B model with GPTQ and AWQ; compare perplexity and task scores |
| 6.2 Weight + activation | SmoothQuant W8A8 (up to 1.56× faster, 2× less memory in its paper); FP8 inference | Run W8A8 vs weight-only; measure throughput |
| 6.3 KV-cache quantisation | Memory per token, cache precision vs quality | Fit 2× more concurrent requests with an int8/FP8 KV cache |
| 6.4 Formats and tools | GGUF for llama.cpp, torchao, LLM Compressor, Transformers quantisation integrations | Produce GGUF and torchao versions of the same model |
| 6.5 Evaluating quantised LLMs | Perplexity is not enough: task evals, long-context tests, multilingual slices | Build a 5-part evaluation for a quantised model, including Hindi prompts |

**Check your understanding:** Why does AWQ protect a small fraction of salient weights? Why is weight-only quantisation enough for memory-bound decoding? What failures can perplexity miss?

### Chapter 7 · Distillation (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Soft targets | Temperature, KL loss on logits (Hinton et al., 2015) | Distil a ResNet-50 into a ResNet-18; compare with training from labels |
| 7.2 Encoders | DistilBERT: 40% smaller, 60% faster, 97% of language-understanding capability | Distil your MLE305 encoder |
| 7.3 Generative models | Sequence-level and on-policy distillation; MiniLLM (reverse KL) | Distil a small instruction model on teacher outputs |
| 7.4 Distillation from APIs and reasoning models | Teacher-generated data (DeepSeek-R1's distilled models); licence and terms-of-use constraints | Build a task-specific student from teacher labels; measure cost per 1,000 requests vs the teacher |

**Check your understanding:** Why do soft targets carry more information than hard labels? When does a student beat its teacher on a narrow task? What legal and licence checks come before distilling a commercial model?

### Chapter 8 · Pruning and sparsity (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Unstructured pruning | Magnitude pruning, iterative pruning and fine-tuning | Prune 50%, 80%, 95%; plot accuracy |
| 8.2 One-shot LLM pruning | SparseGPT (50–60% sparsity on OPT-175B in under 4.5 hours), Wanda (weight × activation, no retraining) | Prune a small LLM with Wanda; measure perplexity |
| 8.3 Structured sparsity | 2:4 sparsity on NVIDIA Ampere and later (2× peak sparse throughput) | Measure real speed-up of a 2:4 model vs dense |
| 8.4 Real vs nominal savings | FLOPs removed vs latency gained; structured pruning of heads and layers | Show 80% unstructured sparsity giving no speed-up on a GPU |

**Check your understanding:** Why does unstructured sparsity rarely speed up GPUs? Why does 2:4 sparsity need hardware support? When is removing whole layers better than sparsifying all of them?

### Chapter 9 · Batching and serving engines (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Dynamic and continuous batching | Request-level vs iteration-level scheduling (Orca) | Compare static, dynamic and continuous batching under bursty load |
| 9.2 KV-cache management | PagedAttention (vLLM); prefix caching with RadixAttention (SGLang) | Measure throughput gain from prefix caching on a RAG-style workload |
| 9.3 Faster decoding | Speculative decoding (2–3× on T5-XXL with identical outputs), FlashAttention-2/3 | Enable speculative decoding; measure acceptance rate and speed-up |
| 9.4 Engines | vLLM, SGLang, TensorRT-LLM; Dynamo-Triton for non-LLM models | Serve one model on two engines; compare at fixed p95 latency |
| 9.5 Disaggregated serving | Separating prefill and decode (DistServe, 2024; NVIDIA Dynamo); KV-aware routing | Explain when disaggregation pays off |
| 9.6 Capacity planning | Throughput at a latency SLO, autoscaling GPUs, cost per 1M tokens | Capacity plan for 100 requests per second at p95 < 2 s |

**Check your understanding:** Why does continuous batching help most when output lengths vary? Why does prefix caching matter for chat and retrieval workloads? Why must speculative decoding be verified by the target model?

### Chapter 10 · CPU inference (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 CPU runtimes | ONNX Runtime CPU, OpenVINO, oneDNN; threads, affinity, batch size | Tune threads and batch size for a CPU service |
| 10.2 int8 on CPUs | Vector instructions for int8 (VNNI) and matrix units (AMX) on recent server CPUs | Compare fp32 vs int8 on your CPU |
| 10.3 LLMs on CPU | llama.cpp and GGUF quantisation levels | Run a 1–3B model on a laptop; tokens/s per quantisation level |
| 10.4 CPU vs GPU economics | Cost per 1,000 predictions; utilisation; when CPUs win | Cost comparison for your MLE305 model |

**Check your understanding:** Why can a CPU beat a GPU for a small model at low traffic? What limits llama.cpp's tokens per second? Why does thread oversubscription hurt latency?

### Chapter 11 · Edge and mobile (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Constraints | Memory, power, thermal throttling, app size, offline use, privacy | Write the constraints for a farmer-advisory app on low-end Android phones (illustrative) |
| 11.2 Runtimes | ExecuTorch 1.0, LiteRT, Core ML, MLC LLM | Deploy one model with ExecuTorch or LiteRT on an Android phone or emulator |
| 11.3 On-device benchmarks | Latency distribution on real devices; cold start; battery | Benchmark on two phones; report p50/p95 |
| 11.4 Updates and security | Model updates over the air, integrity checks (continued in OV09) | Design a signed model-update flow |

**Check your understanding:** Why do phone benchmarks vary run to run? What does on-device inference give users beyond latency? Why must model updates be signed?

### Chapter 12 · Choosing an efficient design (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 The Pareto frontier | Accuracy vs latency vs cost; dominated options | Plot the frontier for 10 variants of one model |
| 12.2 A decision procedure | Measure → profile → cheapest fix first (batching, compile) → precision → distillation → architecture | Apply it to P3 |
| 12.3 Inference FinOps | Cost per request, per user, per feature; reserved vs spot; idle cost | Monthly cost model with 3 traffic scenarios |
| 12.4 Keeping the gains | Latency and slice-accuracy regression gates in CI; re-benchmarking after driver, engine or model upgrades | Add latency and accuracy gates to your CI |

**Check your understanding:** Why try batching and compilation before quantisation? When is a smaller model better than a quantised large one? What does an idle GPU cost you?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Honest benchmarking | — |
| 2 | 2 | Lab 2 · Export and equivalence tests | — |
| 3 | 3 | Lab 2 (continued): compile, TensorRT, OpenVINO | **P1 due** |
| 4 | 4 | Lab 3 · Quantisation from scratch | — |
| 5 | 5 | Lab 4 · int8 vision and encoders by slice | — |
| 6 | 6 | Lab 5 · GPTQ, AWQ, KV cache | Mid-term (AI off) |
| 7 | 7 | Lab 6 · Distillation | — |
| 8 | 8 | Lab 7 · Pruning and 2:4 sparsity | **P2 due** |
| 9 | 9 | Lab 8 · Batching and prefix caching | — |
| 10 | 9 | Lab 8 (continued): engines and speculative decoding | — |
| 11 | 10 | Lab 9 · CPU inference | — |
| 12 | 11 | Lab 10 · On-device deployment | — |
| 13 | 12 | Pareto study (P3) | — |
| 14 | 12 | Cost model and report (P3) | **P3 due** |
| 15 | Review | P3 presentation | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** export and quantisation scripts; engine configuration flags; explaining profiler traces and compiler errors; generating load-test scripts; summarising papers before you read them.
- **Do without AI (drills):** roofline estimates of decode speed; memory for weights and KV cache; quantise/dequantise arithmetic by hand; choosing a method for a stated constraint; reading a latency–throughput curve. The mid-term and final are AI-off.
- **Verify AI output by:** equivalence tests against the original model; slice-level evaluation after every compression step; benchmarking with warm-up and synchronisation under realistic concurrency; checking that the claimed format (for example FP8 or 2:4 sparsity) is actually accelerated on your hardware; reading the engine's current documentation, because flags change between releases.
- **Where AI still fails here:** assistants report speed-ups from flawed GPU timing, recommend formats your hardware does not accelerate, quantise with random or out-of-domain calibration data, judge LLM quantisation by perplexity alone, and suggest archived tools (TorchServe) or old names (TensorFlow Lite). In Lab 1 you reproduce an assistant's benchmark and document where it was wrong.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 45% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 20% |

**Mastery gate.** You pass when you can: (1) take an unseen model and a latency and cost target, and within two working days deliver a compressed, served version that meets the target, with an accuracy report by slice showing no key slice degrades more than an agreed threshold; (2) without AI, estimate decode throughput and memory (weights plus KV cache) for an LLM on given hardware within 2× of measurement; (3) explain why your chosen techniques work on your hardware and why the rejected ones did not.

## Industry reality

Inference optimisation is done by ML engineers, ML infrastructure engineers and performance engineers at AI labs, cloud providers, consumer apps and device makers. Open-source engines (vLLM, SGLang, llama.cpp), vendor stacks (TensorRT-LLM, NVIDIA Dynamo, OpenVINO) and on-device runtimes (ExecuTorch, LiteRT, Core ML) are where the work happens. Illustrative scenario: an Indian product serving price-sensitive users on low-end phones and patchy networks may need on-device or CPU inference as a product requirement, not an optimisation.

**Interview questions from this course**

1. *Serve a 7B-parameter LLM for 50 concurrent users at the lowest cost with p95 under 2 seconds.* Strong answer: memory for weights and KV cache; quantisation choice; continuous batching and prefix caching; GPU type and count from a throughput-at-SLO measurement; speculative decoding; autoscaling; cost per million tokens.
2. *Explain int8 quantisation. Why are LLMs harder to quantise than CNNs?* Strong answer: scale and zero point; per-channel vs per-tensor; calibration; activation outliers; weight-only vs W8A8; methods (LLM.int8(), SmoothQuant, GPTQ, AWQ).
3. *Quantisation, distillation or pruning: how do you choose?* Strong answer: target hardware support, accuracy budget, engineering cost, whether the bottleneck is memory or compute; usually batching and compilation first, then precision, then distillation.
4. *What is continuous batching and why does PagedAttention help?* Strong answer: iteration-level scheduling; variable output lengths; KV-cache fragmentation; paging; effect on throughput and tail latency.
5. *After int8 quantisation, overall accuracy fell 0.5% but one customer segment complains. What happened?* Strong answer: slice-level degradation; calibration data not covering that segment; outlier features; fix by better calibration, mixed precision for sensitive layers, QAT, or a per-segment release gate.

## Resources (free first)

- **Courses:** MIT 6.5940 TinyML and Efficient Deep Learning Computing (2024 lectures; Fall 2026 edition "TinyML and Efficient AI Computing") — https://hanlab.mit.edu/courses/2024-fall-65940 and https://hanlab.mit.edu/courses/2026-fall-65940 ; CMU Deep Learning Systems — https://dlsyscourse.org/ ; CMU Machine Learning Systems — https://mlsyscourse.org/
- **Guides:** Nagel et al., "A White Paper on Neural Network Quantization" — https://arxiv.org/abs/2106.08295 ; Horace He, "Making Deep Learning Go Brrrr" — https://horace.io/brrr_intro.html ; Anyscale, continuous batching explainer — https://www.anyscale.com/blog/continuous-batching-llm-inference ; MLPerf Inference — https://mlcommons.org/benchmarks/inference-datacenter/
- **Export and compilers:** `torch.compile` — https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler.html ; `torch.export` — https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/export.html ; ONNX Runtime quantisation — https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html ; TensorRT — https://docs.nvidia.com/deeplearning/tensorrt/latest/index.html ; OpenVINO — https://docs.openvino.ai/ ; Apache TVM — https://tvm.apache.org/ ; Hugging Face Optimum — https://huggingface.co/docs/optimum/index
- **Quantisation tools:** torchao — https://github.com/pytorch/ao ; LLM Compressor — https://github.com/vllm-project/llm-compressor ; Transformers quantisation overview — https://huggingface.co/docs/transformers/main/en/quantization/overview ; GGUF — https://github.com/ggml-org/ggml/blob/master/docs/gguf.md
- **Serving engines:** vLLM — https://docs.vllm.ai/ ; SGLang — https://docs.sglang.ai/ ; TensorRT-LLM — https://github.com/NVIDIA/TensorRT-LLM ; NVIDIA Dynamo — https://docs.nvidia.com/dynamo/latest/ ; llama.cpp — https://github.com/ggml-org/llama.cpp
- **On-device:** ExecuTorch — https://docs.pytorch.org/executorch/stable/index.html ; LiteRT — https://ai.google.dev/edge/litert ; Core ML — https://developer.apple.com/documentation/coreml ; MLC LLM — https://github.com/mlc-ai/mlc-llm

## Sources

- Yu et al., Orca (OSDI 2022) — https://www.usenix.org/conference/osdi22/presentation/yu ; Kwon et al., PagedAttention/vLLM (SOSP 2023) — https://arxiv.org/abs/2309.06180 ; Zheng et al., SGLang — https://arxiv.org/abs/2312.07104 ; Leviathan et al., speculative decoding — https://arxiv.org/abs/2211.17192 ; Dao et al., FlashAttention — https://arxiv.org/abs/2205.14135 ; Shah et al., FlashAttention-3 — https://arxiv.org/abs/2407.08608 ; Zhong et al., DistServe — https://arxiv.org/abs/2401.09670 (checked 2026-10)
- Frantar et al., GPTQ — https://arxiv.org/abs/2210.17323 ; Lin et al., AWQ (MLSys 2024 Best Paper, per arXiv comment) — https://arxiv.org/abs/2306.00978 ; Xiao et al., SmoothQuant — https://arxiv.org/abs/2211.10438 ; Dettmers et al., LLM.int8() — https://arxiv.org/abs/2208.07339 ; Dettmers et al., QLoRA — https://arxiv.org/abs/2305.14314 ; Jacob et al. (integer-only inference) — https://arxiv.org/abs/1712.05877 ; Rouhani et al., microscaling formats — https://arxiv.org/abs/2310.10537 ; NVIDIA, "Introducing NVFP4" (24 Jun 2025) — https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/ (checked 2026-10)
- Frantar and Alistarh, SparseGPT — https://arxiv.org/abs/2301.00774 ; Sun et al., Wanda — https://arxiv.org/abs/2306.11695 ; NVIDIA, 2:4 sparsity on Ampere (20 Jul 2021) — https://developer.nvidia.com/blog/accelerating-inference-with-sparsity-using-ampere-and-tensorrt/ (checked 2026-10)
- Hinton et al., distillation — https://arxiv.org/abs/1503.02531 ; Sanh et al., DistilBERT — https://arxiv.org/abs/1910.01108 ; Gu et al., MiniLLM — https://arxiv.org/abs/2306.08543 ; DeepSeek-AI, DeepSeek-R1 (six distilled dense models, 1.5B–70B) — https://arxiv.org/abs/2501.12948 (checked 2026-10)
- PyTorch, "Introducing ExecuTorch 1.0" (22 Oct 2025) — https://pytorch.org/blog/introducing-executorch-1-0/ ; Google, "TensorFlow Lite is now LiteRT" (4 Sep 2024) — https://developers.googleblog.com/en/tensorflow-lite-is-now-litert/ ; NVIDIA, "Introducing NVIDIA Dynamo" (18 Mar 2025) — https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/ (checked 2026-10)
- Versions on PyPI (checked 2026-10): vLLM 0.31.0, SGLang 0.5.21, ONNX Runtime 1.31.0, TensorRT 11.4, TensorRT-LLM 1.2.1, ExecuTorch 1.5.1, OpenVINO 2026.4.1, torchao 0.18.0

_Last reviewed: 2026-10_
