# DAN403 · Labs and projects

Every lab and project starts with a one-page domain map (glossary, process, money or patient flow, key metrics, data traps) and ends with a deliverable written for a named domain role: a CFO, a head of marketing, an operations head or a health official. Every figure taken from a filing, survey or report cites the document, table or page and the retrieval date; units (lakh, crore, million) and periods (quarter, fiscal year, standalone vs consolidated) are stated next to every number.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Domain map | Map an unfamiliar domain (insurance or telecom) in 3 hours; fact-check an AI-generated glossary of 30 terms | Map, corrected glossary with sources, and a list of the AI's errors | 3 h |
| 2 · Statements, variances and cohort revenue | Extract 5 years of statements for 2 listed companies; build a variance bridge; compute cohort revenue and NRR from a transaction log | Tidy statement tables, the bridge, and a cohort revenue table | 6 h |
| 3 · Vintages and roll rates | Vintage curves (30+ and 90+ days past due) and a roll-rate matrix on Freddie Mac loan-level data | Charts by origination year, the matrix, and a paragraph on which cohorts are worse | 5 h |
| 4 · Attribution comparison | Credit channels under 4 attribution rules on the Criteo attribution dataset; simulate a channel with high attributed but zero incremental value | Comparison table and the simulation showing why attribution misleads | 4 h |
| 5 · MMM with known truth | Simulate 3 years of weekly geo data with known channel effects; fit Meridian or PyMC-Marketing; calibrate with a simulated lift test | Parameter recovery table, before/after calibration ROI estimates | 6 h |
| 6 · Segments, survival and uplift | RFM segments with actions; Kaplan–Meier curves by channel; uplift analysis on the Hillstrom data | Segment playbook, survival plot, and an uplift-based targeting rule | 4 h |
| 7 · Flow, OTIF and inventory | Little's law on an illustrative warehouse; OTIF on Olist under two definitions; ABC–XYZ on M5 items; a 3-tier bullwhip simulation | Calculations, tables and a one-page operations note | 4 h |
| 8 · Delivery, geography and process mining | Decompose Olist delivery time by stage; map NYC taxi pickups at 3 H3 resolutions; discover a BPI Challenge process with PM4Py | Stage decomposition, maps, and a bottleneck report | 5 h |
| 9 · Health rates and survey comparisons | Age-standardise a rate; compare 5 indicators between NFHS-5 and NFHS-6 for one state's districts; HMIS data-quality checks | Standardised rates, a comparison flagged by meaningfulness, a data-quality report with suppression applied | 4 h |
| 10 · Public panel and diff-in-diff | Build a 3-indicator state panel from data.gov.in, NDAP or MoSPI; evaluate an illustrative programme with diff-in-diff and a placebo | Panel with source log, estimate with interval, placebo result, two-page brief | 4 h |

## Projects

### P1 · Financial health review of two listed Indian companies (L1, ~6 hours)

**Real-world inspiration.** Analysts at banks, funds, rating agencies and corporate strategy teams compare companies from their filings every quarter, and an AI summary of an annual report is only useful if someone checks the numbers.

**What to build.** For two listed companies in the same sector (for example, two consumer-internet companies or two retailers), a review covering: 5 years of P&L, balance sheet and cash flow in tidy tables; growth, margins (including any adjusted metric reconciled to reported profit), cash conversion cycle and return on capital; one chart page; and a one-page memo for a credit committee.

**Acceptance criteria**
- Every number traces to a filing page; standalone vs consolidated and units are stated throughout.
- Each adjusted or non-GAAP metric is reconciled to the reported figure.
- The memo explains at least one divergence between profit and cash with evidence from the cash flow statement.
- An AI-generated summary of one annual report is fact-checked line by line, with each error listed and corrected.

**Stretch goals.** Add a peer from the US using SEC financial statement data sets and compare; build a driver-based forecast for next year's revenue.

**What it proves to an employer.** You can read a company's numbers correctly and explain them to a decision-maker, which is the foundation of finance, strategy and credit roles.

### P2 · Marketing measurement study: attribution, experiments and MMM (L2, ~15 hours)

**Real-world inspiration.** Marketing teams see different answers from platform dashboards, GA4 attribution and marketing mix models. Google's Meridian and Meta's Robyn are open-source MMMs, and GA4 narrowed its attribution options in 2023. The brand and budgets below are illustrative and simulated.

**What to build.** A measurement study for an illustrative consumer brand spending across 5 channels in 20 Indian cities over 3 years:
1. A simulator with known true channel effects, adstock, saturation, seasonality (festivals, monsoon) and a brand-search channel that captures demand created elsewhere.
2. Attribution results (last click and data-driven-style) computed from simulated user journeys.
3. A geo lift test for one channel with matched city pairs and a power analysis.
4. An MMM (Meridian or PyMC-Marketing) fitted without and with calibration from the lift test.
5. A budget reallocation recommendation with uncertainty.

**Acceptance criteria**
- The study shows, with numbers, how attribution misstates at least two channels against the known truth.
- The MMM recovers true channel ROIs within its 90% intervals for at least 4 of 5 channels after calibration, and the report shows how calibration changed the estimates.
- The geo test's power analysis states the detectable effect for the chosen duration and number of cities.
- The reallocation states marginal ROI by channel with intervals and the expected change in conversions as a range.
- All results rebuild from one script with a fixed seed.

**Stretch goals.** Repeat the MMM with Robyn and compare; add reach and frequency inputs in Meridian; write a one-page explainer for a CMO.

**What it proves to an employer.** You understand why marketing numbers disagree and can design a measurement system that a CFO and a CMO would both accept.

### P3 · Domain deep-dive for a named decision-maker (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Senior analysts are trusted because they know a domain well enough to be challenged by its experts and hold their ground. Pick one track; each uses real public data, and the decision-maker is illustrative.

**Track A · Lending portfolio review (Freddie Mac loan-level data).** For a chief risk officer: vintage curves by origination year and product features, roll rates, an expected-loss estimate by segment, a mix-shift analysis, and a recommendation on which segments to tighten, with the trade-off in approvals.

**Track B · Marketplace delivery performance (Olist, plus a process-mining log).** For an operations head: stage-level delivery-time decomposition, OTIF under an agreed definition, seller and region bottlenecks, the link between lateness and reviews (as association), H3-based geographic hotspots, and a process-mining view of order handling.

**Track C · District health programme targeting (NFHS-6 and HMIS).** For a state health official: district-level indicators (for example, anaemia, child nutrition or institutional deliveries) with survey uncertainty, change since NFHS-5, facility-data quality checks, small-cell suppression, and a ranked shortlist of districts with reasons and caveats.

**Deliverables (all tracks).** A reproducible pipeline; a domain map and data dictionary; an analysis report; a dashboard for the decision-maker's team; a two-page decision memo; a 10-minute presentation with Q&A from a reviewer playing the domain expert.

**Acceptance criteria**
- The domain map and glossary are reviewed by a classmate from a different track, and every term they flag is resolved.
- Every number traces to code and source, with units and periods stated.
- At least 3 domain-specific traps (for example: immature vintages, attribution vs incrementality, survey uncertainty, censored delivery times) are identified and handled explicitly in the report.
- Uncertainty is shown wherever estimates come from samples or models, and the memo's recommendation states what would change it.
- Privacy: no table in the deliverables allows re-identification (small cells suppressed or aggregated; rule stated).
- In the Q&A, you answer at least 4 of 5 domain questions from the expert reviewer correctly, and say "I don't know, here is how I would find out" for the rest.

**Stretch goals.** Add a forecast from DAN402 (delinquency, delivery volume or caseload); add an experiment or policy-evaluation design to test your recommendation; publish a public version with suppressed data.

**What it proves to an employer.** You can be put in front of a finance, operations or public-health leader and add value in their language, which is what makes an analyst hard to replace.

## Feeds into

- [DAN501 Frontier Seminar](../../year_5/DAN501_frontier_seminar_decision_intelligence/README.md): decision intelligence and causal analytics applied to a domain.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): P3 is a natural starting point for a domain capstone.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): domain maps and memos are how co-op students get productive quickly.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): finance and marketing measurement for your own venture.
- [OV10 FinTech Systems Engineering](../../../../04_overlaps/OV10_fintech_systems_engineering/README.md): lending and payments analytics meet the systems that produce the data.
