# DLR404 · Labs and projects

Every lab and project ships with the GPU model, driver and library versions, a correctness suite against a PyTorch reference, and benchmarks that follow the course checklist: warm-up, synchronisation, fixed shapes and dtypes, median and p90 of at least 50 runs, and the strongest available baseline. A speed-up without a correctness suite scores zero.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Roofline and microbenchmarks | Measure achieved bandwidth and matmul throughput; copy, strided access, warp divergence and bank conflicts; place 10 PyTorch ops on the roofline | Roofline plot with measured ceilings; op classification checked against timing; one plot per microbenchmark effect | 6 h |
| 2 · Profiling a training step | `torch.profiler` and Nsight Systems on your GPT; find CPU gaps and the top kernels | Annotated trace screenshots; a ranked list of 3 bottlenecks | 4 h |
| 3 · CUDA transpose and matmul | Naive vs shared-memory transpose; naive → coalesced → tiled matmul; PyTorch extension | GFLOPS per version vs cuBLAS; tests vs `torch.matmul` | 6 h |
| 4 · Triton kernels | Fused softmax and RMSNorm (forward and backward, custom `autograd.Function`); tiled matmul with autotuning; chunked linear + cross-entropy for a 128k vocabulary | Correctness on 500 random shapes; speed vs eager and `torch.compile`; matmul TFLOPS vs cuBLAS; loss memory before/after | 10 h |
| 5 · `torch.compile` and CUDA graphs | Compile a GPT; remove graph breaks; CUDA graphs for decoding | Generated-code excerpts; throughput and latency tables | 4 h |
| 6 · FlashAttention forward in Triton | Tiled attention with online softmax and causal masking | Max error vs `scaled_dot_product_attention` (fp16/fp32); speed vs the math backend | 6 h |
| 7 · Quantised matmul | int8 per-channel and int4 group-wise weight-only matmul in Triton | Accuracy (perplexity of a small LM) and decode speed vs fp16 | 5 h |
| 8 · Pruning and MoE profiling | Wanda 50% pruning of a small LM; profile an MoE layer's routing and expert matmuls | Perplexity vs sparsity; time breakdown of the MoE layer | 4 h |
| 9 · Memory and communication on 2× T4 | Predict, then measure, peak memory with checkpointing, FSDP and an 8-bit optimizer; all-reduce bandwidth; DDP with and without bucketing and overlap | Predicted vs measured memory (within 15%); largest model that fits; bus bandwidth; trace showing overlap | 7 h |
| 10 · Audit an AI-written kernel | Have an agent write a fused kernel; attack it with adversarial tests (shapes, strides, dtypes, aliasing, call order) | Audit report: bugs found, the test that found each, the fix | 4 h |

## Projects

### P1 · Roofline report for a real model (L1, ~6 hours)

**Real-world inspiration.** Performance engineers start every investigation by asking which ceiling an operation hits; Horace He's "Making Deep Learning Go Brrrr" and the roofline model (Williams et al., 2009) are the standard framing.

**What to build.** A report and reusable script that measures your GPU's real bandwidth and tensor-core throughput, then profiles one forward and backward pass of your DLR303 GPT and places its top 15 kernels on a measured roofline.

**Acceptance criteria**
- Measured bandwidth and matmul throughput are reported with method, and compared with the datasheet (for a T4: 320+ GB/s and 65 FP16 TFLOPS).
- Each of the 15 kernels has measured FLOPs, bytes, achieved throughput and a classification (compute, memory or overhead bound), with the Nsight Compute metric that supports it.
- The report predicts which single optimisation would help most, implements it (for example `torch.compile` or a larger batch), and measures the actual gain.
- The script reproduces all figures with one command.

**Compute budget.** ≤ 2 GPU-hours on a free T4.

**Stretch goals.** Repeat on a second GPU generation and explain which ops moved category.

**What it proves to an employer.** You reason about performance from measurements, not guesses.

### P2 · A Triton kernel pack for LLM training (L2, ~15 hours)

**Real-world inspiration.** Liger Kernel reports about 20% higher throughput and 60% lower memory than standard Hugging Face implementations by fusing operations and chunking the loss (Hsu et al., 2024). Teams maintain such kernels because frameworks do not fuse everything.

**What to build.** Three Triton kernels with forward and backward passes, each wrapped in `torch.autograd.Function`: (1) fused residual-add + RMSNorm; (2) SwiGLU; (3) chunked linear + cross-entropy that never materialises the full logits. Integrate them into your GPT.

**Acceptance criteria**
- Correctness: outputs and gradients match PyTorch within stated tolerances for fp32 and fp16 (and bf16 where the hardware supports it) on 500 random shapes, including non-power-of-two hidden sizes and non-contiguous inputs; `torch.autograd.gradcheck` passes in fp64 for small shapes.
- Speed: each kernel is faster than PyTorch eager at the stated shapes on your GPU (target ≥ 1.3×), and is compared honestly with `torch.compile`.
- Memory: the cross-entropy kernel cuts peak memory of the loss computation by ≥ 50% for a 128k vocabulary at a stated batch and sequence length.
- End-to-end: a 2,000-step training run with your kernels matches the reference loss curve within seed noise, and tokens per second is reported.

**Compute budget.** ≤ 10 GPU-hours, including the end-to-end training check.

**Stretch goals.** Add rotary embedding and a fused AdamW update; package as a pip-installable module with CI on CPU (interpreter mode) for tests.

**What it proves to an employer.** You can write production-style kernels with the testing discipline that makes them safe to adopt.

### P3 · FlashAttention-style attention with forward and backward passes (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** FlashAttention made exact attention IO-aware (Dao et al., 2022) and has been redesigned for each GPU generation since (FA2 in 2023, FA3 for Hopper in 2024, FA4 for Blackwell in 2026). Meanwhile, AI-generated kernels have both beaten experts (RE-Bench, 2024) and faked results through harness exploits (Sakana AI, 2025), so adversarial testing is part of the job.

**What to build.** A Triton attention kernel with:
1. a forward pass with online softmax, causal masking and grouped-query attention (shared K/V heads);
2. a backward pass with recomputation (no stored attention matrix);
3. support for variable sequence lengths in a batch (padding masks or packed sequences);
4. integration into your GPT through a custom `autograd.Function`;
5. an "AI-kernel audit" appendix: ask an agent to write the same kernel, run your full test suite on it, and document what it got wrong.

**Acceptance criteria**
- Correctness: forward and gradients match a float32 PyTorch reference on 1,000 random configurations (batch, heads, KV heads, head dims 64/128, sequence lengths including non-multiples of the block size, causal and non-causal), with tolerances stated per dtype; tests also randomise call order and use fresh output buffers.
- Memory: peak memory grows linearly, not quadratically, with sequence length up to at least 8k tokens (plot).
- Speed: faster than PyTorch's math attention backend at sequence lengths ≥ 1k on your GPU; compared honestly with `scaled_dot_product_attention`'s best available backend, with a short explanation of any gap.
- End-to-end: training your GPT for 2,000 steps with your kernel matches the reference loss curve within seed noise.
- A write-up explaining the tiling, the IO argument and the profiler evidence (Nsight Compute metrics) for your main bottleneck.
- Compute ≤ 20 GPU-hours on a T4 or better; the GPU is stated for every number.

**Stretch goals.** Sliding-window attention; an FP8 path on Hopper-class hardware; a paged-KV decode kernel.

**What it proves to an employer.** You can build and verify one of the most important kernels in modern AI, and you know how to audit AI-written performance code. This is a direct signal for GPU performance engineer and research-engineer roles.

## Feeds into

- [DLR501 Frontier Seminar](../../year_5/DLR501_frontier_seminar_interpretability_reasoning/README.md): test-time compute and scaling are bounded by the efficiency covered here.
- [MLE404 Efficient Inference: Quantization, Distillation and Compilers](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md): production inference toolchains.
- [MLE402 Distributed Training and Large-Scale ML](../../../machine_learning_engineering/year_4/MLE402_distributed_training_and_large_scale_ml/README.md): parallelism at cluster scale.
- [OV04 MLOps and ML Platform Engineering](../../../../04_overlaps/OV04_mlops_ml_platform/README.md): GPU capacity planning and serving platforms.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): kernel and systems research topics.
