# DSC305 · Labs and projects

Two rules apply throughout. **Every feature has a timestamp:** submissions include a feature timeline and a test that fails if any feature uses data after prediction time minus the data delay. **Every metric has a price:** state the cost assumptions behind each metric and operating point, and report expected cost with an interval.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Point-in-time and numeric features | Rebuild three leaky aggregates with as-of joins and a 1-day data delay; log, Yeo-Johnson, binning and splines in a GLM vs a GBDT; customer aggregates with cut-offs | Before/after scores; the timeline test; comparison table; bin stability across two years | 6 h (2 weeks) |
| 2 · Encoding bake-off | One-hot, hashing, naive target encoding, cross-fitted `TargetEncoder`, CatBoost native, hierarchical backoff on high-cardinality columns | Scores under CV and on a holdout; the leak from naive encoding quantified | 4 h |
| 3 · Calendars and spatial CV | Indian holiday and festival table for five years; cyclical encodings; random vs spatial-block CV on H3 cells | Effect of the holiday table on error; spatial leakage measured | 3 h |
| 4 · Embedding, LLM and missingness features | TF-IDF vs two sentence-embedding models vs LLM-extracted attributes, with 100 extractions validated by hand; missingness-as-signal test; four imputers inside CV; a simulated form change | Extraction accuracy; gain per feature family; cost per 1,000 rows; imputation results; damage from the form change and a mitigation | 7 h (2 weeks) |
| 5 · Leakage forensics (AI off) | A "too good" model with three hidden leaks: a post-outcome text field, a global aggregate, a near-duplicate entity | Forensic report with evidence for each leak | 3 h |
| 6 · Cost curves | Cost matrix → threshold; capacity-based evaluation; a model that wins on accuracy and loses money | Expected cost per 1,000 cases with bootstrap intervals for each model | 3 h |
| 7 · Calibration and conformal intervals | Reliability diagrams with bands; Platt, isotonic and temperature scaling; drift across years; split-conformal intervals | Log loss and Brier before/after; coverage table | 5 h (2 weeks) |
| 8 · Imbalance without resampling | SMOTE vs undersampling vs class weights vs threshold moving on a 1% positive problem | Discrimination and calibration for each; recommendation | 3 h |
| 9 · Paired tests and holdout reuse | Paired bootstrap and McNemar for two models; simulate 200 submissions against one holdout | Verdict on the model gain; optimism of the best "submission" | 3 h |
| 10 · Audit generated features | Ask an LLM (or a CAAFE-style tool) for 20 features; apply the timeline test, CV and out-of-time checks | Accept/reject table with reasons | 3 h |

## Projects

### P1 · Encoding a world of IDs (L1, ~6 hours)

**Real-world inspiration.** In the Amazon.com Employee Access Challenge on Kaggle, every predictor is a high-cardinality categorical code (resource, manager, role identifiers). Many business tables look like this: merchant IDs, pincodes, SKU codes. The choice of encoding, and whether it leaks, decides the result.

**What to build.** A reproducible comparison of at least five encoding strategies with logistic regression and a GBDT, including pairwise-interaction encodings, scored with repeated CV and a late Kaggle submission.

**Acceptance criteria**
- All target-dependent encodings are cross-fitted; a test shows the score inflation from a naive version.
- Results report mean ± sd over 5×2 CV for each encoder–model pair, and a paired test for the top two.
- The best pipeline's private-leaderboard AUC is reported, and the CV-to-leaderboard gap is explained.
- Unseen categories are handled explicitly and tested.
- A one-page note recommends an encoder for a similar production table and explains why.

**Stretch goals.** Learned entity embeddings reused in LightGBM; a hierarchical backoff using the dataset's role hierarchy.

**What it proves to an employer.** You can handle the ID-heavy tables most companies actually have, without the leaks that make offline scores lie.

### P2 · Trip-duration promises with honest intervals (L2, ~15 hours)

**Real-world inspiration.** Ride-hailing and delivery apps show an arrival estimate, and late arrivals cost more goodwill than early ones. The NYC TLC trip records provide real pickup and drop-off times, zones and fares for millions of trips.

**What to build.** A model that, at the moment a trip starts, predicts its duration as a point estimate plus an 80% and a 95% interval, using only features available at that moment (zones, time, calendar, recent zone-level conditions with a data delay). Evaluate it like a product: asymmetric cost, interval coverage by hour and borough, and stability month to month.

**Acceptance criteria**
- A feature timeline and an automated test prove that no feature uses information after trip start (for example, no fare, drop-off or tip fields).
- The point model is trained under an asymmetric loss in which lateness costs 3× earliness (illustrative), and compared with an MAE-trained model on that cost.
- Interval coverage is within 2 percentage points of nominal overall and is reported by hour of day and borough; at least one slice that under-covers is diagnosed.
- Evaluation is out-of-time: train on months 1–9, validate on month 10, test on months 11–12.
- Expected cost per 10,000 trips is reported with a bootstrap interval for each model.

**Stretch goals.** Conformalized quantile regression vs plain split conformal; zone embeddings learned from origin–destination pairs; a short note on how weather data (if added) changes coverage.

**What it proves to an employer.** You can build a prediction a product can promise to users, with uncertainty that is measured, not assumed.

### P3 · A calibrated 12-month mortgage default model (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Lenders estimate the probability that a loan will default in the next year, and those probabilities drive provisioning, pricing and collections. The Freddie Mac Single-Family Loan-Level Dataset provides origination and monthly performance data for loans originated since 1999, so a model can be tested across very different economic periods.

**What to build.** From the monthly performance files, construct loan-month observation snapshots with point-in-time features (payment history, delinquency streaks, loan age, current estimated loan-to-value if derivable, origination attributes), label 12-month-ahead default, and deliver a calibrated GBDT and a scorecard-style GLM with a full evaluation report.

**Acceptance criteria**
- Snapshots use only information available at the snapshot month; the timeline test and a shuffled-label test are included.
- Training, validation and test periods are separated by time, and performance is reported by origination vintage and by calendar year, including the 2007–2009 period.
- Calibration is shown with reliability diagrams and Brier/log loss per period; a recalibration strategy for base-rate shifts is implemented and evaluated.
- An operating point for a collections team with fixed capacity is chosen from an explicit cost model, with expected cost and an interval.
- Feature selection is done inside CV and selection stability across resamples is reported.
- The evaluation report follows the Chapter 11 structure and ends with limitations, including what changes if the model is used outside the US mortgage market.

**Stretch goals.** Conformal intervals for expected loss; a comparison with a survival (hazard) formulation; a fairness review using the geographic fields available, with a clear statement of what can and cannot be concluded.

**What it proves to an employer.** You can build a risk model whose probabilities a bank could put in a provisioning calculation, and show how it behaves when the economy changes.

## Feeds into

- [DSC401 Time Series and Forecasting](../../year_4/DSC401_time_series_analysis_and_forecasting/README.md): lags, calendars and pinball loss carry into forecasting.
- [DSC403 Recommender Systems](../../year_4/DSC403_recommender_systems_and_personalization/README.md): ID encodings and embeddings become user and item representations.
- [DSC404 Data Science in Production](../../year_4/DSC404_data_science_in_production_deployment_monitoring/README.md): the P3 model is deployed, monitored for calibration drift and documented.
- [OV10B Fraud Detection and Risk Systems](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10B_fraud_detection_and_risk_systems/README.md): P3 is the foundation for credit-risk work.
