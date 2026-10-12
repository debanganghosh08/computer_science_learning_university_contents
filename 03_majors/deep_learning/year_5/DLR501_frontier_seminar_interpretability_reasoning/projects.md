# DLR501 · Labs and projects

This is a seminar, so labs are weekly reproductions and projects build towards a research paper. Every lab ships a notebook or script that regenerates its figures, the exact model checkpoints and versions used, and a one-paragraph "what this does and does not show". Experiments on safety-relevant behaviour (refusal directions, misalignment) run only on open models in a local sandbox, and results are reported responsibly: describe effects and mitigations, not recipes for removing safeguards from deployed systems.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Claim audit | Table of every claim in one recent paper, its evidence, and what is missing (seeds, baselines, compute matching) | Audit table and a 300-word verdict | 3 h |
| 2 · Induction heads and IOI | Find induction heads in GPT-2 small and your own model; reproduce IOI name-mover heads with activation patching | Head scores, patching plots, comparison with the papers | 5 h |
| 3 · SAE training and evaluation | Train an SAE on a small model's activations; evaluate reconstruction, L0, downstream loss and auto-interpretation | Metrics table; 20 feature dashboards; dead-feature analysis | 6 h |
| 4 · Steering and refusal direction | Steering vectors on an open chat model; reproduce refusal-direction ablation in a sandbox | Effect sizes with side-effect measurements; a responsible-disclosure paragraph | 4 h |
| 5 · pass@k: RL vs distillation | Compare an RL-trained and a distilled open reasoning model of the same size, and their base | pass@k curves (k up to 128) with CIs; agreement or disagreement with Yue et al. (2025) | 4 h |
| 6 · Test-time scaling curves | Majority vote, best-of-n with a verifier, and budget forcing on a 1.5B reasoning model, binned by difficulty | Accuracy vs FLOPs per strategy and difficulty bin | 5 h |
| 7 · Hint-injection faithfulness | Insert hints into prompts; measure hint use and how often the chain of thought admits it | Reveal rates with CIs per hint type; comparison with Chen et al. (2025) | 4 h |
| 8 · Emergence replot and RL sigmoid fit | Re-plot a "sudden" capability with a continuous metric; fit a sigmoid to an RL reward curve | Two figures and a short note on what each fit predicts | 3 h |
| 9 · Overnight autoresearch loop and audit | Run an autoresearch-style agent loop on a small training script; re-test its top 5 claims with fresh seeds and frozen evaluation code | Loop log; table of claims that survived, failed, or exploited the setup | 6 h |
| 10 · Diffusion LM vs autoregressive | Compare a small open diffusion language model and an AR model on infilling and left-to-right tasks | Accuracy and speed table; one-page analysis | 3 h |

## Projects

### P1 · A reproduction report on one interpretability result (L1 of this seminar, ~6 hours)

**Real-world inspiration.** Interpretability results are often shown on one model and a few hand-picked examples. Independent reproductions on other models are some of the most useful contributions a newcomer can make, and the Open Problems paper (Sharkey et al., 2025) lists validation as a central open issue.

**What to build.** Reproduce one published result (induction heads, an IOI-style circuit, or a specific SAE feature family) on a different open model from the one in the paper.

**Acceptance criteria**
- The claim being reproduced is quoted exactly, with the paper's figure number.
- Causal validation: at least one patching or ablation experiment with a pre-stated metric, and a control (random heads or features).
- Results across at least 2 model sizes or 2 model families.
- A clear verdict (reproduced, partially reproduced, not reproduced) with reasons.

**Compute budget.** ≤ 4 GPU-hours on a free T4.

**Stretch goals.** Post the report publicly (blog or forum) and respond to comments.

**What it proves to an employer.** You can test someone else's claim carefully, which is the first job of any research engineer.

### P2 · Test-time compute vs model size for Indian-language math (L2 of this seminar, ~15 hours)

**Real-world inspiration.** Snell et al. (2024) found that compute-optimal test-time scaling can beat a 14× larger model on some problems, but such results are mostly measured in English. MGSM provides grade-school math problems in 10 languages, including Bengali and Telugu (Shi et al., 2022, https://arxiv.org/abs/2210.03057).

**What to build.** A study comparing a small reasoning model with extra test-time compute (majority vote, verifier-guided best-of-n, budget forcing) against a 4–8× larger model from the same family, on English and on Bengali or Telugu problems, at matched inference FLOPs.

**Acceptance criteria**
- Accuracy vs inference FLOPs curves for each strategy and language, with bootstrap CIs, binned by difficulty (defined by the larger model's pass rate).
- A clear statement, per language, of where the small model with test-time compute matches or beats the larger model, if anywhere.
- Language-specific analysis: tokenization cost per problem in each language and its effect on FLOPs.
- A 4-page write-up with limitations; compute ≤ 15 GPU-hours.

**Stretch goals.** Add a process reward model; test whether reasoning in English for non-English questions changes accuracy.

**What it proves to an employer.** You can design a compute-matched comparison and bring a multilingual angle that frontier papers often miss.

### P3 · Workshop paper (L3, portfolio-grade, ~30 hours in the sprint plus earlier proposal work)

**Real-world inspiration.** Workshops at ICLR, NeurIPS and ICML accept short papers on interpretability, reasoning, scaling and evaluation, and many research careers start with one. Reviews of past submissions are public on OpenReview, which lets you calibrate your work against the real bar.

**What to build.** A 4–6 page paper on a question from your Chapter 10 proposal. Suitable topics: an interpretability analysis of a model you trained in DLR401 or DLR403; a faithfulness or monitorability study of open reasoning models; a scaling or test-time compute study on Indian languages; an audit of automated research loops. Include code, data and a reproducibility statement.

**Acceptance criteria**
- Hypotheses and kill criteria were committed to the repository before the main experiments (timestamped).
- Every main result has at least 3 seeds or a bootstrap interval, and a control or baseline that a reviewer would ask for.
- A limitations section that names the strongest alternative explanation and how far you ruled it out.
- Two classmate reviews in conference format, and a written response with revisions.
- Every figure is regenerated by one command from logged results; total compute ≤ 30 GPU-hours (plus any approved research credits), with a compute log.
- Optional but encouraged: submission to a workshop or arXiv, following the venue's rules on dual submission.

**Stretch goals.** Release a dataset, benchmark or tool that others can use; present at a student research symposium.

**What it proves to an employer.** You can do research end to end: question, design, execution, writing and defence. This is the main signal for research-engineer and research-scientist roles and for PhD admissions.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502 Thesis or Capstone II](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is designed to grow into a thesis.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): the reproduction labs complement its methods.
- [OV05 AI Security and Safety Engineering](../../../../04_overlaps/OV05_ai_security_safety/README.md): faithfulness, monitoring and misalignment evaluation.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): your paper and reproductions become the core of a research portfolio.
