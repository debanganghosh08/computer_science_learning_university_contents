# Flagship industry projects

| Covers | When | Level | Read with |
|---|---|---|---|
| One flagship project per major (20), plus the rules every flagship follows | Year 4, alongside IND401 or THS501; defended in CAR401 and LCH502 | L3 (job-ready) gate, with stretch goals toward L4 and L5 | [Market map](../01_market_map/README.md) · [System design](../03_system_design/) · [AI-driven interviews](../04_ai_driven_interviews/) |

A flagship project is the one piece of work you put in front of every employer. It joins the portfolio-grade (P3) projects of your major into a single system that does something real, is measured, has been broken on purpose and is written up so that a stranger can check every claim. Each major's learning path names its flagship and the course projects that feed it. This page explains what makes such a project worth a hiring panel's time, how panels look at it, how to scope it and how to present it.

## 1. The 20 flagships

| Code | Major | Flagship | Inspired by | Minimum budget |
|---|---|---|---|---|
| CSG | Computer Science | [A verified, fault-tested replicated key-value store, written up as a short paper](CSG_computer_science_general.md) | Raft, TLA+ at AWS, Jepsen, FoundationDB simulation testing | Laptop |
| SWE | Software Engineering | [A surge-proof ticket-booking platform, built with coding agents under review gates](SWE_software_engineering.md) | IRCTC Tatkal openings | Laptop |
| BE | Backend Engineering | [A UPI-style payment switch simulator with idempotency, reconciliation and chaos tests](BE_backend_engineering.md) | UPI and NPCI's 2025 API rules | Laptop |
| FE | Frontend Engineering | [A fast, accessible, multilingual food-label PWA with an evaluated AI assistant](FE_frontend_engineering.md) | Open Food Facts; low-end phones on patchy networks | Laptop, free hosting |
| MOB | Mobile Engineering | [An offline-first trader's ledger and price app for low-end Android, shipped to real testers](MOB_mobile_engineering.md) | Digital ledger apps; Agmarknet mandi prices | Laptop, one low-end phone |
| CLD | Cloud Engineering | [A regulated fintech's cloud foundation, built as code, with DR, residency and unit costs](CLD_cloud_engineering.md) | RBI payment-data localisation, CERT-In log rules | ≤ ₹4,000 cloud spend |
| OPS | DevOps, SRE, Platform | [Operate a microservices shop like an SRE team: SLOs, GitOps, game days, an AI ops assistant](OPS_devops_sre_platform_engineering.md) | OpenTelemetry Demo; CrowdStrike and Cloudflare config incidents | Laptop (16 GB) |
| SEC | Cybersecurity Defense | [A home SOC for an illustrative regulated company, detections mapped to ATT&CK](SEC_cybersecurity_defense.md) | CERT-In, DPDP and RBI reporting duties | Laptop, free tenants |
| OFF | Ethical Hacking (Authorized) | [Secure rebuild of a vulnerable-by-design app: threat model, secure code review, verified fixes](OFF_ethical_hacking_offensive_security.md) | OWASP Juice Shop, ASVS 5.0 | Laptop |
| SAR | Security Architecture | [A security architecture dossier and zero-trust reference slice for an agent-enabled fintech](SAR_security_architecture.md) | NIST SP 800-207, FIPS 203–205 | Laptop |
| DAN | Data Analysis | [The analytics function of a marketplace, from raw tables to a board decision](DAN_data_analysis.md) | Olist public marketplace data | Laptop |
| DSC | Data Science | [An air-quality decision system: probabilistic forecasts, a causal evaluation, a monitored service](DSC_data_science.md) | Delhi-NCR's GRAP, CPCB data via OpenAQ | Laptop |
| DEN | Data Engineering | [A real-time mobility and payments lakehouse on public data, with contracts and erasure](DEN_data_engineering.md) | NYC TLC, Wikimedia EventStreams, DPDP | Laptop (16 GB) |
| MLE | ML Engineering | [A production ETA service: leak-free evaluation, canary, drift monitoring, retraining](MLE_machine_learning_engineering.md) | Uber DeepETA, Swiggy delivery-time posts | Laptop |
| DLR | Deep Learning | [A small Hindi maths-reasoning model: SFT, RL with verifiable rewards, efficiency pass, model card](DLR_deep_learning.md) | DeepSeekMath GRPO, modded-nanoGPT | Free GPU quotas, ≤ ₹5,000 |
| AIE | AI Engineering | [A durable, evaluated payments-support agent platform with permission-aware retrieval](AIE_ai_engineering.md) | τ-bench, MCP, RBI failed-transaction rules | ≤ ₹3,000 API spend |
| FDE | Forward Deployed | [A simulated (or real, consented) enterprise deployment of an AI invoice workflow](FDE_forward_deployed_engineering.md) | ERPNext; FDE roles at AI companies | Laptop, ≤ ₹2,000 API spend |
| EMB | Embedded and IoT | [A battery-powered cold-chain sensor fleet with secure A/B OTA and on-device anomaly detection](EMB_embedded_systems_iot.md) | India's eVIN temperature-logger network | ≤ ₹6,000 hardware |
| QAE | Quality Engineering | [A quality programme for a real open-source application, with upstream bug reports](QAE_software_quality_test_engineering.md) | Google's testing practice; ERPNext | Laptop |
| NET | IT Infrastructure and Networking | [Network-as-code for a multi-branch enterprise with pre-change verification and live BGP monitoring](NET_it_infrastructure_networking.md) | Meta's October 2021 outage; RIPE RIS | Laptop (16 GB) |

## 2. What makes a project hiring-grade in the AI era

AI assistants now produce boilerplate, CRUD endpoints, simple UI components and first-draft tests at almost no cost, so a project made of those things no longer separates candidates (see the [market map, §4 and §8](../01_market_map/README.md)). What employers still pay for is the part AI does unreliably: deciding what to build, designing for failure, verifying output and operating something real. The evidence:

- Canva's AI-assisted interviews evaluate how candidates break down ambiguous problems, when they use AI, and "Can they identify and fix issues in AI-generated code?" ([Canva, Jun 2025](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)).
- 48.0% of developers trust AI output only when they can easily verify it ([Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data)).
- In Veracode's tests of over 100 models, AI-generated code "introduced risky security flaws in 45% of tests" ([Veracode, updated Oct 2025](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/)).
- AI adoption is positively related to delivery throughput but still negatively related to delivery stability ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)).

A hiring-grade project therefore has eight properties:

| Property | What it looks like | The weak version |
|---|---|---|
| **Real users or real data** | Public datasets with a known licence, live public streams, a real organisation that consented, or real testers on a store track | Lorem ipsum, a 50-row CSV, invented "users" |
| **Measurable outcomes** | A small table of numbers with method: p99 latency at a stated load, an eval score with a confidence interval, cost per 1,000 requests, battery life measured over days | "Fast", "scalable", "accurate" |
| **Production concerns** | Tests (unit, property, integration), CI that blocks merges, structured logs, metrics and traces, threat model and secrets handling, a cost budget | One happy-path script; secrets in the repo |
| **Failure as a feature** | Faults injected on purpose (timeouts, duplicates, crashes, bad config, bad data) with the observed behaviour and a fix | "It works on my machine" |
| **Written thinking** | A design doc, numbered architecture decision records (ADRs), at least one postmortem of something that really broke | Code with no explanation of why |
| **Honest AI-use notes** | An `AI_USE.md` that says what was generated, what you wrote, and how you verified both | Silence, or pretending nothing was generated |
| **Reproducibility** | One command to run, pinned versions, seeds, data download scripts, recorded hardware | "Install these 14 things first" |
| **A demo and a write-up** | A two-minute video and a 1,500–2,500-word write-up with the numbers and trade-offs | A screenshot gallery |

## 3. How projects are evaluated

Little is published about how hiring panels score portfolios, so this section separates the two kinds of evidence.

**What is published.** Some employers require AI in interviews and grade whether you can find and fix problems in its output (Canva, above). Others ban it: Anthropic's take-home assessments are done without AI unless stated, and live interviews are "all you–no AI assistance unless we indicate otherwise" ([Anthropic](https://www.anthropic.com/candidate-ai-guidance)). Both mean the same thing for a flagship: you must be able to explain and change every important line of it without help. The market map's summary of what a strong 2026 candidate shows (fundamentals, verification, decomposition, system thinking, production ownership, communication, evidence) is the checklist your flagship should satisfy ([market map, §7](../01_market_map/README.md#7-what-hiring-managers-now-screen-for)).

**Practitioner guidance (not measured).** Projects tend to be looked at in three passes:

| Pass | Who | Time | What they look at | What ends it early |
|---|---|---|---|---|
| Skim | Recruiter or hiring manager | Under a minute | Title, the one-line problem, a headline number, a demo link, a recognisable domain | No README, a tutorial name ("Netflix clone"), no outcome |
| Look | Screening engineer | About five minutes | README, architecture diagram, test and CI status, commit history, one or two core files, `AI_USE.md` | Broken build, giant single commit, no tests on the hard part, obviously generated code nobody trimmed |
| Deep dive | Interview panel | 30–60 minutes | Your design decisions, failure cases, what you would change, live changes to the code | You cannot explain a design choice, a number or a line in the core module |

Questions a panel is likely to ask about any flagship (prepare written answers):

1. What was the hardest correctness problem, and how do you know it is solved?
2. Which number on your README are you least sure of, and why?
3. What broke during the project, and what did you change afterwards?
4. Which design decision would you reverse with hindsight?
5. Where did AI help, where did it mislead you, and how did you catch it?
6. What happens at 10 times the load, or when a dependency is down for an hour?
7. What does it cost to run per month, and per unit of work?
8. What would a security reviewer flag first?
9. If you had two more weeks, what would you build and what would you delete?
10. Walk us through this file. (They choose the file.)

## 4. Scoping: MVP, v1, scale-up

Every flagship page has the same three tiers.

| Tier | Time | Goal | Rule |
|---|---|---|---|
| **MVP** | 2–3 weeks | One complete path through the system, end to end, with tests and one measured number | Thin and complete beats wide and half-built |
| **v1** | 6–8 weeks in total | All acceptance criteria met, failure tests passing, design doc, ADRs, demo and write-up | This is the L3 deliverable |
| **Scale-up** | Open-ended | One or two stretch goals that move toward L4 (design others build on, unplanned failures) or L5 (a new measurement or method) | Pick depth over breadth |

Scoping rules that hold across majors:

- **Start from the acceptance criteria.** Write the tests and measurement scripts for the MVP before the features.
- **Keep a cut list.** Write down what you decided not to build and why; it becomes part of the write-up.
- **One hard thing, done properly.** A payment switch that reconciles under faults beats a payment switch plus chat plus admin panel that do not.
- **Freeze the stack in week 1.** Record it in ADR-001. Changing it later needs its own ADR.
- **Budget time for writing.** Plan at least 20% of v1 for the design doc, ADRs, write-up and demo.
- **Stop at v1 if you are job-hunting.** A finished v1 is worth more than an unfinished scale-up.

## 5. Presenting it

### 5.1 Repository layout

```
README.md            problem, result, demo, how to run, numbers
docs/design.md       design doc (context, goals, non-goals, design, alternatives, risks)
docs/adr/            0001-record-architecture-decisions.md, 0002-..., one decision each
docs/postmortems/    at least one real incident from the project
docs/architecture.md diagrams as code (Mermaid or C4)
AI_USE.md            what AI produced, what you wrote, how you verified
bench/ or evals/     load tests, eval sets and the scripts that produce every number
.github/workflows/   CI: lint, tests, security scans, the gates you claim
LICENSE              your code licence; data licences listed in README
```

### 5.2 README template

```markdown
# <Project name>: <one line saying what it does for whom>

**Result:** <the one number that matters, with conditions> · **Demo:** <2-minute video link> · **Write-up:** <link>

## Problem
Two or three sentences. Who has this problem, and what is hard about it.

## What it does
The main path in five bullets. What is simulated, what is real.

## Architecture
<diagram> One paragraph on the key design choice; link to docs/design.md and the ADRs.

## Results
| Metric | Target | Measured | Method |
|---|---|---|---|
| p99 latency at 500 rps | ≤ 300 ms | 212 ms | bench/k6/steady.js, laptop spec in bench/HW.md |

## Failure testing
What you broke, what happened, what you fixed (link to postmortems).

## Run it
One command. Expected output. Hardware tested on.

## Data and licences
Each dataset, its source and licence.

## AI use
Summary and link to AI_USE.md.

## Limitations and next steps
Honest list.
```

The example row is illustrative; every number in your README must come from a script in the repository.

### 5.3 Architecture diagram

Draw two levels of the [C4 model](https://c4model.com/): a context diagram (your system, its users and external systems) and a container diagram (services, stores, queues). Keep the diagram source in the repository as [Mermaid](https://mermaid.js.org/), which GitHub renders, so it changes with the code. Mark simulated components clearly, for example with a dashed border or "(sim)" in the label.

### 5.4 Design doc and decision records

- **Design doc.** Context and scope, goals and non-goals, the design, alternatives considered, cross-cutting concerns (security, privacy, observability, cost). Google's practice is a good public description ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)). Two to six pages is enough.
- **ADRs.** One short file per decision with title, status, context, decision and consequences ([Nygard, 2011](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)). Aim for 8–15 in a v1.
- **Postmortem.** Blameless, with timeline, impact, root cause, what went well and action items ([Google SRE workbook](https://sre.google/workbook/postmortem-culture/)).

### 5.5 `AI_USE.md` template

```markdown
# AI use in this project
Tools and versions: <assistant, model, date range>
Delegated to AI: <scaffolding, test data generators, dashboards, first drafts of docs ...>
Written by me without AI: <the core modules named on the flagship page>
Verification: <property tests, mutation score, eval sets, manual review of every diff in core/>
Where AI was wrong: <3–5 concrete cases with the commit that fixed them>
Prompts or agent configs worth sharing: <path>
```

### 5.6 The two-minute demo script

| Time | Show | Say |
|---|---|---|
| 0:00–0:15 | Title card with the problem | Who has the problem and why it is hard |
| 0:15–0:35 | The results table | The headline number and how it was measured |
| 0:35–1:15 | One real path, end to end, live | What the user does and what the system does underneath |
| 1:15–1:40 | Inject a failure; show detection and recovery | The failure you designed for and the evidence it works |
| 1:40–1:55 | One diagram and one ADR | The key trade-off and what you gave up |
| 1:55–2:00 | Repository and write-up links | Where to check every claim |

Record at 1080p with readable font sizes, no music, and captions. Show real terminals and dashboards, not slides of them.

### 5.7 The write-up

1,500–2,500 words, published on a blog or as `docs/writeup.md`: the problem, the design and its main trade-off, the hardest bug, the failure tests and results, the numbers with their method, what AI did and did not do, limitations, and what you would do next. A panel should be able to read it in ten minutes and know what to ask you.

## 6. Anti-patterns

| Anti-pattern | Why it fails | Do instead |
|---|---|---|
| Tutorial clone ("Netflix clone", "chat app") | Thousands exist; it shows you can follow steps | Take a real problem with a hard constraint (money, latency, battery, privacy) |
| Toy CRUD | AI writes it in minutes; nothing can go wrong in it | Add the parts where things go wrong: concurrency, duplicates, partial failure, permissions |
| Unverified AI-generated code | Panels test whether you can find flaws in generated code; a flaw in your own flagship ends the interview | Hand-write the core, test the rest, review every diff, keep `AI_USE.md` honest |
| Claims without numbers | "Scalable" without a load test means nothing | Every adjective in the README becomes a measured row in the results table |
| Kitchen-sink stack | Ten technologies, none understood | Fewest moving parts that meet the requirements; justify each in an ADR |
| Invented users or numbers | Easy to detect and disqualifying | Label simulations as simulations; report small real numbers honestly |
| Secrets and open bills | Leaked keys and surprise cloud bills | Secret scanning in CI, budget alerts, a teardown script, tags with an expiry date |
| Happy path only | Production is mostly unhappy paths | A failure-test suite and at least one real postmortem |
| Unlicensed or scraped personal data | Legal risk, and it signals poor judgement | Licensed public data, synthetic data, or consented data with a written agreement |
| Team project with unclear ownership | The panel cannot tell what you did | `CONTRIBUTIONS.md` and commit history that match your claims |

## 7. Rules for every flagship

1. **Data.** Use only data whose licence permits your use, and list every licence in the README. Personal data stays out unless a real organisation consents in writing and you follow the DPDP Rules, 2025 ([PIB, 14 Nov 2025](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014)); synthetic data is the default.
2. **Security.** Defensive and authorised only. Test only systems you own or have written permission to test. Security flagships contain no attack recipes or working exploit code.
3. **Simulations are labelled.** Anything inspired by a real system (UPI, IRCTC, a bank) is an illustrative simulation built from public information and must say so. Never imply a real company uses your design.
4. **Cost safety.** Set a budget alert before creating any cloud resource, tag everything with an owner and expiry, and keep a tested teardown command. No paid API keys in the repository; secret scanning runs in CI.
5. **Licence your code** with an open licence ([choosealicense.com](https://choosealicense.com/)) and respect the licences of everything you use.
6. **Your own work.** Team flagships are allowed if each person owns a named part and `CONTRIBUTIONS.md` says who did what.

## 8. How the flagship fits the curriculum

The flagship is built in Year 4 during [IND401](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) or alongside [THS501](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), presented in [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) interviews and reused in [LCH502](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md). Finishing v1 and defending it to a panel is the main evidence for each major's L3 gate. The scale-up tier and stretch goals are where an L4 or L5 candidate shows they can go further: design something others build on, handle failures nobody planned for, or produce a new, reproducible result.

## Sources

All checked October 2026.

- Canva Engineering, *Yes, you can use AI in our interviews* (11 Jun 2025). https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/
- Anthropic, *Guidance on candidates' AI usage*. https://www.anthropic.com/candidate-ai-guidance
- Stack Overflow, *2026 Developer Survey: AI*. https://survey.stackoverflow.co/2026/ai/data
- Veracode, *2025 GenAI Code Security Report* (updated Oct 2025). https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/
- Google Cloud / DORA, *Announcing the 2025 DORA report* (24 Sep 2025). https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- Malte Ubl, *Design Docs at Google*. https://www.industrialempathy.com/posts/design-docs-at-google/
- Michael Nygard, *Documenting Architecture Decisions* (15 Nov 2011). https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Google SRE workbook, *Postmortem Culture*. https://sre.google/workbook/postmortem-culture/
- C4 model. https://c4model.com/ ; Mermaid. https://mermaid.js.org/
- PIB, DPDP Rules, 2025 notified (14 Nov 2025). https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014
- Choose a License. https://choosealicense.com/

_Last reviewed: 2026-10_
