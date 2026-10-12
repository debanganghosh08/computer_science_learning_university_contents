# SEC401 · Labs and projects

All work uses your own isolated lab (Windows and Linux VMs with Sysmon and `auditd`, a SIEM, Zeek and Suricata from SEC301), your own test cloud or identity tenant, and public datasets such as OTRF Security-Datasets and Splunk BOTS. Emulation tools (Atomic Red Team, Caldera) run **only in the isolated lab**, with a written plan listing every test and its clean-up. Every lab and project lives in a Git repository with tests that run in CI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · ADS and ATT&CK v19 mapping | Write a full ADS for one rule; update 10 rule mappings for the v19 split of Defense Evasion into Stealth and Defense Impairment | ADS document, mapping diff with reasons | 3 h |
| 2 · Data-source scoring | Score lab data sources with DeTT&CT; write one pySigma processing pipeline for a custom log source | Scores, gap list, pipeline code with a test | 4 h |
| 3 · Sigma rules and conversion | Write 10 Sigma rules for behaviours you can generate in the lab, one correlation rule and one filter; convert to two SIEM languages | Rules, conversions, a table of semantic differences | 7 h |
| 4 · Detection-as-code pipeline | Repository with linting, schema checks, unit tests on positive and negative events, conversion and deployment to the lab SIEM through its API | Working CI run, a failing test you introduced and fixed | 6 h |
| 5 · Lab validation | Validation plan with isolation and clean-up; run 10 benign emulation tests; compare expected and observed telemetry | Signed-off plan, results table, three gaps found | 5 h |
| 6 · Tuning | Measure precision of five rules on labelled alerts; tune two noisy ones without breaking their positive tests | Before/after precision and volume, test runs | 4 h |
| 7 · Behavioural analytics | Build a first-seen analytic and a stacking analysis across hosts | Queries or notebook, findings labelled benign or suspicious | 4 h |
| 8 · Hunt plan and execution | PEAK-style hypothesis-driven hunt on an OTRF dataset or a CyberDefenders threat-hunting lab | Plan, notebook, report, one new detection | 6 h |
| 9 · Cross-domain hunts | One identity hunt (OAuth consents, token use) and one cloud hunt (access-key misuse) on sample data | Two short hunt reports | 5 h |
| 10 · Coverage and health | Re-score an ATT&CK heatmap with validation evidence; build a detection health dashboard (last fired, test status, source volume) | Heatmap before/after, dashboard | 4 h |

## Projects

### P1 · Living-off-the-land detection pack (L1, ~6 hours)

**Real-world inspiration.** CISA, the NSA, the FBI and international partners published joint guidance in February 2024 on living-off-the-land techniques used by actors such as Volt Typhoon, stressing behaviour-based detection and baselining because built-in tools look legitimate.

**What to build.** Eight Sigma rules for living-off-the-land behaviours described in the guidance (for example, built-in remote management from unusual sources, scheduled task creation by unusual parents, credential-store access by non-standard processes, event log clearing, shadow copy deletion, and network discovery commands run in bursts), each with an ADS-lite (goal, data, blind spots, false positives) and recorded positive and negative test events from your lab.

**Acceptance criteria**
- All eight rules pass their positive tests and stay silent on a recorded day of normal lab activity.
- Each rule converts cleanly to at least one SIEM language with sigma-cli; conversion is part of the test run.
- Each ADS-lite names at least one legitimate administrative activity that will look similar, and how the analyst tells them apart.
- Rules map to ATT&CK v19 technique IDs.

**Stretch goals.** Score each rule's robustness with Summiting the Pyramid and rewrite the weakest one.

**What it proves to an employer.** You detect behaviour rather than indicators, and you know where your rules are blind.

### P2 · Detection-as-code platform with health monitoring (L2, ~15 hours)

**Real-world inspiration.** Elastic, Splunk and SigmaHQ maintain open detection repositories with tests and CI. ATT&CK's v18 and v19 changes (Detection Strategies; the Defense Evasion split) forced teams to update mappings across whole rule libraries, which is easy only when rules are managed as code.

**What to build.** A platform for at least 30 rules: repository layout with metadata and owners; linting and schema validation against your lab's field names; unit tests with recorded events; automatic conversion and deployment to your lab SIEM; a status workflow (experimental → test → stable → deprecated); a script that updates ATT&CK mappings from a version mapping file; and a health dashboard showing last-fired date, test status and source volume per rule.

**Acceptance criteria**
- A pull request that renames a field in one log source makes CI fail on every affected rule, and the report lists them.
- Deployment is idempotent: running it twice changes nothing; rollback restores the previous rule set in under 5 minutes.
- The health dashboard flags any rule whose data source volume dropped by more than 50% in 24 hours.
- At least 30 rules have positive and negative tests; overall test run time is under 5 minutes.
- Documentation explains how a new analyst adds a rule in under 30 minutes, tested with one classmate.

**Stretch goals.** Add a second SIEM backend; publish a sanitised subset of your rules and tests as open source.

**What it proves to an employer.** You can run a detection library like a software product, which is exactly what mature detection engineering teams do.

### P3 · Threat-informed detection and hunting programme against identity and SaaS intrusions (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** CISA's Scattered Spider advisory (AA23-320A, updated July 2025) describes help-desk social engineering and MFA abuse; Mandiant's 2024 Snowflake investigation found stolen credentials used against accounts without MFA; Google Threat Intelligence Group's August 2025 report on Salesloft Drift describes stolen integration tokens used to export CRM data. Mandiant's M-Trends 2026 recommends routing all SaaS through a central identity provider. The fintech below is illustrative.

**What to build.** For an illustrative Indian fintech (Entra ID or Keycloak, a CRM, a cloud data warehouse, Windows laptops, Linux servers):
1. a threat profile naming the five intrusion patterns that matter most, with sources;
2. a prioritised backlog of 25 detection ideas with data requirements;
3. **15 detections** implemented as code (from P2's platform), at least six of them on identity or SaaS audit logs, each validated in your lab or test tenant with a written plan;
4. **three documented hunts** using PEAK or TaHiTI, at least one of which turns into a detection and one of which ends in a documented visibility gap;
5. a coverage report combining ATT&CK mapping, validation result and robustness level for each technique;
6. an AI-assisted drafting experiment: have an assistant draft the same 15 detections with and without your schema and examples, run them through your tests, and report pass rates and error types.

**Acceptance criteria**
- Every detection has an ADS, passes positive and negative tests in CI, and has been validated with recorded telemetry; total alert volume on two days of baseline activity is within a stated budget.
- Hunt reports state hypothesis, data, method, findings, and the follow-up artefact (detection or data request).
- The coverage report shows, for each technique, "mapped", "validated" and "robust" separately; no cell is marked covered without validation evidence.
- The AI experiment reports pass rates for both conditions, the five most common error types with examples, and a recommendation for how your team should use AI drafting.
- A three-page summary for the CISO explains what is now detectable, what is not, and the next three investments.

**Stretch goals.** Add a correlation layer (risk-based alerting) across identity and endpoint; run a purple-team session with a classmate under written scope and record the results.

**What it proves to an employer.** You can run detection engineering end to end against the attacks that are actually happening in 2025–26, measure your own coverage honestly, and use AI with evidence. This is senior detection engineer and threat hunter work.

## Feeds into

- [SEC501 Frontier Seminar: Threat Intelligence and Security Research](../../year_5/SEC501_frontier_seminar_threat_intelligence/README.md): intelligence-driven detection and research on detection quality.
- [SEC404 AI in Security Operations](../SEC404_ai_in_security_operations/README.md): P3's AI drafting experiment becomes a full evaluation.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): detection robustness and coverage measurement are strong thesis topics.
- [CAR401 Career Lab II](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): P2 and P3 are portfolio centrepieces for detection engineering interviews.
