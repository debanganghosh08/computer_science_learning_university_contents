# DAN403 · Domain Analytics: Finance, Marketing, Operations and Healthcare

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L2 → L4 | [DAN303](../../year_3/DAN303_data_visualization_and_storytelling/README.md) | [DAN501](../../year_5/DAN501_frontier_seminar_decision_intelligence/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

Part of the [Data Analysis major](../../README.md). Draws on every Year 3 course: SQL from [DAN301](../../year_3/DAN301_spreadsheets_to_sql_analytical_querying_in_depth/README.md), experiments from [DAN302](../../year_3/DAN302_business_statistics_and_experimentation/README.md), metrics and unit economics from [DAN305](../../year_3/DAN305_product_and_business_analytics_metrics_funnels/README.md), and forecasting from [DAN402](../DAN402_forecasting_for_business_decisions/README.md) where taken. Fraud-detection modelling is covered in [OV10B](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10B_fraud_detection_and_risk_systems/README.md); this course is about the analyst's view of each domain: its processes, metrics, data quirks and decisions.

## Why this course matters now

SQL and charts are now cheap: an AI assistant produces both on request. What an assistant does not have is the domain context that makes a number mean something. It does not know that revenue is recognised differently from cash collected, that a loan cohort's delinquency is not visible for months, or that last-click attribution credits the channel that happened to be last. It does not know that a delivery time includes food preparation the platform does not control, or that a health indicator from a survey is an estimate with a sampling design behind it. Tools in these domains are changing too. Google Analytics 4 retired its first-click, linear, time-decay and position-based attribution models in November 2023. Google open-sourced Meridian, a Bayesian marketing mix model that can be calibrated with experiments. India released NFHS-6 (2023–24) fact sheets in 2026. NPCI introduced a merchant fee on UPI payments above ₹2,000 from 15 October 2026. Analysts who understand a domain's mechanics ask better questions, catch errors an AI cannot see, and move into strategy, finance and operations roles. This course teaches four domains in depth and a method for learning any new one quickly.

## Learning outcomes

By the end you can:

1. **Learn** a new domain fast: build its glossary, process map, metric tree and data map, and **identify** where its data misleads.
2. **Read and analyse** financial statements and management accounts: P&L, balance sheet, cash flow, variance analysis, working capital and cohort revenue. **Explain** accrual vs cash.
3. **Analyse** lending and payments businesses with vintage curves, roll rates, expected loss and payment success funnels.
4. **Measure** marketing honestly: **contrast** attribution with incrementality, **design** a geo or holdout test, and **fit and calibrate** a marketing mix model.
5. **Segment** customers and **target** campaigns with uplift thinking rather than response rates alone.
6. **Diagnose** operations with Little's law, queueing intuition, OTIF and inventory metrics, delivery-time decomposition, geospatial aggregation and process mining.
7. **Analyse** health and public data correctly: rates, age standardisation, survey estimates, small numbers and re-identification risk.
8. **Deliver** a domain-grade analysis that a finance head, marketing head, operations head or health official would accept as competent.

## Chapters and lessons

### Chapter 1 · Learning a domain fast (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The domain map | Glossary, core processes, money flows, regulators, key reports, decision calendar | Build a one-page map of an unfamiliar domain (insurance or telecom) in 3 hours |
| 1.2 Where data lies | Each domain's traps: accruals, censoring, attribution, survey weights, coding changes | List 3 traps per domain from published sources |
| 1.3 Talking to experts | Interviewing finance, marketing, operations and clinical staff; questions that reveal process | Run and write up a 20-minute expert interview |
| 1.4 Domain AI assistants | Using AI to build glossaries and process maps, then checking them against primary sources | Fact-check an AI-generated glossary of 30 terms |

**Check your understanding:** Why does a correct SQL query on a domain you do not understand still produce wrong conclusions? What is the fastest way to find a domain's decision calendar? Which AI-generated glossary errors are the most dangerous?

### Chapter 2 · Financial statements and FP&A analytics (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 The three statements | P&L, balance sheet, cash flow and how they link; accrual vs cash; revenue recognition (Ind AS 115 / IFRS 15) | Trace one sale through all three statements |
| 2.2 Reading real filings | Indian annual reports and quarterly results (BSE filings), shareholder letters; SEC financial statement data sets (XBRL) for global comparisons | Extract 5 years of statements for 2 companies into tidy tables |
| 2.3 Adjusted metrics | EBITDA, adjusted EBITDA and other non-GAAP measures; reconciling to reported profit | Reconcile one company's adjusted EBITDA to net profit |
| 2.4 Variance analysis | Budget vs actual, price–volume–mix, flexed budgets, explaining variances in a monthly pack | A variance bridge for an illustrative business unit |
| 2.5 Working capital and cash | DSO, DPO, DIO, cash conversion cycle; month-end and quarter-end effects | Cash conversion cycle for 3 listed retailers |
| 2.6 Revenue cohorts | ARR waterfalls, net revenue retention, cohort revenue for subscription and repeat-purchase businesses | Cohort revenue table and NRR from a transaction log |

**Check your understanding:** How can a company report rising profit and falling cash? Why must an adjusted metric always be shown with its reconciliation? Why does a flexed budget give a fairer variance than a static one?

### Chapter 3 · Lending and payments analytics (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 The credit funnel | Applications, approvals, disbursals, activation; approval-rate vs risk trade-off | Funnel and approval analysis on the Home Credit dataset |
| 3.2 Vintage analysis | Delinquency (30+, 90+ days past due) by origination cohort and months on book; why recent cohorts look good | Vintage curves from the Freddie Mac loan-level dataset |
| 3.3 Roll rates and expected loss | Transition matrices between delinquency buckets; expected loss = PD × LGD × EAD (Basel concepts) | Roll-rate matrix and expected-loss estimate for a portfolio |
| 3.4 Payments | Success-rate funnels by method and bank, failure reason codes, settlement times, MDR economics including the October 2026 UPI change | Payment-cost model by ticket-size band |
| 3.5 Fraud and risk monitoring | Alert precision and false positives, review capacity, loss rates; the analyst's role vs the modeller's | Choose an alert threshold from review capacity and loss data (illustrative) |

**Check your understanding:** Why can a lender's portfolio look healthiest just as it is growing fastest? What does a roll rate tell you that a delinquency rate does not? Why does a fraud alert threshold depend on reviewer capacity?

### Chapter 4 · Attribution and digital measurement (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Tracking marketing | UTM parameters, click IDs, channel grouping, consent and data loss (Apple's App Tracking Transparency, 2021) | Audit UTM hygiene in a provided campaign log |
| 4.2 Attribution models | Last click, first click, rules-based, data-driven attribution; GA4's current options after the November 2023 retirements | Compare channel credit under 4 rules on the Criteo attribution dataset |
| 4.3 What attribution cannot tell you | Correlation of touchpoints with conversion vs causal contribution; brand search capture | Show a channel with high attributed and zero incremental value (simulated) |
| 4.4 CAC by channel | Blended vs channel CAC, attribution choices, payback by channel (from DAN305) | Channel CAC table with stated attribution assumptions |

**Check your understanding:** Why does last-click attribution over-credit branded search? What changed for marketers when user-level tracking declined? Why can no attribution model, however sophisticated, prove a channel works?

### Chapter 5 · Incrementality and marketing mix modelling (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Lift tests | Holdouts, geo experiments with matched markets, conversion lift; power for geo tests | Design a geo test across Indian cities with matched pairs |
| 5.2 MMM concepts | Weekly aggregated data, adstock (carry-over), saturation curves, baseline, control variables | Fit a simple MMM by regression on simulated data with known truth |
| 5.3 Bayesian MMM | Google Meridian (Apache 2.0; geo-level data, reach and frequency, calibration with experiments), Meta Robyn, PyMC-Marketing | Fit Meridian or PyMC-Marketing on a sample dataset |
| 5.4 Calibration and validation | Priors from lift tests, holdout periods, parameter recovery on simulated data | Show how calibration changes channel ROI estimates |
| 5.5 Budget decisions | Response curves, marginal ROI, budget reallocation with uncertainty | A reallocation recommendation with ranges |

**Check your understanding:** Why does an MMM need years of weekly data, and what happens with less? Why calibrate an MMM with experiments? What does a marginal ROI tell you that an average ROI hides?

### Chapter 6 · Customer analytics: segmentation, churn and targeting (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Segmentation | RFM, behavioural clusters, needs-based segments; segments that drive action | RFM segments on Online Retail II with an action per segment |
| 6.2 Churn analytics | Churn definitions, survival curves, early-warning indicators | Kaplan–Meier retention curves by acquisition channel |
| 6.3 Uplift and targeting | Response vs uplift; four customer types (persuadable, sure thing, lost cause, do-not-disturb) | Uplift analysis on the Hillstrom or Criteo uplift data |
| 6.4 Consent and fairness | Marketing consent under DPDP; excluding vulnerable groups; frequency caps | Review a campaign plan for consent and fairness issues |

**Check your understanding:** Why can targeting the customers most likely to buy waste the budget? What does a survival curve show that a churn rate does not? Which campaign data uses need fresh consent under DPDP?

### Chapter 7 · Operations and supply chain analytics (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Flow fundamentals | Throughput, cycle time, work in progress, Little's law (L = λW), utilisation and queues | Use Little's law to find the bottleneck in an illustrative warehouse |
| 7.2 Service metrics | OTIF, fill rate, order cycle time, perfect order; defining each precisely | Compute OTIF for Olist orders under two definitions |
| 7.3 Inventory | Inventory turns, days of cover, ABC–XYZ classification, safety stock (from DAN402), dead stock | ABC–XYZ for M5 items; a stock policy per class |
| 7.4 The bullwhip effect | Order variability amplifying upstream; information sharing | Simulate a 3-tier supply chain; measure amplification |
| 7.5 E-commerce logistics in India | Cash on delivery, return-to-origin (RTO), pincode serviceability, delivery attempts | An RTO analysis on illustrative order data |

**Check your understanding:** If average queue length doubles at the same arrival rate, what happened to waiting time? Why can fill rate be high while OTIF is low? What creates the bullwhip effect, and which data-sharing reduces it?

### Chapter 8 · Delivery operations, geospatial analysis and process mining (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Decomposing delivery time | Preparation, wait, pickup, travel; which parts the platform controls; Zomato's published work on food preparation time | Decompose Olist delivery times by stage and state |
| 8.2 Geospatial aggregation | Hexagonal grids (H3), catchments, density; the modifiable areal unit problem | Map NYC taxi pickups at 3 H3 resolutions; show the conclusions change |
| 8.3 Process mining | Event logs (case, activity, timestamp), process discovery, conformance checking, bottlenecks (PM4Py) | Discover the process and bottlenecks in a BPI Challenge log |
| 8.4 SLA analytics | Percentile targets, breach analysis, root causes by stage | p50/p90 delivery-time SLA breaches with stage-level causes |

**Check your understanding:** Why should a delivery-time target be set on the 90th percentile and not the mean? How can changing grid size reverse a geographic conclusion? What does process mining reveal that a funnel cannot?

### Chapter 9 · Healthcare analytics (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Health data types | Surveys (NFHS), facility reporting (HMIS), claims, registries, electronic records; what each can and cannot show | Map 6 questions to the right data source |
| 9.2 Rates and standardisation | Rates per 1,000, crude vs age-standardised rates, confidence intervals for rates | Age-standardise a mortality rate with WHO's standard population |
| 9.3 Survey estimates | NFHS sampling design, weights, standard errors; comparing NFHS-5 and NFHS-6 | Compare 5 state indicators between rounds and flag which changes are meaningful |
| 9.4 Facility data quality | Completeness, timeliness, outliers and reporting artefacts in HMIS-style data | Data-quality report on an HMIS extract |
| 9.5 Privacy and ethics | Small cells and re-identification, children's data under DPDP, ethics review | Apply small-cell suppression to a district table |

**Check your understanding:** Why can a crude death rate rise while every age group's rate falls? When is a change between two survey rounds not meaningful? Why do district-level health tables need small-cell suppression?

### Chapter 10 · Public data and policy analytics (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 India's public data | data.gov.in, NITI Aayog's NDAP, MoSPI (PLFS, CPI), RBI DBIE; licences and revisions | Build a tidy panel of 3 state indicators from 2 sources |
| 10.2 Comparing places fairly | Per-capita normalisation, ecological fallacy, population denominators between censuses | Rank states two ways and explain the difference |
| 10.3 Evaluating programmes | Before–after, difference-in-differences and their assumptions (from DAN302) | Evaluate an illustrative state programme with diff-in-diff and a placebo test |
| 10.4 Writing for policy audiences | Briefs, uncertainty language, what officials need to act | A two-page policy brief |

**Check your understanding:** Why does a state-level correlation not tell you about individuals? What happens to per-capita figures when population denominators are many years old? Which assumption of diff-in-diff would a sceptical official attack first?

### Chapter 11 · Domain sprint and AI in domain work (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 One-week domain sprint | Apply Chapter 1 to a new domain (insurance, energy, telecom or education) | Domain map, metric tree, data map and 3 traps |
| 11.2 AI with domain context | Giving assistants glossaries, definitions and rules; checking outputs against primary sources | Compare assistant answers with and without your domain pack |
| 11.3 Peer review by domain | Finance, marketing, operations and health reviewers critique each other's work | Structured peer review of P3 drafts |
| 11.4 Final presentations | Presenting to a mock domain head | P3 presentation and Q&A |

**Check your understanding:** What did your domain sprint get wrong in the first draft, and how did you find out? Which domain facts must never come from an AI without a primary source? What makes a domain head trust a newcomer's analysis?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Domain map | — |
| 2 | 2 | Lab 2 · Statements from filings | — |
| 3 | 2 | Lab 2 (cont.) · Variance and cohort revenue | **P1 due** |
| 4 | 3 | Lab 3 · Vintages and roll rates | — |
| 5 | 4 | Lab 4 · Attribution comparison | — |
| 6 | 5 | Lab 5 · MMM with known truth | Mid-term (AI off) |
| 7 | 5–6 | Lab 5 (cont.) · Calibration; uplift | — |
| 8 | 7 | Lab 6 · Flow, OTIF, ABC–XYZ | — |
| 9 | 7–8 | Lab 7 · Delivery decomposition and H3 | **P2 due** |
| 10 | 8 | Lab 8 · Process mining | — |
| 11 | 9 | Lab 9 · Health rates and survey comparisons | — |
| 12 | 10 | Lab 10 · Public panel and diff-in-diff | Policy brief |
| 13 | 11 | Domain sprint | — |
| 14 | 11 | Presentations | **P3 due** |
| 15 | Review | Domain viva | Final exam (AI off): 4 domain cases |

## Working with AI in this course

- **Use AI for:** first-draft glossaries and process maps; explaining accounting standards, attribution models or epidemiological terms (then checked against primary sources); writing MMM, vintage and process-mining code you then validate; summarising long filings, with every extracted number checked against the source page.
- **Do without AI (drills):** reading the three statements and linking them; variance bridges; vintage curve interpretation; Little's law calculations; age standardisation by hand on a small table; the mid-term and final cases.
- **Verify AI output by:**
  - tracing every financial figure to the filing page;
  - checking that attribution or MMM outputs are labelled with their assumptions;
  - reproducing one domain metric by hand;
  - testing models on simulated data where the truth is known (MMM parameter recovery, uplift with known effects).
- **Where AI still fails here:** in labs you will see assistants misread units and periods in filings (crore vs lakh, standalone vs consolidated), present attributed conversions as incremental, compare survey rounds without uncertainty, and invent "industry benchmarks". On DABstep, built from real financial-analytics tasks, the best agent solved 14.55% of hard tasks (2025). Log every error you catch with the source that disproved it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| Projects P1 · P2 · P3 | 10% · 20% · 25% |
| Mid-term (AI off) | 10% |
| Final exam (AI off): four domain cases + viva | 15% |

**Mastery gate.** You pass when you can, with AI off: (1) given a company's three statements, explain in 15 minutes why profit and cash diverged and compute its cash conversion cycle; (2) given campaign and sales data, explain why attributed and incremental results differ and design the test that settles it; (3) given a lending portfolio, read vintage curves and say which cohorts are worse and why recent ones may look better than they are; (4) given district health data, produce correctly standardised and suppressed rates with a statement of uncertainty.

## Industry reality

Domain analysts are hired by function: FP&A and finance analytics, risk and credit analytics in banks and NBFCs, marketing and growth analytics, supply-chain and operations analytics, and health and public-policy analytics in government, NGOs and consultancies. Public sources give real material: Indian listed companies' filings, RBI's DBIE, NFHS-6 fact sheets (2023–24), HMIS, and US SEC financial statement data sets. Open-source tools have become standard in marketing measurement (Meridian, Robyn, PyMC-Marketing) and process mining (PM4Py).

**Interview questions from this course**

1. *"Revenue grew 20% but cash fell. Why could that be?"* Strong answer: working capital (receivables, inventory), capital expenditure, revenue recognised before cash, debt repayment; how to check each in the cash flow statement.
2. *"Our paid social campaign shows great ROAS in the dashboard. Should we double the budget?"* Strong answer: attributed vs incremental; diminishing returns; asks for a lift test or geo test; marginal vs average ROI; MMM as a complement.
3. *"How would you check whether loan quality is getting worse?"* Strong answer: vintage curves by origination cohort at equal months on book; roll rates; mix shifts in borrowers or products; warns that fast growth hides delinquency.
4. *"Average delivery time rose 3 minutes. Diagnose."* Strong answer: decomposes into preparation, wait, pickup and travel; checks the mix (cities, restaurants, rain); uses percentiles; checks Little's law and partner utilisation.
5. *"District A's anaemia rate fell from 58% to 52% between survey rounds. Is that real?"* Strong answer: survey estimates have standard errors; checks intervals and design changes; district boundary changes; comparability of definitions; small samples.

## Resources (free first)

- **Finance:** [SEC Financial Statement Data Sets](https://www.sec.gov/data-research/sec-markets-data/financial-statement-data-sets); [BSE corporate announcements](https://www.bseindia.com/corporates/ann.html); [RBI DBIE](https://data.rbi.org.in/DBIE/); [Basel Framework](https://www.bis.org/basel_framework/).
- **Lending data:** [Freddie Mac Single-Family Loan-Level Dataset](https://www.freddiemac.com/research/datasets/sf-loanlevel-dataset) (free registration); [Home Credit Default Risk](https://www.kaggle.com/competitions/home-credit-default-risk).
- **Marketing:** [GA4 attribution models](https://support.google.com/analytics/answer/10596866); [Google Meridian](https://developers.google.com/meridian) and [repository](https://github.com/google/meridian); [Meta Robyn](https://facebookexperimental.github.io/Robyn/); [PyMC-Marketing MMM guide](https://www.pymc-marketing.io/en/stable/guide/mmm/mmm_intro.html); [Criteo attribution dataset](https://ailab.criteo.com/criteo-attribution-modeling-bidding-dataset/); [Criteo uplift dataset](https://ailab.criteo.com/criteo-uplift-prediction-dataset/).
- **Operations:** [H3 hexagonal index](https://h3geo.org/); [PM4Py](https://github.com/process-intelligence-solutions/pm4py); [BPI Challenge logs on 4TU.ResearchData](https://data.4tu.nl/search?search=BPI%20Challenge); [Zomato on food preparation time](https://www.zomato.com/blog/food-preparation-time/); [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce); [NYC TLC trip records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).
- **Health and public data:** [NFHS (IIPS)](https://www.nfhsiips.in/); [HMIS](https://hmis.mohfw.gov.in/); [NITI Aayog NDAP](https://ndap.niti.gov.in/); [MoSPI](https://www.mospi.gov.in/); [data.gov.in](https://www.data.gov.in/); [WHO Global Health Observatory](https://www.who.int/data/gho); [CMS Provider Data](https://data.cms.gov/provider-data/).
- **Finance courses:** [Aswath Damodaran's free valuation and corporate finance materials](https://pages.stern.nyu.edu/~adamodar/) (NYU Stern).
- **Paid, optional:** Douglas Hubbard, *How to Measure Anything* (Wiley).

## Sources

All checked 12 Oct 2026.

- Google Analytics Help, attribution models (first click, linear, time decay and position-based retired November 2023) — https://support.google.com/analytics/answer/10596866
- Google Meridian repository (Apache-2.0; Bayesian; reach and frequency; calibration with experiments) — https://github.com/google/meridian
- NFHS website (NFHS-6 2023–24 fact sheets; release listed 29 May 2026) — https://www.nfhsiips.in/
- NPCI, MDR on select UPI P2M transactions: FAQs (15 Sep 2026) — https://www.npci.org.in/uploads/FA_Qs_Merchant_Discount_Rate_MDR_on_Select_UPI_P2_M_Transactions_58dba1d39e.pdf
- SEC, Financial Statement Data Sets (2009 Q1–2026 Q3; updated quarterly) — https://www.sec.gov/data-research/sec-markets-data/financial-statement-data-sets
- Egg et al., DABstep (arXiv 2506.23719, 2025) — https://arxiv.org/abs/2506.23719
- PIB, DPDP Rules, 2025 notified (17 Nov 2025) — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf

_Last reviewed: 2026-10_
