# MLE304 · Labs and projects

Use Python with scikit-learn, Fairlearn, MAPIE and your own metric code; every reported number carries a confidence interval or a seed spread. Public datasets: Folktables (US census tasks), the UCI "Default of Credit Card Clients" dataset, WILDS, CIFAR-10 and CIFAR-10-C, and a text-classification set of your choice. Any scenario about a specific lender is illustrative.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Baselines and holdout policy | Majority, rule-based and linear baselines for a credit-default task; a written holdout policy | Baseline table; a one-page policy on who may touch the test set and when | 3 h |
| 2 · Metric choice | Precision/recall, PR-AUC, ROC-AUC, Brier, NDCG and pinball loss on 4 tasks; expected cost in rupees for an illustrative lender | Metric recommendations per task with one-line reasons; a cost curve | 3 h |
| 3 · Bootstrap, seeds and paired tests | Bootstrap CIs (row-level vs user-level), paired bootstrap, McNemar, 10-seed variance, 20 simulated null comparisons | CI table; a seed-spread plot; the number of false "wins" from multiple comparisons | 4 h |
| 4 · Calibration and conformal prediction | Reliability diagrams; Platt, isotonic and temperature scaling; probability correction after undersampling; split-conformal sets with MAPIE | Before/after Brier and ECE; empirical coverage overall and by slice | 4 h |
| 5 · Slices and CheckList | Worst slices with CIs; a Simpson's paradox construction; 30 CheckList tests for a sentiment model | Slice report; CheckList failure rates by test type; a pytest release gate | 4 h |
| 6 · Fairness metrics and impossibility | Fairlearn `MetricFrame` on Folktables income or credit default; synthetic base-rate conflict; proxy reconstruction of a removed attribute | Metric table by group and intersection; the conflict plot; proxy AUC; an AI-error log | 4 h |
| 7 · Mitigation frontier | Reweighing, `ExponentiatedGradient` and `ThresholdOptimizer` | Accuracy vs fairness-gap frontier on held-out data, with CIs | 4 h |
| 8 · Reason codes and counterfactuals | SHAP-based top-4 reasons; stability under small perturbations; monotonic GBDT; actionable counterfactuals | Reason-code table for 20 declined cases; stability rate; counterfactual examples | 4 h |
| 9 · Shift detection | Simulated covariate and label shift; KS, MMD and classifier detectors; a WILDS cross-domain evaluation; 10-seed stress test | Detector power table; in-domain vs out-of-domain metrics; underspecification plot | 6 h (2 weeks) |
| 10 · Robustness benchmarks | Your CIFAR-10 model on CIFAR-10-C; standard vs robust models from RobustBench under the same benchmark | Accuracy by corruption type and severity; a written threat-model comparison | 4 h |

## Projects

### P1 · An evaluation report you would sign (L1, ~6 hours)

**Real-world inspiration.** The RBI's draft model-risk guidance (June 2026) would require banks, NBFCs and other regulated entities to validate every model independently, including third-party models, before and after deployment, and to define explainability thresholds for all AI models (paras 29–30 and 54 of the draft). Every validation starts with a report like this.

**What to build.** For a credit-default model trained on the UCI "Default of Credit Card Clients" data (or a Folktables task), write a 4–6 page evaluation report: baselines, task-appropriate metrics with bootstrap CIs, a calibration assessment, the worst 3 slices, and a ship/no-ship recommendation.

**Acceptance criteria**
- At least 3 baselines, including a rule-based one.
- Every headline metric has a 95% bootstrap CI; resampling is grouped if entities repeat.
- A reliability diagram, Brier score and ECE (with the binning stated), before and after recalibration.
- Worst-3 slices with CIs and minimum slice sizes stated.
- A clear recommendation tied to an explicit cost assumption, readable by a non-ML risk manager.

**Stretch goals.** Conformal prediction sets with coverage by slice; a decision curve.

**What it proves to an employer.** You report evidence, uncertainty and limits, not a single number, which is what model-risk and senior ML reviewers look for.

### P2 · Fairness audit of a lending model (L2, ~15 hours)

**Real-world inspiration.** The EU AI Act treats credit scoring as high-risk, with obligations from 2 December 2027; the RBI's FREE-AI report (2025) proposes that AI credit assessments be auditable; and India's DPDP Rules 2025 phase in duties on how personal data is collected and used. Illustrative scenario: an Indian digital lender expanding to a new state asks you to audit its approval model before launch.

**What to build.** An audit of a credit or income-prediction model on public data: group and intersectional fairness metrics, a proxy analysis, at least two mitigations with their trade-off frontier, reason codes for declined cases, and a regulation-mapping table.

**Acceptance criteria**
- At least 3 fairness metrics (for example demographic-parity difference, equal-opportunity difference, calibration within groups) per group and for at least 2 intersections, each with a CI.
- A demonstration that dropping the protected attribute does not remove the disparity, with proxy AUC reported.
- Two mitigations (one in-processing, one post-processing) evaluated on held-out data, with an accuracy-vs-fairness frontier.
- Top-4 reason codes for 20 declined cases and their stability under small input perturbations.
- A table mapping evidence to the EU AI Act high-risk requirements, RBI FREE-AI recommendations, the DPDP Act and the NIST AI RMF "Measure" function, quoting the source paragraphs.
- A 2-page memo for a non-technical board stating the recommended definition and threshold and why the choice is a policy decision.

**Stretch goals.** Counterfactual explanations limited to actionable features; a monotonic-constraint model and its effect on reason-code stability.

**What it proves to an employer.** You can carry a model through a fairness and regulatory review, which banks, fintechs and insurers increasingly need from ML engineers and not only from compliance staff.

### P3 · A reusable evaluation harness with release gates (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Google's ML Test Score rubric (Breck et al., 2017) and practices such as golden sets and per-slice release gates exist because models regress silently. WILDS (Koh et al., 2021) shows how models fail under real distribution shift.

**What to build.** An installable evaluation library and CLI, `evalkit`, that takes a model, a dataset and a YAML spec and produces an HTML or Markdown report plus a pass/fail exit code: metrics with CIs, calibration, slices, fairness metrics, shift tests against a reference sample, conformal coverage, and a generated model-card draft. Demonstrate it on two tasks (one tabular, one text or vision, at least one from WILDS).

**Acceptance criteria**
- One YAML spec per task defines metrics, slices, fairness groups, thresholds and gates; the CLI exits non-zero when any gate fails.
- Bootstrap CIs respect groups; the harness refuses to report slices smaller than a configured minimum.
- The shift module detects a planted covariate shift with power above 0.8 at the configured sample size and a false-alarm rate below 5% in A/A tests (measured by simulation).
- The harness runs in CI (for example GitHub Actions) and blocks a deliberately regressed model on one slice.
- On the WILDS task, the report shows the in-domain vs out-of-domain gap and the worst groups.
- The report for each task fits in 6 pages and includes a model-card draft completed by hand.
- Tests cover at least 80% of the library.

**Stretch goals.** Underspecification stress tests across seeds as a gate; integration with MLflow so every evaluation is logged against a model version; a robustness section using CIFAR-10-C.

**What it proves to an employer.** You can build the safety net an ML team relies on before every release, a core skill for senior ML engineers and ML platform teams.

## Feeds into

- [MLE404 Efficient Inference](../../year_4/MLE404_efficient_inference_quantization_distillation/README.md): your harness checks that quantised and distilled models have not lost accuracy on any slice.
- [MLE401 MLOps](../../year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md): P3's gates become CI/CD promotion checks, and the shift module becomes production monitoring.
- [MLE403 Ranking and Recommendation](../../year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md): ranking metrics and online-experiment statistics go deeper.
- [OV05 AI Security and Safety Engineering](../../../../04_overlaps/OV05_ai_security_safety/README.md): robustness and threat models continue there.
- [PRO301 Professional Practice](../../../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md): P2's regulation mapping connects to the ethics and law course.
