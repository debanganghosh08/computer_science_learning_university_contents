# SEC303 · Labs and projects

Everything runs in your own identity lab: a Windows Server domain controller and two domain-joined clients (evaluation licences are enough), a free Microsoft Entra ID test tenant (for example from the Microsoft 365 Developer Program, if you qualify, or a trial), and Keycloak in a container. Assessment tools such as PingCastle and BloodHound Community Edition are run **only against this lab**. Each submission includes configuration exports or scripts in Git, before/after evidence, and a short write-up with numbers.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Identity lab build | Domain controller, two clients, Entra test tenant, Keycloak federated with one test app | Lab diagram, build notes, proof of SSO into the test app | 5 h |
| 2 · Lifecycle and SCIM | Provision and deprovision users to two apps with SCIM; script a 90-day dormant-account report for AD and Entra | SCIM logs, report script and output, time-to-deprovision measurement | 4 h |
| 3 · Phishing-resistant MFA | Enrol a FIDO2 key or passkey in Entra and Keycloak; host a look-alike login page *in your lab* and show the passkey refuses it while TOTP is accepted | Screen recordings, explanation of origin binding, help-desk verification procedure | 4 h |
| 4 · Tokens and app consent | Trace an OIDC login; decode ID and access tokens; inventory all app registrations and grants in the tenant and remove risky ones | Annotated trace, app inventory with risk ratings, clean-up record | 4 h |
| 5 · Conditional Access | Build five policies in report-only mode (block legacy auth, require phishing-resistant MFA for admins, device compliance, risky sign-ins, location) and read the impact | Policy exports, impact analysis, break-glass exclusion proof | 4 h |
| 6 · PIM and LAPS | Make all admin roles eligible with approval; deploy Windows LAPS; alert on break-glass sign-in | Configuration evidence, alert test | 4 h |
| 7 · AD hardening and attack paths | Run PingCastle and BloodHound CE on the lab domain; apply eight hardening changes; remove the three shortest paths to Domain Admins | Before/after reports and graphs, change log | 6 h |
| 8 · Cloud and workload identity | Fix five Secure Score items; replace a client secret with a managed identity; configure GitHub Actions OIDC to a cloud account with a restrictive trust condition | Evidence, trust-policy file, test showing another repository is refused | 4 h |
| 9 · Secrets and non-human identities | Scan a lab repository's history with Gitleaks; rotate findings; build an inventory of service accounts, app registrations and API keys with owners and expiry | Scan report, rotation proof, NHI inventory | 3 h |
| 10 · Identity detections | Write and test six detections: password spray, MFA fatigue pattern, new MFA method, risky OAuth consent, RC4 service tickets, replication from a non-DC host | Rules, test events generated in your lab, false-positive notes | 6 h |

## Projects

### P1 · Phishing-resistant authentication and recovery plan (L1, ~6 hours)

**Real-world inspiration.** CISA's advisory on Scattered Spider (AA23-320A, updated July 2025) describes help-desk impersonation, push bombing and SIM swapping, and recommends phishing-resistant MFA. Mandiant's M-Trends 2026 reports voice phishing as the second most common initial vector (11%). The company below is an illustrative Indian stockbroker with 1,200 employees and a 24×7 help desk.

**What to build.** A plan the CISO could approve: (1) a ranked table of authenticators by NIST SP 800-63B-4 assurance and phishing resistance; (2) the target state per user group (administrators, traders, call-centre staff, contractors); (3) a help-desk identity verification procedure for password and MFA resets; (4) a phased rollout with exception handling; (5) five metrics with targets.

**Acceptance criteria**
- Every user group has a primary and a backup authenticator, and the plan states how each group recovers a lost authenticator without a phishable step.
- The help-desk procedure is tested in a role-play against three scripted voice-phishing calls written by a classmate; at least two of three are refused at the correct step.
- Exceptions carry an owner and an expiry date of no more than 90 days.
- Metrics include phishing-resistant coverage for administrators (target 100%) and time-to-revoke after a reported lost device.

**Stretch goals.** Implement the administrator portion in your Entra tenant with authentication strengths and Conditional Access.

**What it proves to an employer.** You understand that MFA strength depends on recovery and people, not only on the authenticator.

### P2 · Tier 0 attack-path reduction (L2, ~15 hours)

**Real-world inspiration.** Ransomware intrusions described in CISA #StopRansomware advisories commonly involve gaining domain administrator rights before encryption. Defenders now use attack-path tools such as BloodHound Community Edition and PingCastle to remove those paths before attackers find them.

**What to build.** Seed your lab domain with 12 common misconfigurations from a written list (for example: a service account with a weak password and a service principal name, unconstrained delegation on a server, a vulnerable ADCS certificate template, nested group memberships granting admin, local admin reuse, stale privileged accounts). Alternatively use an open-source deliberately misconfigured AD lab, inside your isolated network. Then:
1. measure: PingCastle score and BloodHound CE paths to Domain Admins and other Tier 0 assets;
2. remediate in priority order with a change record;
3. add detections for the residual risks;
4. write a one-page Tier 0 definition and admin model.

**Acceptance criteria**
- Before/after numbers: paths to Domain Admins reduced by at least 90%, PingCastle risk score improved, with screenshots and exported data.
- Every change states what could break, how it was tested, and how to roll it back.
- At least four detections for Tier 0 changes (group membership, GPO changes on Tier 0, certificate template changes, replication rights) fire on test changes you make.
- No assessment tool is pointed at anything outside the lab; the README states the network isolation used.

**Stretch goals.** Rotate krbtgt twice safely and document the procedure; add Windows LAPS and measure the path reduction it alone gives.

**What it proves to an employer.** You can find and close the paths ransomware operators use in Active Directory, with evidence, which is core work for IAM and SOC engineers in any Windows enterprise.

### P3 · Identity threat detection and response for a SaaS-first company (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Three public cases show identity attacks without malware on endpoints: the 2024 Snowflake customer intrusions (infostealer credentials, no MFA, no network allow lists; Mandiant), Midnight Blizzard's 2023–24 intrusion at Microsoft (password spray on a test account, then a legacy OAuth app with high privileges), and the August 2025 Salesloft Drift token theft (integration OAuth tokens used to export Salesforce data; Google Threat Intelligence Group). The company below is illustrative.

**What to build.** For a 400-person company using Entra ID (or Keycloak), a CRM and a cloud data warehouse (simulated with sample audit logs you generate), deliver:
1. an identity inventory: human users, privileged roles, app registrations, third-party OAuth grants, service accounts and tokens, with owners;
2. ten detections across sign-in, audit and SaaS logs (including a new OAuth grant with broad scopes, an integration token used from a new network, mass export from the CRM, sign-in with a credential not used for over a year, MFA method added then a sign-in from a new country);
3. a response workflow (SOAR or scripts) that revokes sessions and tokens and disables an integration, **only after a human approves**;
4. an OAuth and integration governance policy (approval, scope limits, expiry, review);
5. a tabletop based on a vendor-token compromise, with an after-action report.

**Acceptance criteria**
- Each detection is triggered by a test you perform in the lab and has a documented false-positive scenario.
- From an approved alert, the workflow revokes the relevant sessions and tokens within 5 minutes, and a test shows the revoked token is refused.
- The inventory covers 100% of app registrations and grants in the test tenant; each has an owner or is removed.
- The tabletop report includes the order of eviction steps, the logs reviewed for data export, the secrets found in exported data that must be rotated, and the DPDP Act notification assessment.
- A two-page executive summary explains the residual risk in plain language.

**Stretch goals.** Add continuous access evaluation or sender-constrained tokens for one app and measure the effect; add an AI agent identity with a narrowly scoped permission set and show what it cannot do.

**What it proves to an employer.** You can defend identity where modern breaches actually happen: tokens, integrations and SaaS, not only passwords. This maps directly to ITDR, IAM engineering and cloud security roles.

## Feeds into

- [SEC401 Detection Engineering and Threat Hunting](../../year_4/SEC401_detection_engineering_and_threat_hunting/README.md): identity detections become tested, version-controlled rules.
- [SEC402 Digital Forensics and Incident Response](../../year_4/SEC402_digital_forensics_and_incident_response/README.md): eviction order and credential resets in real incidents.
- [SEC403 Malware Analysis for Defenders](../../year_4/SEC403_malware_analysis_for_defenders/README.md): infostealers and the credentials they harvest.
- [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md): cloud IAM and workload identity at scale.
