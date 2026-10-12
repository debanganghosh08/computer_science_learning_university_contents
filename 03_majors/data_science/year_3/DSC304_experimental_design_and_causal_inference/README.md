# DSC304 · Experimental Design and Causal Inference

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L4 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) (assumes [DSC301](../DSC301_statistical_inference_and_modeling/README.md) from semester 5) | [DSC404](../../year_4/DSC404_data_science_in_production_deployment_monitoring/README.md), [DSC501](../../year_5/DSC501_frontier_seminar_bayesian_methods_causal_ml/README.md), [DSC403](../../year_4/DSC403_recommender_systems_and_personalization/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Data Science major](../../README.md). The Data Analysis major's [DAN302](../../../data_analysis/year_3/DAN302_business_statistics_and_experimentation/README.md) teaches how to read a standard A/B test. This course teaches how to design experiments that stay valid at scale and how to estimate causal effects when you cannot randomize.

## Why this course matters now

"Did it work?" is the most valuable question in a company, and correlations answer it badly. Firms that answer it well built experimentation into how they work: Booking.com describes more than ten years of evidence-based product development through online experiments, open to anyone in the company (Lopez Lopez Kaufman et al., 2017), and Microsoft's Experimentation Platform team published the diagnostics that keep such systems honest, such as sample ratio mismatch checks (Fabijan et al., KDD 2019). Many decisions cannot be randomized at all. India's large policy evaluations show the full toolkit: a randomized rollout of biometric Smartcards across 157 subdistricts and 19 million people in Andhra Pradesh (Muralidharan, Niehaus and Sukhtankar, 2016); a fuzzy regression discontinuity on the population thresholds of the national rural roads programme (Asher and Novosad, 2020); and a triple-difference evaluation of Bihar's bicycle programme for girls (Muralidharan and Prakash, 2017). AI assistants will fit a propensity model or a difference-in-differences regression in seconds, and will just as quickly control for a collider or ignore interference between riders and drivers. Identification is a design argument, not a library call. That argument is the skill this course builds.

## Learning outcomes

By the end you can:

1. **Define** causal estimands (ATE, ATT, CATE, LATE) with potential outcomes, and **draw** a DAG that justifies (or rules out) an adjustment set.
2. **Design** a randomized experiment (unit, metrics, power, duration, guardrails) and **analyse** it with randomization inference and cluster-robust methods.
3. **Run** online A/B tests at scale: SRM checks, triggering, ratio metrics, CUPED variance reduction, sequential (always-valid) testing, novelty checks.
4. **Recognise** interference in marketplaces and networks and **choose** cluster, ego-cluster or switchback designs.
5. **Estimate** effects from observational data with regression adjustment, matching, inverse-probability weighting and doubly robust estimators, and **check** overlap and balance.
6. **Quantify** sensitivity to unmeasured confounding (E-values, omitted-variable-bias bounds).
7. **Apply** difference-in-differences with staggered adoption, instrumental variables, regression discontinuity and synthetic control, and **test** each design's assumptions.
8. **Estimate** heterogeneous effects and uplift, and **evaluate** a targeting policy with Qini curves.
9. **Write** a causal memo that states the design, assumptions, estimate, robustness checks and what would overturn the conclusion.

## Chapters and lessons

### Chapter 1 · Potential outcomes and causal estimands (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Potential outcomes | Rubin causal model; the fundamental problem of causal inference; SUTVA | Write potential outcomes for a discount, a feature launch and a policy |
| 1.2 Estimands | ATE, ATT, ATU, CATE; why "the effect" is ambiguous | Name the estimand a product manager, a CFO and a regulator each need |
| 1.3 Selection bias | Naive difference = effect + selection bias; worked decomposition | Decompose a naive loyalty-programme comparison |
| 1.4 Simpson's paradox | Aggregation reversals and what they say about adjustment | Reproduce a reversal with real admissions-style data |

**Check your understanding:** (1) Why does "users who used the feature retained better" not show the feature works? (2) When would ATT be the right estimand rather than ATE? (3) Which SUTVA violation is most likely in a referral programme?

### Chapter 2 · DAGs and identification (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Graphs as assumptions | Nodes, edges, paths; what an absent arrow claims | Draw the DAG for "does a delivery-time promise raise orders?" |
| 2.2 d-separation and the backdoor criterion | Blocking paths; minimal adjustment sets (dagitty) | Find adjustment sets for five DAGs, then check in dagitty |
| 2.3 Colliders, mediators and bad controls | Conditioning on a collider; post-treatment variables; "control for everything" as an error | Simulate collider bias and show it appearing from nothing |
| 2.4 Testing implications and DoWhy | Conditional independences a DAG implies; refutation tests in DoWhy | Test two implied independences on real data |

**Check your understanding:** (1) Why is adding a post-treatment variable to a regression harmful? (2) A DAG fits the data's conditional independences. Does that prove it? (3) What would you ask an assistant that proposes 30 control variables?

### Chapter 3 · Randomized experiments (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Why randomization works | Balance in expectation; randomization inference; Fisher's sharp null | Run a randomization test on a small field experiment |
| 3.2 Blocking and stratification | Variance reduction by design; re-randomization | Compare variance with and without blocking by city |
| 3.3 Cluster randomization | Intra-cluster correlation, design effect, few-cluster inference | Size the Smartcards-style design for a district-level rollout |
| 3.4 Compliance and attrition | Intention-to-treat vs treatment-on-treated; differential attrition; bounds | Compute ITT and TOT for an encouragement experiment |

**Check your understanding:** (1) Why randomize at the subdistrict level when outcomes are measured on households? (2) What does ITT estimate when only 60% of the treated group takes up the treatment? (3) How can attrition break a perfect randomization?

### Chapter 4 · Online A/B testing at scale I (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Metrics | Overall evaluation criterion, driver and guardrail metrics, metric sensitivity | Build a metric tree for a food-delivery checkout change (illustrative) |
| 4.2 Randomization units and triggering | User vs session vs page; trigger analysis; dilution | Re-analyse a test with and without triggering |
| 4.3 Trust checks | A/A tests, sample ratio mismatch (Fabijan et al., 2019), Twyman's law | Detect an SRM and trace it to a logging bug |
| 4.4 Ratio metrics | Delta-method variance for revenue per session; why naive SEs are wrong | Compare naive, delta-method and bootstrap SEs |

**Check your understanding:** (1) A test shows a 51/49 split when 50/50 was planned on 2 million users. What do you do? (2) Why is "click-through rate per page view" dangerous when randomizing by user? (3) When does triggering bias a result?

### Chapter 5 · Online A/B testing at scale II (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Variance reduction | CUPED (Deng et al., 2013), regression adjustment, stratification; CUPAC with model predictions | Apply CUPED and report the reduction in required sample size |
| 5.2 Peeking and sequential testing | Inflated false positives from repeated looks; always-valid inference and mSPRT (Johari et al., 2017); group-sequential designs | Simulate daily peeking, then fix it two ways |
| 5.3 Novelty, primacy and long-term effects | Effects that change over exposure time; holdouts; surrogate metrics | Plot treatment effect by days since first exposure |
| 5.4 Interleaving for rankers | Comparing ranking algorithms with interleaved results (Chapelle et al., 2012) | Simulate interleaving vs A/B sensitivity |
| 5.5 Intuition busters | Common misreadings of A/B results (Kohavi et al., KDD 2022) | Find the error in five published-style readouts |

**Check your understanding:** (1) Why does CUPED not bias the estimate? (2) A PM checks results daily and stops at the first significant day. What is the real false-positive rate? (3) How would you tell a novelty effect from a real long-term effect?

### Chapter 6 · Interference, marketplaces and networks (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 When SUTVA fails | Shared supply (riders and drivers), social spillovers, budget competition in ads | List interference channels for three marketplace features |
| 6.2 Cluster and ego-cluster designs | Graph clustering; LinkedIn's ego-cluster method (Saint-Jacques et al., 2019) | Estimate network effects on a simulated social graph |
| 6.3 Switchback experiments | Alternating treatment over time in a region; carryover and washout (DoorDash's public write-up) | Simulate a switchback and choose the switch interval |
| 6.4 Two-sided marketplace bias | Why user-level tests overstate supply-constrained wins | Show the bias in a simulated delivery market |

**Check your understanding:** (1) Why can a driver-side incentive test look great in a user-randomized A/B test and fail at launch? (2) What does a too-short switchback interval do to the estimate? (3) What is the cost of cluster randomization?

### Chapter 7 · Observational studies: adjustment, matching and weighting (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Regression adjustment | When it identifies effects; functional-form dependence | Fit adjustment models on LaLonde's NSW data and compare with the experiment |
| 7.2 Propensity scores | Estimation, overlap, trimming; balance diagnostics (standardised differences) | Diagnose poor overlap and decide what population you can speak about |
| 7.3 Matching and IPW | Nearest-neighbour and exact matching, inverse-probability weights, stabilised weights | Recover (or fail to recover) the experimental benchmark |
| 7.4 Doubly robust estimation | AIPW; why two models are better than one; cross-fitting preview (DSC501) | Compare IPW, regression and AIPW on the same data |

**Check your understanding:** (1) Why did LaLonde's comparison of observational estimates with an experiment matter? (2) What does poor overlap force you to change about your claim? (3) When does a doubly robust estimator still fail?

### Chapter 8 · Sensitivity analysis and falsification (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 How strong would a confounder need to be? | E-values (VanderWeele and Ding, 2017) | Compute E-values for three published estimates |
| 8.2 Omitted-variable-bias bounds | Cinelli and Hazlett (2020) sensitivity contours; benchmarking against observed covariates | Run `sensemakr` on your Lab 6 estimate |
| 8.3 Placebo and negative-control tests | Effects that should be zero; pre-period "effects" | Design two placebo tests for a pricing study |
| 8.4 Writing robustness sections | Which checks to report and how to present a fragile result | Write the robustness section of your P2 memo |

**Check your understanding:** (1) What does an E-value of 1.3 tell a decision-maker? (2) Why is a significant placebo effect bad news? (3) How do you report a result that is sensitive to one specification?

### Chapter 9 · Difference-in-differences and event studies (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 The 2×2 design | Parallel trends, the DiD estimator as a regression, clustering by group | Estimate a 2×2 DiD by hand and by regression |
| 9.2 Event studies | Leads and lags; visual pre-trends and their limits | Plot an event study for a staggered city launch |
| 9.3 Staggered adoption problems | Bad comparisons in two-way fixed effects (Goodman-Bacon, 2021); Callaway and Sant'Anna (2021) estimators | Show TWFE giving the wrong sign on simulated staggered data, then fix it |
| 9.4 Triple differences | Adding a within-group comparison: the Bihar cycle programme design | Reconstruct the design logic of Muralidharan and Prakash (2017) |

**Check your understanding:** (1) Do parallel pre-trends prove parallel trends after treatment? (2) Why can TWFE assign negative weights to some treated units? (3) What extra comparison does the Bihar study's third difference provide?

### Chapter 10 · Instrumental variables and regression discontinuity (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Instruments | Relevance, exclusion, monotonicity; LATE; weak-instrument diagnostics | Estimate a LATE from an encouragement design (randomized nudge to use a feature) |
| 10.2 IV in practice | Two-stage least squares, first-stage strength, why IV estimates are noisy | Compare OLS and 2SLS and explain the gap |
| 10.3 Sharp and fuzzy RD | Local estimates at a cutoff; bandwidth and kernel choice (`rdrobust`); fuzzy RD as IV | Reproduce the logic of the rural-roads RD (Asher and Novosad, 2020) |
| 10.4 RD validity | Manipulation (density) tests, covariate balance at the cutoff, donut and placebo cutoffs | Run all validity checks on an RD of your choice |

**Check your understanding:** (1) Whose effect does a LATE describe? (2) Why does an RD estimate say little about units far from the cutoff? (3) What would bunching just above a population threshold suggest?

### Chapter 11 · Synthetic control and time-series causal methods (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Synthetic control | Donor pools and weights; California's tobacco programme (Abadie et al., 2010) | Replicate the Proposition 99 analysis |
| 11.2 Inference for one treated unit | Placebo-in-space and in-time tests; permutation p-values | Run placebo tests on every donor |
| 11.3 Synthetic DiD and Bayesian structural time series | Arkhangelsky et al. (2021); CausalImpact (Brodersen et al., 2015) | Compare SC, SDID and CausalImpact on one launch |
| 11.4 Geo experiments | Randomizing regions for marketing; matched markets | Design a geo test for a city-level campaign (illustrative) |

**Check your understanding:** (1) Why can't you get a standard p-value with one treated unit? (2) What makes a donor pool bad? (3) When would you choose a geo experiment over synthetic control?

### Chapter 12 · Heterogeneous effects, uplift and the causal memo (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 CATE and meta-learners | S-, T- and X-learners (Künzel et al., 2019); honest evaluation | Fit three meta-learners on an experiment |
| 12.2 Uplift modelling | Targeting "persuadables"; Qini and uplift curves; policy value | Build uplift curves on the Criteo uplift data |
| 12.3 From effects to policies | Budget-constrained targeting; evaluating a policy offline; why churn scores are not uplift | Compare targeting by churn risk vs by uplift |
| 12.4 AI as a causal collaborator | Using assistants to brainstorm confounders and DAGs; testing their suggestions | Audit an assistant's DAG and adjustment set for a supplied scenario |
| 12.5 The causal memo | Question, estimand, design, assumptions, estimate, robustness, decision | Write the P3 memo; peer review two others |

**Check your understanding:** (1) Why can't you validate a CATE model with ordinary accuracy metrics? (2) Why target by uplift rather than by predicted churn? (3) Which section of a causal memo should a sceptical executive read first?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Selection bias and Simpson's paradox | Estimand exercise |
| 2 | 2 | Lab 1 (cont.): DAGs, colliders and DoWhy | — |
| 3 | 3 | Lab 2 · Randomization inference and clustering | — |
| 4 | 4 | Lab 3 · SRM and ratio metrics | **P1 due** |
| 5 | 5 | Lab 4 · CUPED and sequential testing | — |
| 6 | 6 | Lab 5 · Switchbacks and ego-clusters (simulation) | — |
| 7 | 7 | Lab 6 · LaLonde benchmark | Mid-term (AI off) |
| 8 | 8 | Lab 6 (cont.): Sensitivity analysis | — |
| 9 | 9 | Lab 7 · Staggered DiD | **P2 due** |
| 10 | 10 | Lab 8 · IV from an encouragement design | — |
| 11 | 10 | Lab 8 (cont.): RD and validity checks | P3 pre-analysis plan |
| 12 | 11 | Lab 9 · Synthetic control (Proposition 99) | — |
| 13 | 12 | Lab 10 · Uplift and Qini | — |
| 14 | 12 | Causal memo peer review | **P3 due** |
| 15 | Review | Design defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** simulation code for designs (power, switchbacks, staggered adoption); boilerplate for DoWhy, EconML, CausalML, pyfixest and `rdrobust`; brainstorming possible confounders and interference channels; drafting memo prose you then edit. Claude, ChatGPT, Gemini, Claude Code and GitHub Copilot all help.
- **Do without AI (drills):** drawing DAGs and choosing adjustment sets; naming the estimand; deciding the randomization unit; listing threats to each design; the weekly "design this study in 15 minutes" exercise. The mid-term, final and P3 design defence are AI-off.
- **Verify AI output by:** (1) simulating data from your DAG with a known effect and checking the suggested estimator recovers it; (2) checking every proposed control against the DAG for colliders and post-treatment variables; (3) running the design's own validity tests (SRM, balance, pre-trends, density, placebos); (4) comparing at least two estimators that rely on different assumptions.
- **Where AI still fails here:** you will document it. In Lab 1 and Lesson 12.4, give an assistant scenarios that contain a collider, a mediator and an interference channel, and log whether it recommends conditioning on the collider or mediator, or misses the interference. Open-ended analysis benchmarks such as BLADE (2024) report that language models often stop at basic analyses; this course's designs are exactly the analytical decisions those benchmarks find hard.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + design defence of P3 | 30% |

**Mastery gate.** You pass when you can, AI off: (1) given a product change in a two-sided marketplace, produce in 30 minutes a complete experiment design (unit, metrics, guardrails, power, duration, interference handling, stopping rule); (2) given an observational question and a dataset description, choose and defend an identification strategy, list its testable and untestable assumptions, and name the robustness checks; (3) spot the flaw in four of five supplied causal claims (collider adjustment, SRM, peeking, staggered TWFE, extrapolated RD).

## Industry reality

Experimentation is a core data science function at large online firms, and many publish their methods. Booking.com (Lopez Lopez Kaufman et al., 2017), Microsoft's Experimentation Platform, Netflix's research on experimentation and causal inference, Spotify's comparison of sequential testing frameworks (2023), LinkedIn's ego-cluster experiments (2019) and DoorDash's switchback experiments are all public. Commercial and open-source platforms such as Statsig and GrowthBook ship CUPED and sequential tests as standard features, which moves the scarce skill from computing the statistic to designing the test and interpreting it. Public policy uses the same methods: the Indian studies cited above are standard teaching examples. A systematic review of A/B testing methodology is Larsen et al. (2023).

**Interview questions from this course**

1. *Design an A/B test for a new one-tap checkout.* Strong answer: hypothesis and primary metric (conversion per user), guardrails (refunds, latency, revenue per user), user-level randomization, power and duration covering weekly cycles, SRM and A/A checks, a pre-registered stopping rule, novelty checks, and a ship/no-ship rule.
2. *Conversion is up 2% but revenue per user is down 1%. Ship?* Strong answer: checks significance and intervals for both; the overall evaluation criterion; mix shift (cheaper baskets); segment heterogeneity; long-term value; proposes a follow-up test instead of guessing.
3. *We want to test a new courier-assignment algorithm.* Strong answer: interference through shared couriers makes user-level tests biased; proposes switchbacks by region and time window, with carryover handling, or region-level randomization; discusses power with few clusters.
4. *A policy launched in some cities at different times. Estimate its effect.* Strong answer: event-study DiD with modern staggered estimators, not plain TWFE; pre-trend checks and their limits; clustering by city; placebo tests; synthetic control if few treated units.
5. *Members of our loyalty programme spend more. Did the programme cause it?* Strong answer: self-selection; DAG with prior spending and engagement as confounders; propensity or doubly robust estimates with overlap checks; sensitivity analysis; recommends a randomized encouragement (IV) design for a clean answer.

## Resources (free first)

- **Texts:** Scott Cunningham, *Causal Inference: The Mixtape* — https://mixtape.scunning.com/ ; Nick Huntington-Klein, *The Effect* — https://theeffectbook.net/ ; Hernán and Robins, *Causal Inference: What If* — https://miguelhernan.org/whatifbook ; Matheus Facure, *Causal Inference for the Brave and True* — https://matheusfacure.github.io/python-causality-handbook/landing-page.html
- **Online experiments:** Kohavi, Tang and Xu, *Trustworthy Online Controlled Experiments* (book site) — https://experimentguide.com/ ; Microsoft Experimentation Platform — https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/ ; Netflix Research, experimentation and causal inference — https://research.netflix.com/research-area/experimentation-and-causal-inference ; Spotify Engineering, choosing a sequential testing framework — https://engineering.atspotify.com/2023/03/choosing-sequential-testing-framework-comparisons-and-discussions ; DoorDash, switchback tests — https://careersatdoordash.com/blog/switchback-tests-and-randomized-experimentation-under-network-effects-at-doordash/
- **Key papers:** CUPED (Deng et al., 2013) — https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf ; Johari et al., always-valid inference — https://arxiv.org/abs/1512.04922 ; Larsen et al., review of A/B testing methodology — https://arxiv.org/abs/2212.11366 ; Athey and Imbens, "The State of Applied Econometrics" — https://doi.org/10.1257/jep.31.2.3
- **Software:** DoWhy — https://www.pywhy.org/dowhy/ ; EconML — https://github.com/py-why/EconML ; CausalML — https://causalml.readthedocs.io/ ; pyfixest — https://pyfixest.org/ ; rdrobust and RD packages — https://rdpackages.github.io/ ; dagitty — https://www.dagitty.net/ ; sensemakr — https://github.com/carloscinelli/sensemakr ; GrowthBook — https://www.growthbook.io/ ; Statsig docs — https://docs.statsig.com/
- **Data:** LaLonde/NSW (Dehejia and Wahba) — https://users.nber.org/~rdehejia/nswdata.html ; Criteo Uplift — https://ai.criteo.com/criteo-uplift-prediction-dataset/ ; Hillstrom email experiment — https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html ; SHRUG — https://www.devdatalab.org/shrug ; Asher and Novosad replication package (via the AEA article page) — https://www.aeaweb.org/articles?id=10.1257/aer.20180268
- **Paid, optional:** Angrist and Pischke, *Mostly Harmless Econometrics*; Imbens and Rubin, *Causal Inference for Statistics, Social, and Biomedical Sciences*.

## Sources

- Lopez Kaufman, Pitchforth and Vermeer, "Democratizing online controlled experiments at Booking.com" (arXiv 1710.08217, 2017) — https://arxiv.org/abs/1710.08217 (checked 2026-10)
- Fabijan et al., "Diagnosing Sample Ratio Mismatch in Online Controlled Experiments", KDD 2019 — https://doi.org/10.1145/3292500.3330722 (checked 2026-10)
- Muralidharan, Niehaus and Sukhtankar, *AER* 106(10) (2016) — https://www.aeaweb.org/articles?id=10.1257/aer.20141346 ; Asher and Novosad, *AER* 110(3) (2020) — https://www.aeaweb.org/articles?id=10.1257/aer.20180268 ; Muralidharan and Prakash, *AEJ: Applied* 9(3) (2017) — https://www.aeaweb.org/articles?id=10.1257/app.20160004 (checked 2026-10)
- Johari et al., "Peeking at A/B Tests", KDD 2017 — https://doi.org/10.1145/3097983.3097992 ; Kohavi, Deng and Vermeer, "A/B Testing Intuition Busters", KDD 2022 — https://doi.org/10.1145/3534678.3539160 ; Chapelle et al., interleaving, *ACM TOIS* (2012) — https://doi.org/10.1145/2094072.2094078 (checked 2026-10)
- Saint-Jacques et al., "Using Ego-Clusters to Measure Network Effects at LinkedIn" (arXiv 1903.08755) — https://arxiv.org/abs/1903.08755 (checked 2026-10)
- Goodman-Bacon (2021) — https://doi.org/10.1016/j.jeconom.2021.03.014 ; Callaway and Sant'Anna (2021) — https://doi.org/10.1016/j.jeconom.2020.12.001 ; Abadie, Diamond and Hainmueller (2010) — https://doi.org/10.1198/jasa.2009.ap08746 ; Arkhangelsky et al. (2021) — https://doi.org/10.1257/aer.20190159 ; Brodersen et al. (2015) — https://doi.org/10.1214/14-AOAS788 (checked 2026-10)
- VanderWeele and Ding (2017) — https://doi.org/10.7326/M16-2607 ; Cinelli and Hazlett (2020) — https://doi.org/10.1111/rssb.12348 ; Künzel et al. (2019) — https://doi.org/10.1073/pnas.1804597116 (checked 2026-10)
- Gu et al., BLADE (arXiv 2408.09667) — https://arxiv.org/abs/2408.09667 (checked 2026-10)
- Platform documentation for CUPED and sequential testing: GrowthBook — https://docs.growthbook.io/statistics/cuped and https://docs.growthbook.io/statistics/sequential ; Statsig — https://docs.statsig.com/stats-engine/methodologies/cuped and https://docs.statsig.com/experiments-plus/sequential-testing (checked 2026-10)

_Last reviewed: 2026-10_
