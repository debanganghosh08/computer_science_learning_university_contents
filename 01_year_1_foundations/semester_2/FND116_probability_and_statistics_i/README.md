# FND116 · Probability and Statistics I

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 1 · 2 | 4 (≈ 120 hours) | L0 → L2 | [FND103](../../semester_1/FND103_discrete_mathematics_for_computing/README.md) | [CS206](../../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md), [DAN301](../../../03_majors/data_analysis/year_3/DAN301_spreadsheets_to_sql_analytical_querying_in_depth/README.md), [DAN302](../../../03_majors/data_analysis/year_3/DAN302_business_statistics_and_experimentation/README.md), [DSC301](../../../03_majors/data_science/year_3/DSC301_statistical_inference_and_modeling/README.md), [DSC304](../../../03_majors/data_science/year_3/DSC304_experimental_design_and_causal_inference/README.md) |

## Why this course matters now

Software teams decide with data: whether a feature ships depends on an A/B test, an SRE alert fires on p99 latency, a fraud model trades false alarms against missed fraud, and every ML model outputs probabilities. Swiggy, for example, has described an in-house experimentation platform with built-in sample-size calculators, gradual ramp-ups and sample-ratio-mismatch checks. AI assistants and AutoML tools will run any test you ask for and write a confident summary. The 2016 American Statistical Association statement exists because people misread the p-values such tools print. What still needs a skilled human is choosing the right question, the right design and the right comparison, and noticing when a "significant" result is an artefact of peeking, bias or chance. This course teaches probability and statistics simulation-first, in Python, so you can check every formula by experiment.

## Learning outcomes

By the end you can:

1. Describe a dataset honestly with plots and robust summaries, and explain why the mean misleads on skewed data such as latencies or incomes.
2. Compute probabilities with counting, conditioning, independence and Bayes' theorem, and confirm each answer by Monte Carlo simulation with a stated error.
3. Model situations with the Bernoulli, binomial, geometric, Poisson, uniform, exponential, normal and log-normal distributions, and justify each choice.
4. Use expectation and variance, including linearity of expectation with indicator variables, to analyse algorithms and systems.
5. Demonstrate the law of large numbers and the central limit theorem by simulation, including a case where the CLT fails.
6. Design samples and spot bias (selection, survivorship, non-response) in real studies, including a national survey.
7. Build and interpret confidence intervals, including bootstrap intervals, and check their coverage by simulation.
8. Run and interpret hypothesis tests (t, chi-square, permutation), compute power and sample size, and correct for multiple comparisons.
9. Design, size and analyse an A/B test, detect peeking and sample ratio mismatch, and compare frequentist and Bayesian readouts.

## Chapters and lessons

### Chapter 1 · Describing data (week 1)

| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Distributions of data | Categorical vs numeric; histograms, bin choice, empirical CDFs | Histogram and ECDF of monthly rainfall for one IMD sub-division (data.gov.in) |
| 1.2 Centre and spread | Mean, median, mode, variance, standard deviation, quantiles, IQR; robust statistics | Show one outlier moving the mean but not the median |
| 1.3 Skew and tails | p50, p95 and p99; log scales; why "average latency" hides pain | Generate log-normal latencies and report what the mean conceals |
| 1.4 Always plot | Anscombe's quartet and the Datasaurus Dozen: same summary statistics, different data | Reproduce both and write the lesson in one sentence |

**Check your understanding:** (1) Why do SRE teams set targets on p99 rather than on the mean? (2) When is the median the wrong summary? (3) What can a histogram hide that an ECDF shows?

### Chapter 2 · Probability and simulation (week 2)

| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Events and axioms | Sample spaces, the Kolmogorov axioms, complements, inclusion–exclusion | P(at least one six in four rolls) by complement and by simulation |
| 2.2 Counting and collisions | Permutations and combinations from [FND103](../../semester_1/FND103_discrete_mathematics_for_computing/README.md); the birthday problem | Birthday problem by formula and simulation; apply it to hash collisions in [FND112](../FND112_data_structures_and_algorithms_i/README.md) |
| 2.3 Monte Carlo | NumPy's `Generator`, seeds, Monte Carlo error shrinking like 1/√n | Estimate five probabilities, each with an error bar |
| 2.4 Intuition traps | Monty Hall, the gambler's fallacy, the hot-hand debate | Simulate Monty Hall 10⁵ times, then a variant where the host opens a door at random |

**Check your understanding:** (1) How many simulation runs do you need for ±0.001 precision on a probability near 0.5? (2) Why does the Monty Hall answer change when the host does not know where the car is? (3) Why does a 64-bit hash still collide sooner than most people expect?

### Chapter 3 · Conditional probability and Bayes (week 3)

| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Conditioning | Conditional probability, the multiplication rule, the law of total probability, tree diagrams | A two-stage delivery-delay tree (illustrative) |
| 3.2 Bayes' theorem | Base rates; P(A given B) is not P(B given A); medical tests and fraud alerts | A 99%-accurate test at 1% prevalence, computed and simulated with 10,000 imaginary people |
| 3.3 Naive Bayes | Spam filtering as Bayesian updating (Graham, 2002); the independence assumption | Build a classifier on the UCI SMS Spam Collection; report precision and recall |
| 3.4 When independence fails | Correlated evidence and double counting | Add duplicated features and watch the classifier become overconfident |

**Check your understanding:** (1) Why does a very accurate test still give mostly false positives for a rare condition? (2) What does "naive" assume, and why does it often work anyway? (3) Give an everyday example of confusing P(A given B) with P(B given A).

### Chapter 4 · Discrete random variables (week 4)

| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Expectation and variance | PMF and CDF; E[X] and Var(X); linearity of expectation with indicators, even without independence | Expected number of people who get their own hat back, derived and simulated |
| 4.2 Bernoulli, binomial, geometric | Successes in n trials; tries until the first success | P(at least 3 failed payments in 100) for a given failure rate |
| 4.3 Poisson | Counts of rare events per interval; Poisson as a limit of the binomial | Model requests per second; compare with synthetic logs |
| 4.4 Expectation in computing | Expected comparisons in randomised quicksort; the coupon collector | Simulate the coupon collector against n·Hₙ |

**Check your understanding:** (1) Why does linearity of expectation not need independence? (2) When is the Poisson a poor model for request counts? (3) Why is randomised quicksort's expected time a statement about the algorithm's coins, not about the input?

### Chapter 5 · Continuous random variables (week 5)

| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Densities | PDF, CDF, uniform; probabilities as areas (integrals from [FND113](../FND113_linear_algebra_and_calculus_for_computing/README.md)) | P(a < X < b) by integration and by simulation |
| 5.2 Exponential | Memorylessness; the link to Poisson arrivals | Check memorylessness empirically on simulated waiting times |
| 5.3 Normal | Standardisation, z-scores, the 68–95–99.7 rule, QQ plots | Test which of three datasets is plausibly normal |
| 5.4 Log-normal and heavy tails | Multiplicative processes; tail percentiles | Fit a log-normal to latency data and predict p99 |

**Check your understanding:** (1) Why is P(X = 2.0) zero for a continuous variable, and why is that fine? (2) What does memorylessness mean for a server's time to next request? (3) Why do heavy tails break intuition built on the normal distribution?

### Chapter 6 · Joint distributions and correlation (week 6)

| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Joint and marginal | Joint tables, marginals, independence tests by eye | A joint table of payment method by success |
| 6.2 Covariance and correlation | Correlation is not causation; confounders; spurious correlation | Find the confounder in a synthetic dataset |
| 6.3 Simpson's paradox | The 1973 Berkeley admissions data (Bickel et al., 1975) | Build a dataset in which every subgroup trend reverses when combined |
| 6.4 Variance of sums | Var(X + Y) with covariance; diversification | Variance of a two-asset portfolio by formula and simulation (illustrative) |

**Check your understanding:** (1) How can a treatment look better in every subgroup and worse overall? (2) Why can zero correlation coexist with strong dependence? (3) When does adding a second, correlated server not halve your risk?

### Chapter 7 · The law of large numbers and the CLT (weeks 7–8)

| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Law of large numbers | Running averages converge; what "converge" means | Running-mean plots for five distributions |
| 7.2 Sampling distributions | Standard error, σ/√n | Sample means of size n from a skewed population |
| 7.3 The central limit theorem | When it works and how fast; where it fails | CLT for exponential and Bernoulli(0.01), and its failure for the Cauchy |
| 7.4 Normal approximations | The binomial approximation and the continuity correction | Exact vs approximate probabilities for n = 20 and n = 100 |

**Check your understanding:** (1) Why does the CLT need far more samples for Bernoulli(0.01) than for Bernoulli(0.5)? (2) What property of the Cauchy breaks the CLT? (3) Why does quadrupling the sample size only halve the standard error?

### Chapter 8 · Sampling and estimation (weeks 8–9)

| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Sampling designs | Simple random, stratified, cluster and systematic samples; sampling frames | Simulate the precision of stratified vs simple random sampling |
| 8.2 A national survey | MoSPI's Periodic Labour Force Survey: first-stage units, rotational panels in urban areas | Summarise the 2023–24 PLFS design in one page |
| 8.3 Bias | Selection, survivorship, non-response and measurement bias | Find the bias in five described studies (illustrative) |
| 8.4 Estimators | Unbiasedness, variance, mean squared error; why n − 1; maximum likelihood, intuitively | Show the n vs n − 1 bias by simulation; MLE for Bernoulli and Poisson |

**Check your understanding:** (1) Why does stratifying by state usually improve a national estimate? (2) What survivorship bias hides in "successful startups all did X"? (3) Why is the n − 1 correction needed?

### Chapter 9 · Confidence intervals and the bootstrap (week 10)

| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Intervals for a mean | z and t intervals; what "95%" means (coverage) | Draw 1,000 samples, build 1,000 intervals, count how many cover the truth |
| 9.2 Intervals for a proportion | Wald vs Wilson intervals at small n or extreme p | Coverage of both at p = 0.02 |
| 9.3 The bootstrap | Resampling (Efron, 1979); percentile intervals; `scipy.stats.bootstrap` | A bootstrap interval for median latency |
| 9.4 Reporting uncertainty | Error bars, effect sizes, sensible precision | Rewrite three overconfident claims with intervals |

**Check your understanding:** (1) Why is "there is a 95% chance the true value is in this interval" a misreading? (2) When does the Wald interval fail badly? (3) What does the bootstrap assume about your sample?

### Chapter 10 · Hypothesis testing (weeks 11–12)

| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The logic | Null and alternative, test statistic, p-value, α, type I and II errors | A permutation test for a difference in means, written from scratch |
| 10.2 Common tests | Welch's t-test, chi-square tests, permutation tests; their assumptions | Run a t-test and a permutation test on the same data and compare |
| 10.3 Power and sample size | Effect size, power curves, simulation vs formula | Power curves for three effect sizes |
| 10.4 Misuse and repair | The ASA statement (2016); p-hacking; multiple comparisons, Bonferroni and Benjamini–Hochberg (`scipy.stats.false_discovery_control`) | Run 20 tests where the null is true; count false positives; fix with a correction |

**Check your understanding:** (1) What does a p-value of 0.03 mean, and what does it not mean? (2) Why does a non-significant result not prove "no effect"? (3) How many false positives do you expect from 100 null tests at α = 0.05?

### Chapter 11 · A/B testing and Bayesian thinking (weeks 13–14)

| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Designing an experiment | Randomisation unit, primary and guardrail metrics, a written hypothesis; Swiggy's platform as a case study | A one-page design for an illustrative checkout change |
| 11.2 Sample size and duration | Minimum detectable effect, power, traffic, full weekly cycles, ramp-ups | Compute with Evan Miller's calculator and confirm by simulation |
| 11.3 Pitfalls | Peeking (repeated significance testing inflates false positives), sample ratio mismatch, novelty effects, interference and switchback designs, Twyman's law | Simulate peeking; implement a chi-square SRM check |
| 11.4 Bayesian A/B | Beta-binomial posteriors; P(B > A) by simulation; credible vs confidence intervals | Analyse one dataset both ways and explain any disagreement |
| 11.5 Honest readouts | Effect size with interval, the decision, the risks | Write a readout a product manager can act on |

**Check your understanding:** (1) Why does stopping as soon as p < 0.05 raise the false-positive rate? (2) What does a 50/50 test that receives 52/48 traffic tell you? (3) When would you randomise by city or time slot instead of by user?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Describe and plot | Rainfall and latency summaries |
| 2 | 2 | Lab 2 · Monte Carlo | Five estimates with error bars; paper quiz 1 |
| 3 | 3 | Lab 3 · Bayes and spam | Classifier with precision and recall; P1 starts |
| 4 | 4 | Lab 4 · Discrete models | Poisson fit to logs |
| 5 | 5 | Lab 5 · Continuous models and tails | Log-normal p99 prediction; P1 due |
| 6 | 6 | Lab 6 · Correlation and Simpson | Reversal dataset |
| 7–8 | 7 | Lab 7 · CLT studio | CLT successes and failure; P2 starts |
| 8–9 | 8 | Sampling simulation and PLFS summary | One-page design summary |
| 10 | 9 | Lab 8 · Coverage and bootstrap | Coverage table |
| 11–12 | 10 | Lab 9 · Tests and corrections | Power curves; P2 due; P3 starts |
| 13–14 | 11 | Lab 10 · A/A tests and peeking | Simulation report |
| 15 | Review and exam | Written exam (AI off) and P3 demo | P3 due |

Every week also has a 30-minute paper quiz, done without AI.

## Working with AI in this course

- **Use AI for:** scaffolding simulation code; explaining a test's assumptions; suggesting a test, then checking it against your own decision table; generating synthetic datasets with stated properties; drafting a readout that you then fact-check line by line.
- **Do without AI (drills):** the weekly paper quiz covers Bayes with base rates, expectations with indicators, normal approximations, and reading p-values and intervals. Before every simulation, write your predicted answer.
- **Verify AI output by:** simulating every probability claim and reporting Monte Carlo error; cross-checking each test with `scipy.stats` and a permutation test; a coverage simulation for any interval method; A/A tests for any experiment pipeline; writing down each assumption (independence, sample size, distribution) and checking it.
- **Where AI still fails here:** the GSM-Symbolic study showed language-model accuracy falling when only the numbers changed or an irrelevant detail was added, which is exactly how probability puzzles are varied. Check generated answers for:
  - the famous answer given to a modified puzzle, such as Monty Hall with a host who does not know;
  - P(A given B) swapped with P(B given A);
  - p-values described as the probability that the null hypothesis is true;
  - analyses that ignore peeking or multiple testing.

  Let your simulations decide, and log every disagreement.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Weekly paper quizzes, AI off | 15% |
| Labs (10) | 20% |
| Projects P1 · P2 · P3 | 8% · 12% · 15% |
| Final exam: 2 hours written (AI off) plus 1 hour computational | 30% |

**Mastery gate.** You pass when you can, without AI:
- solve a base-rate Bayes problem and explain it with a tree;
- derive an expectation with indicator variables;
- compute and interpret a 95% confidence interval and a two-sample test;
- write Python simulations that confirm each answer within its Monte Carlo error.

You must also design an A/B test for a described feature (metric, sample size, duration, stopping rule and SRM check) and defend it under questioning.

## Industry reality

Online controlled experiments are standard practice at large technology companies, and the standard reference, by Kohavi, Tang and Xu (2020), was written by practitioners from Microsoft, Google and LinkedIn. In India, Swiggy has described experimentation infrastructure with sample-size and duration calculators, ramp-ups from 5% of users, SRM checks, and switchback and difference-in-differences designs for cases where users interact. National statistics depend on sampling design: the 2023–24 PLFS surveyed 1,01,920 households across 12,743 first-stage units. Paul Graham's 2002 Bayesian filter missed fewer than 5 in 1,000 spam messages with zero false positives on his own email. Data analyst, data scientist, ML and quantitative interviews test this material, usually as worked problems.

**Interview questions from this course**

1. *"Explain a p-value to a product manager. What is it not?"* The probability of data at least this extreme if the null were true; not the probability that the null is true; not an effect size; pair it with an interval and a decision; the ASA principles.
2. *"You checked an A/B test every day and stopped when p < 0.05. Do you trust the result?"* Peeking inflates false positives; use a fixed horizon or a sequential method; run A/A tests; check SRM and novelty effects.
3. *"A test is 99% sensitive and 99% specific; prevalence is 1%. What is P(disease given positive)?"* About 50%, shown with 10,000 people in a tree; why base rates dominate; what this means for fraud alerts.
4. *"What is the expected number of coin flips to get two heads in a row?"* First-step analysis gives 6; verify by simulation; generalise to k heads.
5. *"How do you choose the sample size for an experiment?"* Baseline rate, minimum detectable effect, α, power and variance; a formula or a simulation; converting to duration with traffic; covering full weekly cycles; ramp-up.

## Resources (free first)

- **Courses:** [Harvard Stat 110 lectures](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) and [edX version](https://www.edx.org/learn/probability/harvard-university-introduction-to-probability) (the Blitzstein–Hwang book is free to read online); [MIT 18.05 Introduction to Probability and Statistics](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/); [Berkeley Data 8](https://www.data8.org/) with its textbook [*Computational and Inferential Thinking*](https://inferentialthinking.com/); [Stanford CS109 course reader](https://chrispiech.github.io/probabilityForComputerScientists/en/); [NPTEL Introduction to Probability and Statistics](https://nptel.ac.in/courses/111106112) (IIT Madras).
- **Free books and visuals:** [OpenIntro Statistics](https://www.openintro.org/book/os/); [Think Stats, 3rd ed.](https://allendowney.github.io/ThinkStats/); [Think Bayes 2](https://allendowney.github.io/ThinkBayes2/); [Seeing Theory](https://seeing-theory.brown.edu/).
- **Experimentation:** Evan Miller, [How Not To Run an A/B Test](https://www.evanmiller.org/how-not-to-run-an-ab-test.html) and his [sample size calculator](https://www.evanmiller.org/ab-testing/sample-size.html); [GrowthBook docs](https://docs.growthbook.io/) (an open-source experimentation platform); [Swiggy Bytes: Experimentation Platform, Part 2](https://medium.com/swiggy-bytes/experimentation-platform-xp-at-swiggy-part-2-90f4c3953b08).
- **Tools:** [`scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html) (including [`bootstrap`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html) and [`permutation_test`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.permutation_test.html)); [statsmodels](https://www.statsmodels.org/stable/stats.html); [NumPy random `Generator`](https://numpy.org/doc/stable/reference/random/generator.html).
- **Datasets:** [IMD rainfall, data.gov.in](https://data.gov.in/catalog/rainfall-india); [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection); [Datasaurus Dozen](https://www.research.autodesk.com/publications/same-stats-different-graphs/).
- **Paid, optional:** Kohavi, Tang and Xu, [*Trustworthy Online Controlled Experiments*](https://experimentguide.com/) (Cambridge, 2020), the standard industry reference.

## Sources

All checked 12 Oct 2026.

- Swiggy Bytes, "Experimentation Platform (XP) at Swiggy — Part 2" (17 Nov 2021) — https://medium.com/swiggy-bytes/experimentation-platform-xp-at-swiggy-part-2-90f4c3953b08
- Wasserstein and Lazar, "The ASA Statement on p-Values" (2016), doi:10.1080/00031305.2016.1154108 · ASA release — https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
- Bickel, Hammel and O'Connell, "Sex Bias in Graduate Admissions: Data from Berkeley", *Science* 187 (1975), doi:10.1126/science.187.4175.398
- Efron, "Bootstrap Methods: Another Look at the Jackknife", *Annals of Statistics* 7(1) (1979) — https://projecteuclid.org/journals/annals-of-statistics/volume-7/issue-1/Bootstrap-Methods-Another-Look-at-the-Jackknife/10.1214/aos/1176344552.full
- Paul Graham, "A Plan for Spam" (Aug 2002) — https://www.paulgraham.com/spam.html
- Evan Miller, "How Not To Run an A/B Test" (2010) — https://www.evanmiller.org/how-not-to-run-an-ab-test.html
- Kohavi, Tang and Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020), doi:10.1017/9781108653985 — https://www.cambridge.org/core/product/identifier/9781108653985/type/book
- MoSPI, PLFS Annual Report 2023–24 (Sep 2024) — https://www.mospi.gov.in/sites/default/files/publication_reports/AnnualReport_PLFS2023-24L2.pdf
- Matejka and Fitzmaurice, "Same Stats, Different Graphs" (CHI 2017) — https://www.research.autodesk.com/publications/same-stats-different-graphs/
- Mirzadeh et al., "GSM-Symbolic" (arXiv 2410.05229) — https://arxiv.org/abs/2410.05229
- SciPy 1.18 statistics reference — https://docs.scipy.org/doc/scipy/reference/stats.html

_Last reviewed: 2026-10_
