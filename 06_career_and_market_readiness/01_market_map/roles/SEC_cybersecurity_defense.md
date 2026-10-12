# SEC · Cybersecurity: Defense, Operations and Governance: roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [Cybersecurity Defense major](../../../03_majors/cybersecurity_defense/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

| Level | Common titles |
|---|---|
| Entry | SOC Analyst (Tier 1), Security Analyst, IT Security Associate, GRC Analyst |
| Mid | SOC Analyst (Tier 2/3), Security Engineer, Incident Responder, IAM Engineer, Vulnerability Management Analyst |
| Senior | Detection Engineer, Threat Hunter, DFIR Lead, Senior Security Engineer, GRC Manager |
| Leadership | Security Operations Manager, Head of Security, Chief Information Security Officer (CISO) |

GRC means governance, risk and compliance. DFIR means digital forensics and incident response.

## What the work looks like day to day

- Triage alerts in a SIEM (security information and event management system) and decide what is real (SEC302).
- Investigate: pivot across endpoint, identity, network and cloud logs.
- Write and tune detection rules, mapped to MITRE ATT&CK techniques (SEC401).
- Run incident response: contain, eradicate, recover, report (SEC402).
- Review access and run identity governance (SEC303).
- Prepare compliance evidence (ISO/IEC 27001, SOC 2, India's DPDP Act 2023) and run risk assessments (SEC305).

## Demand signals

- **US projections.** Information security analysts: 192,900 jobs, +21% from 2025 to 2035, about 14,100 openings a year. BLS says "increased use of artificial intelligence (AI) and the rise of e-commerce have increased the need for enhanced security" ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm)).
- **Global employer survey.** Security Management Specialists rank fifth and Information Security Analysts are in the top 15 fastest-growing jobs to 2030. "Networks and cybersecurity" is the second fastest-growing skill ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).
- **Skills, not headcount.** In ISC2's 2025 study (16,029 respondents), 95% reported at least one skills need and 59% called their needs critical or significant. AI was the top need (41%), then cloud security (36%) and risk assessment (29%). But 24% saw layoffs, 39% hiring freezes and 36% budget cuts, and ISC2 "has not included an estimate of the cybersecurity workforce gap this year" ([ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study)).
- **Entry is hard.** In 2024, 31% of respondents said their security teams had no entry-level professionals ([ISC2 2024](https://www.isc2.org/Insights/2024/09/Employers-Must-Act-Cybersecurity-Workforce-Growth-Stalls-as-Skills-Gaps-Widen)). Among 21–29-year-olds in 2025, 38% entered through an IT pathway and 23% through a cybersecurity degree ([ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study)).
- **India.** Among 524 Indian respondents, "skills shortages have overtaken staffing shortages as the primary workforce concern". Top needs: AI 52%, cloud security 43%, application security 38%. Staffing shortages fell from 59% to 48%, but more than a third still saw layoffs ([ISC2 India, Sept 2026](https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai)).

## How AI is changing the role

**Adoption.** 28% of organisations have integrated AI security tools, 19% are testing them and 22% are evaluating them ([ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study)). In India, 85% of respondents whose teams adopted AI tools reported significant productivity improvements ([ISC2 India](https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai)).

**Automated or mostly automated (analysis).** Alert enrichment (who owns this host, is this IP known bad), phishing-report triage, first-draft incident summaries, query writing for log searches, compliance evidence collection.

**Augmented.** Investigations, threat hunting hypotheses, detection-rule writing and testing, malware triage for defenders (SEC403).

**Growing in value.**

- Judgement on containment: isolating a production system has business cost.
- Detection engineering as software engineering: tested, version-controlled rules.
- Identity and cloud security, where most modern incidents start.
- Securing AI systems themselves: prompt injection, data leakage through AI tools, agent permissions (SEC404, overlap OV05). ISC2 India respondents already report AI-driven social engineering (41%) and AI-related data leakage (31%).

**Analysis.** AI removes much of the repetitive Tier-1 work that used to train new analysts. Entry-level candidates now need to show investigation skill and some engineering (scripting, queries, cloud) from day one.

## Pay (indicative)

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Information security analysts | Median $129,180; 10th $75,090; 90th $199,850 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm) |
| India | Cyber Security Analyst | Average base ₹5.8 lakh; base range ₹2.05–20 lakh; under 1 year ≈₹4.7 lakh total (358 profiles, May 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Cyber_Security_Analyst/Salary) |
| India | Information Security Analyst | Average base ₹6.3 lakh (114 profiles, Jul 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Information_Security_Analyst/Salary) |

## The hiring loop

Typical loop (varies by employer):

1. Fundamentals screen: networking (TCP/IP, DNS, HTTP), Windows and Linux internals, authentication protocols.
2. Scenario: "here is an alert and some logs; what happened, and what do you do next?"
3. Hands-on: write a SIEM query, analyse a packet capture or event log in a lab.
4. Incident response tabletop: roles, communication, evidence handling.
5. Behavioural: ethics, handling pressure, explaining risk to non-specialists.

Certifications (CompTIA Security+, ISC2 CC, vendor SOC certifications) are common early-career filters. They signal knowledge; labs and write-ups show skill. See [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- Networking and operating-system internals.
- Log analysis and at least one query language (KQL, SPL or SQL).
- Scripting in Python or PowerShell.
- Identity: Active Directory, Entra ID, OAuth/OIDC, privileged access.
- Cloud security basics on one provider.
- Clear incident writing and risk communication.
- Security for AI systems.

## Adjacent roles and transitions

- **Offensive security**: purple teaming connects attack and defence ([OFF](OFF_ethical_hacking_offensive_security.md)).
- **Security architecture**: with experience ([SAR](SAR_security_architecture.md)).
- **Cloud security**: overlap OV01 ([CLD](CLD_cloud_engineering.md)).
- **DevSecOps**: overlap OV03 ([OPS](OPS_devops_sre_platform_engineering.md)).
- **Privacy engineering**: overlap OV07.
- **Network engineering** ([NET](NET_it_infrastructure_networking.md)), a common entry path.

## Sources

All checked October 2026.

- BLS, Occupational Outlook Handbook: Information Security Analysts (2025–35; May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm
- WEF, Future of Jobs Report 2025. https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- ISC2, 2024 Cybersecurity Workforce Study (11 Sep 2024). https://www.isc2.org/Insights/2024/09/Employers-Must-Act-Cybersecurity-Workforce-Growth-Stalls-as-Skills-Gaps-Widen
- ISC2, 2025 Cybersecurity Workforce Study (4 Dec 2025). https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study
- ISC2, India's Cybersecurity Workforce (24 Sep 2026). https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai
- Payscale India: Cyber Security Analyst; Information Security Analyst (self-reported; 12 Oct 2026). https://www.payscale.com/research/IN/Job=Cyber_Security_Analyst/Salary ; https://www.payscale.com/research/IN/Job=Information_Security_Analyst/Salary

_Last reviewed: 2026-10_
