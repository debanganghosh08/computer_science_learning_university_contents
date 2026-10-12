# SEC302 · Labs and projects

Use the home lab from [SEC301](../SEC301_network_security_and_defense/README.md) (or build one: a SIEM VM with 8 GB RAM plus two or three small client VMs) and public training datasets. Never open suspicious emails, links or attachments on your everyday machine: use an isolated VM or an online sandbox, and treat every sample as live. Each lab submission contains your queries or configuration in Git, a short write-up with numbers, and screenshots of evidence.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · SIEM build | Deploy Wazuh or Elastic Security; enrol a Windows VM (with Sysmon) and a Linux VM; forward firewall and DNS logs from the SEC301 lab | Architecture diagram, log-source inventory (owner, volume per day, use case) | 5 h |
| 2 · Onboarding and silent-source alert | Normalise two sources to ECS or OCSF; build an alert that fires when any source stops for 30 minutes; measure ingestion delay | Field map, alert rule, delay measurements | 4 h |
| 3 · Correlation and risk rules | Write the same "many failures then success" behaviour as a correlation rule and as a risk-based rule | Both rules, test events, a note on which misses what | 3 h |
| 4 · KQL and SPL | Answer 10 questions with KQL on a Microsoft sample dataset and 10 with SPL on Splunk BOTS v3 | Queries with results and a one-line reasoning each | 6 h |
| 5 · Triage method | Triage 30 mixed alerts (provided export or your own lab alerts) with a written template, then write three tuning requests | Completed templates, verdict counts, tuning requests with evidence | 5 h |
| 6 · Phishing and sign-in cases | Investigate five reported emails (anonymised real samples from the public Phishing Pot collection, opened only in a VM) and one compromised-account scenario | Two investigation reports with timelines | 5 h |
| 7 · Endpoint and cloud cases | Investigate an EDR-style alert set from OTRF Security-Datasets and a CloudTrail scenario from a CyberDefenders or public lab | Two investigation reports with scope and containment | 5 h |
| 8 · Playbook and SOAR | Write a phishing playbook; automate observable enrichment with Shuffle or Sentinel automation; classify 15 actions as auto, approve or never-auto | Playbook, workflow export, action classification | 5 h |
| 9 · Metrics | From a provided case export, compute median and 90th-percentile time to detect, acknowledge and contain; rank rules by value | Notebook, monthly one-page SOC report | 3 h |
| 10 · AI assistant audit | Run an AI assistant (a vendor trial or a local open-weights model) over 25 labelled lab alerts; plant one prompt-injection string in a log field and test the result | Agreement table, error types, injection test result, one-page AI usage policy | 5 h |

## Projects

### P1 · Phishing-report triage kit (L1, ~6 hours)

**Real-world inspiration.** Reported-phish queues are among the highest-volume SOC work, and Microsoft shipped an AI Phishing Triage Agent for them in 2025. Mandiant's M-Trends 2026 shows attackers shifting from email phishing (6% of intrusions) to voice phishing (11%), so triage must also check what happened *after* a click.

**What to build.** A command-line tool plus playbook. The tool takes a `.eml` file and produces a triage report: parsed headers (SPF, DKIM, DMARC results, received path), sender and reply-to mismatch, extracted URLs and attachments with hashes, defanged indicators, and a checklist of follow-up SIEM queries (other recipients, clicks, sign-ins after the click). The playbook defines verdicts and escalation rules.

**Acceptance criteria**
- Correctly parses 20 test emails (10 anonymised samples from Phishing Pot, 10 legitimate emails you supply), with zero crashes on malformed headers.
- Every indicator in the report is defanged (for example `hxxp://`) so it cannot be clicked by accident.
- On the 20 emails, your playbook verdicts match a reviewer's labels on at least 18; each disagreement is explained.
- The tool never fetches URLs or opens attachments itself; the README explains why.

**Stretch goals.** Export observables as a STIX 2.1 bundle; add a Sigma or KQL query generator for "who else received this".

**What it proves to an employer.** You can handle the most common SOC alert type carefully and repeatably, and you can automate safely.

### P2 · SOC in a box for a 50-person company (L2, ~15 hours)

**Real-world inspiration.** Small Indian companies face the same CERT-In duties as large ones: report listed incidents within 6 hours and keep ICT logs for 180 days. Many cannot afford a commercial SIEM, so open-source stacks such as Wazuh and Elastic are common starting points.

**What to build.** In your lab, a working mini-SOC for an illustrative company with Microsoft 365 or Google Workspace (simulated with exported sample logs), Windows laptops, two Linux servers, a firewall and a VPN:
1. at least six onboarded log sources with normalised fields and a retention plan meeting 180 days at a stated storage budget;
2. 15 detections with descriptions, severities and ATT&CK mappings;
3. silent-source monitoring;
4. three dashboards (operations, identity, executive);
5. triage SOPs for the five highest-volume detections;
6. a 6-hour CERT-In reporting checklist tied to the SIEM fields you would need.

**Acceptance criteria**
- Each detection is demonstrated by an event you generated in the lab, and none fires more than 5 times a day on two days of normal lab activity.
- The silent-source alert fires within 30 minutes of stopping any source.
- Storage and retention calculations show assumptions and meet 180 days.
- A peer can follow your SOPs to triage a test alert without asking you questions (tested with one classmate).

**Stretch goals.** Add a SOAR enrichment workflow; map coverage to CIS Controls v8.1 Control 8 (audit log management).

**What it proves to an employer.** You can stand up and run monitoring from nothing, which is what small companies, MSSPs and MDR providers need from a junior engineer.

### P3 · Monitoring a banking technology provider, with an evaluated AI triage assistant (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** In July 2024 a ransomware attack on C-Edge Technologies, a technology provider to co-operative and regional rural banks, led NPCI to isolate it from retail payment systems, disrupting payments for about 300 small banks until 1 August. KPMG's advisory attributed the intrusion to the RansomEXX group and a misconfigured Jenkins server. RBI's July 2026 directions now require commercial banks to report cyber incidents on the DAKSH platform within six hours. The company below is illustrative, not a model of C-Edge.

**What to build.** A monitoring design and lab implementation for an illustrative core-banking service provider (build servers, a hosted banking application, an admin jump host, Active Directory, a cloud account):
1. a threat model listing the 10 behaviours you most need to see (for example: new admin on the build server, build jobs running unexpected commands, mass file renames, backup deletion, unusual outbound data volumes, new remote-access tools, privileged sign-ins outside change windows);
2. detections for all 10 in your SIEM, each tested with a lab-generated event;
3. playbooks for the three most severe, including the customer-bank and regulator communication steps;
4. an AI triage assistant (a local open-weights model through Ollama, or a vendor trial) that receives an alert plus enrichment and returns a verdict with cited evidence as JSON;
5. an evaluation of that assistant on at least 60 labelled alerts (true, benign and false positives, including five containing injected instructions in log fields);
6. a metrics dashboard and a two-page board summary.

**Acceptance criteria**
- All 10 detections fire on their test events and stay below an agreed alert budget (state it) on two days of baseline activity.
- The evaluation reports precision and recall for "escalate" verdicts, the share of verdicts with correct evidence citations, the number of injected instructions obeyed, and median time per alert with and without the assistant.
- The assistant has no write or containment permissions; any action proposal requires a human approval step, shown in the workflow.
- The playbook shows how the 6-hour reporting clock is met, with named roles.
- The repository contains everything needed to reproduce the lab and the evaluation from scratch.

**Stretch goals.** Add a risk-based alerting layer; compare two models on the same evaluation set; measure how verdict quality changes when enrichment is removed.

**What it proves to an employer.** You can build monitoring for a regulated, high-impact supplier and you can measure, rather than assume, what an AI assistant adds. That combination is what senior SOC and SOC engineering roles now ask for.

## Feeds into

- [SEC402 Digital Forensics and Incident Response](../../year_4/SEC402_digital_forensics_and_incident_response/README.md): the investigations and playbooks here become full incident response.
- [SEC401 Detection Engineering and Threat Hunting](../../year_4/SEC401_detection_engineering_and_threat_hunting/README.md): tuning requests and P2's detections move into detection-as-code.
- [SEC404 AI in Security Operations](../../year_4/SEC404_ai_in_security_operations/README.md): P3's evaluation harness is extended to agents.
- [OV03 DevSecOps](../../../../04_overlaps/OV03_devsecops/README.md): monitoring CI/CD systems such as the build server in P3.
