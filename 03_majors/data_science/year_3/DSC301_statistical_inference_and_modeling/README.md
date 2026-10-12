# DSC301 · Statistical Inference and Modeling

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 (L4 in Chapters 10–11) | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | [DSC304](../DSC304_experimental_design_and_causal_inference/README.md), [DSC401](../../year_4/DSC401_time_series_analysis_and_forecasting/README.md), [DSC501](../../year_5/DSC501_frontier_seminar_bayesian_methods_causal_ml/README.md), [OV11A](../../../../04_overlaps/OV11_ai_for_science_research_engineering/OV11A_scientific_machine_learning_and_ai_for_discovery/README.md), [OV11B](../../../../04_overlaps/OV11_ai_for_science_research_engineering/OV11B_research_software_engineering/README.md) |

Part of the [Data Science major](../../README.md).

## Why this course matters now

Every A/B test readout, credit scorecard, insurance price and policy evaluation rests on the same small set of ideas: an estimand, an estimator, its uncertainty, and a model whose assumptions you have checked. When those ideas are applied carelessly, results do not hold up. When 100 published psychology studies were repeated with high-powered designs, 97% of the originals had been statistically significant but only 36% of the replications were (Open Science Collaboration, *Science*, 2015). Simulations showed that ordinary flexibility in data collection and analysis can make a false finding more likely than a true null (Simmons, Nelson and Simonsohn, 2011). Today ChatGPT, Claude, Gemini's Data Science Agent in Colab and Posit Assistant will fit a regression and print p-values in seconds, without asking how the data were sampled, which comparisons were planned, or whether the errors are clustered. This course trains the part they skip: deciding what quantity you are estimating, building a model you can defend, measuring how wrong it might be, and refusing to report a number the design cannot support.

## Learning outcomes

By the end you can:

1. **State** an estimand precisely (population, unit, quantity) and **separate** it from the estimator and the estimate.
2. **Derive** maximum-likelihood estimators and their standard errors, and **check** them against a bootstrap and a simulation.
3. **Design** a test with a stated power, minimum detectable effect and error rates, and **explain** Type M and Type S errors.
4. **Control** multiplicity with Holm and Benjamini–Hochberg, and **demonstrate** by simulation how p-hacking inflates false positives.
5. **Fit, interpret and diagnose** linear models with robust and clustered standard errors and fixed effects, in Python (statsmodels, pyfixest) and R.
6. **Choose** and **fit** the right generalized linear model (logistic, Poisson, negative binomial, with offsets) and **detect** overdispersion and separation.
7. **Use** regularization and multilevel (partial-pooling) models, and **explain** why post-selection p-values are invalid.
8. **Fit** a Bayesian model in PyMC or Bambi, run prior and posterior predictive checks, and **compare** its conclusions with the frequentist fit.
9. **Audit** an AI-generated statistical analysis and **write** a one-page report with effect sizes, intervals and stated assumptions.

## Chapters and lessons

### Chapter 1 · Estimands, data-generating processes and sampling (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Estimand, estimator, estimate | The three-part vocabulary; why "the average order value" is ambiguous until you fix unit, population and time | Rewrite five vague business questions as precise estimands |
| 1.2 Simulation as a microscope | Write the data-generating process first, then check whether your method recovers the truth ("fake-data simulation") | Simulate a skewed revenue variable and recover its mean and median |
| 1.3 Sampling designs | Simple random, stratified and cluster sampling; survey weights and design effects (the NFHS and PLFS designs) | Compute a weighted and an unweighted estimate from a public survey and explain the gap |
| 1.4 Properties of estimators | Bias, variance, mean squared error, consistency; the sample median vs mean under heavy tails | Compare MSE of mean, median and trimmed mean on Pareto data |

**Check your understanding:** (1) Two teams report different "average delivery times" from the same table, and both are correct. How? (2) Why does a cluster sample of 50 villages carry less information than 5,000 independent households? (3) When is a biased estimator better than an unbiased one?

### Chapter 2 · Likelihood and estimation (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Method of moments and maximum likelihood | Likelihood as a function of parameters; MLE for Bernoulli, Poisson, normal, exponential | Derive four MLEs by hand, then confirm numerically with `scipy.optimize` |
| 2.2 Fisher information and standard errors | Curvature of the log-likelihood, observed vs expected information, Wald intervals | Compute the standard error of a Poisson rate two ways |
| 2.3 The delta method | Standard errors of ratios and transformations (conversion rate ratio, log odds) | Derive the SE of a ratio metric and check it by simulation |
| 2.4 Likelihood ratio and profile likelihood | LR tests, profile intervals, when Wald intervals mislead (rates near 0) | Compare Wald and profile intervals for a rare-event rate |

**Check your understanding:** (1) Why does the Wald interval for a proportion fail when you observe 0 events? (2) What does a flat log-likelihood tell you about your data? (3) Why is the delta method needed for a "revenue per user" metric in an A/B test?

### Chapter 3 · Uncertainty by resampling (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 The bootstrap | Efron (1979); percentile, basic and BCa intervals; how many resamples | Bootstrap the median delivery time and compare interval types |
| 3.2 When the bootstrap fails | Maxima, heavy tails, tiny samples, dependent data | Show the bootstrap failing for the sample maximum |
| 3.3 Cluster and block bootstrap | Resample the unit of independence (users, stores, days) | Bootstrap a metric at user level vs event level and compare widths |
| 3.4 Permutation and randomization tests | Exact tests from the design; Fisher's sharp null | Run a permutation test on a small experiment and match it to a t-test |

**Check your understanding:** (1) Why must you resample users, not page views, when users generate many page views? (2) When would a permutation test and a t-test disagree? (3) How do you decide whether 1,000 bootstrap resamples are enough?

### Chapter 4 · Hypothesis testing done right (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 What a p-value is and is not | Neyman–Pearson vs Fisher; the ASA statement on p-values (2016); CI–test duality | Correct ten misstatements of p-values taken from real reports |
| 4.2 The standard tests | z and t tests, Welch, chi-square, Fisher exact, Mann–Whitney, and their assumptions | Choose and justify a test for six scenarios |
| 4.3 Power and sample size | Effect size, alpha, power, MDE; unequal allocation; design effect for clustering | Compute sample sizes analytically and by simulation; reconcile them |
| 4.4 Type M and Type S errors | Gelman and Carlin (2014): significant results from underpowered studies exaggerate effects | Simulate an underpowered test and measure the exaggeration ratio |
| 4.5 Equivalence and non-inferiority | Two one-sided tests (TOST); "no significant difference" is not "no difference" | Show that a migration did not slow a page by more than 50 ms |

**Check your understanding:** (1) A test with 20% power reports a significant 40% lift. What do you expect the true effect to be, and why? (2) Why is "not significant" weak evidence of no effect? (3) What changes in the sample size when you randomize stores instead of customers?

### Chapter 5 · Multiplicity and the garden of forking paths (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Many tests | Family-wise error (Bonferroni, Holm) vs false discovery rate (Benjamini–Hochberg, 1995) | Apply all three to 40 metrics from one experiment |
| 5.2 P-hacking by simulation | Optional stopping, flexible covariates, outlier rules, subgroup fishing (Simmons et al., 2011) | Reproduce a false-positive rate far above 5% with four "reasonable" choices |
| 5.3 Forking paths and many analysts | Gelman and Loken's garden of forking paths; 29 teams, one dataset (Silberzahn et al., 2018) | List every decision in a past analysis that could have gone another way |
| 5.4 Defences | Pre-registration and analysis plans, holdout data, multiverse and specification-curve analysis (Steegen et al., 2016) | Write a one-page analysis plan before touching a dataset |

**Check your understanding:** (1) When is FDR control more appropriate than FWER control? (2) How can an analysis be p-hacked even if only one test is reported? (3) Why does an AI agent that can run 200 specifications in an hour make pre-registration more valuable, not less?

### Chapter 6 · Linear regression as a statistical model (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 OLS assumptions and interpretation | Conditional mean model; what a coefficient means "holding others fixed"; categorical coding and reference levels | Interpret a wage regression with interactions in plain words |
| 6.2 Frisch–Waugh–Lovell and omitted variables | Partialling out; omitted-variable bias formula; why a coefficient changes sign | Reproduce a sign flip by adding one confounder |
| 6.3 Robust and clustered standard errors | HC0–HC3, cluster-robust SEs, few-cluster problems (wild bootstrap) | Compare naive, HC3 and clustered SEs on panel data |
| 6.4 Fixed effects and panels | Within transformation, two-way fixed effects, what they absorb and what they cannot | Fit store and week fixed effects with pyfixest and with R's `fixest` |
| 6.5 Prediction vs explanation | Breiman's two cultures; regression to the mean; why R² is not the goal | Explain why a "most-improved stores" ranking is mostly noise |

**Check your understanding:** (1) Why can heteroskedasticity leave coefficients unbiased but still ruin your conclusions? (2) What is the unit of clustering for an experiment randomized by city? (3) A colleague adds 40 controls "to be safe". What can go wrong?

### Chapter 7 · Model diagnostics and checking (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Residual diagnostics | Residual vs fitted, scale-location, QQ plots, partial residuals | Diagnose four flawed models from their plots alone |
| 7.2 Leverage and influence | Hat values, Cook's distance, DFBETAS; one district driving a national result | Find the observation that flips a conclusion |
| 7.3 Collinearity | VIF, unstable coefficients, why prediction can survive collinearity while interpretation cannot | Show coefficient instability across bootstrap samples |
| 7.4 Simulation-based model checks | Simulate replicated data from the fitted model and compare with reality | Check whether a normal model reproduces the zeros in order data |

**Check your understanding:** (1) Is a high-leverage point always a problem? (2) What does a funnel-shaped residual plot suggest you change? (3) Why are simulated checks more informative than a single goodness-of-fit p-value?

### Chapter 8 · Generalized linear models (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 The GLM framework | Exponential family, link functions, IRLS, deviance | Fit logistic regression by IRLS in NumPy and match statsmodels |
| 8.2 Logistic regression in depth | Odds ratios, marginal effects, separation and penalized fixes (Firth), rare events | Report average marginal effects instead of raw odds ratios |
| 8.3 Count data | Poisson, exposure offsets, overdispersion, negative binomial, zero inflation | Model daily orders per store with an offset for opening hours |
| 8.4 Other outcomes | Gamma for skewed positive amounts, ordinal logit, the frequency–severity split used in insurance pricing | Build a frequency × severity model on a public claims dataset |
| 8.5 GLMs in R and Python | `glm()` vs `statsmodels.formula.api.glm`; the default L2 penalty in scikit-learn's `LogisticRegression` | Reproduce one model in three libraries and explain every difference |

**Check your understanding:** (1) Why is an offset not the same as a covariate? (2) How do you detect overdispersion, and what happens to your p-values if you ignore it? (3) Why do scikit-learn and statsmodels report different logistic coefficients on the same data?

### Chapter 9 · Regularization and model selection (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Penalized likelihood | Ridge, lasso, elastic net as priors and as constraints; shrinkage path | Plot the lasso path on 100 noisy features |
| 9.2 Choosing models | Cross-validation vs AIC/BIC; what each is estimating | Compare CV and AIC choices on the same data |
| 9.3 Post-selection inference | Why p-values after variable selection are invalid; sample splitting as a fix | Simulate selection-then-test and measure the false-positive rate |
| 9.4 Splines and flexible terms | Natural splines, GAMs; flexible functions without losing interpretability | Replace a polynomial with a spline and compare diagnostics |

**Check your understanding:** (1) Why can the lasso pick different variables on two bootstrap samples? (2) What question does AIC answer that cross-validation does not? (3) When is sample splitting worth the lost data?

### Chapter 10 · Multilevel models and missing data (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Partial pooling | No pooling vs complete pooling vs hierarchical; random intercepts and slopes | Estimate a rate for 600 districts three ways and compare |
| 10.2 Fitting mixed models | statsmodels `MixedLM`, R `lme4`; convergence and singular fits | Fit the same model in both and reconcile |
| 10.3 Small-area estimation | Borrowing strength across areas; shrinkage of small districts | Rank districts by raw rate vs shrunken rate and explain the reordering |
| 10.4 Missing data | MCAR, MAR, MNAR; complete-case bias; multiple imputation and Rubin's rules | Show complete-case bias under MAR, then fix it with imputation |

**Check your understanding:** (1) Why do the smallest districts top and bottom every raw ranking? (2) What assumption makes multiple imputation valid, and how could it fail? (3) When should a grouping factor be a fixed effect instead of a random effect?

### Chapter 11 · Bayesian inference: a working introduction (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Priors, likelihood, posterior | Beta-binomial conjugacy; posterior as a compromise | Update a conversion-rate posterior day by day |
| 11.2 MCMC in practice | Why sampling; Hamiltonian Monte Carlo/NUTS intuition; R-hat, effective sample size, divergences | Fit a logistic regression in PyMC and read every diagnostic |
| 11.3 Prior and posterior predictive checks | Simulating from the prior to see if it is sensible; checking fit by simulation | Reject an "uninformative" prior that predicts impossible values |
| 11.4 Hierarchical Bayes | The Chapter 10 model as a Bayesian model in Bambi | Compare MixedLM and Bambi estimates and intervals |
| 11.5 Bayesian vs frequentist answers | Credible vs confidence intervals; "probability B beats A" and its pitfalls | Analyse one A/B test both ways and explain the difference to a PM |

**Check your understanding:** (1) What does a divergence warning tell you about the posterior? (2) Why can a Bayesian A/B test still be fooled by peeking at results? (3) When does the prior matter, and how do you show it?

### Chapter 12 · Communicating inference and auditing analyses (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Reporting effects | Effect sizes with intervals, absolute vs relative effects, base rates | Rewrite a "p < 0.05" report as an effect-size report |
| 12.2 Reproducible reports | Quarto or Jupyter with fixed seeds, pinned environments and a single run command | Rebuild a classmate's report from a clean machine |
| 12.3 Auditing an AI-generated analysis | A checklist: estimand, sampling, independence, multiplicity, diagnostics, overclaiming | Find every error in an assistant-generated analysis of PLFS data |
| 12.4 Writing for decision-makers | One page: question, answer, uncertainty, assumptions, what would change the conclusion | Write the summary for your P2 project |

**Check your understanding:** (1) Why can a relative lift of 50% be unimportant? (2) Which three items on the audit checklist do assistants most often skip in your logged examples? (3) What belongs in the assumptions section, and what belongs in the appendix?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Sampling and estimator simulation | Estimand rewrite exercise |
| 2 | 2 | Lab 2 · MLE, delta method and bootstrap check | Derivations problem set |
| 3 | 3 | Lab 3 · Bootstrap clinic | — |
| 4 | 4 | Lab 4 · Power and MDE | **P1 due** |
| 5 | 5 | Lab 5 · P-hacking simulator | Analysis plan for P2 |
| 6 | 6 | Lab 6 · Regression with robust and clustered SEs | — |
| 7 | 6–7 | Lab 6 (cont.) and diagnostics drills | Mid-term (closed book, AI off) |
| 8 | 8 | Lab 7 · GLMs for counts and amounts | — |
| 9 | 8 | Lab 7 (cont.) | — |
| 10 | 9 | Lab 8 · Selection and post-selection inference | **P2 due** |
| 11 | 10 | Lab 9 · Partial pooling for districts | — |
| 12 | 11 | Lab 9 (cont.): First Bayesian models | — |
| 13 | 11 | Lab 9 (cont.) | P3 checkpoint |
| 14 | 12 | Lab 10 · Audit an AI-generated analysis | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** translating a model between statsmodels, R and PyMC; generating simulation code for a data-generating process you specified; explaining an unfamiliar test or diagnostic; drafting plots; reviewing your written report for unclear wording. ChatGPT, Claude, Gemini (including the Data Science Agent in Colab), GitHub Copilot in VS Code notebooks and Posit Assistant in Positron all do this competently.
- **Do without AI (drills):** every derivation (MLEs, standard errors, delta method); choosing a test and computing power by hand for the weekly problem set; interpreting regression output aloud in 2 minutes; writing the analysis plan before seeing data. The mid-term and final are AI-off.
- **Verify AI output by:** (1) fake-data simulation: generate data with known parameters and check the method recovers them with correct interval coverage (about 95% of 95% intervals contain the truth over 1,000 runs); (2) cross-implementation: the same model in two libraries must agree, or you must explain why; (3) the audit checklist from Lesson 12.3; (4) asking the assistant for its assumptions and testing each one on the data.
- **Where AI still fails here:** in BLADE (2024), language models given open research questions were "often limited to basic analyses" compared with expert analysts. The Many Analysts study shows that reasonable humans disagree widely too, so speed without a plan multiplies forking paths. Build your own evidence: keep a log of every assistant answer that (a) ignored clustering or survey weights, (b) reported post-selection p-values as valid, or (c) misinterpreted a p-value or interval. Lab 10 is graded partly on this log.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10, notebooks plus short write-ups) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 30% |

**Mastery gate.** You pass when you can, without AI tools: (1) given an experiment design, compute the sample size for a stated MDE and power and confirm it by simulation within 2 percentage points of power; (2) fit and diagnose a GLM on unseen count or binary data, choose the right standard errors and explain each coefficient to a non-statistician; (3) in 30 minutes, find at least four of the five planted errors in an analysis report (for example: ignored clustering, post-selection p-values, misread interval, unweighted survey estimate, overclaimed causality).

## Industry reality

Where this is used (public sources): Booking.com describes running evidence-based product development through online experiments for more than ten years (Lopez Lopez Kaufman et al., 2017), and every readout depends on power, variance estimation and multiplicity control from Chapters 2–5. Insurance pricing is built on frequency and severity GLMs, documented for practitioners in the Casualty Actuarial Society's monograph *Generalized Linear Models for Insurance Rating* (Goldburd et al., CAS Monograph 5). India's large field experiments are analysed with cluster-robust inference: the evaluation of biometric Smartcards for NREGS and pension payments in Andhra Pradesh randomized the rollout over 157 subdistricts and 19 million people (Muralidharan, Niehaus and Sukhtankar, *AER*, 2016). National surveys such as NFHS-5 and PLFS publish unit-level data whose weights and cluster design must be used for any valid estimate.

**Interview questions from this course**

1. *Explain a p-value of 0.03 to a product manager, and say what it does not mean.* Strong answer: the probability of data at least this extreme if there were no effect; not the probability the hypothesis is true or that the result will replicate; adds the effect size and interval, and whether the test was pre-specified.
2. *A test with 400 users shows a significant 30% lift. Do you ship?* Strong answer: computes or estimates power; explains Type M exaggeration and the winner's curse; checks for peeking, SRM and novelty; asks for a confirmation run or a shrunken estimate before a large rollout.
3. *We tracked 25 metrics and 3 moved significantly. What do you report?* Strong answer: separates the pre-registered primary metric from exploratory ones; applies Holm or BH; reports all metrics with intervals; treats exploratory wins as hypotheses for the next test.
4. *Model the number of orders per store per day.* Strong answer: Poisson GLM with an offset for opening hours, checks overdispersion and moves to negative binomial, considers store random effects, validates with simulated replicated data, mentions zero inflation only if the data demand it.
5. *A coefficient changes sign when you add a variable. Which estimate is right?* Strong answer: depends on the estimand and causal structure; explains omitted-variable bias with Frisch–Waugh–Lovell; warns against reading either as causal without a design; draws the DAG that would settle it (bridge to DSC304).

## Resources (free first)

- **Courses:** Harvard Stat 110 Probability (Joe Blitzstein), course site https://stat110.hsites.harvard.edu/ and lectures https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo ; Berkeley Data 100 — https://ds100.org/ ; Statistical Rethinking 2025 lectures (Richard McElreath) — https://github.com/rmcelreath/stat_rethinking_2025
- **Primary texts (free):** Gelman, Hill and Vehtari, *Regression and Other Stories* (free PDF and code) — https://avehtari.github.io/ROS-Examples/ ; James, Witten, Hastie, Tibshirani and Taylor, *An Introduction to Statistical Learning with Applications in Python* — https://www.statlearning.com/ ; Efron and Hastie, *Computer Age Statistical Inference* — https://hastie.su.domains/CASI/ ; Çetinkaya-Rundel and Hardin, *Introduction to Modern Statistics* — https://openintro-ims.netlify.app/
- **Key papers:** ASA statement on p-values — https://doi.org/10.1080/00031305.2016.1154108 ; Gelman and Loken, garden of forking paths — http://www.stat.columbia.edu/~gelman/research/unpublished/p_hacking.pdf ; Gelman and Carlin, Type S and M errors — https://doi.org/10.1177/1745691614551642
- **Software docs:** statsmodels (0.15, Aug 2026) — https://www.statsmodels.org/stable/index.html ; pyfixest — https://pyfixest.org/ ; Bambi — https://bambinos.github.io/bambi/ ; PyMC — https://www.pymc.io/ ; R for Data Science (2e) — https://r4ds.hadley.nz/
- **Data:** PLFS and other NSO unit-level data (MoSPI microdata portal) — https://microdata.gov.in/ ; NFHS-5 (India DHS 2019–21, free registration) — https://dhsprogram.com/methodology/survey/survey-display-541.cfm ; Open Government Data platform — https://data.gov.in/
- **Paid, optional:** Casella and Berger, *Statistical Inference*; Wasserman, *All of Statistics*; McElreath, *Statistical Rethinking* (book). The free texts above cover this course.

## Sources

- Open Science Collaboration, "Estimating the reproducibility of psychological science", *Science* 349 (2015) — https://doi.org/10.1126/science.aac4716 (checked 2026-10)
- Simmons, Nelson and Simonsohn, "False-Positive Psychology", *Psychological Science* (2011) — https://doi.org/10.1177/0956797611417632 (checked 2026-10)
- Wasserstein and Lazar, "The ASA Statement on p-Values", *The American Statistician* (2016) — https://doi.org/10.1080/00031305.2016.1154108 (checked 2026-10)
- Silberzahn et al., "Many Analysts, One Data Set" (2018) — https://doi.org/10.1177/2515245917747646 (checked 2026-10)
- Benjamini and Hochberg (1995) — https://doi.org/10.1111/j.2517-6161.1995.tb02031.x ; Efron (1979) — https://doi.org/10.1214/aos/1176344552 ; Steegen et al., multiverse analysis (2016) — https://doi.org/10.1177/1745691616658637 (checked 2026-10)
- Gu et al., BLADE (arXiv 2408.09667, 2024) — https://arxiv.org/abs/2408.09667 (checked 2026-10)
- Google Developers Blog, Data Science Agent in Colab (3 Mar 2025) — https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/ (checked 2026-10)
- Lopez Kaufman, Pitchforth and Vermeer, "Democratizing online controlled experiments at Booking.com" (arXiv 1710.08217, 2017) — https://arxiv.org/abs/1710.08217 (checked 2026-10)
- Goldburd et al., *Generalized Linear Models for Insurance Rating*, CAS Monograph 5 — https://www.casact.org/sites/default/files/2021-01/05-Goldburd-Khare-Tevet.pdf (checked 2026-10)
- Muralidharan, Niehaus and Sukhtankar, "Building State Capacity: Evidence from Biometric Smartcards in India", *AER* 106(10) (2016) — https://www.aeaweb.org/articles?id=10.1257/aer.20141346 (checked 2026-10)
- Library versions from PyPI (statsmodels 0.15.0, Aug 2026; PyMC 6.3, Sep 2026) — https://pypi.org/project/statsmodels/ , https://pypi.org/project/pymc/ (checked 2026-10)

_Last reviewed: 2026-10_
