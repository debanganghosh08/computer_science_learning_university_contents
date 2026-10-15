# IT Infrastructure and Network Engineering (NET)

**Years 3–5 · 10 major courses · Entry requirements: [CS204 Computer Networks](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md) and [CS203 Operating Systems](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) · Levels L2 → L5**

Infrastructure engineers build and run the networks, identity systems, servers, data centres and operations that every other team depends on: the campus Wi-Fi, the branch WAN, Active Directory and Entra ID, the data-centre fabric, the private links to the cloud, the firewall policy, and the processes that keep all of it running at 3 a.m. This major teaches enterprise IT infrastructure and network engineering as it is done in 2026: as code, tested before it ships, observed through telemetry, increasingly operated with AI assistance, and designed by people who can still reason from first principles when the tools are wrong.

It sits next to three neighbouring majors. [Cloud Engineering](../cloud_engineering/README.md) owns cloud platforms, infrastructure as code and cloud migration factories; [DevOps, SRE and Platform Engineering](../devops_sre_platform_engineering/) owns delivery pipelines, SLO-based reliability and service-level AIOps; [Cybersecurity](../cybersecurity_defense/README.md) owns security operations, detection and response. This major owns the enterprise estate itself: routing and switching, wireless and WAN, Windows and identity infrastructure, data centres and hybrid connectivity, network security engineering, IT service management, network automation and network AIOps, and the architecture that ties them together.

## 1. Who this major is for, and the roles it leads to

Choose this major if you like systems you can touch and measure, enjoy finding the one wrong line in a configuration, stay calm when everything is down, and want work that every organisation needs regardless of what software it sells.

| Role | What people in it actually do |
|---|---|
| Service desk / IT support engineer (entry) | Resolve user and device issues, handle access requests, escalate with good evidence; the most AI-exposed rung, so treat it as a short first step |
| NOC engineer | Watch monitoring for many networks, triage alerts, run first-response runbooks, coordinate with ISPs and field teams, often in 24×7 shifts |
| Network engineer | Design, configure and troubleshoot switching, routing (OSPF, BGP), VPNs, firewalls and WAN; run changes in maintenance windows |
| Systems administrator / infrastructure engineer | Run Windows and Linux servers, Active Directory and Entra ID, virtualisation, storage, backups and patching; automate everything repeatable |
| Wireless engineer | Design and survey Wi-Fi for offices, campuses, hospitals and warehouses; tune RF; integrate 802.1X and NAC |
| Network automation (NetDevOps) engineer | Build source-of-truth-driven pipelines, tests and telemetry for network change; integrate controllers and AI assistants safely |
| Data centre engineer | Build and operate spine-leaf fabrics, EVPN, hypervisor clusters, storage and hybrid interconnects; plan power, cooling and capacity |
| Network security engineer | Design segmentation, firewall policy, NAC and VPNs; harden devices; feed logs to the SOC; produce audit evidence |
| IT operations lead / manager | Run incident, problem and change processes, service desks and NOCs, SLAs and suppliers; report service health to the business |
| Solutions architect (vendor, partner or customer side) | Turn a customer's requirements into a network or infrastructure design, prove it in a lab, and support the build |
| Network / infrastructure / enterprise architect | Own target architectures, standards, migration roadmaps and business cases; decide what to keep, move, replace or retire |
| Telecom and 5G core engineer (specialist) | Run mobile cores, transport and private 5G networks for operators and large enterprises (NET501 is the starting point) |

The market page for this role family is [NET in the market map](../../06_career_and_market_readiness/01_market_map/roles/NET_it_infrastructure_networking.md).

## 2. How AI is changing infrastructure work

All figures were checked in October 2026; paragraphs marked **Analysis** are interpretation, not measurement.

**The official data shows a split.** The US Bureau of Labor Statistics projects computer network architects to grow 8% from 2025 to 2035, while network and computer systems administrators decline 4% and computer support specialists decline 3%. BLS gives the reasons: some administrator tasks are shifting to DevOps-focused developers and to outsourced network-as-a-service providers, and administrators are automating routine work; architect growth comes from new and upgraded networks, AI-driven infrastructure modernisation and the continued expansion of cloud computing. Administrators still have about 13,400 openings a year from retirements and job changes, and the median architect earned $134,050 in May 2025 against $99,130 for administrators ([BLS architects](https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm), [BLS administrators](https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm), [BLS support](https://www.bls.gov/ooh/computer-and-information-technology/computer-support-specialists.htm)). Indeed's US "IT Infrastructure, Operations & Support" postings index stood at 69.3 on 2 October 2026 (February 2020 = 100), up from 64.0 a year earlier; in the UK it fell to 45.8 from 55.6 ([Indeed Hiring Lab](https://github.com/hiring-lab/job_postings_tracker)). The World Economic Forum's employer survey ranks "networks and cybersecurity" as the second fastest-growing skill to 2030 ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).

**Vendors are putting agents inside the network.** HPE completed its purchase of Juniper Networks, whose Mist platform is built around AI-driven operations, on 2 July 2025 ([HPE](https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html)). In February 2026 Cisco announced "AgenticOps" for campus, branch and industrial networks: agents that reason "from telemetry to root cause", "autonomously" tune RF, QoS and paths, and run "risk-aware agentic assessments" of changes, with data-centre agents in controlled availability from June 2026 ([Cisco](https://newsroom.cisco.com/content/r/newsroom/en/us/a/y2026/m02/cisco-expands-agenticops-innovations-across-portfolio.html)). Service management is changing at the front line: Salesforce's CEO said in September 2025 that AI let the company cut customer-support headcount from about 9,000 to about 5,000 ([CNBC](https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html)), and PeopleCert introduced ITIL (Version 5) in 2026 as an "AI-native" framework ([PeopleCert](https://www.itil.com/Itil-News-and-Announcements/itil-version-5-foundation-whats-new-guide)).

**But AI is unreliable on network configuration, and automation causes the largest outages.** Researchers testing GPT-4 on router configuration found "egregious errors in topology, syntax, and semantics" unless automated verifiers fed back each error ([Mondal et al., 2023](https://arxiv.org/abs/2307.04945)); the NetConfEval benchmark (CoNEXT 2024) found low-level configuration generation feasible only with the largest models ([NetConfEval](https://github.com/NetConfEval/NetConfEval)). In October 2025 a race condition in AWS's own DNS automation left DynamoDB's us-east-1 endpoint with an empty DNS record ([AWS](https://aws.amazon.com/message/101925/)); in November 2025 a generated Cloudflare configuration file doubled in size and crashed its proxy ([Cloudflare](https://blog.cloudflare.com/18-november-2025-outage/)); the 2022 Rogers outage began with a removed route filter that the change process failed to flag ([CRTC review summary](https://mobilesyrup.com/2024/07/05/july-2022-rogers-outage-report-crtc/)).

| Being automated | Augmented (human decides) | Growing in value |
|---|---|---|
| First-line support answers, password resets, ticket classification and summaries, configuration templates, routine monitoring and patching, documentation | Troubleshooting with AI that reads telemetry, logs and topology; change-plan drafting; alert correlation; migration assessments; RF tuning | Network and infrastructure architecture for hybrid estates; automation with tests and safe rollout; verification of intent; segmentation and network security engineering; identity design; AI-cluster and data-centre fabrics; change-risk judgement; governing what agents may change |

**India.** India's tech workforce was 5.80 million in FY25 and about 6 million is projected for FY26; NASSCOM says providers are moving "away from FTE delivery to outcome-based, risk-sharing constructs" and expects FY27 hiring to shift "from volume to skill mix", which hits headcount-priced infrastructure-management contracts directly ([NASSCOM 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026)). Physical infrastructure is growing fast: Savills counted 258 MW of data-centre IT capacity added in the first half of 2026, taking India to about 1.8 GW, with more than 7 GW projected by 2030 ([Indian Infrastructure, July 2026](https://indianinfrastructure.com/2026/07/22/indias-data-centre-capacity-additions-grow-59-per-cent-in-h1-2026-says-industry-report/)); 5G base stations rose from 1,40,623 in March 2023 to 5,62,971 by 30 June 2026 ([Indian Infrastructure, July 2026](https://indianinfrastructure.com/2026/07/27/india-crosses-0-56-million-5g-base-stations-136-telecom-rd-projects-approved-says-minister-of-state-for-communications/)); and the lower 6 GHz band was delicensed for indoor Wi-Fi in January 2026 ([Indian Infrastructure, January 2026](https://indianinfrastructure.com/?p=265331)). Regulation shapes the work: CERT-In's 2022 directions require 6-hour incident reporting, 180 days of logs kept in India and clocks synced to NIC or NPL time sources ([CERT-In](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf)). Pay is modest at entry: Payscale shows an average base of ₹4.8 lakh for network engineers in India (491 self-reported profiles, July 2026) ([Payscale](https://www.payscale.com/research/IN/Job=Network_Engineer/Salary)). No strong public data on network-engineering job counts in India was found.

**Analysis.** The lowest rungs (service desk, routine administration, alert watching) are the most exposed, both to AI and to managed services, and the large Indian infrastructure-management workforce is exposed to the same pressure as contracts move to outcomes. The growing end is design, automation, security and architecture. This major therefore pushes every student towards that end early: automation from Year 3, AI-off fundamentals so you can judge AI output, measured evidence in every project, and an architecture course before graduation.

## 3. The 5-year path

### Years 1–2: the common core (courses that matter most for this major in bold)

| Year · Semester | Courses |
|---|---|
| 1 · 1 | **[FND101 Programming I (Python)](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md)**, **[FND102 How Computers Work](../../01_year_1_foundations/semester_1/FND102_how_computers_work_bits_hardware/README.md)**, FND103 Discrete Maths, **[FND104 The Developer's Toolkit: Linux, Shell, Git](../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md)**, FND105 AI-Native Learning, **[FND106 Technical Communication](../../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md)** |
| 1 · 2 | FND111 Programming II, FND112 DSA I, FND113 Linear Algebra and Calculus, **[FND114 Web Foundations](../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md)**, FND115 Databases I, FND116 Probability and Statistics |
| 2 · 3 | CS201 Algorithms, CS202 Architecture and C, **[CS203 Operating Systems](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md)**, **[CS204 Computer Networks](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md)**, CS205 Software Engineering I, CS206 Maths for ML |
| 2 · 4 | CS211 Database Internals, **[CS212 Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md)**, **[CS213 Security Foundations](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md)**, [CS214 ML Foundations](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) (useful for NET403), **[CS215 Cloud and DevOps Foundations](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md)**, CS216 Compilers |

Why these matter: CS204 is the foundation of every NET course and both entry requirements (CS204, CS203) gate the major; Python (FND101) and Linux with Git (FND104) are the daily tools of network automation; FND106 is where you learn to write the change plans, incident updates and design documents that this work runs on; CS213 and CS215 prepare you for NET402 and the hybrid half of NET401 and NET404.

### Years 3–5: the major

| Year · Semester | Major courses | Shared and other courses |
|---|---|---|
| 3 · 5 | [NET301 Routing and Switching](year_3/NET301_routing_and_switching/README.md) · [NET302 Windows Server, Active Directory and Enterprise IT](year_3/NET302_windows_server_active_directory_and_enterprise/README.md) · [NET303 Network Automation and NetDevOps](year_3/NET303_network_automation_and_netdevops/README.md) | [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) |
| 3 · 6 | [NET304 Wireless, SD-WAN and Enterprise Networks](year_3/NET304_wireless_sd_wan_and_enterprise_networks/README.md) · [NET305 IT Service Management and Operations](year_3/NET305_it_service_management_and_operations/README.md) | [CAR301 Career Lab I](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) · one elective |
| 4 · 7 | [NET401 Data Center and Hybrid Infrastructure](year_4/NET401_data_center_and_hybrid_infrastructure/README.md) · [NET402 Network Security Engineering](year_4/NET402_network_security_engineering/README.md) | [IND401 Industry Co-op Studio](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) · overlap course 1 |
| 4 · 8 | [NET403 AIOps and Intent-Based Networking](year_4/NET403_aiops_and_intent_based_networking/README.md) · [NET404 Enterprise Architecture and Cloud Migration](year_4/NET404_enterprise_architecture_and_cloud_migration/README.md) | [CAR401 Career Lab II](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) · overlap course 2 |
| 5 · 9 | [NET501 Frontier Seminar: 5G, Satellite Internet and Programmable Networks](year_5/NET501_frontier_seminar_5g_satellite_internet/README.md) | [RES501 Research Methods](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) · [RES502 Reading, Reproducing and Extending Papers](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) · [THS501 Thesis or Capstone I](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |
| 5 · 10 | — | [THS502 Thesis or Capstone II](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) · [LCH502 Career Launch and Founder Studio](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) · one elective |

Course dependencies inside the major: NET301 → NET401; NET302 → NET402; NET303 → NET403; NET304 → NET404; NET401 and NET403 → NET501. NET301–NET305 all require CS204 and CS203. Take NET301 and NET303 in the same semester: from week 1, every network you build by hand in NET301 should also exist as data and templates in NET303, so by Year 4 you own one lab estate (network, identity, monitoring, pipeline) that every later course extends.

## 4. Skill map by level

| Level | You can… | Where you get it |
|---|---|---|
| L0 | Use the shell and Git, explain what an IP address and a router are, follow a guide to set up a home router or a VM | FND102, FND104 |
| L1 | Explain TCP/IP, DNS, DHCP and routing; subnet IPv4 and IPv6 quickly; capture and read packets; write small Python scripts | FND101, CS204, CS203 |
| L2 (intern-ready) | Build multi-VLAN, multi-area OSPF and dual-ISP BGP networks in an emulator; run a two-site AD domain; automate audits with Netmiko and Ansible; troubleshoot with a stated method | NET301, NET302, NET303 |
| L3 (job-ready) | Design and survey enterprise Wi-Fi; build SD-WAN with measured failover; run incident, problem and change processes and monitoring that pages once; deliver network changes through tested pipelines; pass a vendor-style practical lab | NET304, NET305, CAR301 |
| L4 (expert, hard to replace) | Design EVPN data-centre fabrics and hybrid connectivity; engineer and prove segmentation, NAC and VPN controls; build and govern AI-assisted operations with verified intent; lead portfolio and migration decisions with business cases | NET401–NET404, IND401, CAR401 |
| L5 (research and frontier) | Reproduce and extend networking research (5G cores, LEO, P4, eBPF, verification, AI for networks); publish artifacts; contribute to standards or open-source networking | NET501, RES501, RES502, THS501–502 |

Each course states its own mastery gate. The major's overall gate is the flagship project below.

## 5. Recommended overlaps and electives

**Overlap specialisations** (Year 4, two courses each; check prerequisites, because each overlap borrows courses from another major):

- [OV01 Cloud Security](../../04_overlaps/OV01_cloud_security/README.md) (CLD301 + SAR401 + SEC303): for engineers moving from enterprise networks into cloud network security and identity. Cloud security was the second most-cited security skills need in ISC2's 2025 study ([ISC2](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study)). Build on NET302 and NET402.
- [OV03 DevSecOps](../../04_overlaps/OV03_devsecops/README.md) (OPS301 + SAR305 + SEC302): for network automation engineers who want pipelines, security checks and SOC integration as one discipline. Builds on NET303 and NET402.
- [OV09 Edge AI and Secure IoT](../../04_overlaps/OV09_edge_ai_secure_iot/README.md) (EMB401 + EMB402 + MLE404): for engineers who will connect and secure factories, hospitals, buildings and private 5G sites full of devices. Builds on NET304, NET402 and NET501; take EMB-major prerequisites as electives first.

**Electives** (choose by target role):

| Target | Electives |
|---|---|
| Cloud networking and hybrid | [CLD304 Cloud Networking](../cloud_engineering/year_3/CLD304_cloud_networking_vpcs_dns_load_balancing/README.md), [CLD402 Multi-Cloud, Hybrid Cloud and Migration](../cloud_engineering/year_4/CLD402_multi_cloud_hybrid_cloud_and_migration/README.md), [CLD403 FinOps](../cloud_engineering/year_4/CLD403_finops_and_cloud_cost_engineering/README.md) |
| Linux and operations | [OPS302 Linux Systems Administration in Depth](../devops_sre_platform_engineering/year_3/OPS302_linux_systems_administration_in_depth/README.md), [OPS303 Observability](../devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md), [OPS304 Site Reliability Engineering](../devops_sre_platform_engineering/year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md) |
| Automation and AIOps | [OPS305 Configuration Management and GitOps](../devops_sre_platform_engineering/year_3/OPS305_configuration_management_and_gitops/README.md), [OPS403 AIOps and Agentic Operations](../devops_sre_platform_engineering/year_4/OPS403_aiops_and_agentic_operations/README.md) |
| Security | [SEC301 Network Security and Defense](../cybersecurity_defense/year_3/SEC301_network_security_and_defense/README.md), [SEC302 Security Operations](../cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md), [SEC303 Identity and Access Management](../cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md), [SAR303 Zero Trust Architecture](../security_architecture/year_3/SAR303_zero_trust_architecture/README.md) |
| AI and data-centre infrastructure | [CLD404 AI Infrastructure in the Cloud](../cloud_engineering/year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md) |
| IoT and telecom | [EMB304 IoT Protocols and Cloud Connectivity](../embedded_systems_iot/year_3/EMB304_iot_protocols_and_cloud_connectivity/README.md) |

## 6. Flagship industry project

The major's flagship project is specified in [06_career_and_market_readiness/05_industry_projects/NET_it_infrastructure_networking.md](../../06_career_and_market_readiness/05_industry_projects/NET_it_infrastructure_networking.md): network-as-code for an illustrative Indian retail chain (head office, data centre, branches with dual WAN links, and a cloud network), with NetBox as the source of truth, configurations generated and deployed by a pipeline with automatic rollback, Batfish verification of every change, segmentation for payment terminals, central device authentication, streaming telemetry, a read-only AI operations assistant, and live BGP monitoring of real prefixes with RPKI validation. It reuses your course projects directly: the edge and failover work of NET301 P3, the identity work of NET302, the pipeline of NET303 P3, the branch and SD-WAN design of NET304, the operations model of NET305, the hybrid links and EVPN scale-up of NET401, the segmentation evidence of NET402, the guarded agent of NET403 and the design documents of NET404. It is the portfolio piece you show in interviews.

## 7. Certifications worth having (optional, never required)

**Honest value note.** Vendor certifications are used as résumé screens in this field more than in most software roles, especially at Indian IT services firms, network vendors' partners and for first jobs. A hands-on lab exam proves more than a multiple-choice one, and none replaces a portfolio: interviewers will hand you a broken network or ask you to design one. Take one at the end of the course that already prepares you, verify the current exam version on the official page before booking, and stop collecting once you have a job offer that values projects more.

| Certification (October 2026 name) | Best timed after | Note |
|---|---|---|
| CompTIA Network+ (N10-009) | CS204 | Vendor-neutral entry screen; launched 20 June 2024, retirement estimated 2027 |
| Cisco CCNA (200-301 v1.1) | NET301 | The most common networking screen; includes an introduction to automation and programmability |
| Cisco CCNP Enterprise | NET301 + NET304 + NET401 | Worth it with real experience; core plus a concentration exam |
| Cisco CCNA Automation / CCNP Automation | NET303 | Cisco's automation track (formerly DevNet); good signal for NetDevOps roles |
| Cisco CCNP Wireless, CCNP Data Center, CCNP Security | NET304 / NET401 / NET402 | Specialist tracks; take only if your target employer runs Cisco |
| Juniper JNCIA-Junos (JN0-106) | NET301 | Juniper is now part of HPE ("HPE Juniper Networking"); useful in service-provider and Juniper shops |
| Microsoft Certified: Windows Server Administrator Associate (AZ-802) | NET302 | Single-exam Windows Server hybrid administrator certification |
| ITIL 4 Foundation or ITIL (Version 5) Foundation | NET305 | ITIL 4 remains valid and available; Version 5 Foundation launched in 2026, with a bridge exam for ITIL 4 holders |
| CWNA (CWNP) | NET304 | Vendor-neutral wireless certification respected by wireless engineers |
| Cloud networking certifications | NET401 + CLD304 | See the [Cloud Engineering major](../cloud_engineering/README.md) for current AWS, Azure and Google Cloud options |

## 8. The interview loop for infrastructure and network roles

A typical loop in 2026 (based on the [NET market page](../../06_career_and_market_readiness/01_market_map/roles/NET_it_infrastructure_networking.md); practise with the [AI-driven interviews section](../../06_career_and_market_readiness/04_ai_driven_interviews/)):

1. **Screen:** recruiter call, often an online test of networking fundamentals (OSI and TCP/IP, subnetting, DNS, DHCP, routing, NAT). Subnetting is usually AI-off and timed. Read the rules on AI use for each assessment.
2. **Fundamentals deep dive:** OSPF adjacency states, BGP best-path and policy, STP, VLANs and trunks, NAT, DNS, AD and Kerberos basics, explained aloud (NET301, NET302).
3. **Troubleshooting scenarios:** "users in one branch cannot reach an application; walk through it". The strongest predictor for network and NOC roles; a structured method and named commands matter more than the answer (NET301 Chapter 12, NET304 Chapter 6).
4. **Practical lab:** fix or configure devices in Packet Tracer, CML or a vendor lab, or write a small automation script, sometimes with AI allowed and judged on review quality (NET301 gate, NET303 gate).
5. **Process questions:** change management, incident handling, documentation, on-call (NET305).
6. **Design round (mid and senior):** a campus, branch WAN, data-centre fabric, segmentation or migration design with numbers, failure modes and cost (NET304, NET401, NET402, NET404; practise in CAR401).
7. **Behavioural:** an outage you handled, a change that went wrong, a migration you planned, with evidence.

Automation roles add a coding exercise (Python with Netmiko, Nornir or APIs) and a pipeline design question; architect roles add a business case and a stakeholder role-play; AIOps roles add an evaluation question ("how would you prove this AI helps?").

## 9. Fast track for working professionals

Budget about 15 hours a week. Take the gate tests of CS204 and CS203 first; if you pass, start directly. The common ladder is **service desk → network or infrastructure engineer → automation or cloud**, and each row below moves you one or two rungs up.

| You are now | Path (about 6–9 months) | Proof to build |
|---|---|---|
| Service desk / IT support (L1–L2) | CS204 gate → NET301 → NET302 → NET305 | NET301 P2, NET302 P1, and a CCNA or Network+ |
| NOC engineer | NET301 → NET303 → NET305 Chapters 8–9 → NET403 | NET305 P2 and NET303 P2 |
| Windows or Linux systems administrator | NET302 (gate test, then Chapters 7–12) → NET303 → NET401 Chapters 7–11 | NET302 P3 and NET401 P3 |
| Network engineer (CCNA level) moving to automation | NET303 → NET401 → NET403 | NET303 P3 and NET403 P2 |
| Network engineer moving to cloud | NET303 → [CLD304](../cloud_engineering/year_3/CLD304_cloud_networking_vpcs_dns_load_balancing/README.md) → NET401 Chapter 10 → NET404 | NET401 P3 and CLD304 P3 |
| Telecom field or transmission engineer | NET301 → NET303 → NET501 Chapters 2–5 | NET303 P2 and a 5G core lab write-up |
| Senior engineer aiming at architecture | NET402 → NET404 → NET403 Chapters 6–8 | NET404 P3 |

Finish with the flagship project and [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) for interview preparation.

## Sources

All checked October 2026.
- BLS Occupational Outlook Handbook (2025–35 projections; May 2025 pay): [computer network architects](https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm), [network and computer systems administrators](https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm), [computer support specialists](https://www.bls.gov/ooh/computer-and-information-technology/computer-support-specialists.htm).
- [Indeed Hiring Lab job postings tracker](https://github.com/hiring-lab/job_postings_tracker) (to 2 Oct 2026); [WEF Future of Jobs Report 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf); [ISC2 2025 Cybersecurity Workforce Study](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study) — as summarised in the [market map](../../06_career_and_market_readiness/01_market_map/README.md).
- [NASSCOM Strategic Review 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026); [Payscale India, Network Engineer](https://www.payscale.com/research/IN/Job=Network_Engineer/Salary) (self-reported, Jul 2026).
- [HPE closes Juniper acquisition](https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html) (2 Jul 2025); [Cisco AgenticOps announcement](https://newsroom.cisco.com/content/r/newsroom/en/us/a/y2026/m02/cisco-expands-agenticops-innovations-across-portfolio.html) (10 Feb 2026).
- [CNBC on Salesforce support headcount](https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html) (2 Sep 2025); [PeopleCert ITIL (Version 5) Foundation guide](https://www.itil.com/Itil-News-and-Announcements/itil-version-5-foundation-whats-new-guide) and [ITIL Version 5 explained](https://www.peoplecert.org/news-and-announcements/itil-version-5-explained).
- [Mondal et al., arXiv 2307.04945](https://arxiv.org/abs/2307.04945) (Jul 2023); [NetConfEval](https://github.com/NetConfEval/NetConfEval) (CoNEXT 2024).
- [AWS DynamoDB us-east-1 summary](https://aws.amazon.com/message/101925/) (Oct 2025); [Cloudflare 18 November 2025 outage](https://blog.cloudflare.com/18-november-2025-outage/); [Rogers outage review summary](https://mobilesyrup.com/2024/07/05/july-2022-rogers-outage-report-crtc/) (5 Jul 2024).
- India infrastructure: [Savills H1 2026 data-centre figures](https://indianinfrastructure.com/2026/07/22/indias-data-centre-capacity-additions-grow-59-per-cent-in-h1-2026-says-industry-report/) (22 Jul 2026); [5G base stations](https://indianinfrastructure.com/2026/07/27/india-crosses-0-56-million-5g-base-stations-136-telecom-rd-projects-approved-says-minister-of-state-for-communications/) (27 Jul 2026); [6 GHz delicensing](https://indianinfrastructure.com/?p=265331) (22 Jan 2026); [CERT-In Directions](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) (28 Apr 2022).
- Certifications: [Cisco certifications](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html) and [CCNA](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/enterprise/ccna/index.html); [JNCIA-Junos](https://learningportal.juniper.net/juniper/user_activity_info.aspx?id=14354); [CompTIA Network+](https://www.comptia.org/en-us/certifications/network/); [Microsoft Windows Server Administrator Associate](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-hybrid-administrator/); [PeopleCert ITIL certifications](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1); CWNA at [CWNP](https://www.cwnp.com/) (current exam version not checked).

_Last reviewed: 2026-10_
