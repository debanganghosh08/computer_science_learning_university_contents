# OV08B · Product Analytics and Growth for AI Apps

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L2 → L4 | [FE302](../../../03_majors/frontend_engineering/year_3/FE302_react_and_component_architecture/README.md), [BE301](../../../03_majors/backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md), [AIE302](../../../03_majors/ai_engineering/year_3/AIE302_prompt_and_context_engineering/README.md); co-requisites [FE403](../../../03_majors/frontend_engineering/year_4/FE403_ai_native_interfaces_streaming_generative_ui/README.md), [BE403](../../../03_majors/backend_engineering/year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md), [AIE404](../../../03_majors/ai_engineering/year_4/AIE404_ai_product_engineering_and_ux/README.md); [OV08A](../OV08A_shipping_ai_features_end_to_end/README.md) strongly recommended | [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [LCH502](../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

## Why this course matters now

An AI feature can look loved in a demo and still lose users, money or trust in production. AI products add three measurement problems that classic product analytics did not have: the output differs on every request, so quality must be measured, not assumed; every action has a marginal cost in tokens, so a growing heavy-user segment can shrink margins; and the most informative signals (accepting, editing, copying, regenerating, abandoning) live in the interface, not the database. GitHub's study of Copilot users found that the rate at which shown suggestions were accepted, rather than more detailed persistence metrics, best reflected developers' perceived productivity ([Ziegler et al., 2022](https://arxiv.org/abs/2205.06537)), a reminder that choosing the metric is the work. AI tools now write tracking code, SQL for funnels and experiment readouts in seconds; they also count bots as users, peek at experiments daily, mistake correlation for impact and log prompt text into analytics without consent. This course teaches the measurement discipline that makes growth decisions trustworthy. [DSC304](../../../03_majors/data_science/year_3/DSC304_experimental_design_and_causal_inference/README.md) covers causal inference in depth, [AIE404](../../../03_majors/ai_engineering/year_4/AIE404_ai_product_engineering_and_ux/README.md) covers value and pricing models, and [MOB404](../../../03_majors/mobile_engineering/year_4/MOB404_mobile_analytics_experimentation_and_growth/README.md) is the mobile counterpart; this course is the engineer's version for full-stack AI apps.

## Learning outcomes

By the end you can:

1. **Design** a tracking plan with a typed event schema, identity rules and data contracts, and **validate** events in CI.
2. **Instrument** AI-specific signals (accept, edit distance, copy, regenerate, abandon, feedback) and **join** them to model traces without logging prompt content by default.
3. **Model** sessions, funnels, retention and cohorts in a warehouse with tested SQL.
4. **Measure** production quality with sampled human and calibrated automated review, and **report** it alongside engagement.
5. **Run** experiments on prompts, models and UX with correct randomisation units, sample-ratio checks, variance reduction and guardrails for cost and latency.
6. **Analyse** activation and growth loops, and **choose** interventions with expected impact and cost.
7. **Compute** unit economics per cohort (cost to serve, gross margin, heavy-user exposure).
8. **Write** decision memos that state uncertainty honestly and recommend ship, iterate or stop.

## Chapters and lessons

### Chapter 1 · What is different about measuring AI products (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Three new problems | Non-deterministic output, marginal cost per action, quality as a first-class metric | List three decisions in your OV08A product that need data you do not collect yet |
| 1.2 Metric trees | North Star metric, input metrics, guardrails; "successful task" as the unit for AI features | Build a metric tree for your product |
| 1.3 The funnel for AI features | Exposure → first use → successful outcome → repeat use; why "used the AI" is not activation | Define activation for your product with a threshold you can defend |
| 1.4 Reading vendor metrics | Deflection vs resolution; "assumed" resolutions (AIE404 8.2); productivity claims and their study designs | Critique one published AI product metric |

**Check your understanding:** Why is "messages sent" a poor North Star for an AI assistant? Which guardrail would catch a feature that grows usage while hurting outcomes? What would convince you a vendor's resolution rate is real?

### Chapter 2 · Event design and instrumentation (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Tracking plans | Object–action naming, required properties, versions, owners | Write a 25-event tracking plan |
| 2.2 Client vs server events | Ad blockers and loss, server-side confirmation of outcomes, clock skew, duplicates and idempotent event IDs | Measure client event loss against server truth in a test |
| 2.3 Identity | Anonymous to signed-in merging, multiple devices, organisation accounts; bots and internal users | Implement identity stitching and a bot filter; count what it removes |
| 2.4 Tools and contracts | Open-source pipelines (RudderStack, Snowplow) and product analytics (PostHog); schema validation in CI | Block a malformed event in CI |

**Check your understanding:** Which events must be confirmed server-side and why? What happens to retention numbers if identity merging fails? How do internal testers distort an early-stage product's metrics?

### Chapter 3 · AI-specific telemetry (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Implicit signals | Accept, insert, copy, edit distance of accepted output, regenerate, stop, abandon; what each means and does not mean | Instrument five implicit signals |
| 3.2 Explicit feedback | Thumbs with reasons, corrections, reports; low response rates and selection bias | Estimate feedback response rate and who responds |
| 3.3 Joining analytics and traces | Carrying the trace ID into analytics events; sampling; storage cost | Query: retention of users whose first answer was regenerated |
| 3.4 Content and consent | Not logging prompts or outputs into analytics by default; purpose-limited access to content for quality review (DPDP notice and consent) | Write the data-use notice for quality review and implement opt-in |

**Check your understanding:** Why can a high regenerate rate mean both failure and engagement? What bias does voluntary feedback introduce? Who should be allowed to read prompt text, and for what purpose?

### Chapter 4 · Analytics models in the warehouse (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Sessions and activity tables | Sessionisation, daily activity tables, late-arriving events | Build sessions and a daily user activity model in dbt |
| 4.2 Funnels | Ordered steps, time windows, conversion definitions, open vs closed funnels | Funnel from signup to first successful task |
| 4.3 Metric definitions as code | A semantic layer or metrics file so every dashboard computes the same number ([DAN304](../../../03_majors/data_analysis/year_3/DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md)) | Define three metrics once; reuse in two dashboards |
| 4.4 Testing analytics | Uniqueness, freshness, accepted values, reconciliation with production counts | Data tests that catch a planted duplicate-event bug |

**Check your understanding:** Why do two dashboards disagree about weekly active users, and how do you prevent it? What does a 30-minute session timeout assume about your users? Which metric should reconcile with billing?

### Chapter 5 · Retention, cohorts and engagement (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Retention curves | N-day and unbounded retention, cohort tables, flattening curves as a signal of fit | Plot weekly retention by signup cohort |
| 5.2 Engagement depth | DAU/MAU, active-days histograms, power-user distributions | Find your top 10% of users and what they do differently |
| 5.3 Survival analysis | Kaplan–Meier curves for time to churn; censoring | Kaplan–Meier by first-week experience |
| 5.4 Correlation traps | "Users who use feature X retain better" and self-selection | Rewrite three misleading retention claims honestly |

**Check your understanding:** Why does a flattening retention curve matter more than its starting height? What is censoring and why does ignoring it bias churn estimates? How would you test whether feature X causes retention?

### Chapter 6 · Measuring AI quality in production (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Sampling for review | Stratified samples by intent, language and user segment; reviewer guidelines | Design a weekly 200-item review sample |
| 6.2 Automated quality scores | LLM judges calibrated against human labels ([AIE305](../../../03_majors/ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md)); drift in the judge itself | Calibrate a judge on 100 production samples |
| 6.3 Quality and engagement together | Quality by cohort; does better quality predict retention in your data | Join quality scores to retention; report the association with caveats |
| 6.4 Closing the loop | Production failures to eval cases to fixes (OV08A); tracking time to fix | Add 20 production failures to the eval set |

**Check your understanding:** Why must the review sample be stratified? What would make your judge's scores drift over a month? Why is a quality–retention correlation not proof that quality drives retention?

### Chapter 7 · Experiments on AI features (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The essentials | Randomisation unit, assignment, exposure logging, pre-registered primary metric (DSC304 for depth) | Pre-register an experiment on your product |
| 7.2 Trustworthiness checks | Sample ratio mismatch (Fabijan et al., 2019), A/A tests, Twyman's law | Detect a planted SRM caused by a redirect bug |
| 7.3 Sensitivity | CUPED variance reduction (Deng et al., 2013); power for small products | Apply CUPED; report the variance reduction |
| 7.4 Peeking and sequential tests | Why daily peeking inflates false positives; always-valid inference (Johari et al., 2017) | Simulate peeking; then use a sequential method |
| 7.5 Prompt and model experiments | Extra variance from sampling; guardrails on cost, latency and refusals; interleaving for ranking changes (Chapelle et al., 2012) | Run a prompt A/B with cost and latency guardrails |
| 7.6 Long-term effects | Holdouts, novelty and learning effects | Design a 6-week holdout for a major feature |

**Check your understanding:** Why randomise by user rather than by request for an assistant? Your model experiment wins on engagement but costs 40% more per task: how do you decide? What does an SRM tell you about the experiment's results?

### Chapter 8 · Growth loops and activation (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Loops vs funnels | Acquisition loops: content, collaboration and sharing, referral, integrations | Map your product's one plausible loop and its leak points |
| 8.2 Onboarding to first value | Examples, templates, pre-filled prompts, empty states; time to first successful task | Cut time to first success in a usability test |
| 8.3 Content and search | AI-generated pages and Google's "scaled content abuse" spam policy (Mar 2024) | Review a content-growth idea against the policy |
| 8.4 Lifecycle messaging | Triggered emails or notifications on value moments; frequency caps; consent | Design two triggered messages with a holdout |

**Check your understanding:** Why does an AI product's growth loop often depend on outputs users share? What makes generated pages a risk rather than a loop? How do you measure whether a message caused a return visit?

### Chapter 9 · Unit economics of AI products (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Cost to serve | Inference, retrieval, tools and human review per user and per cohort, from traces | Cost-to-serve table per cohort |
| 9.2 Heavy users and margins | Cost distribution tails; plans and limits that protect margins without punishing value | Simulate margin under three limit policies |
| 9.3 Pricing measurement | Willingness to pay surveys and their limits; price experiments and their ethics and legal limits | Design a fair pricing test or explain why not to run one |
| 9.4 Payback | Acquisition cost, retention and margin combined; sensitivity analysis | Payback model with best, base and worst cases |

**Check your understanding:** Why can growth make an AI product less profitable? What does a fair usage limit look like to a user? Which unit-economics input is least certain in your model?

### Chapter 10 · Attribution and privacy (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Attribution basics | UTM parameters, first and last touch, multi-touch and their bias | Attribute signups three ways and compare |
| 10.2 Platform limits | Apple's App Tracking Transparency (iOS 14.5, 2021) and aggregated attribution; consent banners | Explain what attribution you lose on iOS without consent |
| 10.3 Lawful analytics | DPDP itemised notice and purpose limits; GDPR and ePrivacy consent for non-essential tracking; dark-pattern rules ([OV07B](../../../04_overlaps/OV07_privacy_engineering/OV07B_data_protection_law_for_engineers_in_practice/README.md)) | Audit your analytics for purpose and consent |
| 10.4 Privacy-preserving measurement | Aggregation thresholds, cohort-level reporting, differential privacy for published metrics ([OV07A](../../../04_overlaps/OV07_privacy_engineering/OV07A_privacy_by_design_and_privacy_enhancing/README.md)) | Publish one public usage statistic with thresholds |

**Check your understanding:** Why does last-touch attribution overvalue search ads? What tracking is allowed before consent? When is a public growth number a privacy risk?

### Chapter 11 · Causal questions without a clean experiment (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 When you cannot randomise | Launches to everyone, pricing changes, outages | List three decisions in your product that could not be A/B tested |
| 11.2 Before–after with controls | Difference-in-differences, synthetic control (DSC304 for depth) | Estimate a launch's effect with a comparison group |
| 11.3 Natural experiments | Outages and staggered rollouts as accidental experiments | Use a provider outage to estimate the feature's value |
| 11.4 Goodhart's law | Optimising acceptance rate or time-in-app until it stops meaning value | Propose a counter-metric for your primary metric |

**Check your understanding:** What assumption does difference-in-differences make, and how would you check it? Why is an outage informative? How would you know your metric had been gamed?

### Chapter 12 · Decisions and communication (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Experiment readouts | Effect sizes with intervals, guardrails, segments with multiplicity caution, decision | Write a one-page readout |
| 12.2 Dashboards people use | Few metrics, definitions linked, annotations for releases and incidents | Redesign a cluttered dashboard |
| 12.3 Decision logs | Ship, iterate or stop; what would change the decision | Decision log for your product's last four weeks |
| 12.4 Capstone review | Present P3 to a panel acting as founder, data lead and privacy lead | Defend your numbers |

**Check your understanding:** What belongs in the first sentence of a readout? When should a positive but uncertain result not ship? Which of your metrics would a sceptical investor challenge first?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Metric tree | Metric tree and activation definition |
| 2 | 2 | Lab 2 · Tracking plan and event CI | — |
| 3 | 3 | Lab 3 · AI signals joined to traces | **P1 due** |
| 4 | 4 | Lab 4 · dbt models and data tests | — |
| 5 | 5 | Lab 5 · Retention and survival (no AI) | Retention report |
| 6 | 6 | Lab 6 · Production quality review | Mid-term (AI off) |
| 7 | 7 | Lab 7 · SRM and CUPED | — |
| 8 | 7 | Lab 7 (cont.) · Sequential and prompt experiments | Pre-registration |
| 9 | 8 | Lab 8 · Onboarding experiment | **P2 due** |
| 10 | 9 | Lab 9 · Unit economics | Cost-to-serve model |
| 11 | 10 | Lab 10 · Consent and attribution audit | Audit report |
| 12 | 11 | Natural-experiment analysis | Causal memo |
| 13 | 12 | Readouts and dashboards | — |
| 14 | 12 | Panel review | **P3 due** |
| 15 | Review | Oral defence | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** drafting tracking plans and dbt models; writing SQL for funnels and cohorts (then testing it); generating synthetic event data for labs; summarising qualitative feedback into themes you verify by reading samples; first drafts of readouts. Tools: Claude, ChatGPT, Gemini; coding agents for dbt and instrumentation code; AI features inside PostHog and other analytics tools.
- **Do without AI (drills):** retention and survival analysis in Lab 5; the power and sample-size calculation for every experiment; the mid-term and final; the final recommendation in each readout.
- **Verify AI output by:** reconciling every AI-written metric query with a hand-computed count on a small sample; checking that queries exclude bots and internal users; checking the randomisation unit and SRM before reading results; asking for, and checking, the exact definition behind every number in an AI-drafted summary; reading 20 raw items behind any AI-generated theme.
- **Where AI still fails here (collect your own evidence):** log every AI-written analysis error you catch (double-counted users, wrong time windows, peeking, causal claims from correlations, prompt text written into analytics). The log is part of P3.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 40% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 25% |

**Mastery gate.** You pass when you can, with AI tools off: (1) given a raw event table, compute activation, 4-week retention by cohort and a funnel, matching the key within 1%; (2) given an experiment's data, detect whether it is trustworthy (SRM, exposure bugs, peeking), estimate the effect with an interval, and make a defensible call including cost guardrails; (3) write a one-page decision memo a reviewer accepts as honest about uncertainty.

## Industry reality

Product analytics and experimentation are standard at consumer and SaaS companies; Microsoft's experimentation group has published widely on trustworthy experiments, including the sample-ratio-mismatch taxonomy and CUPED. For AI products, GitHub's Copilot research tied acceptance rate to perceived productivity (2022), and AIE404 documents how vendor resolution rates can include assumed resolutions. Google's spam policies since March 2024 treat mass-produced pages made to manipulate rankings as "scaled content abuse", whoever or whatever wrote them, which limits one tempting AI growth tactic. In India, analytics also has to respect DPDP notice and purpose rules from May 2027 (see [OV07](../../OV07_privacy_engineering/README.md)).

**Interview questions from this course**

1. *Define activation for an AI writing assistant.* Strong answer: tied to a successful outcome (accepted or exported draft with limited edits) within a time window; validated against later retention; with a guardrail on quality.
2. *Our prompt experiment shows +4% engagement. Ship it?* Strong answer: checks SRM, exposure logging, randomisation unit, peeking; looks at cost, latency and quality guardrails; considers novelty; reports interval; decides with a holdout if uncertain.
3. *How would you measure answer quality in production without reading everyone's chats?* Strong answer: consent and purpose limits, stratified sampling, calibrated judge, human review of a small sample, aggregates only for most staff, retention limits.
4. *Users who use the AI feature retain 2× better. Is the feature working?* Strong answer: self-selection; proposes an experiment, a holdout or a staggered rollout analysis; checks pre-period behaviour.
5. *Our costs grow faster than revenue. What analysis do you run?* Strong answer: cost to serve by cohort and plan, tail of heavy users, cost per successful task, cache and routing opportunities, limit and pricing options with simulated margin impact.

## Resources (free first)

- **Experimentation:** Microsoft ExP papers (CUPED, SRM and more) — https://exp-platform.com/ ; Deng et al., CUPED (WSDM 2013) — https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf ; Johari et al., Always Valid Inference — https://arxiv.org/abs/1512.04922
- **AI product metrics:** Ziegler et al., Productivity Assessment of Neural Code Completion — https://arxiv.org/abs/2205.06537
- **Tools:** PostHog docs — https://posthog.com/docs ; GrowthBook docs — https://docs.growthbook.io/ ; RudderStack — https://github.com/rudderlabs/rudder-server ; Snowplow docs — https://docs.snowplow.io/ ; dbt docs — https://docs.getdbt.com/
- **Policies:** Google Search spam policies update (Mar 2024) — https://developers.google.com/search/blog/2024/03/core-update-spam-policies ; Apple User Privacy and Data Use — https://developer.apple.com/app-store/user-privacy-and-data-use/
- **Paid, optional:** Kohavi, Tang and Xu, *Trustworthy Online Controlled Experiments* (Cambridge, 2020) — https://experimentguide.com/ ; the free papers above cover the core methods.

## Sources

All checked October 2026.

- Ziegler et al., "Productivity Assessment of Neural Code Completion" (MAPS 2022) — https://arxiv.org/abs/2205.06537
- Deng, Xu, Kohavi and Walker, CUPED (WSDM 2013) — https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf
- Fabijan et al., "Diagnosing Sample Ratio Mismatch in Online Controlled Experiments" (KDD 2019) — https://dl.acm.org/doi/10.1145/3292500.3330722
- Johari, Pekelis and Walsh, "Always Valid Inference" (2015; KDD 2017 version "Peeking at A/B Tests") — https://arxiv.org/abs/1512.04922
- Chapelle, Joachims, Radlinski and Yue, "Large-scale validation and analysis of interleaved search evaluation" (ACM TOIS, 2012)
- Google Search Central, March 2024 core update and spam policies (5 Mar 2024) — https://developers.google.com/search/blog/2024/03/core-update-spam-policies
- Apple, User Privacy and Data Use (App Tracking Transparency) — https://developer.apple.com/app-store/user-privacy-and-data-use/
- Vendor resolution-rate caveats: see the sources of [AIE404](../../../03_majors/ai_engineering/year_4/AIE404_ai_product_engineering_and_ux/README.md)

_Last reviewed: 2026-10_
