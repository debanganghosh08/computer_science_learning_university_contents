# DLR501 · Frontier Seminar: Interpretability, Reasoning Models and Scaling

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L3 → L5 | [DLR401](../../year_4/DLR401_large_language_models_pretraining_fine_tuning/README.md), [DLR403](../../year_4/DLR403_reinforcement_learning_including_rl_for_language/README.md) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md); taken alongside [RES501](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) and [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) |

## Why this course matters now

Three research questions now shape deep learning. **What is happening inside these models?** Interpretability has moved from toy models of superposition (2022) to sparse dictionaries with millions of features in production models (2024) and attribution graphs that trace computations in a deployed model (2025). The same field still lists many basic problems as open (Sharkey et al., 2025). **How do models reason, and can we trust what they say about it?** Reasoning models trained with RL use extra test-time compute. A compute-optimal allocation of that compute can beat a 14× larger model on some problems (Snell et al., 2024). Yet chain-of-thought often fails to mention the hints a model actually used, with reveal rates "often below 20%" (Chen et al., 2025). **What does scaling still buy, and what runs out?** Public human text may be fully used for training between 2026 and 2032 (Villalobos et al., 2022). RL compute follows predictable sigmoids (Khatri et al., 2025). AI agents now do part of AI research themselves. METR measured AI time horizons doubling about every seven months (Kwa et al., 2025). On PaperBench the best agent reached an average replication score of 21% on 20 ICML papers and did not outperform ML PhDs (Starace et al., 2025). Karpathy's autoresearch runs overnight agent experiments on a real training setup (2026). This seminar trains you to read, reproduce and extend frontier work at that level, and to judge claims with the rigour the field often lacks.

## Learning outcomes

By the end you can:

1. **Reproduce** a published interpretability result (induction heads, a known circuit, or SAE features) on an open model, and **validate** it with causal interventions.
2. **Train** a sparse autoencoder or transcoder on a small model and **evaluate** feature quality beyond reconstruction loss.
3. **Measure** test-time scaling (majority vote, best-of-n with verifiers, budget forcing) and **explain** when it beats a larger model.
4. **Test** chain-of-thought faithfulness and monitorability with controlled hint injection.
5. **Critique** scaling claims (emergence, data limits, RL scaling, AI research automation) using the original data and methods.
6. **Run** an autonomous experiment loop and **audit** its claims for validity.
7. **Write** a workshop-quality paper and a peer review in conference format.

## Format

Each week has one theme, 2–3 required papers, a 20-minute student presentation with a "claims vs evidence" slide, a hands-on reproduction lab, and a written response. Chapters 1–10 run in weeks 1–11. Weeks 12–14 are a research sprint ending in a workshop-style paper.

## Chapters and lessons

### Chapter 1 · How to read and reproduce frontier work (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Claims vs evidence | Separating the headline from what was measured; baselines, compute matching, seeds | "Claim audit" of one recent arXiv paper: every claim, its evidence, what is missing |
| 1.2 Reproduction plans | Minimum viable reproduction; the smallest scale where the effect should appear | Write a reproduction plan for one paper in this reading list |
| 1.3 Benchmarks and leaderboards | Contamination, prompt sensitivity, private test sets; "The Leaderboard Illusion" | Re-score one leaderboard result with a different prompt format |
| 1.4 Research taste | Choosing problems by importance, tractability and your comparative advantage; small-scale proxies for big questions | Rank 5 candidate projects with a written rationale |

**Check your understanding:** Which single missing detail most often blocks reproductions in deep learning papers? Why is "state of the art on benchmark X" weak evidence on its own? How small can a reproduction be and still test the claim?

### Chapter 2 · Mechanistic interpretability I: circuits (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 The residual stream view | Attention heads and MLPs reading from and writing to a shared stream; logit lens | Logit-lens plots for GPT-2 small with TransformerLens |
| 2.2 Induction heads | Previous-token and induction heads; in-context learning (Olsson et al., 2022) | Find induction heads in GPT-2 small and in your DLR303 model |
| 2.3 Circuits in the wild | Indirect object identification (Wang et al., 2022) | Reproduce the IOI name-mover heads |
| 2.4 Causal methods | Activation patching, path patching, attribution patching; best practices (Zhang and Nanda, 2023) | Patching experiment with two metrics; show they can disagree |

**Check your understanding:** Why is activation patching evidence of causation and attention maps are not? What makes a circuit explanation "complete"? How would you detect that two components are redundant backups?

### Chapter 3 · Mechanistic interpretability II: superposition and dictionaries (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Superposition | More features than dimensions; toy models (Elhage et al., 2022) | Reproduce the toy-model phase diagram at small scale |
| 3.2 Sparse autoencoders | Dictionary learning on activations (Cunningham et al., 2023; "Towards Monosemanticity", 2023); scaling to production models ("Scaling Monosemanticity", 2024) | Train an SAE on a small model's MLP outputs |
| 3.3 Open SAEs and evaluation | Gemma Scope (Lieberum et al., 2024); dead features, feature splitting, interpretability scoring | Evaluate your SAE: reconstruction, sparsity, downstream loss, auto-interpretation |
| 3.4 Attribution graphs | Transcoders and circuit tracing on a deployed model ("On the Biology of a Large Language Model", 2025) | Trace one multi-step computation with an open circuit-tracing tool |

**Check your understanding:** Why can low reconstruction loss coexist with a useless dictionary? What does feature splitting tell you about the "true" features? What can an attribution graph not show?

### Chapter 4 · Using interpretability (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Steering | Representation engineering (Zou et al., 2023); steering vectors | Steer a small chat model along a sentiment direction; measure side effects |
| 4.2 Refusal and safety directions | "Refusal is mediated by a single direction" (Arditi et al., 2024) | Reproduce refusal-direction ablation on an open model in a sandbox |
| 4.3 Probes and their limits | Linear probes, control tasks, probing vs causal use | Probe for a property; then test whether the model uses it |
| 4.4 Learning dynamics | Grokking and progress measures (Nanda et al., 2023) | Reverse-engineer a modular-addition network |

**Check your understanding:** Why is a high-accuracy probe not proof that the model uses that information? What safety questions does the refusal-direction result raise for open-weight releases? What would make a steering result reliable enough to deploy?

### Chapter 5 · Reasoning models I: from chain-of-thought to RL (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Prompted reasoning | Chain-of-thought (Wei et al., 2022), self-consistency (Wang et al., 2022) | Measure CoT gains vs model size on a small benchmark |
| 5.2 Supervising the process | Outcome vs process reward models ("Let's Verify Step by Step", Lightman et al., 2023); Math-Shepherd | Train a small outcome verifier; compare with majority vote |
| 5.3 Bootstrapping | STaR (Zelikman et al., 2022) and its descendants | One STaR iteration on a small model |
| 5.4 RL-trained reasoning | OpenAI's o1 announcement (Sep 2024); DeepSeek-R1 (2025); Olmo 3 Think (2025); what RL adds vs distillation (Yue et al., 2025) | pass@k for RL-trained vs distilled open models of the same size |

**Check your understanding:** Why does self-consistency help even without any training? What is the practical difference between a process and an outcome reward model? Why might distillation from a strong reasoner add capabilities that RL on the student does not?

### Chapter 6 · Reasoning models II: test-time compute (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Compute-optimal test-time scaling | Allocating compute by difficulty; beating a larger model on some problems (Snell et al., 2024) | Difficulty-binned scaling curves for a 1.5B model |
| 6.2 Repeated sampling | Coverage grows with samples ("Large Language Monkeys", Brown et al., 2024); verifier bottleneck | Coverage vs n up to 256 with and without a verifier |
| 6.3 Budget forcing | s1's 1,000 examples and "Wait" tokens (Muennighoff et al., 2025) | Reproduce budget forcing on an open reasoning model |
| 6.4 Inference scaling laws | Compute-optimal inference (Wu et al., 2024); cost per solved problem | Plot accuracy against FLOPs for 4 strategies |

**Check your understanding:** Why does test-time compute help most on medium-difficulty problems? When does more sampling stop helping without a better verifier? How would you price a reasoning model's answer versus a larger model's?

### Chapter 7 · Faithfulness, monitoring and misalignment (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Faithfulness | Hint-reveal rates "often below 20%" (Chen et al., 2025) | Hint-injection test on an open reasoning model |
| 7.2 Monitorability | CoT monitoring as a "new and fragile opportunity" (Korbak et al., 2025); obfuscation under optimisation (Baker et al., 2025) | Train a monitor; test it on obfuscated vs plain traces |
| 7.3 Misalignment results | Alignment faking (Greenblatt et al., 2024); sleeper agents (Hubinger et al., 2024); emergent misalignment (Betley et al., 2025); reward-hacking generalisation (MacDiarmid et al., 2025) | Presentation: what each experiment does and does not show |
| 7.4 Oversight | Weak-to-strong generalisation (Burns et al., 2023) | Reproduce a small weak-to-strong experiment |

**Check your understanding:** Why does an unfaithful chain of thought not make chain-of-thought monitoring useless? What experimental design separates "the model is deceptive" from "the model follows a prompt"? Why does training against a monitor risk destroying the monitor's value?

### Chapter 8 · Scaling I: laws, limits and data (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Scaling-law recap | Kaplan vs Chinchilla, reconciled (Pearce and Song, 2024); inference-aware sizing | Re-plot published scaling data; extrapolate |
| 8.2 Emergence | Emergent abilities as metric artefacts (Schaeffer et al., 2023) | Replot a "sudden" ability with a continuous metric |
| 8.3 Data limits | Exhausting public human text (Villalobos et al., 2022); repetition (Muennighoff et al., 2023); synthetic data | Estimate how many epochs your favourite open model's data implies |
| 8.4 New scaling axes | Precision (Kumar et al., 2024); RL compute (Khatri et al., 2025); long context and sparse attention (DeepSeek-V4, 2026) | Fit a sigmoid to an RL curve and a power law to a pretraining curve; compare |

**Check your understanding:** Why do discontinuous metrics create apparent emergence? If data runs out, which of the scaling axes in this chapter can continue, and at what cost? What would make you trust a scaling law fitted on a new axis?

### Chapter 9 · Scaling II: AI that does AI research (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Measuring autonomy | METR time horizons (Kwa et al., 2025; current values on the [market map](../../../../06_career_and_market_readiness/01_market_map/README.md)); RE-Bench | Read METR's caveats; list what the metric does not capture |
| 9.2 Replicating papers | PaperBench (best average replication score 21%; models did not beat the human baseline); MLE-bench; The AI Scientist | Run one open replication agent on a small paper; grade it with the rubric |
| 9.3 Autonomous experiment loops | Karpathy's autoresearch (2026): agents edit `train.py`, train 5 minutes, keep or discard | Run an autoresearch-style loop overnight on your DLR304 setup |
| 9.4 Auditing automated research | Seed noise, leakage, evaluation exploits (Sakana AI, 2025), p-hacking at machine speed | Re-test the loop's top 5 claims; report which survive |

**Check your understanding:** What does a 50% time horizon of several hours mean, and not mean, for a research engineer's job? Why are automated loops especially prone to overfitting the validation set? Which research skills become more valuable when experiments get cheap?

### Chapter 10 · Open problems and new directions (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Beyond autoregressive transformers | Diffusion language models (LLaDA, Nie et al., 2025); state-space hybrids; test-time memory (Titans, Behrouz et al., 2024) | Compare a small diffusion LM and an AR model on infilling |
| 10.2 Open problems in interpretability | The agenda in Sharkey et al. (2025) | Choose one open problem; write a 1-page attack plan |
| 10.3 Research proposals | Question, hypothesis, minimum experiment, kill criteria | 2-page proposal for the sprint, reviewed by two classmates |
| 10.4 Responsible publication | Dual-use results, responsible disclosure, norms for safety-relevant findings | Write the disclosure section of your proposal |

**Check your understanding:** What evidence would show that a non-transformer architecture is better, rather than just different? Which open problem in your proposal could be tested at small scale? What result would make you abandon your project?

### Chapter 11 · Research sprint (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Executing | Pre-registered hypotheses, ablations, seeds, compute log | Run the sprint experiments |
| 11.2 Writing | Workshop paper structure; figures that carry the argument; limitations | 4–6 page paper |
| 11.3 Reviewing | Conference-style review (summary, strengths, weaknesses, questions, score) | Two reviews of classmates' papers |
| 11.4 Presenting | Workshop talks and posters; handling hard questions | 10-minute talk with 5 minutes of questions |

**Check your understanding:** Which of your results would survive a reviewer asking for one more seed? What is the single figure that makes your paper's point? What did you leave out, and is that honest?

## Reading list (core; all free)

| Theme | Papers and links |
|---|---|
| Circuits | Induction heads — https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html ; IOI circuit — https://arxiv.org/abs/2211.00593 ; activation patching best practices — https://arxiv.org/abs/2309.16042 |
| Superposition and dictionaries | Toy models of superposition — https://transformer-circuits.pub/2022/toy_model/index.html ; Towards Monosemanticity — https://transformer-circuits.pub/2023/monosemantic-features/index.html ; Scaling Monosemanticity — https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html ; SAEs (Cunningham et al.) — https://arxiv.org/abs/2309.08600 ; Gemma Scope — https://arxiv.org/abs/2408.05147 ; On the Biology of a Large Language Model — https://transformer-circuits.pub/2025/attribution-graphs/biology.html ; Open Problems in Mechanistic Interpretability — https://arxiv.org/abs/2501.16496 |
| Using internals | Representation engineering — https://arxiv.org/abs/2310.01405 ; refusal direction — https://arxiv.org/abs/2406.11717 ; grokking progress measures — https://arxiv.org/abs/2301.05217 |
| Reasoning | Chain-of-thought — https://arxiv.org/abs/2201.11903 ; self-consistency — https://arxiv.org/abs/2203.11171 ; Let's Verify Step by Step — https://arxiv.org/abs/2305.20050 ; STaR — https://arxiv.org/abs/2203.14465 ; Learning to reason with LLMs (OpenAI, 2024) — https://openai.com/index/learning-to-reason-with-llms/ ; DeepSeek-R1 — https://arxiv.org/abs/2501.12948 ; Olmo 3 — https://arxiv.org/abs/2512.13961 ; RLVR limits — https://arxiv.org/abs/2504.13837 |
| Test-time compute | Snell et al. — https://arxiv.org/abs/2408.03314 ; Large Language Monkeys — https://arxiv.org/abs/2407.21787 ; s1 — https://arxiv.org/abs/2501.19393 ; inference scaling laws — https://arxiv.org/abs/2408.00724 |
| Faithfulness and misalignment | CoT faithfulness — https://arxiv.org/abs/2505.05410 ; CoT monitorability — https://arxiv.org/abs/2507.11473 ; obfuscated reward hacking — https://arxiv.org/abs/2503.11926 ; alignment faking — https://arxiv.org/abs/2412.14093 ; sleeper agents — https://arxiv.org/abs/2401.05566 ; emergent misalignment — https://arxiv.org/abs/2502.17424 ; reward hacking in production RL — https://arxiv.org/abs/2511.18397 ; weak-to-strong — https://arxiv.org/abs/2312.09390 |
| Scaling | Kaplan — https://arxiv.org/abs/2001.08361 ; Chinchilla — https://arxiv.org/abs/2203.15556 ; reconciliation — https://arxiv.org/abs/2406.12907 ; emergence mirage — https://arxiv.org/abs/2304.15004 ; data limits — https://arxiv.org/abs/2211.04325 ; precision — https://arxiv.org/abs/2411.04330 ; RL scaling — https://arxiv.org/abs/2510.13786 ; DeepSeek-V4 — https://arxiv.org/abs/2606.19348 ; The Bitter Lesson (Sutton, 2019) — http://www.incompleteideas.net/IncIdeas/BitterLesson.html |
| AI doing AI research | METR time horizons — https://arxiv.org/abs/2503.14499 and https://metr.org/time-horizons/ ; RE-Bench — https://arxiv.org/abs/2411.15114 ; PaperBench — https://arxiv.org/abs/2504.01848 ; MLE-bench — https://arxiv.org/abs/2410.07095 ; The AI Scientist — https://arxiv.org/abs/2408.06292 ; KernelBench — https://arxiv.org/abs/2502.10517 ; autoresearch — https://github.com/karpathy/autoresearch |
| New directions | LLaDA — https://arxiv.org/abs/2502.09992 ; Mamba — https://arxiv.org/abs/2312.00752 ; Titans — https://arxiv.org/abs/2501.00663 |

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Claim audit | Audit of one paper |
| 2 | 2 | Induction heads and IOI | Reproduction notebook |
| 3 | 3 | SAE training and evaluation | **P1 due** |
| 4 | 4 | Steering and refusal direction | Response paper |
| 5 | 5 | pass@k: RL vs distillation | — |
| 6 | 6 | Test-time scaling curves | Scaling report |
| 7 | 7 | Hint-injection faithfulness | Mid-term oral (AI off) |
| 8 | 8 | Emergence replot; RL sigmoid fit | — |
| 9 | 9 | Overnight autoresearch loop and audit | **P2 due** |
| 10 | 10 | Diffusion LM vs AR | Proposal draft |
| 11 | 10 | Proposal review | Final proposal |
| 12 | 11 | Sprint | Experiment log |
| 13 | 11 | Sprint | Paper draft and reviews |
| 14 | 11 | Sprint | **P3 due** |
| 15 | Review | Mini-workshop: talks and poster session | Final oral (AI off) |

## Working with AI in this course

- **Use AI for:** literature search and first-pass summaries (always checked against the paper); code for experiments you have specified; running autonomous experiment loops as hypothesis generators; drafting reviews you then rewrite; auto-interpreting SAE features (scored against held-out activations).
- **Do without AI (drills):** the "claims vs evidence" slide for every presentation; derivations behind each week's method; experimental design and kill criteria; the mid-term and final orals.
- **Verify AI output by:** (1) checking every cited claim against the paper's own figures and tables; (2) re-running every automated-loop "improvement" with fresh seeds and untouched evaluation code; (3) validating interpretability claims with causal interventions, not only correlations; (4) reporting confidence intervals for every number in your paper.
- **Where AI still fails here:** this course measures it directly. On PaperBench, the best agent's average replication score was 21% and it did not beat human ML PhDs (Starace et al., 2025). In Lab 9 you will record how many of an automated loop's claimed gains survive re-testing, and in your weekly responses you will log every factual error an AI summary made about a paper you read.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Presentations and written responses | 20% |
| Labs (reproductions) | 20% |
| Projects P1–P2 | 20% |
| P3 workshop paper and reviews | 30% |
| Orals (AI off) | 10% |

**Mastery gate.** You pass when you can: (1) present any paper on the reading list for 20 minutes and answer questions on its methods and weaknesses without notes; (2) reproduce one interpretability or reasoning result at small scale with causal or statistical validation; (3) produce a workshop-quality paper whose main claim survives two peer reviews and an oral defence, with code that reproduces every figure.

## Industry reality

Interpretability, reasoning and scaling are now hiring areas at frontier labs and research groups. The DLR market page lists interpretability as a growing area, along with research taste and experimental rigour as skills "growing in value" ([DLR market page](../../../../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md)). Anthropic publishes its interpretability research openly (transformer-circuits.pub), and Google DeepMind released Gemma Scope's open SAEs. Research interviews centre on a talk about your own work and a discussion of papers.

**Interview questions from this course**

1. *Tell us about a result you reproduced that did not hold up.* Strong answer: precise claim, setup, what differed, how it was diagnosed (seeds, scale, a hidden detail), what was learned, and how it changed the next experiment.
2. *How would you test whether a feature found by an SAE is real and used by the model?* Strong answer: activation examples beyond the top ones, held-out auto-interpretation scoring, ablation and steering with measured behavioural effects, controls for dead or split features.
3. *Does test-time compute make pretraining scale less important?* Strong answer: compute-optimal test-time results depend on difficulty and base capability; verifier bottlenecks; costs per query; complementarity with pretraining; cites evidence.
4. *Can we rely on chain-of-thought monitoring for safety?* Strong answer: useful but not sufficient; faithfulness rates; obfuscation under optimisation pressure; keep monitors out of the training reward; combine with other evaluations.
5. *An agent says it found a 10% training speed-up overnight. What do you do?* Strong answer: re-run with fresh seeds and identical evaluation; inspect the diff for changes to evaluation or data; check tuning parity and compute matching; ablate each change; only then adopt.

## Resources (free first)

- **Curricula:** ARENA (mechanistic interpretability and RL exercises) — https://arena.education/ ; Neel Nanda's getting-started guide — https://www.neelnanda.io/mechanistic-interpretability/getting-started ; Stanford CS336 — https://cs336.stanford.edu/
- **Tools:** TransformerLens — https://github.com/TransformerLensOrg/TransformerLens ; TRL — https://github.com/huggingface/trl ; `lm-evaluation-harness` — https://github.com/EleutherAI/lm-evaluation-harness
- **Research venues:** Transformer Circuits Thread — https://transformer-circuits.pub/ ; METR — https://metr.org/time-horizons/ ; OpenReview (reviews of past ICLR and NeurIPS papers) — https://openreview.net/
- **Compute (free):** interpretability labs on GPT-2 small and 1–2B open models fit a Colab or Kaggle T4; test-time scaling labs use a 1.5B reasoning model with short generations. Researchers can apply to Google's TPU Research Cloud — https://sites.research.google/trc/about/

## Sources

- Snell et al., "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters" (2024) — https://arxiv.org/abs/2408.03314 (checked 2026-10)
- Chen et al., "Reasoning Models Don't Always Say What They Think" (2025) — https://arxiv.org/abs/2505.05410 (checked 2026-10)
- Sharkey et al., "Open Problems in Mechanistic Interpretability" (2025) — https://arxiv.org/abs/2501.16496 (checked 2026-10)
- Villalobos et al., "Will we run out of data?" (2022, revised) — https://arxiv.org/abs/2211.04325 (checked 2026-10)
- Khatri et al., "The Art of Scaling Reinforcement Learning Compute for LLMs" (2025) — https://arxiv.org/abs/2510.13786 (checked 2026-10)
- Kwa et al., "Measuring AI Ability to Complete Long Software Tasks" (2025) — https://arxiv.org/abs/2503.14499 (checked 2026-10)
- Starace et al., "PaperBench" (2025) — https://arxiv.org/abs/2504.01848 (checked 2026-10)
- Karpathy, autoresearch (Mar 2026) — https://github.com/karpathy/autoresearch (checked 2026-10)
- Sutton, "The Bitter Lesson" (2019) — http://www.incompleteideas.net/IncIdeas/BitterLesson.html (site unreachable when checked on 2026-10-12)

_Last reviewed: 2026-10_
