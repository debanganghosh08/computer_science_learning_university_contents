# DSC301 · Labs and projects

Two rules apply to every lab and project. **Simulate before you trust:** any method you use must first recover known parameters on fake data you generated. **Plan before you look:** write the analysis plan (estimand, model, primary test, multiplicity rule) before running the main analysis, and mark every later change as exploratory. Assistants may be used except where a lab says "AI off"; list in each submission what the assistant produced and how you checked it.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Sampling and estimators | Simulate simple, stratified and cluster samples from a synthetic population; compare bias, variance and MSE of mean, median and trimmed mean under heavy tails | Notebook; one table of MSEs; a paragraph on design effect | 3 h |
| 2 · MLE, delta method and bootstrap (AI off for derivations) | Derive MLEs and SEs for Poisson and Bernoulli models; delta-method SE for a ratio metric; confirm with bootstrap and simulation | Hand derivations (photo or LaTeX) plus a notebook where the three SEs agree within 5% | 3 h |
| 3 · Bootstrap clinic | Percentile vs BCa intervals; a case where the bootstrap fails (sample maximum); user-level vs event-level resampling | Coverage table over 1,000 simulated datasets for each method | 3 h |
| 4 · Power and MDE | Sample size for two-proportion and two-mean tests analytically and by simulation; unequal allocation; cluster design effect | Power curves; reconciliation of analytic and simulated answers | 3 h |
| 5 · P-hacking simulator | Reproduce optional stopping, covariate choice, outlier rules and subgroup fishing on pure-noise data; then apply Holm and BH | False-positive rate for each trick and combined; corrected rates | 3 h |
| 6 · Regression with robust and clustered SEs | Wage or hours regressions on PLFS unit-level data with survey weights; HC3 vs state-clustered SEs; fixed effects with pyfixest and R `fixest` | Coefficient table with three SE types; written interpretation of two interactions | 5 h (2 weeks) |
| 7 · GLMs for counts and amounts | Poisson vs negative binomial with exposure offset on the UCI Bike Sharing data; a gamma model for skewed amounts | Overdispersion test, residual and simulated-replicate checks, chosen model with justification | 5 h (2 weeks) |
| 8 · Selection and post-selection inference | Lasso selection then OLS p-values on noise; fix with sample splitting | Measured false-positive rate before and after the fix | 3 h |
| 9 · Partial pooling, frequentist and Bayesian | District-level rates from a public survey: no pooling, complete pooling, random intercepts (MixedLM and lme4); then a beta-binomial A/B posterior, a PyMC logistic regression with prior predictive checks, and a Bambi version of the district model | Shrinkage plot; the ten districts whose ranking changes most, explained; all MCMC diagnostics (R-hat, ESS, divergences); a prior you rejected and why | 8 h (3 weeks) |
| 10 · Audit an AI-generated analysis | Ask an assistant to analyse a supplied survey extract; audit the result with the Lesson 12.3 checklist | Error log with category, evidence and fix; corrected one-page summary | 3 h |

## Projects

### P1 · A power and sample-size calculator you can trust (L1, ~6 hours)

**Real-world inspiration.** Experimentation platforms show a minimum detectable effect before a test starts, and Booking.com describes safeguards that let anyone in the company run experiments without breaking them (Lopez Lopez Kaufman et al., 2017). A wrong power calculation either wastes weeks of traffic or produces underpowered tests whose "wins" are exaggerated (Gelman and Carlin, 2014).

**What to build.** A small Python package and command-line tool that computes sample size, power and MDE for two-proportion, two-mean and ratio metrics, with unequal allocation and a cluster design effect. Every analytic answer can be checked by a built-in simulation mode.

**Acceptance criteria**
- Analytic results match `statsmodels.stats.power` within 1% for the cases statsmodels covers.
- The simulation mode (≥ 5,000 replications) agrees with the analytic power within 2 percentage points for at least 12 documented scenarios, including one with a design effect above 2.
- The ratio-metric option uses a delta-method variance and is validated by simulation.
- Unit tests cover edge cases (allocation 1:9, baseline rate below 1%, MDE larger than baseline).
- A README explains Type M error with one worked example from your tool.

**Stretch goals.** A CUPED-style variance-reduction input (expected correlation with a pre-period metric) that previews DSC304; a Bayesian assurance calculation.

**What it proves to an employer.** You understand the design of an experiment before its analysis, and you validate statistical code the way engineers validate software.

### P2 · Reproduce and extend an official labour statistic (L2, ~15 hours)

**Real-world inspiration.** The National Statistics Office publishes Periodic Labour Force Survey (PLFS) bulletins, and the unit-level data are on MoSPI's microdata portal. Official figures depend on survey weights and definitions (current weekly status, age 15+); getting them right is the first test of any analyst who uses Indian survey data.

**What to build.** First, reproduce published PLFS headline indicators (labour force participation rate and unemployment rate by sex and rural/urban) from the unit-level files. Then answer one pre-registered question of your choice, for example "how much of the urban gender gap in earnings remains after adjusting for education, age, state and occupation?", with weighted regressions, appropriate standard errors and a specification curve.

**Acceptance criteria**
- At least six published headline figures are reproduced within 0.3 percentage points, with the weighting code documented.
- The analysis plan is committed to Git before the main regression is run (commit timestamps are checked).
- The main estimate is reported with HC3 and state-clustered standard errors, and the choice is justified.
- A specification curve covers at least 30 defensible specifications and shows where the primary estimate falls.
- Diagnostics (residual plots, influence) are included, and one influential group is investigated.
- A one-page summary states the estimand, the result with its interval, and why the estimate is not causal.

**Stretch goals.** Repeat the analysis on two survey rounds and test whether the gap changed, accounting for both rounds' sampling uncertainty; port the model to R and confirm identical results.

**What it proves to an employer.** You can work with complex public survey data correctly, separate confirmatory from exploratory analysis, and report a number a policy team could rely on.

### P3 · District-level estimates with honest uncertainty (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** NFHS-5 (2019–21) publishes district fact sheets, but many districts have small samples, so raw estimates are noisy and rankings mislead. Small-area estimation with partial pooling is how statistical agencies and researchers produce usable district numbers, and the [SHRUG](https://www.devdatalab.org/shrug) platform provides district and village covariates to strengthen them.

**What to build.** Using NFHS-5 unit-level data (India Standard DHS 2019–21, free registration with the DHS Program), estimate one child-health indicator such as the share of children under five who are stunted for every district. Build three estimators (direct weighted, frequentist multilevel, Bayesian hierarchical with district covariates) and a reproducible report and map.

**Acceptance criteria**
- Direct estimates reproduce the published NFHS-5 state figures for the indicator within 1 percentage point.
- The hierarchical model passes prior predictive, posterior predictive and MCMC diagnostics (R-hat < 1.01, no unexplained divergences), all reported.
- Validation: in the 50 largest-sample districts, randomly subsample to small-district sizes many times; the 90% intervals from your model cover the full-sample direct estimate between 85% and 95% of the time, and the model's error is lower than the subsampled direct estimate's.
- The report shows how district rankings change after pooling and explains the change for five districts.
- The whole analysis reruns from raw files with one command; the environment is pinned.
- An ethics section covers the risk of ranking districts, the uncertainty that must accompany any list, and DHS data-use terms.

**Stretch goals.** Multilevel regression and post-stratification to a covariate source; a sensitivity analysis on the prior for district variance; a short policy brief readable in two minutes.

**What it proves to an employer.** You can build a model that is useful because it is honest about uncertainty, on real Indian data, at a level expected of research data scientists and public-sector analytics teams.

## Feeds into

- [DSC304 Experimental Design and Causal Inference](../DSC304_experimental_design_and_causal_inference/README.md): P1 becomes the design tool for every experiment; Lab 6's clustered inference is used for policy evaluations.
- [DSC401 Time Series and Forecasting](../../year_4/DSC401_time_series_analysis_and_forecasting/README.md): likelihood, GLMs and predictive checks reappear for count and demand forecasting.
- [DSC501 Frontier Seminar](../../year_5/DSC501_frontier_seminar_bayesian_methods_causal_ml/README.md): P3's hierarchical model is the starting point for the full Bayesian workflow.
- [OV11A Scientific ML and AI for Discovery](../../../../04_overlaps/OV11_ai_for_science_research_engineering/OV11A_scientific_machine_learning_and_ai_for_discovery/README.md) and [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): small-area estimation on Indian survey data is a strong thesis topic.
