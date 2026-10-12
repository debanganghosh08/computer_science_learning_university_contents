# FND116 · Labs and projects

All work is in Python (NumPy, SciPy, pandas, matplotlib) under Git, with random seeds fixed through NumPy's `Generator`. Before any simulation, write down your predicted answer. Every probability you report from a simulation comes with its Monte Carlo standard error, and every estimate from data comes with an interval.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Describe and plot | Histograms, ECDFs and robust summaries for IMD rainfall and synthetic latencies; reproduce Anscombe's quartet and the Datasaurus Dozen | Notebook with a one-paragraph lesson per dataset | 3 h |
| 2 · Monte Carlo | Five probabilities with error bars; birthday collisions for 32-bit hashes; Monty Hall and the variant with a host who does not know | Prediction, simulation and exact answer side by side | 3 h |
| 3 · Bayes and spam | A base-rate simulation with 10,000 imaginary people; naive Bayes on the UCI SMS Spam Collection | Classifier, confusion matrix, precision and recall, one false positive explained | 4 h |
| 4 · Discrete models | Fit a Poisson to synthetic request logs that hide a traffic burst; binomial counts of failed payments | Fit, a chi-square goodness-of-fit test, and where the model breaks | 4 h |
| 5 · Continuous models and tails | Exponential waiting times, normal QQ plots, a log-normal latency fit with a p99 prediction | Notebook with plots and the predicted vs observed p99 | 3 h |
| 6 · Correlation and Simpson | Build a dataset that reverses when combined; find the confounder | Dataset, plots and a plain-English explanation | 3 h |
| 7 · CLT studio | Sampling distributions for four distributions and several n; the Cauchy failure | Plots and a one-page explanation | 4 h |
| 8 · Coverage and bootstrap | Coverage of t, Wald, Wilson and bootstrap-percentile intervals across n and p | A coverage table with interpretation | 4 h |
| 9 · Tests and corrections | t-test vs permutation test; power curves; 20 null tests with Bonferroni and Benjamini–Hochberg | Notebook with false-positive counts before and after correction | 4 h |
| 10 · A/A tests and peeking | 10,000 simulated A/A experiments with and without daily peeking; an SRM check | A report of false-positive rates and SRM detection rates | 4 h |

## Projects

### P1 · Simulation casebook (L1, ~6 hours)

**Real-world inspiration.** Engineers use Monte Carlo simulation when formulas get hard, from risk estimates to hash-collision budgets. The problem style follows Harvard Stat 110 and Stanford CS109.

**What to build.** A small Python package with eight classic problems, each solved exactly and by simulation:
1. the birthday problem;
2. Monty Hall, plus the version where the host does not know;
3. the coupon collector;
4. gambler's ruin;
5. two heads in a row;
6. Buffon's needle;
7. the hat-check problem (derangements);
8. collision probability for random 32-bit keys.

**Acceptance criteria**
- Every simulated estimate is within 3 standard errors of the exact answer, and the standard error is reported.
- It is reproducible with fixed seeds and runs end to end in under 60 seconds.
- Exact answers are derived on paper and computed in code with `fractions` or SymPy where possible.
- `pytest` checks each exact formula against brute-force enumeration for small n.
- A prediction log records your guess for every problem before you simulated it.

**Stretch goals.** A log-log plot of error against the number of runs showing slope −½; antithetic variates to reduce variance for one problem.

**What it proves to an employer.** You can model uncertainty and check your own reasoning by computation instead of trusting intuition, or an assistant.

### P2 · Monsoon rainfall: an honest statistical report (L2, ~15 hours)

**Real-world inspiration.** The India Meteorological Department's [sub-divisional monthly rainfall, 1901–2017](https://data.gov.in/catalog/rainfall-india), published on India's Open Government Data platform, is the kind of data behind public debate about the monsoon. This project tests whether you can analyse it without overclaiming.

**What to build.** A reproducible notebook and a 4-page report covering:
- descriptive statistics and plots for at least 10 sub-divisions;
- the distribution of annual totals, with QQ plots;
- a comparison of two 50-year periods using Welch's t-test, a permutation test, and bootstrap intervals for the difference in means and medians;
- correlations between neighbouring sub-divisions;
- a least-squares trend with a bootstrap interval for the slope;
- a multiple-comparison correction across sub-divisions.

**Acceptance criteria**
- Every reported number has an interval, and every test lists its assumptions and how they were checked. That includes a lag-1 autocorrelation check and an honest note on what autocorrelation does to the p-values.
- Permutation and t-test p-values are reported side by side, and any disagreement is explained.
- Benjamini–Hochberg is applied across all sub-divisions tested, and the adjusted results are reported.
- One command regenerates every figure and number from the raw CSV.
- A limitations section lists at least five specific points (for example: changes in station coverage, autocorrelation, choice of periods, the number of analyses tried).
- Another learner reproduces all your numbers exactly from your repository.

**Stretch goals.** A block bootstrap for autocorrelated data; a Bayesian estimate of the period difference, compared with the frequentist one.

**What it proves to an employer.** You can analyse real public data, quantify uncertainty and state limits, which matters more than any single test.

### P3 · A/B testing toolkit and experiment readout (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Swiggy's [experimentation platform](https://medium.com/swiggy-bytes/experimentation-platform-xp-at-swiggy-part-2-90f4c3953b08) builds sample-size calculators, ramp-ups and SRM checks into its workflow. [GrowthBook](https://github.com/growthbook/growthbook) is an open-source experimentation platform. Evan Miller's [calculator](https://www.evanmiller.org/ab-testing/sample-size.html) and Kohavi, Tang and Xu's book set the practice standard.

**What to build.**
- **The `abkit` library** includes:
  - a sample-size and duration calculator for proportions and means;
  - a two-proportion z-test, Welch's t-test and bootstrap intervals;
  - a Bayesian beta-binomial analysis with P(B > A) and expected loss;
  - an SRM chi-square check, a peeking simulator and an A/A harness;
  - a CLI, documentation and tests.
- **A full experiment design and readout** for an illustrative food-delivery checkout change, using synthetic data with a planted true effect.

**Acceptance criteria**
- **Calibration.** Across 10,000 simulated A/A tests at α = 0.05, the false-positive rate is 5% ± 0.5 percentage points.
- **Power.** At the sample size your calculator returns, simulated power is within ±2 percentage points of the 80% target in three scenarios.
- **Agreement.**
  - Test statistics and p-values match `scipy.stats` or statsmodels to 1e-8.
  - Sample sizes match Evan Miller's calculator within 2% for five documented inputs, or each difference is traced to the choice of formula.
- **SRM detection.**
  - The check flags a 50.5/49.5 split at n = 1,000,000 with p < 0.001.
  - At α = 0.001 it raises no flag in at least 99% of simulated fair splits.
- **Peeking.** The simulator reports the false-positive rate with daily peeking over 14 days against a fixed horizon, and the result appears in the readout.
- **Readout.** The 95% interval covers the planted effect. A decision memo of at most 2 pages states the effect, the interval, the guardrail metrics, the risks and the decision.
- **Engineering.** At least 90% test coverage, type hints, CI, and a worked example in the documentation.

**Stretch goals.** CUPED variance reduction using pre-experiment data; an always-valid sequential test; a switchback simulation for marketplace interference.

**What it proves to an employer.** You can be trusted with decisions that move revenue. You can size an experiment, catch a broken one, and explain the result to people who are not statisticians.

## Feeds into

- [CS206 Mathematics for Machine Learning](../../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md) and [CS214 Machine Learning Foundations](../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md): likelihood, Bayes and estimation continue into ML.
- [DAN302 Business Statistics and Experimentation](../../../03_majors/data_analysis/year_3/DAN302_business_statistics_and_experimentation/README.md) and [DSC304 Experimental Design and Causal Inference](../../../03_majors/data_science/year_3/DSC304_experimental_design_and_causal_inference/README.md) extend P3.
- [DSC301 Statistical Inference and Modeling](../../../03_majors/data_science/year_3/DSC301_statistical_inference_and_modeling/README.md) extends Chapters 8–10.
- [FND115 Databases I](../FND115_databases_i_data_modeling_and_sql/README.md): the experiment data in P3 is usually pulled with the SQL from that course.
