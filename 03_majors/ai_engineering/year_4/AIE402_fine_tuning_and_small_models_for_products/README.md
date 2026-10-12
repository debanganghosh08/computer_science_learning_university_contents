# AIE402 · Fine-Tuning and Small Models for Products

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L2 → L4 | [AIE302](../../year_3/AIE302_prompt_and_context_engineering/README.md); assumes [AIE301](../../year_3/AIE301_llm_fundamentals_for_engineers/README.md), [AIE305](../../year_3/AIE305_evaluating_llm_systems/README.md) and [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) | [AIE403](../AIE403_llmops_observability_guardrails_cost_and_latency/README.md), [AIE501](../../year_5/AIE501_frontier_seminar_long_horizon_autonomous_agents/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md); pairs with [MLE404](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md) and [DLR401](../../../deep_learning/year_4/DLR401_large_language_models_pretraining_fine_tuning/README.md) |

## Why this course matters now

Most product teams should not fine-tune first. Prompting, retrieval and better evals solve most problems more cheaply. When a task is narrow, high-volume and well specified, though, a small tuned model can beat a large general one on quality, latency and cost. In Predibase's LoRA Land study (2024), 224 of 310 LoRA fine-tuned models beat GPT-4 on their tasks, and the best adapter per task beat it on 24 of 31 tasks. DeepSeek released six dense models, from 1.5B to 70B parameters, distilled from its R1 reasoning model (2025). Flipkart described labelling search relevance with an LLM trained by supervised fine-tuning followed by GRPO reinforcement learning (2025). The vendor landscape also shifts underfoot. OpenAI notified developers in May 2026 that it was winding down its self-serve fine-tuning platform, which is now closed to new users, and Meta's torchtune is no longer actively maintained. Open-weight models with open tooling (Hugging Face TRL and PEFT, Unsloth, Axolotl, vLLM multi-LoRA serving) are now the durable path. AI assistants write training scripts easily. Your value lies in deciding whether to fine-tune at all, curating data that teaches the right behaviour, proving the tuned model is better without breaking anything else, and serving it cheaply.

## Learning outcomes

By the end you can:

1. **Decide** between prompting, RAG, fine-tuning and distillation for a task, using a written cost–quality–risk analysis backed by baseline numbers.
2. **Curate** a fine-tuning dataset (sourcing, consent, PII redaction, deduplication, decontamination against the eval set, label quality) and **document** it with a data card.
3. **Run** supervised fine-tuning with LoRA and QLoRA, **choose** rank, target modules and learning rate with evidence, and **diagnose** under- and overfitting.
4. **Apply** preference tuning (DPO and variants) and reinforcement fine-tuning with verifiable rewards (GRPO), and **detect** reward hacking.
5. **Distil** a large model's behaviour into a small model and **measure** the quality retained per unit of cost.
6. **Evaluate** a fine-tune on the target task, on general capabilities and on safety behaviour, against a prompted baseline at equal cost.
7. **Serve** fine-tuned models (merged weights, multi-LoRA serving, quantised small models) and **compute** cost per million tokens.
8. **Operate** fine-tuning reproducibly: data and model versioning, experiment tracking, licences and model cards.

## Chapters and lessons

### Chapter 1 · Should you fine-tune? (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What tuning changes | Format, style, task behaviour, refusal boundaries, latency (smaller model) vs what it does not reliably add (fresh facts; use retrieval) | Classify 12 real problem statements as prompt, RAG, fine-tune or none |
| 1.2 The baseline ladder | Zero-shot → few-shot → optimised prompt → RAG → fine-tune; measure each rung before climbing | Build the first three rungs for a classification task; record quality and cost |
| 1.3 Evidence | LoRA Land (Zhao et al., 2024); where tuned small models win and where they lose | Read the report; list the task types where adapters lost to GPT-4 |
| 1.4 Platform risk | Managed fine-tuning APIs can change or close (OpenAI's May 2026 wind-down); owning weights vs renting a service | Write a vendor-risk section for a fine-tuning proposal |

**Check your understanding:** Why does fine-tuning a model on your documents not replace retrieval? What has to be true about traffic volume for fine-tuning to pay back? What do you lose if your fine-tuning provider shuts down?

### Chapter 2 · Data is the product (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Sources | Product logs (consent and purpose under India's DPDP Act), expert-written examples, synthetic data from a stronger model (check terms of use), public datasets and their licences | Draft a data-sourcing plan with consent and licence columns |
| 2.2 Quality over quantity | LIMA: 1,000 carefully curated examples aligned a 65B model well (Zhou et al., 2023); diversity and difficulty coverage | Build two 1,000-example sets (random vs curated); compare after training |
| 2.3 Cleaning | Deduplication (exact and near-duplicate), PII detection and redaction (Presidio), toxic and low-quality filtering | Clean a 20k-example log export; report what you removed and why |
| 2.4 Decontamination | Keep eval items out of training data; n-gram and embedding overlap checks | Write a decontamination check that fails the build on overlap |
| 2.5 Labelling at scale | Guidelines, annotator agreement, Argilla or Label Studio, adjudication; data cards | Label 300 examples with a partner; report κ; write the data card |

**Check your understanding:** Why can 1,000 good examples beat 50,000 noisy ones? What is the legal and ethical difference between using logs for debugging and using them for training? How does test data leak into a fine-tuning set without anyone noticing?

### Chapter 3 · Supervised fine-tuning mechanics (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 The objective | Next-token loss on completions only, chat templates and special tokens, packing, sequence length | Train with and without completion-only loss; compare outputs |
| 3.2 Hyperparameters | Learning rate and schedule, epochs, batch size, warm-up; reading loss curves | Run a learning-rate sweep; pick the best by dev eval, not by loss |
| 3.3 Memory math | Full fine-tuning (weights + gradients + optimiser states) vs parameter-efficient methods; gradient checkpointing | Compute GPU memory for full vs LoRA tuning of an 8B model; verify by measurement |
| 3.4 Tooling | Hugging Face TRL `SFTTrainer`, PEFT, Unsloth, Axolotl; torchtune's maintenance status as a reminder to check tool health | Fine-tune a 1–3B model on a free or low-cost GPU with TRL |

**Check your understanding:** Why can training loss keep falling while your task metric gets worse? What happens if the chat template at training time differs from the one at serving time? Why does an optimiser like Adam need much more memory than the weights alone?

### Chapter 4 · LoRA and QLoRA (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Low-rank adapters | LoRA (Hu et al., 2021): frozen weights + trainable low-rank matrices; rank, alpha, target modules | Implement a LoRA layer from scratch in PyTorch on a small model |
| 4.2 What the evidence says | LoRA learns less and forgets less than full fine-tuning (Biderman et al., 2024); applying LoRA to all layers, especially MLPs, and a learning rate about 10× that of full fine-tuning ("LoRA Without Regret", Thinking Machines, Sept 2025) | Compare attention-only vs all-layer LoRA on your task |
| 4.3 QLoRA | 4-bit NF4 base weights, double quantisation, paged optimisers; a 65B model on one 48 GB GPU (Dettmers et al., 2023) | QLoRA-tune a 7–8B model on a 16–24 GB GPU; measure quality vs 16-bit LoRA |
| 4.4 Variants | DoRA (Liu et al., 2024); adapter merging; when full fine-tuning is still worth it | Merge an adapter; confirm outputs match unmerged inference |

**Check your understanding:** Why does LoRA forget less of the base model's abilities? Your LoRA run underperforms: which three settings do you check before increasing rank? When is QLoRA's quality loss acceptable?

### Chapter 5 · Preference tuning (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 From RLHF to DPO | Reward models and PPO (Ouyang et al., 2022) vs Direct Preference Optimization (Rafailov et al., 2023) | Derive the DPO loss on one page; explain each term |
| 5.2 Preference data | Chosen/rejected pairs from human raters or judges; position and length biases in collection | Collect 500 preference pairs for tone and helpfulness with a calibrated judge plus human spot checks |
| 5.3 Variants | KTO (binary feedback), ORPO (no reference model), SimPO; what each removes | Run DPO and one variant with TRL; compare win rate and response length |
| 5.4 Failure modes | Length exploitation, over-refusal or under-refusal, mode collapse | Measure response length and refusal rate before and after tuning |

**Check your understanding:** Why does preference tuning often make answers longer, and how do you control it? When is a thumbs-up/down signal enough (KTO) and when do you need pairs? What would convince you that a DPO run made the model less safe?

### Chapter 6 · Reinforcement fine-tuning with verifiable rewards (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 GRPO | Group-relative advantages without a value model (Shao et al., DeepSeekMath, 2024); TRL `GRPOTrainer` | Train a small model on arithmetic or SQL with an executable reward |
| 6.2 Reward design | Checkers (unit tests, SQL execution, schema validation, exact match); partial credit; format rewards | Design rewards for an invoice-extraction task; test them on adversarial outputs |
| 6.3 Reward hacking | Outputs that satisfy the checker but not the intent; monitoring samples during training | Plant a loophole in the reward; watch the model find it; close it |
| 6.4 Low-rank RL | RL needs little capacity: LoRA matched full fine-tuning even at rank 1 in Thinking Machines' experiments (2025); managed training APIs such as Tinker | Compare rank 1, 8 and 64 for your RL task |

**Check your understanding:** Why does RL with verifiable rewards suit extraction and code better than open-ended writing? How do you notice reward hacking before it reaches production? Why might SFT before RL help (as in Flipkart's relevance pipeline)?

### Chapter 7 · Distillation and synthetic data (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Knowledge distillation | Soft targets (Hinton et al., 2015) vs sequence-level distillation from teacher outputs | Distil a large model's labels into a small classifier and a small LLM; compare |
| 7.2 Synthetic data pipelines | Self-Instruct (Wang et al., 2022), explanation traces (Orca, 2023), textbook-quality data (Gunasekar et al., 2023); filtering by a verifier | Generate 5,000 examples from a teacher; filter with a checker; train |
| 7.3 Reasoning distillation | DeepSeek-R1's distilled 1.5B–70B models; what transfers and what does not | Distil reasoning traces for a narrow task into a 1.5B model; measure accuracy and tokens |
| 7.4 Terms and licences | Provider terms on using outputs to train competing models; base-model licences; attribution | Audit the legal basis of your synthetic dataset |

**Check your understanding:** Why does a distilled student sometimes beat its teacher on a narrow task? What does a verifier add to a synthetic data pipeline? Which licence terms must you check before distilling?

### Chapter 8 · Small models (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 The small-model landscape | Phi-3 (2024), Gemma 3 270M (Aug 2025), SmolLM3 (Jul 2025), small Qwen3 models; what small models are good and bad at | Benchmark three sub-4B models on your task before tuning |
| 8.2 Quantisation for deployment | GPTQ, AWQ, GGUF K-quants; accuracy vs memory vs speed | Quantise your tuned model three ways; plot quality vs tokens/s |
| 8.3 Edge and on-device | CPU and mobile inference, privacy benefits, offline use (deeper in [MLE404](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md)) | Run your tuned model on a laptop CPU through llama.cpp; report latency |
| 8.4 Indic small models | Translation and multilingual models from AI4Bharat (IndicTrans2) and Sarvam; tokenizer efficiency for Indic scripts | Fine-tune a small model for a Hindi or Tamil classification task; compare with a large prompted model |

**Check your understanding:** When is a fine-tuned classifier with no generation the best "small model"? Why might quantisation hurt a fine-tuned model more than its base? What does a better Indic tokenizer change for cost and quality?

### Chapter 9 · Evaluating fine-tunes (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Task evaluation | Held-out test sets, paired comparison with the prompted baseline at equal cost, error analysis (from [AIE305](../../year_3/AIE305_evaluating_llm_systems/README.md)) | Compare tuned vs prompted on 300 cases with a paired bootstrap |
| 9.2 Regression on general skills | lm-evaluation-harness and lighteval; catastrophic forgetting | Run a small general benchmark suite before and after tuning |
| 9.3 Safety regression | Fine-tuning, even on benign data, can weaken safety behaviour (Qi et al., 2023) | Run a refusal and harmful-request test set before and after; report changes |
| 9.4 Calibration and abstention | Confidence after tuning, "I don't know" behaviour | Measure accuracy vs coverage with a logprob threshold |

**Check your understanding:** Your tuned model wins on the task but loses 6 points on general reasoning. Ship or not? Why must safety be re-tested after a benign fine-tune? What is an "equal cost" comparison?

### Chapter 10 · Serving fine-tuned models (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Merge or keep adapters | Merged weights for one task; dynamic adapters for many tenants | Serve one merged model and one base + 3 adapters; compare |
| 10.2 Multi-LoRA serving | S-LoRA (Sheng et al., 2023; up to 4× throughput vs naive serving), vLLM LoRA support, LoRAX | Load-test 10 adapters on one GPU; plot throughput and p95 |
| 10.3 Cost per token | GPU hourly cost, utilisation, batch size → cost per million tokens; compare with API prices | Build the cost model; find the utilisation where self-hosting wins |
| 10.4 Versioning and rollback | Model registry, adapter versions, canary releases, shadow traffic | Roll out adapter v2 to 10% traffic; roll back on a metric breach |

**Check your understanding:** Why is multi-LoRA serving attractive for a SaaS with 200 customers? What utilisation do you need for self-hosting to beat an API? What must a model registry record?

### Chapter 11 · Fine-tuning operations and governance (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Reproducibility | Seeds, data snapshots, config files, experiment tracking (MLflow) | Reproduce a teammate's run from their config within 1% on the eval |
| 11.2 Model cards and licences | Documenting data, intended use, limits, evals; base-model licence obligations (Apache 2.0 vs custom community licences) | Write a model card for your P3 model |
| 11.3 Continuous improvement | Collecting new failure examples, periodic retraining, drift detection, avoiding feedback loops | Design the retraining loop with triggers and eval gates |
| 11.4 Regulation | Obligations for providers who modify models, data protection for training data, the right to erasure and its limits for trained weights (see [PRO301](../../../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md)) | Write the compliance section of a fine-tuning design doc |

**Check your understanding:** What would you need to rebuild a model you trained eight months ago? Why is deleting a user's data from a trained model hard, and what do you do about it? Which retraining trigger is too risky to automate?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Baseline ladder | Fine-tune-or-not memo |
| 2 | 2 | Lab 2 · Data sourcing and cleaning | — |
| 3 | 2 | Lab 2 (cont.): decontamination and labelling | **P1 due** · data card |
| 4 | 3 | Lab 3 · First SFT run and LR sweep | — |
| 5 | 4 | Lab 4 · LoRA from scratch; QLoRA run | — |
| 6 | 5 | Lab 5 · DPO and a variant | Mid-term (AI off): memory maths and design choices |
| 7 | 6 | Lab 6 · GRPO with executable rewards | — |
| 8 | 7 | Lab 7 · Distillation pipeline | — |
| 9 | 8 | Lab 8 · Small-model and quantisation bake-off | **P2 due** |
| 10 | 9 | Lab 9 · Task, general and safety regression | — |
| 11 | 10 | Lab 10 · Multi-LoRA serving and cost model | — |
| 12 | 11 | Lab 10 (cont.): Reproducibility drill | — |
| 13 | 11 | Lab 10 (cont.): model card and retraining loop | Model card |
| 14 | Integration | P3 demo day | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** writing training and data-cleaning scripts (Claude Code, Cursor, Copilot, Codex); generating synthetic examples under your filters; explaining training errors; producing first drafts of data and model cards.
- **Do without AI (drills):** compute GPU memory for full, LoRA and QLoRA tuning by hand; derive the DPO loss; read a loss curve and diagnose it; design a reward function and find its loopholes on paper; write the fine-tune-or-not memo from your own baseline numbers.
- **Verify AI output by:** checking that generated training code uses the right chat template and completion-only loss (print a batch); running decontamination before every training run; comparing every tuned model with the prompted baseline on the same test cases; sampling and reading outputs during training, not only metrics.
- **Where AI still fails here (show it):** assistants recommend fine-tuning for problems that retrieval solves (track their advice against your baseline ladder); generated scripts often mismatch chat templates between training and serving, silently degrading quality (catch it in Lab 3); synthetic datasets from one teacher lack diversity, which you can measure with embedding-cluster coverage; and code suggestions still reference unmaintained tools or closed managed APIs.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Memo, data card and model card | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can: (1) given a task and 2,000 raw examples, decide in writing whether to fine-tune, and if so deliver a cleaned, decontaminated dataset and a LoRA model that beats the best prompted baseline of equal serving cost on a held-out test (paired CI excludes zero), within two working days; (2) show that the tuned model's general-skill and safety regressions are within agreed limits; (3) serve it with a documented cost per million tokens and a rollback path.

## Industry reality

Fine-tuning is now mostly an open-weight activity. Hugging Face's TRL and PEFT, Unsloth and Axolotl are the common training stacks, and vLLM and LoRAX serve many adapters on one GPU. Managed services exist (for example Thinking Machines' Tinker training API, launched Oct 2025), while OpenAI's May 2026 wind-down of its fine-tuning platform shows the risk of depending on one vendor. Public case studies show where tuning pays: high-volume narrow tasks like relevance labelling at Flipkart (SFT followed by GRPO), and translation and Indic language tasks from AI4Bharat and Sarvam. Distillation of reasoning into small models became mainstream after DeepSeek-R1's distilled releases (2025). Small open models such as Gemma 3 270M and SmolLM3 target on-device and low-cost serving.

**Interview questions from this course**

1. *Product wants to fine-tune on our support docs so the bot "knows" them. Respond.* Strong answer: fine-tuning teaches behaviour and format better than facts; docs change, so use retrieval; propose a fine-tune only for tone, format or classification after a baseline ladder; data, eval and maintenance costs.
2. *Walk me through a LoRA fine-tune from raw logs to production.* Strong answer: consent and redaction, dedup, decontamination, labelling with agreement, chat template, completion-only loss, LR sweep, all-layer LoRA, held-out and regression evals, safety check, adapter serving, canary, rollback.
3. *DPO or GRPO for our task?* Strong answer: DPO for preference-shaped goals (tone, helpfulness) with pair data; GRPO or RFT when a checker can verify correctness (SQL, extraction, code); discusses reward hacking and length bias.
4. *Your fine-tuned model is better on the task but users report it refuses less. What happened?* Strong answer: fine-tuning can erode safety behaviour (Qi et al., 2023); run refusal and harmful-request suites; add safety examples or constrain with guardrails; make safety regression a release gate.
5. *Is self-hosting a fine-tuned 8B model cheaper than calling a frontier API?* Strong answer: builds the cost model (GPU price, utilisation, throughput, engineering time) vs API price per million tokens with caching and batch; finds the volume threshold; includes quality at equal cost and operational risk.

## Resources (free first)

- **Courses and guides:** Hugging Face LLM Course (fine-tuning chapters) — https://huggingface.co/learn/llm-course ; Hugging Face smol course — https://github.com/huggingface/smol-course ; Maxime Labonne's LLM Course — https://github.com/mlabonne/llm-course ; Stanford CS336 — https://cs336.stanford.edu/
- **Libraries:** TRL — https://huggingface.co/docs/trl/index (SFT — https://huggingface.co/docs/trl/sft_trainer , DPO — https://huggingface.co/docs/trl/dpo_trainer , GRPO — https://huggingface.co/docs/trl/grpo_trainer) ; PEFT — https://huggingface.co/docs/peft/index ; Unsloth — https://unsloth.ai/docs ; Axolotl — https://github.com/axolotl-ai-cloud/axolotl ; lm-evaluation-harness — https://github.com/EleutherAI/lm-evaluation-harness ; lighteval — https://github.com/huggingface/lighteval ; MLflow — https://mlflow.org/
- **Serving:** vLLM LoRA adapters — https://docs.vllm.ai/en/latest/features/lora/ ; LoRAX — https://github.com/predibase/lorax ; llama.cpp — https://github.com/ggml-org/llama.cpp
- **Data:** Argilla — https://github.com/argilla-io/argilla ; Label Studio — https://github.com/HumanSignal/label-studio ; Presidio — https://github.com/data-privacy-stack/presidio
- **Reading:** Thinking Machines, "LoRA Without Regret" — https://thinkingmachines.ai/blog/lora/ ; Gemma 3 270M — https://developers.googleblog.com/en/introducing-gemma-3-270m/ ; SmolLM3 — https://huggingface.co/blog/smollm3
- **Licences:** Gemma terms — https://ai.google.dev/gemma/terms ; Llama 4 licence — https://dev.meta.ai/llama/llama4/license

## Sources

- Zhao et al., "LoRA Land: 310 Fine-tuned LLMs that Rival GPT-4" (2024) — https://arxiv.org/abs/2405.00732 (checked 2026-10)
- OpenAI model optimization docs ("OpenAI is winding down the fine-tuning platform… no longer accessible to new users") — https://developers.openai.com/api/docs/guides/model-optimization ; deprecations page (developers notified 7 May 2026) — https://developers.openai.com/api/docs/deprecations (checked 2026-10)
- torchtune README ("no longer actively maintained") — https://github.com/meta-pytorch/torchtune (checked 2026-10)
- Flipkart Tech Blog, "LLMs for Relevance: Automating High-Quality Product Relevance Labeling in Flipkart Search" (Nov 2025) — https://blog.flipkart.tech/llms-for-relevance-automating-high-quality-product-relevance-labeling-in-flipkart-search-ddd5ca50b584 (checked 2026-10)
- DeepSeek-AI, DeepSeek-R1 (2025) — https://arxiv.org/abs/2501.12948 ; Shao et al., DeepSeekMath/GRPO (2024) — https://arxiv.org/abs/2402.03300 (checked 2026-10)
- Hu et al., LoRA (2021) — https://arxiv.org/abs/2106.09685 ; Dettmers et al., QLoRA (2023) — https://arxiv.org/abs/2305.14314 ; Biderman et al. (2024) — https://arxiv.org/abs/2405.09673 ; Liu et al., DoRA (2024) — https://arxiv.org/abs/2402.09353 ; Thinking Machines, "LoRA Without Regret" (29 Sept 2025) — https://thinkingmachines.ai/blog/lora/ ; Tinker announcement (1 Oct 2025) — https://thinkingmachines.ai/news/announcing-tinker/ (checked 2026-10)
- Ouyang et al. (2022) — https://arxiv.org/abs/2203.02155 ; Rafailov et al., DPO (2023) — https://arxiv.org/abs/2305.18290 ; Ethayarajh et al., KTO (2024) — https://arxiv.org/abs/2402.01306 ; Hong et al., ORPO (2024) — https://arxiv.org/abs/2403.07691 ; Meng et al., SimPO (2024) — https://arxiv.org/abs/2405.14734 (checked 2026-10)
- Zhou et al., LIMA (2023) — https://arxiv.org/abs/2305.11206 ; Hinton et al. (2015) — https://arxiv.org/abs/1503.02531 ; Wang et al., Self-Instruct (2022) — https://arxiv.org/abs/2212.10560 ; Mukherjee et al., Orca (2023) — https://arxiv.org/abs/2306.02707 ; Gunasekar et al. (2023) — https://arxiv.org/abs/2306.11644 (checked 2026-10)
- Abdin et al., Phi-3 (2024) — https://arxiv.org/abs/2404.14219 ; Gala et al., IndicTrans2 (2023) — https://arxiv.org/abs/2305.16307 (checked 2026-10)
- Qi et al., "Fine-tuning Aligned Language Models Compromises Safety" (2023) — https://arxiv.org/abs/2310.03693 (checked 2026-10)
- Sheng et al., S-LoRA (2023) — https://arxiv.org/abs/2311.03285 ; Frantar et al., GPTQ (2022) — https://arxiv.org/abs/2210.17323 ; Lin et al., AWQ (2023) — https://arxiv.org/abs/2306.00978 (checked 2026-10)

_Last reviewed: 2026-10_
