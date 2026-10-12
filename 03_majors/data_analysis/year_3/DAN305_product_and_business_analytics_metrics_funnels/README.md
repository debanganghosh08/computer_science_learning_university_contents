# DAN305 · Product and Business Analytics: Metrics, Funnels and Cohorts

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L1 → L3 | [FND115](../../../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | [DAN403](../../year_4/DAN403_domain_analytics_finance_marketing_operations/README.md), [DAN402](../../year_4/DAN402_forecasting_for_business_decisions/README.md), [DAN501](../../year_5/DAN501_frontier_seminar_decision_intelligence/README.md) |

Part of the [Data Analysis major](../../README.md). Uses the cohort, funnel and sessionization SQL from [DAN301](../DAN301_spreadsheets_to_sql_analytical_querying_in_depth/README.md), the experiment design from [DAN302](../DAN302_business_statistics_and_experimentation/README.md) and the presentation skills from [DAN303](../DAN303_data_visualization_and_storytelling/README.md). Taught alongside [DAN304](../DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md), where the metrics you design here are implemented once in a semantic layer.

## Why this course matters now

Product and business analysts decide which numbers a company steers by, and those numbers shape behaviour. In July 2026 Eternal, Blinkit's parent, said it would stop reporting Gross Order Value and use Net Order Value as its primary operating metric from the June quarter. A metric change like that changes every growth chart, target and comparison that depended on the old one. Economics also move under you. NPCI says a 0.4% merchant discount rate applies to UPI person-to-merchant payments above ₹2,000 from 15 October 2026, capped at ₹300 per transaction, while payments up to ₹2,000 (more than 95% of P2M volume) stay free. Every Indian fintech and merchant unit-economics model has to be re-run. AI assistants can now compute any funnel or cohort in seconds. They cannot decide what "active" should mean for your business, which input metric a team can move, or whether a payback period is believable. That judgement is what this course trains.

## Learning outcomes

By the end you can:

1. **Design** metrics that are precise, sensitive, attributable and hard to game, each paired with guardrail metrics. **Write** a definition with no ambiguity left in it.
2. **Choose** a north-star metric and **decompose** it into a metric tree of inputs that teams can own and move.
3. **Write** an event tracking plan (names, properties, identity, consent) and **validate** incoming events against it.
4. **Build and interpret** funnels, retention curves, cohort tables, stickiness and growth accounting, in SQL and in a product analytics tool.
5. **Investigate** a metric drop with a structured root-cause method and **separate** data issues from real changes.
6. **Estimate** customer lifetime value (historical, cohort-based and probabilistic with BG/NBD) and CAC payback, and **show** how sensitive they are to their assumptions.
7. **Model** unit economics (contribution margin per order or per user) for quick-commerce, fintech and subscription businesses from public disclosures and stated assumptions.
8. **Recommend** a product decision in a written analysis that sizes the opportunity, states uncertainty and proposes how to measure success.

## Chapters and lessons

### Chapter 1 · The product analyst's job (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Four kinds of question | What happened, why, what if, what should we do; matching method to question | Classify 20 stakeholder requests; rewrite 5 vague ones |
| 1.2 Business models to metrics | Marketplaces, subscriptions, ads, lending, payments; where revenue and cost come from | Metric list for 4 Indian business models |
| 1.3 Reading company disclosures | Shareholder letters and annual reports as metric sources; definitions in footnotes | Extract every operating metric and its definition from one Eternal or Swiggy shareholder letter |
| 1.4 Metrics change | Eternal's switch from GOV to NOV (2026); restating history; communicating a definition change | Restate a 6-quarter trend under a new definition with a reconciliation |

**Check your understanding:** Why might a company prefer a "net" order value over a "gross" one as its headline metric? What breaks in a dashboard when a metric definition changes mid-year? Which of your 20 requests could an analyst refuse, and why?

### Chapter 2 · Designing metrics (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Properties of good metrics | Sensitive, attributable, timely, hard to game, aligned with value; precise denominators and time windows | Score 10 real-sounding metrics on these properties |
| 2.2 Goodhart's law | Targets that stop measuring; call-centre handle time, delivery time promises, "orders" with no margin | Design a guardrail for each of 5 gamed metrics |
| 2.3 Frameworks | AARRR (acquisition, activation, retention, referral, revenue); Google's HEART framework (Rodden, Hutchinson and Fu, 2010) | Apply HEART to a UPI app's bill-payment feature |
| 2.4 Leading and lagging | Input vs output metrics; activation events that predict retention (and the selection trap in finding them) | Propose and test an activation metric on TheLook data |
| 2.5 Writing the definition | Event, entity, window, filters, exclusions (test users, bots, refunds), time zone, owner | Write 6 definitions a stranger could implement identically |

**Check your understanding:** Why is "users who did X in week 1 retain better, so X causes retention" weak evidence? What does a guardrail metric protect against? Which parts of a definition most often differ between two teams' "active user"?

### Chapter 3 · North-star metrics and metric trees (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Choosing a north star | Value delivered to customers that leads to revenue; Amplitude's North Star Playbook; when a single metric is wrong | Propose and critique north stars for 4 companies |
| 3.2 Decomposition | Multiplicative trees (GMV = buyers × orders per buyer × AOV) and additive trees (revenue by channel) | Build a 3-level tree for an illustrative quick-commerce business |
| 3.3 Ownership | Mapping input metrics to teams; avoiding double ownership | Assign owners and targets to your tree |
| 3.4 Diagnosis with trees | Contribution of each branch to a change; log decomposition for multiplicative trees | Explain a 6% GMV drop branch by branch with numbers |
| 3.5 Sensitivity | Which input moves the output most per unit of effort | A sensitivity table for your tree |

**Check your understanding:** Why are multiplicative contributions hard to split, and how does a log decomposition help? When does a north star encourage bad behaviour? What makes an input metric "ownable"?

### Chapter 4 · Event tracking and instrumentation (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Tracking plans | Object–action event names, required properties, types, versioning | Write a tracking plan for an illustrative grocery app's checkout |
| 4.2 Identity | Anonymous IDs, login stitching, multiple devices, shared phones (common in Indian households) | Stitch anonymous and logged-in events in SQL; measure the merge rate |
| 4.3 Client vs server events | Ad blockers, offline sessions, duplicate sends; which events must come from the server | Decide the source for 12 events and justify each |
| 4.4 Validation | Schema validation at collection (Snowplow, RudderStack, Segment Protocols, PostHog); monitoring event volume | Validate a synthetic event stream; catch 4 planted breaks |
| 4.5 Consent and purpose | Consent before tracking, purpose limitation and data minimisation under India's DPDP Act, 2023 and Rules, 2025 | Mark which planned properties are personal data and which are unnecessary |

**Check your understanding:** Why should a payment confirmation event never rely only on the client? What breaks in retention numbers when login stitching fails? Which tracking properties would you drop to minimise personal data without losing analysis value?

### Chapter 5 · Funnels (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Funnel definitions | User vs session funnels, time-bounded, strict vs loose order, re-entry | Compute one checkout funnel 4 ways; explain the differences |
| 5.2 Drop-off diagnosis | Step conversion, time to convert, segment cuts (device, city, payment method, new vs returning) | Find the step and segment behind a funnel decline |
| 5.3 Payment funnels in India | UPI intent and collect flows, card OTP steps, cash on delivery; failure reason codes | Model a payment-success funnel with failure reasons (illustrative data) |
| 5.4 Tools | Funnels in PostHog, Mixpanel or Amplitude vs your own SQL; reconciling the two | Rebuild a tool's funnel in SQL to the same number |

**Check your understanding:** Why can a loose funnel make a broken step look healthy? What would make a session funnel and a user funnel disagree sharply? Where do payment funnels in India lose users that a card-only funnel would miss?

### Chapter 6 · Retention and engagement (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Retention curves | N-day, bounded and unbounded retention; acquisition vs behavioural cohorts; curves that flatten vs decay to zero | Plot retention curves for 6 monthly cohorts of TheLook |
| 6.2 Churn without subscriptions | Inactivity windows; choosing the window from return-gap distributions | Pick a churn window from data and defend it |
| 6.3 Stickiness and frequency | DAU/MAU, active-days-per-month histograms, power users | Active-days histogram for the GA4 sample |
| 6.4 Resurrection | Returning users, win-back campaigns, why resurrected users behave differently | Count and profile resurrected users |
| 6.5 Engagement in AI features | Acceptance rate, retry rate, cost per successful task, feedback-button bias | Define 4 metrics for an AI assistant feature (illustrative) |

**Check your understanding:** What does a retention curve that flattens tell you about product–market fit for a segment? Why is DAU/MAU misleading for a weekly-use product? Why are thumbs-up rates on an AI feature a biased sample?

### Chapter 7 · Growth accounting and root-cause analysis (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Growth accounting | New, retained, resurrected and churned users (or revenue); the growth "quick ratio" | Growth accounting table for 12 months of TheLook |
| 7.2 Revenue movements | New, expansion, contraction and churned revenue; net revenue retention | NRR by cohort for an illustrative SaaS dataset |
| 7.3 Root-cause method | Is it real (pipeline, definition, logging)? Internal change? External (festival, holiday, outage, competitor)? Which segment? | Work through 3 "orders fell 8% yesterday" cases |
| 7.4 Mix vs rate | Separating composition change from behaviour change (from DAN302) | Decompose a conversion change into mix and rate |

**Check your understanding:** Why should the first question about a metric drop be "is the data right"? How can total users grow while retention worsens? What does a quick ratio below 1 mean?

### Chapter 8 · Customer value: LTV, CAC and payback (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Historical and cohort LTV | Cumulative contribution per acquired customer by cohort; margins, not revenue | Cohort LTV curves for Online Retail II |
| 8.2 Probabilistic LTV | BG/NBD and Gamma-Gamma (Fader, Hardie and Lee, 2005); PyMC-Marketing's CLV module | Fit BG/NBD; check predicted vs actual purchases on a holdout period |
| 8.3 CAC | Blended vs paid CAC, attribution choices, organic halo | Compute CAC three ways for an illustrative channel mix |
| 8.4 Payback and ratios | Payback months; the common LTV/CAC ≥ 3 heuristic and how it is abused (undiscounted, revenue-based, immature cohorts) | Rebuild an inflated LTV/CAC claim honestly |
| 8.5 Discounting and uncertainty | Discount rates, intervals on LTV, sensitivity to churn assumptions | LTV with a 90% interval and a tornado chart |

**Check your understanding:** Why is revenue-based LTV misleading for a low-margin business? What happens to LTV estimates when the newest cohorts dominate? Why does blended CAC flatter paid channels?

### Chapter 9 · Unit economics (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Contribution margin per order | Order value, commission or margin, fees, ad income minus delivery cost, discounts, payment costs, packaging and wastage | An order-level contribution model for an illustrative quick-commerce dark store |
| 9.2 Payments economics | MDR: UPI P2M at 0% up to ₹2,000 and 0.4% above (capped at ₹300) from 15 Oct 2026; card MDRs; where payment apps earn instead | Recompute a merchant's payment costs before and after the October 2026 change |
| 9.3 Subscription and SaaS | ARR, gross margin, NRR, CAC payback, the effect of annual pre-payment | A SaaS unit-economics sheet with 3 scenarios |
| 9.4 Fixed vs variable costs | Dark-store utilisation, order density, operating leverage; why unit economics improve with density | Break-even orders per day for a store under stated assumptions |
| 9.5 Building from disclosures | Using shareholder letters for definitions and ranges; labelling every assumption | A one-page model sourced from one public letter, with assumptions flagged |

**Check your understanding:** Why can contribution per order rise while total profit falls? How does a payment-cost change hit low-ticket and high-ticket merchants differently? Which inputs to a unit-economics model would you never present without a range?

### Chapter 10 · From analysis to decision (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Opportunity sizing | Top-down from public data, bottom-up from funnels, guesstimates with explicit assumptions | Size an opportunity three ways; reconcile the gap |
| 10.2 Prioritisation | Expected value, confidence, effort; why "impact" estimates are usually inflated | Rank 6 proposals with expected value and confidence |
| 10.3 The analysis doc | Question, answer, evidence, uncertainty, recommendation, how we will measure it | A 2-page product analysis for one proposal |
| 10.4 Weekly business reviews | Metric pages, variance explanations, commitments; avoiding narrative fallacy | Run a mock WBR on your P2 dashboard |
| 10.5 Working with product managers | Pre-registering success criteria with the PM before launch | Write success criteria for a PM's feature brief |

**Check your understanding:** Why should success criteria be agreed before a launch? What makes a guesstimate defensible in an interview or a meeting? When should an analyst recommend not building something?

### Chapter 11 · AI-assisted product analytics (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Where AI helps | Drafting funnel and cohort SQL, summarising feedback text, first-pass anomaly explanations; Claude, ChatGPT, Gemini and the AI features in BI tools | Have an assistant produce 10 standard analyses; time it |
| 11.2 Where it misleads | Silent definition choices, survivorship in cohorts, causal stories for correlations, invented benchmarks | Find the errors in 5 AI-written analyses with planted flaws |
| 11.3 Verification | Reconcile to your semantic layer; check definitions, windows and denominators; demand the query | Build a 15-item checklist and apply it |
| 11.4 Final review | Present P3 to a mock leadership panel | Panel presentation and Q&A |

**Check your understanding:** Why should an assistant's funnel be reconciled against your own definition before it is shared? What does an "invented benchmark" look like, and how do you catch it? Which part of a product analysis should never be delegated?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Metrics from disclosures | — |
| 2 | 2 | Lab 2 · Definitions and guardrails | Definition sheet |
| 3 | 3 | Lab 3 · Metric tree diagnosis | **P1 due** |
| 4 | 4 | Lab 4 · Tracking plan and validation | Tracking plan |
| 5 | 5 | Lab 5 · Funnels four ways | — |
| 6 | 6 | Lab 6 · Retention and churn windows | Mid-term case (AI off) |
| 7 | 7 | Lab 7 · Growth accounting and root cause | — |
| 8 | 8 | Lab 8 · Cohort and BG/NBD LTV | — |
| 9 | 8–9 | Lab 8 (cont.) | **P2 due** |
| 10 | 9 | Lab 9 · Unit economics and MDR scenarios | — |
| 11 | 10 | Lab 10 · Sizing and prioritisation | Analysis doc |
| 12 | 10 | Mock WBR | — |
| 13 | 11 | AI analysis audit | — |
| 14 | 11 | Leadership panel | **P3 due** |
| 15 | Review | Case interviews (AI off) | Final exam: case + SQL |

## Working with AI in this course

- **Use AI for:** drafting funnel, cohort and growth-accounting SQL; summarising app reviews and support tickets into themes you then verify; challenging your metric definitions; generating synthetic event data for tests; drafting the analysis document you then rewrite.
- **Do without AI (drills):** metric definitions; metric trees; root-cause cases out loud in 15 minutes; guesstimates; unit-economics models built from a blank sheet; the mid-term and final cases. These are exactly what analyst interviews test.
- **Verify AI output by:**
  - asking for the full query and checking the event, window, filters and denominator against your written definition;
  - reconciling to a semantic-layer metric or your own SQL;
  - checking every causal claim against the design that produced the data;
  - tracing every external number (benchmarks, market sizes) to a source, and deleting it if there is none.
- **Where AI still fails here:** in your labs you will see assistants choose a session funnel when you meant a user funnel, include immature cohorts in averages, and quote "industry benchmark" retention rates with no source. On DABstep, a benchmark of multi-step analysis tasks from a financial analytics platform, the best agent solved 14.55% of hard tasks (2025). Keep a log of each failure and the check that caught it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| Projects P1 · P2 · P3 | 10% · 15% · 25% |
| Mid-term case (AI off) | 10% |
| Final exam (AI off): live case + SQL | 20% |

**Mastery gate.** You pass when you can, with AI off: (1) in a 20-minute live case, diagnose a metric drop by asking the right data-quality, segment and external questions and reach a testable hypothesis; (2) in 45 minutes, design a north-star metric, a 3-level metric tree with owners, and 3 guardrails for an unseen business; (3) build a contribution-margin-per-order model from a public disclosure plus stated assumptions, and show which two assumptions matter most.

## Industry reality

Product analytics is a core analyst role at Indian consumer internet, fintech and SaaS companies, and at global firms' capability centres. Public companies such as Eternal and Swiggy publish quarterly shareholder letters with operating metrics and their definitions, the best free material for learning how real businesses measure themselves. Product analytics tools (Amplitude, Mixpanel, PostHog, GA4) and warehouse-native analysis coexist. Analysts are expected to reconcile them, and to own definitions rather than accept a tool's defaults.

**Interview questions from this course**

1. *"Daily orders fell 8% yesterday. Investigate."* Strong answer: checks data first (pipeline delays, tracking releases, definition changes); then external factors (holiday, weather, outage, competitor promotion); then decomposes by tree (users × frequency) and segments (city, platform, new vs returning); states hypotheses and the query for each.
2. *"Pick a north-star metric for a UPI payments app."* Strong answer: ties value to repeat successful payments (for example, monthly transacting users or successful payments per active user), explains why not downloads or GMV alone, adds guardrails (failure rate, fraud, complaints) and inputs teams can own.
3. *"How would you define and measure retention for a quick-commerce app?"* Strong answer: chooses an order-based activity event, picks a window from return-gap data, uses cohort curves with immature cohorts masked, separates new from resurrected users, and mentions frequency as well as retention.
4. *"Is our LTV/CAC of 5 good?"* Strong answer: asks whether LTV is margin-based, discounted and built from mature cohorts; whether CAC is blended or paid; checks payback months and sensitivity to churn; is sceptical of rules of thumb.
5. *"Guesstimate the number of UPI QR codes at kirana stores in Pune."* Strong answer: structures population → households → kirana stores per household or per area → QR adoption rate; states every assumption with a range; sanity-checks against any public figure available; gives a range, not a point.

## Resources (free first)

- **Metrics and frameworks:** [Amplitude North Star Playbook](https://amplitude.com/books/north-star); Rodden, Hutchinson and Fu, [HEART framework](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) (CHI 2010).
- **Instrumentation:** [Snowplow docs](https://docs.snowplow.io/); [RudderStack docs](https://www.rudderstack.com/docs/); [PostHog docs](https://posthog.com/docs); [Mixpanel docs](https://docs.mixpanel.com/docs/what-is-mixpanel).
- **Customer value:** Fader, Hardie and Lee, ["Counting Your Customers" the Easy Way](http://brucehardie.com/papers/018/fader_et_al_mksc_05.pdf) (*Marketing Science*, 2005); [PyMC-Marketing CLV guide](https://www.pymc-marketing.io/en/stable/guide/clv/clv_intro.html).
- **Company disclosures:** [Eternal investor relations](https://www.eternal.com/investor-relations/); [Swiggy investor relations](https://www.swiggy.com/corporate/investor-relations/).
- **Payments:** NPCI, [FAQs on MDR on select UPI P2M transactions](https://www.npci.org.in/uploads/FA_Qs_Merchant_Discount_Rate_MDR_on_Select_UPI_P2_M_Transactions_58dba1d39e.pdf) (15 Sep 2026); [NPCI UPI statistics](https://www.npci.org.in/what-we-do/upi/product-statistics).
- **Datasets:** BigQuery `thelook_ecommerce` and `ga4_obfuscated_sample_ecommerce`; [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii); [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
- **Paid, optional:** Alistair Croll and Benjamin Yoskovitz, *Lean Analytics* (O'Reilly, 2013).

## Sources

All checked 12 Oct 2026.

- Kotak Neo, "Eternal Q1 FY27 Results" (22 Jul 2026), on discontinuing GOV in favour of NOV and Blinkit NOV — https://www.kotakneo.com/news/stocks/eternal-q1-fy27-results-net-profit-rs-92-crore-revenue-rs-20211-crore-blinkit-growth/
- NPCI, "Merchant Discount Rate (MDR) on Select UPI (P2M) Transactions: FAQs" (15 Sep 2026) — https://www.npci.org.in/uploads/FA_Qs_Merchant_Discount_Rate_MDR_on_Select_UPI_P2_M_Transactions_58dba1d39e.pdf
- RBI, Discussion Paper on Charges in Payment Systems (zero MDR on UPI and RuPay debit cards from 1 Jan 2020) — https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=21082
- PIB, DPDP Rules, 2025 notified (17 Nov 2025) — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf
- Egg et al., DABstep (arXiv 2506.23719, 2025) — https://arxiv.org/abs/2506.23719
- Fader, Hardie and Lee, *Marketing Science* 24(2), 2005, doi:10.1287/mksc.1040.0098
- Rodden, Hutchinson and Fu, "Measuring the User Experience on a Large Scale", CHI 2010 — https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/

_Last reviewed: 2026-10_
