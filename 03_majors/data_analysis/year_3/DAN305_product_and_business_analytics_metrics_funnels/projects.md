# DAN305 · Labs and projects

Every lab and project ships with the SQL or notebook that produced each number, a written definition for every metric used (event, entity, window, filters, time zone, owner), and a short memo that a product manager could act on. Assumptions taken from public disclosures cite the document and page; anything invented is labelled "assumption" with a range.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Metrics from disclosures | Extract every operating metric and definition from two consecutive Eternal or Swiggy shareholder letters | A metric dictionary with page references; a list of definitions that changed between the letters | 3 h |
| 2 · Definitions and guardrails | Write 6 metric definitions precise enough that two classmates implement them identically; add a guardrail for each | Definitions, both classmates' SQL, and a diff of their results | 3 h |
| 3 · Metric tree diagnosis | Build a 3-level tree for TheLook revenue; explain a planted 6% drop branch by branch with a log decomposition | Tree diagram, contribution table, and a one-paragraph explanation | 4 h |
| 4 · Tracking plan and validation | Write a checkout tracking plan; validate a synthetic event stream against it (JSON Schema or PostHog/Snowplow validation) | Plan, validator, and the 4 planted breaks you caught | 4 h |
| 5 · Funnels four ways | One checkout funnel on the GA4 sample computed as user, session, strict and loose; reproduce one in a product analytics tool | SQL, tool screenshot, and a reconciliation to the same number | 4 h |
| 6 · Retention and churn windows | Cohort retention curves; choose a churn window from the return-gap distribution | Curves with immature cohorts masked; churn-window justification | 3 h |
| 7 · Growth accounting and root cause | Growth accounting for 12 months; work through 3 "metric fell" cases with planted causes | Tables, and a root-cause write-up per case with the query that proved it | 4 h |
| 8 · Cohort and BG/NBD LTV | Cohort LTV curves and a BG/NBD + Gamma-Gamma fit on Online Retail II with a holdout period | Calibration plot (predicted vs actual purchases in holdout) and LTV with intervals | 5 h |
| 9 · Unit economics and MDR scenarios | Contribution per order for an illustrative merchant; recompute payment costs before and after NPCI's 15 Oct 2026 UPI MDR change across ticket sizes | Model, a scenario table by ticket-size band, and the share of orders affected | 4 h |
| 10 · Sizing and prioritisation | Size one opportunity top-down, bottom-up and by guesstimate; rank 6 proposals by expected value | Three estimates with assumptions, a reconciliation, and a ranked list | 3 h |

## Projects

### P1 · Metric dictionary and tree for a listed company (L1, ~6 hours)

**Real-world inspiration.** Listed Indian consumer-internet companies publish operating metrics every quarter, and occasionally change them, as Eternal did when it moved from Gross Order Value to Net Order Value as its primary operating metric in 2026. Analysts at funds, competitors and the companies themselves rebuild these numbers into models.

**What to build.** For Eternal or Swiggy, using at least four quarterly shareholder letters: a metric dictionary, a metric tree from the headline metric down to inputs the company reports, and a quarter-by-quarter table of every reported input.

**Acceptance criteria**
- Every metric has a definition quoted or paraphrased from the source, with document and page reference.
- The tree's arithmetic reconciles with reported totals where the company reports both levels (differences explained).
- Any definition change across quarters is flagged, and where the company gives both old and new figures, a reconciliation table is included.
- A one-page memo states which input explained most of the latest quarter's change, with numbers.

**Stretch goals.** Do the same for a second company and compare definitions; note every metric that looks similar but is defined differently.

**What it proves to an employer.** You read disclosures carefully, respect definitions, and can explain a company's performance through a metric tree.

### P2 · Product health dashboard and root-cause playbook (L2, ~15 hours)

**Real-world inspiration.** Product teams in e-commerce and fintech run weekly business reviews from a product health dashboard, and analysts are paged when a metric moves. Speed and accuracy of diagnosis are what get noticed.

**What to build.** On the BigQuery GA4 sample and TheLook datasets: a reverse-engineered tracking plan documenting the events you rely on; a dashboard (any DAN303 tool) with a north-star metric, its tree, funnels, retention cohorts, stickiness and growth accounting; and a written root-cause playbook. Your instructor or a classmate then injects 3 anomalies into a copy of the data (for example, a tracking break, a mix shift and a real behaviour change), and you diagnose each.

**Acceptance criteria**
- Every dashboard metric links to a written definition, and SQL reproduces each tile to the unit.
- Funnel and retention numbers reconcile with a second computation (product analytics tool import or an independent query).
- Immature cohorts are masked; time-zone handling is stated.
- All 3 injected anomalies are correctly classified (data issue, mix or behaviour) with a proving query, each within 45 minutes.
- The playbook is a one-page ordered checklist that a new analyst could follow.

**Stretch goals.** Add automated alerts with thresholds based on historical variability; add an AI-written first-pass explanation and grade it against your diagnosis.

**What it proves to an employer.** You can watch a product's health, tell real changes from broken data, and explain both quickly, which is the daily job of a product analyst.

### P3 · Unit economics and growth model with a decision memo (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Quick-commerce companies report contribution margins that depend on order value, density and costs. Payment costs change too: NPCI's FAQ says a 0.4% MDR applies to UPI P2M payments above ₹2,000 from 15 October 2026, capped at ₹300. The business below is illustrative; its assumptions come from public ranges and are labelled as such.

**What to build.** A decision model for an illustrative quick-commerce or merchant-payments business:
1. An order-level contribution model (order value, margin or commission, fees, ad income, delivery cost, discounts, payment costs, packaging, wastage), with every input sourced from a public disclosure or given as a labelled assumption range.
2. A customer model: cohort retention and BG/NBD-based LTV estimated on real transaction data (Online Retail II as a proxy for repeat behaviour, with that limitation stated), combined with CAC scenarios to give payback months.
3. A store or merchant economics layer: break-even orders per day and how contribution changes with order density.
4. A Monte Carlo simulation over the assumption ranges and a tornado chart of the inputs that matter most.
5. A two-page memo recommending one decision (for example, a minimum order value, a delivery-fee rule, or a merchant's response to the MDR change), plus an experiment design from DAN302 to measure it.

**Acceptance criteria**
- Every input has a source reference or an "assumption" label with a low, base and high value.
- The model reproduces a published company-level figure (for example, a reported contribution margin range) within a stated tolerance, or explains why it cannot.
- BG/NBD holdout calibration is shown and its error is reported.
- The memo states the recommendation, the expected effect with a range, the two assumptions that could reverse it, and the experiment that would settle it.
- Model logic lives in a script or a spreadsheet with a "Checks" tab; changing any assumption updates every output.
- Panel defence: you answer "what if order density falls 20%?" live from the model.

**Stretch goals.** Add a cash-flow view (working capital, inventory days); compare two cities with different density; publish an interactive version with Evidence or Streamlit.

**What it proves to an employer.** You can connect product metrics to profit, be honest about uncertainty, and turn a model into a decision with a plan to test it. Strategy, finance and product teams at consumer and fintech companies hire for this.

## Feeds into

- [DAN403 Domain Analytics](../../year_4/DAN403_domain_analytics_finance_marketing_operations/README.md): unit economics, CAC and attribution extend into finance and marketing analytics.
- [DAN402 Forecasting for Business Decisions](../../year_4/DAN402_forecasting_for_business_decisions/README.md): metric trees become driver-based forecasts.
- [DAN501 Frontier Seminar](../../year_5/DAN501_frontier_seminar_decision_intelligence/README.md): decision memos become decision models.
- [OV08B Product Analytics and Growth for AI Apps](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08B_product_analytics_and_growth_for_ai_apps/README.md): AI-feature metrics from Chapter 6 in depth.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): unit economics for your own venture.
