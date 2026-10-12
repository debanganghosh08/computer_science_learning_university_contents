# DAN402 · Labs and projects

Every lab and project uses time-ordered validation (rolling origin), reports a seasonal-naive benchmark on the same folds, states the accuracy metric and why it fits the decision, and includes a leakage test: a unit test that must fail if any feature uses future data. Python with StatsForecast, LightGBM and pandas is the default; R with `fable` is accepted.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Framing and cost functions | Frame forecasts for a dark store, a support centre and a finance team: horizon, grain, lead time, cost of over- and under-forecasting | Three framing sheets and the metric each implies | 3 h |
| 2 · Indian calendar and censoring | Build a 5-year holiday and event table with moving festival dates; flag stock-out (censored) days in an M5 subset | Holiday table checked against an official calendar; censoring flags with the rule used | 4 h |
| 3 · Baselines and leakage hunt | Naive, seasonal naive, mean and drift with rolling-origin CV on 100 series; find 4 leaks in a provided model | CV results by horizon; the leaks with fixes and the corrected score | 4 h |
| 4 · Metric shoot-out | Show that MAE, RMSE, MAPE and pinball loss each prefer a different forecast; break MAPE on intermittent data | Notebook, a table of "best" forecasts by metric, and a one-paragraph metric recommendation | 3 h |
| 5 · ETS at scale | AutoETS and damped trends on 1,000 series; compare with seasonal naive by hierarchy level | Accuracy table with MASE and WAPE; run time | 3 h |
| 6 · Regressors and festivals | Dynamic regression with price, promotion and festival regressors; Fourier terms for hourly data; Prophet under the same CV | Effects with intervals; a comparison table; where Prophet lost | 4 h |
| 7 · Hierarchical reconciliation | Bottom-up, top-down and MinT on the M5 hierarchy | Accuracy at every level for each method | 4 h |
| 8 · Global LightGBM, intermittent and quantiles | Global model with past-only features; Croston/SBA/TSB for intermittent items; quantile models with coverage | Results vs ETS; coverage at 50/80/95%; leakage unit test passing | 6 h |
| 9 · Foundation models vs baselines | Zero-shot TimesFM or Chronos vs seasonal naive, ETS and LightGBM on the same folds | Results with intervals across series; where each wins | 4 h |
| 10 · FVA, overrides and scenarios | Forecast value added on an illustrative override log; an override policy; three scenarios with triggers | FVA table, policy, scenario memo | 4 h |

## Projects

### P1 · Forecasting an Indian public series with honest benchmarks (L1, ~6 hours)

**Real-world inspiration.** Analysts at banks, fintechs, commodity traders and government departments forecast public monthly and daily series: payments volumes, tax collections, power demand and mandi prices.

**What to build.** Choose one series with at least 5 years of history: monthly UPI transaction volume (NPCI, downloaded by hand), daily all-India peak demand from Grid-India reports, or daily modal prices and arrivals for one commodity in one major mandi from Agmarknet. Forecast 6 months (monthly) or 8 weeks (daily) ahead with naive, seasonal naive, drift and ETS, plus one regression with calendar effects.

**Acceptance criteria**
- Rolling-origin cross-validation with at least 6 origins; results by horizon.
- MASE and one business metric (WAPE, or pinball loss for intervals) reported for every method, with the choice of metric justified in two sentences.
- An 80% prediction interval whose empirical coverage on the test folds is reported.
- Calendar effects (festival timing, fiscal year-end, monsoon) are handled explicitly and documented.
- A one-page memo with a fan chart, the forecast in words ("between X and Y, most likely Z"), and what would change it.

**Stretch goals.** Add a second series and test whether it helps (for example, rainfall for mandi prices); compare a zero-shot foundation model.

**What it proves to an employer.** You forecast honestly: with baselines, proper validation, sensible metrics and ranges, on real Indian data.

### P2 · Store–item demand forecasting at scale (L2, ~15 hours)

**Real-world inspiration.** The M5 competition asked for daily unit sales of 3,049 Walmart products across 10 stores, aggregated into 42,840 hierarchical series. Its top entries used global gradient-boosted models. Quick-commerce and grocery chains in India face the same problem at the dark-store level.

**What to build.** On the M5 data (one state, or one category across all stores), forecast 28 days ahead at item × store level and reconcile through the hierarchy. Compare seasonal naive, AutoETS, a global LightGBM with past-only features, and an intermittent-demand method for slow movers. Produce quantile forecasts (50%, 80%, 95%).

**Acceptance criteria**
- Rolling-origin validation with at least 3 origins of 28 days; no feature uses information after the forecast origin (leakage test in CI).
- Accuracy reported with WRMSSE (as in M5) or MASE at at least 4 hierarchy levels, with seasonal naive as the reference.
- Reconciled forecasts are coherent (bottom sums to top exactly) and their accuracy is compared with unreconciled ones.
- Empirical coverage of 80% intervals is between 72% and 88% on the test folds, or the gap is explained and corrected.
- Slow-moving items are identified by a stated rule and evaluated with an appropriate metric.
- The full pipeline runs from raw files with one command; run time and machine are stated.

**Stretch goals.** Add a zero-shot foundation model and an ensemble; analyse errors on festival and promotion days separately.

**What it proves to an employer.** You can build a production-shaped demand forecasting pipeline that beats baselines where it matters and reports uncertainty correctly.

### P3 · Forecast-to-decision planner for perishables (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Grocery and quick-commerce operators must decide every day how much perishable stock to order and how many staff to roster. Waste and stock-outs both cost money, and planners adjust model forecasts by hand. The business below is illustrative; demand comes from real data (M5 FOODS items or Rossmann stores).

**What to build.**
1. Reconciled quantile forecasts for a set of perishable-like items across 3 stores (M5 FOODS) or for store traffic (Rossmann), with a seasonal-naive baseline, ETS, a global LightGBM and one foundation model.
2. An ordering policy using the newsvendor critical quantile from stated costs of waste and of a lost sale, and a staffing plan from traffic forecasts.
3. A simulation over held-out periods comparing total cost (waste + lost sales + staffing) under your policy vs a policy based on seasonal-naive point forecasts.
4. A forecast value added study with simulated planner overrides following realistic patterns (frequent small upward adjustments), and an override policy.
5. A scenario module: a festival shifting between months and a 10% price increase on one category, each with its effect on orders.
6. A monitoring dashboard: errors by level, bias, interval coverage and alert rules.
7. A two-page decision memo and a 10-minute presentation to a mock operations head.

**Acceptance criteria**
- Total simulated cost of your policy vs the baseline policy is reported with a bootstrap interval across periods; any claimed saving must have an interval that excludes zero.
- Order quantities change correctly when the cost ratio changes (a test with 3 cost settings).
- The FVA study states whether overrides improved accuracy, by size and direction of adjustment.
- Foundation-model results are reported on the same folds and metrics as everything else, including where they lose.
- Every number in the memo traces to code; the repository rebuilds all results with one command.
- Oral defence: answer "what if waste cost doubles?" live by rerunning the policy.

**Stretch goals.** Add weather as a regressor using public historical weather data; add a shelf-life constraint (items carried over for one day); deploy the dashboard with Evidence or Streamlit.

**What it proves to an employer.** You do not stop at a forecast. You turn it into decisions, measure the rupee value against a simple policy, and manage the human side of forecasting, which is what operations and supply-chain analytics teams need.

## Feeds into

- [DAN403 Domain Analytics](../DAN403_domain_analytics_finance_marketing_operations/README.md): demand, cash and capacity forecasts in finance and operations work.
- [DAN501 Frontier Seminar](../../year_5/DAN501_frontier_seminar_decision_intelligence/README.md): forecasts become inputs to decision models and optimisation.
- [DSC401 Time Series Analysis and Forecasting](../../../data_science/year_4/DSC401_time_series_analysis_and_forecasting/README.md), for students who want the statistical theory in depth.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): foundation-model evaluation on Indian retail or public data is a viable thesis topic.
