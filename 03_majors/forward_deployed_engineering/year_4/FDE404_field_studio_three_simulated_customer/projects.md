# FDE404 · Labs and projects

The three team deployments described in the [syllabus](README.md) are the core of this course. The labs below are short drills embedded in the deployment weeks, and the projects are individual work that turns the studio into portfolio evidence. All customers, data and incidents are illustrative and synthetic; no real patient, shipment or banking data is used. Every team keeps a decision log, an AI-use log and an AI-failure log throughout.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Toolkit smoke test | Assemble the team toolkit (playbook templates, connectors, eval harness, diagnostic tool, demo checklist) and run it end to end on a sample brief | Toolkit repository, smoke-test log | 3 h |
| 2 · First-meeting simulation | Run a 30-minute first meeting with a customer actor; leave with a discovery plan and an agreed next step | Meeting notes, discovery plan, actor's feedback | 2 h |
| 3 · FHIR ingestion drill | Pull Patient, Encounter, Observation and MedicationRequest resources incrementally from a HAPI FHIR server; build a patient timeline | Connector, timeline for 20 synthetic patients, reconciliation counts | 3 h |
| 4 · Clinical evaluation session | Run a labelling session with the "clinician" panel on 60 draft summaries; agree error severities | Labelled set, agreement statistic, severity scheme | 3 h |
| 5 · Process-mining sprint | Mine a synthetic shipment event log: exception variants, handling times, hand-offs | Notebook, top variants, time breakdown | 3 h |
| 6 · AI-off integration drill | Build one connector per deployment without AI tools; compare time and defects with the AI-assisted version | Both versions, comparison table | 3 h per deployment |
| 7 · Night-time incident drill | Handle a scripted partner API schema change: detect, mitigate, communicate, postmortem | Timeline, customer updates, postmortem | 3 h |
| 8 · Requirements-to-controls map | Map RBI, FREE-AI, DPDP and CERT-In requirements to controls for the bank before designing | Map with sources, gaps list | 3 h |
| 9 · On-premises model swap | Serve an open-weight model inside the bank replica; rerun the evaluation; compare with the hosted baseline | Eval comparison, latency and capacity note, recommendation | 3 h |
| 10 · Risk committee rehearsal | Rehearse the governance presentation with a panel asking scripted hard questions | Slides, question log, revised answers | 2 h |

## Projects

### P1 · Your personal first-week deployment kit (L1, ~6 hours)

**Real-world inspiration.** OpenAI asks FDEs to "codify working patterns into tools, playbooks, or building blocks"; a16z advises services teams to "leave a trail" and automate the services motion (2025).

**What to build.** Before Deployment A, build your own first-week kit: a qualification and discovery checklist, interview guides by stakeholder type, an environment survey, a data request template, an access request, a pilot charter template, a status-report template and a diagnostic script. Use it in Deployment A and revise it after each deployment.

**Acceptance criteria**
- Every item is used in at least two of the three deployments; a revision log records at least six changes with the reason for each.
- A classmate from another team uses your kit to run a first meeting and rates it on a rubric.
- The diagnostic script catches at least three of the environment problems you met in the studio.

**Stretch goals.** Turn the kit into a small command-line tool that scaffolds a new engagement repository.

**What it proves to an employer.** You have a repeatable method for starting engagements, refined by real use.

### P2 · A reusable component proven across deployments (L2, ~15 hours)

**Real-world inspiration.** Palantir's Deltas decide whether to build into the core platform or deliver something custom (2019); Anthropic asks FDEs to "identify and codify repeatable deployment patterns"; Razorpay asks for a write-up when the same thing is built for "2+ merchants" (2026).

**What to build.** Choose one thing your team built in Deployment A that recurs in B and C (for example, a human-review screen with edit tracking, a reconciliation framework, an evaluation-agreement harness, a redacting support-bundle tool). Generalise it, use it in the later deployments, measure the time saved, and write a field report proposing it as a product feature.

**Acceptance criteria**
- The component is used, by configuration rather than code changes, in at least two deployments.
- Measured build time for its second and third uses is reported against the first, with an honest note on what still needed custom work.
- Tests and documentation good enough that another team adopts it in their Deployment C.
- A field report with evidence from two or more deployments, rated actionable by a panel playing product managers.

**Stretch goals.** Add an extension point for the case that did not fit and show it working on a fourth brief.

**What it proves to an employer.** You turn field work into leverage, the habit that distinguishes senior FDEs.

### P3 · Solo deployment for a fourth customer (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Sarvam AI's FDSEs take "end-to-end ownership of bringing client engagements to success"; Anthropic expects FDEs to "operate autonomously" and "thrive under ambiguity" (2026). Founders who start from services do the same work alone.

**What to build.** In weeks 14–15, alone, deploy for a fourth illustrative customer from a two-page brief, chosen by lot: a district cooperative milk union (procurement payments and farmer queries, Hindi and Marathi), a chain of 30 schools (attendance and parent communication), or a mid-size pharmaceutical distributor (expiry and returns). Run compressed discovery with a customer actor, integrate two systems, deploy one AI workflow with an evaluation agreement and human review, complete a one-page security and data note, demo, and hand over.

**Acceptance criteria**
- Evaluation agreement signed by the customer actor before results; results reported against it.
- Integrations are idempotent and reconciled; SSO or equivalent access control in place.
- A measured outcome on a simulated workload, with the baseline and full cost.
- Demo and readout to the customer actor end with a recorded decision.
- Handover pack tested by one classmate who operates the system for a day without help.
- A public case study (illustrative customer clearly labelled) suitable for a portfolio, with metrics and lessons.

**Stretch goals.** Price the deployment as an offer for ten similar customers and estimate the margin with your P2 component reused.

**What it proves to an employer.** You can run a deployment alone, end to end, which is what early-stage AI companies and your own future company need.

## Feeds into

- [FDE501 Frontier Seminar](../../year_5/FDE501_frontier_seminar_productizing_field_patterns/README.md): field reports and reusable components are the raw material for productising field patterns.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): a deployment case study or a cross-deployment study can become a capstone.
- [CAR401 Career Lab II](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): studio stories answer behavioural and case interviews.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) and the [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/FDE_forward_deployed_engineering.md).
