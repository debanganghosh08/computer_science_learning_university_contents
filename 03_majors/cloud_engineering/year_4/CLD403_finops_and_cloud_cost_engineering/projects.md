# CLD403 · Labs and projects

Analysis labs use billing exports from your own sandbox accounts plus the public [FOCUS sample data](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS-Sample-Data), loaded into DuckDB on your laptop or BigQuery's free tier. Optimisation labs change real resources in a sandbox for short, measured windows. Lab 1's reconciliation, Lab 4's break-even maths and Lab 9's cost models are done without AI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Exports, reconciliation and FOCUS (no AI) | Enable exports on two providers; reconcile a month's invoice to the export within 1%; normalise both to FOCUS columns in one table | SQL, reconciliation table, FOCUS view definition | 6 h |
| 2 · Tagging and shared costs | Raise tag coverage from a seeded 40% to 95% with tag policies and IaC; split a shared NAT and platform bill three ways | Coverage before/after, three split methods compared, recommendation | 4 h |
| 3 · Unit-cost dashboard | Join billing to app metrics (orders per hour) for a demo app; dashboard cost per order with a target | Dashboard export, SQL, one insight with action | 4 h |
| 4 · Commitment plan (break-even by hand) | From 12 months of usage, design a laddered Savings Plan or CUD portfolio; compute break-even utilisation and a downside case | Plan, effective savings rate and downside scenario | 4 h |
| 5 · Spot with checkpointing | Run a 2-hour batch job on Spot or Spot VMs with checkpoints; survive two interruptions (simulated with fault injection where available) | Completion evidence, cost versus on-demand | 3 h |
| 6 · Rightsizing and orphans | Rightsize 10 seeded instances using p95 metrics; write a weekly orphan-finder (volumes, snapshots, idle load balancers, idle NAT) with safe, tagged deletion | Savings measured, performance check, script | 5 h |
| 7 · Cost gate in CI | Infracost on PRs with a policy that blocks unapproved hourly network resources and changes over a monthly threshold | A blocked PR and an approved one | 3 h |
| 8 · Forecasts and anomalies | Back-test a driver-based forecast against 3 months; inject a cost spike and measure time to owner notification | Forecast error table, detection timeline | 4 h |
| 9 · AI cost models (no AI) | Cost per training run at two utilisation levels; cost per million tokens for self-hosted inference versus a managed API at three traffic levels | Spreadsheet models with stated assumptions and the crossover point | 4 h |
| 10 · AI cost reduction with evals | Cut a chatbot's token cost by caching, routing and context trimming while keeping eval scores within 2% | Before/after cost per conversation and eval results | 5 h |

## Projects

### P1 · Cost visibility for a start-up in one week (L1, ~6 hours)

**Real-world inspiration:** Flexera's 2026 survey reports managing cloud spend as a top challenge for 85% of respondents ([Flexera](https://www.flexera.com/about-us/press-center/flexera-finds-cloud-value-is-rising-while-ai-waste-grows)); most start-ups begin with no allocation at all. The company is an *illustrative scenario*: a Bengaluru SaaS start-up with one AWS account and runway of 14 months.

**What to build:** from a provided (or your own) export: a FOCUS-normalised dataset, cost by service and environment, a tagging plan with enforcement code, a budget with alerts, and a one-page "where the money goes" note for the founders.

**Acceptance criteria:**
- The FOCUS view reconciles to the invoice within 1%.
- The founders' note fits on one page and names the top three cost drivers and one action each with estimated monthly saving.
- Tag enforcement is in IaC and blocks an untagged resource in a test.
- **Cost ceiling:** US$0 (analysis plus free-tier budgets).

**Stretch goals:** unit cost per active customer; a Slack or email weekly digest.

**What it proves to an employer:** you can make cost visible fast, which is the first FinOps deliverable anywhere.

### P2 · Optimise a real workload and prove the savings (L2, ~15 hours)

**Real-world inspiration:** Swiggy reported Graviton-based Kubernetes nodes costing 10% less than its x86 nodes ([Swiggy Bytes](https://bytes.swiggy.com/how-swiggy-migrated-its-k8s-workload-to-graviton-d2643bbc7871)); AWS's December 2025 launches added Kubernetes-label cost allocation and NAT idle detection ([AWS](https://aws.amazon.com/blogs/aws-cloud-financial-management/aws-cloud-financial-management-key-reinvent-2025-launches-to-transform-your-finops-practice/)).

**What to build:** take your CLD303 P2 or CLD301 P3 workload, run it for a baseline period under a scripted load, then apply a set of optimisations: rightsizing, Arm nodes, Karpenter consolidation or bin-packing, Spot for tolerant components, endpoints instead of NAT, storage lifecycle and log retention. Allocate the cluster cost per team with OpenCost or split cost allocation.

**Acceptance criteria:**
- Cost per 1,000 requests falls by at least 30% against the baseline under the same load.
- p99 latency and error rate stay within agreed limits (no more than 10% latency increase, no error increase).
- Every saving is attributed to a specific change with before/after data.
- Per-team allocation covers 100% of cluster cost, including idle, with the method documented.
- **Cost ceiling:** US$25.

**Stretch goals:** a commitment recommendation for the optimised baseline; carbon comparison before/after.

**What it proves to an employer:** you deliver measured savings without breaking production, the core of cloud cost engineering roles.

### P3 · Unit economics and cost controls for an AI product (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:**
- Flexera ties 2026's rise in estimated waste to AI workloads.
- The FinOps Foundation's 2026 framework expands scope to SaaS and other technology categories ([FinOps Foundation](https://www.finops.org/insights/2026-finops-framework/)).
- India's IndiaAI compute portal offers subsidised GPUs below ₹100 an hour, which changes the self-hosting maths for eligible teams ([PIB, February 2026](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc2026210784401.pdf)).
- The product is an *illustrative scenario*: a multilingual (Hindi, Tamil, English) customer-support assistant sold to Indian D2C brands, priced per conversation.

**What to build:**
- per-tenant and per-feature metering of model tokens, retrieval calls, compute and storage, joined into a FOCUS-style dataset alongside the cloud bill and one SaaS bill;
- a unit-economics model: cost per conversation and gross margin per tenant at three price points;
- cost controls: prompt caching, model routing by difficulty, context trimming, per-tenant quotas and budgets, and anomaly alerts per tenant;
- an evaluation harness so each control's quality impact is measured;
- a self-hosted versus API decision with a crossover chart, including a subsidised-GPU scenario;
- a 12-month forecast with a commitment or provisioned-throughput recommendation.

**Acceptance criteria:**
- **Allocation:** 100% of AI-related spend is attributed to tenant and feature; reconciliation within 3% of the bill for a test week.
- **Savings:** cost per conversation falls by at least 40% from baseline, with evaluation scores (answer accuracy and language quality) within 2% of baseline.
- **Controls:** a runaway tenant (10× normal usage) is detected within 15 minutes and throttled by quota without affecting others.
- **Decision:** the crossover chart shows the monthly conversation volume at which self-hosting becomes cheaper, with GPU utilisation assumptions stated and tested on a short benchmark.
- **Communication:** a 10-slide board-style deck with margin, risks and the commitment recommendation.
- **Cost ceiling:** US$40 including model and GPU usage; use small models and short benchmarks.

**Stretch goals:** FOCUS 1.3 Contract Commitment dataset for your commitments; an assistant connected to your dataset that answers cost questions, with an accuracy audit against SQL.

**What it proves to an employer:** you can make an AI product profitable, which founders, product leaders and FinOps teams all need in 2026.

## Feeds into

- [CLD404 AI Infrastructure](../CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md): GPU utilisation and cost per token in depth.
- [CLD501 Frontier Seminar](../../year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md): carbon-aware and planet-scale cost questions.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): unit economics for your own product.
- [OPS404 Performance and Capacity Engineering](../../../devops_sre_platform_engineering/year_4/OPS404_performance_and_capacity_engineering/README.md): capacity planning as the other half of cost.
