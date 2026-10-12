# MLE501 · Frontier Seminar: ML Research Engineering and Reproducing Papers

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [MLE401](../../year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md), [MLE403](../../year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md) (taken alongside [RES501](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) and [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md)) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [OV11 AI for Science and Research Engineering](../../../../04_overlaps/OV11_ai_for_science_research_engineering/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

## Why this course matters now

AI agents now do real research-engineering work, which makes the human part sharper rather than smaller. On OpenAI's PaperBench (2025), the best agent achieved a 21.0% average replication score on 20 ICML 2024 papers; on a three-paper subset, ML PhDs reached 41.4% after 48 hours against 26.6% for the best model tested. METR's RE-Bench (2024) found the best agents scored about 4× higher than human experts with a 2-hour budget, humans narrowly ahead at 8 hours, and humans about 2× ahead at 32 hours. Sakana's AI Scientist-v2 produced a paper that scored above the acceptance threshold at an ICLR 2025 workshop (withdrawn by design). Meanwhile the field's infrastructure shifted: Papers with Code now redirects to Hugging Face's trending papers, and the ML Reproducibility Challenge runs as an official NeurIPS 2026 track. Long-horizon, open-ended work, deciding what to test, spotting a broken baseline, and knowing when a result is real, remains the research engineer's job. This seminar trains you to do that job at the level of a strong lab: read critically, reproduce exactly, extend carefully, and publish evidence others can trust.

## Learning outcomes

By the end you can:

1. **Read** an ML paper critically: separate claims from evidence, find missing baselines, and judge whether the experiments support the conclusion.
2. **Reproduce** a published result with a written protocol, a compute budget and a clear definition of "reproduced", and **diagnose** discrepancies.
3. **Build** research infrastructure (configs, sweeps, tracking, job arrays, result databases, plotting) that makes iteration fast and results traceable.
4. **Design** fair comparisons: compute-matched baselines, equal tuning budgets, seeds, confidence intervals, contamination checks.
5. **Run** small-scale proxy experiments and scaling studies, and **state** the risks of extrapolating them.
6. **Use** AI agents for literature search, coding and sweeps with verification protocols, and **explain** what current benchmarks say about their limits.
7. **Identify** open problems in ML engineering research and **frame** one as a thesis-sized question.
8. **Write** a reproduction report to the standard of the ML Reproducibility Challenge and **review** others' work constructively.

## Chapters and lessons

### Chapter 1 · Research engineering as a discipline (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What research engineers do | Turning ideas into experiments; infrastructure, baselines, ablations, scaling | Interview notes: compare two public descriptions of the role |
| 1.2 Habits of good training | "Become one with the data", overfit one batch, add complexity slowly (Karpathy, 2019) | Apply the recipe to a model you have never trained |
| 1.3 Tuning systematically | Google's Deep Learning Tuning Playbook: incremental tuning, exploration vs exploitation | Write a tuning plan for a fixed compute budget |
| 1.4 How scale shapes decisions | Scaling laws (Kaplan et al., 2020; Hoffmann et al., 2022) and why labs run small experiments first | Fit a 3-point scaling curve on a toy model |

**Check your understanding:** Why should you overfit a single batch before tuning? What does a tuning playbook protect you from? Why do labs trust small-scale experiments, and when shouldn't they?

### Chapter 2 · Reading papers critically (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Claims and evidence | Three-pass reading; mapping each claim to its table or figure | Claim–evidence map for one recent paper |
| 2.2 Troubling trends | Explanation vs speculation, unclear sources of gains, mathiness, misused language (Lipton and Steinhardt, 2018) | Find two such patterns in a paper of your choice |
| 2.3 Reproducibility failures | Deep RL variance (Henderson et al., 2018); recommender baselines (Ferrari Dacrema et al., 2019); benchmark variance (Bouthillier et al., 2021) | Present one failure and its lesson |
| 2.4 Metrics that create illusions | "Emergent abilities" (Wei et al., 2022) and the metric-choice critique (Schaeffer et al., 2023) | Debate: what would settle the question? |
| 2.5 Checklists | The NeurIPS paper checklist (16 questions; papers without it are desk-rejected) | Score two papers against the checklist |

**Check your understanding:** What evidence would distinguish "the method helps" from "the baseline was under-tuned"? Why can a metric choice create an apparent jump in capability? Which checklist item is most often answered weakly?

### Chapter 3 · Reproduction methodology (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Choosing a target | Feasibility, compute, data availability, code availability, what is at stake | Shortlist 3 papers; estimate compute for each |
| 3.2 Defining success | Exact numbers vs trends vs conclusions; tolerance from the paper's own variance | Write the success criteria before running anything |
| 3.3 Protocol | Environment, seeds, data versions, deviations log; contacting authors | Pre-register your reproduction protocol |
| 3.4 Debugging divergence | Bisecting differences: data, preprocessing, initialisation, optimiser, evaluation script | Diagnose a planted discrepancy in a provided reproduction |
| 3.5 The venues | ML Reproducibility Challenge (NeurIPS 2026 track, reviewed through TMLR); PaperBench's rubric approach | Read two accepted MLRC reports; list what made them convincing |

**Check your understanding:** Why define success before seeing results? Why is "the code runs and gives a number" not a reproduction? When is a failed reproduction a publishable result?

### Chapter 4 · Infrastructure for fast, traceable research (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Configs and sweeps | Hierarchical configs, sweep definitions, job arrays on Slurm | Launch a 50-run sweep from one command |
| 4.2 Results as data | Tracking runs (MLflow or W&B), result databases, plots generated from code | Regenerate every figure from stored results |
| 4.3 Fast iteration loops | Small proxies, cached data, short runs that predict long runs | Measure how well 10-minute runs rank configurations vs 2-hour runs |
| 4.4 A case study | The modded-nanogpt speedrun: from 45 minutes (2024 baseline) to under 40 seconds on 8×H100 (2026) through many small, measured changes | Read the record history; classify changes as optimiser, kernel, data or architecture |

**Check your understanding:** Why should figures never be edited by hand? When does a short proxy run mislead? What made the speedrun's progress trustworthy?

### Chapter 5 · Rigour: baselines, ablations and statistics (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Fair baselines | Equal tuning budgets, compute-matched comparisons, strong simple methods | Re-tune a paper's baseline with the method's budget |
| 5.2 Ablations | One change at a time; interaction effects; ablation tables that answer "why" | Design the ablation table before running experiments |
| 5.3 Statistics | Seeds, confidence intervals, multiple comparisons, effect sizes | Report a result with CIs over 5 seeds |
| 5.4 Contamination | Train–test overlap and benchmark contamination in LLM evaluation (Golchin and Surdeanu, 2023) | Run an n-gram overlap check between a training corpus and a benchmark |

**Check your understanding:** Why can a stronger baseline erase a paper's contribution? How many seeds are enough, and how do you decide? Why is contamination hard to rule out for closed models?

### Chapter 6 · Scaling and efficiency research (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Fitting scaling laws | Power-law fits, compute-optimal frontiers, uncertainty in extrapolation | Fit and extrapolate; report the prediction interval |
| 6.2 Transferring hyperparameters | µP / µTransfer (Yang et al., 2022) | Tune on a small width; transfer to a larger one |
| 6.3 Efficiency claims | Wall-clock vs FLOPs vs memory; hardware-specific results | Re-measure one efficiency claim on your hardware |
| 6.4 Compute accounting | Reporting GPU-hours, energy and cost for every experiment, including failed and exploratory runs | Add compute accounting to your tracking and report it weekly |

**Check your understanding:** Why are scaling-law extrapolations risky beyond one order of magnitude? What does µP change about how hyperparameters scale? Why can a FLOP reduction fail to speed up training?

### Chapter 7 · AI agents in research (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 What the benchmarks show | MLE-bench (best main-board entry 64.4% medal rate, Feb 2026), RE-Bench, PaperBench; METR time horizons and the gap between 50% and 80% reliability | Summarise what each benchmark does and does not measure |
| 7.2 Automated science systems | The AI Scientist (2024) and AI Scientist-v2 (2025); what their workshop result means and does not mean | Critique an AI-generated paper's experiments |
| 7.3 Agents as collaborators | Literature search, code, sweeps, plotting; verification protocols; keeping a human-readable log | Use an agent (Claude Code, Codex, Gemini CLI, AIDE) for one week of your project; audit every change |
| 7.4 Integrity | Disclosure of AI assistance, venue policies, data and licence terms | Write your project's AI-use statement |

**Check your understanding:** Why do agents beat humans at 2 hours but not at 32? What would convince you an AI-generated result is correct? What must a paper disclose about AI assistance?

### Chapter 8 · Open problems in ML engineering research (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Data | Data attribution (TRAK, 2023), label errors, deduplication, contamination | Pick one open question; write a one-page proposal |
| 8.2 Evaluation | Saturating benchmarks (the 2026 AI Index reports SWE-bench Verified going from 60% to near 100% in a year); evaluation under shift (from MLE304) | Propose a benchmark that would not saturate in a year |
| 8.3 Efficiency | Sub-4-bit inference, disaggregated serving, speculative decoding (from MLE404) | Identify one unmeasured trade-off |
| 8.4 Recommendation at scale | Generative recommenders, semantic IDs, interference in experiments (from MLE403) | Identify one claim that needs a stronger baseline |
| 8.5 ML for systems and privacy | Learned index structures (Kraska et al., 2017); differentially private training (Abadi et al., 2016) | Estimate the accuracy cost of DP-SGD on a small task |

**Check your understanding:** Which of these problems can a student make progress on with one GPU? Why does benchmark saturation matter for the whole field? What makes a problem "open" rather than merely unsolved by you?

### Chapter 9 · Writing, reviewing and releasing (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Writing | Structure, figures, related work, limitations; "research debt" and clear explanation (Distill, 2017) | Draft your reproduction report |
| 9.2 Reviewing | Writing a constructive review on OpenReview conventions | Review two classmates' drafts |
| 9.3 Releasing artefacts | Code, configs, checkpoints, model cards, licences | Prepare a release that reproduces your main table |
| 9.4 Talking about research | Talks, posters, blog posts; what you may and may not claim in public | Give a 5-minute lightning talk on your reproduction |

**Check your understanding:** What does a limitations section owe the reader? What makes a review useful to authors? Why release configs and not only code?

### Chapter 10 · Reproduce and extend (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Final experiments | Closing the reproduction; one extension experiment | Run the extension with seeds and CIs |
| 10.2 Presenting | Research talk, Q&A, defending choices | 15-minute talk |
| 10.3 Submitting | MLRC/TMLR format, arXiv, or a workshop | Submit or prepare a submission |
| 10.4 What comes next | Turning the extension into a thesis question, an open-source contribution or a product idea | Write a one-page next-steps memo for THS501 |

**Check your understanding:** Is your extension a new result or a re-measurement? What is the single most important limitation of your work? What would a sceptical reviewer ask first?

## Weekly rhythm

| Week | Chapter | Seminar and lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Two papers presented; Lab 1 · Karpathy recipe | — |
| 2 | 2 | Two papers presented; Lab 2 · Claim–evidence map | Reading log |
| 3 | 3 | Paper shortlist review | **P1 due** (critical review) |
| 4 | 3 | Lab 3 · Reproduction protocol | Pre-registered protocol |
| 5 | 4 | Lab 4 · Sweep and result pipeline | — |
| 6 | 5 | Lab 5 · Baseline re-tuning and ablations | — |
| 7 | 6 | Lab 6 · Scaling fit and µP | Mid-term check-in (AI off, oral) |
| 8 | 7 | Lab 7 · Agent audit | **P2 due** (infrastructure + first reproduction numbers) |
| 9 | 8 | Open-problems seminar 1 | — |
| 10 | 8 | Open-problems seminar 2 | Thesis-question proposal |
| 11 | 9 | Peer review workshop | Draft report |
| 12 | 10 | Extension experiments | — |
| 13 | 10 | Extension experiments | — |
| 14 | 10 | Talks | **P3 due** (reproduction report + release) |
| 15 | Review | Final talks and reviews | Oral exam (AI off) |

## Working with AI in this course

- **Use AI for:** literature search and summaries (verified against the paper), boilerplate for sweeps and plotting, porting code between frameworks, generating hypotheses for discrepancies, drafting text you then rewrite. Coding agents such as Claude Code, OpenAI Codex and Gemini CLI, and research agents such as AIDE, are allowed with logging.
- **Do without AI (drills):** the claim–evidence map; the success criteria and protocol; choosing baselines and ablations; interpreting results; the oral exam. These decisions must be yours and defensible in person.
- **Verify AI output by:** reproducing any number an assistant reports from your own logs; checking every citation exists and says what is claimed; diffing agent changes and rerunning tests; running small known-answer experiments before trusting new code; keeping a full log of AI contributions in the report.
- **Where AI still fails here:** benchmarks show agents fall behind humans on long, open-ended research tasks (RE-Bench at 8 and 32 hours, PaperBench against PhD baselines); assistants invent citations and paper details, silently change evaluation code, and over-claim from single runs. Lab 7 is an audit of one week of agent-assisted work.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Seminar presentations and reading log | 15% |
| Labs (7) | 15% |
| P1–P3 | 50% |
| Oral exam (AI off) | 20% |

**Mastery gate.** You pass when you: (1) complete a reproduction of a published ML result to a pre-registered standard, with every discrepancy diagnosed or bounded; (2) add one extension experiment with seeds and confidence intervals that a reviewer could rerun from your release; (3) in an AI-off oral exam, defend every design choice in your report and critique an unseen paper's evidence in 20 minutes.

## Industry reality

Research engineers and applied scientists work at AI labs, big-tech research groups, and product teams that adapt published methods. Their value lies in fast, trustworthy iteration, which is why benchmarks like MLE-bench, RE-Bench and PaperBench now measure exactly these tasks for AI systems. Reproductions are publishable: the ML Reproducibility Challenge is an official NeurIPS 2026 track, with papers reviewed through TMLR.

**Interview questions from this course**

1. *Walk me through a paper you reproduced. What didn't match, and why?* Strong answer: success criteria set in advance; specific discrepancies; how they were bisected; what was concluded and with what confidence.
2. *A new method beats the baseline by 1 point. What do you check before believing it?* Strong answer: tuning budgets, compute matching, seeds and CIs, evaluation code, data leakage or contamination, ablations, multiple comparisons.
3. *How would you set up infrastructure for a 3-month research project?* Strong answer: configs, tracking, sweeps, job scheduling, result storage, plots from code, small-proxy loops, checkpoints, a log of decisions.
4. *How do you use AI agents in research without losing rigour?* Strong answer: delegate bounded tasks, verify with tests and known-answer runs, diff and log changes, never accept unverified numbers or citations, disclose use.
5. *Pick an open problem in ML engineering and propose a first experiment.* Strong answer: precise question, why it matters, a feasible small-scale experiment, baselines, metrics, what result would change your mind.

## Resources (free first)

- **Reproducibility and rigour:** ML Reproducibility Challenge — https://reproml.org/ ; NeurIPS paper checklist — https://neurips.cc/public/guides/PaperChecklist ; Google, Deep Learning Tuning Playbook — https://github.com/google-research/tuning_playbook ; Karpathy, "A Recipe for Training Neural Networks" — https://karpathy.github.io/2019/04/25/recipe/ ; ML Retrospectives — https://ml-retrospectives.github.io/ ; Distill, "Research Debt" — https://distill.pub/2017/research-debt/
- **Courses:** Stanford CS197 Computer Science Research — https://web.stanford.edu/class/cs197/ ; Stanford CS336 — https://cs336.stanford.edu/
- **Finding papers:** arXiv; Hugging Face trending papers (successor to Papers with Code) — https://huggingface.co/papers/trending ; Semantic Scholar — https://www.semanticscholar.org/ ; OpenReview — https://openreview.net/ ; TMLR — https://jmlr.org/tmlr/
- **Reading list (core):** Kaplan et al. — https://arxiv.org/abs/2001.08361 ; Hoffmann et al. — https://arxiv.org/abs/2203.15556 ; Henderson et al. — https://arxiv.org/abs/1709.06560 ; Lipton and Steinhardt — https://arxiv.org/abs/1807.03341 ; Ferrari Dacrema et al. — https://arxiv.org/abs/1907.06902 ; Bouthillier et al. — https://arxiv.org/abs/2103.03098 ; Wei et al. — https://arxiv.org/abs/2206.07682 ; Schaeffer et al. — https://arxiv.org/abs/2304.15004 ; Yang et al., µTransfer — https://arxiv.org/abs/2203.03466 ; Golchin and Surdeanu — https://arxiv.org/abs/2308.08493 ; Park et al., TRAK — https://arxiv.org/abs/2303.14186 ; Kraska et al. — https://arxiv.org/abs/1712.01208 ; Abadi et al. — https://arxiv.org/abs/1607.00133 ; Sculley et al. — https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html ; D'Amour et al. — https://arxiv.org/abs/2011.03395 ; Northcutt et al. — https://arxiv.org/abs/2103.14749
- **AI agents and research:** MLE-bench — https://github.com/openai/mle-bench ; PaperBench — https://arxiv.org/abs/2504.01848 ; RE-Bench — https://arxiv.org/abs/2411.15114 ; METR time horizons — https://metr.org/time-horizons/ ; The AI Scientist — https://arxiv.org/abs/2408.06292 ; AI Scientist-v2 — https://arxiv.org/abs/2504.08066 ; AIDE — https://arxiv.org/abs/2502.13138 ; MLE-STAR — https://research.google/blog/mle-star-a-state-of-the-art-machine-learning-engineering-agents/ ; SWE-bench — https://www.swebench.com/

## Sources

- Starace et al., "PaperBench: Evaluating AI's Ability to Replicate AI Research" (arXiv 2504.01848, Apr 2025): 20 ICML 2024 papers, 8,316 gradable tasks; best agent 21.0%; PhD baseline 41.4% vs o1 26.6% on a 3-paper subset — https://arxiv.org/abs/2504.01848 (checked 2026-10)
- Wijk et al., RE-Bench (arXiv 2411.15114) and METR blog (22 Nov 2024) — https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/ (checked 2026-10)
- Sakana AI, "The AI Scientist Generates its First Peer-Reviewed Scientific Publication" (12 Mar 2025): ICLR 2025 ICBINB workshop, scores 6/7/6, withdrawn by protocol — https://sakana.ai/ai-scientist-first-publication/ (checked 2026-10)
- MLE-bench leaderboard (top entry 64.44% any medal, 23 Feb 2026) — https://github.com/openai/mle-bench (checked 2026-10)
- Papers with Code redirect to Hugging Face trending papers (verified 12 Oct 2026) — https://paperswithcode.com/ ; ML Reproducibility Challenge 2026 as a NeurIPS 2026 track — https://reproml.org/ ; NeurIPS 2026 paper checklist — https://neurips.cc/public/guides/PaperChecklist (checked 2026-10)
- modded-nanogpt record history (main track under 40 s on 8×H100, 30 Aug 2026; llm.c baseline 45 min, May 2024) — https://github.com/KellerJordan/modded-nanogpt (checked 2026-10)
- Stanford HAI, AI Index 2026 (SWE-bench Verified from 60% to near 100% in one year) — https://hai.stanford.edu/ai-index/2026-ai-index-report (checked 2026-10)
- Kwa et al., "Measuring AI Ability to Complete Long Tasks" (METR) — https://arxiv.org/abs/2503.14499 (checked 2026-10)

_Last reviewed: 2026-10_
