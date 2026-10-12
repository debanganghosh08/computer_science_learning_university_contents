# DSC302 · Labs and projects

Every lab and project starts with a one-paragraph **decision statement** (who acts, what action, when, at what cost) and ends with a number on a **hidden holdout** that you score exactly once. Keep an experiment log (MLflow or a CSV) from Lab 2. Coding agents and AutoML are allowed and encouraged as baselines; when you use them, report their result next to yours under the same splits.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Framing workshop | Turn five vague requests ("predict churn", "find fraud", "who needs help?") into decision statements, labels and horizons | Five one-page task specs; one argued "no model needed" | 3 h |
| 2 · Baseline ladder | Rule → logistic → LightGBM → AutoGluon → TabPFN on the same repeated CV | Results table (mean ± sd over 5×2 CV) and a paired-comparison verdict | 3 h |
| 3 · Validation design | Random vs time vs group split on a dataset with repeated entities; nested vs non-nested CV; adversarial validation | Score drop under each split, explained; the drifting features | 3 h |
| 4 · Leakage hunt (AI off) | A pipeline with six planted leaks, including a post-outcome feature and a label window overlapping the feature window | Leak report: location, type, measured inflation, fix | 4 h |
| 5 · GBDT tuning vs glass-box models | LightGBM and CatBoost with 50 Optuna trials each and monotone constraints on two features; then an EBM and an elastic-net GLM with splines on the same data | Tuning curves, hyperparameter importance, cost of constraints in AUC; performance table; three EBM shape functions interpreted | 7 h (2 weeks) |
| 6 · Thresholds and decision curves | Cost matrix → threshold; capacity-limited top-k; decision curves vs treat-all and treat-none | The recommended operating point with expected cost per 1,000 cases | 3 h |
| 7 · Interpretability traps | Permutation importance with duplicated features; PDP vs ALE; SHAP ranking a proxy above the cause on simulated data | Notebook demonstrating each failure, with a two-line lesson per failure | 5 h (2 weeks) |
| 8 · Slices and fairness | Recall and calibration by group with bootstrap intervals; Fairlearn audit; one mitigation | Slice table with intervals; trade-off chart; recommendation | 4 h |
| 9 · Segments and anomalies | Bootstrap stability of k-means segments; isolation forest tuned to an alert budget | Stability score; alert-budget curve | 3 h |
| 10 · Agent pipeline audit | Give a coding agent the P1 task; audit its pipeline and two others supplied by the instructor | Defect log (type, line, score inflation) and corrected pipelines | 3 h |

## Projects

### P1 · Who should the bank call? (L1, ~6 hours)

**Real-world inspiration.** The UCI Bank Marketing dataset comes from real telemarketing campaigns of a Portuguese bank selling term deposits. It contains a classic trap: the duration of the call is recorded, but it is only known after the call ends, so a model that uses it cannot be used to decide whom to call.

**What to build.** A decision-ready model for a call centre that can make a fixed number of calls per week: framing document, leakage-free pipeline, baseline ladder, capacity-based operating point and a one-page memo.

**Acceptance criteria**
- The decision statement names the action, the weekly capacity (illustrative: 500 calls), and the cost and benefit assumptions.
- Call duration and any other post-decision fields are excluded, and the memo shows how much they would have inflated the score.
- The baseline ladder has at least four rungs evaluated with the same repeated CV; gains are reported as mean ± sd.
- The operating point is chosen for the capacity, and the expected conversions per 500 calls are reported with a bootstrap interval.
- The hidden-holdout score is within 2 standard errors of the CV estimate.

**Stretch goals.** Compare the time-ordered version of the data with a random split; estimate how many conversions would have happened anyway (a causal question you flag for DSC304).

**What it proves to an employer.** You frame before you fit, and you catch the leak that makes most public notebooks on this dataset misleading.

### P2 · Readmission risk with limited care capacity (L2, ~15 hours)

**Real-world inspiration.** Hospitals run care-transition programmes for patients at high risk of readmission, and capacity is limited. The UCI "Diabetes 130-US Hospitals for Years 1999–2008" dataset contains about 100,000 real encounters with a readmission label; many patients appear more than once, which makes split design part of the problem.

**What to build.** A model that ranks discharged patients for a programme that can enrol a fixed share of them, evaluated with decision curves, slice analysis and a model card.

**Acceptance criteria**
- Splits are grouped by patient; the report shows the score under a naive encounter-level split and explains the difference.
- At least one glass-box model (EBM or spline GLM) and one GBDT are compared; the choice is justified on performance, calibration and explainability.
- A decision curve compares the model with treat-all and treat-none across a stated range of threshold probabilities.
- Recall and calibration are reported by age band and by the race field with bootstrap intervals; any gap is discussed with its uncertainty and the limits of the recorded categories.
- A model card states intended use, out-of-scope uses, data period (1999–2008) and why performance in a present-day hospital is unknown.
- All runs are in the experiment log and the final model rebuilds from it.

**Stretch goals.** Counterfactual explanations for ten high-risk patients, judged for actionability by a classmate playing a clinician; a comparison of the model's ranking with a simple clinical rule.

**What it proves to an employer.** You can deliver a model whose value depends on a real operational constraint, and document it the way regulated industries expect.

### P3 · A credit-risk model with model-risk documentation (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Home Credit, a lender focused on people with little credit history, released a multi-table dataset (applications, credit-bureau records, previous applications, instalment payments) in a 2018 Kaggle competition. Banks document such models under model-risk rules such as the Federal Reserve's SR 11-7 (conceptual soundness, outcomes analysis, ongoing monitoring).

**What to build.** A default-risk model from the full multi-table data, plus a validation document that an independent model-risk reviewer could check: data lineage, feature rationale, leakage tests, performance and calibration by segment, a scorecard alternative, explanation method with stated limits, and a monitoring plan.

**Acceptance criteria**
- Features are built only from information available at application time; every aggregate from secondary tables has a documented time window and a leakage test.
- The final model is scored by late submission on Kaggle's private leaderboard, and the CV-to-leaderboard gap is reported and explained.
- A monotone-constrained GBDT and a points-based scorecard are both delivered; the document quantifies the performance cost of the scorecard.
- Calibration (reliability diagram, Brier score) is shown overall and for at least three segments, with recalibration if needed.
- The explanation section shows SHAP results and a demonstration, on this data, of one way they could mislead a reviewer.
- A section on selection bias explains why a model trained on approved applicants may misjudge rejected ones and proposes how to measure it.
- The monitoring plan lists the metrics, their alert thresholds and the expected label delay.
- A three-page memo for a credit committee summarises the recommendation, risks and conditions for use.

**Stretch goals.** Fairness audit across the gender field and age bands with a documented mitigation decision; an agent-built competitor model audited line by line; a stress test of performance on applicants with no bureau history.

**What it proves to an employer.** You can build a strong model and also defend it to risk, compliance and business reviewers, which is what separates a modelling data scientist from a Kaggle competitor.

## Feeds into

- [DSC305 Feature Engineering and Model Evaluation](../DSC305_feature_engineering_and_model_evaluation/README.md): calibration, cost-based metrics and point-in-time features go deeper on the P3 data.
- [DSC402 NLP and Text Analytics with LLMs](../../year_4/DSC402_nlp_and_text_analytics_with_llms/README.md): the baseline ladder and validation discipline transfer to text.
- [DSC404 Data Science in Production](../../year_4/DSC404_data_science_in_production_deployment_monitoring/README.md): the P3 monitoring plan is implemented.
- [OV10B Fraud Detection and Risk Systems](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10B_fraud_detection_and_risk_systems/README.md): P3 is the entry point for credit and fraud risk work.
