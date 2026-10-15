# OV08 · Full-Stack AI Product Engineering

| Composed of | Overlap courses | Typical entry majors | Market pages |
|---|---|---|---|
| [FE403](../../03_majors/frontend_engineering/year_4/FE403_ai_native_interfaces_streaming_generative_ui/README.md) × [BE403](../../03_majors/backend_engineering/year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md) × [AIE404](../../03_majors/ai_engineering/year_4/AIE404_ai_product_engineering_and_ux/README.md) | [OV08A](OV08A_shipping_ai_features_end_to_end/README.md), [OV08B](OV08B_product_analytics_and_growth_for_ai_apps/README.md) | FE, BE, AIE, SWE, FDE, MOB | [AIE](../../06_career_and_market_readiness/01_market_map/roles/AIE_ai_engineering.md) · [FE](../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md) · [BE](../../06_career_and_market_readiness/01_market_map/roles/BE_backend_engineering.md) · [FDE](../../06_career_and_market_readiness/01_market_map/roles/FDE_forward_deployed_engineering.md) |

## The job this overlap maps to

Most AI value reaches people as a feature inside a product: a support assistant, a search box that answers, a drafting tool, an agent that files a form. The engineer who builds it end to end owns the interface, the backend, the model calls, the evaluation, the release and the numbers that say whether it worked.

Common titles: **AI Product Engineer**, **Product Engineer (AI)**, **Full-Stack AI Engineer**, **Applied AI Engineer**, **Founding Engineer** at AI start-ups, and **Growth Engineer** on AI products. Forward-deployed engineers do the same work inside customer organisations ([FDE major](../../03_majors/forward_deployed_engineering/README.md)).

Day to day:

- turning a vague request ("add AI to onboarding") into a spec with users, success metrics, an evaluation plan and a fallback;
- building the vertical slice: streaming UI, API, retrieval, model and tool calls, persistence;
- gating releases on evaluations, rolling out behind flags, watching traces, cost and quality;
- instrumenting usage, running experiments, and deciding to iterate, expand or remove the feature.

**Demand evidence (checked October 2026; figures from this university's [market map](../../06_career_and_market_readiness/01_market_map/README.md)).**

- Mentions of generative AI skills in US AI job postings grew 111% from 2024 to 2025, and postings referencing AI agents rose sharply ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)).
- More than 1.1 million public GitHub repositories import an LLM SDK, and new ones rose 178% in a year ([Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)).
- Organisational AI adoption reached 88%, but agent deployment was "in the single digits across nearly all business functions" ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)). The gap between trying AI and shipping it is this role's work (**analysis**).
- Software and applications developers, and UI and UX designers, are among the fastest-growing jobs employers expect to 2030 ([WEF Future of Jobs 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).
- On 12 October 2026, OpenAI listed 66 and Anthropic 47 roles with "Applied AI" in the title, including India-based roles ([AIE role page](../../06_career_and_market_readiness/01_market_map/roles/AIE_ai_engineering.md)). This is a one-day snapshot of two employers, not a trend.

No official statistics count "AI product engineers" separately.

## Why the overlap exists

Each composing course owns one layer well:

| Course | Owns | Typical gap when taken alone |
|---|---|---|
| [FE403](../../03_majors/frontend_engineering/year_4/FE403_ai_native_interfaces_streaming_generative_ui/README.md) | Streaming UIs, generative UI, agent UX, safe rendering, on-device AI in the browser | What the backend must guarantee; how to measure the feature |
| [BE403](../../03_majors/backend_engineering/year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md) | Model APIs, gateways, vector search, cost control, long jobs | What the user sees when things fail; product metrics |
| [AIE404](../../03_majors/ai_engineering/year_4/AIE404_ai_product_engineering_and_ux/README.md) | Problem choice, human–AI interaction, trust, value measurement, pricing | Building and operating the whole stack |

AI features fail at the joins: a schema change in a tool breaks the UI mid-stream; a model upgrade passes offline evals and drops conversion; a cost spike comes from one tenant's retry loop; nobody can connect a user's thumbs-down to the trace that produced the answer. The overlap teaches the joins: contracts, tests, evaluations as release gates, end-to-end tracing, rollouts ([OV08A](OV08A_shipping_ai_features_end_to_end/README.md)), and then the measurement and growth discipline that decides what to build next ([OV08B](OV08B_product_analytics_and_growth_for_ai_apps/README.md)).

## Composed courses and sequencing

From [`catalog.json`](../../catalog.json): OV08A and OV08B require [FE302](../../03_majors/frontend_engineering/year_3/FE302_react_and_component_architecture/README.md), [BE301](../../03_majors/backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md) and [AIE302](../../03_majors/ai_engineering/year_3/AIE302_prompt_and_context_engineering/README.md), and list FE403, BE403 and AIE404 as co-requisites. All three composing courses run in semester 8. OV08A (semester 7) therefore builds a working vertical slice with "just enough" of each layer; the semester-8 courses then take each layer deeper while OV08B adds measurement on top of the same product.

| Semester | Prerequisites and composing courses | Overlap course | Notes |
|---|---|---|---|
| 5 (Y3) | FE302, BE301, AIE302 (take the two outside your major as electives) | — | [FE301](../../03_majors/frontend_engineering/year_3/FE301_modern_javascript_and_typescript_in_depth/README.md) helps non-FE majors |
| 6 (Y3) | Recommended: [AIE304](../../03_majors/ai_engineering/year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md), [AIE305](../../03_majors/ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md), [BE304](../../03_majors/backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md) | — | AIE305's eval methods are used from week 7 of OV08A |
| 7 (Y4) | — | **OV08A** Shipping AI Features End to End | Builds the product used in OV08B |
| 8 (Y4) | FE403, BE403, AIE404 (pick at least two) | **OV08B** Product Analytics and Growth for AI Apps | Mobile students pair with [MOB404](../../03_majors/mobile_engineering/year_4/MOB404_mobile_analytics_experimentation_and_growth/README.md) |
| 9–10 (Y5) | [THS501](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) or [LCH502](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) | Capstone below | Natural founder path |

Taking all three semester-8 courses alongside OV08B is heavy (four courses on one product). Most students take two of them and audit the third's chapters that their OV08B work touches.

## The two overlap courses

| Course | Semester | What it adds | Projects |
|---|---|---|---|
| [OV08A · Shipping AI Features End to End](OV08A_shipping_ai_features_end_to_end/README.md) | 7 | Specs with eval plans, typed contracts across the stack, streaming vertical slices, permission-aware retrieval, testing with recorded model responses, evals as release gates, flags and canaries, browser-to-model tracing, cost budgets, on-call for AI features | [labs and projects](OV08A_shipping_ai_features_end_to_end/projects.md) |
| [OV08B · Product Analytics and Growth for AI Apps](OV08B_product_analytics_and_growth_for_ai_apps/README.md) | 8 | Tracking plans, AI-specific signals linked to traces, funnels and retention, production quality measurement, experiments on prompts and models, growth loops, unit economics, privacy-safe attribution, decision memos | [labs and projects](OV08B_product_analytics_and_growth_for_ai_apps/projects.md) |

## Capstone brief: ship an AI feature to real users and prove its value

**Scenario.** Choose a real problem for real users you can reach (a college department, a small business, an NGO, an open-source community), for example multilingual answers over a department's notices, or a drafting assistant for a shop's catalogue. Build, launch and measure one AI feature for at least eight weeks.

**Acceptance criteria:**

- **Users:** at least 30 external users with consent, of whom at least 10 are weekly active in the final four weeks; retention curve reported with its cohort sizes.
- **Spec:** a one-page spec written before building, with a success metric, a guardrail metric, an evaluation plan and a fallback; the final report compares outcomes with it.
- **Quality gate:** an offline evaluation suite of at least 150 cases runs in CI; any change that drops the primary score by more than 2 points (with a paired confidence interval excluding zero) blocks the merge, demonstrated on a planted regression.
- **Performance:** p95 time to first token under 1.5 s and p95 full response under 8 s at the observed peak load, from production traces.
- **Traceability:** 100% of AI requests carry one trace ID from the browser through the backend to model and tool spans; any user feedback event can be joined to its trace in under one minute.
- **Cost:** cost per successful task is tracked daily per feature; a budget alert and a kill switch are both demonstrated.
- **Experiment:** one controlled experiment (prompt, model, or UX change) with a pre-registered metric, a sample-ratio-mismatch check, and a written decision; a null result is acceptable if reported honestly.
- **Safety and law:** output sanitised before rendering (zero findings from a provided injection test set); analytics consent and notices follow the DPDP Act's itemised-notice model; accessibility of the main flow passes automated checks with zero serious issues and a manual screen-reader walkthrough.
- **Operations:** one incident drill (provider outage or quality regression) with a written post-incident review.

## Roles it leads to

| Role | What you would own | Entry route from this overlap |
|---|---|---|
| AI Product Engineer / Product Engineer (AI) | AI features end to end, from spec to metrics | Capstone + OV08A P3 |
| Full-Stack AI Engineer | Streaming UIs, backends for AI, evals and releases | FE or BE major + OV08 |
| Founding Engineer (AI start-up) | The whole product, early users, analytics | Capstone + [LCH502](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |
| Growth or Experimentation Engineer (AI products) | Instrumentation, experiments, activation and retention | OV08B P3; [DSC304](../../03_majors/data_science/year_3/DSC304_experimental_design_and_causal_inference/README.md) as an elective |
| Forward Deployed Engineer | Shipping AI tools inside customer organisations | FDE major + OV08 |
| Design Engineer (AI interfaces) | Interaction design and implementation of AI UX | FE major + OV08 |

## Sources

All checked October 2026, via this university's market map and role pages unless linked directly.

- Stanford HAI, *AI Index Report 2026*. https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- GitHub, *Octoverse 2025*. https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- World Economic Forum, *Future of Jobs Report 2025*. https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- OpenAI and Anthropic careers pages (snapshot 12 Oct 2026), as recorded in the [AIE role page](../../06_career_and_market_readiness/01_market_map/roles/AIE_ai_engineering.md).

_Last reviewed: 2026-10_
