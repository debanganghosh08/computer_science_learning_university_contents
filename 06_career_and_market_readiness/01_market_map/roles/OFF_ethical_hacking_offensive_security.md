# OFF · Ethical Hacking and Offensive Security (Authorized Testing): roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [Ethical Hacking and Offensive Security major](../../../03_majors/ethical_hacking_offensive_security/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement. Everything in this family happens **only with written authorisation and an agreed scope**. Testing systems without permission is a crime in India (Information Technology Act, 2000) and almost everywhere else.

## Role titles and seniority ladder

| Level | Common titles |
|---|---|
| Entry | Junior Penetration Tester, Security Testing Analyst, Application Security (AppSec) Analyst, VAPT Analyst |
| Mid | Penetration Tester, Application Security Engineer, Cloud Security Tester |
| Senior | Senior Penetration Tester, Red Team Operator, Lead Consultant |
| Expert | Principal Security Consultant, Red Team Lead, Vulnerability Researcher, AI Red Team Lead |

"VAPT" (vulnerability assessment and penetration testing) is the common Indian job-posting term. Independent bug bounty work through platforms such as HackerOne, Bugcrowd or Intigriti runs alongside, under each programme's published rules.

## What the work looks like day to day

- Agree scope, rules of engagement and legal sign-off before any testing (OFF301).
- Test web applications and APIs against the OWASP Top 10 and OWASP API Security Top 10 classes of weakness (OFF302, OFF402).
- Assess internal networks, cloud accounts and containers for misconfiguration (OFF303, OFF304).
- Document each finding with evidence, business impact, severity (for example CVSS) and a fix.
- Present results to developers and managers, then retest fixes (OFF305).
- In red-team roles, emulate a realistic adversary over weeks and work with defenders (purple teaming) (OFF401).
- Increasingly: test AI and LLM applications for prompt injection, data leakage and unsafe tool use (OFF403).

## Demand signals

**No official occupation separates penetration testers.** They are usually counted with information security analysts.

- **US projections.** Information security analysts +21% from 2025 to 2035 ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm)).
- **Skills gaps.** In 2024, application security and penetration testing were each cited as a skills gap by 24% of security professionals ([ISC2 2024](https://www.isc2.org/Insights/2024/09/Employers-Must-Act-Cybersecurity-Workforce-Growth-Stalls-as-Skills-Gaps-Widen)). In India, application security was the third most-cited skills need (38%) in 2025 data ([ISC2 India, Sept 2026](https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai)).
- **Budget pressure.** Security budgets are tight: 36% of organisations saw budget cuts and 39% hiring freezes in 2025 ([ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study)). Testing work tied to compliance requirements tends to continue; discretionary red-team work is easier to cut (**analysis**).
- **No strong public data** was found on the number of penetration-testing jobs or bug-bounty earnings that meets this curriculum's sourcing standard.

## How AI is changing the role

**Automated or mostly automated (analysis).** Asset discovery summaries, first-pass vulnerability scanning output review, report formatting and finding write-ups, remediation guidance drafts, and explanation of unfamiliar code or protocols.

**Augmented.** Source-code review for security flaws, triage of large scanner outputs, hypothesis generation during testing. AI-assisted vulnerability discovery is an active research area (OFF501); this curriculum teaches it at the level of concepts, defences and responsible disclosure only.

**Growing in value.**

- Judgement about business impact: chaining low-severity issues into a real risk, and explaining it.
- Authorisation, scope discipline and legal awareness.
- Testing AI systems: LLM applications create new classes of weakness (prompt injection, excessive agency, improper output handling), described in the 2025 OWASP Top 10 for LLM Applications.
- Writing fixes developers can apply, and verifying them.

**Analysis.** Scanners have automated the easy findings for years, and AI extends that. Clients pay testers for what tools miss: logic flaws, authorisation errors and creative combinations, plus a trustworthy report. The same capabilities that help testers also help attackers, which raises demand for skilled defenders and authorised testers alike.

## Pay (indicative)

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Information security analysts (closest official occupation) | Median $129,180; 10th $75,090; 90th $199,850 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm) |
| India | Penetration Tester | Average base ₹5.1 lakh; base range ₹1.95–20 lakh; under 1 year ≈₹5.0 lakh total (127 profiles, Jun 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Penetration_Tester/Salary) |

Bug bounty income varies widely and no reliable public median exists; do not plan a career on bounty income alone.

## The hiring loop

Typical loop (varies by employer):

1. Fundamentals: HTTP, authentication and session handling, common web weakness classes, networking, Linux and Windows basics.
2. Practical assessment in a provided lab: find and document issues in an intentionally vulnerable application within scope.
3. Report review: you submit a sample report or write up a finding; clarity and accuracy are scored.
4. Ethics and legal scenario: "you find customer data outside scope; what do you do?"
5. Behavioural and client-communication round, especially for consulting firms.

Certifications (for example OSCP, CEH, PNPT, or cloud security certifications) are used as filters, particularly by Indian consultancies; public write-ups of legal practice (CTFs, PortSwigger Web Security Academy, Hack The Box) show skill. See [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- Deep understanding of HTTP, browsers, authentication and authorisation.
- Reading code in several languages to spot unsafe patterns.
- Networking, Active Directory concepts and cloud IAM.
- Report writing and risk communication.
- Ethics, law and rules of engagement.
- Security testing of AI and LLM applications.

## Adjacent roles and transitions

- **Defensive security and detection engineering** ([SEC](SEC_cybersecurity_defense.md)).
- **Application security engineering**: shifting left into the development process ([SAR](SAR_security_architecture.md), [QAE](QAE_software_quality_test_engineering.md)).
- **AI security and safety**: overlap OV05 ([AIE](AIE_ai_engineering.md)).
- **Vulnerability research and responsible disclosure** (OFF404).
- **Cloud security** ([CLD](CLD_cloud_engineering.md)).

## Legal practice environments

PortSwigger Web Security Academy, OWASP Juice Shop, TryHackMe, Hack The Box, OverTheWire and picoCTF.

## Sources

All checked October 2026.

- BLS, Occupational Outlook Handbook: Information Security Analysts (2025–35; May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm
- ISC2, 2024 Cybersecurity Workforce Study (11 Sep 2024). https://www.isc2.org/Insights/2024/09/Employers-Must-Act-Cybersecurity-Workforce-Growth-Stalls-as-Skills-Gaps-Widen
- ISC2, 2025 Cybersecurity Workforce Study (4 Dec 2025). https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study
- ISC2, India's Cybersecurity Workforce (24 Sep 2026). https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai
- Payscale India: Penetration Tester (self-reported; 12 Oct 2026). https://www.payscale.com/research/IN/Job=Penetration_Tester/Salary
- OWASP, Top 10 for LLM Applications (2025 version). https://genai.owasp.org/llm-top-10/

_Last reviewed: 2026-10_
