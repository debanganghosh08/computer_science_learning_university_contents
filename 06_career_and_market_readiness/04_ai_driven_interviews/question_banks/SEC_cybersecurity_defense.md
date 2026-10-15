# SEC · Cybersecurity Defense: interview question bank

| Role and market | Levels | Practise with | Score with |
|---|---|---|---|
| [SEC role page](../../01_market_map/roles/SEC_cybersecurity_defense.md) · [Cybersecurity major](../../../03_majors/cybersecurity_defense/README.md) | NG → Mid → Sr | [Mock kit 4.8](../how_to_run_a_mock_with_any_llm.md#48-security-scenario-defensive-45-minutes) | [Rubrics](../rubrics.md), especially section 10 |

Defensive security interviews test whether you can turn noisy signals into correct decisions: what happened, how bad it is, what to do now, and what to change so it does not happen again. All scenarios here are defensive and use synthetic data. Practise hands-on skills in legal environments (for example vendor training labs, TryHackMe or Hack The Box defensive paths, and public detection-engineering datasets).

## 1. The typical loop

| Round | Duration | What it tests | AI policy you may meet | Mock brief |
|---|---|---|---|---|
| Fundamentals screen | 30–45 min | Networking, Windows and Linux internals, authentication | AI-off | Kit 4.8 (short) |
| Alert and log scenario | 45 min | Triage, scoping, next steps | AI-off | Kit 4.8 |
| Hands-on lab | 60–90 min | Write a SIEM query, analyse a packet capture or event log | Sometimes documentation allowed | Kit 4.8 with a lab QUESTION |
| Incident-response tabletop | 45–60 min | Roles, communication, evidence, decisions | AI-off | Kit 4.8 |
| Behavioural | 45 min | Ethics, pressure, explaining risk | AI-off | Kit 4.11 |

**Certifications** (CompTIA Security+, ISC2 CC, vendor SOC certifications) are common early-career filters; labs and write-ups show skill (see the role page).

## 2. How to use this bank

Answer aloud with a timer, then open the guide. Run scenario questions as mocks by adding `QUESTION: <text>` to brief 4.8, which plays the environment and reveals logs only when you ask for them.

## 3. Questions

### Fundamentals

**Q1 · NG · Why is SMS one-time-password MFA weaker than a security key or passkey?**

<details><summary>Answer guide</summary>

- **Testing:** authentication strength.
- **Strong answer:** SMS codes can be intercepted or redirected (SIM swap, SS7 weaknesses) and, like any code a user types, relayed by a phishing site in real time. FIDO2/WebAuthn credentials (security keys, passkeys) are bound to the site's origin, so a look-alike domain cannot use them: phishing-resistant. Rollout considerations: recovery flows (often the weakest link), shared devices, accessibility.
- **Common mistakes:** "all MFA is equally strong".
- **Follow-ups:** MFA fatigue (repeated push prompts): defences such as number matching and rate limits.
</details>

**Q2 · NG · Authentication vs authorisation, with an example of a failure in each.**

<details><summary>Answer guide</summary>

- **Testing:** basic concepts precisely stated.
- **Strong answer:** authentication proves who you are (password plus MFA); authorisation decides what you may do (role checks, object ownership). Authentication failure example: weak password reset that lets someone take over an account. Authorisation failure example: a user changes an order ID in a request and sees another user's order (broken object-level authorisation). Defences differ: strong identity proofing vs server-side checks on every object access.
- **Common mistakes:** using the terms interchangeably.
- **Follow-ups:** where should authorisation checks live in a microservice architecture?
</details>

**Q3 · NG · Why are domain controllers protected so heavily in a Windows environment?**

<details><summary>Answer guide</summary>

- **Testing:** identity infrastructure awareness.
- **Strong answer:** Active Directory domain controllers hold credential material for every account and issue Kerberos tickets; control of one means control of the domain. Defences: tiered administration (separate admin accounts and workstations for domain admins), minimal membership of privileged groups, monitoring of privileged group changes and replication requests, patching, backups tested offline, and limiting which systems can log on with privileged accounts.
- **Common mistakes:** treating them as ordinary servers.
- **Follow-ups:** which events would you alert on for privileged group changes?
</details>

**Q4 · Mid · Name Windows security events you would collect to spot suspicious administrative activity, and why.**

<details><summary>Answer guide</summary>

- **Testing:** practical log knowledge.
- **Strong answer:** 4624 and 4625 (successful and failed logons, with logon type), 4672 (special privileges assigned at logon), 4688 (process creation, with command-line logging enabled), 4720 and 4728/4732/4756 (account created; member added to security groups), 4740 (account lockout), 1102 (audit log cleared), 7045 in the System log (new service installed). Add Sysmon for richer process and network telemetry. Explain baselining per host type.
- **Common mistakes:** collecting everything without a use case, or nothing beyond logons.
- **Follow-ups:** log volume is too expensive; how do you prioritise?
</details>

### SOC triage scenarios

**Q5 · NG · Alert: a user signed in from Bengaluru and, 20 minutes later, from Frankfurt. Triage it.**

<details><summary>Answer guide</summary>

- **Testing:** triage method, false-positive awareness.
- **Strong answer:** check whether one location is a VPN, cloud proxy or mobile carrier egress; device and browser details; whether MFA was satisfied and how; what the session did afterwards (mailbox rules, file downloads, admin actions); user's travel and recent password reset. If suspicious: revoke sessions, reset credentials, check for persistence (mail forwarding rules, new MFA methods, OAuth app consents), and document. Tune the rule with known egress ranges.
- **Common mistakes:** closing it as "VPN" without evidence, or disabling the account without checking business impact.
- **Follow-ups:** the user is the CFO and is travelling; how do you proceed?
</details>

**Q6 · Mid · Endpoint alert: a spreadsheet application started a script interpreter with an encoded command line. What do you do?**

<details><summary>Answer guide</summary>

- **Testing:** endpoint triage at a defensive level.
- **Strong answer:** an office application spawning a script interpreter is a classic indicator of a malicious document. Isolate the host if policy allows (network containment through the EDR); collect the process tree, the document's origin (email, download), decoded command line in a safe analysis tool, network connections, and file writes; search the fleet for the same hash, sender or domain; block indicators; check whether credentials on the host need resetting. Preserve evidence before cleaning. Preventive control: attack surface reduction rules blocking child processes from office apps, macro policies.
- **Common mistakes:** deleting the file and closing the ticket.
- **Follow-ups:** the same email reached 300 users; how do you scope and remove it?
</details>

**Q7 · Mid · Many accounts show one or two failed logins each, from a few IP addresses, over an hour. Explain and respond.**

<details><summary>Answer guide</summary>

- **Testing:** recognising credential attacks from logs.
- **Strong answer:** a low-and-slow password-spraying pattern: few attempts per account to avoid lockout, many accounts. Check for any successful logins from those sources and investigate those accounts first; block or challenge the source IPs; enforce MFA and check legacy authentication protocols that bypass it; ban common passwords; detection rule on distinct accounts per source over time rather than failures per account.
- **Common mistakes:** looking only at per-account failure counts.
- **Follow-ups:** the source IPs belong to a large cloud provider shared by legitimate users.
</details>

**Q8 · Mid · DNS logs show one host making thousands of queries for long, random-looking subdomains of a single domain.**

<details><summary>Answer guide</summary>

- **Testing:** network-signal interpretation.
- **Strong answer:** possible DNS tunnelling (data encoded in queries) or malware using generated domains; also possible benign causes (some security and CDN products use encoded subdomains). Check domain age and reputation, query volume and size over time, the process making the queries (endpoint telemetry), and data volume. Contain the host if malicious; block the domain at the resolver; hunt for other hosts querying it. Prevent with DNS filtering and egress controls.
- **Common mistakes:** blocking without checking for a business tool.
- **Follow-ups:** what DNS fields would you log, and for how long?
</details>

### Detection engineering

**Q9 · Mid · Write detection logic: alert when a new account is added to a privileged group outside an approved change window.**

<details><summary>Answer guide</summary>

- **Testing:** turning a requirement into a reliable detection.
- **Strong answer:** source events (Windows 4728/4732/4756 or the cloud identity provider's audit log); filter to a maintained list of privileged groups; join with a change-calendar lookup or ticket system; exclude approved automation accounts by identity, not by name pattern; include who made the change and from where; severity by group. Test with replayed events; document the rule, its owner and expected false positives; version it in Git (detection as code).
- **Common mistakes:** hard-coded exclusions that attackers could match; no testing.
- **Follow-ups:** how do you know the rule still works six months later (synthetic test events)?
</details>

**Q10 · Mid · How do you use MITRE ATT&CK in a SOC without turning it into a box-ticking exercise?**

<details><summary>Answer guide</summary>

- **Testing:** threat-informed defence.
- **Strong answer:** map existing detections and telemetry to techniques to find gaps; prioritise techniques used by threat groups relevant to your sector; validate coverage with tests (for example atomic test frameworks in a lab, purple-team exercises) rather than assuming; track detection quality (true-positive rate), not just count of techniques covered.
- **Common mistakes:** a heat map that claims coverage without testing.
- **Follow-ups:** which data sources give the most coverage for the cost?
</details>

**Q11 · Sr · How do you measure whether a SOC is effective?**

<details><summary>Answer guide</summary>

- **Testing:** security management judgement.
- **Strong answer:** time to detect and time to respond (by severity), share of incidents detected internally vs reported externally, true-positive rate per detection, alert-to-analyst ratio and toil, coverage validated by exercises, repeat incidents, time to close high-risk vulnerabilities. Avoid vanity metrics (number of alerts handled). Pair metrics with periodic red- or purple-team results.
- **Common mistakes:** measuring volume.
- **Follow-ups:** leadership wants one number; what do you give them?
</details>

### Incident response

**Q12 · Mid · Ransomware is found encrypting a file server on a Saturday morning. Walk through your response.**

<details><summary>Answer guide</summary>

- **Testing:** incident-response lifecycle under pressure.
- **Strong answer:** activate the incident plan and roles; contain (isolate affected hosts and segments, disable compromised accounts, block known indicators) while preserving evidence; determine scope and initial access; protect backups (verify they are offline or immutable and uncompromised); involve legal, management and communications; regulatory duties (in India, CERT-In directions require reporting specified incidents within 6 hours of noticing; data-protection law may require notifying affected people and the regulator); eradicate, restore from clean backups, monitor; lessons learned. Ransom payment decisions involve executives and legal advice, not the analyst alone. Frameworks: NIST SP 800-61.
- **Common mistakes:** wiping systems before scoping; restoring from backups that contain the malware.
- **Follow-ups:** the attackers also claim to have stolen data; what changes?
</details>

**Q13 · Mid · How do you collect evidence from a compromised server without destroying it?**

<details><summary>Answer guide</summary>

- **Testing:** forensic discipline.
- **Strong answer:** follow the order of volatility: memory and live state (running processes, network connections) before disk; avoid shutting down before memory capture if policy allows; use trusted tools from external media; hash images; record chain of custody (who, when, what, where stored); work on copies; snapshot cloud volumes and preserve audit logs. Coordinate with legal if the case may go to court or law enforcement.
- **Common mistakes:** running antivirus clean-up first; logging in with a privileged account and changing timestamps unknowingly.
- **Follow-ups:** what changes for a cloud virtual machine or a container?
</details>

**Q14 · Mid · A finance employee entered their password on a phishing page an hour ago. Respond.**

<details><summary>Answer guide</summary>

- **Testing:** business email compromise response.
- **Strong answer:** reset the password and revoke all sessions and tokens; check MFA registration changes; review sign-ins since the click; look for mailbox rules (forwarding, deletion of replies), OAuth app consents, sent emails (especially payment-change requests to vendors); search for the phishing email in other mailboxes and remove it; block the domain; warn finance to verify any payment changes by phone; report to the bank quickly if a fraudulent transfer occurred.
- **Common mistakes:** only resetting the password (existing sessions and forwarding rules survive).
- **Follow-ups:** how would you reduce the chance of this succeeding next time?
</details>

**Q15 · Sr · Design a tabletop exercise for the executive team.**

<details><summary>Answer guide</summary>

- **Testing:** preparedness leadership.
- **Strong answer:** pick a realistic scenario tied to top risks (ransomware with data theft, a cloud key leak, a supplier breach); define objectives (decision rights, communication, legal duties); prepare injects that force decisions (media inquiry, regulator deadline, ransom demand, partial backup failure); include legal, communications, IT and business owners; time-box; capture decisions and gaps; produce an action list with owners; repeat yearly.
- **Common mistakes:** a technical walkthrough that executives cannot engage with.
- **Follow-ups:** how do you measure improvement between exercises?
</details>

### Vulnerability management

**Q16 · Mid · A scan reports 2,000 vulnerabilities. Prioritise.**

<details><summary>Answer guide</summary>

- **Testing:** risk-based prioritisation.
- **Strong answer:** combine severity (CVSS) with likelihood of exploitation (EPSS scores, presence in CISA's Known Exploited Vulnerabilities catalogue), exposure (internet-facing or internal), asset criticality and compensating controls. Fix known-exploited, internet-facing issues on critical assets first with tight deadlines; group by fix (one patch resolves hundreds of findings); track service-level targets; accept risk formally where needed.
- **Common mistakes:** sorting by CVSS alone.
- **Follow-ups:** the business owner refuses downtime for patching.
</details>

**Q17 · Mid · A critical vulnerability in a widely used logging library is announced on Friday evening. What do you do?**

<details><summary>Answer guide</summary>

- **Testing:** emergency response for supply-chain vulnerabilities.
- **Strong answer:** find where it is used (SBOMs, dependency scanning, asset inventory, including vendors' products); apply vendor mitigations or configuration workarounds immediately for internet-facing systems; deploy detections for exploitation attempts and hunt in logs from before the announcement; patch in order of exposure; communicate status to leadership; ask suppliers for their status. Afterwards: improve the inventory that slowed you down.
- **Common mistakes:** waiting for Monday's change board.
- **Follow-ups:** you have no SBOMs; how do you find the library quickly?
</details>

### Cloud and identity

**Q18 · Mid · Cloud audit logs show an access key used from an unfamiliar country to list storage buckets.**

<details><summary>Answer guide</summary>

- **Testing:** cloud incident handling.
- **Strong answer:** identify the key's owner and permissions; check all actions taken with it (audit logs across regions); deactivate the key (not delete, to keep evidence) after confirming it is not legitimate; look for persistence (new users, keys, roles, policy changes); check data access logs; find how it leaked (public repository, laptop, CI logs); replace long-lived keys with federated short-lived credentials.
- **Common mistakes:** deleting the key and moving on.
- **Follow-ups:** the key belongs to a production integration; how do you avoid an outage?
</details>

**Q19 · Sr · What does "zero trust" mean in practice, and how would you start?**

<details><summary>Answer guide</summary>

- **Testing:** architecture beyond buzzwords.
- **Strong answer:** no implicit trust from network location; every access decision uses identity, device health and context, with least privilege and continuous verification (NIST SP 800-207). Start with strong identity (phishing-resistant MFA, single sign-on), device inventory and health signals, access proxies for internal applications instead of broad VPN access, segmentation of critical systems, and logging of decisions. Prioritise by crown-jewel systems.
- **Common mistakes:** buying a product called zero trust.
- **Follow-ups:** legacy applications that cannot use modern authentication.
</details>

### Governance and law

**Q20 · Mid · ISO/IEC 27001, SOC 2 and the NIST Cybersecurity Framework: how do they differ?**

<details><summary>Answer guide</summary>

- **Testing:** governance literacy.
- **Strong answer:** ISO/IEC 27001 is a certifiable standard for an information security management system (risk process plus controls from Annex A). SOC 2 is an attestation report by an auditor against trust services criteria, common for US customers of service providers. The NIST CSF (version 2.0, 2024, which added a Govern function) is a voluntary framework for organising and measuring a programme. Many organisations map controls once to satisfy several.
- **Common mistakes:** calling SOC 2 a certification issued by a standards body.
- **Follow-ups:** a customer asks for a SOC 2 report you do not have; what do you offer?
</details>

**Q21 · Mid · In India, what reporting duties might apply after a security incident?**

<details><summary>Answer guide</summary>

- **Testing:** regulatory awareness (not legal advice).
- **Strong answer:** CERT-In's directions of April 2022 require reporting specified cyber incidents to CERT-In within 6 hours of noticing them, and require log retention for 180 days. Sector regulators (for example RBI for banks and payment operators, SEBI for market entities) add their own rules. The Digital Personal Data Protection Act, 2023 requires notifying the Data Protection Board and affected individuals of personal data breaches as its rules specify. Involve legal counsel early; keep a timeline.
- **Common mistakes:** waiting until the investigation is complete to report.
- **Follow-ups:** your company also processes EU residents' data; what changes?
</details>

### Network and email

**Q22 · Mid · You suspect a host is beaconing to a command-and-control server. What would you look for in network data?**

<details><summary>Answer guide</summary>

- **Testing:** defensive network analysis.
- **Strong answer:** periodic connections with regular intervals (possibly with jitter) to the same destination, small consistent payload sizes, rare destinations in your environment, young domains, unusual TLS characteristics (certificate details, client fingerprint hashes such as JA3/JA4), and long-lived connections. Confirm with endpoint telemetry (which process). Many benign updaters also beacon, so baseline.
- **Common mistakes:** concluding from one signal.
- **Follow-ups:** traffic goes to a large cloud provider; how do you separate good from bad?
</details>

**Q23 · NG · What do SPF, DKIM and DMARC each do, and how do you roll out DMARC safely?**

<details><summary>Answer guide</summary>

- **Testing:** email authentication.
- **Strong answer:** SPF lists servers allowed to send for a domain (checked against the envelope sender); DKIM signs messages so receivers verify integrity and the signing domain; DMARC requires SPF or DKIM to pass and align with the visible From domain, sets a policy (none, quarantine, reject) and sends reports. Roll out: publish `p=none` with reporting, find all legitimate senders (marketing tools, ticketing systems), fix their alignment, then move to quarantine and reject gradually.
- **Common mistakes:** jumping to `p=reject` and blocking your own invoices.
- **Follow-ups:** a look-alike domain is used for phishing; does DMARC help?
</details>

### AI-era judgement

**Q24 · Mid · An AI assistant in your SIEM summarises an incident and concludes "benign, no action". What do you check before closing?**

<details><summary>Answer guide</summary>

- **Testing:** verification of AI output in security.
- **Strong answer:** read the raw evidence the summary cites; check whether it considered all relevant data sources (it may have seen only part of the logs); verify facts it states (IP ownership, process names, timestamps); look for the specific signals that would change the conclusion; document your own reasoning in the ticket. Track how often the assistant's verdicts are overturned, to calibrate trust. Treat attacker-controlled content in logs (for example email bodies) as untrusted input to the assistant.
- **Common mistakes:** closing on the summary alone.
- **Follow-ups:** how would you evaluate an AI triage assistant before rolling it out?
</details>

**Q25 · Mid · Review this AI-written detection query.** The intent: alert when a user signs in successfully from a country they have never used.

```kusto
SigninLogs
| where ResultType == 0
| where Location != "IN"
| summarize count() by UserPrincipalName
| where count_ > 5
```

<details><summary>Answer guide</summary>

- **Testing:** detection logic review.
- **Strong answer:** it does not implement the intent: it hard-codes India as normal (missing attackers in India and flagging every legitimate traveller), requires more than five sign-ins (a single malicious login passes), has no per-user history, and no explicit time window. Fix: build a per-user baseline of countries over, say, 30 days; alert on a successful sign-in from a country not in that user's baseline within the last hour; enrich with MFA details, device, IP reputation; exclude known corporate egress. Test against historical data for volume before enabling.
- **Common mistakes:** tweaking the threshold only.
- **Follow-ups:** the alert volume is still too high for travellers; what context reduces it?
</details>

**Q26 · Sr · The company deploys an internal LLM assistant over its documents. What security controls do you require?**

<details><summary>Answer guide</summary>

- **Testing:** securing AI systems defensively.
- **Strong answer:** retrieval must enforce the user's existing document permissions; treat document content and user input as untrusted (prompt injection is a top risk in the OWASP Top 10 for LLM Applications); limit tools and actions the assistant can take, with human approval for sensitive actions; data-loss controls for outputs; no training on sensitive data without approval; logging and monitoring of prompts and responses with privacy rules; vendor and data-residency review; red-teaming and evaluation before launch; an incident process for harmful outputs.
- **Common mistakes:** one service account with access to every document.
- **Follow-ups:** how do you detect that a document contains instructions aimed at the assistant?
</details>

### Behavioural

**Q27 · Mid · Tell me about explaining a security risk to a non-technical decision-maker.**

<details><summary>Answer guide</summary>

- **Testing:** risk communication.
- **Strong answer:** the risk in business terms (likelihood, impact in money, customers or regulation); options with cost and residual risk; your recommendation; the decision made and how you recorded it (including accepted risk); what happened next.
- **Common mistakes:** jargon; fear without options.
- **Follow-ups:** they accepted the risk and it later materialised; what did you do?
</details>

## Sources

Checked October 2026.

- NIST SP 800-61 (incident handling; Revision 3, 2025): https://csrc.nist.gov/pubs/sp/800/61/r3/final ; NIST SP 800-207 (zero trust architecture): https://csrc.nist.gov/pubs/sp/800/207/final ; NIST Cybersecurity Framework 2.0: https://www.nist.gov/cyberframework
- CERT-In, *Directions under section 70B(6) of the IT Act, 2000* (28 Apr 2022): https://www.cert-in.org.in/
- CISA, *Known Exploited Vulnerabilities Catalog*: https://www.cisa.gov/known-exploited-vulnerabilities-catalog ; FIRST, *EPSS*: https://www.first.org/epss/
- MITRE ATT&CK: https://attack.mitre.org/
- OWASP, *Top 10 for Large Language Model Applications*: https://genai.owasp.org/
- Loop structure: [SEC role page](../../01_market_map/roles/SEC_cybersecurity_defense.md).

_Last reviewed: 2026-10_
