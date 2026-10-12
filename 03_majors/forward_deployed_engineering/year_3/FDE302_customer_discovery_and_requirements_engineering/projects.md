# FDE302 · Labs and projects

All interviews and observations need informed consent, recorded in writing. Personal data is anonymised before it leaves the participant's organisation, and recordings are deleted at the end of the course unless the participant agrees otherwise. Scenarios you invent are labelled "illustrative". Every finding you submit links to raw evidence (quote, observation, log query).

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Asks to problems | Rewrite ten illustrative asks as problem hypotheses; build an issue tree; estimate one problem's annual cost with ranges | Problem statements, issue tree, cost model with assumptions | 3 h |
| 2 · Stakeholder map and guides | Map 12 stakeholders for an illustrative hospital deployment; write sponsor, manager and front-line interview guides | Power-interest grid with reasons; three guides | 3 h |
| 3 · Interviews and synthesis | Run five interviews about a real routine task (e.g., paying fees, booking lab slots); synthesise | Consent forms, notes with quote/observation/interpretation, findings with evidence counts | 6 h |
| 4 · Contextual observation | Observe one real workflow for at least 30 minutes; catalogue workarounds and artefacts | Observation log, workaround catalogue, say-versus-do comparison | 4 h |
| 5 · BPMN and value stream map | Model the observed workflow in BPMN 2.0; compute process time versus wait time | BPMN file (bpmn.io or Camunda Modeler), timing table, three improvement hypotheses | 4 h |
| 6 · Process mining | Discover variants and conformance on a public event log with PM4Py | Notebook, top-ten variants, conformance rate, five data caveats | 5 h |
| 7 · Jobs and outcomes | Write job statements, job stories and ranked outcome statements; map switching forces | Jobs document, ranking from at least three users | 3 h |
| 8 · Requirements and traceability | Write acceptance criteria (Gherkin), EARS requirements, a non-functional table and a traceability matrix for one pilot | Requirements pack; matrix linking each requirement to a test | 6 h |
| 9 · Data inventory and profiling | Inventory data for an illustrative distributor; profile a messy public dataset; draft the access request | Inventory table, profiling report, access request with approval chain | 4 h |
| 10 · Pilot charter | Write a full pilot charter with go/extend/stop thresholds; have a classmate in the sponsor role challenge and sign it | Signed charter; list of changes from the challenge | 3 h |
| 11 · AI-assisted synthesis audit | Transcribe a consented interview; run AI clustering; compare with manual synthesis | Word error rate on a sample, invented and dropped themes with evidence | 3 h |

## Projects

### P1 · Problem discovery for a campus or community service (L1, ~6 hours)

**Real-world inspiration.** Public-sector service teams in the UK run a discovery phase to understand users and constraints before building anything (GOV.UK Service Manual). Palantir's deployment strategists co-create workflows with the people who will use them (2022).

**What to build.** Pick a real service near you with a known pain point: hostel maintenance requests, library fines, clinic appointment queues, a society's maintenance collections. Interview at least five users and one staff member, observe the service once, and write a discovery report.

**Acceptance criteria**
- Five consented interviews and one observation, with anonymised notes submitted.
- A problem statement with who, how often and estimated cost (with ranges and assumptions).
- At least four findings, each backed by two or more pieces of evidence; at least one finding that contradicts what staff said about the process.
- A one-page recommendation that includes at least one non-software option.

**Stretch goals.** Present the report to the service owner and record their response.

**What it proves to an employer.** You find the real problem before writing code, and you can back it with evidence.

### P2 · Workflow map and requirements pack for an illustrative distributor (L2, ~15 hours)

**Real-world inspiration.** Palantir describes an early pilot task as integrating a customer's ERP into an application "that automatically resolves discrepancies in shipments" (2022). In India, distributors reconcile purchase orders, GST invoices and e-way bills across several systems (illustrative scenario).

**What to build.** You are given (or build, from a public dataset) an event log of order-to-invoice cases for an illustrative FMCG distributor in Pune, plus three role-play interviews with classmates acting as the sales coordinator, the accounts executive and the warehouse supervisor (briefs provided by the instructor). Produce: a BPMN map of the process as performed, process-mining analysis of variants and wait times, a list of exceptions with frequencies, job stories for each role, and a requirements pack for a discrepancy-resolution tool.

**Acceptance criteria**
- BPMN model validated by the role-play participants; differences between documented and mined process listed.
- Wait-time analysis identifying the top three delays with their share of total cycle time.
- At least 15 requirements: 8 in Gherkin with failure cases, 4 non-functional with numeric targets, 3 compliance requirements traced to a source.
- A traceability matrix linking every requirement to an evidence item and a test.
- A list of data quality problems found in the log, each with its effect on the analysis.

**Stretch goals.** Simulate the effect of removing the largest delay on cycle time with a simple model.

**What it proves to an employer.** You can turn interviews and logs into a precise, testable specification that an engineering team can build from.

### P3 · Full discovery and pilot design for an AI deployment (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** OpenAI's Deployment Leads map workflows and success criteria and set "impact hypotheses, baselines, and KPIs"; Anthropic's Applied AI Architects help customers "develop evaluation frameworks". Many enterprise AI pilots stall without a decision owner or production path (analysis).

**What to build.** A complete discovery engagement for an illustrative customer chosen from three briefs: (a) a Bengaluru insurance third-party administrator processing hospital claims, (b) a state transport corporation's grievance cell, (c) a mid-size law firm's contract review team. Classmates and, where possible, an industry mentor play stakeholders from instructor-written briefs that contain hidden constraints. Deliver: stakeholder map, interview and observation synthesis, workflow and exception analysis, jobs and outcomes, data inventory and access plan, a 30-example seed evaluation set labelled by the "domain expert", requirements pack, and a signed pilot charter.

**Acceptance criteria**
- At least eight stakeholder sessions; every hidden constraint in the briefs is discovered and documented (the instructor checks against the brief).
- Charter with baseline method, go/extend/stop thresholds, kill criteria, decision owner and decision date.
- Seed evaluation set with labelling guidelines and agreement between two labellers reported.
- Requirements include data residency, consent, audit and human-review rules relevant to the chosen sector.
- A 10-minute readout to a panel playing the executive sponsor, followed by a 10-minute Q&A, scored on a published rubric.

**Stretch goals.** Run the same discovery with an AI-synthesis workflow in parallel and report what it missed.

**What it proves to an employer.** You can run the first two weeks of a real AI engagement and leave the customer with a pilot that will produce a clear decision.

## Feeds into

- [FDE304 Deploying AI in the Enterprise](../FDE304_deploying_ai_in_the_enterprise/README.md): the P3 charter and seed evaluation set become the starting point for an AI deployment.
- [FDE305 Technical Communication](../FDE305_technical_communication_in_the_field_demos/README.md): discovery readouts and workshops.
- [FDE402 Debugging and Operating in Customer Environments](../../year_4/FDE402_debugging_and_operating_in_customer_environments/README.md): requirements and constraints discovered here shape operating plans.
- [FDE404 Field Studio](../../year_4/FDE404_field_studio_three_simulated_customer/README.md): each simulated deployment opens with this course's discovery method.
