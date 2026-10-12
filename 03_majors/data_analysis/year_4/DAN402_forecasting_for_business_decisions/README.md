# DAN402 · Forecasting for Business Decisions

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L2 → L4 | [DAN302](../../year_3/DAN302_business_statistics_and_experimentation/README.md) | [DAN403](../DAN403_domain_analytics_finance_marketing_operations/README.md), [DAN501](../../year_5/DAN501_frontier_seminar_decision_intelligence/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Data Analysis major](../../README.md). Uses the uncertainty, regression and calendar-effect skills from DAN302, the SQL from [DAN301](../../year_3/DAN301_spreadsheets_to_sql_analytical_querying_in_depth/README.md) and the metric trees from [DAN305](../../year_3/DAN305_product_and_business_analytics_metrics_funnels/README.md). The statistical theory of time series (state-space models in depth, spectral methods, deep sequence models) is taught in [DSC401](../../../data_science/year_4/DSC401_time_series_analysis_and_forecasting/README.md). This course is about forecasts that drive inventory, staffing, budgets and cash, and about the people and processes that use them.

## Why this course matters now

Every plan is a forecast: how much stock a dark store holds before Diwali, how many delivery partners are on shift on a rainy Friday, what next quarter's budget assumes. Uber described forecasting as central to marketplace balancing, hardware capacity planning and marketing (2018). The largest open forecasting competition on retail data, M5, used 42,840 hierarchical Walmart sales series, and its top entries relied heavily on gradient-boosted trees learned across many series. Tools now make forecasts cheap. Pretrained "foundation" models such as Google's TimesFM and Amazon's Chronos forecast a series they have never seen with no training, and an AI assistant will write a Prophet or LightGBM pipeline in a minute. Most of what goes wrong is still human. People pick an accuracy metric that rewards the wrong forecast, train on data that leaks the future, treat sales as demand when shelves were empty, override models with optimistic adjustments, and present one number where a range was needed. This course trains the judgement that turns a forecast into a good decision.

## Learning outcomes

By the end you can:

1. **Frame** a forecasting problem from the decision it serves: horizon, granularity, lead time, the cost of over- and under-forecasting, and whether a point, quantile or full distribution is needed.
2. **Prepare** business time series correctly: calendars (Indian fiscal year, festivals that move with lunar calendars, paydays), stock-out censoring, structural breaks and new items.
3. **Benchmark** every model against naive, seasonal naive and ETS baselines with rolling-origin cross-validation, and **detect** leakage.
4. **Choose** an accuracy metric from the decision's costs. **Explain** why MAPE misleads, and **report** MASE, WAPE, bias, quantile loss and interval coverage.
5. **Build** ETS, ARIMA-with-regressors, gradient-boosted global models and intermittent-demand methods, and **reconcile** forecasts across a hierarchy.
6. **Evaluate** pretrained time-series foundation models honestly against strong baselines on your own data.
7. **Run** a forecasting process: forecast value added, judgmental adjustment rules, scenarios and driver-based budget forecasts.
8. **Convert** probabilistic forecasts into decisions (service levels, the newsvendor quantile, staffing) and **communicate** them with fan charts and ranges.

## Chapters and lessons

### Chapter 1 · Forecasts serve decisions (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Forecast, target, plan | A forecast is what we expect; a target is what we want; a plan is what we will do; mixing them corrupts all three | Classify 10 "forecasts" from a mock business review |
| 1.2 Framing | Horizon, granularity (SKU × store × day vs category × month), lead time, update frequency | Frame forecasts for a dark store, a call centre and a CFO |
| 1.3 Cost of error | Asymmetric costs (stock-out vs waste); why the decision sets the metric | Write the cost function for 3 decisions |
| 1.4 Point vs probabilistic | Quantiles, intervals, full distributions; who needs which | Rewrite 3 point forecasts as decision-ready ranges |

**Check your understanding:** Why does a sales team's "forecast" that equals its target damage inventory planning? For perishable groceries, is over- or under-forecasting worse, and how does that change the forecast you should publish? Who needs a single number, and who needs a distribution?

### Chapter 2 · Data for forecasting (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Time-series structure | Trend, seasonality (weekly, yearly, multiple), cycles, noise; seasonal and subseries plots; autocorrelation | Explore monthly UPI volumes and daily all-India power demand (Grid-India reports) |
| 2.2 Indian calendars | April–March fiscal year; Diwali, Eid and other festivals that move between months; monsoon; paydays and month-end | Build a holiday table for 5 years with moving festival dates |
| 2.3 Sales are not demand | Stock-outs censor demand; lost sales; substitution | Flag censored days in M5 data; estimate what demand might have been |
| 2.4 Breaks and anomalies | 2020 lockdowns, policy changes, outages; when to drop, adjust or model them | Decide a treatment for the 2020 break in 3 series |
| 2.5 New items and short histories | Analogues, category curves, cold start | Forecast a new SKU from analogous launches |

**Check your understanding:** Why does a model trained on sales under-forecast demand for popular items that often sell out? Why can a monthly model show a "Diwali effect" in the wrong month? When should a structural break be removed from training data, and when must it stay?

### Chapter 3 · Baselines and honest validation (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Simple methods | Mean, naive, seasonal naive, drift; why they are hard to beat | Baselines for 100 M5 series |
| 3.2 Rolling-origin cross-validation | Expanding vs sliding windows; horizon-specific errors | Cross-validate baselines at 1, 7 and 28 days ahead |
| 3.3 Leakage | Future information in features, rolling statistics computed over the whole series, target-derived features, revised data | Find the 4 leaks in a provided "great" model |
| 3.4 Benchmark discipline | What the M competitions taught about simple methods and combinations | Write the benchmark section of a forecast report |

**Check your understanding:** Why is a random train/test split wrong for time series? A model beats seasonal naive by 30% in testing and loses in production: list three causes. Why should every forecast report include a naive benchmark?

### Chapter 4 · Measuring accuracy (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Scale-dependent errors | MAE, RMSE, and which central value each rewards (median vs mean) | Show that the best forecast changes with the metric (Kolassa, 2020) |
| 4.2 Percentage errors and their traps | MAPE undefined at zero, explosive near zero, asymmetric; sMAPE's own problems | Break MAPE on intermittent series; compare with WAPE |
| 4.3 Scaled errors | MASE (Hyndman and Koehler, 2006); RMSSE and WRMSSE as used in M5 | Compute MASE across 100 series of different scales |
| 4.4 Bias and tracking | Mean error, tracking signal, persistent over-forecasting | Detect a biased forecaster from its error history |
| 4.5 Probabilistic accuracy | Pinball (quantile) loss, interval coverage and width, CRPS in outline | Score quantile forecasts at 50%, 80% and 95% |

**Check your understanding:** Why does minimising MAPE push forecasts down? When is RMSE the right metric for a business decision? A 90% interval covers the truth 70% of the time: what does that tell you, and what do you change?

### Chapter 5 · Exponential smoothing (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Simple and Holt | Level and trend smoothing; damped trends for long horizons | Fit SES and damped Holt to 10 series; compare at 12 months |
| 5.2 Holt-Winters | Additive vs multiplicative seasonality | Seasonal forecasts for monthly GST or UPI series |
| 5.3 ETS framework | Error–trend–seasonal state-space models, prediction intervals, AIC-based selection | AutoETS with StatsForecast on 1,000 series |
| 5.4 When ETS wins | Many short, stable series; speed; transparency | ETS vs seasonal naive across the M5 hierarchy levels |

**Check your understanding:** Why do damped trends usually forecast better at long horizons than linear ones? When is multiplicative seasonality the right choice? What does an ETS prediction interval assume that real business data often violates?

### Chapter 6 · Regression, ARIMA and calendar effects (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 ARIMA in outline | Differencing, autocorrelation, ARIMA as a baseline family (depth in DSC401) | AutoARIMA vs AutoETS on 100 series |
| 6.2 Dynamic regression | Regression with ARIMA errors; price, promotion and festival regressors; lagged effects | Promotion and festival effects for a store category |
| 6.3 Multiple seasonality | Fourier terms for daily, weekly and yearly patterns | Hourly demand for NYC taxi trips or Grid-India data |
| 6.4 Prophet and its limits | Decomposable trend + seasonality + holidays (Taylor and Letham, 2018); where it underperforms baselines | Prophet vs ETS vs seasonal naive under cross-validation |

**Check your understanding:** Why do you need to forecast your regressors too, and what if you cannot? How do you model a festival whose date moves every year? Why is a good-looking decomposition plot not evidence of forecast accuracy?

### Chapter 7 · Hierarchies and coherence (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Hierarchical and grouped series | Store × category × region × total; why plans must add up | Build the M5 hierarchy (12 levels) |
| 7.2 Bottom-up, top-down, middle-out | Strengths at each level; noise at the bottom, lost detail at the top | Compare the three on 2 levels |
| 7.3 Optimal reconciliation | MinT reconciliation (Wickramasuriya, Athanasopoulos and Hyndman, 2019) | Reconcile base forecasts; measure accuracy at every level |
| 7.4 Coherence in planning | Finance, supply chain and sales using one number | Show how incoherent forecasts create conflicting plans (illustrative) |

**Check your understanding:** Why can reconciliation improve accuracy at every level, not just make numbers add up? When is bottom-up the right choice? What organisational problem does a coherent hierarchy solve?

### Chapter 8 · Machine learning and global models (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Features | Lags, rolling statistics (computed only from the past), calendar, price, promotions, item attributes | Feature pipeline with a leakage test |
| 8.2 Global gradient boosting | One LightGBM model across thousands of series; why it did well in M5 | Global LightGBM vs local ETS on 3,000 series |
| 8.3 Multi-step strategies | Recursive vs direct vs multi-output; error accumulation | Compare recursive and direct at 28 days ahead |
| 8.4 Intermittent demand | Croston, SBA, TSB; zero-inflated thinking; which metrics make sense | Spare-parts-style series: Croston vs zero forecast vs LightGBM |
| 8.5 Quantile models | Quantile regression with gradient boosting; conformal intervals in outline | 80% intervals with measured coverage |

**Check your understanding:** Why can a global model forecast a short series better than a model trained on that series alone? Why can a "zero" forecast score well on some metrics for intermittent items, and why is it useless? How do rolling-window features leak if computed carelessly?

### Chapter 9 · Foundation models and AI assistants (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Pretrained forecasters | TimesFM (Das et al., 2024) and Chronos (Ansari et al., 2024): zero-shot forecasts from patterns learned on large corpora | Zero-shot forecasts on 500 series of your project data |
| 9.2 Benchmarks | GIFT-Eval and similar suites; what zero-shot leaderboards do and do not cover | Read one leaderboard; list its blind spots for Indian retail |
| 9.3 Honest comparison | Same cross-validation, same metrics, against seasonal naive, ETS and LightGBM with regressors | A results table with intervals across series |
| 9.4 AI-written pipelines | Assistants writing forecasting code; typical errors: random splits, leakage, wrong seasonal period, ignored holidays | Audit 3 AI-written pipelines with planted errors |

**Check your understanding:** Where do zero-shot models help most (cold start, many short series), and where do they struggle (strong known drivers such as price and promotions)? Why must a foundation model's test data be checked against its training corpus? What is the first thing you check in an AI-written forecasting script?

### Chapter 10 · Judgement, scenarios and the forecasting process (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Forecast value added | Measuring whether each step (statistical model, planner override, consensus meeting) improves accuracy | FVA analysis of an illustrative override log |
| 10.2 Judgmental adjustments | Evidence that large adjustments help more than small ones and upward adjustments often hurt (Fildes et al., 2009); rules for overrides | Write an override policy with logging |
| 10.3 Scenarios | Events with no history: a competitor launch, a regulatory change (UPI MDR above ₹2,000 from 15 Oct 2026), a weak monsoon | Three scenarios with triggers and leading indicators |
| 10.4 Driver-based forecasts | Budgets from metric trees (users × frequency × AOV); Monte Carlo over drivers | A driver-based revenue forecast with a P10–P90 range |
| 10.5 Sales and operations planning | One forecast feeding demand, supply and finance; meeting cadence | Run a mock monthly planning meeting |

**Check your understanding:** Why do small, frequent overrides often reduce accuracy? How is a scenario different from a forecast interval? What makes a driver-based forecast easier to discuss with a CFO than a model output?

### Chapter 11 · From forecast to decision (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Inventory decisions | Service levels, safety stock, the newsvendor critical quantile from cost of overage and underage | Order quantities from quantile forecasts for perishables |
| 11.2 Staffing | Translating demand forecasts into shifts; queueing intuition (Erlang C) for call centres and delivery partners | Staff plan for an illustrative support centre |
| 11.3 Cash and finance | Collections and payments forecasting; month-end and quarter-end effects | 13-week cash forecast for an illustrative company |
| 11.4 Communicating forecasts | Fan charts, ranges in words, what would change the forecast | Present P3 with a fan chart and decision |
| 11.5 Monitoring | Drift in errors, retraining triggers, post-mortems after big misses | A monitoring dashboard with alert rules |

**Check your understanding:** Why should the order quantity for a perishable item usually differ from the median forecast? What does a staffing plan need that a demand forecast does not give? What should a forecast post-mortem conclude besides "the model was wrong"?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Framing and cost functions | — |
| 2 | 2 | Lab 2 · Indian calendar and censoring | Holiday table |
| 3 | 3 | Lab 3 · Baselines and leakage hunt | **P1 due** |
| 4 | 4 | Lab 4 · Metric shoot-out | — |
| 5 | 5 | Lab 5 · ETS at scale | — |
| 6 | 6 | Lab 6 · Regressors and festivals | Mid-term (AI off) |
| 7 | 7 | Lab 7 · Hierarchical reconciliation | — |
| 8 | 8 | Lab 8 · Global LightGBM | — |
| 9 | 8 | Lab 8 (cont.) · Intermittent and quantiles | **P2 due** |
| 10 | 9 | Lab 9 · Foundation models vs baselines | Comparison table |
| 11 | 10 | Lab 10 · FVA and overrides | — |
| 12 | 10 | Scenarios and driver-based budget | Scenario memo |
| 13 | 11 | Newsvendor and staffing | — |
| 14 | 11 | Forecast review presentations | **P3 due** |
| 15 | Review | Oral defence | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** writing StatsForecast, LightGBM and plotting code you then test; generating holiday tables (checked against official calendars); explaining a model's equations; drafting scenario narratives. Claude, ChatGPT, Gemini in Colab and GitHub Copilot all help here.
- **Do without AI (drills):** framing forecasts and writing cost functions; computing MASE and pinball loss by hand on small examples; spotting leakage in code; the newsvendor calculation; the mid-term and final.
- **Verify AI output by:**
  - checking every split is time-ordered and every feature uses only past data (a unit test that shifts the target and expects failure);
  - comparing against seasonal naive and ETS on the same folds;
  - checking the seasonal period and holiday dates;
  - checking that interval coverage on held-out data is close to nominal.
- **Where AI still fails here:** in labs you will see assistants use random train/test splits, compute rolling features over the full series, choose MAPE for intermittent demand, and set weekly seasonality on monthly data. Foundation models can also look strong on a benchmark and weak on your series with promotions and festivals. You will measure that in Lab 9, not assume it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| Projects P1 · P2 · P3 | 10% · 20% · 25% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 15% |

**Mastery gate.** You pass when you can: (1) with AI off, given a decision and its costs, choose the metric and the forecast quantile and justify both in 20 minutes; (2) with AI off, find the leakage and validation errors in a provided forecasting script in 30 minutes; (3) deliver a hierarchical forecast for an unseen dataset that beats seasonal naive on MASE at the levels that matter, with intervals whose held-out coverage is within 5 points of nominal, and turn it into an order or staffing decision.

## Industry reality

Retailers, quick-commerce companies, airlines, utilities, banks and ride-hailing firms all forecast at scale. Uber's 2018 overview lists marketplace, capacity and marketing forecasting; the M4 competition was won by a hybrid of exponential smoothing and neural networks, and M5 by gradient-boosted global models. In India, power-system operators forecast demand daily, and consumer companies plan around festivals whose dates move every year. Pretrained forecasting models are being tested in industry. Honest comparisons against baselines on in-house data decide whether they are adopted.

**Interview questions from this course**

1. *"How would you forecast daily orders for each dark store for the next 4 weeks?"* Strong answer: frames the decision (staffing, inventory); handles calendar effects and stock-out censoring; starts with seasonal naive and ETS; considers a global LightGBM with regressors; reconciles store and city levels; reports quantiles; validates with rolling origin.
2. *"Why not just use MAPE?"* Strong answer: undefined at zero, explodes near zero, rewards under-forecasting, cannot be averaged across scales sensibly; proposes WAPE, MASE or a cost-weighted metric tied to the decision; mentions bias tracking.
3. *"Your model is 25% better than naive in testing but worse in production."* Strong answer: leakage, random splits, revised data, regime change, different horizon or aggregation; describes how to check each.
4. *"Sales planners keep overriding the forecast. What do you do?"* Strong answer: measure forecast value added for overrides; log reasons; restrict small adjustments; feed known events in as regressors; review persistent bias.
5. *"How much bread should a store order if waste costs ₹20 a loaf and a lost sale costs ₹10?"* Strong answer: newsvendor critical ratio = underage / (underage + overage) = 10/30 ≈ 0.33; order the 33rd percentile of the demand forecast; explains why it is below the median.

## Resources (free first)

- **Textbooks:** Hyndman and Athanasopoulos, [*Forecasting: Principles and Practice*, 3rd ed.](https://otexts.com/fpp3/) (R); Hyndman, Athanasopoulos, Garza, Challu, Mergenthaler and Olivares, [*Forecasting: Principles and Practice, the Pythonic Way*](https://otexts.com/fpppy/) (Python, Nixtla libraries).
- **Libraries:** [StatsForecast](https://nixtlaverse.nixtla.io/statsforecast/index.html); [Prophet](https://facebook.github.io/prophet/); [TimesFM](https://github.com/google-research/timesfm); [Chronos](https://github.com/amazon-science/chronos-forecasting).
- **Papers:** Hyndman and Koehler, [Another look at measures of forecast accuracy](https://robjhyndman.com/papers/mase.pdf) (2006); Das et al., [TimesFM](https://arxiv.org/abs/2310.10688); Ansari et al., [Chronos](https://arxiv.org/abs/2403.07815); Aksu et al., [GIFT-Eval](https://arxiv.org/abs/2410.10393); Salinas et al., [DeepAR](https://arxiv.org/abs/1704.04110).
- **Industry:** Uber Engineering, [Forecasting at Uber: An Introduction](https://www.uber.com/blog/forecasting-introduction/) (2018).
- **Datasets:** [M5 Forecasting](https://www.kaggle.com/competitions/m5-forecasting-accuracy); [Rossmann Store Sales](https://www.kaggle.com/competitions/rossmann-store-sales); [UCI Electricity Load Diagrams](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014); [NYC TLC trip records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page); [Grid-India](https://grid-india.in/) daily power supply reports; [Agmarknet](https://agmarknet.gov.in/) mandi prices; [NPCI UPI statistics](https://www.npci.org.in/what-we-do/upi/product-statistics); [RBI DBIE](https://data.rbi.org.in/DBIE/).
- **Paid, optional:** Michael Gilliland, *The Business Forecasting Deal* (Wiley, 2010), on forecast value added.

## Sources

All checked 12 Oct 2026.

- Uber Engineering, "Forecasting at Uber: An Introduction" (6 Sep 2018) — https://www.uber.com/blog/forecasting-introduction/
- Makridakis, Spiliotis and Assimakopoulos, "M5 accuracy competition: Results, findings, and conclusions", *International Journal of Forecasting* 38(4), 2022 · competition page — https://www.kaggle.com/competitions/m5-forecasting-accuracy
- Hyndman and Koehler, *International Journal of Forecasting* 22(4), 2006 — https://robjhyndman.com/papers/mase.pdf
- Kolassa, "Why the 'best' point forecast depends on the error or accuracy measure", *International Journal of Forecasting* 36(1), 2020
- Fildes, Goodwin, Lawrence and Nikolopoulos, "Effective forecasting and judgmental adjustments", *International Journal of Forecasting* 25(1), 2009
- Wickramasuriya, Athanasopoulos and Hyndman, "Optimal forecast reconciliation for hierarchical and grouped time series through trace minimization", *JASA* 114(526), 2019
- Taylor and Letham, "Forecasting at Scale", *The American Statistician* 72(1), 2018
- Das, Kong, Sen and Zhou, TimesFM (arXiv 2310.10688) · Ansari et al., Chronos (arXiv 2403.07815) · Aksu et al., GIFT-Eval (arXiv 2410.10393)
- *Forecasting: Principles and Practice, the Pythonic Way* (updated 10 Oct 2026) — https://otexts.com/fpppy/
- NPCI, MDR on select UPI P2M transactions: FAQs (15 Sep 2026) — https://www.npci.org.in/uploads/FA_Qs_Merchant_Discount_Rate_MDR_on_Select_UPI_P2_M_Transactions_58dba1d39e.pdf

_Last reviewed: 2026-10_
