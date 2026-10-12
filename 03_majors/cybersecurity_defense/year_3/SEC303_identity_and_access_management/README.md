# SEC303 · Identity and Access Management

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) | [SEC403](../../year_4/SEC403_malware_analysis_for_defenders/README.md), [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md), [SAR402 Identity Architecture at Scale](../../../security_architecture/year_4/SAR402_identity_architecture_at_scale/README.md) (for architects) |

Part of the [Cybersecurity Defense major](../../README.md). This course teaches identity **defense and operations**. Attack techniques against identity systems are named so you can detect and prevent them; they are never taught step by step. Assessment tools are run only against your own lab directory.

## Why this course matters now

Most serious intrusions now involve a stolen or abused identity rather than a broken firewall. In 2024, attackers used credentials stolen by infostealer malware to log in to about 165 organisations' Snowflake accounts that had no multi-factor authentication (MFA). Change Healthcare's February 2024 ransomware attack began with stolen credentials on a remote-access portal without MFA, according to UnitedHealth's CEO's testimony to the US Congress. Russia's Midnight Blizzard got into Microsoft in late 2023 through a password spray on a legacy test account without MFA, then abused an old OAuth application with high privileges. In August 2025 attackers stole OAuth tokens from the Salesloft Drift chat integration and exported data from hundreds of Salesforce instances without touching a password. Mandiant's M-Trends 2026 found voice phishing, often against help desks, rose to 11% of intrusions, and warned that interactive social engineering "frequently bypasses traditional MFA". AI tools now write access reviews, flag risky sign-ins (Microsoft Entra ID Protection, Okta ThreatInsight) and draft Conditional Access policies, and AI agents are getting their own identities (Microsoft Entra Agent ID entered preview in May 2025). Someone still has to design the controls, decide who gets privilege, and investigate when a token is used from the wrong place.

## Learning outcomes

By the end you can:

1. **Run** the identity lifecycle (joiner, mover, leaver) with an authoritative source and automated provisioning (SCIM), and **measure** time to deprovision.
2. **Choose** authenticators by NIST SP 800-63B-4 assurance level, and **roll out** phishing-resistant MFA (FIDO2 security keys, passkeys, smart cards) with safe account recovery.
3. **Explain and debug** SAML 2.0, OAuth 2.0 and OpenID Connect flows, and **find** risky token lifetimes, scopes and consents.
4. **Design** least-privilege access with RBAC/ABAC, access reviews and separation of duties, and **report** standing privilege.
5. **Implement** privileged access controls: tiering, privileged access workstations, just-in-time elevation, Windows LAPS, break-glass accounts.
6. **Assess** an Active Directory and Microsoft Entra ID tenant in your lab with defensive tools (PingCastle, BloodHound Community Edition, Microsoft Secure Score) and **fix** the top findings.
7. **Govern** non-human identities: service accounts, API keys, workload identity federation and AI agent identities.
8. **Detect and respond** to identity attacks (password spray, MFA fatigue, token theft, malicious OAuth consent, Kerberos abuse, DCSync) from identity-provider and domain controller logs.

## Chapters and lessons

### Chapter 1 · Identity as the new perimeter (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Why identity | Case studies: Snowflake customers (2024), Change Healthcare (2024), Midnight Blizzard (2024), Salesloft Drift (2025), Scattered Spider help-desk social engineering (CISA advisory AA23-320A, updated July 2025) | For each case, name the control that would have broken the chain |
| 1.2 Vocabulary | Identity, account, credential, authenticator, session, token, entitlement, principal; human vs non-human identities | Draw the identity map of a college ERP system (illustrative) |
| 1.3 Identity providers | Active Directory, Microsoft Entra ID, Okta, Google Workspace, Keycloak (open source); how they federate | Install Keycloak in the lab and federate one test app |
| 1.4 The lab | A Windows Server domain controller, two domain-joined clients, an Entra ID free/developer tenant, Keycloak | Build and document the lab |

**Check your understanding:** Why do stolen session tokens bypass MFA? Which of the five cases needed no password at all? Why are non-human identities often the largest population in a tenant?

### Chapter 2 · Identity lifecycle and governance (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Joiner, mover, leaver | HR system as source of truth, birthright access, role changes, termination; orphan and dormant accounts (RBI's 2026 directions for banks require removing dormant accounts) | Script a report of accounts with no sign-in for 90 days |
| 2.2 Provisioning | SCIM 2.0 (RFC 7643/7644), just-in-time provisioning, deprovisioning gaps in SaaS | Provision and deprovision a test user to two apps via SCIM |
| 2.3 Access reviews | Certification campaigns, reviewer fatigue, risk-based reviews; identity governance tools (Microsoft Entra ID Governance, SailPoint, Saviynt, open-source midPoint) | Run a review of 50 entitlements and record decisions |
| 2.4 Separation of duties | Toxic combinations (create vendor + approve payment), detective vs preventive SoD | Write five SoD rules for a payments team |

**Check your understanding:** Why are movers riskier than joiners? What makes a reviewer approve everything, and how do you fix it? Why is deprovisioning in SaaS harder than disabling an AD account?

### Chapter 3 · Authentication and phishing-resistant MFA (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Assurance levels | NIST SP 800-63B-4 (2025): AAL1–3, syncable passkeys, phishing resistance as a requirement at AAL3 | Classify 10 authenticators by AAL and phishing resistance |
| 3.2 MFA weaknesses | SMS and voice OTP, push fatigue (push bombing), adversary-in-the-middle phishing, SIM swap (named, not taught); number matching | Map each weakness to the authenticator it defeats |
| 3.3 Phishing-resistant MFA | FIDO2/WebAuthn origin binding, passkeys, PIV smart cards; CISA's phishing-resistant MFA guidance | Enrol a security key or passkey in Entra ID and Keycloak; test a look-alike domain |
| 3.4 Recovery and the help desk | Recovery as an authentication path; caller verification; temporary access passes | Write a help-desk identity verification procedure that resists voice phishing |
| 3.5 Rollout | Pilot groups, exceptions with expiry, legacy protocol blocking, measuring coverage | Plan an MFA rollout for 3,000 users with metrics |

**Check your understanding:** Why does a passkey refuse to sign in on a look-alike domain when a TOTP code does not? Why is account recovery often the weakest link? What is the risk of an "MFA exception" with no expiry?

### Chapter 4 · Federation, SSO and tokens (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 SAML 2.0 | Assertions, signatures, audience and recipient checks, clock skew | Decode a SAML response in the lab and verify each security check |
| 4.2 OAuth 2.0 and OIDC | Authorization code with PKCE, ID vs access vs refresh tokens, scopes, consent; OAuth 2.0 Security Best Current Practice (RFC 9700, 2025) | Trace an OIDC login with browser developer tools |
| 4.3 Token risk | Token lifetimes, refresh token theft, sender-constrained tokens (DPoP, RFC 9449), continuous access evaluation | Shorten lifetimes for a high-risk app and test the user impact |
| 4.4 App and integration governance | Third-party OAuth apps, admin consent workflows, unused high-privilege apps (Midnight Blizzard), integration tokens (Salesloft Drift) | Inventory all apps and grants in your test tenant and remove risky ones |

**Check your understanding:** Why is PKCE needed even for confidential clients today? What should happen to an integration's tokens when the vendor reports a breach? Why can an old test app be more dangerous than an active one?

### Chapter 5 · Authorization and least privilege (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Models in practice | RBAC role explosion, ABAC attributes, relationship-based access; cloud IAM policies (AWS IAM, Azure RBAC) | Refactor 40 overlapping roles into a smaller set |
| 5.2 Measuring privilege | Standing vs eligible privilege, effective permissions, unused permissions (AWS IAM Access Analyzer, Entra role reports) | Report unused permissions for three lab roles |
| 5.3 Conditional access | Device, location, risk and app conditions; report-only mode; avoiding lock-outs | Build five Conditional Access policies in report-only mode and read the impact |
| 5.4 Policy as code for access | Open Policy Agent or Cedar for application access (recap from CS213) and reviews in Git | Put one access policy under code review with tests |

**Check your understanding:** Why does RBAC tend to drift towards over-privilege? Why test Conditional Access in report-only mode first? What is the difference between "can" and "did" in permission analysis?

### Chapter 6 · Privileged access management (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Tiering and the enterprise access model | Separating control-plane, management-plane and user access; privileged access workstations | Redesign a lab where domain admins browse the web from their laptops |
| 6.2 Just-in-time and just-enough | Microsoft Entra Privileged Identity Management, approval and time limits, Just Enough Administration | Make all lab admin roles eligible, not active |
| 6.3 Vaulting and sessions | PAM vaults, credential rotation, session recording (CyberArk, Delinea, open-source Teleport) | Rotate a service credential automatically and prove nothing broke |
| 6.4 Local admin and break-glass | Windows LAPS, removing local admin, break-glass accounts with monitoring and phishing-resistant MFA | Deploy Windows LAPS; build an alert on any break-glass sign-in |

**Check your understanding:** Why is a privileged account used for email a tier violation? What should alert when a break-glass account is used? Why does LAPS stop one class of lateral movement?

### Chapter 7 · Active Directory security for defenders (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 How AD authenticates | Kerberos (AS, TGS, service tickets), NTLM, LDAP; why NTLM and RC4 are legacy risks | Capture a Kerberos logon in the lab and label each message |
| 7.2 Attack classes (names and defenses only) | Password spraying, Kerberoasting, AS-REP roasting, DCSync, Golden and Silver Tickets, delegation abuse, AD Certificate Services misconfigurations (the "ESC" classes from SpecterOps' 2021 *Certified Pre-Owned*) | For each class: precondition, defense, and the log evidence it leaves |
| 7.3 Hardening | Group Managed Service Accounts, AES-only Kerberos, Protected Users group, removing unconstrained delegation, ADCS template review, tiered admin, krbtgt rotation | Apply eight hardening changes and record the effect |
| 7.4 Assessing your own directory | PingCastle health check, BloodHound Community Edition attack-path graph, Purple Knight; prioritising paths to Tier 0 | Assess the lab domain, then remove the three shortest paths to Domain Admin |

**Check your understanding:** Why do service accounts with weak passwords matter more than user accounts in Kerberos? Why must krbtgt be reset twice after a compromise? Why does an attack-path graph change your priorities more than a list of misconfigurations?

### Chapter 8 · Cloud identity: Entra ID, Okta and workloads (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Entra ID security | Security defaults, Conditional Access, Identity Protection risk, mandatory MFA for Azure administration (portal from 2024–25, Azure Resource Manager write operations from October 2025) | Review your tenant with Microsoft Secure Score and fix five items |
| 8.2 App registrations and service principals | Secrets vs certificates vs managed identities, owner hygiene, credential expiry | Replace a client secret with a managed identity |
| 8.3 Workload identity federation | GitHub Actions to cloud via OIDC with no stored secrets; trust conditions | Configure OIDC from a lab repository to a cloud account |
| 8.4 Hybrid identity | Entra Connect sync, pass-through vs password hash sync vs federation, protecting the sync server as Tier 0 | Draw the hybrid trust chain and mark Tier 0 assets |

**Check your understanding:** Why is the sync server as sensitive as a domain controller? Why are long-lived client secrets risky even when stored in a vault? What trust condition stops any repository from assuming your cloud role?

### Chapter 9 · Non-human identities and AI agents (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Secrets sprawl | API keys, tokens in code and CI logs, secret scanning (GitHub secret scanning, Gitleaks), rotation | Scan a lab repository history and rotate what you find |
| 9.2 Service account governance | Ownership, purpose, expiry, interactive sign-in blocked, monitoring | Build an inventory of non-human identities with owners |
| 9.3 AI agent identities | Agents acting for users vs as themselves, delegated scopes, OWASP Top 10 for Agentic Applications (December 2025), Microsoft Entra Agent ID (preview from May 2025) | Design the identity and permissions for a support agent that can read tickets but not issue refunds |
| 9.4 Secrets management | HashiCorp Vault or OpenBao, dynamic credentials, short TTLs | Issue a 15-minute database credential from a vault |

**Check your understanding:** Who is accountable when an AI agent misuses its permissions? Why is a dynamic credential safer than a rotated static one? Why block interactive sign-in for service accounts?

### Chapter 10 · Identity threat detection and response (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Identity telemetry | Entra sign-in and audit logs, Okta System Log, Windows events 4624/4625/4768/4769/4776, 4662 for directory replication, 4720/4728/4732 for account and group changes | Build a field reference for 15 identity events |
| 10.2 Detections | Password spray (many users, few attempts each), MFA fatigue, impossible travel, new MFA method registration, risky OAuth consent, Kerberos service-ticket requests with RC4, DCSync from a non-DC | Write and test six detections in your SIEM |
| 10.3 ITDR tools | Microsoft Defender for Identity, Entra ID Protection, Okta Identity Threat Protection; what they see that a SIEM may not | Compare one detection's output in a tool vs your SIEM rule |
| 10.4 Response | Revoke sessions and refresh tokens, reset credentials in the right order, remove persistence (new MFA methods, app consents, mail rules), contain a compromised help desk | Run a compromised-admin tabletop and write the eviction order |

**Check your understanding:** Why does a password reset alone not end a session-token compromise? What is the signal that separates a password spray from a forgotten password? Why must new MFA registrations be monitored?

### Chapter 11 · Programme, metrics and AI in IAM (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Metrics | Phishing-resistant MFA coverage, standing privileged accounts, time to deprovision, orphaned accounts, stale apps | Build an identity posture dashboard |
| 11.2 AI in IAM | AI-drafted Conditional Access and access-review recommendations; verification in report-only mode; risks of AI-suggested broad grants | Review three AI-drafted policies and find the flaws |
| 11.3 Regulation | RBI 2026 directions (MFA for privileged users, dormant account removal, centralised identity management), CERT-In, DPDP Act access controls for personal data | Map your lab controls to these requirements |
| 11.4 Recovering identity itself | Break-glass drills, emergency access reviews, backing up identity-provider configuration, tenant and directory recovery plans | Run a break-glass drill in the lab and time it |

**Check your understanding:** Which single metric best predicts identity-led breaches, and why? How would you test an AI-proposed access policy safely? What does "centralised identity management" require in practice?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Identity lab build | Lab documentation |
| 2 | 2 | Lab 2 · Lifecycle and SCIM | Dormant-account report |
| 3 | 3 | Lab 3 · Phishing-resistant MFA | Enrolment and look-alike test |
| 4 | 3 | Lab 3 (cont.) · Help-desk procedure | Rollout plan; **P1 due** |
| 5 | 4 | Lab 4 · Tokens and app consent | App inventory and clean-up |
| 6 | 5 | Lab 5 · Conditional Access (report-only) | Impact report |
| 7 | 6 | Lab 6 · PIM and LAPS | Mid-term (AI off) |
| 8 | 7 | Lab 7 · AD hardening | Hardening record |
| 9 | 7 | Lab 7 (cont.) · Attack-path reduction | Before/after graph; **P2 due** |
| 10 | 8 | Lab 8 · Entra and workload federation | Secure Score fixes |
| 11 | 9 | Lab 9 · Secrets and agents | NHI inventory |
| 12 | 10 | Lab 10 · Identity detections | Six tested detections |
| 13 | 10 | Tabletop | Eviction order |
| 14 | 11 | Posture dashboard | **P3 due** |
| 15 | Review | Practical exam and oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** explaining token contents and protocol traces; drafting Conditional Access policies, SCIM mappings and PowerShell/Microsoft Graph scripts; summarising sign-in logs; first drafts of access-review decisions. Microsoft Security Copilot in Entra, Claude, ChatGPT and Gemini all help; Claude Code or GitHub Copilot can write Graph API scripts.
- **Do without AI (drills):** reading a SAML response and an OIDC token by hand; ranking authenticators; the AD attack-class table (precondition, defense, evidence); eviction ordering in the tabletop; the mid-term and final.
- **Verify AI output by:** deploying every policy in report-only mode first and reading the sign-in impact; checking each Graph or PowerShell call against Microsoft Learn; testing that a "least privilege" role really fails on the actions it should deny; confirming every claimed event ID in Microsoft's documentation.
- **Where AI still fails here (show it, do not assume it):** record cases where an assistant suggests broad roles ("Global Administrator to be safe"), invents Graph endpoints or policy fields, misses that a change locks out break-glass accounts, or describes a deprecated control as current. Identity mistakes can lock out a whole company, so nothing AI-drafted goes live without a tested rollback.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Mid-term (AI off) | 10% |
| Final practical (AI off) + oral defence of P3 | 25% |

**Mastery gate.** You pass when you can, without AI tools: (1) given an unseen lab tenant and domain, find and fix the five highest-risk identity issues in three hours, with before/after evidence; (2) investigate a provided compromised-account log set and produce the timeline, the persistence the attacker added, and the correct eviction order; (3) explain from first principles why a passkey resists phishing and a push notification does not.

## Industry reality

IAM engineers, identity governance analysts and identity-focused detection engineers work in every large organisation, and identity is one of the "growing in value" skills on the [SEC market page](../../../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md). Real anchors: CISA recommends phishing-resistant MFA in its Scattered Spider advisory; Microsoft now enforces MFA for Azure administration; RBI's 2026 directions require MFA for privileged users at commercial banks.

**Interview questions from this course**

1. *Why is SMS OTP not enough, and what would you roll out instead?* Strong answer: phishing and adversary-in-the-middle relay, SIM swap; FIDO2/passkeys with origin binding; plan for recovery, exceptions with expiry, legacy protocol blocking, coverage metrics.
2. *Explain the OIDC authorization code flow with PKCE and where tokens can be stolen.* Strong answer: correct sequence, purpose of PKCE and state/nonce, token types and lifetimes, theft points (browser, logs, integrations), mitigations (short lifetimes, sender-constraining, continuous access evaluation, revocation).
3. *How would you reduce Domain Admin exposure in an AD environment you just inherited?* Strong answer: inventory Tier 0, attack-path analysis (BloodHound CE, PingCastle), remove unnecessary admin memberships and delegation, tiering and PAWs, LAPS, gMSA, ADCS review, monitoring of Tier 0 changes.
4. *A user's account shows a sign-in from another country right after an MFA approval they deny making. What do you do?* Strong answer: treat as likely MFA fatigue or token theft; revoke sessions and refresh tokens, reset credentials, check new MFA methods, mail rules, OAuth consents, data access; contact user out of band; scope other users from the same source.
5. *A SaaS vendor whose integration has broad OAuth access to your CRM reports a breach. What now?* Strong answer: revoke the integration's tokens and grants, review API/audit logs for exports during the window, search exported data for secrets and rotate them, assess notification duties (DPDP Act, contracts), reduce scopes on re-enable.

## Resources (free first)

- **Standards:** [NIST SP 800-63B-4](https://csrc.nist.gov/pubs/sp/800/63/b/4/final) · [RFC 9700, OAuth 2.0 Security BCP](https://www.rfc-editor.org/rfc/rfc9700) · [RFC 7644, SCIM](https://www.rfc-editor.org/rfc/rfc7644) · [RFC 9449, DPoP](https://www.rfc-editor.org/rfc/rfc9449) · [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html) · [W3C WebAuthn Level 3](https://www.w3.org/TR/webauthn-3/)
- **Guidance:** [CISA, Implementing phishing-resistant MFA](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf) · [Microsoft, Securing privileged access](https://learn.microsoft.com/en-us/security/privileged-access-workstations/overview) · [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/) · [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) · [SpecterOps, *Certified Pre-Owned* (ADCS)](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf)
- **Tools (use on your own lab only):** [Keycloak](https://www.keycloak.org/) · [PingCastle](https://www.pingcastle.com/) · [BloodHound Community Edition](https://github.com/SpecterOps/BloodHound) · [Windows LAPS](https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview) · [Gitleaks](https://github.com/gitleaks/gitleaks) · [OpenBao](https://openbao.org/)
- **Practice:** [TryHackMe](https://tryhackme.com/) Active Directory and identity rooms (many subscription-only) · [CyberDefenders](https://cyberdefenders.org/) identity-focused labs · your own Microsoft Entra ID test tenant.

## Sources

All checked 12 Oct 2026.

- Mandiant, UNC5537 and Snowflake customer instances (Jun 2024) — https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion
- TechTarget, "Change Healthcare breached via Citrix portal with no MFA" (Apr–May 2024, on UnitedHealth testimony) — https://www.techtarget.com/cybersecurity/news/366582824/Change-Healthcare-breached-via-Citrix-portal-with-no-MFA
- Microsoft Security blog, "Midnight Blizzard: Guidance for responders on nation-state attack" (25 Jan 2024) — https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/
- Google Threat Intelligence Group, widespread data theft via Salesloft Drift (Aug 2025) — https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift
- CISA, Scattered Spider advisory AA23-320A (Nov 2023, updated Jul 2025) — https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a
- Google Cloud / Mandiant, *M-Trends 2026* — https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026
- Microsoft Learn, mandatory MFA for Azure (phase 1 portal; phase 2 from 1 Oct 2025) — https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication
- Microsoft, Entra Agent ID announcement (Build, May 2025), as reported by Redmond Magazine — https://redmondmag.com/articles/2025/05/19/microsoft-unveils-future-for-ai-agents-at-build-2025.aspx
- DSCI brief on RBI Commercial Banks cybersecurity directions (31 Jul 2026) — https://www.dsci.in/files/content/knowledge-centre/2026/dsci-brief-on-rbi-cybersecurity-commercial-banks-directions-2026.pdf
- NIST SP 800-63B-4 (final, Jul 2025) — https://csrc.nist.gov/pubs/sp/800/63/b/4/final

_Last reviewed: 2026-10_
