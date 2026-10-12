# DSC501 · Labs and projects

This is a seminar, so labs are **replication sprints**: each reproduces a central result or diagnostic from that week's papers in 3–5 hours. Projects are research-grade. Every submission includes a reproducibility package (pinned environment, data access instructions, one command to rebuild every number) and a short "what would change my conclusion" section. AI tools may be used throughout except where marked; agent-generated analyses must ship with their logs.

## Labs (replication sprints)

| Sprint | Goal | You submit | Time |
|---|---|---|---|
| 1 · Prior predictive and SBC | Prior predictive checks and simulation-based calibration for a hierarchical binomial model | Rank histograms; a prior you rejected and why | 4 h |
| 2 · Three PPLs, funnels and VI | The same hierarchical model in PyMC, Stan (CmdStanPy or brms) and NumPyro; fix divergences with a non-centred parameterisation; compare ADVI with NUTS | Comparison table with matching posteriors; before/after diagnostics; where VI was wrong | 7 h (2 weeks) |
| 3 · MRP | Multilevel regression and post-stratification from a non-representative sample to state estimates | Estimates vs a benchmark source; sensitivity to the post-stratification table | 4 h |
| 4 · DML from scratch (AI off for the derivation) | Derive the partially linear orthogonal score; implement cross-fitted DML; match DoubleML | Derivation; code; matched estimates | 4 h |
| 5 · 401(k) replication | Reproduce the DML 401(k) eligibility estimates with several learners | Estimates and intervals by learner; comparison with the published values | 3 h |
| 6 · Causal forests and RATE | Causal forest and DR-learner on an experiment; RATE evaluation; policy value under a budget | RATE with intervals; learned policy and its estimated value | 4 h |
| 7 · Conformal and PPI | Conformal intervals for a forecaster under shift; counterfactual intervals; PPI for a regression coefficient | Coverage tables; interval widths vs baselines | 3 h |
| 8 · Surrogate index | Simulated long-term retention with short-term surrogates; bias when the surrogate assumption fails | Bias table across scenarios | 3 h |
| 9 · Agent evaluation | Run two data-science agents on five tasks drawn from your past projects; classify failures | Task specs, scores, failure taxonomy | 5 h |
| 10 · Silicon samples | Compare LLM-simulated survey answers with real survey margins and subgroups | Comparison plots; a written validity assessment | 3 h |

## Projects

### P1 · A complete Bayesian workflow report (~6 hours)

**Real-world inspiration.** Gelman et al.'s "Bayesian Workflow" (2020) argues that real Bayesian analysis is a loop of building, checking and comparing models, not a single fit. Few published analyses show the full loop; this project does.

**What to build.** Take the hierarchical model from DSC301 P3 (or another hierarchical model you built) and produce a workflow report: prior predictive checks, SBC, computation diagnostics, posterior predictive checks, at least two model expansions compared with PSIS-LOO, and a final model with stated limitations.

**Acceptance criteria**
- SBC rank histograms show no systematic deviation for all key parameters (or the deviation is diagnosed and fixed).
- All reported fits have rank-normalised R-hat below 1.01, adequate bulk and tail ESS, and no unexplained divergences.
- At least two model expansions are compared with PSIS-LOO; Pareto-k diagnostics are reported and acted upon.
- Posterior predictive checks target features of the data that matter for the decision (for example, small-district extremes).
- The report fits in eight pages plus an appendix, and a classmate reruns it from the package.

**Stretch goals.** Implement the model in a second language and compare; add a decision analysis with expected loss.

**What it proves to an employer.** You can deliver Bayesian analysis to a standard a research team or a statistics reviewer would accept.

### P2 · Causal ML replication and extension (~15 hours)

**Real-world inspiration.** Double machine learning and causal forests are now standard tools for estimating effects and targeting treatments in economics and industry. The 401(k) eligibility example used in the DML literature, and public randomized datasets such as Criteo Uplift, allow full replication.

**What to build.** Part A: replicate the 401(k) DML estimates and show their sensitivity to learners and to the overlap assumption. Part B: on a randomized dataset (Criteo Uplift or your DSC304 P2 data), estimate heterogeneous effects with a causal forest and two meta-learners, evaluate them with RATE, learn a budget-constrained policy, and estimate its value with a doubly robust estimator on held-out data.

**Acceptance criteria**
- Part A estimates match published values within reported uncertainty, or each discrepancy is traced to a documented cause.
- A simulation in which the true effect is known shows that your DML implementation's 95% intervals cover the truth in 93–97% of runs.
- Part B reports RATE and policy value with intervals, compared with treating everyone, no one and a random subset of the same size.
- A sensitivity analysis states how strong unmeasured confounding would need to be to overturn Part A's conclusion.
- A six-page report presents methods, results and limits.

**Stretch goals.** Compare with a Bayesian causal model (for example, BART-based); test policy stability across bootstrap samples.

**What it proves to an employer.** You can apply modern causal ML correctly and know where it stops being reliable, which is rare even among senior data scientists.

### P3 · A research-grade contribution (~30 hours)

**Real-world inspiration.** Workshop papers and well-documented preprints are how new methods and evaluations enter the field. AI-assisted science, Bayesian methods for sparse groups and causal ML on Indian data all have open questions that a strong student can address in a semester.

**What to build.** Choose one track and deliver a paper-style report (8–12 pages) with code and data:
- **Track A · Evaluating AI analysts.** Build a benchmark of at least 15 data-analysis tasks with ground truth from your own past projects or from published replications; evaluate at least two agents and one human baseline; publish a failure taxonomy.
- **Track B · Methods replication and extension.** Reproduce a recent methods paper from this seminar's reading list and extend it (new data, a failure case, a simpler alternative, or a robustness study).
- **Track C · Applied Bayesian or causal study on Indian data.** For example, small-area estimation with MRP, or causal-forest heterogeneity in a public policy evaluation, using SHRUG, NFHS or PLFS data.

**Acceptance criteria**
- A pre-registered plan (questions, data, methods, success criteria) is committed before main analyses.
- A classmate reproduces every table and figure from the package without help.
- The report includes related work, a limitations section and a statement of AI tools used and how their outputs were checked.
- For Track A: tasks have documented ground truth and scoring rules; results include variance across runs and a contamination discussion. For Track B: the original result is reproduced or the failure explained. For Track C: diagnostics (Bayesian) or identification and sensitivity analyses (causal) meet the standards of Chapters 1–5.
- The work is presented in a 15-minute conference-style talk and survives questions from a panel.

**Stretch goals.** Submit to a workshop or post a preprint; release the benchmark or dataset with a datasheet.

**What it proves to an employer.** You can create new, checkable knowledge, the entry ticket to research data science, applied science and PhD programmes.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is designed to become the first chapter of a thesis.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): sprints and P2 count as reproduction practice.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): a published benchmark or preprint is a strong signal for research and applied-scientist roles.
