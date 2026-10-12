# DAN303 · Data Visualization and Storytelling

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [FND115](../../../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | [DAN403](../../year_4/DAN403_domain_analytics_finance_marketing_operations/README.md), [DAN304](../DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md), [DAN305](../DAN305_product_and_business_analytics_metrics_funnels/README.md) |

Part of the [Data Analysis major](../../README.md). Builds on the writing skills from [FND106](../../../../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md) and the SQL from FND115. Taught alongside [DAN301](../DAN301_spreadsheets_to_sql_analytical_querying_in_depth/README.md) and [DAN302](../DAN302_business_statistics_and_experimentation/README.md), whose results you will chart and present here.

## Why this course matters now

An analysis changes nothing until someone understands it and acts. Every major BI tool now generates charts and summaries from a sentence. Copilot in Power BI creates report pages and writes DAX. Tableau Pulse describes metric changes in plain language. Looker's Conversational Analytics answers questions over the LookML model, though its documentation lists only line, area, bar, scatter and pie charts as fully supported (October 2026). Microsoft's own documentation warns that without a prepared semantic model, Copilot "can misinterpret the data and return generic or inaccurate results". Machines also still read charts worse than people: on the CharXiv benchmark, GPT-4o answered 47.1% of chart-reasoning questions correctly against 80.5% for humans (2024). What stays human is choosing which comparison matters, drawing it so it cannot be misread, and telling a decision-maker what to do and how sure you are.

## Learning outcomes

By the end you can:

1. **Choose** a chart from the question being asked (comparison, change, distribution, part-to-whole, relationship, geography, flow), and **justify** it with graphical-perception evidence.
2. **Detect and fix** misleading charts: truncated or dual axes, unnormalised maps, area distortions, missing uncertainty.
3. **Design** accessible charts that meet WCAG 2.2 contrast ratios and do not rely on colour alone.
4. **Build** reproducible charts in code with a grammar of graphics (Vega-Lite/Altair or ggplot2/plotnine).
5. **Build** a dashboard in Power BI on a star-schema model with DAX measures, time intelligence for the Indian fiscal year and row-level security; and an equivalent in Tableau or Looker Studio and in one open-source tool (Metabase or Superset).
6. **Write** an analysis memo whose title states the finding, whose structure puts the answer first, and whose numbers are traceable.
7. **Present** a recommendation to executives in 3 and 10 minutes, and **handle** hostile questions about the data.
8. **Critique** AI-generated charts and narratives, and **prove** each error you find.

## Chapters and lessons

### Chapter 1 · How people read charts (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Graphical perception | Cleveland and McGill's ranking (1984): position beats length, angle, area and colour; Heer and Bostock's crowdsourced replication (2010) | Run the classic judgement experiment on 10 classmates; compare errors for bars vs pies |
| 1.2 Pre-attentive attributes | Colour, size and position that the eye sees before reading; using them to direct attention | Highlight one series out of 12 without a legend |
| 1.3 Data-ink and clutter | Tufte's data-ink ratio and lie factor; removing chartjunk without removing meaning | Declutter 3 default Excel charts; show before and after |
| 1.4 What a chart is for | Exploration vs explanation; the one question each chart answers | Write the question above each of 10 published charts |

**Check your understanding:** Why are pie charts hard to compare across two years? When does decoration help memory without hurting accuracy? What is the difference between a chart for you and a chart for a decision-maker?

### Chapter 2 · Choosing the chart (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Comparisons and rankings | Sorted bars, dot plots, lollipops, slopegraphs for two time points | Redraw a 15-state comparison three ways; pick one |
| 2.2 Change over time | Line charts, indexed lines (base = 100), small multiples, cycle plots for weekly patterns | Monthly UPI volume indexed to a base month |
| 2.3 Distributions | Histograms, ECDFs, box and violin plots, beeswarms; showing n | Delivery-time distributions for 6 cities |
| 2.4 Part-to-whole and flows | Stacked bars and their limits, waterfalls for bridges (revenue last year → this year), Sankey for flows | A revenue bridge from DAN302's price–volume–mix decomposition |
| 2.5 Maps | Choropleths normalised per capita, proportional symbols, when a map is the wrong choice; official Survey of India boundaries for maps of India | State-wise per-capita indicator from NFHS-5, with and without normalisation |

**Check your understanding:** Why does a stacked bar make every series except the bottom one hard to compare? When is a map worse than a sorted bar chart of the same data? What does a waterfall show that a pair of bars hides?

### Chapter 3 · Honest scales and uncertainty (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Baselines and axes | Zero baselines for bars, when lines may truncate, log scales for growth, aspect ratio and banking to 45° | Find and fix 6 misleading charts from a provided set |
| 3.2 Dual axes and rescaling | Why dual axes invent correlations; indexed alternatives | Rebuild a dual-axis "marketing spend vs sales" chart honestly |
| 3.3 Normalising | Per capita, per user, per order; rates with their denominators visible | Re-chart crime or health counts per 1 lakh population |
| 3.4 Showing uncertainty | Error bars, intervals, fan charts, quantile dot plots, hypothetical outcome plots | Show a DAN302 experiment result four ways; test which a manager reads correctly |
| 3.5 Small numbers | Suppressing or flagging cells with tiny n; funnel plots | A city league table with small-n flags |

**Check your understanding:** When is a truncated y-axis acceptable on a line chart and never on a bar chart? Why do dual-axis charts mislead even when both scales are labelled? What is the minimum uncertainty information an executive chart should carry?

### Chapter 4 · Colour, text and accessibility (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Palettes | Sequential, diverging and categorical palettes; ColorBrewer and viridis; perceptual uniformity | Assign palettes to 8 described datasets |
| 4.2 Colour vision deficiency | Red–green confusion; simulators; redundant encoding with shape, labels and position | Make a red/green KPI table readable in a deuteranopia simulator |
| 4.3 Contrast and accessibility | WCAG 2.2 contrast (4.5:1 for normal text, 3:1 for graphical objects), alt text for charts, keyboard-usable dashboards | Audit a dashboard; fix every failure |
| 4.4 Words on charts | Titles that state the finding, direct labels instead of legends, annotations of events | Rewrite 10 chart titles from "Sales by month" to a finding |
| 4.5 Audience conventions | Lakh/crore vs million/billion, Indian fiscal year labels (FY26 = April 2025–March 2026), units in every label | Localise one executive chart for an Indian board and a global board |

**Check your understanding:** Why is "Revenue by month" a weak title? How do you show "good vs bad" without relying on red and green? When should a chart use lakh and crore, and what goes wrong if you mix systems in one deck?

### Chapter 5 · Charts in code (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Grammar of graphics | Data, marks, encodings, scales, facets; Vega-Lite and Altair (or ggplot2/plotnine) | Rebuild 5 charts from Chapter 2 declaratively |
| 5.2 Reproducibility | Charts generated from queries and versioned specs; no manual edits after export | A script that regenerates a 6-chart pack from raw data |
| 5.3 Fine control | matplotlib for publication-quality detail: annotations, custom axes, export sizes | Replicate an Our World in Data chart to within visible tolerance |
| 5.4 Interaction | Tooltips, linked selection, filters; when interaction hides the message | An interactive exploration and a static explanation of the same data |

**Check your understanding:** Why is a chart produced by a script easier to trust than one adjusted by hand? When does interactivity help an executive and when does it shift work onto them? What is a facet, and when does it beat colour?

### Chapter 6 · Dashboard design (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Dashboard types | Strategic (few KPIs, monthly), operational (real-time, alerts), analytical (exploration); one audience per dashboard | Classify 6 real requests; reject one with reasons |
| 6.2 Layout | Most important number top-left; KPI cards with comparison and trend; consistent filters | Wireframe a sales dashboard on paper before any tool |
| 6.3 Requirements | Interviewing users: the decisions they make, how often, at what grain; definitions agreed in writing | Run a 20-minute requirements interview; write the spec |
| 6.4 Performance and freshness | Load time budgets, pre-aggregation, refresh schedules, showing "data as of" | Make a slow dashboard load in under 5 seconds |
| 6.5 Sprawl and retirement | Usage logs, duplicate dashboards, certifying trusted ones, deleting the rest | Audit an illustrative BI estate and propose what to retire |

**Check your understanding:** Why does a dashboard for everyone usually serve no one? What should every KPI card show besides the number? How do you decide that a dashboard should be deleted?

### Chapter 7 · Power BI and DAX (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The model first | Power Query into a star schema; one-to-many relationships, filter direction, why flat tables break measures | Model DAN301's TheLook extract as a star schema |
| 7.2 DAX evaluation | Measures vs calculated columns; row context vs filter context; `CALCULATE` and context transition | Predict 10 measure results under different slicers, then check |
| 7.3 Time intelligence | Date table, `TOTALYTD` with a 31 March year end, same-period-last-year, rolling 3 months | An Indian fiscal-year YTD and YoY page |
| 7.4 Security and sharing | Row-level security by region, workspaces, apps, certified semantic models | RLS so each regional manager sees only their region |
| 7.5 Copilot in Power BI | Report page generation, DAX query writing, measure descriptions; requirements (Fabric F2+ or Premium P1+); preparing the model for AI; verified answers | Generate a page with Copilot; list everything you had to correct |

**Check your understanding:** Why does a measure give a different number in a card and in a table row? What happens to `SAMEPERIODLASTYEAR` without a continuous date table? Why does Microsoft say model preparation decides Copilot's quality?

### Chapter 8 · Tableau and Looker Studio (week 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Tableau fundamentals | Dimensions and measures, marks card, discrete vs continuous, Tableau Public | Rebuild your Power BI page in Tableau Public |
| 8.2 Level-of-detail expressions | `FIXED`, `INCLUDE`, `EXCLUDE`; table calculations and their order of operations | Customer first-order cohort with a `FIXED` LOD |
| 8.3 Tableau Pulse | Metric definitions (measure, time dimension, filters), AI-generated insight summaries, Tableau Agent in Pulse | Define 3 metrics; compare the generated insights with your own analysis |
| 8.4 Looker Studio | Free connectors to BigQuery and Sheets, calculated fields, blending pitfalls (every blend is a join, and the wrong join type or key silently drops or duplicates rows) | A BigQuery-backed dashboard on the GA4 sample |

**Check your understanding:** When would you use a `FIXED` LOD instead of a table calculation? Why can a Looker Studio blend silently drop or duplicate rows? What does Pulse need from you before its insights can be trusted?

### Chapter 9 · Open-source BI and BI as code (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Metabase | Questions, models, metrics, collections; self-hosting with Docker | Self-host Metabase on your DuckDB or Postgres warehouse |
| 9.2 Apache Superset | SQL Lab, datasets, virtual metrics, chart plugins, role-based access | The same dashboard in Superset; compare effort |
| 9.3 BI as code | Evidence (Markdown + SQL), Quarto, Streamlit; pull requests for dashboards | A versioned report rebuilt on every merge |
| 9.4 Choosing a tool | Licence and cost, governance, semantic-layer support, skills on the team, AI features | A one-page tool recommendation for a 40-person Indian startup (illustrative) |

**Check your understanding:** What do you gain and lose by defining a report in code instead of a GUI? Why might a startup pick Metabase over Power BI, and when would that decision reverse? What must stay consistent across tools for numbers to match?

### Chapter 10 · Memos, stories and executive presentations (weeks 11–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Answer first | Situation–complication–resolution; the pyramid principle; the "so what" in every heading | Restructure a chronological analysis into answer-first |
| 10.2 The analysis memo | Amazon's narrative six-page memos (Bezos, 2017 letter) as a model; a one-page version for analysts; appendices for method | A 1-page memo with 3 charts and a recommendation |
| 10.3 Chart sequences | One idea per slide or figure, progressive reveal, consistent scales across a deck | Turn a 15-chart deck into 5 charts that build an argument |
| 10.4 Presenting to executives | The 3-minute version, anticipating objections, pre-wiring with stakeholders, saying "I don't know yet" | Present to a panel playing a CFO, a sales head and a sceptic |
| 10.5 When they say the number is wrong | Tracing a figure to its query, definitions and refresh time in front of the room | Live drill: defend or correct a challenged number |

**Check your understanding:** Why does a chronological "here is what I did" presentation lose executives? What belongs in the appendix rather than the body? What do you do when a senior leader's number contradicts yours?

### Chapter 11 · AI in visualisation, and dashboard critique (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 AI-generated charts | Copilot report pages, Tableau Agent, Looker Conversational Analytics, Claude and ChatGPT chart code; default choices you must override | Generate 10 charts from prompts; grade each against Chapters 2–4 |
| 11.2 AI narratives | Auto-summaries that state causes the data cannot show, round numbers wrongly or miss the denominator | Fact-check 5 generated summaries line by line |
| 11.3 Machines reading charts | CharXiv's gap; why an AI should read your data, not your screenshot | Ask an assistant to read 5 of your charts; log its errors |
| 11.4 Dashboard critique | A structured critique: audience, question, chart choice, honesty, accessibility, performance, definitions | Critique 3 public dashboards in 10 minutes each, interview style |

**Check your understanding:** Why should a model be given the query result instead of a chart image? What is the most common error in AI-generated dashboard summaries in your log? How do you structure a 10-minute dashboard critique?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Perception experiment | — |
| 2 | 2 | Lab 2 · Chart chooser | — |
| 3 | 3 | Lab 3 · Misleading-chart clinic | **P1 due** |
| 4 | 4 | Lab 4 · Accessibility audit | — |
| 5 | 5 | Lab 5 · Charts in code | Reproducible chart pack |
| 6 | 6 | Lab 6 · Requirements and wireframe | Mid-term critique (AI off) |
| 7 | 7 | Lab 7 · Star schema and DAX | — |
| 8 | 7–8 | Lab 7 (cont.) · Tableau rebuild | — |
| 9 | 8–9 | Lab 8 · Looker Studio and Metabase | **P2 due** |
| 10 | 9 | Lab 9 · BI as code | — |
| 11 | 10 | Lab 10 · Memo writing | Memo draft |
| 12 | 10 | Presentation rehearsal | Peer feedback |
| 13 | 10 | Executive panel | — |
| 14 | 11 | AI chart audit, critique drills | **P3 due** |
| 15 | Review | Live presentation of P3 | Final exam (AI off): critique + build |

## Working with AI in this course

- **Use AI for:** first drafts of chart code; DAX patterns you then test; alternative chart ideas; alt text drafts; a hostile reviewer for your memo ("list every claim this memo cannot support"). Copilot in Power BI, Tableau Agent, Looker's Conversational Analytics, Claude and ChatGPT all do some of this well.
- **Do without AI (drills):** paper wireframes before every dashboard; chart selection for 10 questions a week; predicting DAX results; writing the memo's first version; the critique and build exams.
- **Verify AI output by:**
  - recomputing every number in a generated summary from the query;
  - checking aggregation (sum vs average vs distinct count) and filters behind each generated visual;
  - running a colour-blindness simulator and a contrast checker;
  - checking every causal word ("because", "driven by") against what the data can show.
- **Where AI still fails here:** CharXiv measures a 33-point gap between GPT-4o and humans on chart reasoning. Looker's documentation says Conversational Analytics does not support prediction, forecasting, correlation or anomaly-detection questions. Your own audit log is the main evidence: record each generated chart or summary that was wrong, and how you proved it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| Projects P1 · P2 · P3 | 10% · 15% · 25% |
| Mid-term critique (AI off) | 10% |
| Final exam (AI off) + live presentation | 20% |

**Mastery gate.** You pass when you can: (1) with AI off, critique an unseen dashboard in 10 minutes, naming at least 5 concrete problems with fixes; (2) with AI off, from a provided star schema, build a one-page Power BI report with correct YTD and YoY measures for an Indian fiscal year in 75 minutes; (3) present a recommendation in 3 minutes to a panel and answer a challenge to one of your numbers by tracing it to its source on the spot.

## Industry reality

Power BI, Tableau and Looker dominate enterprise BI, and Metabase and Superset are common in startups because they are open source and self-hostable. Microsoft's PL-300 exam expects candidates to be "proficient at using Power Query and Data Analysis Expressions (DAX)". BI vendors are shifting from dashboards to metrics with generated narratives (Tableau Pulse) and chat (Copilot, Conversational Analytics), which puts more weight on the semantic model behind them. Many analyst loops include a dashboard-critique or presentation round.

**Interview questions from this course**

1. *"Critique this dashboard."* Strong answer: starts with audience and decision; then chart choice, scales, colour, clutter, definitions, freshness and performance; prioritises the three fixes that matter most.
2. *"How would you show this experiment result to the CEO?"* Strong answer: the effect with its interval on a simple dot-and-interval chart, the decision, the risk; no p-value tables; a backup slide for method.
3. *"Explain filter context in DAX."* Strong answer: the set of filters active when a measure evaluates (slicers, rows, columns, `CALCULATE` arguments); contrast with row context; context transition; an example where they differ.
4. *"Sales are up but the chart makes it look flat. What happened?"* Strong answer: axis range, scale, aggregation level or a dominant series; shows how to diagnose and redraw.
5. *"Your dashboard says ₹4.2 crore, finance says ₹3.9 crore."* Strong answer: compares definitions (gross vs net, returns, taxes), time zones and cut-off, refresh times, filters; traces both to source; documents the agreed definition.

## Resources (free first)

- **Books and guides:** Claus Wilke, [*Fundamentals of Data Visualization*](https://clauswilke.com/dataviz/); [FT Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary); [Datawrapper Academy](https://academy.datawrapper.de/); [ColorBrewer](https://colorbrewer2.org/); [WCAG 2.2](https://www.w3.org/TR/WCAG22/).
- **Code:** [Vega-Lite](https://vega.github.io/vega-lite/); [Altair](https://altair-viz.github.io/); [plotnine](https://plotnine.org/).
- **Power BI:** [Star schema guidance](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema); [Prepare your data for AI](https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai); [DAX Guide](https://dax.guide/); [SQLBI articles](https://www.sqlbi.com/articles/).
- **Tableau and Looker Studio:** [LOD expressions](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm); [Tableau Pulse](https://help.tableau.com/current/online/en-us/pulse_intro.htm); [Tableau Public](https://public.tableau.com/); [Looker Studio help](https://support.google.com/looker-studio).
- **Open source:** [Metabase docs](https://www.metabase.com/docs/latest/); [Apache Superset docs](https://superset.apache.org/docs/intro); [Evidence docs](https://docs.evidence.dev/).
- **Data:** [Our World in Data](https://ourworldindata.org/); [Open Government Data Platform India](https://www.data.gov.in/).
- **Paid, optional:** Cole Nussbaumer Knaflic, *Storytelling with Data* (Wiley, 2015); Tamara Munzner, *Visualization Analysis and Design* (CRC, 2014); Barbara Minto, *The Pyramid Principle*.

## Sources

All checked 12 Oct 2026.

- Microsoft Learn, Copilot for Power BI overview (updated 24 Aug 2026) — https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
- Google Cloud, Conversational Analytics in Looker overview (updated 9 Oct 2026) — https://docs.cloud.google.com/looker/docs/conversational-analytics-overview
- Tableau Help, Tableau Pulse — https://help.tableau.com/current/online/en-us/pulse_intro.htm
- Wang et al., "CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs" (arXiv 2406.18521, Jun 2024) — https://arxiv.org/abs/2406.18521
- Cleveland and McGill, "Graphical Perception", *JASA* 79(387), 1984, doi:10.1080/01621459.1984.10478080 · Heer and Bostock, "Crowdsourcing Graphical Perception", CHI 2010, doi:10.1145/1753326.1753357
- Jeff Bezos, 2017 Letter to Shareholders (six-page memos) — https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders
- Microsoft Learn, PL-300 Power BI Data Analyst Associate — https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/
- W3C, Web Content Accessibility Guidelines 2.2 — https://www.w3.org/TR/WCAG22/

_Last reviewed: 2026-10_
