# MLE501 · Labs and projects

The seminar's projects build one piece of work: a critical review, then research infrastructure and first reproduction numbers, then a complete reproduction with one extension. Choose a paper from the last three years in an area this major covers (tabular or applied ML, ML systems, recommendation, efficient inference, distributed training, evaluation), with public data and a compute need you can afford (as a guide, under 200 GPU-hours). Every AI-assisted step is logged.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · The training recipe | Apply Karpathy's recipe to an unfamiliar model and dataset: inspect data, overfit one batch, add complexity step by step | A log of each step with plots; the bugs you found | 4 h |
| 2 · Claim–evidence map | Map every claim of a recent paper to its evidence; mark unsupported claims; score the paper on the NeurIPS checklist | Claim–evidence table; checklist scores | 3 h |
| 3 · Reproduction protocol | Pre-register your target numbers, tolerances, environment, seeds, compute budget and planned deviations | Protocol document, timestamped in your repository | 3 h |
| 4 · Sweep and result pipeline | Configs, a 50-run sweep on Slurm or a cloud equivalent, tracked runs, figures generated from stored results | One command that regenerates every figure | 5 h |
| 5 · Baseline re-tuning and ablations | Give the paper's baseline the same tuning budget as the method; design and run a 4-row ablation | Before/after baseline results; ablation table with CIs | 6 h |
| 6 · Scaling fit and µP | Fit a scaling curve from 3–5 small runs; try µTransfer from a small to a larger width | Fit with prediction interval; transfer results | 5 h |
| 7 · Agent audit | Use a coding or research agent for one week of project work; audit every change and number | Audit log: accepted, corrected and rejected agent contributions, with reasons | 4 h |

## Projects

### P1 · A critical review with a reproduction plan (L1, ~6 hours)

**Real-world inspiration.** Lipton and Steinhardt (2018) documented recurring weaknesses in ML papers; Henderson et al. (2018) and Ferrari Dacrema et al. (2019) showed results that did not survive careful re-examination. Reviewers at NeurIPS, ICML, ICLR and TMLR do this analysis for every submission.

**What to build.** A 3–4 page critical review of your chosen paper in the style of an OpenReview review (summary, strengths, weaknesses, questions, requested experiments), plus a one-page reproduction plan.

**Acceptance criteria**
- Every major claim is mapped to evidence, and at least two evidence gaps are identified with a concrete experiment that would close each.
- The baseline setup is assessed (tuning budget, compute match, seeds).
- The reproduction plan states what will count as success, the compute budget, and the main risks.
- Every citation is checked against the source; an assistant's summary, if used, is compared with the paper and errors are noted.

**Stretch goals.** Contact the authors with a precise question and report the exchange (with permission).

**What it proves to an employer.** You can read research the way a senior reviewer or research lead does.

### P2 · Research infrastructure and first reproduction numbers (L2, ~15 hours)

**Real-world inspiration.** The modded-nanogpt speedrun improved the same task from 45 minutes to under 40 seconds through many small changes, each measured against a fixed target; RE-Bench and MLE-bench measure agents on exactly this kind of iterative engineering. Fast, traceable iteration is what makes a research engineer productive.

**What to build.** The infrastructure for your reproduction (configs, sweeps, tracking, result storage, figure generation) and the first reproduction of the paper's main baseline and method at small scale.

**Acceptance criteria**
- One command launches any experiment in the protocol; one command regenerates all figures from stored results.
- Every run records code commit, config, data version, seed, hardware and wall-clock time.
- The paper's main baseline is reproduced at small scale within your pre-registered tolerance, or the gap is bisected to a specific cause.
- A deviations log lists every difference from the paper's setup, with reasons.
- A short proxy-vs-full study shows whether short runs rank configurations the same way as longer runs.

**Stretch goals.** A results dashboard; automatic detection of runs that diverge from the protocol.

**What it proves to an employer.** You can set up a research project so that a team can trust and extend its results.

### P3 · Reproduce and extend, with a public release (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** The ML Reproducibility Challenge publishes reproduction reports as an official NeurIPS 2026 track, reviewed through TMLR. On PaperBench (2025) the best agent scored 21.0% on average across 20 papers, so careful human reproduction remains valuable and publishable.

**What to build.** A complete reproduction of the paper's main result (or a clearly bounded subset) and one extension: a stronger baseline, a new dataset or distribution shift, a scaling point, an efficiency measurement, or an ablation the authors did not run. Write it up in MLRC or TMLR format and release code, configs and, where licences allow, checkpoints.

**Acceptance criteria**
- The report states the pre-registered success criteria and whether each was met, with seeds and confidence intervals.
- Every discrepancy is diagnosed or bounded, with the experiments that support the diagnosis.
- The extension answers a stated question and includes its own baseline and ablation.
- A stranger can reproduce the main table from the release on the stated hardware; a classmate confirms this.
- The report includes limitations, compute used (GPU-hours and cost), and an AI-assistance statement.
- A 15-minute talk with Q&A.

**Stretch goals.** Submit to the ML Reproducibility Challenge, a workshop or arXiv; open an issue or pull request upstream fixing a bug you found.

**What it proves to an employer.** You can produce research evidence other people trust, the defining skill of research engineers, applied scientists and anyone founding a technical company on new methods.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): your extension and the open-problem proposal from Chapter 8 can become the thesis.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): the shared course's reproduction work can use the same paper and infrastructure.
- [OV11 AI for Science and Research Engineering](../../../../04_overlaps/OV11_ai_for_science_research_engineering/README.md): research-software engineering and scientific ML build on this seminar.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): a published reproduction is strong evidence for research-engineering roles.
