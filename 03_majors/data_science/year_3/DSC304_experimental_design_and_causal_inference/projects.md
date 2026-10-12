# DSC304 · Labs and projects

Every causal analysis in this course is preceded by a **pre-analysis plan** committed to Git: question, estimand, design, assumptions, primary specification and planned robustness checks. Every estimator is first run on **simulated data with a known effect** drawn from your DAG. Assistants may write code; the DAG, the estimand and the design are yours.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Selection bias, Simpson's paradox and DAGs (AI off for the DAGs) | Decompose a naive comparison into effect plus bias on simulated loyalty data; reproduce an aggregation reversal; adjustment sets for five DAGs; simulate collider bias; DoWhy refutation tests; log an assistant's DAG advice | Decomposition table; DAGs and adjustment sets checked in dagitty; assistant log | 5 h (2 weeks) |
| 2 · Randomization inference and clustering | Fisher randomization test; cluster-randomized design with design effect; ITT vs TOT | p-values from three methods; sample-size calculation for a cluster rollout | 3 h |
| 3 · SRM and ratio metrics | Detect an SRM in supplied logs and find its cause; delta-method SE for revenue per session | SRM diagnosis note; SE comparison table | 3 h |
| 4 · CUPED and sequential testing | CUPED on an experiment with pre-period data; simulate daily peeking; fix it with mSPRT and a group-sequential design | Sample-size reduction from CUPED; false-positive rates under each stopping rule | 4 h |
| 5 · Interference by simulation | A simulated delivery market: user-level A/B vs switchback vs region randomization; choose the switch interval | Bias and variance of each design against the known truth | 4 h |
| 6 · The LaLonde benchmark and sensitivity analysis | Regression, matching, IPW and AIPW on NSW observational samples vs the experimental estimate; then E-values, `sensemakr` contours and two placebo tests | Estimates table, balance and overlap plots, failed assumptions; a robustness section written as for a memo | 7 h (2 weeks) |
| 7 · Staggered difference-in-differences | Simulated staggered adoption where TWFE gets the sign wrong; Callaway–Sant'Anna fix; event-study plot | Plots and a paragraph on why TWFE failed | 3 h |
| 8 · IV and regression discontinuity | Randomized nudge to use a feature: first stage, 2SLS, LATE, weak-instrument check; sharp and fuzzy RD with `rdrobust` on a public dataset with density test, covariate balance, donut and placebo cutoffs | IV estimates with an explanation of whose effect they describe; all RD validity checks with a verdict | 7 h (2 weeks) |
| 9 · Synthetic control | Replicate California Proposition 99; placebo-in-space inference; compare with synthetic DiD | Replication figures and permutation p-value | 3 h |
| 10 · Uplift and Qini | S-, T- and X-learners on the Hillstrom email experiment; Qini curves; targeting under a budget | Qini plot, policy value with bootstrap interval | 3 h |

## Projects

### P1 · A trustworthy A/B test readout tool (L1, ~6 hours)

**Real-world inspiration.** Microsoft's Experimentation Platform team showed that sample ratio mismatch is a common sign of broken experiments (Fabijan et al., 2019), and CUPED (Deng et al., 2013) is now a standard feature of commercial platforms. A readout that skips these checks can ship the wrong decision with high confidence.

**What to build.** A Python function and command-line tool that takes user-level experiment data (with optional pre-period metrics) and produces a readout: SRM test, per-metric effects with delta-method intervals, CUPED-adjusted estimates, multiplicity-adjusted guardrails and a plain-language verdict.

**Acceptance criteria**
- On 1,000 simulated A/A tests, the false-positive rate of the primary metric is between 4% and 6%, and the SRM check flags a 50.5/49.5 split at 1 million users.
- CUPED estimates are unbiased in simulation (mean error within 1 standard error of zero) and the variance reduction matches the theoretical 1 − ρ² within 10%.
- Ratio metrics use delta-method variance, validated against a user-level bootstrap within 5%.
- The verdict refuses to recommend shipping when SRM fails or a guardrail is significantly harmed.
- The tool runs on the Hillstrom email data and the readout is included.

**Stretch goals.** An always-valid (mSPRT) mode with a simulation showing the false-positive rate stays at the nominal level under daily peeking; a novelty plot by exposure day.

**What it proves to an employer.** You can be trusted with the company's experiment readouts, which is the first responsibility of most product data scientists.

### P2 · Who should get the campaign? Uplift targeting (L2, ~15 hours)

**Real-world inspiration.** Criteo released a large randomized dataset for uplift modelling, and Kevin Hillstrom's email experiment is a classic teaching dataset. Marketers waste budget on customers who would buy anyway; uplift modelling targets those whose behaviour the campaign changes.

**What to build.** An uplift targeting system on the Criteo Uplift data (with Hillstrom as a second, smaller test): meta-learners and at least one direct uplift method, honest evaluation with Qini and uplift curves, and a budget-constrained targeting policy compared with targeting by predicted conversion.

**Acceptance criteria**
- The analysis plan fixes the evaluation split and metrics before modelling.
- At least three CATE estimators are compared on a held-out set with Qini coefficients and bootstrap intervals.
- The chosen policy's incremental conversions at budgets of 10%, 20% and 30% of users are reported with intervals and compared with random targeting and with targeting by conversion probability.
- A calibration check of uplift by decile shows whether predicted and observed uplift agree.
- A two-page memo recommends a budget level and states the risks (for example, effect heterogeneity over time and audience shift).

**Stretch goals.** Policy learning with a doubly robust objective; a check of how stable the targeted set is across random seeds.

**What it proves to an employer.** You understand that the right target is the effect, not the outcome, and can show the money that this distinction saves.

### P3 · Replicate and extend a published Indian policy evaluation (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Asher and Novosad (2020) estimated the impact of India's national rural roads programme (PMGSY) with a fuzzy regression discontinuity at the programme's village-population eligibility thresholds, using census microdata harmonised in SHRUG. They found that new feeder roads moved workers out of agriculture but found no major changes in agricultural outcomes, income or assets. The article's replication package is published with it.

**What to build.** A replication of the paper's main first-stage and reduced-form results from the replication package and public SHRUG data, followed by a pre-registered extension: a new outcome from SHRUG, a heterogeneity analysis, or a different design applied to the same question. Deliver a reproducible repository and a causal memo.

**Acceptance criteria**
- The pre-analysis plan for the extension is committed before the extension's outcome data are merged.
- The main first-stage and reduced-form estimates are reproduced within 10% of the published values (or each discrepancy is traced to a documented cause).
- Validity checks are reported: density test at the threshold, covariate balance, bandwidth sensitivity, donut specification and placebo cutoffs.
- The extension states its estimand, design and assumptions, and reports at least one sensitivity analysis.
- The repository rebuilds every number and figure with one command.
- A four-page causal memo written for a policy audience states the finding, its population (villages near the threshold), its uncertainty and what it does not show.

**Stretch goals.** A comparison of the RD estimate with a difference-in-differences or matching estimate on the same data, explaining any disagreement; a short blog-style explainer for non-specialists.

**What it proves to an employer.** You can read, reproduce and extend serious causal work on Indian data, which is the core skill of research, policy and senior product data scientists.

## Feeds into

- [DSC404 Data Science in Production](../../year_4/DSC404_data_science_in_production_deployment_monitoring/README.md): P1 measures post-launch impact; the causal memo format is the course's main writing assignment.
- [DSC403 Recommender Systems](../../year_4/DSC403_recommender_systems_and_personalization/README.md): interleaving, off-policy evaluation and interference build on Chapters 5–6.
- [DSC501 Frontier Seminar](../../year_5/DSC501_frontier_seminar_bayesian_methods_causal_ml/README.md): P2's CATE estimators lead to double machine learning and causal forests.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): P3 is a strong starting point for an empirical thesis.
