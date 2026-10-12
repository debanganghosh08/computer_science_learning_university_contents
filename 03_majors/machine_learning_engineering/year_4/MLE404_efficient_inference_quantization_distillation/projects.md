# MLE404 · Labs and projects

Use PyTorch, ONNX Runtime, TensorRT or OpenVINO, torchao or LLM Compressor, vLLM and SGLang, llama.cpp, and ExecuTorch or LiteRT. A single modern GPU (cloud or university) covers the GPU labs; CPU and phone labs run on a laptop and an Android phone or emulator. Every result states hardware, software versions, batch size, concurrency and how latency was measured. Every compressed model is evaluated with your MLE304 harness by slice, not only on average.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Honest benchmarking | Build a timing harness with warm-up and synchronisation; reproduce an assistant's benchmark claim and find its errors | Naive vs correct timings; a note on each error found | 3 h |
| 2 · Export, compile and runtimes | `torch.export` and ONNX export with equivalence tests per dtype; fix 3 export failures; `torch.compile` modes; CUDA graphs at batch size 1; a TensorRT engine and an OpenVINO model | Test suite; fixed exports; speed-up table with compile and build times | 8 h (2 weeks) |
| 3 · Quantisation from scratch | Implement symmetric/asymmetric, per-tensor/per-channel/per-group quantise–dequantise; simulate FP8 and block-scaled 4-bit formats | Error tables per format and granularity | 4 h |
| 4 · int8 by slice | Static PTQ of a ResNet; dynamic quantisation of your MLE305 encoder; QAT recovery; slice-level evaluation | Accuracy and latency, overall and by slice; the worst slice explained | 4 h |
| 5 · GPTQ, AWQ and KV cache | Quantise a 1–8B open-weight LLM with GPTQ and AWQ; W8A8 vs weight-only; int8/FP8 KV cache | Perplexity, task scores (including a Hindi or other Indian-language set), memory and tokens/s | 5 h |
| 6 · Distillation | ResNet-50 → ResNet-18 with soft targets; distil your MLE305 encoder; a task-specific student from teacher labels | Accuracy and speed of each student vs teacher and vs training from labels | 5 h |
| 7 · Pruning and 2:4 sparsity | Magnitude pruning curves; Wanda on a small LLM; 2:4 sparse vs dense speed on supported hardware | Accuracy/perplexity vs sparsity; real speed-up table | 4 h |
| 8 · Batching, engines and speculative decoding | Static vs dynamic vs continuous batching under bursty load; prefix caching on a retrieval-style workload; one model on vLLM and SGLang at fixed p95; speculative decoding with a draft model | Throughput vs p95 curves; engine comparison at the SLO; acceptance rate and speed-up | 8 h (2 weeks) |
| 9 · CPU inference | ONNX Runtime and OpenVINO thread/batch tuning; fp32 vs int8; llama.cpp across GGUF quantisation levels | Latency and cost per 1,000 predictions; tokens/s per level | 3 h |
| 10 · On-device deployment | Deploy a model with ExecuTorch or LiteRT on an Android phone or emulator; benchmark cold start and p95 | App or harness; on-device latency distribution | 5 h |

## Projects

### P1 · An inference benchmarking toolkit (L1, ~6 hours)

**Real-world inspiration.** MLPerf Inference defines scenarios (offline, server, single-stream) because "how fast is this model?" has no answer without a load pattern. Engine papers such as Orca and vLLM report throughput at stated latency targets for the same reason.

**What to build.** A command-line tool that benchmarks any HTTP or Python inference endpoint in closed-loop and open-loop (Poisson arrivals) modes, reporting p50/p95/p99 latency, throughput, TTFT and TPOT for streaming LLM endpoints, error rate and cost per 1,000 requests from a configured hourly price. Produce baseline reports for one classic model and one small LLM.

**Acceptance criteria**
- Includes warm-up, correct GPU synchronisation for in-process benchmarks, and fixed random seeds for arrival patterns.
- Repeated runs agree within 5% on p50 and 10% on p99 (coefficient of variation reported).
- Results for one LLM endpoint agree within 10% with the engine's own benchmark script under the same settings.
- Reports include hardware, versions, concurrency and arrival process automatically.
- A latency–throughput curve is generated for each endpoint.

**Stretch goals.** GPU utilisation and memory sampling during runs; an HTML report comparing two runs.

**What it proves to an employer.** You measure before you optimise, and your numbers can be trusted.

### P2 · Compress a production classifier without breaking a slice (L2, ~15 hours)

**Real-world inspiration.** DistilBERT kept 97% of BERT's language-understanding capability while being 40% smaller and 60% faster (2019); int8 quantisation is standard on CPUs and GPUs. In production the risk is not average accuracy but a segment that silently gets worse.

**What to build.** Take your MLE305 text or vision classifier and produce at least five variants: compiled baseline, int8 PTQ, int8 QAT, a distilled student, and a pruned or structured-sparse version. Evaluate each with your MLE304 harness and deploy the best one on CPU with ONNX Runtime or OpenVINO behind your MLE401 service.

**Acceptance criteria**
- A Pareto plot of accuracy vs p95 latency vs cost per 1,000 predictions for all variants, each with seeds or CIs.
- The chosen variant is at least 3× cheaper or faster than the baseline at its serving concurrency, with no more than 1 point overall accuracy loss.
- No predefined key slice (for example class, language or source) loses more than 2 points; a release gate in CI enforces it.
- Calibration data choice is documented, with an experiment showing the effect of out-of-domain calibration data.
- A 2-page report explains why each technique helped or did not on your hardware.

**Stretch goals.** Mixed precision for sensitive layers chosen by per-layer sensitivity analysis; an on-device version with ExecuTorch or LiteRT.

**What it proves to an employer.** You can cut serving cost substantially while protecting quality where it matters, a measurable business result.

### P3 · Cost-optimised LLM serving with multilingual quality gates (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Continuous batching (Orca), PagedAttention (vLLM), prefix caching (SGLang), speculative decoding and 4-bit weight quantisation (GPTQ, AWQ) are the levers behind affordable LLM products; NVIDIA Dynamo adds disaggregated prefill and decode for large deployments. Illustrative scenario: a start-up offering an assistant in English and Hindi must serve it at a price its users can afford.

**What to build.** Serve an open-weight LLM (1–8B, with at least one Indian language in its documented training or evaluation) at the lowest cost that meets a service-level objective you set (for example p95 time-to-first-token under 1 s and time-per-output-token under 50 ms at a stated concurrency). Compare precisions (bf16, FP8 or int8, 4-bit GPTQ or AWQ), two engines (vLLM and SGLang), prefix caching and speculative decoding, plus a CPU or laptop path with llama.cpp for offline use.

**Acceptance criteria**
- A quality evaluation suite covering English and at least one Indian language, long-context prompts and a task set relevant to the scenario; every variant's score is reported by language.
- The chosen configuration meets the SLO in a load test with realistic arrivals and prompt-length distribution, using your P1 toolkit.
- Quality loss of the chosen configuration is within a threshold you set and justify, overall and for each language.
- Cost per 1 million output tokens is computed for each variant from measured throughput and stated prices (cloud and, where eligible, IndiaAI rates).
- A capacity plan states GPUs needed for 10× traffic, with and without prefix caching.
- A report (6–8 pages) includes the Pareto frontier, rejected options with reasons, and a reproducible launch script.

**Stretch goals.** KV-cache quantisation with a measured concurrency gain; a disaggregated prefill/decode experiment; distil a task-specific small model and compare its cost and quality with the quantised general model.

**What it proves to an employer.** You can make an LLM product economically viable with evidence, one of the most in-demand skills in AI infrastructure.

## Feeds into

- [OV09 Edge AI and Secure IoT](../../../../04_overlaps/OV09_edge_ai_secure_iot/README.md): Lab 10 and P2's on-device path continue in OV09A (deploying models on edge devices).
- [OV04 MLOps and ML Platform Engineering](../../../../04_overlaps/OV04_mlops_ml_platform/README.md): P3's capacity planning and cost model feed OV04B (LLMOps at scale).
- [MLE501 Frontier Seminar](../../year_5/MLE501_frontier_seminar_ml_research_engineering/README.md): reproducing a compression or serving paper is a natural seminar project.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): multilingual quality under compression is an open, practical research topic.
