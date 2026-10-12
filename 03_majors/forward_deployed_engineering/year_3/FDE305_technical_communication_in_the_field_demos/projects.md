# FDE305 · Labs and projects

Every demo you submit includes its script, a reset procedure for the environment, a list of every mocked or cached component with the disclosure you used, and a recording. Every document you submit states which parts were AI-assisted and how you verified them. Customers are illustrative unless a real organisation agreed in writing.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Audience map and rewrites | Map six audiences for an illustrative deployment; rewrite three chronological emails conclusion-first; cut a vague update by 40% while adding specifics | Audience map, before/after texts with word counts | 3 h |
| 2 · Demo script and environment | Script a five-minute story demo of a system you built (FDE303 or FDE304); build a resettable environment with seeded data | Script, seed and reset scripts, disclosure list | 4 h |
| 3 · Failure-injected rehearsal | Rehearse with a classmate who injects three failures (network, login, wrong AI answer); run your demo prompt 20 times and record variance | Recording, recovery notes, variance log | 3 h |
| 4 · Design doc, ADRs and C4 | Design doc for an earlier integration, five ADRs, C4 context and container diagrams in Mermaid, a review with a resolution log | Documents in a repository, review log | 5 h |
| 5 · Executive summary and honest status | One-page go/no-go summary from a ten-page report; rewrite a misleading green status honestly; design a three-month cadence | Summary, status rewrite, cadence plan | 4 h |
| 6 · Workshops | Run a 90-minute EventStorming session on a real process and two Liberating Structures with six participants; write up within 24 hours | Agenda with defined outputs, photos or board export, report with owners and dates | 6 h |
| 7 · Objection role-plays | Handle ten objections (security, cost, accuracy, jobs, build-it-ourselves) with an observer scoring each step | Scored rubric, three improved responses in writing | 3 h |
| 8 · Explaining evaluation results | Turn an AIE305- or FDE304-style eval report into a one-page explanation for a branch manager using natural frequencies and one honest chart | Explanation, chart, a reader's comprehension check | 3 h |
| 9 · Runbook handoff test | Write a customer runbook; a classmate follows it with no help; fix every point of confusion | Runbook, the classmate's log, revised runbook | 4 h |
| 10 · Timed readout and Q&A | Ten-minute assertion-evidence readout to a panel; five-minute hostile Q&A | Slides, recording, self-assessment against the rubric | 3 h |
| 11 · AI-draft audit | Draft three documents with an assistant from your notes; mark unsupported claims, filler and tone errors; get one translation reviewed by a fluent speaker | Annotated drafts, error counts, translation review | 3 h |

## Projects

### P1 · A demo that survives (L1, ~6 hours)

**Real-world inspiration.** Sarvam AI's early-career FDEs "support pre-sales activities with technical demonstrations"; Anthropic's Applied AI Architects tailor technical content from engineers to executives (2026).

**What to build.** A five-minute demo of a working system you built earlier, aimed at a named illustrative audience (for example, the operations head of a Chennai logistics company). Story-first script, seeded realistic data, resettable environment, offline fallback and a recorded backup.

**Acceptance criteria**
- Delivered live to a panel that injects two failures; you recover from both within 60 seconds each.
- Every mocked or cached component is disclosed during the demo.
- The panel's audience member can state the problem, the new workflow and the result in one sentence each after the demo.
- Environment resets to a clean state with one command in under two minutes.

**Stretch goals.** Run the demo in two languages (for example, English and Hindi) for two audiences.

**What it proves to an employer.** You can show value convincingly and honestly, even when things go wrong.

### P2 · Design document and executive pack for a deployment decision (L2, ~15 hours)

**Real-world inspiration.** Google engineers describe design docs with goals, non-goals and alternatives as the place where design trade-offs are decided (Ubl); OpenAI's Deployment Leads make "complex technical trade-offs legible to business leaders" (2026).

**What to build.** For your FDE304 P2 or P3 deployment (or a provided illustrative case: an AI assistant for a Lucknow-based housing finance company's loan servicing team), produce: a design document with C4 diagrams and at least six ADRs; a one-page executive summary with a recommendation and options; an explanation of evaluation results for front-line managers; and a ten-minute steering-committee deck.

**Acceptance criteria**
- Design doc reviewed by two classmates playing the customer's architect and CISO; every objection resolved or recorded as an open risk.
- Executive summary passes a test: a non-technical reader answers five questions about the decision correctly after two minutes of reading.
- Evaluation explanation uses natural frequencies and states uncertainty; a reviewer finds no misleading statement.
- Deck uses sentence headlines; delivered in ten minutes with five minutes of Q&A, scored on the course rubric.

**Stretch goals.** Write the same summary for two different executives (CFO and Chief Risk Officer) and explain the differences.

**What it proves to an employer.** You can get decisions made by the people who hold the budget and the risk.

### P3 · Run a customer workshop-to-readout cycle (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Palantir's deployment strategists co-create workflows with customers in short pilots (2022); a16z advises services teams to "be there in person" and to "leave a trail" of documentation so others can repeat the work (2025).

**What to build.** With a real organisation (a college department, NGO or small business, with written consent) or an instructor-run simulation with industry mentors: plan and facilitate a two-hour discovery workshop, write it up within 24 hours, run a design review, build or adapt a small working prototype, deliver a demo and a readout to the decision-maker, and leave behind handover documentation organised with Diátaxis.

**Acceptance criteria**
- Workshop agenda with outputs defined in advance; all outputs produced; report sent within 24 hours with owners and dates.
- Design review with at least two stakeholders; resolution log complete.
- Demo with disclosures; readout ends with a recorded decision (proceed, change or stop).
- Handover pack (tutorial, how-to, reference, explanation) tested by someone from the organisation who completes a task using it without help.
- A reflection comparing what you planned to say with what the audience needed, with three changes for next time.

**Stretch goals.** Produce a partner handover guide that another student team uses to repeat the workshop with a different organisation.

**What it proves to an employer.** You can run the human side of a deployment from first workshop to decision to handover.

## Feeds into

- [FDE404 Field Studio](../../year_4/FDE404_field_studio_three_simulated_customer/README.md): every simulated deployment ends with a demo, a readout and a handover.
- [FDE403 Solution Architecture, Pricing and ROI](../../year_4/FDE403_solution_architecture_pricing_and_roi/README.md): business cases and proposals.
- [CAR401 Career Lab II](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): customer role-play and written-communication interview rounds.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): investor and customer pitches.
