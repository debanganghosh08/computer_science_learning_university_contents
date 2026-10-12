# DAN302 · Business Statistics and Experimentation

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [FND115](../../../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | [DAN402](../../year_4/DAN402_forecasting_for_business_decisions/README.md), [DAN305](../DAN305_product_and_business_analytics_metrics_funnels/README.md), [DAN501](../../year_5/DAN501_frontier_seminar_decision_intelligence/README.md) |

Part of the [Data Analysis major](../../README.md). FND116 gave you probability, confidence intervals, hypothesis tests, power and a first A/B test. This course applies them to the numbers businesses actually argue about: ratios, growth rates, skewed revenue, segment comparisons and experiments that real organisations run and misread. Formal causal inference (instrumental variables, regression discontinuity, synthetic control) is taught in depth in [DSC304](../../../data_science/year_3/DSC304_experimental_design_and_causal_inference/README.md); here you learn to recognise when you need it and to avoid the mistakes that make it necessary.

## Why this course matters now

Most product ideas do not work. At Microsoft, of well-designed experiments meant to improve a key metric, "only about one-third were successful at improving the key metric" (Kohavi et al., 2009). An analyst who cannot tell a real effect from noise will help ship the other two-thirds. In India, Swiggy has described an experimentation platform with ramp-ups, sample-ratio-mismatch checks, and switchback and difference-in-differences designs for cases where users affect each other (2021). AI assistants now write the statistics code in seconds: ChatGPT, Claude, Gemini and Copilot in Excel will all run a t-test on request. They will also run the wrong one, on the wrong unit, and call a segment-fishing result a finding. On the DABstep benchmark of multi-step data-analysis tasks, the best agent solved 14.55% of the hard tasks (2025). Choosing the comparison, the unit and the decision rule, and saying what the number does not show, is the analyst's job.

## Learning outcomes

By the end you can:

1. **Compute and explain** business ratios correctly: ratio of sums vs mean of ratios, percentage points vs percent, CAGR, index numbers, and a price–volume–mix decomposition.
2. **Summarise** skewed and zero-heavy business data with robust statistics, and **justify** an outlier policy before seeing results.
3. **Quantify** uncertainty for means, proportions, medians and ratio metrics (bootstrap and the delta method), at the correct unit of analysis.
4. **Diagnose** Simpson's paradox, regression to the mean, survivorship and selection bias in real dashboards, and **draw** the causal diagram that explains each.
5. **Fit and interpret** linear and logistic regressions for business questions, including dummies, interactions and log outcomes, and **state** what they cannot establish.
6. **Design** an A/B test: hypothesis, primary and guardrail metrics, randomisation unit, power, duration and a written decision rule.
7. **Analyse** an experiment end to end: SRM check, CUPED variance reduction, capped metrics, multiple-metric correction, and a readout with intervals.
8. **Choose** an alternative design (cluster, switchback, geo, holdout, sequential test) when users interfere or decisions cannot wait, and **explain** its cost.

## Chapters and lessons

### Chapter 1 · Business numbers done right (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Rates and ratios | Ratio of sums vs mean of ratios; weighted averages; which denominator answers the question | Compute "average order value" three ways on Online Retail II; explain which a CFO wants |
| 1.2 Percent and percentage points | Relative vs absolute change; small bases; "conversion up 50%" from 2% to 3% | Rewrite 10 misleading headlines correctly |
| 1.3 Growth | Month-on-month, year-on-year, CAGR, compounding, annualising; base effects in Indian inflation data | CAGR of monthly UPI volume over 3 years (NPCI data); show a base effect |
| 1.4 Index numbers | Base periods, chain-linking, real vs nominal using CPI (MoSPI) | Deflate 5 years of revenue to real terms |
| 1.5 Price–volume–mix | Decomposing a revenue change into price, volume and mix; why the order of steps matters | Decompose a year's revenue change for a 3-product illustrative business |

**Check your understanding:** Average order value rose while every city's AOV fell. How? When is a mean of ratios the right summary? Why can two analysts report different "price effects" for the same revenue change, and both be arithmetically correct?

### Chapter 2 · Distributions of business data (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Skew and whales | Revenue per user is heavy-tailed; a few customers move the mean | Share of revenue from the top 1% of customers in Online Retail II |
| 2.2 Zero-heavy metrics | Most users spend nothing; conversion × spend-per-converter decomposition | Split revenue per visitor into its two components |
| 2.3 Robust summaries | Median, trimmed mean, winsorizing (capping at p99), log transforms and how to report them | Compare 4 summaries of order value; choose one and defend it |
| 2.4 Outlier policy | Bots, test accounts, bulk B2B orders; deciding the rule before looking at results | Write a one-paragraph outlier policy for a marketplace |

**Check your understanding:** Why does a capped mean change the question you are answering? A median moved but the mean did not: what happened to the distribution? Why must an outlier rule be fixed before an experiment's results are seen?

### Chapter 3 · Uncertainty for decision-makers (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Intervals that business users read | Wilson intervals for rates, t intervals for means, intervals for a difference | Add 95% intervals to a weekly KPI table |
| 3.2 Bootstrap in practice | Percentile and BCa intervals for medians and ratios; resampling the right unit | Bootstrap median delivery time per city |
| 3.3 Ratio metrics and the delta method | Click-through rate per user vs per page view; variance when numerator and denominator are correlated (Deng, Knoblich and Lu, 2018) | Show a naive interval is too narrow, then fix it with the delta method |
| 3.4 Unit of analysis | Clustered data (orders within users, users within cities); design effect | Simulate how ignoring clustering inflates false positives |
| 3.5 Small numbers in league tables | Funnel plots, shrinkage intuition; why the "best" and "worst" stores are usually the smallest | Rank 200 stores by return rate; redo with funnel-plot limits |

**Check your understanding:** Why is a per-page-view interval wrong when users were randomised? A city with 12 orders tops the satisfaction ranking: what do you say? When is a bootstrap interval unreliable?

### Chapter 4 · Comparisons, segments and paradoxes (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Simpson's paradox in dashboards | Device or city mix shifts that reverse a trend; standardised rates | Rebuild a conversion dashboard that shows a fake decline |
| 4.2 Regression to the mean | "Worst stores improved after the visit"; selecting on extreme values | Simulate a coaching programme with zero effect that looks successful |
| 4.3 Survivorship and selection | Analysing only retained users; "users who used feature X retain better" | List the selection effects in 5 product claims (illustrative) |
| 4.4 Twyman's law | Any figure that looks interesting or different is usually wrong; checking pipelines before celebrating | Debug a "40% lift" caused by a logging change |

**Check your understanding:** How can every segment improve while the total gets worse? Why will a programme aimed at the worst-performing branches always look like it worked? What three checks do you run before announcing a surprising number?

### Chapter 5 · Correlation and cause in business data (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Causal diagrams | Confounders, mediators and colliders as directed acyclic graphs; what to control for and what not to | Draw the diagram for "app users spend more than web users" |
| 5.2 Pre–post comparisons | Seasonality, trends and festivals (Diwali, end of financial year) contaminate before/after | Show a "launch effect" that is really a festive-season effect |
| 5.3 Comparison groups | Matched controls and difference-in-differences intuition; the parallel-trends assumption | A diff-in-diff on an illustrative city-level price change |
| 5.4 When to ask for an experiment | Cost of being wrong vs cost of testing; what observational data can and cannot settle | Write a one-page recommendation: test, analyse, or decide now |

**Check your understanding:** Why does controlling for a mediator hide the effect you want to measure? What would make a diff-in-diff estimate wrong even with perfect data? When is it rational to decide without an experiment?

### Chapter 6 · Regression for analysts (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Regression as conditional averages | Ordinary least squares with `statsmodels` formulas; coefficients as adjusted differences | Order value on city, channel and weekday |
| 6.2 Categorical variables and interactions | Dummies, reference levels, interaction terms, reading them in plain language | Does the weekend effect differ by city? |
| 6.3 Log outcomes | Coefficients as approximate percentage changes; when the approximation fails | Explain a log-revenue model to a manager in two sentences |
| 6.4 Logistic regression for conversion | Odds ratios vs probability differences; average marginal effects | Conversion on traffic source and device in the GA4 sample |
| 6.5 Checking a model | Residual plots, influential points, multicollinearity; why R² is not the goal | Find the one influential B2B customer driving a coefficient |

**Check your understanding:** Why is "a coefficient of 0.3 on `is_app_user`" not evidence that moving users to the app raises spend? When should you report an average marginal effect instead of an odds ratio? A regression's R² is 0.08; is it useless?

### Chapter 7 · Designing an A/B test (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The written plan | Hypothesis, primary metric, guardrails (latency, cancellations, complaints), decision rule fixed in advance | A pre-registration document for an illustrative checkout change |
| 7.2 Randomisation unit | User, session, device, store, city; consistency, leakage and interference | Choose the unit for 6 scenarios and defend each |
| 7.3 Power for business metrics | Power for proportions, means and ratio metrics; minimum detectable effect vs the smallest effect worth shipping | Power curves by simulation; compare with Evan Miller's calculator |
| 7.4 Duration and ramps | Full weekly cycles, paydays and month-end in India, ramp from 1% to 50% with stop criteria | A ramp plan with kill switches |
| 7.5 Before launch | A/A tests, instrumentation checks, sample-ratio expectations | Run 1,000 simulated A/A tests; confirm about 5% are "significant" at α = 0.05 |

**Check your understanding:** Why should the decision rule be written before the test starts? When is the minimum detectable effect too small to bother with? What can a failed A/A test reveal that no A/B test can?

### Chapter 8 · Running and reading experiments (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Sample ratio mismatch | Chi-square SRM test; common causes such as redirects, bot filtering and late assignment (Fabijan et al., 2019) | Diagnose 3 SRM cases from logs |
| 8.2 CUPED | Variance reduction using pre-experiment data (Deng, Xu, Kohavi and Walker, 2013); when it helps little | Apply CUPED; report the variance reduction and the narrower interval |
| 8.3 Many metrics, many segments | False discovery rate across metrics; why post-hoc segment wins rarely replicate | Find the "winning segment" in pure noise, then correct for it |
| 8.4 Null results | Intervals that rule out large effects; equivalence thinking; what "not significant" does not mean | Write the readout for a flat test |
| 8.5 Novelty and primacy | Effects that fade or grow; plotting the effect by days since exposure | Detect a decaying novelty effect in simulated data |

**Check your understanding:** A test has a 50.6/49.4 split on 2 million users: is that a problem? Why does CUPED not bias the estimate? What do you tell a product manager whose test is flat but whose favourite segment is up 12%?

### Chapter 9 · When standard A/B tests break (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Interference in marketplaces | Riders, restaurants and drivers share supply; treatment spills onto control | Simulate a surge-pricing test where user-level randomisation is biased |
| 9.2 Switchback and cluster designs | Randomising time × region blocks; carry-over; fewer units, wider intervals | Analyse an illustrative switchback with block-level inference |
| 9.3 Geo experiments and holdouts | Matched markets; long-term holdouts to measure cumulative impact | Pick matched city pairs from public city-level data |
| 9.4 Peeking done right | Sequential testing with always-valid p-values (Johari et al.); group-sequential boundaries | Compare false-positive rates: naive daily peeking vs a sequential method |
| 9.5 Bayesian decisions | Posterior of the lift, expected loss, and when bandits are worth their complexity | Make a ship decision from expected loss for one dataset |

**Check your understanding:** Why does user-level randomisation overstate the effect of a feature that redistributes delivery partners? What do switchbacks trade away to fix interference? When is a multi-armed bandit a bad idea for learning?

### Chapter 10 · Experimentation as a programme (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Platforms | Assignment, exposure logging, metric computation; GrowthBook (open source), Statsig, Optimizely, in-house platforms | Run an experiment end to end in a local GrowthBook instance with simulated traffic |
| 10.2 Metric catalogues | One definition per metric, owners, guardrails shared across teams | Write 5 metric definitions with owner, formula and known caveats |
| 10.3 Review and culture | Experiment review, win rates, the cost of shipping neutral changes | Review three classmates' designs against a checklist |
| 10.4 Ethics and consent | Experiments on pricing and credit, vulnerable users, informed consent norms | Identify which of 6 proposed tests need extra review, and why |

**Check your understanding:** Why should most teams expect most experiments not to win? What goes wrong when each team defines "conversion" its own way? Which experiments should never run without legal or ethics review?

### Chapter 11 · Readouts and decisions (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 The one-page readout | Effect with interval, decision, risks, what we learned; no p-value without an effect size | Readout for your P2 experiment |
| 11.2 Cost of errors | False positives and false negatives in rupees; asymmetric decisions | Choose α and power from a cost model for two products |
| 11.3 Verifying an AI analysis | Re-running an assistant's analysis; checking the test, unit and denominator | Audit 5 AI-written analyses with planted errors |
| 11.4 Defending a result | Answering "is it real?", "will it last?" and "does it apply to us?" | Oral defence of P3 |

**Check your understanding:** When should a team accept a higher false-positive rate? What is the minimum content of a readout that a decision-maker can act on? Which three things do you check first in an AI-generated experiment analysis?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Ratios and decompositions | — |
| 2 | 2 | Lab 2 · Skewed revenue | Outlier policy |
| 3 | 3 | Lab 3 · Delta method and bootstrap | **P1 due** |
| 4 | 4 | Lab 4 · Paradox hunt | — |
| 5 | 5 | Lab 5 · Causal diagrams and diff-in-diff | One-page "test or decide" memo |
| 6 | 6 | Lab 6 · Regression for decisions | Mid-term (AI off) |
| 7 | 7 | Lab 7 · Power by simulation | Pre-registration document |
| 8 | 7–8 | Lab 8 · SRM and CUPED | — |
| 9 | 8 | Lab 8 (cont.) | **P2 due** |
| 10 | 9 | Lab 9 · Interference and switchbacks | — |
| 11 | 9 | Lab 10 · Sequential testing | — |
| 12 | 10 | GrowthBook end to end | Metric definitions |
| 13 | 11 | AI analysis audit | — |
| 14 | 11 | Readout practice | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** writing `statsmodels`, SciPy and simulation code you then check; explaining a method in a second way; generating synthetic data with a known true effect; drafting a readout you then edit. ChatGPT's data analysis mode, Claude, Gemini, Julius and Copilot in Excel all run analyses on uploaded files.
- **Do without AI (drills):** every power calculation by formula first; drawing causal diagrams; hand-computing a delta-method variance once; predicting the direction of Simpson's reversals; the mid-term and final. You need to know what the right answer looks like before you can spot a wrong one.
- **Verify AI output by:**
  - simulating data with a known effect and checking the method recovers it;
  - running A/A simulations to confirm the false-positive rate is near α;
  - checking that the analysis unit matches the randomisation unit;
  - recomputing the headline number by a second method;
  - checking that every segment result is labelled exploratory unless it was pre-registered.
- **Where AI still fails here:** in the course labs you will see assistants (1) run a two-sample t-test on page views when users were randomised, (2) report a "significant" segment found after looking at 20, and (3) describe a non-significant result as "no effect". On DABstep, built from real financial-analytics tasks, the best agent reached 14.55% on hard tasks (2025). Keep a log of every error you catch, with the test that caught it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 20% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can, with AI off: (1) given an experiment's raw assignment and outcome tables, run the SRM check, estimate the effect of a ratio metric with a correct interval (delta method or bootstrap at the user level) and write a decision in 60 minutes; (2) given a misleading dashboard, identify the paradox or bias, draw the causal diagram and produce the corrected comparison in 30 minutes; (3) design a test for a two-sided marketplace feature, choosing and justifying a randomisation unit that avoids interference, with a power calculation.

## Industry reality

Online controlled experiments are routine at large technology firms, and the standard reference (Kohavi, Tang and Xu, 2020) was written by practitioners from Microsoft, Google and LinkedIn. Swiggy has written publicly about its experimentation platform, including switchback and difference-in-differences designs (2021), and DoorDash about switchback tests for network effects in delivery (2018). Public experiment data exists: the ASOS Digital Experiments Dataset (Liu et al., NeurIPS 2021) records daily checkpoints of real e-commerce experiments; the Criteo uplift dataset and Kevin Hillstrom's e-mail experiment dataset are randomised marketing tests.

**Interview questions from this course**

1. *"Conversion rose 3% in the treatment group. Should we ship?"* Strong answer: asks for the interval, the pre-registered metric and decision rule, SRM, test duration and guardrails; distinguishes statistical from practical significance; mentions novelty.
2. *"Our app users spend 40% more than web users. Should we push everyone to the app?"* Strong answer: selection and confounding (engaged users choose the app); draws the diagram; proposes an experiment or a natural experiment; does not control for the mediator.
3. *"How would you test a new delivery-fee algorithm?"* Strong answer: interference between users sharing delivery partners; switchback or geo randomisation; carry-over; fewer effective units and the power cost; guardrails such as cancellation rate.
4. *"The experiment's split is 50.8/49.2 on 1.5 million users."* Strong answer: chi-square SRM test shows this is extremely unlikely by chance; do not trust the result; list causes (bot filtering, redirects, assignment bugs) and how to locate them.
5. *"Average order value went up in every city but down overall. Explain."* Strong answer: Simpson's paradox via a mix shift towards low-AOV cities; shows the arithmetic; proposes a mix-standardised metric.

## Resources (free first)

- **Experimentation:** [Online Experimentation at Microsoft](https://exp-platform.com/Documents/ExPThinkWeek2009Public.pdf) (Kohavi et al., 2009); Evan Miller, [How Not To Run an A/B Test](https://www.evanmiller.org/how-not-to-run-an-ab-test.html) and [sample size calculator](https://www.evanmiller.org/ab-testing/sample-size.html); [GrowthBook statistics docs](https://docs.growthbook.io/statistics/overview); Swiggy Bytes, [Experimentation Platform Part 2](https://medium.com/swiggy-bytes/experimentation-platform-xp-at-swiggy-part-2-90f4c3953b08).
- **Papers:** Deng, Knoblich and Lu, [Applying the Delta Method in Metric Analytics](https://arxiv.org/abs/1803.06336) (KDD 2018); Deng, Xu, Kohavi and Walker, CUPED (WSDM 2013, doi:10.1145/2433396.2433413); Fabijan et al., sample ratio mismatch (KDD 2019, doi:10.1145/3292500.3330722); Johari et al., [Always Valid Inference](https://arxiv.org/abs/1512.04922).
- **Free books:** Alex Reinhart, [Statistics Done Wrong](https://www.statisticsdonewrong.com/); Scott Cunningham, [Causal Inference: The Mixtape](https://mixtape.scunning.com/); [OpenIntro Statistics](https://www.openintro.org/book/os/); Gelman, Hill and Vehtari, [Regression and Other Stories examples](https://avehtari.github.io/ROS-Examples/).
- **Tools:** [statsmodels](https://www.statsmodels.org/stable/index.html); [SciPy stats](https://docs.scipy.org/doc/scipy/reference/stats.html).
- **Datasets:** [ASOS Digital Experiments Dataset](https://arxiv.org/abs/2111.10198); [Criteo uplift dataset](https://ailab.criteo.com/criteo-uplift-prediction-dataset/); [Hillstrom e-mail experiment](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html); [NPCI UPI statistics](https://www.npci.org.in/what-we-do/upi/product-statistics); [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii).
- **Paid, optional:** Kohavi, Tang and Xu, [*Trustworthy Online Controlled Experiments*](https://experimentguide.com/) (Cambridge, 2020); David Spiegelhalter, *The Art of Statistics* (2019).

## Sources

All checked 12 Oct 2026.

- Kohavi, Crook, Longbotham, Frasca et al., "Online Experimentation at Microsoft" (ThinkWeek 2009, public version) — https://exp-platform.com/Documents/ExPThinkWeek2009Public.pdf
- Swiggy Bytes, "Experimentation Platform (XP) at Swiggy — Part 2" (17 Nov 2021) — https://medium.com/swiggy-bytes/experimentation-platform-xp-at-swiggy-part-2-90f4c3953b08
- DoorDash Engineering, "Switchback Tests and Randomized Experimentation Under Network Effects at DoorDash" (2018) — https://careersatdoordash.com/blog/switchback-tests-and-randomized-experimentation-under-network-effects-at-doordash/
- Egg et al., "DABstep: Data Agent Benchmark for Multi-step Reasoning" (arXiv 2506.23719, Jun 2025) — https://arxiv.org/abs/2506.23719
- Liu, Cardoso, Couturier and McCoy, "Datasets for Online Controlled Experiments" (NeurIPS 2021 Datasets and Benchmarks) — https://arxiv.org/abs/2111.10198
- Deng, Knoblich and Lu (2018) — https://arxiv.org/abs/1803.06336 · Johari, Koomen, Pekelis and Walsh — https://arxiv.org/abs/1512.04922
- Kohavi, Tang and Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020), doi:10.1017/9781108653985

_Last reviewed: 2026-10_
