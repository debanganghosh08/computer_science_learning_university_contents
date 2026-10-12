# DAN302 · Labs and projects

Every lab and project ships as a reproducible notebook or script (Python with `pandas`, `numpy`, `scipy` and `statsmodels`, or R), a fixed random seed, and a short write-up that states the question, the unit of analysis, the method, the result with an interval, and what the result does not show. Any method you use on real data must first recover a known effect on simulated data.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Ratios and decompositions | Compute AOV, conversion and revenue per visitor three ways; decompose a revenue change into price, volume and mix | Notebook; a table showing the decomposition sums exactly to the total change; 5 corrected headlines | 3 h |
| 2 · Skewed revenue | Profile revenue per customer in Online Retail II; compare mean, median, trimmed mean, capped mean and log-scale summaries | Plots, a top-1% revenue share figure, and a pre-registered outlier policy | 3 h |
| 3 · Delta method and bootstrap | Interval for a ratio metric (clicks per user) three ways: naive, delta method, user-level bootstrap | Coverage check over 1,000 simulations for each method, with the naive one shown to under-cover | 4 h |
| 4 · Paradox hunt | Debug 4 provided dashboards: Simpson's paradox, regression to the mean, survivorship, a logging change (Twyman's law) | For each: the causal story, the corrected chart and a one-line correction for the dashboard owner | 4 h |
| 5 · Causal diagrams and diff-in-diff | Draw diagrams for 5 product claims; run a diff-in-diff on an illustrative city price change with a placebo test | Diagrams (DAGitty or Mermaid), the estimate, and a parallel-trends plot | 4 h |
| 6 · Regression for decisions | Linear and logistic models on the GA4 sample and Online Retail II; interactions; influential points | Model tables, marginal effects, residual plots, and a plain-language summary for a manager | 4 h |
| 7 · Power by simulation | Power curves for a proportion, a mean and a ratio metric; translate to days of traffic with weekly cycles | Curves, a duration recommendation, and a comparison with Evan Miller's calculator | 3 h |
| 8 · SRM and CUPED | Detect sample ratio mismatch in 3 log extracts; apply CUPED with pre-period spend | SRM diagnoses with likely causes; variance reduction achieved and the narrower interval | 4 h |
| 9 · Interference and switchbacks | Simulate a two-sided marketplace; compare user-level and switchback estimates of a fee change against the true effect | Bias and variance of each design over 500 simulated runs | 5 h |
| 10 · Sequential testing | Show daily peeking inflates false positives; implement an always-valid or group-sequential rule | A/A simulation results for both approaches at α = 0.05 | 3 h |

## Projects

### P1 · KPI pack with honest uncertainty (L1, ~6 hours)

**Real-world inspiration.** Monthly business reviews at Indian payments, retail and lending companies argue over KPIs that move by a few percent. Reported changes are often within noise, or driven by mix, base effects or calendar effects.

**What to build.** A monthly KPI pack from one public source: NPCI's monthly UPI statistics (volume and value, downloaded by hand) or the UCI Online Retail II transactions aggregated by month and country. Include growth (MoM, YoY, CAGR), a price–volume–mix or value-per-transaction decomposition, intervals where the metric is a sample-based rate, and a short commentary.

**Acceptance criteria**
- Every growth figure states its base period; percent and percentage-point changes are labelled correctly throughout.
- The decomposition reconciles exactly (to the rupee or pound) with the total change, and the order of decomposition steps is stated.
- At least one apparent change is shown to be a base effect, mix shift or calendar effect (number of weekends, festival timing), with evidence.
- Every rate computed from a sample of transactions carries a 95% interval.
- A "What this pack does not show" section lists at least three limits.

**Stretch goals.** Deflate value series with MoSPI CPI to real terms; add a funnel plot for country-level return rates.

**What it proves to an employer.** You report numbers that survive a CFO's questions, and you can say when a movement is not news.

### P2 · Experiment analysis toolkit (L2, ~15 hours)

**Real-world inspiration.** Experimentation platforms such as GrowthBook and the in-house system Swiggy describes automate SRM checks, variance reduction and metric computation, so that every team analyses tests the same way.

**What to build.** A small Python package with a command-line interface. It takes an assignment table and a metrics table and produces: an SRM check, effects with intervals for mean, proportion and ratio metrics (delta method), CUPED-adjusted estimates when a pre-period column is supplied, capped-metric options, and Benjamini–Hochberg correction across metrics. Validate it on simulated data, then apply it to Kevin Hillstrom's e-mail experiment (customers randomised to a men's e-mail, a women's e-mail or no e-mail).

**Acceptance criteria**
- On 1,000 simulated A/A tests, the false-positive rate for each metric type is between 4% and 6% at α = 0.05.
- On simulated tests with a known effect, 95% intervals cover the truth in 93–97% of runs for all three metric types.
- CUPED reduces the variance on simulated data with correlated pre-period values, and the report states the reduction.
- The SRM check flags a planted 51/49 split on 200,000 users.
- Unit tests in CI; a README with a worked example; the Hillstrom readout states the effect of each e-mail on visits, conversion and spend with intervals, and a decision.

**Stretch goals.** Add a sequential-testing option; add a Bayesian expected-loss summary; compare your results with GrowthBook's on the same data.

**What it proves to an employer.** You can build and validate the statistical core of an experimentation platform and explain every number it outputs.

### P3 · Pricing experiment in a two-sided marketplace (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Delivery marketplaces cannot test delivery fees or dispatch rules by randomising users, because treated and control users share the same delivery partners. Swiggy and DoorDash have both described switchback designs for this problem. The marketplace below is an illustrative simulation, not a model of any company.

**What to build.**
1. A simulator of an illustrative food-delivery city: zones, hourly demand with weekday and festival patterns, a partner pool, and customers whose ordering depends on fee and delivery time. The true effect of a fee change is known by construction.
2. A pre-registration document: hypothesis, primary metric (orders per zone-hour or contribution per order), guardrails (delivery time, cancellations), randomisation design, power analysis, decision rule.
3. Two designs run on the simulator: user-level A/B and a zone × time-block switchback, each repeated at least 300 times.
4. Analysis with block-level inference for the switchback, a carry-over check, and a sequential monitoring rule.
5. A calibration section using the ASOS Digital Experiments Dataset to show what effect sizes and noise levels look like in real e-commerce tests.
6. A two-page readout recommending a decision, with intervals and risks.

**Acceptance criteria**
- The user-level design's bias relative to the known true effect is measured and explained by the interference mechanism.
- The switchback estimate's bias is within ±10% of the true effect on average across runs, and its interval coverage is reported.
- Power analysis matches simulated power within 5 percentage points.
- The sequential rule keeps the simulated false-positive rate at or below 5.5%.
- The pre-registration document is committed before any results file (checked by Git history).
- Oral defence: explain to a non-technical panel why the user-level result was wrong, in under 3 minutes.

**Stretch goals.** Add a geo-holdout design and compare cost; model carry-over explicitly and choose the block length that minimises error.

**What it proves to an employer.** You can design experiments for the hard cases (marketplaces, pricing, logistics) that product and operations teams in quick commerce, food delivery and mobility face every week.

## Feeds into

- [DAN305 Product and Business Analytics](../DAN305_product_and_business_analytics_metrics_funnels/README.md): metric definitions and guardrails become metric trees and north-star metrics.
- [DAN402 Forecasting for Business Decisions](../../year_4/DAN402_forecasting_for_business_decisions/README.md): intervals, seasonality and calendar effects return as forecast uncertainty.
- [DAN403 Domain Analytics](../../year_4/DAN403_domain_analytics_finance_marketing_operations/README.md): lift tests calibrate marketing mix models.
- [DAN501 Frontier Seminar](../../year_5/DAN501_frontier_seminar_decision_intelligence/README.md): causal analytics builds on Chapters 5 and 9.
- [DSC304 Experimental Design and Causal Inference](../../../data_science/year_3/DSC304_experimental_design_and_causal_inference/README.md), for students who want the formal methods in depth.
