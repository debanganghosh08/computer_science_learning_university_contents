# SAR404 · Labs and projects

Technical labs run in a personal cloud organisation with a budget alarm (tear down the same day) or locally. Tabletop exercises use scenarios written by the instructor or by classmates. All organisations below are *illustrative scenarios* unless a source is given. Lab 2 is done without AI assistants. No lab involves real malware; "ransomware" in drills is simulated by deleting or overwriting your own test data.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Case lessons | Analyse Maersk 2017, Change Healthcare 2024, CrowdStrike 2024 and C-Edge 2024; define a "minimum viable company" for an illustrative hospital | Lesson table; list of services and manual workarounds for 72 hours without IT | 3 h |
| 2 · Dependency graph (no AI) | Model five critical services of an illustrative payment bank as a dependency graph in Python (NetworkX); compute single points of failure; set impact tolerances, RTO and RPO | Graph code, SPOF list, tolerance table with reasons | 4 h |
| 3 · Locked backups | Configure immutable backups in a separate account with separate keys; prove the production administrator cannot delete them; replicate a corruption to a standby and recover by point-in-time restore | Denied deletion logs, corruption replay, restore evidence | 4 h |
| 4 · Rebuild from code | Rebuild a three-tier demo app and its identity realm from infrastructure as code and backups into a clean account | Timed runbook with each step's duration and blockers | 5 h |
| 5 · Hidden dependencies | Review a provided DR design for control-plane, DNS, identity, certificate and licence dependencies; choose DR patterns for five systems | Findings and pattern choices with cost estimates | 3 h |
| 6 · Vendor failure | Design update rings for 10,000 endpoints and an exit plan for one critical SaaS | Ring design with promotion criteria; exit plan with data export test | 3 h |
| 7 · Crisis and tabletop | Write an out-of-band communication plan; run a 90-minute ransomware tabletop with injects and observers | Plan, decision log, after-action report | 4 h |
| 8 · Instrumented drill | Run a recovery drill on your Lab 4 app with timing and data-loss measurement | Measured RTO and RPO against targets, evidence pack | 5 h |
| 9 · Strategy building blocks | Build a capability map with current and target levels and a three-year roadmap for an illustrative insurer | Map and dependency-checked roadmap | 4 h |
| 10 · AI runbook drill | Generate a recovery runbook with an assistant, run it in a drill and log every defect | Defect log classified as wrong, missing or impossible | 3 h |

## Projects

### P1 · From business impact to backup architecture for a clinic chain (L1, ~6 hours)

**Real-world inspiration:** hospitals and clinics are frequent ransomware targets, and recovery depends on knowing which services matter first. The clinic chain is an *illustrative scenario*: eight clinics sharing appointment, prescription, billing and lab-result systems.

**What to build:** a brief with critical services, a dependency graph, tolerances, RTO and RPO per system, and a backup architecture with an immutable copy, separate identity and keys, and a restore-test schedule.

**Acceptance criteria:**
- Every system in the graph has an RTO and RPO traced to a service tolerance.
- At least three single points of failure are identified, each with a mitigation or a written acceptance.
- The backup design states who can delete backups, under what controls, and shows that the production administrator role cannot.
- The restore-test schedule covers every critical system at least quarterly, with a measurable pass criterion.

**Stretch goals:** a 72-hour paper-based operating procedure for one clinic; a cost estimate for the backup design.

**What it proves to an employer:** you can connect business impact to concrete recovery architecture.

### P2 · Ransomware recovery architecture and drill for a district hospital (L2, ~15 hours)

**Real-world inspiration:** the Change Healthcare attack (2024) showed how one compromise can halt healthcare operations for weeks ([TechTarget](https://www.techtarget.com/cybersecurity/news/366582824/Change-Healthcare-breached-via-Citrix-portal-with-no-MFA)); CISA's #StopRansomware Guide lists the controls ([CISA](https://www.cisa.gov/stopransomware/ransomware-guide)). The hospital is an *illustrative scenario* with a demo records application, an identity realm and a lab-results integration.

**What to build:** a recovery architecture (Tier 0 map, immutable backups in a separate account, an isolated recovery environment with its own identity, rebuild-from-code pipelines, identity recovery procedure) and a full simulated recovery drill with a tabletop for the hospital's crisis team, plus draft CERT-In and DPDP notifications.

**Acceptance criteria:**
- After you simulate destruction of production data and the identity realm, the application is restored in the isolated environment within the RTO you set in advance, with measured data loss within the RPO.
- Restored systems are validated (checksums of data, known-good image digests, configuration baselines) before reconnecting; the validation record is part of the evidence.
- No production identity can access the backup account or the isolated environment (tests shown).
- The tabletop produces a decision log with at least eight timed decisions and an after-action report with owners and dates.
- Notification drafts meet CERT-In's 6-hour reporting window and the DPDP Rules' content requirements as summarised in SEC305.

**Stretch goals:** clinical downtime procedures for two departments; a second drill one week later measuring improvement.

**What it proves to an employer:** you have designed and actually exercised a ransomware recovery, which few candidates can show.

### P3 · Security strategy and resilience programme for an insurer (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** regulators now expect tested resilience (RBI's 2026 directions for banks, the EU's DORA), boards face disclosure duties, and concentration risk became a board topic after July 2024. The insurer is an *illustrative scenario*: 4,000 staff, agents across India, a policy administration system on-premises, digital sales on cloud, a claims platform from a SaaS vendor, and plans for AI-assisted claims handling.

**What to build:**
- a strategy document: diagnosis, guiding policy, coherent actions, CSF 2.0 current and target profiles, capability map, operating model and a three-year roadmap;
- a budget with ranges and a risk-reduction argument for the top five investments;
- a resilience architecture: critical services and tolerances, DR pattern per system, concentration analysis of suppliers, exit plans for two, update-ring policy;
- a crisis management framework with decision rights and a notification matrix (CERT-In, DPDP, IRDAI if applicable, marked "(unconfirmed)" where you could not verify a requirement);
- a metrics set and a one-page board paper;
- a policy for AI use in resilience and incident response.

**Acceptance criteria:**
- The strategy contains a diagnosis, a guiding policy and actions that a panel can trace to each other; at least two things the strategy explicitly will not do, with reasons.
- The roadmap passes a dependency check, and each initiative has an owner, cost range and success metric.
- The concentration analysis covers at least 20 suppliers and identifies at least three where a 48-hour outage breaches a tolerance, each with a mitigation.
- The board paper fits one page, names three decisions and their costs, and is understood by a non-specialist reviewer (a peer from another major) without help.
- In a 10-minute board presentation followed by 15 minutes of questions, you answer at least one question on cost, one on regulation and one on a scenario the panel chooses.

**Stretch goals:** a FAIR-style analysis for the top two risks with sensitivity analysis; a second scenario exercise with the panel playing regulators.

**What it proves to an employer:** you can think and communicate like a security leader, which is what separates principal architects and deputy CISOs from senior engineers.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): resilience measurement and strategy topics make strong capstones.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): P3 is a leadership-track portfolio piece.
- [SAR501 Frontier Seminar](../../year_5/SAR501_frontier_seminar_post_quantum_migration/README.md): migration programmes need the strategy and budget skills from this course.
- The [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SAR_security_architecture.md): its resilience and executive sections.
