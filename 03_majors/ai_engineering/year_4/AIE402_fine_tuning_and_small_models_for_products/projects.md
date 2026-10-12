# AIE402 · Labs and projects

Every lab and project ships a data card, training configs, seeds and the exact base-model revision, an evaluation notebook that compares against the best prompted baseline at equal serving cost, and a short model card. Use only data you have the right to train on, and record the licence of every base model and dataset. A free-tier or rented GPU with 16–24 GB of memory is enough for every lab; P3 may need a few hours on a larger rented GPU.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Baseline ladder | Zero-shot, few-shot, optimised-prompt and RAG baselines for one classification and one extraction task | Quality, cost and latency per rung; a fine-tune-or-not memo | 4 h |
| 2 · Data sourcing, cleaning, decontamination and labelling | Clean a 20k-example log export (dedup, PII redaction with Presidio, filters); decontaminate against the eval set; label 300 examples with a partner | Cleaning report, decontamination check that fails the build on overlap, κ, data card | 7 h |
| 3 · First SFT run and learning-rate sweep | Fine-tune a 1–3B model with TRL using completion-only loss; sweep the learning rate; print a training batch to verify the chat template | Loss curves, dev-eval curve, chosen settings with reasons | 5 h |
| 4 · LoRA from scratch and QLoRA | Implement a LoRA layer in PyTorch; compare attention-only vs all-layer LoRA; QLoRA-tune a 7–8B model; merge an adapter | Code, comparison table, memory measured vs computed | 6 h |
| 5 · DPO and a variant | Collect 500 preference pairs (judge + human spot checks); run DPO and one of KTO, ORPO or SimPO | Win rates, response-length and refusal-rate changes | 5 h |
| 6 · GRPO with executable rewards | Train a small model on SQL or arithmetic with an execution reward; plant and close a reward loophole; compare LoRA ranks 1, 8 and 64 | Reward curves, hacked samples, rank comparison | 6 h |
| 7 · Distillation pipeline | Generate 5,000 teacher examples, filter with a verifier, train a small student; audit the terms of use for teacher outputs | Student vs teacher quality and cost per 1k requests; legal-basis note | 5 h |
| 8 · Small-model and quantisation bake-off | Benchmark three sub-4B models; quantise your tuned model with GPTQ or AWQ and GGUF; run on a laptop CPU | Quality vs tokens/s plot; CPU latency report | 4 h |
| 9 · Task, general-skill and safety regression | Run the held-out task eval, a small lm-evaluation-harness suite and a refusal/harmful-request suite before and after tuning | Regression table with CIs; ship/no-ship note | 4 h |
| 10 · Serving, cost and reproducibility | Serve 10 adapters with vLLM or LoRAX; build the cost-per-million-tokens model; reproduce a teammate's run from config; write a model card and a retraining loop | Load-test results, cost model, reproduction log, model card | 8 h |

## Projects

### P1 · Should we fine-tune? A data-backed decision (L1, ~6 hours)

**Real-world inspiration.** LoRA Land found fine-tuned adapters beat GPT-4 on most of 31 tasks, but not all, and the losses are informative (Zhao et al., 2024). LIMA showed that about 1,000 carefully curated examples can go a long way (Zhou et al., 2023). Most teams skip the baseline ladder and regret it.

**What to build.** For an intent-classification task on customer messages in English, Hindi and Hinglish (start from the Bitext customer-support dataset and IndicSentiment, plus your own labelled additions), build the baseline ladder, a cleaned and decontaminated training set of 1,000–3,000 examples with a data card, and a written recommendation.

**Acceptance criteria**
- Four baseline rungs measured on the same 300-case held-out set, with cost per 1,000 requests and p95 latency.
- Training data passes dedup, PII redaction and decontamination checks (scripts included); 200 examples double-labelled with κ ≥ 0.7.
- The memo states the target the fine-tune must hit (quality and cost) and the conditions under which you would not fine-tune.

**Stretch goals.** Estimate the labelling budget needed to reach the target with a learning curve from 250/500/1,000 examples.

**What it proves to an employer.** You treat fine-tuning as an investment decision with evidence, not a reflex.

### P2 · A small invoice extractor that beats a large prompted model (L2, ~15 hours)

**Real-world inspiration.** Indian businesses process GST invoices with GSTINs, HSN codes and tax breakdowns in many layouts. High-volume narrow extraction is where tuned small models can win on cost and latency (LoRA Land, 2024). The data below is synthetic plus public samples; the task is illustrative.

**What to build.** Generate a synthetic but realistic invoice dataset (templated layouts, OCR noise, Hindi and English labels) plus at least 100 real public sample invoices you annotate. Fine-tune a 1–4B open model with LoRA or QLoRA to output a strict JSON schema. Serve it locally with vLLM or llama.cpp and compare it with a large prompted model using structured outputs.

**Acceptance criteria**
- Held-out test set of 300 invoices (at least 100 real); field-level F1 and whole-document exact match reported with CIs.
- The tuned model matches or beats the prompted large model on field F1 (paired bootstrap), at ≤ 25% of its cost per 1,000 documents and lower p95 latency.
- 100% schema-valid outputs (constrained decoding or validation), and a safety and general-skill regression check run and reported.
- Training is reproducible from config by a teammate within 1 F1 point.

**Stretch goals.** GRPO with a field-level reward after SFT; a CPU-only quantised build for offline branch offices.

**What it proves to an employer.** You can deliver the classic business case for small models, with cheaper, faster and measurably better results on a narrow task.

### P3 · A specialist model: distilled, RL-tuned and served at scale (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Flipkart described labelling search relevance with an LLM trained by supervised fine-tuning followed by GRPO (2025). DeepSeek distilled its R1 reasoning model into 1.5B–70B dense models (2025). Thinking Machines reported that RL fine-tuning needs very little adapter capacity (2025), and S-LoRA showed many adapters can share one GPU (2023). OpenAI's wind-down of its self-serve fine-tuning platform (May 2026) shows why owning the pipeline matters.

**What to build.** Choose one: (a) a text-to-SQL specialist for a public schema (Spider or BIRD), or (b) a product-relevance labeller for e-commerce queries and listings (built on public product data). Pipeline: teacher distillation with verifier filtering → SFT with LoRA → GRPO with an executable or rubric-based reward → evaluation (task, general skills, safety, calibration) → multi-LoRA serving alongside your P2 adapter → model card and retraining plan.

**Acceptance criteria**
- Each stage's contribution is measured on a held-out set (ablation table: base, +SFT, +distillation data, +GRPO) with CIs.
- The final model is within 3 points of the teacher (or beats it) at ≤ 10% of the teacher's cost per 1,000 requests.
- No reward hacking in 100 manually inspected samples; any found loophole is documented and closed.
- Serving two or more adapters on one GPU sustains a stated throughput at p95 under 1.5 s; cost per million tokens computed at three utilisation levels.
- Model card covers data provenance, licences, intended use, evals, limits and a retraining trigger policy.

**Stretch goals.** Run the RL stage through a managed training API and compare cost and results with your own GPU run; publish the adapter with its model card.

**What it proves to an employer.** You can run the full post-training pipeline end to end and justify every stage with numbers. Applied AI, model-customisation and inference teams look for exactly this.

## Feeds into

- [AIE403 LLMOps](../AIE403_llmops_observability_guardrails_cost_and_latency/README.md): self-hosted serving, canaries and cost engineering for your models.
- [AIE501 Frontier Seminar](../../year_5/AIE501_frontier_seminar_long_horizon_autonomous_agents/README.md) and [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): post-training experiments are common thesis topics.
- [MLE404 Efficient Inference](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md) and [DLR401 Large Language Models](../../../deep_learning/year_4/DLR401_large_language_models_pretraining_fine_tuning/README.md): deeper quantisation and training theory.

## Sources

- Zhao et al., LoRA Land (2024) — https://arxiv.org/abs/2405.00732 ; Zhou et al., LIMA (2023) — https://arxiv.org/abs/2305.11206 ; Sheng et al., S-LoRA (2023) — https://arxiv.org/abs/2311.03285 ; DeepSeek-R1 (2025) — https://arxiv.org/abs/2501.12948 (checked 2026-10)
- Flipkart Tech Blog, LLMs for relevance labelling (Nov 2025) — https://blog.flipkart.tech/llms-for-relevance-automating-high-quality-product-relevance-labeling-in-flipkart-search-ddd5ca50b584 ; Thinking Machines, "LoRA Without Regret" (Sept 2025) — https://thinkingmachines.ai/blog/lora/ (checked 2026-10)
- OpenAI deprecations page (fine-tuning notice, 7 May 2026) — https://developers.openai.com/api/docs/deprecations (checked 2026-10)
- Datasets: Bitext — https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset ; IndicSentiment — https://huggingface.co/datasets/ai4bharat/IndicSentiment ; Spider — https://yale-lily.github.io/spider ; BIRD — https://bird-bench.github.io/ (checked 2026-10)
- Tools: TRL — https://huggingface.co/docs/trl/index ; vLLM LoRA — https://docs.vllm.ai/en/latest/features/lora/ ; LoRAX — https://github.com/predibase/lorax ; Presidio — https://github.com/data-privacy-stack/presidio (checked 2026-10)
