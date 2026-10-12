# DLR303 · Sequence Models and Transformers

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L4 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS206](../../../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md) | [DLR403](../../year_4/DLR403_reinforcement_learning_including_rl_for_language/README.md); taken alongside [DLR301](../DLR301_neural_networks_from_scratch_autograd/README.md) and [DLR302](../DLR302_computer_vision_from_cnns_to_vision_transformers/README.md); prepares for [DLR401](../../year_4/DLR401_large_language_models_pretraining_fine_tuning/README.md) and [DLR402](../../year_4/DLR402_multimodal_models/README.md) |

## Why this course matters now

The transformer (Vaswani et al., 2017) is the architecture behind language models, most modern vision encoders, speech recognisers and many protein and weather models. Its details keep evolving while the core stays the same. Recent open models use rotary position embeddings, RMSNorm, SwiGLU, grouped-query or latent attention and mixture-of-experts layers. DeepSeek-V2's multi-head latent attention cut the KV cache by 93.3% compared with DeepSeek 67B (DeepSeek-AI, 2024). Building a GPT from scratch is now a weekend project: Karpathy's nanochat trains a GPT-2-capability model for about $48 of rented GPU time, about 2 hours on an 8×H100 node (nanochat README, 2026). Coding assistants write a transformer block from memory. They also make the classic errors: a missing causal mask, the wrong head reshape, position embeddings applied after attention. A model with any of these still trains, and the bug often leaks future tokens into training. Engineers who know the block line by line, can derive KV-cache memory, and can predict loss from a scaling law are the ones trusted with real training runs.

## Learning outcomes

By the end you can:

1. **Implement** a decoder-only transformer from scratch (attention, multi-head reshape, RoPE, RMSNorm, SwiGLU, weight tying) and **test** it for causality and shape correctness.
2. **Explain** why attention replaced recurrence, using vanishing gradients, parallelism and path length.
3. **Train** a byte-level BPE tokenizer and **measure** its fertility and fairness across English and Indian languages.
4. **Train** a small GPT end to end, **evaluate** it with bits per byte, and **sample** from it with temperature, top-k and top-p.
5. **Derive** parameter counts, FLOPs per token and KV-cache memory, and **implement** a KV cache, grouped-query attention and a mixture-of-experts layer.
6. **Fit** a simple scaling law from your own runs and **predict** the loss of a larger run before training it.
7. **Compare** attention with state-space and linear-attention alternatives on a controlled task.
8. **Audit** generated transformer code for masking, shape and positional-encoding errors.

## Chapters and lessons

### Chapter 1 · Language modelling basics (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Autoregressive factorisation | p(x₁…xₙ) = ∏ p(xₜ \| x<ₜ); teacher forcing | Count-based bigram model on a names dataset |
| 1.2 Measuring a language model | Cross-entropy, perplexity, bits per byte (tokenizer-independent) | Convert between the three for 3 models |
| 1.3 Smoothing and n-grams | Add-k, backoff; why counts do not generalise | Trigram with add-k; tune k on validation |
| 1.4 Neural language models | Embeddings plus MLP over a fixed context (Bengio et al., 2003) | Beat the trigram with an MLP language model |

**Check your understanding:** Why is bits per byte fairer than perplexity when comparing models with different tokenizers? What does a perplexity of 1 mean, and what bug usually causes it? Why can an n-gram model not share statistics between "cat sat" and "dog sat"?

### Chapter 2 · Recurrent networks, briefly (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 RNNs and BPTT | Hidden state recurrence; backpropagation through time; truncation | Character RNN on Tiny Shakespeare |
| 2.2 Vanishing and exploding gradients | Products of Jacobians (Pascanu et al., 2013); gradient clipping | Plot gradient norm vs time step |
| 2.3 LSTM and GRU | Gates and the additive cell path (Hochreiter and Schmidhuber, 1997) | LSTM vs RNN on a long-range copy task |
| 2.4 Sequence-to-sequence | Encoder–decoder (Sutskever et al., 2014); the fixed-vector bottleneck | Reverse-a-string seq2seq; accuracy vs length |

**Check your understanding:** Why does the LSTM's cell state help gradients survive? Why can an RNN not be parallelised across time during training? What limits a seq2seq model that compresses the input into one vector?

### Chapter 3 · Attention (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Additive attention | Bahdanau et al. (2014): the decoder looks back at all encoder states | Add attention to your seq2seq; plot alignments |
| 3.2 Queries, keys and values | Attention as a soft dictionary lookup; scaled dot-product | Implement `attention(Q, K, V, mask)` in 10 lines |
| 3.3 Why divide by √d | Variance of dot products; softmax saturation | Show softmax entropy collapse without scaling |
| 3.4 Masks | Causal masks, padding masks, combining them; the leak test | A unit test that fails if any position sees the future |

**Check your understanding:** What does the √d scaling protect against, and what happens to gradients without it? How do you test that a causal mask has no off-by-one error? What is the cost of attention in time and memory as sequence length grows?

### Chapter 4 · The transformer block line by line (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Multi-head attention | Splitting into heads, `einsum` formulation, output projection | Implement it; match `F.scaled_dot_product_attention` |
| 4.2 The residual stream | Blocks read from and write to a shared residual; pre-norm vs post-norm (Xiong et al., 2020) | Train 12-layer pre-norm and post-norm models; compare stability |
| 4.3 Feed-forward layers | GELU MLP vs SwiGLU (Shazeer, 2020); expansion ratio | Swap MLP types at equal parameter count |
| 4.4 Normalisation | LayerNorm vs RMSNorm (Zhang and Sennrich, 2019) | Implement both; measure speed |
| 4.5 Counting | Parameters per block (~12d²), training FLOPs ≈ 6 × parameters × tokens | Predict, then measure, parameters and step time |

**Check your understanding:** Why does pre-norm train more stably in deep stacks? Where do most parameters of a small GPT live, and how does that change with vocabulary size? Derive the "6N FLOPs per token" rule from the forward and backward passes.

### Chapter 5 · Positional information (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Why order is lost | Attention is permutation-equivariant | Show that shuffling tokens permutes the outputs |
| 5.2 Absolute positions | Sinusoidal and learned embeddings | Train both; test at 2× training length |
| 5.3 RoPE | Rotating query/key pairs; dot products depend on relative offsets (Su et al., 2021) | Implement RoPE; verify the relative-position property numerically |
| 5.4 ALiBi and context extension | Linear biases (Press et al., 2021); position interpolation and YaRN | Extend a RoPE model's context with interpolation; measure loss by position |

**Check your understanding:** Why does RoPE give relative-position behaviour while being applied to absolute positions? Why do models fail beyond their training length, and what do interpolation methods change? Where in the block must RoPE be applied?

### Chapter 6 · Tokenization (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Bytes and Unicode | UTF-8 lengths for Latin, Devanagari, Bengali, Tamil; normalisation | Count bytes per character across 5 scripts |
| 6.2 BPE | Training merges, encoding, byte-level BPE as in GPT-2 (Sennrich et al., 2015) | Train a byte-level BPE in pure Python |
| 6.3 Unigram and SentencePiece | Probabilistic segmentation; language-independent training (Kudo and Richardson, 2018) | Train SentencePiece; compare segmentations |
| 6.4 Fairness and cost | The same text can need up to 15× more tokens in some languages (Petrov et al., 2023); tokenizer choice affects downstream quality (Ali et al., 2023) | Fertility (tokens per word) for English, Hindi, Bengali, Tamil with 3 tokenizers |
| 6.5 Tokenizer bugs | Special tokens, whitespace handling, digit splitting, glitch tokens | Find 5 strange tokenizations in a public tokenizer |

**Check your understanding:** Why does a high token count for Hindi mean higher cost and a shorter effective context for Hindi users? Why do many tokenizers split numbers into single digits? What breaks if training and inference use different normalisation?

### Chapter 7 · Build a GPT I: model and training (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The nanoGPT architecture | Embeddings, blocks, final norm, tied unembedding | Write the model in under 200 lines |
| 7.2 Initialisation for depth | Scaled residual initialisation; zero-init variants | Compare losses at step 0 and step 500 |
| 7.3 The training loop | AdamW, warmup plus cosine, gradient accumulation, bfloat16 autocast, gradient clipping | Train on Tiny Shakespeare; then on a FineWeb-Edu sample |
| 7.4 Data loading | Memory-mapped token files, random windows, document boundaries | Pre-tokenise 200M tokens to a `uint16` file |

**Check your understanding:** Why tie input and output embeddings? What does gradient accumulation change and not change compared with a larger batch? What goes wrong if training windows cross document boundaries without a separator?

### Chapter 8 · Build a GPT II: sampling and evaluation (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Decoding | Greedy, temperature, top-k, nucleus (top-p); repetition | Sample with 6 settings; rate diversity and quality |
| 8.2 Evaluation | Validation bits per byte; few-shot tasks such as HellaSwag through `lm-evaluation-harness` | Evaluate your model and GPT-2 124M on the same tasks |
| 8.3 Reproducing GPT-2 small | The 124M configuration; Karpathy's reproduction as a reference | Train a scaled-down version on 2× T4 within your quota |
| 8.4 Overfitting and memorisation | Train/validation gaps; regurgitating training text | Measure verbatim overlap of samples with training data |

**Check your understanding:** Why does lowering the temperature reduce diversity but not necessarily errors? Why is validation loss on your own data not enough to compare with GPT-2? How would you detect a model that memorised its training set?

### Chapter 9 · Inference: the KV cache (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Prefill and decode | Why decoding is memory-bound; arithmetic intensity per token | Time prefill and decode separately |
| 9.2 The KV cache | Memory = 2 × layers × KV heads × head dim × tokens × bytes | Add a cache; measure speed-up and memory at 1k and 4k tokens |
| 9.3 Shrinking the cache | Multi-query (Shazeer, 2019), grouped-query (Ainslie et al., 2023), multi-head latent attention | Implement GQA; compare quality and cache size |
| 9.4 Faster decoding | Speculative decoding with a draft model (Leviathan et al., 2022) | Speculative decoding with your small model as draft |

**Check your understanding:** Compute the KV cache for a 32-layer model with 8 KV heads of dimension 128 at 32k tokens in bfloat16. Why is speculative decoding exact rather than approximate? Why does GQA hurt quality less than MQA?

### Chapter 10 · Model families and mixture-of-experts (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Encoder, decoder, encoder–decoder | BERT-style masked LM, T5 span corruption, why decoder-only dominates generation | Fine-tune a small encoder for classification; compare with a decoder |
| 10.2 Mixture-of-experts | Routing, top-k gating, load-balancing loss (Switch Transformer, Mixtral) | Add a top-2 MoE MLP; plot expert load |
| 10.3 Modern open architectures | DeepSeek-V3's MoE and latent attention; Qwen3 design choices | Read two model configs; explain every field |
| 10.4 Multi-token prediction and infilling | Predicting several future tokens (multi-token prediction in DeepSeek-V3); fill-in-the-middle training for code | Add a second-token prediction head; compare loss and speculative-decoding speed |

**Check your understanding:** Why can an MoE model have many more parameters than it uses per token? What goes wrong without a load-balancing loss? Why are decoder-only models used even for tasks that look like classification?

### Chapter 11 · Scaling behaviour (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Power laws | Loss vs parameters, data and compute (Kaplan et al., 2020) | Train 5 sizes; plot log-loss vs log-parameters |
| 11.2 Compute-optimal training | Chinchilla: scale parameters and tokens equally, about 20 tokens per parameter (Hoffmann et al., 2022) | An isoFLOP sweep at 3 tiny budgets |
| 11.3 Why the two laws disagreed | Counting embedding parameters, schedules and scale (Pearce and Song, 2024) | Refit your data with and without embedding parameters |
| 11.4 Beyond compute-optimal | Over-training small models for cheap inference (Sardana et al., 2023); nanochat's single "depth" dial | Predict the loss of an unseen larger run; then train it |

**Check your understanding:** Why did Chinchilla conclude that earlier large models were undertrained? Why would a company deliberately train a small model far past the Chinchilla point? What can make a scaling-law prediction from tiny models fail?

### Chapter 12 · Beyond standard attention (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 The quadratic cost | Memory and compute vs sequence length; sliding-window attention | Plot memory vs length for full and windowed attention |
| 12.2 State-space models | Mamba's selective scan (Gu and Dao, 2023); hybrids with attention | Compare a small Mamba-style model and a transformer on a copy task |
| 12.3 In-context learning | Induction heads (Olsson et al., 2022) | Detect induction heads in your GPT with a repeated-sequence test |
| 12.4 Open questions | Length generalisation, recall vs recurrence trade-off | One-page critique of a recent architecture paper |

**Check your understanding:** Why do recurrent and state-space models struggle with exact recall from far back? What evidence would convince you that a new architecture beats attention, and at what scale? How does an induction head implement copying?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Count models, MLP language model and RNNs | Bits-per-byte table |
| 2 | 2 | Lab 1 (cont.) | — |
| 3 | 3 | Lab 2 · Attention and the leak test | Mask unit tests |
| 4 | 4 | Lab 3 · The block | Block passing shape and causality tests |
| 5 | 5 | Lab 4 · Positions | **P1 due** |
| 6 | 6 | Lab 5 · Tokenizer audit | Fertility report |
| 7 | 7 | Lab 6 · GPT training | Training curves |
| 8 | 8 | Lab 6 (cont.) | Mid-term (AI off) |
| 9 | 9 | Lab 7 · KV cache and GQA | Speed and memory report |
| 10 | 10 | Lab 8 · MoE | **P2 due** |
| 11 | 11 | Lab 9 · Scaling sweep | — |
| 12 | 11 | Lab 9 (cont.) | Scaling-law fit and prediction |
| 13 | 12 | Lab 10 · Attention vs SSM | — |
| 14 | 12 | Project studio | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining paper notation; generating unit tests for shapes and masks; writing data-preparation and plotting scripts; reviewing your model code for known pitfalls after you have written it; comparing your implementation with reference code (nanoGPT, Hugging Face Transformers).
- **Do without AI (drills):** the attention function and multi-head reshape from memory (timed, 15 minutes); RoPE derivation; KV-cache and FLOP arithmetic; BPE training loop; both exams.
- **Verify AI output by:** (1) the leak test: perturb token t and assert that no output before t changes; (2) matching `F.scaled_dot_product_attention` within tolerance; (3) checking the loss at initialisation ≈ ln(vocabulary size); (4) overfitting a single batch; (5) checking parameter counts against your formula.
- **Where AI still fails here:** collect evidence in a log. Ask an assistant for a RoPE implementation and test the relative-position property; ask for a causal attention with padding and run the leak test with left-padded batches; ask for a KV-cache implementation and compare its outputs with the uncached model token by token. Record which tests fail. Generated code that "trains fine" but leaks future tokens is the most important failure to catch, because its validation loss looks better than it should.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) and oral defence of P3 | 30% |

**Mastery gate.** You pass when you can, with AI off: (1) write a causal multi-head attention with RoPE and a KV cache in 45 minutes that passes the leak test and matches the uncached outputs; (2) compute parameters, training FLOPs and KV-cache memory for a model described only by its config; (3) train a small GPT, report bits per byte with confidence intervals across seeds, and explain the shape of its learning curve in an oral exam.

## Industry reality

Open-weight models document their transformer variants in technical reports: grouped-query attention and RoPE in the Llama 3 family (2024), multi-head latent attention and DeepSeekMoE in DeepSeek-V2 and V3 (2024), and Muon plus a hybrid compressed-attention design for million-token contexts in DeepSeek-V4 (2026). Tokenization is a fairness and cost issue for Indian languages: Petrov et al. (2023) found up to 15× differences in token counts for the same content across languages. Implementation questions (write attention, find the bug in this block, compute this memory) are standard in research-engineer loops ([DLR market page](../../../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md)).

**Interview questions from this course**

1. *Implement causal self-attention.* Strong answer: correct Q/K/V projections and head reshape; scaling by √d; mask applied before softmax with −inf; dropout placement; output projection; states time and memory complexity; offers a test for leakage.
2. *How much memory does the KV cache need for this model at this context, and how would you reduce it?* Strong answer: the formula with numbers; GQA/MQA/latent attention; quantised KV; paged allocation; sliding windows; trade-offs for quality.
3. *Why RoPE instead of learned absolute positions?* Strong answer: relative behaviour through rotation; no extra parameters; extrapolation limits and interpolation/YaRN; applied to Q and K only.
4. *You have a fixed compute budget. How big a model, and how many tokens?* Strong answer: Chinchilla-style isoFLOP reasoning; about 20 tokens per parameter as a rough guide; over-training when inference cost dominates; checks data availability and repetition.
5. *Your validation loss is suspiciously low. What do you check?* Strong answer: causal-mask leak; train/validation overlap or duplicated documents; evaluation on the wrong split; tokenizer mismatch inflating per-token metrics; reports bits per byte.

## Resources (free first)

- **Primary courses:** Stanford CS224N, NLP with Deep Learning — https://web.stanford.edu/class/cs224n/ ; Karpathy, *Neural Networks: Zero to Hero* ("Let's build GPT", "Let's build the GPT Tokenizer", "Let's reproduce GPT-2") — https://karpathy.ai/zero-to-hero.html ; Stanford CS336, Language Modeling from Scratch (Spring 2026) — https://cs336.stanford.edu/
- **Code:** nanoGPT — https://github.com/karpathy/nanoGPT ; nanochat — https://github.com/karpathy/nanochat ; *The Annotated Transformer* — https://nlp.seas.harvard.edu/annotated-transformer/
- **Textbooks:** *Dive into Deep Learning*, attention and transformer chapters — https://d2l.ai/ ; Prince, *Understanding Deep Learning* — https://udlbook.github.io/udlbook/
- **Papers:** Attention Is All You Need https://arxiv.org/abs/1706.03762 ; Bahdanau et al. https://arxiv.org/abs/1409.0473 ; BPE https://arxiv.org/abs/1508.07909 ; RoPE https://arxiv.org/abs/2104.09864 ; GQA https://arxiv.org/abs/2305.13245 ; Switch Transformers https://arxiv.org/abs/2101.03961 ; Kaplan et al. https://arxiv.org/abs/2001.08361 ; Chinchilla https://arxiv.org/abs/2203.15556 ; Mamba https://arxiv.org/abs/2312.00752 ; induction heads https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html
- **Data:** FineWeb-Edu — https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu ; FineWeb2 (1,000+ languages, including Indian languages) — https://arxiv.org/abs/2506.20920
- **Evaluation:** EleutherAI `lm-evaluation-harness` — https://github.com/EleutherAI/lm-evaluation-harness
- **Compute (free):** Kaggle's 2× T4 option suits Labs 7–10 (weekly quota in account settings; sessions up to 12 hours); Colab's free tier suits shorter labs. Keep models at 10–50M parameters for the scaling sweep.

## Sources

- Vaswani et al., "Attention Is All You Need" (2017) — https://arxiv.org/abs/1706.03762 (checked 2026-10)
- DeepSeek-AI, "DeepSeek-V2" (May 2024; MLA reduces KV cache by 93.3% vs DeepSeek 67B) — https://arxiv.org/abs/2405.04434 (checked 2026-10)
- DeepSeek-AI, "DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence" (2026) — https://arxiv.org/abs/2606.19348 (checked 2026-10)
- nanochat README ("GPT-2 capability" for about $48, ~2 hours on 8×H100) — https://github.com/karpathy/nanochat (checked 2026-10)
- Petrov et al., "Language Model Tokenizers Introduce Unfairness Between Languages" (2023) — https://arxiv.org/abs/2305.15425 ; Ali et al., "Tokenizer Choice for LLM Training: Negligible or Crucial?" (2023) — https://arxiv.org/abs/2310.08754 (checked 2026-10)
- Hoffmann et al., "Training Compute-Optimal Large Language Models" (2022) — https://arxiv.org/abs/2203.15556 ; Pearce and Song, "Reconciling Kaplan and Chinchilla Scaling Laws" (2024) — https://arxiv.org/abs/2406.12907 ; Sardana et al., "Beyond Chinchilla-Optimal" (2023) — https://arxiv.org/abs/2401.00448 (checked 2026-10)
- Llama Team, "The Llama 3 Herd of Models" (2024) — https://arxiv.org/abs/2407.21783 ; DeepSeek-AI, "DeepSeek-V3 Technical Report" (2024) — https://arxiv.org/abs/2412.19437 (checked 2026-10)

_Last reviewed: 2026-10_
