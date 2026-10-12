# DSC401 · Labs and projects

Every forecasting result in this course comes from a **rolling-origin backtest** with at least five forecast origins, is reported **relative to seasonal naive**, and includes **interval coverage**. Features must be available at forecast time for the whole horizon; state the data delay you assume. Foundation models may be used anywhere, but always next to tuned statistical and ML baselines, with their licence recorded.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Spec, newsvendor and decomposition | Specs for three forecasting use cases with critical ratios and order quantities; STL/MSTL on Indian power-demand data from Grid-India reports, calendar and festival effects, break detection | Specs and newsvendor calculations; decomposition plots; calendar table; annotated breaks | 5 h (2 weeks) |
| 2 · ETS at scale | AutoETS with statsforecast on 1,000 retail series; interval coverage check | Accuracy and coverage vs seasonal naive | 3 h |
| 3 · ARIMA and dynamic regression | Manual vs AutoARIMA on a CPI or IIP series from RBI DBIE; dynamic regression with temperature for electricity | Diagnostics (Ljung–Box, residual ACF); backtest table | 4 h |
| 4 · Backtest harness and metric pitfalls | A reusable rolling-origin harness; MAPE vs MASE vs pinball; a planted look-ahead leak | Harness code with tests; the leak found and quantified; log of assistant-introduced leaks | 5 h (2 weeks) |
| 5 · Prophet vs benchmarks | Prophet with an Indian holiday table vs ETS and seasonal naive on 50 series | Win/loss table with skill scores | 3 h |
| 6 · Global and intermittent demand models | mlforecast on an M5 subset (recursive vs direct, lags with a data delay); Croston, SBA, TSB and a Tweedie GBDT on slow-moving SKUs | RMSSE by horizon; leakage test; intermittent-demand scores with appropriate metrics; recommendation | 7 h (2 weeks) |
| 7 · Reconciliation | Bottom-up, top-down and MinT on the M5 hierarchy with hierarchicalforecast | Accuracy by level before and after reconciliation | 3 h |
| 8 · Conformal intervals and inventory simulation | Conformal intervals in a backtest; simulate fill rate and waste under three forecasting methods | Coverage table; inventory cost comparison | 4 h |
| 9 · Foundation models and licences | Chronos-2, TimesFM 2.5 (and 3.0 for non-commercial evaluation) and Moirai 2.0 zero-shot vs tuned ETS and LightGBM; covariates on and off | Share of series where each model wins; cost and latency; licence table | 4 h |
| 10 · FVA and monitoring | Forecast value added of planner overrides in a supplied log; monitoring table with alert thresholds | FVA report; monitoring spec | 3 h |

## Projects

### P1 · Forecasting India's UPI volumes (L1, ~6 hours)

**Real-world inspiration.** NPCI publishes monthly UPI transaction volumes and values. Banks, payment companies and infrastructure teams plan capacity months ahead, and the series combines steep growth, festival peaks and month-length effects.

**What to build.** A 12-month forecast of monthly UPI transaction volume with 80% and 95% intervals, comparing seasonal naive, drift, ETS (on the log scale) and ARIMA, with a written explanation for a capacity planner.

**Acceptance criteria**
- Data are reproducibly collected from the NPCI statistics page (or a documented snapshot), with the snapshot date recorded.
- A rolling-origin backtest with at least 12 origins reports MASE and interval coverage for each method.
- The chosen model beats drift and seasonal naive on MASE in the backtest, or the report says honestly that it does not.
- Back-transformed intervals from the log scale are handled correctly and explained.
- A one-page note for a capacity planner gives the P50 and P95 for peak month and states the main risks (growth saturation, policy changes).

**Stretch goals.** A daily-average version that adjusts for month length; a scenario forecast assuming growth slows by half.

**What it proves to an employer.** You can produce a defensible forecast with honest uncertainty for a real Indian payments series, and explain it to non-specialists.

### P2 · Probabilistic air-quality forecasts for Delhi (L2, ~15 hours)

**Real-world inspiration.** In Delhi-NCR, the Commission for Air Quality Management runs the Graded Response Action Plan (GRAP), which triggers restrictions as air-quality index categories worsen. Public station data from CPCB monitors are available through OpenAQ. Decisions depend on the probability that pollution crosses a category boundary, not on a point forecast.

**What to build.** Hourly PM2.5 forecasts for 1–72 hours ahead at five or more Delhi stations, as quantiles, plus the probability of exceeding the PM2.5 level that corresponds to a chosen AQI category, compared across a statistical model, a global LightGBM model and at least one foundation model.

**Acceptance criteria**
- Data gaps, station outages and outliers are handled explicitly and documented; no imputation uses future values.
- The backtest covers at least one full winter season with at least 20 forecast origins.
- Quantile forecasts are scored with pinball loss and coverage by horizon; exceedance probabilities are scored with the Brier score and a reliability diagram.
- At least one model beats a persistence (naive) forecast on pinball loss at horizons beyond 6 hours, or the report explains why not.
- Weather covariates, if used, are limited to values that would have been available at forecast time (forecasts, not observations), and the report says which.
- A short brief explains, for a non-technical audience, how to read a 70% exceedance probability.

**Stretch goals.** A Chronos-2 or TimesFM model with covariates vs without; spatial pooling across stations; a comparison with publicly issued official forecasts if accessible.

**What it proves to an employer.** You can deliver calibrated probabilistic forecasts for a public decision with real, messy sensor data.

### P3 · Hierarchical retail demand forecasting with inventory decisions (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** The M5 competition released Walmart unit sales for 42,840 hierarchical series (3,049 products in 10 stores), with prices, promotions and calendar events. Retailers and quick-commerce operators face the same structure: many intermittent SKU–store series feeding store, region and company plans.

**What to build.** A full forecasting system for the M5 28-day horizon: statistical baselines, a global ML model, at least one foundation model, hierarchical reconciliation, quantile forecasts, and an inventory simulation that turns forecasts into order decisions.

**Acceptance criteria**
- The M5 evaluation period is untouched until the end; model selection uses rolling-origin validation on earlier periods.
- The final system's WRMSSE on the evaluation period is reported and beats the best statistical benchmark listed in the M5 Competitors' Guide.
- Reconciled forecasts are coherent at all 12 aggregation levels, and accuracy is reported by level before and after reconciliation.
- Quantile forecasts (at least P10, P50, P90) are scored with pinball loss and coverage at the product–store level.
- An inventory simulation for 100 sampled product–store pairs reports fill rate and holding cost under three forecasting methods, with a stated cost model.
- A model-selection note compares accuracy, compute cost and licence for each model family, including any foundation model used.
- The repository reruns the full pipeline with one command and documents hardware and run time.

**Stretch goals.** The M5 Uncertainty metric (weighted scaled pinball loss); a fine-tuned foundation model vs zero-shot; an error analysis of the 50 worst series with causes (promotions, stock-outs, new products).

**What it proves to an employer.** You can build a forecasting system of the kind used by retail and quick-commerce companies, judged on the decisions it drives, not just its error.

## Feeds into

- [DSC404 Data Science in Production](../DSC404_data_science_in_production_deployment_monitoring/README.md): the P2 or P3 system is deployed, monitored and presented to stakeholders.
- [DSC501 Frontier Seminar](../../year_5/DSC501_frontier_seminar_bayesian_methods_causal_ml/README.md): hierarchical Bayesian forecasting and conformal methods extend Chapters 9–10.
- [OV10B Fraud Detection and Risk Systems](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10B_fraud_detection_and_risk_systems/README.md): transaction-volume and loss forecasting.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): evaluating foundation models on Indian series is an open, publishable topic.
