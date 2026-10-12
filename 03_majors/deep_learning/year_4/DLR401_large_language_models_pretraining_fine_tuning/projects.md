# DLR401 · Labs and projects

Every lab and project ships with configs, data-provenance notes (source and licence of every dataset), evaluation results with bootstrap confidence intervals, and a short model card for any model you train. Base models must have licences that permit your use; record them.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Licence and release audit | Audit 8 open model releases: licence, use restrictions, what is published (weights, code, data, checkpoints) | Audit table with quotes from each model card; a one-paragraph recommendation for a commercial Indic product | 2 h |
| 2 · WARC to clean text | Extract one Common Crawl WARC; language ID; Gopher/C4-style heuristics (with `datatrove` or your own code) | Stage-by-stage document and token counts; 50 removed and 50 kept documents with notes | 5 h |
| 3 · Dedup, decontamination and mixtures | MinHash LSH dedup; decontaminate against 5 benchmarks; a 2-mixture ablation at 20M parameters | Duplicate clusters found; contamination hits; mixture-ablation losses with 2 seeds | 5 h |
| 4 · Small pretraining run | ~100M model on 1–2B tokens on Kaggle 2× T4 with WSD schedule and checkpointing | Training report: tokens/s, MFU, loss curve, spikes and responses, evaluation on 3 tasks | 6 h |
| 5 · Long-context extension | RoPE scaling or YaRN from 1k to 4k context; a 3-level long-context test | Loss by position before/after; test results; failure examples | 4 h |
| 6 · SFT: masking, LoRA vs full | Correct chat template and loss masking; full vs LoRA fine-tune of a 0.5–1.5B base | Decoded batch showing loss masks; task gain and forgetting (base-benchmark drop) for both | 5 h |
| 7 · Reward model and best-of-n | Train a Bradley–Terry reward model; best-of-n with n up to 64 scored by a stronger "gold" judge | Held-out pair accuracy; proxy vs gold reward curve showing over-optimisation | 4 h |
| 8 · DPO and SimPO | Both on the same preference pairs; 3 seeds | Win rate (judge plus 50 human ratings), length shift, base-benchmark retention | 4 h |
| 9 · Verifiers and GRPO | A robust answer verifier tested on 50 adversarial outputs; GRPO on GSM8K with TRL | Verifier test report; reward, length and entropy curves; pass@1 and pass@k vs base | 8 h |
| 10 · Evaluation, safety and release | `lm-evaluation-harness` with 3 prompt formats; a contamination test on one public model; harmful-compliance and over-refusal rates before/after safety SFT | Score spread by format with CIs; contamination evidence or its absence; both safety rates; model card and release checklist | 7 h |

## Projects

### P1 · A Hindi web-data pipeline you can audit (L1, ~6 hours)

**Real-world inspiration.** FineWeb (Penedo et al., 2024) and FineWeb2 (2025) published every filtering decision and its effect on model quality; IndicLLMSuite (Khan et al., 2024) documents a pipeline for 22 Indian languages.

**What to build.** A pipeline that turns at least 5 Common Crawl WARC files into deduplicated, filtered Hindi text, with a report showing what each stage removed and why.

**Acceptance criteria**
- Stages: extraction, language ID (handling Devanagari and romanised Hindi separately), at least 5 heuristic filters, MinHash dedup (Jaccard ≥ 0.8), PII masking for phone numbers and email addresses, decontamination against at least 2 benchmarks.
- Document and token counts after every stage, with 20 random examples removed by each filter.
- Manual audit of 200 kept documents: share judged "good training text" is reported with a confidence interval; target ≥ 80%.
- The pipeline is re-runnable from a single command, and its output is deterministic given the inputs.

**Compute budget.** CPU only (a multi-core laptop or a free Kaggle CPU session); ≤ 1 GPU-hour for the optional classifier.

**Stretch goals.** Train a small fastText quality classifier on 1,000 hand-labelled documents and compare it with your heuristics; extend to Bengali.

**What it proves to an employer.** You can produce pretraining data that someone else can trust and audit, which is the most leveraged job in LLM training.

### P2 · SFT plus preference tuning of a small open model for Indian agricultural questions (L2, ~15 hours)

**Real-world inspiration.** Farmers' queries to the Kisan Call Centre (KCC) are published on India's Open Government Data platform (https://www.data.gov.in/catalog/kisan-call-centre-kcc-transcripts-farmers-queries-answers), showing the kinds of questions (pests, fertiliser, weather, schemes) that an assistant in Indian languages would need to handle. The assistant here is illustrative and is not for real agronomic advice without expert review.

**What to build.** Take a permissively licensed base model of 0.5–2B parameters. Build an SFT set of 2,000–5,000 Hindi (or another Indian language) question–answer pairs from openly licensed sources, with quality filtering. Train SFT (LoRA allowed), then DPO or SimPO on 1,000+ preference pairs that you generate on-policy and label with a rubric (AI-assisted labelling allowed, with 150 pairs labelled by humans to measure agreement).

**Acceptance criteria**
- Held-out evaluation of 200 questions with a rubric; scores for base, SFT and SFT+preference models with bootstrap 95% CIs; the final model beats SFT-only by a margin outside the interval or the write-up explains why not.
- Judge–human agreement on the 150 human-labelled pairs is reported (Cohen's κ).
- Retention: the drop on a general benchmark (a MILU subset in the same language) is ≤ 2 points, or the regression is explained and mitigated.
- Response length before and after preference tuning is reported, with a length-controlled comparison.
- A model card lists data sources, licences, intended use and known failure modes (including unsafe agronomic advice).
- Compute ≤ 15 GPU-hours.

**Stretch goals.** Code-switched Hinglish inputs; an over-refusal and harmful-advice evaluation set.

**What it proves to an employer.** You can run a full post-training pipeline with honest evaluation for a real Indian-language use case.

### P3 · A tiny reasoning model trained with verifiable rewards (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** DeepSeek-R1 (2025) and Tülu 3's RLVR (2024) made reinforcement learning with checkable rewards a standard post-training stage. Yue et al. (2025) showed that RLVR models often win at pass@1 while their base models win at large k, which raises the question of what RL actually adds. MGSM translates grade-school math problems into 10 languages, including Bengali and Telugu (Shi et al., 2022, https://arxiv.org/abs/2210.03057); GSM8K is at https://huggingface.co/datasets/openai/gsm8k.

**What to build.** Start from a permissively licensed base or instruct model of 0.5–1.5B parameters. Train with a GRPO-family algorithm (your choice of one stability fix: DAPO-style clipping, Dr. GRPO normalisation or GSPO sequence ratios) on GSM8K-style English problems plus a Bengali or Telugu subset. Write the verifier yourself and test it adversarially.

**Acceptance criteria**
- The verifier passes a 100-case adversarial test (extra text, multiple answers, units, LaTeX, native-script numerals) before training starts.
- pass@1 on held-out English and Indic test sets improves over the starting model by a margin larger than the 95% bootstrap interval.
- pass@k curves for k = 1…64 for base, RL model and (optionally) an SFT-distilled model; the write-up states whether your results agree with Yue et al.
- A reward-hacking audit: 100 random high-reward samples are inspected; any exploit (format gaming, answer guessing patterns) is documented, and the verifier is patched and re-tested if needed.
- Training curves for reward, response length, entropy and KL; at least one ablation of the chosen stability fix.
- Compute ≤ 30 GPU-hours on one 24–48 GB GPU, or a smaller model on Kaggle 2× T4; all runs logged.

**Stretch goals.** Compare with Olmo 3's published RL-Zero checkpoints at matched size; test whether gains transfer to a language not used in training.

**What it proves to an employer.** You can run the post-training stage that frontier labs depend on, evaluate it rigorously, and catch reward exploits. This is a strong portfolio piece for post-training and research-engineer roles.

## Feeds into

- [DLR403 Reinforcement Learning, Including RL for Language Models](../DLR403_reinforcement_learning_including_rl_for_language/README.md): the RL theory behind PPO, GRPO and reward hacking.
- [DLR404 Efficient Deep Learning and GPU Programming](../DLR404_efficient_deep_learning_and_gpu_programming/README.md): memory and kernel efficiency for fine-tuning and rollouts.
- [DLR501 Frontier Seminar](../../year_5/DLR501_frontier_seminar_interpretability_reasoning/README.md): reasoning models, test-time compute and interpretability of the models you trained.
- [OV05 AI Security and Safety Engineering](../../../../04_overlaps/OV05_ai_security_safety/README.md): safety evaluation and alignment at release.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): P3 is a strong starting point for a thesis on Indic reasoning models.
