# DSC401 · Time Series Analysis and Forecasting

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [DSC301](../../year_3/DSC301_statistical_inference_and_modeling/README.md) (uses [DSC303](../../year_3/DSC303_data_wrangling_at_scale_pandas_polars_and_spark/README.md) and [DSC305](../../year_3/DSC305_feature_engineering_and_model_evaluation/README.md)) | [DSC501](../../year_5/DSC501_frontier_seminar_bayesian_methods_causal_ml/README.md), [DSC404](../DSC404_data_science_in_production_deployment_monitoring/README.md), [OV10B](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10B_fraud_detection_and_risk_systems/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Data Science major](../../README.md). The Data Analysis major's [DAN402](../../../data_analysis/year_4/DAN402_forecasting_for_business_decisions/README.md) teaches analysts to produce and use business forecasts with standard tools. This course goes deeper: the models' statistics, large-scale global and hierarchical forecasting, probabilistic forecasts, rigorous backtesting and foundation models.

## Why this course matters now

Forecasts set inventory, staffing, cash, prices and grid capacity, and forecast error has ended businesses. When Zillow wound down its home-buying business in November 2021, its CEO said "the unpredictability in forecasting home prices far exceeds what we anticipated". The largest public forecasting test of the last decade, the M5 competition, asked teams to forecast 42,840 hierarchical Walmart sales series; its findings shifted practice toward global machine-learning models trained across many series (Makridakis et al., 2022). Since 2024, pretrained time-series foundation models forecast new series zero-shot: Amazon's Chronos-2 (October 2025, Apache-2.0 licence), Google's TimesFM 3.0 (August 2026, with native multivariate and covariate support, but pretrained weights restricted to non-commercial use, with production use offered through BigQuery ML) and Salesforce's Moirai 2.0 (CC BY-NC 4.0 weights). Vendors report leaderboard wins on GIFT-Eval and fev-bench, and new "living" benchmarks such as LiveHouse-TS (August 2026) test models prequentially on real future data because static test windows can flatter them. A forecaster in 2026 must still decide what to forecast, at what level and horizon, how to backtest without leakage, whether a foundation model's licence and accuracy fit the use, and how to turn a distribution into a decision.

## Learning outcomes

By the end you can:

1. **Frame** a forecasting problem as a decision (quantity, level, horizon, lead time, cost of over- and under-forecasting) and **derive** the optimal quantile for a newsvendor decision.
2. **Explore** series with decompositions, autocorrelation and calendar analysis, and **detect** structural breaks.
3. **Fit and diagnose** ETS and (S)ARIMA(X) models, and **explain** their assumptions and prediction intervals.
4. **Design** a rolling-origin backtest and **choose** scale-free point and probabilistic metrics (MASE, RMSSE, pinball loss, WQL, CRPS, coverage).
5. **Build** global machine-learning forecasters (LightGBM with lag features, direct vs recursive strategies) and **handle** intermittent demand.
6. **Reconcile** hierarchical forecasts (bottom-up, top-down, MinT) and **measure** the gain.
7. **Produce** calibrated probabilistic forecasts (quantile, conformal, simulation) and **use** them for inventory and staffing decisions.
8. **Evaluate** time-series foundation models fairly against tuned baselines, including licence, contamination and cost.
9. **Run** a forecasting process in production: forecast value added, judgemental overrides, monitoring and communication.

## Chapters and lessons

### Chapter 1 · Forecasting as a decision (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What to forecast | Quantity, unit, aggregation level, horizon, frequency, lead time; who uses it | Write the forecasting spec for dark-store demand in a quick-commerce business (illustrative) |
| 1.2 Point vs distribution | Why the mean is rarely the decision; quantiles, intervals, scenarios | Explain to an operations manager why the P90 matters |
| 1.3 The newsvendor | Critical ratio from understock and overstock costs; quantile as the optimal order | Compute order quantities for perishable vs non-perishable SKUs |
| 1.4 Forecastability | Signal vs noise, coefficient of variation, when to stop improving | Classify 20 series as smooth, erratic, intermittent or lumpy |

**Check your understanding:** (1) Why can the most accurate point forecast give the worst inventory decision? (2) What changes in the spec when lead time moves from 1 day to 2 weeks? (3) When is a series not worth modelling individually?

### Chapter 2 · Time-series data and graphics (weeks 1–2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Time-series data structures | Regular vs irregular timestamps, explicit gaps, time zones, keyed panels | Turn an event log into a regular store × day panel |
| 2.2 Seeing patterns | Time plots, seasonal and subseries plots, lag plots, ACF and PACF | Describe the patterns in all-India electricity demand data |
| 2.3 Calendar effects | Weekday, month length, Indian festivals with moving dates, fiscal-year ends, payday effects | Build a calendar table and measure festival lift |
| 2.4 Breaks and anomalies | Structural breaks (for example, the 2020 lockdowns), level shifts, outliers and how to treat them | Detect and annotate breaks in a monthly payments series |

**Check your understanding:** (1) Why must missing days be explicit before computing lags? (2) What does a slowly decaying ACF suggest? (3) Should lockdown months be removed, modelled or down-weighted? Defend one choice.

### Chapter 3 · Benchmarks and decomposition (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Simple benchmarks | Mean, naive, seasonal naive, drift; why they are hard to beat | Score four benchmarks on 100 series |
| 3.2 Transformations | Log and Box-Cox, calendar and population adjustments | Forecast per-capita and convert back |
| 3.3 Classical and STL decomposition | Trend-cycle, seasonal, remainder; MSTL for multiple seasonalities | Decompose hourly demand with daily and weekly cycles |
| 3.4 Using decomposition to forecast | Seasonally adjusted forecasting and re-seasonalising | Compare STL + ETS with direct ETS |

**Check your understanding:** (1) Why report every model's skill relative to seasonal naive? (2) When does a log transform change the interval shape? (3) What does a large remainder component tell you?

### Chapter 4 · Exponential smoothing (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Simple to Holt–Winters | Level, trend (damped), seasonality; additive vs multiplicative | Fit Holt–Winters by hand on a short series |
| 4.2 ETS state-space models | Error–trend–seasonal taxonomy, likelihood, AIC selection | Run AutoETS on 1,000 series with statsforecast |
| 4.3 Prediction intervals | Analytical vs simulated intervals; why they are often too narrow | Check interval coverage in a backtest |
| 4.4 Automatic selection at scale | AutoETS across thousands of series; short series, outliers and level shifts that break it | Find the 20 series where AutoETS fails worst and explain why |

**Check your understanding:** (1) Why does a damped trend often forecast better than a linear trend? (2) When is multiplicative seasonality needed? (3) What makes model-based intervals too narrow?

### Chapter 5 · ARIMA and dynamic regression (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Stationarity and differencing | Unit roots, KPSS and ADF tests, seasonal differencing | Make a CPI series stationary and justify each step |
| 5.2 ARIMA and SARIMA | AR, MA, identification from ACF/PACF, AutoARIMA | Fit and compare manual and automatic models |
| 5.3 Residual diagnostics | Ljung–Box, residual ACF, normality and its importance for intervals | Diagnose a model with remaining seasonality |
| 5.4 Dynamic regression | ARIMA errors with covariates (prices, promotions, temperature); future covariate availability | Forecast electricity demand with temperature forecasts as inputs |
| 5.5 ETS vs ARIMA | Equivalences, differences, when each wins | Backtest both on the same 200 series |

**Check your understanding:** (1) Why can a regression with ARIMA errors use temperature only if you also forecast temperature? (2) What does a significant Ljung–Box test tell you to do? (3) Why can't you compare AIC between ETS and ARIMA?

### Chapter 6 · Evaluation and backtesting (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Rolling-origin evaluation | Expanding and sliding windows, refit frequency, horizon-wise errors | Build a reusable backtest harness |
| 6.2 Point metrics | MAE, RMSE, MAPE and sMAPE pitfalls, MASE and RMSSE (the M5 metric) | Show MAPE rewarding under-forecasts |
| 6.3 Probabilistic metrics | Pinball loss, weighted quantile loss, CRPS, interval coverage and width | Score quantile forecasts three ways |
| 6.4 Pitfalls | Leakage through features, look-ahead in scaling, cherry-picked windows (Hewamalage et al., 2023) | Find the leak in a supplied backtest |
| 6.5 Comparing forecasters | Many series, many windows; Diebold–Mariano and its limits; skill scores | Decide if model B beats A across 500 series |

**Check your understanding:** (1) Why is a single train/test split weak evidence for a forecaster? (2) Why does MASE use the in-sample naive error as its scale? (3) How can normalising with the full series leak?

### Chapter 7 · Regression-based and Prophet-style models (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Decomposable regression | Piecewise trends, Fourier seasonality, holiday regressors | Build the model by hand with linear regression |
| 7.2 Prophet | Design goals: analyst-in-the-loop forecasting at scale (Taylor and Letham, 2018); changepoints | Fit Prophet with an Indian holiday table |
| 7.3 Where Prophet-style models fail | Short series, strong autocorrelation, regime changes; why benchmarks matter | Backtest Prophet against ETS and seasonal naive |
| 7.4 Dynamic harmonic regression | Fourier terms with ARIMA errors for long seasonal periods | Model hourly data with weekly seasonality |

**Check your understanding:** (1) What problem was Prophet designed to solve, and does yours match? (2) Why can automatic changepoints overfit? (3) When are Fourier terms better than seasonal dummies?

### Chapter 8 · Machine learning for forecasting (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Global models | One model across many series; series-level features; scaling | Train LightGBM across 3,000 products |
| 8.2 Feature engineering for time | Lags respecting the horizon, rolling stats, calendar, price and promotion features | Build an mlforecast pipeline with a 2-day data delay |
| 8.3 Multi-step strategies | Recursive vs direct vs multi-output; error accumulation | Compare recursive and direct for a 28-day horizon |
| 8.4 Intermittent demand | Croston, SBA, TSB, zero-inflated and Tweedie losses | Forecast slow-moving SKUs and score with the right metric |
| 8.5 Lessons from M5 | What the top solutions had in common; ensembles; the cost of complexity | Reproduce a simplified top-50 approach on a subset |

**Check your understanding:** (1) Why do global models help short series? (2) What leakage appears when a lag is shorter than the horizon? (3) Why is MAE a poor loss for intermittent demand?

### Chapter 9 · Hierarchical and grouped forecasting (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Coherence | Store → region → country; product → category; why separate forecasts disagree | Show incoherent forecasts in the M5 hierarchy |
| 9.2 Reconciliation methods | Bottom-up, top-down, middle-out, MinT (Wickramasuriya, Athanasopoulos and Hyndman) | Reconcile with hierarchicalforecast and compare accuracy by level |
| 9.3 Temporal hierarchies | Daily, weekly, monthly forecasts of the same quantity | Reconcile daily and weekly forecasts |
| 9.4 Probabilistic coherence | Reconciling distributions, not just means | Produce coherent quantiles for two levels |

**Check your understanding:** (1) Why can reconciliation improve accuracy at every level? (2) When is bottom-up a bad idea? (3) Who needs which level of the hierarchy?

### Chapter 10 · Probabilistic forecasting and decisions (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Quantile models | Quantile regression and quantile GBDTs; crossing quantiles | Fit P10/P50/P90 models and fix crossings |
| 10.2 Conformal intervals for time series | Split conformal with temporal calibration windows; adaptive conformal ideas | Achieve 90% coverage in a backtest |
| 10.3 Simulation and scenarios | Bootstrapped residual paths, scenario sets for planning | Simulate 1,000 demand paths for a festival week |
| 10.4 From forecasts to decisions | Inventory (newsvendor and base-stock), staffing, capacity | Compute fill rate and waste under three forecasting methods |

**Check your understanding:** (1) Why does exchangeability matter for conformal intervals on time series? (2) Why can a forecast with worse RMSE give better fill rates? (3) What is a scenario set useful for that a quantile is not?

### Chapter 11 · Foundation models for time series (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 How they work | Tokenising or patching series; encoder and decoder designs; Chronos (2024), Chronos-Bolt and Chronos-2, TimesFM 2.5 and 3.0, Moirai 2.0 | Run three models zero-shot on the same 500 series |
| 11.2 Covariates and multivariate inputs | What Chronos-2 and TimesFM 3.0 add; when covariates help | Add price and holiday covariates and measure the gain |
| 11.3 Evaluating them fairly | GIFT-Eval (23 datasets, about 144,000 series), fev-bench, LiveHouse-TS; contamination between pretraining corpora and test sets; tuned baselines | Compare zero-shot models with tuned ETS and LightGBM under your backtest |
| 11.4 Licences, cost and deployment | Apache-2.0 vs non-commercial weights; managed services; latency and GPU cost | Write a one-page model-selection note including licence terms |
| 11.5 Fine-tuning | When to fine-tune; LoRA and full fine-tuning; risk of overfitting small data | Fine-tune one model and compare with zero-shot |

**Check your understanding:** (1) Why might a foundation model score well on a public benchmark and poorly on your data? (2) Can you deploy TimesFM 3.0's downloaded weights in a commercial product? (3) When is zero-shot forecasting the right default?

### Chapter 12 · Forecasting in production (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 The forecasting process | Cadence, owners, forecast value added (FVA), judgemental overrides and their track record | Compute FVA for planner overrides in a supplied log |
| 12.2 Monitoring | Error tracking by segment, bias alarms, drift, automatic fallbacks to benchmarks | Build a monitoring table with alert thresholds |
| 12.3 Nowcasting and mixed frequency | Using weekly or daily indicators to estimate the current month | Nowcast a monthly index from higher-frequency data |
| 12.4 Communicating forecasts | Fan charts, scenario narratives, explaining misses | Present a forecast and its uncertainty to a mock operations review |
| 12.5 Case study: when forecasts break | Zillow Offers (2021); lessons on model risk and business exposure | Write a one-page post-mortem from public sources |

**Check your understanding:** (1) How do you decide whether planners' overrides help? (2) What should happen automatically when a forecast's error doubles? (3) What made forecast error so costly in the Zillow case, beyond the model itself?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1–2 | Lab 1 · Forecasting spec and newsvendor | — |
| 2 | 2–3 | Lab 1 (cont.): Electricity demand decomposition | — |
| 3 | 4 | Lab 2 · ETS at scale | — |
| 4 | 5 | Lab 3 · ARIMA and dynamic regression | **P1 due** |
| 5 | 5–6 | Lab 4 · Backtest harness | — |
| 6 | 6 | Lab 4 (cont.): metric pitfalls | — |
| 7 | 7 | Lab 5 · Prophet vs benchmarks | Mid-term (AI off) |
| 8 | 8 | Lab 6 · Global LightGBM forecaster | — |
| 9 | 8 | Lab 6 (cont.): Intermittent demand | — |
| 10 | 9 | Lab 7 · Reconciliation | **P2 due** |
| 11 | 10 | Lab 8 · Conformal intervals and inventory simulation | — |
| 12 | 11 | Lab 9 · Foundation models and licences | P3 checkpoint |
| 13 | 12 | Lab 10 · FVA and monitoring | — |
| 14 | 12 | Forecast review rehearsal | **P3 due** |
| 15 | Review | Forecast review panel on P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** backtest harness code; translating between statsforecast, sktime, Darts and R's fable; feature pipelines for mlforecast; running foundation models through their documented APIs; drafting the forecast narrative. Claude Code, GitHub Copilot, ChatGPT and Gemini all help; BigQuery ML exposes TimesFM through SQL.
- **Do without AI (drills):** reading ACF/PACF plots; specifying the forecast (level, horizon, lead time, cost); computing a newsvendor quantity; spotting leakage in a backtest; explaining an interval to an operations manager. The mid-term and final are AI-off.
- **Verify AI output by:** (1) beating seasonal naive and a tuned ETS in your own rolling-origin backtest before believing any model; (2) checking that every feature is available at forecast time for the full horizon; (3) checking interval coverage, not only point error; (4) reading the model card and licence of any foundation model before use.
- **Where AI still fails here:** foundation-model leaderboards are reported mostly by the models' own developers, on public data that may overlap pretraining corpora, which is why benchmark builders publish "non-leaking" pretraining sets and live benchmarks. You will produce your own evidence in Lab 9: the share of your series where each zero-shot model beats tuned ETS and LightGBM, and by how much. Assistants also routinely compute rolling features over the full series before splitting; Lab 4 asks you to log every instance you catch.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 40% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + forecast review panel | 25% |

**Mastery gate.** You pass when you can: (1) given an unseen panel of 500 series and a decision brief, deliver within one day a backtested forecasting system that beats seasonal naive on MASE and achieves interval coverage within 3 points of nominal; (2) AI off, choose and justify a model family, a metric and a reconciliation method for a described hierarchy; (3) recommend for or against a foundation model for a stated commercial use, with evidence on accuracy, cost and licence.

## Industry reality

Retail, quick commerce, energy, finance and logistics all forecast at scale. Public evidence includes the M5 competition on Walmart data (Makridakis et al., 2022), Meta's description of Prophet as analyst-in-the-loop forecasting at scale (Taylor and Letham, 2018), and TimesFM's integration into BigQuery ML and Google Sheets connected sheets (per the TimesFM repository, 2026). In India, the Reserve Bank's Database on Indian Economy, NPCI's monthly UPI statistics and Grid-India's power-supply reports are public series used for nowcasting and planning. Zillow's 2021 exit from home-buying is a public example of forecast error turning into balance-sheet risk.

**Interview questions from this course**

1. *Forecast daily demand for 5,000 SKUs across 300 dark stores.* Strong answer: clarifies decision, horizon and lead time; global LightGBM or similar with lags respecting the horizon, plus a statistical baseline; intermittent-demand handling; hierarchical reconciliation; quantiles for replenishment; rolling backtests; monitoring.
2. *Why not just use MAPE?* Strong answer: undefined or exploding near zero, asymmetric, favours under-forecasting; proposes MASE/RMSSE for point and pinball/WQL or CRPS for probabilistic forecasts, tied to the decision cost.
3. *A foundation model beats your model on a public leaderboard. Switch?* Strong answer: tests on your data with your backtest; checks contamination risk, covariate support, latency and cost; reads the licence (for example, non-commercial weights); keeps a fallback.
4. *Your forecast missed badly during a festival week. What do you do?* Strong answer: separates a bias from a variance problem; checks the calendar feature (moving dates), data delays and promotion inputs; measures historical festival errors; adds scenario forecasts and override rules with FVA tracking.
5. *How do you make forecasts for stores, cities and the country agree?* Strong answer: explains incoherence; bottom-up vs top-down vs MinT; evaluates accuracy at each level; reconciles quantiles carefully; notes who uses each level.

## Resources (free first)

- **Texts:** Hyndman and Athanasopoulos, *Forecasting: Principles and Practice*, 3rd ed. (R) — https://otexts.com/fpp3/ ; Python edition — https://otexts.com/fpppy/ ; Hewamalage, Ackermann and Bergmeir, "Forecast evaluation for data scientists" — https://doi.org/10.1007/s10618-022-00894-5
- **Software:** statsforecast — https://nixtlaverse.nixtla.io/statsforecast/ ; mlforecast — https://nixtlaverse.nixtla.io/mlforecast/ ; hierarchicalforecast — https://nixtlaverse.nixtla.io/hierarchicalforecast/ ; Prophet — https://facebook.github.io/prophet/ ; fev (benchmarking) — https://github.com/autogluon/fev
- **Foundation models:** Chronos-2 — https://huggingface.co/amazon/chronos-2 ; TimesFM — https://github.com/google-research/timesfm ; Moirai 2.0 — https://arxiv.org/abs/2511.11698 ; GIFT-Eval — https://huggingface.co/spaces/Salesforce/GIFT-Eval ; LiveHouse-TS — https://arxiv.org/abs/2608.17299
- **Data:** M5 (Kaggle) — https://www.kaggle.com/c/m5-forecasting-accuracy and materials — https://github.com/Mcompetitions/M5-methods ; Corporación Favorita grocery sales (Kaggle) — https://www.kaggle.com/c/favorita-grocery-sales-forecasting ; RBI Database on Indian Economy — https://data.rbi.org.in/ ; NPCI UPI product statistics — https://www.npci.org.in/what-we-do/upi/product-statistics ; Grid-India — https://grid-india.in/ ; OpenAQ air-quality API — https://docs.openaq.org/
- **Further reading:** Petropoulos et al., "Forecasting: theory and practice", *International Journal of Forecasting* (2022), an encyclopaedic review — https://doi.org/10.1016/j.ijforecast.2021.11.001 . No paid text is required for this course.

## Sources

- Zillow Group, Q3 2021 results and plan to wind down Zillow Offers, Form 8-K Exhibit 99.1 (2 Nov 2021) — https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/q32021991.htm (checked 2026-10)
- Makridakis, Spiliotis and Assimakopoulos, "M5 accuracy competition: Results, findings, and conclusions", *International Journal of Forecasting* (2022) — https://doi.org/10.1016/j.ijforecast.2021.11.013 (checked 2026-10)
- Taylor and Letham, "Forecasting at Scale", *The American Statistician* (2018) — https://doi.org/10.1080/00031305.2017.1380080 (checked 2026-10)
- Wickramasuriya, Athanasopoulos and Hyndman, MinT reconciliation, *JASA* — https://doi.org/10.1080/01621459.2018.1448825 (checked 2026-10)
- Hewamalage, Ackermann and Bergmeir, *Data Mining and Knowledge Discovery* (2023) — https://doi.org/10.1007/s10618-022-00894-5 (checked 2026-10)
- Amazon Science, chronos-forecasting repository (Chronos-2 released 20 Oct 2025; Apache-2.0) — https://github.com/amazon-science/chronos-forecasting ; Ansari et al., Chronos-2 report (arXiv 2510.15821) — https://arxiv.org/abs/2510.15821 (checked 2026-10)
- Google Research, TimesFM repository (TimesFM 3.0, Aug 2026; weight licence notice; BigQuery ML rollout Sep 2026) — https://github.com/google-research/timesfm ; Das et al., "A decoder-only foundation model for time-series forecasting" (ICML 2024) — https://arxiv.org/abs/2310.10688 (checked 2026-10)
- Liu et al., "Moirai 2.0" (arXiv 2511.11698) — https://arxiv.org/abs/2511.11698 ; model card licence CC BY-NC 4.0 — https://huggingface.co/Salesforce/moirai-2.0-R-small (checked 2026-10)
- Aksu et al., "GIFT-Eval" (arXiv 2410.10393) — https://arxiv.org/abs/2410.10393 ; fev-bench (arXiv 2509.26468) — https://arxiv.org/abs/2509.26468 ; Wen et al., "LiveHouse-TS" (arXiv 2608.17299, Aug 2026) — https://arxiv.org/abs/2608.17299 (checked 2026-10)

_Last reviewed: 2026-10_
