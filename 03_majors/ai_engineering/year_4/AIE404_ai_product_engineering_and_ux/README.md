# AIE404 · AI Product Engineering and UX

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L2 → L4 | [AIE304](../../year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md); assumes [AIE305](../../year_3/AIE305_evaluating_llm_systems/README.md) and [FND114](../../../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md) | [OV08 Full-Stack AI Product Engineering](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

## Why this course matters now

An AI feature succeeds when users finish their task faster and trust the result, not when the demo impresses. The public record shows both outcomes. Klarna announced in February 2024 that its AI assistant handled 2.3 million conversations in its first month, doing "the equivalent work of 700 full-time agents" (company claim). In May 2025 its CEO said Klarna was hiring human support staff again because the AI service had given "lower quality". In India, Meesho's voice bot handled about 60,000 calls a day in English and Hindi and cut per-call cost by 75% (TechCrunch, Nov 2024). In Moffatt v. Air Canada (2024), a tribunal held an airline liable for its chatbot's wrong advice. Product teams now iterate on live behaviour too: Cursor retrained its Tab completion model with online reinforcement learning on user accept and reject signals. The new model made 21% fewer suggestions with a 28% higher accept rate (Sept 2025). AI can generate interfaces, copy and even product specs. The work that stays human is choosing problems where AI output can be checked cheaply, designing for an assistant that is sometimes wrong, measuring value honestly, and deciding what ships.

## Learning outcomes

By the end you can:

1. **Select** AI product opportunities using frequency, pain, error tolerance and verification cost, and **kill** ideas that fail the test.
2. **Design** interaction patterns for probabilistic output (expectation setting, correction, dismissal, scoping when uncertain) using the Microsoft HAX guidelines and Google's People + AI Guidebook.
3. **Build** latency-aware interfaces: streaming text and structured data, progress for agents, background tasks, fast and deep modes.
4. **Implement** generative UI and tool-result rendering (Vercel AI SDK, AG-UI or MCP Apps) that stays accessible.
5. **Design** human-in-the-loop flows (draft → review → act; approvals; escalation with context) that avoid approval fatigue.
6. **Design** trust and error UX: citations, provenance, uncertainty, undo, AI disclosure, refusal handling.
7. **Define** and **measure** value with task success, time saved, quality-adjusted resolution and cost per outcome, using experiments with holdouts.
8. **Build** a feedback flywheel (explicit and implicit signals) that respects consent and avoids self-reinforcing errors.
9. **Ship** an AI feature through dogfood, beta and staged rollout with a launch checklist, and **run** the post-launch review.

## Chapters and lessons

### Chapter 1 · Choosing problems AI should solve (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Jobs, not features | Jobs-to-be-done; frequency × pain; where current workarounds cost time or money | Interview three users about one workflow; map their job steps |
| 1.2 The verification test | Who checks the output, how long it takes, what an error costs; tasks where checking is cheaper than doing | Score 10 AI ideas on error cost and verification cost; plot them |
| 1.3 Mandates vs problems | "AI-first" memos (Shopify, Apr 2025; Duolingo, Apr 2025) and the risk of solution-first products | Rewrite one mandate-driven idea as a problem statement with a success metric |
| 1.4 Public-good examples | Jugalbandi: a WhatsApp bot built with AI4Bharat speech models, Bhashini translation and Azure OpenAI to explain government schemes (Microsoft, 2023) | Analyse its scope choices: 10 languages and 171 schemes at the time of the report |

**Check your understanding:** Why is "AI writes the first draft, a human approves" sometimes slower than no AI? Which kinds of errors make an AI feature unshippable regardless of average quality? What would make you kill a feature after a successful demo?

### Chapter 2 · Designing for probabilistic output (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Human–AI interaction guidelines | Amershi et al.'s 18 guidelines (CHI 2019): make clear what the system can do and how well; support efficient correction and dismissal; scope services when in doubt | Audit a shipped AI product against all 18 guidelines |
| 2.2 Mental models | Onboarding, examples of good requests, capability boundaries; Google PAIR People + AI Guidebook | Write onboarding for an assistant that sets accurate expectations |
| 2.3 Error states | Wrong answer, partial answer, refusal, timeout, tool failure; each needs a designed state | Design and prototype screens for five error states |
| 2.4 Overreliance | Automation bias; designs that keep users thinking (show sources, ask for confirmation of key facts) | Run a small study: does showing sources change acceptance of wrong answers? |

**Check your understanding:** Why should an assistant sometimes do less when it is unsure? How do you design a refusal that does not feel like a dead end? What signals would show users are over-trusting the system?

### Chapter 3 · Latency-aware UX (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Response-time limits | 0.1 s feels instant, 1 s keeps flow, 10 s is the limit of attention (Nielsen) | Classify your product's interactions by these limits |
| 3.2 Streaming and skeletons | Time to first useful token; streaming partial structure; skeleton states | Compare perceived wait for blocking vs streaming in a 10-person test |
| 3.3 Agent progress | Plans, step lists, live tool activity, interruptibility, background runs with notifications | Design progress UI for a 3-minute research agent |
| 3.4 Fast and deep modes | Small model first, escalate to reasoning model on request; latency/quality tiers | Implement a "quick answer / think longer" toggle; measure usage |

**Check your understanding:** Why can a slower answer with visible progress feel faster than a quicker silent one? When should an agent run in the background instead of in the chat? What is the cost of letting users interrupt an agent mid-run?

### Chapter 4 · Streaming and generative UI implementation (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Transport | Server-Sent Events (WHATWG HTML), chunked responses, reconnection, back-pressure | Implement SSE streaming end to end with reconnection |
| 4.2 AI SDK patterns | Vercel AI SDK streaming and chat hooks, message parts, tool-call rendering | Build a chat UI that renders tool calls as cards |
| 4.3 Generative UI | Model-selected components with typed props; MCP Apps for inline UI; AG-UI event streams | Let the model render a booking form or comparison table as a component |
| 4.4 Accessible streaming | `aria-live` regions, focus management, reduced motion, screen-reader-friendly updates (WCAG) | Test your UI with a screen reader; fix three issues |

**Check your understanding:** What breaks when a stream drops halfway through a JSON component? Why should generated components come from a fixed, typed library? How does constant streaming text affect screen-reader users?

### Chapter 5 · Human-in-the-loop design (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Autonomy levels | Suggest → draft → act with approval → act and report; matching level to risk | Assign autonomy levels to 10 actions in a CRM assistant |
| 5.2 Approval UX | Showing diffs and consequences, batching, remembering safe decisions, avoiding fatigue | Prototype an approval screen; measure decision time and errors |
| 5.3 Escalation | Handing off to a human with full context, warm transfer, SLA for humans | Design the handoff payload and the agent-side UI |
| 5.4 Review queues | Sampling AI actions for review, reviewer tools, feedback into evals | Build a review queue that feeds labels into your eval set |

**Check your understanding:** Why do people approve dangerous actions after many safe ones, and how do you design against it? What must a human agent see when a bot escalates? Which actions should never be automated?

### Chapter 6 · Trust, transparency and error UX (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Citations and provenance | Inline citations, quote highlighting, source freshness, "verified" vs "generated" content | Add verifiable citations to an answer UI; test whether users click them |
| 6.2 Uncertainty | Showing confidence without fake precision; abstention messages; asking clarifying questions | Compare three uncertainty designs in a user test |
| 6.3 Undo and reversibility | Undo windows, drafts, soft deletes, confirmation for irreversible actions | Add undo to every agent action in your prototype |
| 6.4 Disclosure and liability | Telling users they are talking to AI (EU AI Act Article 50 transparency duties from Aug 2026); Moffatt v. Air Canada; terms and policies | Write disclosure copy and a policy-answer design that links to authoritative pages |

**Check your understanding:** Why does a confident tone increase the harm of a wrong answer? What did the Air Canada decision mean for chatbot product design? When do citations create false trust?

### Chapter 7 · Conversational and voice UX for India (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Language and script | Code-mixed Hinglish, transliteration, answering in the user's script, Bhashini and AI4Bharat models | Build and test a bilingual flow with 8 users |
| 7.2 Voice-first | Speech recognition errors, confirmations, turn-taking, call costs (Meesho's voice bot) | Prototype a voice flow; log recognition errors by accent |
| 7.3 Channels | WhatsApp and SMS constraints, low bandwidth, feature phones, IVR integration | Design one flow for WhatsApp and one for IVR |
| 7.4 Inclusive design | Low literacy, older users, accessibility; testing with real users, not personas | Run a usability session with two users outside your peer group |

**Check your understanding:** Why is a confirmation step more important in voice than in text? What changes when your users pay for data by the megabyte? How would you test a Tamil flow if no one on your team speaks Tamil?

### Chapter 8 · Measuring value (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Metric design | Task success, time to complete, quality-adjusted resolution, cost per outcome; guardrail metrics | Write a metric spec with exact definitions and denominators |
| 8.2 Deflection is not resolution | Vendor resolution rates can count "assumed" resolutions (Intercom Fin reports 76% average, company claim); repeat contacts; Klarna's 2025 reversal | Recompute a resolution rate with repeat-contact and CSAT adjustments on a sample dataset |
| 8.3 Experiments | A/B tests with long-term holdouts; novelty effects; network effects in support queues | Design an experiment for a support assistant with a 4-week holdout |
| 8.4 Productivity claims | A Copilot RCT found a coding task done 55.8% faster (Peng et al., 2023); a METR RCT found experienced developers 19% slower on their own repositories (2025); why both can be true | Write a one-page critique comparing the two study designs |

**Check your understanding:** Why can "70% of chats handled by AI" coexist with falling customer satisfaction? What does a long-term holdout protect against? Which metric would you refuse to report without a quality adjustment?

### Chapter 9 · Learning from usage (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Signals | Explicit (ratings, reports) vs implicit (accepts, edits, copy, abandon, retry) | Instrument five implicit signals; check which correlate with judged quality |
| 9.2 The flywheel | Turning signals into eval cases, prompt fixes, routing changes and training data; Cursor's online RL for Tab (2025) | Build a pipeline that turns weekly rejects into eval cases |
| 9.3 Consent and privacy | Using customer data for improvement: consent, opt-outs, DPDP purpose limitation, enterprise contracts | Write the data-use section of your product's privacy notice |
| 9.4 Feedback loops | Self-reinforcing errors, popularity bias, Goodhart's law on accept rate | Identify one way optimising accept rate could hurt users |

**Check your understanding:** Why is "accepted" not the same as "correct"? What must you tell users before training on their interactions? How would you detect that your flywheel is amplifying a bias?

### Chapter 10 · Pricing and unit economics (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Cost structure | Inference, retrieval, tools, human review and support costs per task | Build the cost-per-task model for your P2 product |
| 10.2 Pricing models | Seat, usage, credit and outcome-based pricing; heavy users and margin risk | Model margins for three pricing schemes under realistic usage distributions |
| 10.3 Abuse and limits | Free-tier abuse, scraping, spend caps, fair-use policies (link to [AIE403](../AIE403_llmops_observability_guardrails_cost_and_latency/README.md)) | Design limits that stop abuse without hurting the top 5% of honest users |
| 10.4 Selling value to buyers | ROI cases for enterprise buyers, procurement questions (data handling, SLAs, audit), pilot-to-contract success metrics | Write a one-page ROI case for your P2 product aimed at an Indian mid-size company |

**Check your understanding:** Why can usage-based pricing make customers use your product less? What happens to margins when a model price drops 80%? Who pays for human review in an outcome-priced product?

### Chapter 11 · Shipping and iterating (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 The AI product spec | Problem, users, success metrics, eval plan, risks, autonomy level, fallback, rollout plan | Write a spec for your P3 feature and get it reviewed |
| 11.2 Launch readiness | Checklist: evals and thresholds, guardrails, observability, support playbook, kill switch, disclosure, legal review | Run the checklist on your P3; fix every gap |
| 11.3 Staged release | Dogfood, private beta, % rollout, feedback programmes; LinkedIn's "80% in a month, four more months for the rest" (2024) | Plan a 6-week rollout with exit criteria per stage |
| 11.4 Post-launch review | Comparing outcomes with the spec, deciding to iterate, expand or kill | Hold a post-launch review of your P3 with real or simulated data |

**Check your understanding:** What belongs in an AI feature spec that a normal feature spec lacks? Which launch checklist item is most often skipped, and what does it cost later? How do you decide to kill a feature that users like but that loses money?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Opportunity scoring and user interviews | Problem brief |
| 2 | 2 | Lab 2 · HAX audit and error states | — |
| 3 | 3 | Lab 3 · Streaming vs blocking user test | **P1 due** |
| 4 | 4 | Lab 3 (cont.): Generative UI with accessible streaming | — |
| 5 | 5 | Lab 4 · Approval and escalation flows | — |
| 6 | 6 | Lab 5 · Citations, uncertainty and undo | Mid-term (AI off): design critique |
| 7 | 7 | Lab 6 · Bilingual and voice prototype | — |
| 8 | 8 | Lab 7 · Metric spec and resolution recompute | — |
| 9 | 8 | Lab 7 (cont.): experiment design | **P2 due** |
| 10 | 9 | Lab 8 · Feedback flywheel | — |
| 11 | 10 | Lab 9 · Unit economics and pricing model | — |
| 12 | 11 | Lab 10 · Spec and launch checklist | — |
| 13 | 11 | Lab 10 (cont.): staged rollout plan | Rollout plan |
| 14 | Integration | P3 demo day with real users | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating UI prototypes (v0, Claude, ChatGPT or Cursor), drafting copy and onboarding text, synthesising interview notes, generating test scenarios, building analytics queries.
- **Do without AI (drills):** run user interviews and usability sessions yourself; write metric definitions with denominators; critique an AI product's UX against the HAX guidelines in a timed exercise; build the unit-economics model by hand; write the launch decision memo.
- **Verify AI output by:** testing generated UIs with real users and a screen reader; checking generated copy against legal and policy text; recomputing any metric an assistant reports from raw events; comparing synthesised interview themes with your own notes.
- **Where AI still fails here (show it):** AI-generated personas and interview summaries invent plausible needs that real users never mentioned (compare with transcripts); generated UIs often ignore error, empty and slow states (count missing states in Lab 2); assistants report vendor resolution rates as if they were measured outcomes (correct one in Lab 7).

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Problem brief, metric spec and launch memo | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can: (1) take an ambiguous business request, interview users and deliver a problem brief, an AI feature spec with an eval plan and a working prototype within one week; (2) run a usability test with at least five real users and show the changes it caused; (3) define and compute a quality-adjusted value metric and a cost per outcome, and make a written ship / iterate / kill decision that a reviewer can check from your data.

## Industry reality

The pattern across public AI products is fast adoption followed by hard lessons about quality and trust. Klarna's 2024 automation claims and its 2025 return to human support are a well-documented case. Intercom markets Fin's average resolution rate (76%, company claim, undated), and its own documentation explains that some resolutions are "assumed" when the customer leaves. Indian companies report large cost effects in support: Meesho's voice bot (Nov 2024), and Zomato's Nugget platform (Feb 2025), which Zomato says resolves up to 80% of queries autonomously (company claim). Human–AI design guidance from Microsoft (HAX) and Google (PAIR) remains the reference for interaction design, and EU transparency duties for AI interactions apply from August 2026. Learning from usage at scale is now a product capability, as Cursor's online RL for Tab shows.

**Interview questions from this course**

1. *Our support bot "handles" 70% of chats, yet CSAT fell. What do you do?* Strong answer: separate handled, resolved and assumed-resolved; measure repeat contacts and escalations; segment by intent; sample transcripts; add escalation paths and quality-adjusted metrics; test changes against a holdout.
2. *Design the UX for an agent that books travel for employees.* Strong answer: capability onboarding; plan preview; streaming progress; approvals before payment with a clear diff; policy checks; undo windows; escalation to a human; receipts and audit trail; error states.
3. *How do you decide whether an AI feature is worth building?* Strong answer: frequency and pain of the job, error cost, verification cost, data availability, a baseline, a success metric agreed before building, unit economics, and a cheap prototype test.
4. *How would you show uncertainty to users?* Strong answer: avoid fake percentages; use citations, "I'm not sure" with next steps, clarifying questions, abstention; test designs with users for over- and under-trust.
5. *Should we use user interactions to improve the model?* Strong answer: consent and purpose limitation under DPDP and contracts; implicit vs explicit signals and their biases; turn signals into evals first; guard against feedback loops; opt-outs and retention.

## Resources (free first)

- **Human–AI interaction:** Microsoft, Guidelines for Human-AI Interaction — https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/ ; HAX Toolkit — https://www.microsoft.com/en-us/haxtoolkit/ ; Google PAIR People + AI Guidebook — https://pair.withgoogle.com/guidebook/ ; Nielsen Norman Group, response-time limits — https://www.nngroup.com/articles/response-times-3-important-limits/
- **Building:** Vercel AI SDK streaming — https://ai-sdk.dev/docs/foundations/streaming ; generative UI — https://ai-sdk.dev/docs/ai-sdk-ui/generative-user-interfaces ; Server-Sent Events (WHATWG) — https://html.spec.whatwg.org/multipage/server-sent-events.html ; AG-UI — https://docs.ag-ui.com/introduction ; MCP Apps — https://modelcontextprotocol.io/extensions/apps/overview ; MDN `aria-live` — https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-live ; WCAG — https://www.w3.org/WAI/standards-guidelines/wcag/
- **India:** Bhashini — https://bhashini.gov.in/ ; AI4Bharat — https://ai4bharat.iitm.ac.in/
- **Product practice:** "What We've Learned From A Year of Building with LLMs" — https://applied-llms.org/ ; Hamel Husain, "A Field Guide to Rapidly Improving AI Products" — https://hamel.dev/blog/posts/field-guide/ ; SVPG articles on product discovery — https://www.svpg.com/
- **Regulation:** EU AI Act Article 50 (transparency) — https://artificialintelligenceact.eu/article/50/

## Sources

- Klarna press release (27 Feb 2024; company claims) — https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ ; Entrepreneur, "Klarna CEO Reverses Course…" (9 May 2025) — https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 (checked 2026-10)
- TechCrunch, "AI helps India's Meesho cut customer call costs by 75%" (26 Nov 2024) — https://techcrunch.com/2024/11/26/ai-helps-indias-meesho-cut-customer-call-costs-by-75/ ; People Matters, Zomato Nugget (Feb 2025; company claims) — https://www.peoplematters.in/news/ai-and-emerging-tech/zomato-introduces-nugget-an-in-house-ai-enabled-customer-support-platform-44412 (checked 2026-10)
- CTV News on Moffatt v. Air Canada, 2024 BCCRT 149 (Feb 2024) — https://www.ctvnews.ca/vancouver/article/air-canadas-chatbot-gave-a-bc-man-the-wrong-information-now-the-airline-has-to-pay-for-the-mistake/ (checked 2026-10)
- Cursor, "Improving Cursor Tab with online RL" (12 Sept 2025) — https://cursor.com/blog/tab-rl (checked 2026-10)
- Fin.ai (average resolution rate 76%, company claim, undated) — https://fin.ai/ ; Intercom Help, Fin outcomes (confirmed vs assumed resolutions) — https://www.intercom.com/help/en/articles/8205718 (checked 2026-10)
- Amershi et al., "Guidelines for Human-AI Interaction" (CHI 2019) — https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/ ; Google PAIR Guidebook — https://pair.withgoogle.com/guidebook/ (checked 2026-10)
- Peng et al., "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot" (2023) — https://arxiv.org/abs/2302.06590 ; METR, early-2025 experienced developer study (Jul 2025) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ (checked 2026-10)
- Digital Commerce 360 on Shopify's AI memo (Apr 2025) — https://www.digitalcommerce360.com/2025/04/08/internal-memo-shopify-ceo-declares-ai-non-optional/ ; Duolingo all-hands email posted on LinkedIn (28 Apr 2025) — https://www.linkedin.com/posts/duolingo_below-is-an-all-hands-email-from-our-activity-7322560534824865792-l9vh/ (checked 2026-10)
- Microsoft, Jugalbandi feature (May 2023) — https://news.microsoft.com/source/asia/features/with-help-from-next-generation-ai-indian-villagers-gain-easier-access-to-government-services/ (checked 2026-10)
- LinkedIn Engineering, "Musings on building a Generative AI product" (Apr 2024) — https://www.linkedin.com/blog/engineering/generative-ai/musings-on-building-a-generative-ai-product (checked 2026-10)
- EU AI Act Article 50 and Commission timeline (transparency obligations from Aug 2026) — https://artificialintelligenceact.eu/article/50/ and https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai (checked 2026-10)

_Last reviewed: 2026-10_
