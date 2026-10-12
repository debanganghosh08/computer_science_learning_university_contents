# CLD403 · FinOps and Cloud Cost Engineering

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [CLD303](../../year_3/CLD303_containers_and_kubernetes/README.md) | [CLD501](../../year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

Part of the [Cloud Engineering major](../../README.md). Draws on the cost sections of every Year 3 CLD course and on SQL from [FND115](../../../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md). This is an engineering course: you will query billing data, change architectures and write automation, not only build dashboards.

## Why this course matters now

Cloud spending is now large enough that cost is an architecture property, like latency. Flexera's 2026 survey of more than 750 cloud decision-makers found managing cloud spend was a top challenge for 85% of them, and estimated wasted IaaS and PaaS spend rose to 29%, the first increase in five years, with AI workloads named as a cause ([Flexera, March 2026](https://www.flexera.com/about-us/press-center/flexera-finds-cloud-value-is-rising-while-ai-waste-grows)). The FinOps Foundation's 2026 framework update widened the discipline from public cloud to "technology value", including SaaS, licences and data centres ([FinOps Foundation](https://www.finops.org/insights/2026-finops-framework/)), and the FOCUS 1.3 specification (December 2025) standardised how providers describe cost data, including shared-resource allocation and commitments.

AI changes both sides of the ledger. GPU instances and model tokens are the fastest-growing and least predictable line items, while AI assistants now answer cost questions in natural language: AWS released a Billing and Cost Management MCP server and AI explanations for forecasts in December 2025. A cost engineer who can join a FOCUS dataset to business metrics, compute cost per order or per million tokens, and change the architecture to bend that curve is valuable to every company that runs in the cloud, and to every founder watching runway.

## Learning outcomes

By the end you can:

1. **Explain** the FinOps Framework (principles, personas, phases, maturity, domains and capabilities, scopes) and **assess** an organisation's maturity.
2. **Query** raw billing exports (AWS Data Exports, Azure cost exports, Google BigQuery billing export) and **normalise** them to FOCUS.
3. **Design and enforce** cost allocation: account structure, tags, shared-cost splitting, and Kubernetes allocation.
4. **Define and track** unit economics such as cost per order, per active user and per million tokens.
5. **Optimise rates** with Savings Plans, reservations, committed-use discounts and Spot, and **quantify** commitment risk.
6. **Optimise usage** through rightsizing, scheduling, storage tiering, data-transfer redesign and Kubernetes bin-packing, with measured savings.
7. **Build** forecasts, budgets and anomaly detection that route to the people who can act.
8. **Model** the cost of AI workloads (training, self-hosted inference and managed model APIs) and **reduce** it without breaking quality targets.

## Chapters and lessons

### Chapter 1 · FinOps as a discipline (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Why cloud cost is different | Variable, decentralised spending; engineers as buyers; the "iron triangle" of speed, quality and cost | List 10 engineering decisions from last semester that changed a bill |
| 1.2 The FinOps Framework | Principles, personas (engineering, finance, procurement, product, leadership), phases (Inform, Optimize, Operate), crawl–walk–run maturity, domains and capabilities | Map a sample company's activities onto the framework |
| 1.3 Scopes and technology categories | Scopes (introduced 2025) and the 2026 expansion to SaaS, licensing, private cloud and data centres; the new Executive Strategy Alignment capability | Define three scopes for a company with cloud, SaaS and an on-premises cluster |
| 1.4 The evidence base | Flexera 2026 (29% estimated waste), State of FinOps reports; how survey samples bias results | Critique one headline statistic's sample and wording |

**Check your understanding:** (1) Why is FinOps not the same as cost cutting? (2) Which persona owns usage optimisation, and which owns rate optimisation? (3) What does a 29% "waste" estimate actually measure?

### Chapter 2 · Reading the bill (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Billing data sources | AWS Data Exports (CUR 2.0 and FOCUS), Azure Cost Management exports, Google Cloud billing export to BigQuery | Set up exports on your sandbox accounts |
| 2.2 Cost types | List, unblended, blended, amortised and net costs; credits, refunds, support fees, taxes; currency | Reconcile one month's invoice to the export within 1% |
| 2.3 FOCUS | Columns (BilledCost, EffectiveCost, ListCost, ChargeCategory, ServiceCategory), FOCUS 1.3 additions (shared-resource allocation columns, Contract Commitment dataset, data-completeness flags); AWS FOCUS 1.2 export (November 2025) | Load two providers' exports into one FOCUS table in DuckDB or BigQuery |
| 2.4 SQL for cost | Top-N services, day-over-day deltas, commitment coverage, untagged spend | Write 10 standard cost queries and save them as views |

**Check your understanding:** (1) Why do amortised and unblended cost disagree for a month with an upfront reservation? (2) What problem does FOCUS solve for multi-cloud companies? (3) Why is "untagged spend" a metric worth tracking?

### Chapter 3 · Allocation (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Structure first | Accounts, subscriptions and projects as allocation boundaries; the CLD301 landing zone revisited | Allocate 100% of a sandbox bill by account alone |
| 3.2 Tags and labels | Tag strategy, activation for billing, tag policies and enforcement in IaC (CLD302 policies) | Raise tag coverage from 40% to 95% with policy and back-fill |
| 3.3 Shared costs | Splitting support, networking, platform and data costs: even, proportional, fixed; what is fair and what is gamed | Split a shared Kubernetes and NAT bill three ways and compare outcomes |
| 3.4 Kubernetes allocation | Requests versus usage, idle cluster cost, OpenCost, AWS split cost allocation with Kubernetes labels (December 2025) | Produce per-team cost from your CLD303 cluster |
| 3.5 Showback and chargeback | Reports teams act on, internal pricing, incentives | Design a monthly showback email a team lead would read |

**Check your understanding:** (1) Why allocate Kubernetes cost by requests rather than usage, and what does that encourage? (2) Who should pay for idle capacity? (3) When does chargeback make behaviour worse?

### Chapter 4 · Unit economics (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Choosing units | Cost per order, per active user, per GB processed, per API call, per million tokens; demand drivers | Pick units for a food-delivery app, a SaaS and an AI chatbot |
| 4.2 Joining cost to business data | Time alignment, allocation keys, marginal versus average cost | Compute cost per order for a demo app from billing and app metrics |
| 4.3 Dashboards that change decisions | AWS Cloud Intelligence Dashboards, Looker Studio, Grafana; AWS Cost Efficiency score (December 2025) | Build a unit-cost dashboard with a target line |

**Check your understanding:** (1) Why can total cost rise while unit cost falls, and which matters? (2) What is the marginal cost of one more order? (3) Why do unit costs mislead when fixed costs dominate?

### Chapter 5 · Rate optimisation (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Commitment instruments | AWS Savings Plans (up to 72% off on-demand) and Reserved Instances, Database Savings Plans (up to 35%, December 2025), Google committed-use discounts (resource-based, spend-based and flexible), Azure reservations and savings plan | Map each instrument to the usage it covers |
| 5.2 Coverage and utilisation | Coverage, utilisation, effective savings rate; break-even utilisation | Compute the effective savings rate of a portfolio |
| 5.3 Commitment strategy | Laddering, terms, payment options, sharing across accounts, risk of over-commitment, timing after migrations | Build a 12-month commitment plan with a downside scenario |
| 5.4 Spot and preemptible | Discounts, AWS's two-minute interruption notice and rebalance signals, Google and Azure's 30-second notices, diversification, Karpenter Spot | Run a batch job on Spot with checkpointing through two interruptions |
| 5.5 Negotiated discounts | Enterprise agreements, private pricing, marketplace commitments; what an engineer contributes to a negotiation | Prepare usage evidence for a renewal |

**Check your understanding:** (1) Why can a 40% discount lose money? (2) Which workloads should never run on Spot? (3) Why buy commitments in ladders instead of all at once?

### Chapter 6 · Usage optimisation (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Rightsizing | Utilisation percentiles, memory metrics, Compute Optimizer and recommenders, Arm migration | Rightsize 10 instances with evidence and no performance regression |
| 6.2 Idle and orphaned resources | Unattached volumes, old snapshots, idle load balancers and NAT gateways (AWS added NAT idle detection in December 2025), forgotten test environments | Write a weekly orphan-finder with safe deletion |
| 6.3 Scheduling | Non-production shutdown schedules, scale-to-zero, ephemeral environments | Cut non-prod compute hours by 65% with schedules |
| 6.4 Storage and data transfer | Lifecycle tiers, compression, log retention, endpoints instead of NAT, CDN offload, cross-AZ chatter | Cut a data-transfer line by 40% with design changes |
| 6.5 Kubernetes efficiency | Requests rightsizing, bin-packing, Karpenter consolidation, VPA recommendations, cluster idle cost | Raise cluster CPU allocation efficiency from 30% to 60% |

**Check your understanding:** (1) Why is p95 utilisation a better rightsizing basis than average? (2) Why do idle resources reappear after every clean-up? (3) Why does over-requesting in Kubernetes waste money even when nodes look busy?

### Chapter 7 · Designing for cost (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Cost as a requirement | Cost budgets per feature, cost in design reviews and ADRs | Add a cost section to a design doc and defend it |
| 7.2 Cost in the pipeline | Infracost in pull requests, cost policies, pre-deployment estimates | Fail a PR that adds an unapproved NAT gateway |
| 7.3 Architectural levers | Caching, batching, async processing, serverless versus containers break-even, multi-AZ and multi-region cost | Redesign one CLD301 P3 component to halve its unit cost |

**Check your understanding:** (1) Why is the cheapest moment to save money before deployment? (2) Which architectural choice usually has the largest cost effect? (3) When is spending more the right cost decision?

### Chapter 8 · Forecasts, budgets and anomalies (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Forecasting | Trend, seasonality, driver-based forecasts, ML forecasts (AWS extended to 18 months in December 2025) | Forecast next quarter from 12 months of data and back-test |
| 8.2 Budgets and actions | Budgets per scope, alerts, automated actions, guardrails for sandboxes | Configure budgets that stop sandbox resources at a threshold |
| 8.3 Anomaly detection | Cost Anomaly Detection, Azure and Google anomaly alerts, thresholds versus statistical detection, routing to owners | Inject a cost spike and time detection to owner notification |

**Check your understanding:** (1) Why do forecasts based only on past spend miss launches? (2) Who should receive an anomaly alert? (3) What is the false-positive cost of anomaly alerts?

### Chapter 9 · The cost of AI workloads (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 GPU economics | On-demand, capacity blocks, commitments and Spot for accelerators; AWS cut P5 on-demand prices by up to 45% in June 2025; utilisation as the dominant variable | Compute cost per training run at 40% versus 80% GPU utilisation |
| 9.2 Managed model APIs | Input, output and cached-token pricing, batch discounts, provisioned throughput; cost per conversation | Model a support bot's monthly cost from traffic and token counts |
| 9.3 Self-hosted inference | Cost per million tokens from GPU-hour price, throughput, batch size and utilisation; quantisation and smaller models | Compare self-hosted and API cost per million tokens across three traffic levels |
| 9.4 AI cost controls | Prompt caching, model routing, context trimming, per-tenant quotas, evaluation so savings do not break quality | Cut a chatbot's token cost by 40% while keeping eval scores within 2% |
| 9.5 Allocating AI spend | Tagging model calls by feature and tenant, FOCUS for AI and SaaS charges | Produce cost per feature for an AI product |

**Check your understanding:** (1) Why is GPU utilisation a bigger lever than GPU price? (2) When does self-hosting beat an API on cost, and what else changes? (3) Why must every AI cost cut be checked with evals?

### Chapter 10 · Running a FinOps practice (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Operating model | Central team versus federated, cadences, KPIs, executive reporting | Design the FinOps operating model for a 300-engineer company |
| 10.2 Tooling | Native tools versus third-party platforms, OpenCost, building your own on FOCUS | Write a build-or-buy decision |
| 10.3 Beyond public cloud | SaaS and licence spend, private cloud, data-centre costs, the 2026 technology-value scope | Add one SaaS bill to your FOCUS dataset |

**Check your understanding:** (1) Why do FinOps teams that only send reports fail? (2) What should a FinOps KPI incentivise? (3) Why include SaaS in cloud cost management?

### Chapter 11 · Cost and carbon (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Carbon tools | AWS Customer Carbon Footprint Tool, Google Cloud Carbon Footprint, Azure Emissions Impact Dashboard; their methods and lags | Pull carbon data for your sandbox and compare with cost |
| 11.2 When cost and carbon agree and conflict | Rightsizing and idle removal help both; region choice may not | Compare cost and carbon for running a batch job in two regions |

**Check your understanding:** (1) Why do carbon reports lag by months? (2) When does a cheaper region increase emissions? (3) What is the most reliable carbon saving?

### Chapter 12 · AI for FinOps (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Natural-language cost analysis | AWS Billing and Cost Management MCP server, Amazon Q cost analysis, Azure Copilot optimisation agent, Gemini Cloud Assist cost features | Ask 20 cost questions to an assistant and check each answer with SQL |
| 12.2 Automated optimisation | Auto-applied recommendations (for example Compute Optimizer automation for EBS, December 2025), guardrails and approvals | Design approval rules for automated rightsizing |

**Check your understanding:** (1) Why must AI cost answers be checked against the raw export? (2) Which optimisations are safe to automate? (3) What should never be auto-applied?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Maturity assessment | Framework map |
| 2 | 2 | Lab 1: exports, reconciliation and FOCUS | Normalised dataset |
| 3 | 3 | Lab 2: tagging and shared-cost split | 95% coverage; P1 starts |
| 4 | 4 | Lab 3: unit-cost dashboard | Cost per order; P1 due |
| 5 | 5 | Lab 4: commitment plan | 12-month plan |
| 6 | 5 | Lab 5: Spot with checkpointing | Interruptions survived; P2 starts |
| 7 | 6 | Lab 6: rightsizing and orphan finder | Measured savings |
| 8 | 7 | Lab 7: cost gate in CI | Blocked PR |
| 9 | 8 | Lab 8: forecast and anomaly drill | Back-test and detection time; P2 due |
| 10 | 9 | Lab 9: GPU and token cost models | Models |
| 11 | 9 | Lab 10: AI cost reduction with evals | 40% saving; P3 starts |
| 12 | 10 | Operating model design | Memo |
| 13 | 11 | Cost and carbon comparison | Analysis |
| 14 | 12 | P3 completion | Board-style presentation |
| 15 | Review and exam | — | Written exam and SQL practical |

## Working with AI in this course

- **Use AI for:** drafting SQL over billing data (then checking it), explaining unfamiliar line items, summarising pricing pages, generating Infracost policies, and writing showback narratives. Named tools: AWS Billing and Cost Management MCP server, Amazon Q Developer, Azure Copilot, Gemini Cloud Assist, Claude Code.
- **Do without AI (drills):** the reconciliation of an invoice to the export, commitment break-even calculations, the GPU and token cost models, and the SQL practical exam.
- **Verify AI output by:** re-running every number with your own SQL on the raw export; checking prices against the provider's pricing page for the exact region; testing optimisation advice in a sandbox with before-and-after measurements; checking AI cost reductions against evaluation scores.
- **Where AI still fails here (show it):** assistants quote list prices for the wrong region or out-of-date prices, confuse amortised and unblended cost, and recommend commitments without considering planned migrations. Ask one "what was our most expensive service last month and why?" and compare with your query; record discrepancies for P3.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Written exam (framework, rates, usage, AI cost) | 15% |
| SQL practical on a real billing export (no AI) | 15% |

**Mastery gate:** you pass when you can, without AI help, (a) take an unseen billing export and, in 90 minutes, produce allocated cost by team, the top five savings opportunities with estimated value, and a commitment recommendation with its downside; (b) compute cost per unit for a product from billing and usage data; and (c) build a cost model for a self-hosted versus API-based LLM feature and state the traffic level where the decision flips.

## Industry reality

FinOps teams now sit in most large cloud users, and the FinOps Foundation offers the FinOps Certified Practitioner credential. In India, start-ups watch runway closely and GCCs report cloud unit costs to global headquarters, so engineers who can explain and change the bill are promoted into architecture and platform leadership. AI spend has become the most scrutinised line item.

Interview questions from this course:

1. **"Our AWS bill grew 40% last quarter. Find out why."** Cover the export and FOCUS view, decomposing by service, account, tag and usage type, separating price from volume, unit cost trends, anomalies, and talking to owners.
2. **"Should we buy a 3-year Savings Plan for our compute?"** Cover baseline usage, coverage and utilisation, laddering, planned migrations and architecture changes, payment options, and the downside scenario.
3. **"How would you allocate the cost of a shared Kubernetes platform to 20 teams?"** Cover requests-based allocation, idle cost, shared services, OpenCost or split cost allocation, and incentives.
4. **"Our LLM feature costs too much. What do you do?"** Cover cost per request breakdown, caching, routing to smaller models, context trimming, batching, self-hosting break-even, quotas, and evals to protect quality.
5. **"How do you stop cost surprises?"** Cover budgets and actions, anomaly detection with routing, cost gates in CI, tagging enforcement, forecasts, and regular reviews.

## Resources (free first)

- **Framework:** [FinOps Framework](https://www.finops.org/framework/), [FinOps Framework 2026 update](https://www.finops.org/insights/2026-finops-framework/), [FOCUS specification](https://focus.finops.org/).
- **Provider docs:** [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html), [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html), [Savings Plans](https://aws.amazon.com/savingsplans/), [Spot interruption notices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-instance-termination-notices.html), [Google Cloud billing export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery), [Google committed use discounts](https://docs.cloud.google.com/docs/cuds), [Azure Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/overview-cost-management).
- **Tools:** [OpenCost](https://www.opencost.io/docs/), [Infracost](https://www.infracost.io/docs/), [Cloud Intelligence Dashboards](https://catalog.workshops.aws/awscid/en-US), [DuckDB](https://duckdb.org/docs/) for local analysis of exports.
- **Reports:** [Flexera 2026 State of the Cloud press release](https://www.flexera.com/about-us/press-center/flexera-finds-cloud-value-is-rising-while-ai-waste-grows); State of FinOps (annual, [data.finops.org](https://data.finops.org/)).
- **Practising without a big bill:** most of this course is analysis. Use the free [FOCUS sample data](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS-Sample-Data), your own sandbox exports, and DuckDB on your laptop; run Spot and rightsizing labs on the smallest instances for minutes at a time.
- **Paid, worth it:** *Cloud FinOps*, 2nd edition (J.R. Storment and Mike Fuller, O'Reilly).

## Sources

All checked 12 Oct 2026.
- [Flexera 2026 State of the Cloud](https://www.flexera.com/about-us/press-center/flexera-finds-cloud-value-is-rising-while-ai-waste-grows) (18 Mar 2026).
- [FinOps Framework 2026 update](https://www.finops.org/insights/2026-finops-framework/) (19 Mar 2026).
- [FOCUS 1.3 launch](https://www.linuxfoundation.org/press/finops-foundation-launches-focus-1.3-to-deepen-cloud-and-saas-billing-transparency-announces-expanded-vendor-support-for-focus-1.2) (ratified 5 Dec 2025); [AWS Data Exports for FOCUS 1.2](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-data-exports-focus-1-2-available) (19 Nov 2025).
- [AWS Cloud Financial Management re:Invent 2025 launches](https://aws.amazon.com/blogs/aws-cloud-financial-management/aws-cloud-financial-management-key-reinvent-2025-launches-to-transform-your-finops-practice/) (10 Dec 2025: Database Savings Plans, Cost Efficiency score, split cost allocation with Kubernetes labels, NAT idle detection, 18-month forecasting, Billing and Cost Management MCP server, Compute Optimizer automation).
- [AWS Savings Plans](https://aws.amazon.com/savingsplans/) (up to 72%).
- [Up to 45% price reduction for EC2 NVIDIA GPU instances](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/) (Jun 2025).
- [Azure Copilot agents](https://azure.microsoft.com/en-us/blog/announcing-azure-copilot-agents-and-ai-infrastructure-innovations/) (optimisation agent, preview).

_Last reviewed: 2026-10_
