# AIE404 · Labs and projects

Every lab and project involves real people: interview notes, usability-session recordings (with consent) or anonymised summaries, and decisions traced to evidence. Deliverables combine working software with product artefacts: briefs, specs, metric definitions and launch memos. If you collect user data, follow the course's consent template and India's DPDP principles (notice, purpose, minimisation, deletion).

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Opportunity scoring and user interviews | Interview three users about one workflow; score 10 AI ideas on frequency, pain, error cost and verification cost | Interview notes, scored opportunity map, one chosen problem | 4 h |
| 2 · HAX audit and error states | Audit a shipped AI product against the 18 Human-AI Interaction guidelines; design five error states for your product | Audit table with screenshots; prototypes of the error states | 4 h |
| 3 · Streaming UX and accessible generative UI | Run a 10-person test of blocking vs streaming; build a chat UI that renders tool calls and model-selected components; fix three screen-reader issues | Test results; code; accessibility checklist | 7 h |
| 4 · Approval and escalation flows | Assign autonomy levels to 10 actions; prototype an approval screen and a human-handoff payload | Decision-time and error measurements; handoff spec | 4 h |
| 5 · Citations, uncertainty and undo | Add verifiable citations, three uncertainty designs and undo for every agent action; test which designs change over-trust | User-test results; chosen designs | 5 h |
| 6 · Bilingual and voice prototype | Build a Hindi/English (or another Indian language) flow and a voice flow; log recognition errors | Prototype, error log by accent and language, design changes | 5 h |
| 7 · Metric spec, resolution recompute and experiment design | Define five metrics with denominators; recompute a "resolution rate" with repeat-contact and CSAT adjustments; plan an A/B test with a 4-week holdout | Metric spec, recomputation notebook, experiment plan with power analysis | 6 h |
| 8 · Feedback flywheel | Instrument five implicit signals; check which correlate with judged quality; route weekly rejects into eval cases | Correlation table, pipeline code, privacy-notice section | 4 h |
| 9 · Unit economics and pricing | Build cost per task (inference, retrieval, tools, human review); model margins under three pricing schemes and realistic usage | Spreadsheet, recommendation | 3 h |
| 10 · Spec, launch checklist and rollout plan | Write the AI feature spec for P3; run the launch checklist; plan a 6-week staged rollout with exit criteria | Reviewed spec, checklist with gaps fixed, rollout plan | 5 h |

## Projects

### P1 · Problem brief and a streaming prototype (L1, ~6 hours)

**Real-world inspiration.** Jugalbandi, built with AI4Bharat speech models, Bhashini translation and Azure OpenAI, scoped itself to explaining government schemes over WhatsApp: 10 of 22 official languages and 171 schemes at the time Microsoft reported it (2023). A narrow, verifiable scope made it workable.

**What to build.** A two-page problem brief for an AI feature serving an Indian user group you can reach (students, shopkeepers, clinic staff, farmers through a family member), based on at least three interviews. Add a clickable or working streaming prototype of the core interaction, including its main error state.

**Acceptance criteria**
- The brief states the job, the current workaround and its cost, the error cost, who verifies output and how long that takes, and one success metric with a target.
- At least three interview notes support the brief, with quotes.
- The prototype streams the first useful content within 1 s (measured) and has a designed error state.
- Two users try the prototype; the brief lists what changed because of them.

**Stretch goals.** A voice or WhatsApp variant of the same interaction.

**What it proves to an employer.** You start from users and verification cost, not from the model, which is the most common gap in AI teams.

### P2 · A human-in-the-loop assistant people trust appropriately (L2, ~15 hours)

**Real-world inspiration.** Moffatt v. Air Canada (2024) showed that confident wrong answers carry liability. Klarna's 2024 automation claims and its 2025 return to human support show that volume metrics can hide quality problems. Microsoft's HAX guidelines and Google's PAIR guidebook describe how to design for systems that are sometimes wrong. The domain below is illustrative.

**What to build.** An assistant for a support team at a mid-size Indian e-commerce or travel company that drafts replies and proposes actions (refund, rebook, escalate) from policy documents and order data (mock). Agents review drafts, see citations and uncertainty, approve or edit actions, and escalate with full context. Include undo windows, AI disclosure for the end customer and error states.

**Acceptance criteria**
- Usability test with at least 6 participants playing support agents on 10 scripted cases each; report task time, error rate and approval accuracy compared with a no-AI baseline.
- Over-trust check: on 3 planted wrong drafts per participant, the share accepted without edits is measured and reduced by a design change you test.
- Every proposed action shows its policy citation; irreversible actions require an explicit confirmation showing the consequence.
- Escalations carry the conversation, the draft and the reason; a human agent can act without re-asking the customer.
- Accessibility: passes keyboard-only and screen-reader checks on the core flow.

**Stretch goals.** A "think longer" mode with a reasoning model and a measurement of when agents use it.

**What it proves to an employer.** You can design AI that speeds people up without making them careless, and prove it with user data.

### P3 · Ship an AI feature to real users and decide its future (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Meesho's voice bot handled about 60,000 calls a day and cut per-call cost by 75% (TechCrunch, Nov 2024). Cursor improved its Tab model with online reinforcement learning on user signals, making 21% fewer suggestions with a 28% higher accept rate (Sept 2025). LinkedIn reported reaching 80% of its target experience in one month, then spending four more months trying to pass 95% (2024). Real products are decided by real usage.

**What to build.** Take P1 or P2 (or a new problem) to at least 20 real users outside your course for at least two weeks. Ship it through a staged rollout with a launch checklist (evals, guardrails, observability, support playbook, kill switch, disclosure). Instrument quality-adjusted value metrics and cost per outcome. Run one controlled experiment (A/B or before/after with a holdout). Build a feedback flywheel that turns user signals into eval cases. End with a written ship / iterate / kill decision.

**Acceptance criteria**
- At least 20 active users and 2 weeks of usage data, collected with consent and deletable on request.
- The metric spec defines every metric with numerator and denominator; the headline value metric is quality-adjusted (for example resolved without repeat contact, or accepted without major edit).
- One experiment with a pre-registered hypothesis, sample-size reasoning, and a result reported with a CI (a null result is acceptable if reported honestly).
- Unit economics: cost per successful outcome and the price or budget at which the feature breaks even.
- At least 25 eval cases added from real usage, and one improvement shipped because of them with before/after numbers.
- A post-launch review memo (≤ 2 pages) that a reviewer can check against your data.

**Stretch goals.** A second language; an outcome-based pricing experiment; a public case study.

**What it proves to an employer.** You have shipped an AI product to real people, measured whether it helped, and made a decision with evidence. Founders, product engineers and forward-deployed engineers all need this.

## Feeds into

- [OV08A Shipping AI Features End to End](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08A_shipping_ai_features_end_to_end/README.md) and [OV08B Product Analytics and Growth for AI Apps](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08B_product_analytics_and_growth_for_ai_apps/README.md): P3 is the natural starting point.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): the brief, metrics and launch memo become a founder's evidence pack.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): human–AI interaction studies make strong capstones.

## Sources

- Microsoft, Jugalbandi feature (May 2023) — https://news.microsoft.com/source/asia/features/with-help-from-next-generation-ai-indian-villagers-gain-easier-access-to-government-services/ (checked 2026-10)
- CTV News on Moffatt v. Air Canada (Feb 2024) — https://www.ctvnews.ca/vancouver/article/air-canadas-chatbot-gave-a-bc-man-the-wrong-information-now-the-airline-has-to-pay-for-the-mistake/ ; Klarna press release (Feb 2024) — https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ ; Entrepreneur on Klarna (May 2025) — https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 (checked 2026-10)
- Microsoft HAX guidelines — https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/ ; Google PAIR Guidebook — https://pair.withgoogle.com/guidebook/ (checked 2026-10)
- TechCrunch on Meesho (Nov 2024) — https://techcrunch.com/2024/11/26/ai-helps-indias-meesho-cut-customer-call-costs-by-75/ ; Cursor, "Improving Cursor Tab with online RL" (Sept 2025) — https://cursor.com/blog/tab-rl ; LinkedIn Engineering (Apr 2024) — https://www.linkedin.com/blog/engineering/generative-ai/musings-on-building-a-generative-ai-product (checked 2026-10)
