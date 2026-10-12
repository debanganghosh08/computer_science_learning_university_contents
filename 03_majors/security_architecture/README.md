# Security Architecture (SAR)

**Years 3–5 · 10 major courses · Entry requirements: [CS213 Security Foundations](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) and [CS212 Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) · Levels L2 → L5**

Security architects design systems and organisations so that attacks are hard, damage is contained and recovery is fast. They decide where trust boundaries sit, which controls are mandatory, how identity, keys and data flow, how software is built and verified, how AI agents are allowed to act, and which risks a business may accept, and they write those decisions down so that hundreds of engineers can build on them. This major teaches that work from first principles to frontier research, using standards (NIST, OWASP, ISO, IETF), real incidents and Indian regulation (CERT-In, the DPDP Act, RBI, UIDAI) as design inputs.

It sits between three neighbours. [Cybersecurity Defense](../cybersecurity_defense/README.md) (SEC) runs security operations, incident response and governance programmes; [Ethical Hacking](../ethical_hacking_offensive_security/README.md) (OFF) tests systems under authorization; [Cloud Engineering](../cloud_engineering/README.md) (CLD) builds the infrastructure. Security Architecture designs: it takes their findings, constraints and platforms and turns them into architectures, standards, reviews and strategy.

## 1. Who this major is for, and the roles it leads to

Choose this major if you like seeing the whole system, enjoy arguing trade-offs in writing, and want work where judgement matters more than speed of typing. Security architecture is rarely an entry-level job: most people arrive after several years as security, cloud, backend or identity engineers ([SAR market page](../../06_career_and_market_readiness/01_market_map/roles/SAR_security_architecture.md)). This major gives you the depth those people build over years, plus portfolio evidence, so that your first roles (security engineer, cloud security engineer, application or product security engineer, IAM engineer) lead quickly to architect titles.

| Role | What people in it actually do |
|---|---|
| Security architect | Review designs before they are built, write security requirements and standards, run threat-modeling sessions, define reference architectures and guardrails, record risk acceptances |
| Cloud security architect | Design multi-account guardrails, IAM, data perimeters, network security, key management and logging for cloud estates; govern what automation and agents may change |
| Application security architect / product security engineer | Embed security into the delivery pipeline (SAST, SCA, provenance, signing), build paved roads and secure frameworks, review high-risk features, run vulnerability management |
| Identity architect | Design workforce, customer, workload and agent identity: IdPs, federation, token architecture, authorization services, e-KYC integration, passkeys |
| Zero trust architect | Plan and sequence the move from network-based trust to per-request identity, device and context decisions; measure maturity |
| AI security architect (emerging) | Design data boundaries, tool permissions, sandboxes, connector trust and approval for LLM applications and agents; map them to AI governance frameworks |
| Cryptography and PQC migration lead (emerging) | Inventory cryptography, choose primitives and key custody, run certificate automation and post-quantum migration programmes |
| Head of security architecture / security engineering lead | Run the architecture review board, own reference architectures, lead architects and security engineers, set technical strategy |
| Deputy CISO / CISO | Own security strategy, budget, risk communication to the board and regulators, crisis leadership |

## 2. How AI is changing security architecture

All figures were checked in October 2026; paragraphs marked **Analysis** are interpretation.

**Demand is shifting to AI and cloud skills.** In ISC2's 2025 study of 16,029 professionals, AI (41%) and cloud security (36%) were the most-cited skills needs ([ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study)); in its September 2026 India study the top needs were AI (52%), cloud security (43%) and application security (38%) ([ISC2 India](https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai)). In an informal ISC2 poll (September 2026), 68% chose AI governance and compliance as the most important area to define, a weak but consistent signal ([ISC2](https://www.isc2.org/insights/2026/09/ai-governance-emerges-as-top-priority)). The World Economic Forum lists Security Management Specialists among the fastest-growing jobs to 2030, including in India ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).

**Architecture tasks are being automated in preview.** AWS Security Agent previewed design review against requirement packs (NIST CSF, PCI DSS, Well-Architected) in December 2025, added full-repository code review in May 2026 and STRIDE threat modeling from design documents or code on 17 June 2026, usable from coding tools such as Kiro and Claude Code ([AWS](https://aws.amazon.com/blogs/aws/new-aws-security-agent-secures-applications-proactively-from-design-to-deployment-preview/); [AWS](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-security-agent-threat-modeling/)). Open-source tools (AWS Labs' Threat Designer, STRIDE GPT) generate threat models from diagrams.

**Reliability is the limit.** Five LLMs classifying six 5G threats with STRIDE reached at most 72% accuracy ([arXiv 2505.04101](https://arxiv.org/abs/2505.04101)); a May 2026 study found that bigger or domain-adapted models gave gains "neither consistent nor sufficient for reliable threat modelling" ([arXiv 2605.10808](https://arxiv.org/abs/2605.10808)). When generating code, models chose the insecure implementation in 45% of security-relevant tasks in Veracode's 2025 study ([Veracode](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/)).

**AI systems are a new thing to secure.** OWASP published a Top 10 for Agentic Applications in December 2025 ([OWASP](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)); CISA, NSA and four partner agencies published *Careful adoption of agentic AI services* in 2026, advising limited agent privileges and human approval for decision-making steps ([CISA](https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai)); the Model Context Protocol's specification now carries detailed security requirements for connector servers ([MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)).

| Being automated | Augmented (human decides) | Growing in value |
|---|---|---|
| First-draft threat models, policy documents and control mappings; configuration scanning against benchmarks; summarising standards and vendor documents; first-pass code review | Design reviews (AI lists candidate threats, the architect decides), IAM and policy authoring with automated checks, evidence gathering, tabletop facilitation | Securing AI systems and agents; identity for workloads and agents; post-quantum migration planning; resilience and recovery design; risk sign-off and board communication; reasoning about new system classes from first principles |

**Analysis.** AI makes security documents cheap, so the reviewer's judgement becomes the scarce part ([SAR market page](../../06_career_and_market_readiness/01_market_map/roles/SAR_security_architecture.md)). Every course in this major therefore includes AI-off drills, a verification method, and a demonstrated failure mode of current tools, and three courses (SAR302, SAR403, SAR501) treat AI systems themselves as the object of design.

## 3. The 5-year path

### Years 1–2: the common core (courses that matter most for this major in bold)

| Year · Semester | Courses |
|---|---|
| 1 · 1 | FND101 Programming I, FND102 How Computers Work, **[FND103 Discrete Mathematics](../../01_year_1_foundations/semester_1/FND103_discrete_mathematics_for_computing/README.md)**, **[FND104 The Developer's Toolkit](../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md)**, **[FND105 AI-Native Learning and Building](../../01_year_1_foundations/semester_1/FND105_ai_native_learning_and_building/README.md)**, **[FND106 Technical Communication](../../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md)** |
| 1 · 2 | FND111 Programming II, FND112 DSA I, FND113 Linear Algebra and Calculus, **[FND114 Web Foundations](../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md)**, **[FND115 Databases I](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md)**, FND116 Probability and Statistics |
| 2 · 3 | CS201 Algorithms, CS202 Architecture and C, **[CS203 Operating Systems](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md)**, **[CS204 Computer Networks](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md)**, **[CS205 Software Engineering I](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md)**, CS206 Maths for ML |
| 2 · 4 | CS211 Database Internals, **[CS212 Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md)**, **[CS213 Security Foundations](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md)**, CS214 ML Foundations, **[CS215 Cloud and DevOps Foundations](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md)**, CS216 Compilers |

Why these matter: discrete maths (FND103) underpins cryptography; operating systems and networks (CS203, CS204) explain isolation, segmentation and TLS; distributed systems (CS212) explain consistency, failure and replication, which shape authorization, key rotation and recovery; CS213 is the gateway to this major; CS215 is the base for cloud security; technical communication (FND106) is half of an architect's job.

### Years 3–5: the major

| Year · Semester | Major courses | Shared and other courses |
|---|---|---|
| 3 · 5 | [SAR301 Security Architecture Principles and Frameworks](year_3/SAR301_security_architecture_principles_and_frameworks/README.md) · [SAR302 Threat Modeling](year_3/SAR302_threat_modeling/README.md) · [SAR303 Zero Trust Architecture](year_3/SAR303_zero_trust_architecture/README.md) | [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) |
| 3 · 6 | [SAR304 Applied Cryptography and PKI for Architects](year_3/SAR304_applied_cryptography_and_pki_for_architects/README.md) · [SAR305 Secure SDLC and DevSecOps Architecture](year_3/SAR305_secure_sdlc_and_devsecops_architecture/README.md) | [CAR301 Career Lab I](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) · one elective |
| 4 · 7 | [SAR401 Cloud Security Architecture](year_4/SAR401_cloud_security_architecture/README.md) · [SAR402 Identity Architecture at Scale](year_4/SAR402_identity_architecture_at_scale/README.md) | [IND401 Industry Co-op Studio](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) · overlap course 1 |
| 4 · 8 | [SAR403 Security Architecture for AI Systems and Agents](year_4/SAR403_security_architecture_for_ai_systems_and_agents/README.md) · [SAR404 Resilience, Business Continuity and Security Strategy](year_4/SAR404_resilience_business_continuity_and_security/README.md) | [CAR401 Career Lab II](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) · overlap course 2 |
| 5 · 9 | [SAR501 Frontier Seminar: Post-Quantum Migration and Securing Autonomous Systems](year_5/SAR501_frontier_seminar_post_quantum_migration/README.md) | [RES501 Research Methods](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) · [RES502 Reading, Reproducing and Extending Papers](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) · [THS501 Thesis or Capstone I](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |
| 5 · 10 | — | [THS502 Thesis or Capstone II](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) · [LCH502 Career Launch and Founder Studio](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) · one elective |

Course dependencies inside the major: SAR301 → SAR401; SAR302 → SAR402; SAR303 → SAR403; SAR304 → SAR404; SAR401 and SAR403 → SAR501. Each course also lists recommended earlier courses (for example, SAR402 for SAR403). Projects are designed to accumulate: the threat models, reference architectures, pipelines, identity platform and resilience designs you build in Years 3 and 4 become the flagship dossier below.

## 4. Skill map by level

| Level | You can… | Where you get it |
|---|---|---|
| L0 | Use Linux, Git and the web; explain what a password hash and HTTPS do; follow a security checklist | FND104, FND114 |
| L1 | Explain the CIA triad, STRIDE, TLS, OAuth and the OWASP Top 10; fix common web flaws in legal labs | CS204, CS213 |
| L2 (intern-ready) | Threat-model a small system, write testable security requirements, harden a pipeline, choose primitives correctly, configure least-privilege access in one cloud account | CS213, SAR301–SAR303 (first half) |
| L3 (job-ready) | Review real designs and find principle-level flaws; run threat-modeling sessions; design zero trust access, key management and PKI automation; build a DevSecOps control map with provenance and signing; secure a cloud estate's guardrails, IAM and data perimeters | SAR301–SAR305, SAR401, CAR301 |
| L4 (expert, hard to replace) | Design identity and authorization at scale, secure AI agent platforms, design ransomware-resilient recovery, write and defend a security strategy and budget to a board, lead an architecture review board | SAR402–SAR404, IND401, CAR401 |
| L5 (research and frontier) | Plan post-quantum migration programmes, design bounded autonomy for agents and cyber-physical systems, use automated reasoning, publish reproducible research | SAR501, RES501, RES502, THS501–THS502 |

Each course states its own mastery gate. The major's overall gate is the flagship project.

## 5. Recommended overlaps and electives

**Overlap specialisations** (Year 4; the SAR course in each is already part of this major, so take the other two):

- [OV01 Cloud Security](../../04_overlaps/OV01_cloud_security/README.md) (CLD301 + SAR401 + SEC303): take [CLD301](../cloud_engineering/year_3/CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md) and [SEC303](../cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md). The most direct route to cloud security architect roles.
- [OV03 DevSecOps](../../04_overlaps/OV03_devsecops/README.md) (OPS301 + SAR305 + SEC302): take [OPS301](../devops_sre_platform_engineering/year_3/OPS301_ci_cd_engineering/README.md) and [SEC302](../cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md). For product security and security engineering lead roles.
- [OV05 AI Security and Safety](../../04_overlaps/OV05_ai_security_safety/README.md) (AIE305 + OFF403 + SAR403): take [AIE305](../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md) and [OFF403](../ethical_hacking_offensive_security/year_4/OFF403_ai_and_llm_red_teaming/README.md). For AI security architect roles.
- [OV07 Privacy Engineering](../../04_overlaps/OV07_privacy_engineering/README.md) (DEN404 + SEC305 + PRO301): take [DEN404](../data_engineering/year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md) and [SEC305](../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md). For identity, data protection and privacy architect roles under the DPDP Act and GDPR.

**Electives** (choose by target role):

| Target | Electives |
|---|---|
| Identity architect | [SEC303 Identity and Access Management](../cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md), [BE305 Authentication, Authorization and Backend Security](../backend_engineering/year_3/BE305_authentication_authorization_and_backend/README.md) |
| Cloud security architect | [CLD302 Infrastructure as Code](../cloud_engineering/year_3/CLD302_infrastructure_as_code_terraform_opentofu/README.md), [CLD303 Containers and Kubernetes](../cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md) |
| Application and product security | [OFF302 Web Application Security Testing](../ethical_hacking_offensive_security/year_3/OFF302_web_application_security_testing/README.md), [SWE301 Software Architecture and Design Patterns](../software_engineering/year_3/SWE301_software_architecture_and_design_patterns/README.md) |
| Attacker intuition (authorized only) | [OFF301 Ethics, Law, Rules of Engagement and Methodology](../ethical_hacking_offensive_security/year_3/OFF301_ethics_law_rules_of_engagement_and_methodology/README.md) |
| AI security | [AIE304 Tool Use and AI Agents](../ai_engineering/year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md), [AIE401 Multi-Agent Systems, MCP and Orchestration](../ai_engineering/year_4/AIE401_multi_agent_systems_mcp_and_orchestration/README.md) |
| Strategy and governance | [SEC305 Governance, Risk and Compliance](../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md), [NET404 Enterprise Architecture and Cloud Migration](../it_infrastructure_networking/year_4/NET404_enterprise_architecture_and_cloud_migration/README.md) |
| FinTech and payments | [BE401 Payments-Grade Systems](../backend_engineering/year_4/BE401_payments_grade_systems_transactions_idempotency/README.md) |
| IoT, OT and devices | [EMB402 Embedded and IoT Security](../embedded_systems_iot/year_4/EMB402_embedded_and_iot_security/README.md) |

## 6. Flagship industry project

The flagship project is specified in [06_career_and_market_readiness/05_industry_projects/SAR_security_architecture.md](../../06_career_and_market_readiness/05_industry_projects/SAR_security_architecture.md). It joins the course projects into one architecture dossier for an *illustrative* regulated platform, for example a UPI-style payments company with an AI support agent:

- a design review pack and SABSA and CSF 2.0 profiles (SAR301);
- a full threat model, including the agent (SAR302);
- zero trust access and a migration roadmap (SAR303);
- key management, PKI automation and a post-quantum plan (SAR304);
- a verifiable delivery pipeline (SAR305);
- a tested cloud foundation (SAR401);
- an identity and authorization platform with e-KYC integration (SAR402);
- the agent platform design (SAR403);
- a resilience architecture, strategy and board paper (SAR404).

You defend it to a panel playing engineering leads, a regulator and a board. It is the portfolio piece you take to architect interviews.

## 7. Certifications worth having (optional, never required)

**Honest value note.** Architect hiring weighs experience and evidence of designs you have reviewed, built and defended; your SAR301 P3, SAR302 P3 and the flagship dossier say more than any badge. Certifications help with résumé filters, consulting and services firms, government and regulated-sector roles, and some employers list them in architect job descriptions. The senior ones (CISSP, CCSP, ISSAP) require years of paid experience, so they are career-stage goals, not student goals. During the degree, at most one cloud security certification is worth the time. Check the current exam outline before booking: several changed in 2025–2026.

| Certification (October 2026) | Best timed after | Note |
|---|---|---|
| ISC2 CISSP | 5 years of experience (or "Associate of ISC2" before that) | Broad management-level certification; frequently requested for senior security roles |
| ISC2 CISSP-ISSAP (architecture concentration) | CISSP plus architecture experience | Outline revised in 2025: governance and risk, security architecture modelling, infrastructure and system security architecture, IAM architecture |
| ISC2 CCSP | SAR401 plus experience | New exam outline effective 1 August 2026 |
| SABSA Chartered Foundation (SCF) → Practitioner (SCP) → Master (SCM) | SAR301 | The only certification path specific to enterprise security architecture; strongest in enterprises that use SABSA |
| TOGAF Enterprise Architecture Foundation / Practitioner; The Open Group "Integrating Risk and Security" credential | SAR301, NET404 | Useful where security architects sit inside enterprise architecture teams |
| AWS Certified Security – Specialty (SCS-C03) | SAR401 | 170 minutes, 65 questions, US$300 |
| Microsoft Certified: Cybersecurity Architect Expert (SC-100) | SAR401, SAR402 | Requires an associate certification first (identity, security operations, or cloud and AI security engineer); English exam updated 21 October 2026 |
| Google Cloud Professional Cloud Security Engineer | SAR401 | Check the current exam guide on Google Cloud's site |
| CSA Certificate of Cloud Security Knowledge (CCSK) | SAR401 | Vendor-neutral cloud security knowledge; current version unconfirmed, check CSA's site |

## 8. The interview loop for security architecture roles

A typical loop for experienced hires, from the [SAR market page](../../06_career_and_market_readiness/01_market_map/roles/SAR_security_architecture.md) (varies by employer):

1. **Deep dive into architectures you designed:** decisions, trade-offs, what failed. Prepare with your SAR301, SAR401 and SAR402 projects and ADRs.
2. **Design review exercise:** "here is a payments service or an AI agent with tool access; find the risks and propose controls" (SAR301 Chapter 11, SAR403).
3. **Live threat modeling with an engineering team** (SAR302 final exam format).
4. **Risk communication scenario:** present a risk and a recommendation to a non-technical executive (SAR404 Chapter 11).
5. **Behavioural:** influencing without authority, handling pushback from delivery teams (SAR301 Chapter 11).

Employers differ on AI use in interviews: some allow or expect AI tools, others forbid them; read the instructions for each round. See the [AI-driven interviews section](../../06_career_and_market_readiness/04_ai_driven_interviews/) for how these rounds work and for simulation question banks, and practise full loops in [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md).

## 9. Fast track for working professionals

Budget about 15 hours a week. Take the mastery-gate tests of CS213 and CS212 first; if you pass, start directly.

| You are now | Path (about 6–9 months) | Proof to build |
|---|---|---|
| Senior backend or software engineer | SAR301 → SAR302 → SAR305 → SAR402 | SAR302 P3 and SAR305 P3 |
| Cloud or platform engineer | SAR301 → SAR303 → SAR401 → SAR304 (Chapters 3–8) | SAR401 P3 |
| SOC analyst or security engineer (SEC) | SAR301 → SAR302 → SAR303 → SAR401 | SAR301 P3 and SAR303 P3 |
| GRC, audit or risk professional | SAR301 → SAR302 → SAR404 → SAR303 (Chapters 1–2, 10) | SAR404 P3 and a design review pack |
| Penetration tester or AppSec engineer (OFF) | SAR301 → SAR305 → SAR403 → SAR402 | SAR403 P3 |
| Identity or IAM engineer | SAR302 → SAR402 → SAR303 → SAR403 Chapters 5 and 7 | SAR402 P3 |
| ML or AI engineer moving into AI security | SAR302 → SAR403 → SAR402 Chapter 10 → SAR305 Chapter 12 | SAR403 P3 |

Finish with the flagship project and [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) for interview preparation.

## Sources

All checked 12 Oct 2026.

- [SAR market page](../../06_career_and_market_readiness/01_market_map/roles/SAR_security_architecture.md) and [market map](../../06_career_and_market_readiness/01_market_map/README.md) (roles, hiring loop, demand signals; checked Oct 2026).
- ISC2, 2025 Cybersecurity Workforce Study (4 Dec 2025) — https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study ; India study (24 Sep 2026) — https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai ; AI governance poll (25 Sep 2026) — https://www.isc2.org/insights/2026/09/ai-governance-emerges-as-top-priority
- WEF, Future of Jobs Report 2025 — https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- AWS Security Agent: preview with design review (Dec 2025) — https://aws.amazon.com/blogs/aws/new-aws-security-agent-secures-applications-proactively-from-design-to-deployment-preview/ ; full repository code review (May 2026) — https://aws.amazon.com/about-aws/whats-new/2026/05/aws-security-agent-full-repository-code-review/ ; threat modeling (17 Jun 2026) — https://aws.amazon.com/about-aws/whats-new/2026/06/aws-security-agent-threat-modeling/
- AbdulGhaffar and Matrawy (arXiv 2505.04101, 2025) — https://arxiv.org/abs/2505.04101 ; Pourhanifeh, AbdulGhaffar and Matrawy (arXiv 2605.10808, May 2026) — https://arxiv.org/abs/2605.10808
- Veracode 2025 GenAI Code Security Report (30 Jul 2025) — https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/
- OWASP Top 10 for Agentic Applications (9 Dec 2025) — https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ ; CISA and partners, *Careful adoption of agentic AI services* (1 May 2026) — https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai ; MCP security best practices (2026-07-28) — https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices
- Certifications: ISC2 ISSAP outline (2025) — https://www.isc2.org/certifications/issap/issap-certification-exam-outline ; ISC2 CCSP refresh (Jun 2026; effective 1 Aug 2026) — https://www.isc2.org/insights/2026/06/isc2-ccsp-exam-outline-revised ; ISC2 CISSP — https://www.isc2.org/certifications/cissp ; SABSA certification — https://sabsa.org/certification/ ; The Open Group TOGAF certifications — https://www.opengroup.org/certifications/togaf ; AWS Certified Security – Specialty — https://aws.amazon.com/certification/certified-security-specialty/ ; Microsoft Cybersecurity Architect Expert (page updated Sep 2026) — https://learn.microsoft.com/en-us/credentials/certifications/cybersecurity-architect-expert/ ; Google Cloud certifications — https://cloud.google.com/learn/certification ; CSA CCSK — https://cloudsecurityalliance.org/education/ccsk

_Last reviewed: 2026-10_
