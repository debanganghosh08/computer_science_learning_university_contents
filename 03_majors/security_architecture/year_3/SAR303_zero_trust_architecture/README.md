# SAR303 · Zero Trust Architecture

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L4 | [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [SAR403](../../year_4/SAR403_security_architecture_for_ai_systems_and_agents/README.md), [SAR401](../../year_4/SAR401_cloud_security_architecture/README.md), [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md) |

Part of the [Security Architecture major](../../README.md). Taken alongside [SAR301](../SAR301_security_architecture_principles_and_frameworks/README.md) and [SAR302](../SAR302_threat_modeling/README.md). CS213 Lesson 10.2 asked you to rewrite one VPN design as zero trust. This course teaches you to design, sequence and measure a zero trust programme for a whole organisation, and to explain it to the people who pay for it. Identity operations (lifecycle, PAM, Conditional Access tuning) belong to [SEC303](../../../cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md); detection belongs to [SEC302](../../../cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md).

## Why this course matters now

"Zero trust" means no request is trusted because of where it comes from; every access is authenticated, authorised and evaluated against current context. The old model failed in public: in January 2024 CISA ordered US federal agencies to mitigate actively exploited flaws in Ivanti Connect Secure VPN appliances (Emergency Directive 24-01), a reminder that the device guarding the perimeter is itself a target. Guidance has matured. NIST SP 1800-35 (final, June 2025) documents 19 example zero trust implementations built with 24 collaborators ([NIST](https://csrc.nist.gov/pubs/sp/1800/35/final)), CISA's Zero Trust Maturity Model 2.0 (April 2023) gives stages per pillar, and in January 2026 the NSA began publishing Zero Trust Implementation Guidelines that organise the US defence department's 152 zero trust activities into phases ([NSA primer](https://media.defense.gov/2026/Jan/08/2003852320/-1/-1/0/CTR_ZERO_TRUST_IMPLEMENTATION_GUIDELINE_PRIMER.PDF)). Demand follows: zero trust was named as a skills gap by 27% of respondents in ISC2's 2024 study ([ISC2](https://www.isc2.org/Insights/2024/09/Employers-Must-Act-Cybersecurity-Workforce-Growth-Stalls-as-Skills-Gaps-Widen)). AI adds a new kind of subject, the agent, that needs per-request authorization, and AI assistants now draft access policies. A person still has to choose the sequence, decide what fails open or closed, and prove the policies do what the design says.

## Learning outcomes

By the end you can:

1. **Explain** the NIST SP 800-207 tenets and logical architecture (policy engine, policy administrator, policy enforcement points) and **map** a real product set onto it.
2. **Design** identity-centric access with phishing-resistant authentication, continuous evaluation (OpenID CAEP and Shared Signals) and short-lived, bound sessions.
3. **Design** device trust from device identity, attestation and posture, and **handle** unmanaged devices and contractors.
4. **Build** an identity-aware proxy deployment for web, SSH and database access, and **replace** a VPN for a defined user group.
5. **Implement** microsegmentation with identity-based policies (Kubernetes NetworkPolicy, Cilium, service-mesh authorization) and **roll it out** default-deny without an outage.
6. **Write** and **test** access policies as code, and **choose** fail-open or fail-closed behaviour for each enforcement point.
7. **Assess** an organisation against CISA ZTMM 2.0 and **produce** a sequenced, costed migration roadmap.
8. **Extend** zero trust to workloads, partners, OT and AI agents, and **audit** AI-drafted policies for over-broad grants.

## Chapters and lessons

### Chapter 1 · Why the perimeter failed (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Castle and moat | Implicit trust inside the network; lateral movement; flat networks; VPNs that grant network-level access | Trace how one phished laptop reaches a database in a flat network diagram |
| 1.2 Perimeter devices as targets | Edge appliances (VPN, firewall, file transfer) in CISA emergency directives; why internet-facing management planes are dangerous | Summarise ED 24-01 and list the architectural lessons, not the exploit |
| 1.3 BeyondCorp | Google's move to device- and user-based access without a privileged network (Ward and Beyer, 2014, and later papers) | Extract BeyondCorp's components and map them to today's product categories |
| 1.4 The tenets | NIST SP 800-207's seven tenets: all resources, all communication secured, per-session access, dynamic policy, asset integrity, dynamic authentication, collect and improve | Score a provided architecture against each tenet |

**Check your understanding:** (1) Why does a VPN that grants network access violate "per-session access"? (2) What did BeyondCorp have to build before it could remove the privileged network? (3) Which tenet is hardest to meet for legacy systems, and why?

### Chapter 2 · The SP 800-207 logical architecture (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 PE, PA and PEP | Decision vs administration vs enforcement; control plane vs data plane | Label the PE, PA and PEPs in three vendor architectures |
| 2.2 Deployment models | Device agent and gateway, enclave gateway, resource portal, application sandboxing | Pick a model for four applications and justify each |
| 2.3 The trust algorithm | Criteria-based vs score-based, singular vs contextual; inputs (identity, device, behaviour, threat intelligence) | Design a trust algorithm for a brokerage back office |
| 2.4 Threats to zero trust itself | Subversion of the decision process, denial of service on the PDP, stolen credentials, insider threats, reliance on proprietary data formats (SP 800-207 Section 5) | Threat-model your own trust algorithm with STRIDE |

**Check your understanding:** (1) Why is the policy engine a crown jewel? (2) When is a score-based algorithm risky? (3) What happens to access if the PDP is unreachable, and who decides?

### Chapter 3 · Identity as the control plane (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Strong authentication | Phishing-resistant MFA (FIDO2, PIV) as the baseline; OMB M-22-09 (January 2022) set it for US agencies | Plan phishing-resistant MFA for 2,000 users including a call centre |
| 3.2 Continuous evaluation | OpenID Shared Signals Framework, CAEP and RISC (final 2025); revoking sessions when risk changes | Wire a session-revocation signal from a test IdP to a demo app |
| 3.3 Sessions and tokens | Short lifetimes, refresh rotation, sender-constrained tokens (DPoP, RFC 9449, or mTLS-bound) | Shorten session lifetimes for one app and measure user friction |
| 3.4 Cloud-native and workload identity | SP 800-207A (2023): identity-based segmentation for multi-cloud microservices; SPIFFE IDs | Map SP 800-207A's policy tiers onto a Kubernetes deployment |

**Check your understanding:** (1) Why is phishing resistance the property that matters, not the number of factors? (2) What does continuous evaluation add that short sessions do not? (3) Why must workloads be first-class identities in zero trust?

### Chapter 4 · Device trust (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Device identity | Device certificates, TPM-backed keys, enrolment; why a device ID must be hard to copy | Issue device certificates from a lab CA to two VMs |
| 4.2 Posture | Patch level, disk encryption, EDR health, OS integrity; MDM/UEM (Microsoft Intune, Jamf), osquery and Fleet | Write five osquery checks and feed them to a policy decision |
| 4.3 Unmanaged devices | Contractors, BYOD, partner staff; browser-only access, isolation, reduced data access | Design three access tiers by device trust level |
| 4.4 Privacy and fairness | What posture data reveals about employees; minimum collection; DPDP considerations | Write the posture-data notice for staff |

**Check your understanding:** (1) Why is a self-reported posture signal weak? (2) What should an unmanaged device never reach? (3) Which posture checks give the most risk reduction per unit of friction?

### Chapter 5 · Identity-aware proxies and access brokers (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 How an identity-aware proxy works | Authenticate at the proxy, authorise per request, pass verified identity downstream; signed headers and their pitfalls | Deploy Pomerium (open source) in front of a lab web app |
| 5.2 Infrastructure access | SSH, RDP, Kubernetes and databases through brokers (Teleport, OpenZiti); short-lived certificates instead of keys | Replace static SSH keys with short-lived certificates in the lab |
| 5.3 Managed services | Google Cloud IAP, Cloudflare Access, Microsoft Entra Private Access, Zscaler-style security service edge; evaluating vendors on architecture, not features | Write a vendor-neutral evaluation rubric with 12 criteria |
| 5.4 Retiring the VPN | User segmentation, app-by-app migration, legacy protocols, rollback | Plan VPN retirement for one department |

**Check your understanding:** (1) Why must the application verify that a request came through the proxy? (2) What does a short-lived SSH certificate remove? (3) Which application types resist proxy-based access?

### Chapter 6 · Microsegmentation (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 From IP rules to identity rules | Why IP-based rules break in dynamic environments; labels, service accounts and SPIFFE IDs as policy subjects | Rewrite ten IP rules as identity-based rules |
| 6.2 Kubernetes and eBPF | NetworkPolicy, Cilium identity-aware and L7 policies, default deny per namespace | Enforce default deny in a lab cluster and open only required flows |
| 6.3 Service-mesh authorization | mTLS everywhere, Istio authorization policies, ambient vs sidecar models | Allow only the checkout service to call payments, and prove it |
| 6.4 Rollout without outages | Flow discovery, observe-only mode, staged enforcement, rollback | Write a rollout plan with success metrics for 40 services |

**Check your understanding:** (1) Why do segmentation projects stall, and how does observe-only mode help? (2) What does mTLS prove and what does it not? (3) Where should east-west authorization decisions be made?

### Chapter 7 · Data-centric zero trust (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Classification and labels | Labels that travel with data; automatic classification and its error rates | Design a four-level scheme for a hospital and its label rules |
| 7.2 Access to data, not networks | Attribute-based access, row- and column-level security, query-time policies | Enforce column masking for PAN numbers in a lab database |
| 7.3 Encryption with policy | Key access tied to identity and context; customer-managed keys; envelope encryption (preview of SAR304) | Design key access policies for two data classes |
| 7.4 SaaS data | Sharing links, OAuth integrations, data loss prevention in SaaS | Audit sharing settings in a test SaaS tenant |

**Check your understanding:** (1) Why is the data pillar usually the least mature? (2) What does key access policy add to storage access policy? (3) How do OAuth integrations bypass network controls?

### Chapter 8 · Policy design and enforcement behaviour (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Policy as code | Open Policy Agent (Rego), Cedar; unit tests for policies; review in Git | Write and test 15 access policies for an internal admin portal |
| 8.2 Context and risk | Time, location, device tier, behaviour signals; avoiding rules nobody can explain | Add two contextual conditions and show their effect in tests |
| 8.3 Fail-open vs fail-closed | Per enforcement point, with availability and safety costs; caching decisions vs complete mediation | Decide behaviour for six PEPs and simulate a PDP outage |
| 8.4 Break-glass | Emergency access outside the normal path, with alerts and review | Build a break-glass path and its alert |

**Check your understanding:** (1) When is caching an authorization decision acceptable? (2) Why must break-glass be tested regularly? (3) What makes a policy explainable to an auditor?

### Chapter 9 · Visibility, analytics and automation (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Decision logs | Logging every allow and deny with the inputs used; privacy limits; retention (CERT-In's 180 days in India) | Ship decision logs from your proxy and PDP to a log store |
| 9.2 Signals into decisions | Detection outputs as policy inputs; risk scores; feedback loops | Make a high-risk sign-in signal revoke an active session |
| 9.3 Automation | Automatic session revocation, device quarantine, access reviews driven by usage | Automate removal of access unused for 60 days in the lab |
| 9.4 Measuring zero trust | Coverage (apps behind PEPs), phishing-resistant MFA rate, standing privilege, east-west default-deny share | Define eight metrics with formulas and data sources |

**Check your understanding:** (1) Why are deny logs as valuable as allow logs? (2) What can go wrong when detections drive access automatically? (3) Which metric best shows progress to a board?

### Chapter 10 · Maturity models and migration roadmaps (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 CISA ZTMM 2.0 | Pillars (identity, devices, networks, applications and workloads, data), cross-cutting capabilities, stages (traditional, initial, advanced, optimal) | Assess an illustrative mid-size bank against the model |
| 10.2 Phased guidance | NSA Zero Trust Implementation Guidelines (primer and discovery phase, January 2026); the defence department's target-level activities | Build a discovery-phase checklist for your assessment |
| 10.3 Example builds | NIST SP 1800-35's 19 example implementations and lessons learned | Pick the build closest to your case and list what you would reuse |
| 10.4 Sequencing | Inventory, identity, devices, applications, networks, data; quick wins vs foundations; dependencies; regulatory drivers (RBI's 2026 directions require MFA for privileged users) | Draw a three-year roadmap with dependencies |
| 10.5 Cost and the business case | Licences, staff, retired VPN and MPLS costs, risk reduction; what to promise and what not to | Write a two-page business case |

**Check your understanding:** (1) Why do roadmaps that start with network segmentation often stall? (2) What makes a maturity score honest? (3) What would you cut first if the budget halves?

### Chapter 11 · Workloads, partners and operational technology (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Workload-to-workload | Workload identity federation, no long-lived keys, CI/CD as a subject | Remove a long-lived cloud key from a pipeline with OIDC federation |
| 11.2 Partners and suppliers | Federated access, scoped partner portals, time-boxed access, supplier offboarding | Design access for an outsourced call centre |
| 11.3 OT and legacy | IEC 62443 zones and conduits; when you cannot install agents; enclave gateways | Draw zones and conduits for a small factory (illustrative) |
| 11.4 Managed service providers | Outsourced IT and MSP access as a supply-chain path; scoped, time-boxed, recorded administrative access; separate administration tenants | Design MSP access for a bank's outsourced desktop support |

**Check your understanding:** (1) Why is a CI pipeline one of the most privileged identities? (2) What changes about zero trust where availability is a safety property? (3) How do you time-box partner access in practice?

### Chapter 12 · Zero trust for AI agents, and AI for zero trust (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Agents as subjects | Agent identity separate from user identity; delegation (acting for a user) vs autonomy; per-tool, per-call authorization | Design the identity and policy model for an expense-approval agent |
| 12.2 Approval as policy | Human approval steps encoded in the PDP, not in prompts; the Five Eyes guidance on limiting agent privileges | Make one high-risk tool require approval at the PEP |
| 12.3 AI-assisted policy work | Drafting Rego or Cedar, summarising decision logs, proposing least-privilege changes from usage | Have an assistant draft 10 policies and test them against your suite |
| 12.4 Failure modes | Wildcard grants, missing deny cases, policies that pass tests but break intent, invented attribute names | Log every defect you find in the AI drafts |

**Check your understanding:** (1) Why can't a system prompt enforce an agent's permissions? (2) What should an agent's token look like compared with its user's? (3) Which AI policy errors do unit tests miss?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Flat-network trace and tenet scoring | Scored architecture |
| 2 | 2 | Lab 2 · Trust algorithm and its threat model | Design and threat list |
| 3 | 3 | Lab 3 · Session revocation signal | Working demo; **P1 due** |
| 4 | 4 | Lab 4 · Device certificates and osquery posture | Posture-driven decision |
| 5 | 5 | Lab 5 · Identity-aware proxy and SSH certificates | Proxy deployment |
| 6 | 6 | Lab 6 · Default deny in Kubernetes (no AI) | Policy set and tests |
| 7 | 7 | Lab 7 · Data masking | Masked queries; mid-term (AI off) |
| 8 | 8 | Lab 8 · Policies as code and PDP outage | Tested policies |
| 9 | 9 | Lab 9 · Decision logs and automation | Revocation automation |
| 10 | 10 | ZTMM assessment | Assessment; **P2 due** |
| 11 | 10 | Roadmap and business case | Roadmap draft |
| 12 | 11 | Lab 10 · Pipeline without long-lived keys | Federated workflow |
| 13 | 12 | Agent policy design | Policy model |
| 14 | 12 | AI policy audit | **P3 due** |
| 15 | Review | Design exam and oral | Final exam |

## Working with AI in this course

- **Use AI for:** summarising vendor documentation into a neutral comparison; drafting Rego or Cedar policies and their tests; generating osquery checks; summarising decision logs; producing first-draft roadmap narratives.
- **Do without AI (drills):** the tenet scoring in Lab 1; the Kubernetes default-deny policy set (Lab 6); fail-open/fail-closed decisions; the mid-term; the final design exam.
- **Verify AI output by:** running every policy against a test suite that includes deny cases you wrote first; checking attribute names against your identity provider's real claims; diffing effective permissions before and after; checking claims about product capabilities against vendor documentation dated this year.
- **Where AI still fails here (show it):** ask an assistant for a "least-privilege" Kubernetes NetworkPolicy and check whether it forgets DNS egress or allows all egress; ask for a Cedar or Rego policy for "managers can approve their team's expenses" and test whether a manager can approve their own; record wildcard grants and invented attributes.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off) | 10% |
| Final: design exam on an unseen organisation plus oral defence of P3 | 20% |

**Mastery gate.** You pass when you can, without AI and in three hours: (a) assess an unseen organisation's description against CISA ZTMM 2.0 with evidence for each stage you assign; (b) design the target architecture on the SP 800-207 model with named PEPs, PDP inputs and fail behaviour for each; and (c) write a first-year roadmap whose dependencies an assessor cannot break (no step requires something scheduled later).

## Industry reality

- Google's BeyondCorp papers describe how it moved employees off a privileged network; NIST SP 1800-35 shows 19 multi-vendor builds of the same idea.
- US federal agencies were directed to phishing-resistant MFA and zero trust goals by OMB M-22-09, and the defence department's strategy sets target-level zero trust activities that NSA's 2026 guidelines now break into phases.
- In India, RBI's 2026 cybersecurity directions for commercial banks require MFA for privileged users (see [SEC305](../../../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md)), and CERT-In requires log retention that zero trust decision logs must meet.
- Architect interviews often include "replace our VPN" or "design access for contractors" exercises.

**Interview questions from this course**

1. *"We have a VPN for 3,000 staff. Design our move to zero trust."* Strong answer: inventory apps and users; phishing-resistant MFA first; device trust tiers; identity-aware proxy app by app; legacy exceptions; decision logging; metrics; rollback; the order and why.
2. *"Explain PE, PA and PEP with a real product example."* Strong answer: correct roles, control vs data plane, what happens when the PDP fails, how a proxy and an IdP fill the roles.
3. *"How would you implement microsegmentation in Kubernetes without breaking production?"* Strong answer: flow discovery, observe mode, namespace default deny, identity-based policies, mesh authorization for L7, staged enforcement and rollback, metrics.
4. *"How does zero trust apply to an AI agent that can call internal APIs?"* Strong answer: the agent has its own identity, delegated tokens scoped per tool, PEP-enforced approval for high-risk actions, no trust in prompt instructions, logging of every call.
5. *"Our board asks whether we are 'zero trust'. What do you report?"* Strong answer: it is a direction, not a state; ZTMM stages per pillar with evidence; a few metrics with trend; the next decisions and their cost.

## Resources (free first)

- **Standards and guidance:** [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final); [SP 800-207A](https://csrc.nist.gov/pubs/sp/800/207/a/final); [SP 1800-35](https://csrc.nist.gov/pubs/sp/1800/35/final); [CISA Zero Trust Maturity Model](https://www.cisa.gov/zero-trust-maturity-model); [NSA ZIG primer](https://media.defense.gov/2026/Jan/08/2003852320/-1/-1/0/CTR_ZERO_TRUST_IMPLEMENTATION_GUIDELINE_PRIMER.PDF) and [discovery phase](https://media.defense.gov/2026/Jan/08/2003852321/-1/-1/0/CTR_ZIG_DISCOVERY_PHASE.PDF); [OMB M-22-09](https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf); [NCSC zero trust architecture design principles](https://www.ncsc.gov.uk/collection/zero-trust-architecture); [OpenID CAEP](https://openid.net/specs/openid-caep-1_0-final.html).
- **Papers:** Ward and Beyer, [BeyondCorp: A New Approach to Enterprise Security](https://research.google/pubs/beyondcorp-a-new-approach-to-enterprise-security/) (2014) and the follow-up papers linked from it.
- **Open-source tools for labs:** [Pomerium](https://www.pomerium.com/docs), [OpenZiti](https://openziti.io/docs/), [Teleport Community Edition](https://goteleport.com/docs/), [Keycloak](https://www.keycloak.org/documentation), [SPIRE](https://spiffe.io/docs/latest/spire-about/), [Cilium](https://docs.cilium.io/), [Istio](https://istio.io/latest/docs/), [osquery](https://osquery.readthedocs.io/), [Open Policy Agent](https://www.openpolicyagent.org/docs), [Cedar](https://www.cedarpolicy.com/).
- **Managed services (free tiers vary; check current limits):** [Google Cloud IAP](https://cloud.google.com/iap/docs), [Cloudflare Zero Trust](https://developers.cloudflare.com/cloudflare-one/).
- **Paid, optional:** Razi Rais, Christina Morillo, Evan Gilman and Doug Barth, *Zero Trust Networks*, 2nd edition (O'Reilly, 2024). The NIST and CISA documents cover the architecture for free.

## Sources

All checked 12 Oct 2026.

- NIST SP 1800-35, *Implementing a Zero Trust Architecture* (final, June 2025): 19 example implementations, 24 collaborators — https://csrc.nist.gov/pubs/sp/1800/35/final
- NSA, Zero Trust Implementation Guideline primer and discovery phase (January 2026); later phases as reported by Help Net Security (15 Jan 2026) — https://media.defense.gov/2026/Jan/08/2003852320/-1/-1/0/CTR_ZERO_TRUST_IMPLEMENTATION_GUIDELINE_PRIMER.PDF ; https://www.helpnetsecurity.com/2026/01/15/nsa-zero-trust-implementation-guidelines/
- CISA, Zero Trust Maturity Model 2.0 (April 2023) — https://www.cisa.gov/zero-trust-maturity-model
- CISA, Emergency Directive 24-01 on Ivanti Connect Secure and Policy Secure (January 2024) — https://www.cisa.gov/news-events/directives/ed-24-01-mitigate-ivanti-connect-secure-and-ivanti-policy-secure-vulnerabilities
- ISC2, 2024 Cybersecurity Workforce Study (11 Sep 2024) — https://www.isc2.org/Insights/2024/09/Employers-Must-Act-Cybersecurity-Workforce-Growth-Stalls-as-Skills-Gaps-Widen
- OpenID Foundation, Shared Signals Framework, CAEP and RISC final specifications (2025) — https://openid.net/three-shared-signals-final-specifications-approved/
- CISA and partners, *Careful adoption of agentic AI services* (1 May 2026) — https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai
- RBI 2026 directions as summarised by DSCI (31 Jul 2026) — https://www.dsci.in/files/content/knowledge-centre/2026/dsci-brief-on-rbi-cybersecurity-commercial-banks-directions-2026.pdf

_Last reviewed: 2026-10_
