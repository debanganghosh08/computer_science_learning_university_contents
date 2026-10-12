# DLR401 · Large Language Models: Pretraining, Fine-Tuning and Alignment

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L2 → L4 | [DLR301](../../year_3/DLR301_neural_networks_from_scratch_autograd/README.md); in practice also [DLR303](../../year_3/DLR303_sequence_models_and_transformers/README.md) and [DLR304](../../year_3/DLR304_training_deep_networks_optimization/README.md) | [DLR501](../../year_5/DLR501_frontier_seminar_interpretability_reasoning/README.md); taken alongside [DLR402](../DLR402_multimodal_models/README.md); pairs with [DLR403](../DLR403_reinforcement_learning_including_rl_for_language/README.md) |

## Why this course matters now

This course is about how language models are made, not how they are used in applications (that is the [AI Engineering major](../../../ai_engineering/year_3/AIE301_llm_fundamentals_for_engineers/README.md)). The recipe has become public in detail. FineWeb documents a 15-trillion-token web dataset and every filtering decision behind it (Penedo et al., 2024). Tülu 3 releases a full post-training recipe of supervised fine-tuning, direct preference optimisation and "reinforcement learning with verifiable rewards" (RLVR) (Lambert et al., 2024). Olmo 3 releases "the entire model flow": every stage, checkpoint, data point and dependency (Team Olmo, 2025). DeepSeek-R1, published in *Nature* in 2025, showed that reasoning behaviour can be "incentivized through pure reinforcement learning". Strong open-weight families now ship under permissive licences: gpt-oss (Apache 2.0, 2025), Gemma 4 (Apache 2.0, 2026), DeepSeek-V4 (MIT, 2026), and India's Sarvam 30B and 105B (Apache 2.0, 2026). Others carry custom terms, such as Meta's Llama 4 licence with its 700-million-monthly-user clause. Agents can now write a TRL fine-tuning script or an evaluation harness in minutes. The scarce skills are judgement about data, recipes that do not silently regress, evaluations that are not contaminated, and knowing what each training stage can and cannot add.

## Learning outcomes

By the end you can:

1. **Build** a web-text pipeline (extraction, language identification, heuristic and model-based quality filtering, MinHash deduplication, PII removal, decontamination) and **measure** what each stage removes.
2. **Pretrain** a small decoder-only model with a documented data mixture and schedule, and **report** its compute, throughput and evaluation.
3. **Run** supervised fine-tuning with correct chat templates and loss masking, and **compare** full fine-tuning with LoRA on quality and forgetting.
4. **Derive** the KL-regularised RLHF objective, the Bradley–Terry reward model and the DPO loss, and **implement** reward-model training, DPO and one reference-free variant.
5. **Train** a small model with RLVR (GRPO-style) on verifiable tasks, and **evaluate** what it gained using pass@k against the base model.
6. **Design** an evaluation suite with confidence intervals, contamination checks and multilingual coverage (including Indian languages), and **critique** leaderboard results.
7. **Audit** model licences and training-data obligations, and **write** a model card and release checklist.

## Chapters and lessons

### Chapter 1 · The lifecycle and the open-model landscape (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Stages | Pretraining → mid-training → SFT → preference optimisation → RL → evaluation → release; what each stage changes | Map Olmo 3's published flow onto these stages |
| 1.2 Open weights vs open source | Weights, code, data, checkpoints and licence as separate questions | Classify 8 releases by what they actually publish |
| 1.3 The 2026 landscape | Llama 4, Qwen3.x, DeepSeek-V4, Gemma 4, gpt-oss, Mistral, GLM-5, Kimi, Olmo 3; Sarvam and BharatGen Param from India | Licence audit table from each model card (licence, use limits, attribution) |
| 1.4 Reading a technical report | Data, architecture, compute, recipe, evaluation, what is omitted | Annotate the Llama 3 or Qwen3 report; list 10 unstated details |

**Check your understanding:** Why is "open-weight" not the same as "open-source"? What can you reproduce from Olmo 3 that you cannot from Llama 4? Which licence terms would stop a startup from shipping a product built on a given checkpoint?

### Chapter 2 · Pretraining data I: web-scale pipelines (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 From Common Crawl to text | WARC vs WET, HTML extraction (trafilatura), boilerplate | Extract text from one WARC file; compare with WET |
| 2.2 Language identification | fastText-style LID; GlotLID for low-resource languages (Kargaran et al., 2023); code-mixed text | Measure LID errors on Hinglish and romanised Bengali |
| 2.3 Heuristic filters | Gopher and C4 rules: repetition, symbol ratios, stop words, line endings | Implement 6 rules; inspect 50 removed documents |
| 2.4 Model-based quality filters | FineWeb-Edu's educational classifier; DCLM's fastText classifier (Li et al., 2024) | Train a small quality classifier; measure precision by manual audit |
| 2.5 Deduplication | Exact hashing, MinHash LSH, near-duplicate thresholds; why dedup helps (Lee et al., 2021) | MinHash dedup at Jaccard 0.8 on 1M documents |

**Check your understanding:** Why does FineWeb deduplicate per snapshot rather than globally, and what did its ablations show? How can a quality classifier encode bias against dialects or non-standard writing? Why does deduplication reduce memorisation?

### Chapter 3 · Pretraining data II: languages, mixtures and rights (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Multilingual pipelines | FineWeb2's per-language thresholds across 1,000+ languages; Indic corpora (IndicLLMSuite/Sangraha, Khan et al., 2024) | Compare Hindi FineWeb2 with an Indic corpus on 100 samples |
| 3.2 Data mixtures | Domain weights; DoReMi (Xie et al., 2023); upsampling code and math | Mixture ablation at 20M parameters |
| 3.3 Synthetic and repeated data | Textbook-style synthetic data (Gunasekar et al., 2023); repetition limits (Muennighoff et al., 2023) | Measure loss with 1, 4 and 16 epochs of the same data |
| 3.4 PII, safety and decontamination | PII scrubbing; toxic-content filters; removing benchmark text by n-gram overlap | Decontaminate your corpus against 5 benchmarks; report hits |
| 3.5 Rights and consent | robots.txt and opt-outs, licences of datasets, India's Digital Personal Data Protection Act, 2023 | Data-provenance sheet for your corpus |

**Check your understanding:** Why can a mixture that minimises average loss hurt a low-resource language? When is synthetic data likely to help, and when does it narrow the model? Why must decontamination happen before training, not after?

### Chapter 4 · Pretraining at small scale (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Architecture choices | GQA, RoPE, SwiGLU, RMSNorm, MoE; reading `config.json` files | Explain every field of two open-model configs |
| 4.2 Packing and masking | Sequence packing, document masking, end-of-text handling | Measure throughput and loss with and without document masking |
| 4.3 The training run | WSD schedules, Muon or AdamW, checkpointing, loss-spike handling, MFU | Pretrain a ~100M model on Kaggle 2× T4 for a fixed token budget |
| 4.4 A reference harness | nanochat: tokenizer, pretraining, fine-tuning, evaluation and inference in one repo; "GPT-2 capability" for about $48 on 8×H100 | Run nanochat's smallest configuration and compare with your own model |

**Check your understanding:** Why does document masking matter more for long contexts? How would you decide between a dense and an MoE model at your compute budget? What signals in the first 1% of a run predict that it will fail?

### Chapter 5 · Mid-training and long context (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Annealing on high-quality data | Late-stage mixtures of math, code and curated text during learning-rate cooldown | Anneal ablation: same cooldown, two mixtures |
| 5.2 Long-context extension | RoPE base changes, position interpolation, YaRN; data for long contexts | Extend your model from 1k to 4k tokens; loss by position |
| 5.3 Measuring long context | Needle-in-a-haystack and its limits; multi-hop retrieval tests | Build a 3-level long-context test set |
| 5.4 Checkpoint averaging | Weight averaging across late checkpoints | Average 3 checkpoints; compare evaluation results |

**Check your understanding:** Why does annealing on a small high-quality set move benchmarks more than its size suggests, and what is the contamination risk? Why can a model pass needle tests yet fail real long-document tasks? What does checkpoint averaging approximate?

### Chapter 6 · Supervised fine-tuning (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Chat templates | Roles, special tokens, generation prompts; template mismatches as silent bugs | Break and fix a template; observe the effect on outputs |
| 6.2 Loss masking and packing | Train on responses only; packed SFT with correct masks | Masked vs unmasked loss on the same data |
| 6.3 Data quality | LIMA's 1,000 examples (Zhou et al., 2023); Self-Instruct; distillation from stronger models and their terms of use | Curate 2,000 Hindi instruction examples; filter half; compare |
| 6.4 Full vs parameter-efficient | LoRA (Hu et al., 2021), QLoRA (Dettmers et al., 2023); "LoRA learns less and forgets less" (Biderman et al., 2024) | Full fine-tune vs LoRA on a 0.5–1.5B model; measure gain and forgetting |

**Check your understanding:** Why does training on prompt tokens hurt? What does LIMA's result suggest about where capabilities come from? When would you choose full fine-tuning despite its cost?

### Chapter 7 · Reward models and RLHF (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Preference data | Pairwise comparisons, annotation guidelines, rater agreement, AI feedback (Constitutional AI, Bai et al., 2022) | Write guidelines; label 100 pairs with a partner; compute agreement |
| 7.2 Reward models | Bradley–Terry loss; evaluation on held-out pairs and RewardBench (Lambert et al., 2024) | Train a reward model from a small base model |
| 7.3 RLHF with PPO | The InstructGPT pipeline (Ouyang et al., 2022); KL penalty to a reference model | Trace the three InstructGPT stages and their data sizes |
| 7.4 Over-optimisation | Proxy vs gold reward under optimisation pressure (Gao et al., 2022); length and sycophancy biases | Best-of-n with a proxy reward; plot gold reward as n grows |

**Check your understanding:** Why does a KL penalty keep RLHF from collapsing onto reward-model exploits? Why does best-of-n eventually lower true quality when the reward model is imperfect? What does low inter-rater agreement mean for the ceiling of a reward model?

### Chapter 8 · Direct preference methods (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 DPO | Closed-form optimal policy of KL-regularised RL; the implicit reward (Rafailov et al., 2023) | Derive the DPO loss on paper |
| 8.2 Variants | IPO, KTO (unpaired feedback), ORPO (no reference model), SimPO (length-normalised, reference-free) | DPO vs SimPO on the same pairs, 3 seeds |
| 8.3 On-policy vs off-policy data | Why preference pairs sampled from your own model help; iterative DPO | Compare off-policy and on-policy pair sets |
| 8.4 Length bias and evaluation | Length-controlled win rates; LLM-as-judge biases | Measure response length shift after DPO |

**Check your understanding:** What assumption lets DPO skip the explicit reward model? Why can DPO lower the likelihood of both the chosen and rejected answers? Why is a raw win rate against a judge model not enough evidence?

### Chapter 9 · RL with verifiable rewards and reasoning (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Verifiable rewards | Answer checkers, unit tests, format rewards; RLVR as named in Tülu 3 | Write a robust math-answer verifier; test it against 50 tricky outputs |
| 9.2 GRPO | Group-relative advantages without a critic (Shao et al., 2024); R1-Zero and R1 (DeepSeek-AI, 2025) | GRPO on GSM8K with a 0.5–1.5B model using TRL |
| 9.3 Fixes and variants | DAPO (Yu et al., 2025), Dr. GRPO bias corrections (Liu et al., 2025), GSPO sequence-level ratios (Zheng et al., 2025) | Ablate one fix; observe length and entropy curves |
| 9.4 What RL adds | RLVR raises pass@1 but base models can win at large k (Yue et al., 2025); distillation can add new patterns; spurious-reward results (Shao et al., 2025) | pass@k curves (k = 1…64) for base, SFT-distilled and RL models |
| 9.5 Open testbeds | Olmo 3's RL-Zero checkpoints and released data | Reproduce one RL-Zero evaluation number |

**Check your understanding:** Why does GRPO need several samples per prompt? What does "base model wins at pass@256" imply about what RLVR learned? How could a weak verifier be exploited, and how would you detect it?

### Chapter 10 · Evaluation science (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Harnesses | `lm-evaluation-harness`; few-shot formats; prompt sensitivity | Evaluate 3 models; vary the prompt format; report spread |
| 10.2 Benchmarks | MMLU, GPQA, Humanity's Last Exam, IFEval, MILU for 11 Indian languages (Verma et al., 2024) | Build a 300-item Indic evaluation set with a held-out split |
| 10.3 Contamination | n-gram overlap; exchangeability tests (Oren et al., 2023); dated benchmarks | Test a public model for contamination on one benchmark |
| 10.4 Arenas and leaderboards | Chatbot Arena; "The Leaderboard Illusion" (Singh et al., 2025) | Critique one leaderboard's methodology in one page |
| 10.5 Statistics | Bootstrap confidence intervals; paired tests; minimum detectable differences | Add CIs to every number in your evaluation report |

**Check your understanding:** Why can two harnesses report different MMLU scores for the same model? How would you show that a benchmark leaked into training? What makes an arena ranking hard to reproduce?

### Chapter 11 · Safety in training and release (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Refusals and over-refusal | Safety SFT data; measuring both harmful compliance and needless refusal | Measure both on a small benchmark before and after safety tuning |
| 11.2 Fine-tuning side effects | Emergent misalignment from narrow fine-tuning (Betley et al., 2025) | Read the paper; design an evaluation that would catch it |
| 11.3 Reward hacking during RL | Hacking in production coding environments generalised to broader misalignment; inoculation prompting as a mitigation (MacDiarmid et al., 2025) | Add a reward-hacking check to your RL run |
| 11.4 Release | Model cards, licences (Apache 2.0, MIT, custom community licences, OpenRAIL), acceptable-use policies, staged release | Model card and release checklist for your fine-tuned model |

**Check your understanding:** Why might safety training on chat prompts not transfer to agentic use? What evidence belongs in a model card that a leaderboard score does not give? Which licence would you choose for an Indic model you want widely used, and why?

### Chapter 12 · End-to-end sprint (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Integration | Data → base → SFT → DPO or RLVR → evaluation → card | Project P3 build week |
| 12.2 Reviews | Reading another team's recipe critically | Peer review of two P3 drafts |
| 12.3 Attributing gains | Stage-by-stage evaluation with data held fixed; cost per point of improvement; regressions by language and task | Ablation table for your P3 pipeline |
| 12.4 The technical report | Data, recipe, compute, evaluation and limitations, in the style of the Tülu 3 and Olmo 3 reports | A 6-page technical report for your model |

**Check your understanding:** Which stage of your pipeline contributed the most to your final score, and how do you know? What would you change with 10× compute? What did you choose not to measure, and why?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Licence and release audit | Audit table |
| 2 | 2 | Lab 2 · WARC to clean text | Stage-by-stage removal stats |
| 3 | 3 | Lab 3 · Dedup, decontamination and mixtures | **P1 due** |
| 4 | 4 | Lab 4 · Small pretraining run | Training report |
| 5 | 5 | Lab 5 · Long-context extension | — |
| 6 | 6 | Lab 6 · SFT: masking, LoRA vs full | Forgetting measurement |
| 7 | 7 | Lab 7 · Reward model and best-of-n | Over-optimisation plot |
| 8 | 8 | Lab 8 · DPO and SimPO | Mid-term (AI off) |
| 9 | 9 | Lab 9 · Verifiers and GRPO | — |
| 10 | 9 | Lab 9 (cont.) | **P2 due** |
| 11 | 10 | Lab 10 · Evaluation, safety and release | Evaluation report |
| 12 | 11 | Lab 10 (cont.) | Model card |
| 13 | 12 | Project studio | Peer reviews |
| 14 | 12 | Project studio | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** writing data-pipeline glue and TRL configs; generating candidate SFT data (with licences checked and filtering applied); acting as one judge among several in evaluations; summarising technical reports after you have read them; spotting bugs in chat templates.
- **Do without AI (drills):** the Bradley–Terry, DPO and GRPO derivations; KV and memory budgets for fine-tuning runs; designing an evaluation and its statistics; reading loss and reward curves; both exams.
- **Verify AI output by:** (1) decoding a tokenised SFT batch and checking which tokens carry loss; (2) running verifiers against adversarial outputs (extra text, multiple answers, wrong units); (3) measuring judge-model agreement against 50 human labels; (4) checking every licence claim against the model card text itself; (5) re-running the baseline yourself instead of trusting reported numbers.
- **Where AI still fails here:** the documented failures are in what RL optimises. Policies trained against weak checks learn to exploit them, and in Anthropic's experiments this generalised to broader misalignment (MacDiarmid et al., 2025). In your own runs, log every case where reward rose while held-out correctness did not, and every judge-model verdict that disagreed with human raters.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) and oral defence of P3 | 30% |

**Mastery gate.** You pass when you can: (1) with AI off, derive the DPO loss from the KL-regularised objective and explain GRPO's advantage estimate; (2) take an open base model through SFT and one preference or RL stage, and show with confidence intervals and a contamination check what each stage changed, including any regressions; (3) defend your data, licence and evaluation choices in an oral exam.

## Industry reality

Post-training is where much of the recent progress and hiring sits: the DLR market page lists "pretraining, post-training, evaluation, inference" as Member of Technical Staff specialisms ([DLR market page](../../../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md)). Public recipes now include Tülu 3 (SFT, DPO, RLVR), Olmo 3 (fully open model flow), DeepSeek-R1 (RL-first reasoning) and Kimi K2 (large-scale agentic RL). In India, Sarvam released 30B and 105B models under Apache 2.0 in March 2026, and BharatGen publishes Param models on Hugging Face. Interviews test derivations (RLHF, DPO), data-pipeline design and evaluation judgement.

**Interview questions from this course**

1. *Design a pretraining data pipeline for a Hindi–English model from Common Crawl.* Strong answer: extraction; language ID that handles code-mixing and romanised text; heuristic plus classifier filtering with audited precision; MinHash dedup; PII removal; benchmark decontamination; mixture weights with ablations; provenance and opt-out records.
2. *Derive DPO from the RLHF objective.* Strong answer: optimal policy π* ∝ π_ref · exp(r/β); invert for r; substitute into Bradley–Terry; partition function cancels; final loss; notes assumptions and length bias.
3. *Compare PPO and GRPO for training a reasoning model.* Strong answer: GRPO drops the value network and uses group-normalised rewards; needs several samples per prompt; known biases (length, standard-deviation normalisation) and fixes (Dr. GRPO, DAPO); stability and compute trade-offs.
4. *How do you know a benchmark gain is real?* Strong answer: confidence intervals across seeds and prompt formats; contamination checks; held-out and dated evaluations; human spot checks; comparison against a re-run baseline, not reported numbers.
5. *Which open base model would you choose for a commercial Indian-language assistant?* Strong answer: licence terms first (Apache/MIT vs custom clauses); tokenizer efficiency for the target languages; base-model quality on Indic benchmarks such as MILU; size vs serving cost; availability of base (not only instruct) checkpoints; data provenance.

## Resources (free first)

- **Courses:** Stanford CS336, Language Modeling from Scratch (Spring 2026; assignments on data, scaling and alignment) — https://cs336.stanford.edu/ ; Hugging Face LLM Course — https://huggingface.co/learn/llm-course/chapter1/1
- **Books and guides:** Nathan Lambert, *Reinforcement Learning from Human Feedback* (free online) — https://rlhfbook.com/ ; Hugging Face, *The Ultra-Scale Playbook* — https://huggingface.co/spaces/nanotron/ultrascale-playbook
- **Code:** TRL — https://github.com/huggingface/trl (GRPO trainer docs: https://huggingface.co/docs/trl/main/en/grpo_trainer) ; nanochat — https://github.com/karpathy/nanochat ; `lm-evaluation-harness` — https://github.com/EleutherAI/lm-evaluation-harness ; Olmo — https://allenai.org/olmo
- **Data:** FineWeb-Edu — https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu ; FineWeb2 — https://arxiv.org/abs/2506.20920 ; IndicLLMSuite — https://arxiv.org/abs/2403.06350
- **Key papers:** InstructGPT https://arxiv.org/abs/2203.02155 ; Christiano et al. https://arxiv.org/abs/1706.03741 ; Constitutional AI https://arxiv.org/abs/2212.08073 ; DPO https://arxiv.org/abs/2305.18290 ; SimPO https://arxiv.org/abs/2405.14734 ; KTO https://arxiv.org/abs/2402.01306 ; Tülu 3 https://arxiv.org/abs/2411.15124 ; DeepSeekMath (GRPO) https://arxiv.org/abs/2402.03300 ; DeepSeek-R1 https://arxiv.org/abs/2501.12948 ; DAPO https://arxiv.org/abs/2503.14476 ; Dr. GRPO https://arxiv.org/abs/2503.20783 ; Yue et al. https://arxiv.org/abs/2504.13837 ; reward over-optimisation https://arxiv.org/abs/2210.10760 ; dedup https://arxiv.org/abs/2107.06499 ; DCLM https://arxiv.org/abs/2406.11794 ; Leaderboard Illusion https://arxiv.org/abs/2504.20879
- **Licences:** Llama 4 Community License — https://www.llama.com/llama4/license/ ; gpt-oss announcement — https://openai.com/index/introducing-gpt-oss/
- **Compute (free):** SFT, DPO and GRPO on 0.5–1.5B models fit Kaggle's 2× T4 or Colab with LoRA and bf16/fp16; small pretraining runs fit Kaggle's weekly quota. Researchers can apply to Google's TPU Research Cloud — https://sites.research.google/trc/about/. The IndiaAI Mission offers subsidised GPU access to eligible Indian institutions, researchers and startups through its compute portal (student eligibility and rates unconfirmed) — https://indiaai.gov.in/

## Sources

- Penedo et al., "The FineWeb Datasets" (2024) — https://arxiv.org/abs/2406.17557 (checked 2026-10)
- Lambert et al., "Tülu 3: Pushing Frontiers in Open Language Model Post-Training" (2024) — https://arxiv.org/abs/2411.15124 (checked 2026-10)
- Team Olmo, "Olmo 3" (Dec 2025) — https://arxiv.org/abs/2512.13961 (checked 2026-10)
- DeepSeek-AI, "DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning", *Nature* (2025) — https://www.nature.com/articles/s41586-025-09422-z ; arXiv version — https://arxiv.org/abs/2501.12948 (checked 2026-10)
- Model-card licences on Hugging Face, checked 12 Oct 2026: gpt-oss — https://huggingface.co/openai/gpt-oss-120b ; Gemma 4 — https://huggingface.co/google/gemma-4-31B-it ; DeepSeek-V4 collection — https://huggingface.co/collections/deepseek-ai/deepseek-v4 ; Sarvam — https://huggingface.co/sarvamai/sarvam-105b
- Meta, Llama 4 Community License (700M MAU clause) — https://www.llama.com/llama4/license/ (checked 2026-10)
- MacDiarmid et al., "Natural Emergent Misalignment from Reward Hacking in Production RL" (Nov 2025) — https://arxiv.org/abs/2511.18397 (checked 2026-10)
- Betley et al., "Emergent Misalignment" (2025) — https://arxiv.org/abs/2502.17424 (checked 2026-10)
- Verma et al., "MILU: A Multi-task Indic Language Understanding Benchmark" (2024) — https://arxiv.org/abs/2411.02538 (checked 2026-10)

_Last reviewed: 2026-10_
