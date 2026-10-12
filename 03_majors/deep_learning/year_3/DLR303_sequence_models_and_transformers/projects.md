# DLR303 · Labs and projects

Every lab and project ships with code, unit tests (shapes, causal-mask leak test, parameter-count test), training logs, and a write-up with bits-per-byte numbers and seeds. Free Kaggle (2× T4) or Colab GPUs are enough for everything here.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Count models, MLP language model and RNNs | Bigram and trigram count models and a Bengio-style MLP language model; then a character RNN and LSTM with gradient-norm tracking and clipping | Bits per byte for all models on one held-out split; gradient-norm plots linked to the vanishing-gradient argument | 7 h |
| 2 · Attention and the leak test | Additive and scaled dot-product attention; causal and padding masks | Leak test that perturbs token t and asserts no earlier output changes; alignment plots | 3 h |
| 3 · The block | Multi-head attention, pre-norm residual block, SwiGLU, RMSNorm | Match `F.scaled_dot_product_attention`; parameter count matches your formula | 4 h |
| 4 · Positions | Sinusoidal, learned and RoPE; position interpolation | Loss vs position at 1× and 2× training length for each scheme | 4 h |
| 5 · Tokenizer audit | Train byte-level BPE; compare with GPT-2 and two open-model tokenizers | Fertility and bytes-per-token for English, Hindi, Bengali, Tamil, Hinglish | 4 h |
| 6 · GPT training | nanoGPT-style model on Tiny Shakespeare, then on a 200M-token FineWeb-Edu sample | Curves, bits per byte, samples, and a config file that reproduces the run | 6 h |
| 7 · KV cache and GQA | Cached decoding; grouped-query attention; speculative decoding with a small draft | Token-by-token equality with uncached outputs; speed and memory at 1k/4k tokens | 4 h |
| 8 · Mixture-of-experts | Top-2 routed MLP with a load-balancing loss | Expert-load histograms with and without the auxiliary loss; quality at equal active parameters | 4 h |
| 9 · Scaling sweep | 5 model sizes × 3 token budgets; fit a power law | Fitted law, residuals, and a prediction for an unseen size made before training it | 6 h |
| 10 · Attention vs state-space model | Small transformer and a Mamba-style model on copy and associative-recall tasks | Accuracy vs sequence length and distance; a short explanation | 4 h |

## Projects

### P1 · A fair tokenizer for Indian languages (L1, ~6 hours)

**Real-world inspiration.** Petrov et al. (2023) showed that the same content can need up to 15× more tokens in some languages, which raises cost and shortens the usable context for those users. Many people in India type in mixed scripts or romanised text (Hinglish), which makes the problem worse.

**What to build.** A byte-level BPE tokenizer (pure Python training, with an optional fast encoder) trained on a balanced mix of English, Hindi, Bengali, Tamil and romanised Hindi drawn from FineWeb2 or another openly licensed corpus. Compare it with GPT-2's tokenizer and with two recent open-model tokenizers.

**Acceptance criteria**
- Encoding and decoding are lossless on 100% of a 10,000-line test set that includes emoji, URLs, numbers, mixed scripts and Unicode normalisation edge cases.
- Fertility (tokens per word) and bytes per token are reported per language for all four tokenizers, on parallel or comparable text.
- The worst-to-best fertility ratio across the five languages is lower for your tokenizer than for GPT-2's, at an equal or smaller vocabulary size.
- Training is deterministic (the same merges file from the same input and seed) and documented.

**Compute budget.** CPU only; tokenizer training on ≤ 1 GB of text.

**Stretch goals.** Add digit splitting and measure arithmetic accuracy downstream in P2; train a SentencePiece unigram model and compare.

**What it proves to an employer.** You understand a part of the LLM stack that most people ignore, and you can measure its effect on real users.

### P2 · A small GPT for Hindi trained from scratch (L2, ~15 hours)

**Real-world inspiration.** Indian-language model efforts such as Sarvam's open models (Apache 2.0, 2026) and AI4Bharat's datasets show demand for models trained with Indian languages in mind. FineWeb2 provides cleaned web text for more than a thousand languages, including Hindi (Penedo et al., 2025).

**What to build.** A 10–40M-parameter decoder-only transformer (RoPE, RMSNorm, SwiGLU, tied embeddings) trained on Hindi text from FineWeb2 with your P1 tokenizer. Include a KV-cache sampler and an evaluation script.

**Acceptance criteria**
- Unit tests pass: causal leak test, cached vs uncached equality, parameter count matching your formula.
- Validation bits per byte beats a smoothed character 5-gram baseline and is reported over 3 seeds.
- Training uses ≤ 8 GPU-hours on Kaggle 2× T4; throughput (tokens per second) and the share of time in data loading are reported.
- KV-cache decoding is at least 3× faster than uncached decoding at 512 generated tokens.
- 30 samples at two temperatures with a short qualitative analysis written by someone who reads Hindi (or with that limitation stated).

**Stretch goals.** Mixed Hindi–English training and a code-switching analysis; GQA vs full multi-head attention at equal parameters.

**What it proves to an employer.** You can take a model from tokenizer to trained checkpoint, with tests that rule out the common silent bugs.

### P3 · A mini scaling-law study (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Kaplan et al. (2020) and Chinchilla (Hoffmann et al., 2022) turned model sizing into a predictive science, and nanochat sets all hyperparameters from a single depth setting to train a "miniseries" of compute-optimal models (nanochat README, 2026). Labs decide what to train at large scale by fitting small runs first.

**What to build.** A reproducible study on FineWeb-Edu (or your P2 Hindi corpus):
1. at least 4 model sizes (about 2M to 40M non-embedding parameters) at 3 compute budgets each, in an isoFLOP design;
2. fitted loss as a function of parameters and tokens, with uncertainty from bootstrap over runs;
3. a pre-registered prediction (committed to git before training) of the optimal size and loss at a budget 4× larger than your largest;
4. the prediction tested with one run at that budget.

**Acceptance criteria**
- At least 12 completed runs with identical data order rules, warmup and decay; all configs are generated by one script.
- The fitted optimal tokens-per-parameter ratio is reported with a confidence interval and compared with Chinchilla's roughly 20, with reasons for any difference (scale, tokenizer, schedule, embeddings counted or not).
- The held-out prediction's loss error is reported; a prediction within 2% of the measured loss is a strong result, and a miss must be explained.
- Total compute ≤ 30 GPU-hours (T4-equivalent), accounted per run.
- A write-up in paper format (4–6 pages) with an honest limitations section.

**Stretch goals.** Repeat with two learning-rate schedules (cosine vs warmup–stable–decay) and show whether the fitted law changes; add a data-repetition axis following Muennighoff et al. (2023).

**What it proves to an employer.** You can design an experiment that predicts the outcome of an expensive run, which is how pretraining teams decide what to train.

## Feeds into

- [DLR401 Large Language Models](../../year_4/DLR401_large_language_models_pretraining_fine_tuning/README.md): your GPT, tokenizer and scaling study become the base for pretraining, fine-tuning and alignment.
- [DLR403 Reinforcement Learning, Including RL for Language Models](../../year_4/DLR403_reinforcement_learning_including_rl_for_language/README.md): the formal follow-on; language models become RL policies.
- [DLR402 Multimodal Models](../../year_4/DLR402_multimodal_models/README.md): transformers over image, audio and video tokens.
- [DLR404 Efficient Deep Learning and GPU Programming](../../year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md): FlashAttention-style kernels and KV-cache efficiency.
- [DLR501 Frontier Seminar](../../year_5/DLR501_frontier_seminar_interpretability_reasoning/README.md): induction heads and scaling laws reappear in interpretability and scaling research.
