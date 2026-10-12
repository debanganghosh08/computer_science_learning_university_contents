# DLR404 · Efficient Deep Learning and GPU Programming

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L2 → L4 | [DLR304](../../year_3/DLR304_training_deep_networks_optimization/README.md); in practice also [CS202](../../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md) and [DLR303](../../year_3/DLR303_sequence_models_and_transformers/README.md) | [DLR501](../../year_5/DLR501_frontier_seminar_interpretability_reasoning/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md); taken alongside [DLR403](../DLR403_reinforcement_learning_including_rl_for_language/README.md) |

## Why this course matters now

Compute is the scarcest input in deep learning, and a kernel that wastes half the GPU wastes half the budget. FlashAttention showed that rethinking memory traffic, not arithmetic, could make exact attention several times faster (Dao et al., 2022). Each GPU generation since has needed a new design. FlashAttention-3 targets Hopper's asynchronous tensor cores and FP8 (2024). FlashAttention-4 targets Blackwell, where "tensor core throughput doubles while other functional units ... scale more slowly". It reaches 1,613 TFLOPs/s (71% utilisation) on B200 and is written in a Python-embedded DSL (Zadouri et al., 2026). Triton lets researchers write fused kernels in Python, and LinkedIn's Liger kernels report about 20% higher training throughput and 60% less memory than standard Hugging Face implementations (Hsu et al., 2024). AI now writes kernels too, with mixed results. On METR's RE-Bench an agent "wrote a faster custom Triton kernel than any of our human experts" (Wijk et al., 2024). On KernelBench, frontier models matched the PyTorch baseline in "less than 20% of the cases" (Ouyang et al., 2025). Sakana AI withdrew claims of up to 100× speed-ups after its system was found exploiting the evaluation code (TechCrunch, 2025). Writing kernels, testing them adversarially and profiling honestly is a scarce specialism, the GPU performance engineer, and every research engineer needs its basics. This course stays at the kernel and memory level. Production inference toolchains are covered in [MLE404](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md), and large-scale parallelism in [MLE402](../../../machine_learning_engineering/year_4/MLE402_distributed_training_and_large_scale_ml/README.md).

## Learning outcomes

By the end you can:

1. **Classify** any operation as compute-, memory- or overhead-bound with a roofline model, using measured hardware numbers.
2. **Explain** GPU architecture (SMs, warps, tensor cores, the memory hierarchy, occupancy) and how Hopper and Blackwell change kernel design.
3. **Profile** training and inference with `torch.profiler`, Nsight Systems and Nsight Compute, and **attribute** time and memory to specific kernels.
4. **Write** CUDA kernels (coalescing, shared-memory tiling) and Triton kernels (fused softmax, normalisation, matmul, attention), with forward and backward passes.
5. **Implement** FlashAttention-style tiled attention with online softmax, and **verify** it against a reference.
6. **Apply** low precision (bf16, FP8, int8/int4 weight-only) and structured sparsity, and **measure** the accuracy–speed trade-off.
7. **Budget** memory for training (weights, gradients, optimizer states, activations) and **reduce** it with checkpointing, sharding and fused kernels.
8. **Audit** AI-written kernels with adversarial correctness tests and honest benchmarks.

## Chapters and lessons

### Chapter 1 · Where time goes (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 FLOPs and bytes | Arithmetic intensity; FLOPs of matmul, softmax, layer norm | Compute intensity for 10 common ops |
| 1.2 The roofline model | Peak compute, peak bandwidth, ridge point (Williams et al., 2009) | Draw the T4 roofline: 65 FP16 tensor TFLOPS, 320 GB/s (NVIDIA datasheet) |
| 1.3 Three regimes | Compute-bound, memory-bound, overhead-bound ("Making Deep Learning Go Brrrr", He, 2022) | Classify a GPT training step's ops; check with timing |
| 1.4 Utilisation metrics | MFU vs HFU; achieved occupancy; why 100% is impossible | Compute MFU of your DLR303 GPT on a T4 |

**Check your understanding:** Why is layer norm memory-bound while a large matmul is compute-bound? Why does a model run slower than its FLOP count predicts at small batch sizes? What does MFU ignore?

### Chapter 2 · GPU architecture (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Execution model | SMs, warps of 32 threads, SIMT, divergence, latency hiding | Measure the cost of warp divergence in a toy kernel |
| 2.2 Memory hierarchy | Registers, shared memory/L1, L2, HBM/GDDR; bandwidth and latency at each level | Bandwidth microbenchmark: copy kernel vs `cudaMemcpy` |
| 2.3 Tensor cores | Matrix-multiply-accumulate units; supported precisions per generation (T4: FP16/INT8; Ampere adds BF16 and 2:4 sparsity) | Matmul throughput in fp32 vs fp16 on a T4 |
| 2.4 Hopper and Blackwell | TMA, warp specialisation, FP8 (Hopper); FP4 and tensor memory (Blackwell); asymmetric scaling | Read the FA3 and FA4 abstracts; list each hardware feature they exploit |

**Check your understanding:** Why does a warp-divergent branch halve throughput? Why can occupancy be low and performance still high? Why did each new GPU generation need a new FlashAttention?

### Chapter 3 · Profiling (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Timing correctly | Asynchronous execution, CUDA events, warm-up, synchronisation | Show a 100× timing error from missing synchronisation |
| 3.2 PyTorch profiler | Operator and kernel views, trace export, memory timeline | Profile one GPT training step; top 10 kernels |
| 3.3 Nsight Systems and Nsight Compute | Timelines, CPU gaps, launch overhead; per-kernel memory throughput and stall reasons | Find a CPU-bound gap and a memory-bound kernel |
| 3.4 Memory snapshots | Allocator behaviour, fragmentation, `torch.cuda.memory` snapshots | Explain your peak memory allocation by allocation |

**Check your understanding:** Why does a timeline full of small kernels suggest overhead-bound work? What does Nsight Compute's "memory throughput 90% of peak" tell you about optimisation headroom? Why can peak memory exceed the sum of tensors you know about?

### Chapter 4 · CUDA basics (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Kernels and grids | Threads, blocks, grids, indexing, bounds checks | Vector add; 2-D elementwise op |
| 4.2 Coalescing | Contiguous access per warp; strided access penalties | Transpose: naive vs shared-memory tiled |
| 4.3 Tiled matmul | Shared-memory tiling, register blocking; Simon Boehm's worklog | Naive → coalesced → tiled matmul; GFLOPS vs cuBLAS |
| 4.4 Integration | PyTorch C++/CUDA extensions with `load_inline`; streams | Call your kernel from PyTorch; test against `torch.matmul` |

**Check your understanding:** Why does a naive transpose run far below peak bandwidth? What limits a tiled matmul before it reaches cuBLAS speed? Why are bounds checks needed even when you "know" the size?

### Chapter 5 · Triton (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Programming model | Programs operating on blocks; `tl.load`/`tl.store` with masks; `constexpr` block sizes | Triton puzzles 1–8 |
| 5.2 Fused elementwise and reductions | Fusing to avoid HBM round trips; fused softmax | Fused softmax faster than PyTorch eager on a T4 |
| 5.3 Normalisation forward and backward | Layer norm and RMSNorm with saved statistics; atomic vs two-pass reductions for weight gradients | RMSNorm fwd/bwd in Triton with a custom `autograd.Function` |
| 5.4 Matmul in Triton | `tl.dot`, tiling, grouped ordering for L2 reuse, autotuning | Match the official tutorial's performance on your GPU |
| 5.5 Kernels for LLM training | Liger's fused linear-cross-entropy (chunking to avoid materialising logits) | Chunked cross-entropy for a 128k vocabulary; memory before/after |

**Check your understanding:** Why does fusing a chain of elementwise ops speed it up even though FLOPs are unchanged? Why is a fused linear-plus-cross-entropy kernel such a large memory saving for big vocabularies? When should you not write a custom kernel?

### Chapter 6 · Fusion and compilers (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 `torch.compile` | TorchDynamo graph capture, TorchInductor code generation (Triton on GPU), guards and recompiles | Compile your GPT; read the generated Triton |
| 6.2 Graph breaks | Python constructs that break graphs; how to find and remove them | Remove 3 graph breaks; measure the gain |
| 6.3 Launch overhead | CUDA graphs; small-batch decoding | CUDA graphs for decode; tokens per second before/after |
| 6.4 Compiler vs hand-written | Where compilers win (elementwise chains) and lose (attention, novel algorithms) | Compare compiled vs hand-written RMSNorm |

**Check your understanding:** Why does `torch.compile` sometimes make the first steps slower? Why do CUDA graphs help decoding much more than training? What does a compiler not know that you do?

### Chapter 7 · Attention kernels (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Online softmax | Running max and sum in one pass (Milakov and Gimelshein, 2018) | Prove its correctness; implement in NumPy |
| 7.2 FlashAttention | Tiling Q, K, V into SRAM; never materialising the N×N matrix; recomputation in backward; IO complexity (Dao et al., 2022) | Triton forward pass following the official fused-attention tutorial |
| 7.3 FA2, FA3, FA4 | Work partitioning across warps (FA2); asynchrony and FP8 on Hopper (FA3); Blackwell pipelines and software exponentials (FA4) | Benchmark `scaled_dot_product_attention` backends on your GPU |
| 7.4 Serving-side attention | Paged KV cache (Kwon et al., 2023); variable-length batches | Implement a toy paged KV-cache allocator |

**Check your understanding:** Why is FlashAttention exact rather than approximate? Where does its backward pass get the attention matrix from? Why does paging the KV cache raise serving throughput?

### Chapter 8 · Low-precision arithmetic (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Formats | fp16, bf16, FP8 E4M3/E5M2, microscaling (MX) formats with shared block scales (Rouhani et al., 2023) | Quantise a tensor to each; plot error distribution |
| 8.2 Scaling granularity | Per-tensor, per-channel, per-group, per-block; outliers | Show one outlier channel ruining per-tensor int8 |
| 8.3 Weight-only quantisation | GPTQ (Frantar et al., 2022), AWQ (Lin et al., 2023); dequantise-in-kernel | Triton int4 weight-only matmul with group scales; accuracy and speed |
| 8.4 Activation quantisation | LLM.int8() outlier decomposition (Dettmers et al., 2022); SmoothQuant (Xiao et al., 2022) | SmoothQuant-style rescaling on a small model; perplexity before/after |

**Check your understanding:** Why does weight-only int4 speed up decoding but not large-batch prefill? Why do activation outliers make int8 hard, and how does SmoothQuant move the difficulty? What do block scales in MX formats buy?

### Chapter 9 · Sparsity and pruning (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Kinds of sparsity | Unstructured vs structured; 2:4 semi-structured on Ampere-and-later tensor cores (Mishra et al., 2021) | Measure dense vs 2:4 sparse matmul on an Ampere-or-newer GPU (cloud credits or a lab machine) |
| 9.2 One-shot pruning of LLMs | SparseGPT (Frantar and Alistarh, 2023), Wanda (Sun et al., 2023) | Wanda-prune a small LM to 50%; perplexity vs dense |
| 9.3 Conditional computation | Mixture-of-experts as sparsity; routing kernels | Profile an MoE layer: routing, permutation and expert matmuls |
| 9.4 Distillation in brief | Training a small student on a large teacher's outputs (Hinton et al., 2015); when to distil rather than prune (toolchains in MLE404) | Distil your GPT into a half-width student; compare with 50% pruning at equal size |

**Check your understanding:** Why does unstructured sparsity rarely speed things up on GPUs? Why does 2:4 sparsity need hardware support? When is MoE cheaper than a dense model, and when is it not?

### Chapter 10 · Memory-efficient training (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The memory budget | Weights, gradients, master weights, optimizer states, activations, temporary buffers | Predict peak memory of a 1B model step; measure |
| 10.2 Activation checkpointing | Selective recomputation; which layers to checkpoint | Find the best checkpointing policy for your GPT |
| 10.3 Optimizer memory | 8-bit optimizer states; sharding with ZeRO and FSDP; CPU offload | Fit the largest model you can on 2× T4 |
| 10.4 Kernel-level savings | Fused cross-entropy, fused norms, in-place operations | Combine savings; report each one's share |

**Check your understanding:** Why do Adam's two moments often dominate memory for small models and activations for large-context ones? What is the compute cost of full checkpointing? Why does CPU offload hurt throughput on PCIe-connected GPUs?

### Chapter 11 · Distributed basics and communication (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Collectives | All-reduce, reduce-scatter, all-gather; ring and tree algorithms; NCCL | Measure bus bandwidth with `nccl-tests` or `torch.distributed` on 2× T4 |
| 11.2 Parallelism overview | Data, tensor (Megatron-LM, Shoeybi et al., 2019), pipeline, sequence and expert parallelism | Compute communication volume per step for each |
| 11.3 Overlap | Overlapping gradient all-reduce with backward compute; bucketing | Show the overlap in an Nsight Systems trace |
| 11.4 Planning at scale | *How to Scale Your Model*; Hugging Face's *Ultra-Scale Playbook* | Plan the parallelism for a 7B model on 64 GPUs |

**Check your understanding:** Why does tensor parallelism need fast intra-node links while data parallelism tolerates slower networks? How much data does a ring all-reduce move per GPU? What is the pipeline "bubble", and how is it reduced?

### Chapter 12 · Inference efficiency and AI-written kernels (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Prefill and decode | Compute-bound prefill vs memory-bound decode; batching; continuous batching | Throughput vs batch size for your GPT |
| 12.2 Speculative decoding and KV quantisation | Draft models (Leviathan et al., 2022); quantised KV caches | Speculative decoding speed-up vs acceptance rate |
| 12.3 AI-written kernels | KernelBench's `fast_p` metric; RE-Bench's Triton result; the Sakana harness exploit | Ask an agent for a fused kernel; attack it with adversarial tests |
| 12.4 Honest benchmarking | Fixed shapes and dtypes, warm-up, clocks, comparing against the right baseline | Benchmark checklist applied to your P3 kernel |

**Check your understanding:** Why does decoding speed scale with memory bandwidth rather than FLOPs? How could a kernel pass a correctness check yet be wrong in use? What makes a speed-up claim trustworthy?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Roofline and microbenchmarks | **P1 starts** |
| 2 | 2 | Lab 1 (cont.) | **P1 due** |
| 3 | 3 | Lab 2 · Profiling a training step | Profile report |
| 4 | 4 | Lab 3 · CUDA transpose and matmul | GFLOPS vs cuBLAS |
| 5 | 5 | Lab 4 · Triton kernels | — |
| 6 | 5 | Lab 4 (cont.) | — |
| 7 | 6 | Lab 5 · `torch.compile` and CUDA graphs | — |
| 8 | 7 | Lab 6 · FlashAttention forward in Triton | Mid-term (AI off) |
| 9 | 8 | Lab 7 · Quantised matmul | **P2 due** |
| 10 | 9 | Lab 8 · Pruning and MoE profiling | — |
| 11 | 10 | Lab 9 · Memory and communication on 2× T4 | Predicted vs measured memory |
| 12 | 11 | Lab 9 (cont.) | — |
| 13 | 12 | Lab 10 · Audit an AI-written kernel | Audit report |
| 14 | 12 | Project studio | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** first drafts of kernels you will then test; explaining Nsight metrics; writing benchmark harnesses and plots; translating CUDA examples to Triton and back; searching for tuning parameters (with your harness as judge).
- **Do without AI (drills):** roofline and arithmetic-intensity calculations; memory budgets; the online-softmax derivation; writing a tiled matmul and a fused softmax from memory in timed sessions; both exams.
- **Verify AI output by:** (1) comparing every kernel with a PyTorch reference on hundreds of random shapes, including non-power-of-two sizes, size 1, non-contiguous and transposed inputs, and every supported dtype; (2) checking results with fresh output buffers and randomised call order, so a kernel cannot pass by reusing a previous result; (3) benchmarking with warm-up, synchronisation and fixed clocks against the strongest available baseline (cuBLAS, `scaled_dot_product_attention`, `torch.compile`); (4) running an end-to-end training run and comparing loss curves.
- **Where AI still fails here:** KernelBench measured frontier models matching the PyTorch baseline in under 20% of tasks at release (2025), and the Sakana case showed generated kernels passing a weak evaluation by exploiting it. RE-Bench shows the opposite as well: an agent beat every human expert on one Triton task. Both are true, so the tests decide. In Lab 10 you document what your adversarial tests caught in AI-written kernels.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) and oral defence of P3 | 30% |

**Mastery gate.** You pass when you can: (1) with AI off, place any operation on a roofline, write a memory budget for a training run, and write a correct fused softmax in Triton in 45 minutes; (2) deliver a Triton kernel with forward and backward passes that is faster than PyTorch eager on stated shapes and passes an adversarial correctness suite; (3) explain a profiler trace of an unfamiliar model and name its top two bottlenecks in an oral exam.

## Industry reality

Kernel work is visible in public repositories: FlashAttention (Dao-AILab), ThunderKittens (Spector et al., 2024), Liger Kernel (LinkedIn), and Triton itself, used inside PyTorch's compiler. The DLR market page describes the GPU performance engineer as a separate specialism that "writes kernels in CUDA or Triton and optimises training and inference" ([DLR market page](../../../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md)). Interviews test roofline reasoning, memory budgets, profiling stories and live kernel writing.

**Interview questions from this course**

1. *This model trains at 25% MFU. How do you find out why?* Strong answer: profile first (timeline for CPU gaps and launch overhead; kernel table for top time); classify bottlenecks with a roofline; check data loading, small kernels, communication stalls and precision; fix the largest and re-measure.
2. *Explain FlashAttention.* Strong answer: standard attention is memory-bound because it writes the N×N matrix to HBM; tiling plus online softmax keeps blocks in SRAM; recomputation in backward; exact results; IO complexity argument; newer versions exploit hardware asynchrony and low precision.
3. *Write a fused softmax kernel and tell me how you would test it.* Strong answer: one row per program, max-subtraction, masking for non-power-of-two widths; tests with random shapes, extreme values, fp16/bf16, non-contiguous inputs; benchmark against PyTorch with synchronisation.
4. *How much memory to fine-tune this model, and how would you halve it?* Strong answer: per-parameter bytes for weights, gradients, master weights and Adam states; activation estimate; checkpointing, 8-bit optimizer, sharding, LoRA, fused loss kernels; trade-offs in speed.
5. *Why does int4 weight-only quantisation speed up chat decoding but not batch-1024 prefill?* Strong answer: decode is memory-bound so fewer weight bytes help; large-batch prefill is compute-bound and dequantisation adds work; activation quantisation needed for compute-bound speed-ups.

## Resources (free first)

- **Courses and lectures:** GPU MODE lectures — https://github.com/gpu-mode/lectures ; MIT 6.5940 TinyML and Efficient Deep Learning Computing — https://efficientml.ai/ ; Stanford CS336 (systems assignment) — https://cs336.stanford.edu/
- **Guides:** Horace He, "Making Deep Learning Go Brrrr From First Principles" — https://horace.io/brrr_intro.html ; Modal GPU Glossary — https://modal.com/gpu-glossary ; Simon Boehm, "How to Optimize a CUDA Matmul Kernel" — https://siboehm.com/articles/22/CUDA-MMM ; *How to Scale Your Model* — https://jax-ml.github.io/scaling-book/ ; *The Ultra-Scale Playbook* — https://huggingface.co/spaces/nanotron/ultrascale-playbook
- **Documentation:** CUDA Programming Guide — https://docs.nvidia.com/cuda/cuda-programming-guide/ ; Triton tutorials — https://triton-lang.org/main/getting-started/tutorials/index.html ; `torch.compile` — https://docs.pytorch.org/docs/stable/torch.compiler.html ; PyTorch CUDA memory snapshots — https://docs.pytorch.org/docs/stable/torch_cuda_memory.html ; Nsight Systems — https://docs.nvidia.com/nsight-systems/ ; Nsight Compute — https://docs.nvidia.com/nsight-compute/
- **Practice:** Sasha Rush's GPU Puzzles — https://github.com/srush/GPU-Puzzles and Triton Puzzles — https://github.com/srush/Triton-Puzzles ; LeetGPU — https://leetgpu.com/ ; KernelBench — https://github.com/ScalingIntelligence/KernelBench
- **Code:** FlashAttention — https://github.com/Dao-AILab/flash-attention ; Liger Kernel — https://github.com/linkedin/Liger-Kernel ; ThunderKittens — https://github.com/HazyResearch/ThunderKittens ; `nccl-tests` — https://github.com/NVIDIA/nccl-tests
- **Key papers:** FlashAttention https://arxiv.org/abs/2205.14135 ; FlashAttention-2 https://arxiv.org/abs/2307.08691 ; FlashAttention-3 https://arxiv.org/abs/2407.08608 ; FlashAttention-4 https://arxiv.org/abs/2603.05451 ; online softmax https://arxiv.org/abs/1805.02867 ; PagedAttention https://arxiv.org/abs/2309.06180 ; LLM.int8() https://arxiv.org/abs/2208.07339 ; GPTQ https://arxiv.org/abs/2210.17323 ; AWQ https://arxiv.org/abs/2306.00978 ; SmoothQuant https://arxiv.org/abs/2211.10438 ; Microscaling formats https://arxiv.org/abs/2310.10537 ; SparseGPT https://arxiv.org/abs/2301.00774 ; Wanda https://arxiv.org/abs/2306.11695 ; ZeRO https://arxiv.org/abs/1910.02054 ; Megatron-LM https://arxiv.org/abs/1909.08053 ; KernelBench https://arxiv.org/abs/2502.10517
- **Paid, optional:** Hwu, Kirk and El Hajj, *Programming Massively Parallel Processors*, 4th ed. (2022). The free resources above cover most of it.
- **Compute (free):** a Colab or Kaggle T4 runs CUDA and Triton labs (T4 is Turing: FP16 tensor cores, no BF16 tensor cores, no 2:4 sparsity, no FP8). For Ampere/Hopper-only features, use a short rented session or a university machine, and say which GPU produced each number.

## Sources

- Dao et al., "FlashAttention" (2022) — https://arxiv.org/abs/2205.14135 ; Shah et al., "FlashAttention-3" (2024) — https://arxiv.org/abs/2407.08608 ; Zadouri et al., "FlashAttention-4" (Mar 2026) — https://arxiv.org/abs/2603.05451 (checked 2026-10)
- Hsu et al., "Liger Kernel: Efficient Triton Kernels for LLM Training" (2024) — https://arxiv.org/abs/2410.10989 (checked 2026-10)
- Wijk et al., "RE-Bench" (2024) — https://arxiv.org/abs/2411.15114 ; Ouyang et al., "KernelBench" (Feb 2025) — https://arxiv.org/abs/2502.10517 (checked 2026-10)
- TechCrunch, "Sakana walks back claims that its AI can dramatically speed up model training" (21 Feb 2025) — https://techcrunch.com/2025/02/21/sakana-walks-back-claims-that-its-ai-can-dramatically-speed-up-model-training/ (checked 2026-10)
- NVIDIA T4 specifications (65 FP16 TFLOPS mixed precision, 16 GB GDDR6, 320+ GB/s) — https://www.nvidia.com/en-us/data-center/tesla-t4/ (checked 2026-10)
- Williams, Waterman and Patterson, "Roofline: an insightful visual performance model for multicore architectures", *Communications of the ACM* (2009) — https://doi.org/10.1145/1498765.1498785 ; free copy — https://people.eecs.berkeley.edu/~kubitron/cs252/handouts/papers/RooflineVyNoYellow.pdf (checked 2026-10)

_Last reviewed: 2026-10_
