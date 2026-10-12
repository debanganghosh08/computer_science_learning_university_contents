# SAR · Security Architecture: roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [Security Architecture major](../../../03_majors/security_architecture/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

Security architecture is rarely an entry-level job. People usually arrive after several years as security engineers, cloud engineers or backend engineers.

| Level | Common titles |
|---|---|
| Feeder roles | Security Engineer, Cloud Security Engineer, Application Security Engineer, IAM Engineer |
| Architect | Security Architect, Cloud Security Architect, Application Security Architect, Identity Architect |
| Senior | Principal Security Architect, Enterprise Security Architect, Zero Trust Architect |
| Leadership | Head of Security Architecture, Deputy CISO, CISO |

## What the work looks like day to day

- Run threat-modelling sessions for new systems using STRIDE or attack trees (SAR302).
- Review designs before they are built and write the security requirements.
- Define reference architectures and guardrails: network segmentation, identity, encryption, logging (SAR301).
- Plan zero trust adoption following NIST SP 800-207 (SAR303).
- Make cryptography and PKI decisions: key management, certificate lifecycles, and migration to post-quantum algorithms such as NIST FIPS 203 (ML-KEM) (SAR304, SAR501).
- Secure the software delivery pipeline: signing, provenance, dependency policy (SAR305).
- Review AI systems and agents: what data they see, what tools they can call, and what approval they need (SAR403).
- Explain risk to leadership in business terms and record risk acceptances.

## Demand signals

**No official occupation is called "security architect".**

- **Global employer survey.** Security Management Specialists are the fifth fastest-growing job to 2030; WEF attributes this partly to geopolitical fragmentation as well as technology ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)). WEF also lists Security Management Specialists among India's fastest-growing roles.
- **Architecture-level skills gaps.** In 2024, zero trust was cited as a skills gap by 27% and cloud computing by 30% ([ISC2 2024](https://www.isc2.org/Insights/2024/09/Employers-Must-Act-Cybersecurity-Workforce-Growth-Stalls-as-Skills-Gaps-Widen)). In 2025, AI (41%) and cloud security (36%) led all skills needs ([ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study)). In India, cloud security was cited by 43% ([ISC2 India, Sept 2026](https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai)).
- **US proxies.** Information security analysts +21% and computer network architects +8% from 2025 to 2035 ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm); [BLS](https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm)).
- **AI governance.** In an informal ISC2 LinkedIn poll of more than 500 professionals (September 2026), 68% chose "AI governance and compliance" as the most important area to define, ahead of AI threat-modelling frameworks (16%) ([ISC2, Sept 2026](https://www.isc2.org/insights/2026/09/ai-governance-emerges-as-top-priority)). A self-selected poll is a weak signal, but it matches the AI skills needs above.

## How AI is changing the role

**Automated or mostly automated (analysis).** First drafts of threat models, policy documents and control mappings (for example mapping a design to ISO/IEC 27001 controls), configuration scanning against benchmarks, and summarising long vendor documentation.

**Augmented.** Design reviews (AI can list candidate threats; the architect decides which matter), architecture diagram analysis, evidence gathering for audits.

**Growing in value.**

- **Security of AI systems and agents.** Agents that read untrusted content and call tools combine access to data, exposure to attacker-controlled input and the ability to act. Deciding permissions, isolation and human approval for them is new architecture work (SAR403, overlap OV05).
- **Identity at scale.** Machine identities, workload identity and agent identities multiply (SAR402).
- **Post-quantum migration planning**: inventorying cryptography and sequencing changes (SAR501).
- **Accountability.** Someone must sign off on risk. That remains a human, and often a regulatory, responsibility.

**Analysis.** AI makes generating security documents cheap, which makes the reviewer's judgement the scarce part. Architects who can reason about a new system class, such as AI agents, from first principles are in short supply because there is little precedent to copy.

## Pay (indicative)

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Information security analysts (closest official occupation; architects sit at the top of this range) | Median $129,180; 90th percentile $199,850 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm) |
| US | Computer network architects | Median $134,050; 90th $202,680 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm) |
| India | Security Architect, IT | Average base ₹25.2 lakh (32 profiles, Nov 2025) | Self-reported, small sample | [Payscale](https://www.payscale.com/research/IN/Job=Security_Architect%2C_IT/Salary) |

The India sample is very small; treat it as a rough indication only.

## The hiring loop

Typical loop for experienced hires (varies by employer):

1. Deep dive into architectures you have designed: decisions, trade-offs, what failed.
2. Design review exercise: "here is an architecture for a payments service (or an AI agent with tool access); find the risks and propose controls."
3. Live threat-modelling session with an engineering team.
4. Scenario on risk communication: present a risk and a recommendation to a non-technical executive.
5. Behavioural: influencing without authority, handling pushback from delivery teams.

See [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- Threat modelling as a habit, not a document.
- Identity and access design across cloud, workforce and machines.
- Applied cryptography and PKI.
- Cloud and network architecture.
- Secure software supply chain practice.
- Standards literacy: NIST Cybersecurity Framework 2.0, ISO/IEC 27001, India's DPDP Act 2023.
- Writing and persuasion.

## Adjacent roles and transitions

- **Security engineering and operations** ([SEC](SEC_cybersecurity_defense.md)).
- **Cloud architecture**: overlap OV01 Cloud Security ([CLD](CLD_cloud_engineering.md)).
- **AI security and safety**: overlap OV05 ([AIE](AIE_ai_engineering.md)).
- **Enterprise architecture** (NET404, [NET](NET_it_infrastructure_networking.md)).
- **Privacy engineering**: overlap OV07.
- **Offensive security** for architects who want attacker intuition ([OFF](OFF_ethical_hacking_offensive_security.md)).

## Sources

All checked October 2026.

- WEF, Future of Jobs Report 2025. https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- ISC2, 2024 Cybersecurity Workforce Study (11 Sep 2024). https://www.isc2.org/Insights/2024/09/Employers-Must-Act-Cybersecurity-Workforce-Growth-Stalls-as-Skills-Gaps-Widen
- ISC2, 2025 Cybersecurity Workforce Study (4 Dec 2025). https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study
- ISC2, India's Cybersecurity Workforce (24 Sep 2026); AI governance LinkedIn poll (25 Sep 2026). https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai ; https://www.isc2.org/insights/2026/09/ai-governance-emerges-as-top-priority
- BLS, Occupational Outlook Handbook: Information Security Analysts; Computer Network Architects (2025–35; May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm ; https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm
- Payscale India: Security Architect, IT (self-reported; 12 Oct 2026). https://www.payscale.com/research/IN/Job=Security_Architect%2C_IT/Salary
- NIST SP 800-207, Zero Trust Architecture. https://csrc.nist.gov/pubs/sp/800/207/final ; NIST FIPS 203. https://csrc.nist.gov/pubs/fips/203/final

_Last reviewed: 2026-10_
