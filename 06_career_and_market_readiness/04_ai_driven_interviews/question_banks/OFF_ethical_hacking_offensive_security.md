# OFF · Application Security and Authorized Testing: interview question bank

| Role and market | Levels | Practise with | Score with |
|---|---|---|---|
| [OFF role page](../../01_market_map/roles/OFF_ethical_hacking_offensive_security.md) | NG → Mid → Sr | [Mock kit 4.8](../how_to_run_a_mock_with_any_llm.md#48-security-scenario-defensive-45-minutes) and 4.2 (review variant) | [Rubrics](../rubrics.md), especially section 10 |

This bank prepares you for interviews for authorised security testing and application security roles: penetration tester, application security engineer, product security engineer, security consultant. It deliberately focuses on what these interviews weigh most and what makes the work valuable to clients: methodology, scope and ethics, root-cause understanding of weakness classes, secure code review, threat modelling, clear reporting and remediation. It contains no attack instructions or payloads. Build hands-on skill only in legal practice environments such as PortSwigger Web Security Academy, OWASP Juice Shop, TryHackMe, Hack The Box and picoCTF, and only with written authorisation in real engagements.

## 1. The typical loop

| Round | Duration | What it tests | AI policy you may meet | Mock brief |
|---|---|---|---|---|
| Fundamentals | 45 min | HTTP, authentication and sessions, weakness classes, networking, Linux and Windows basics | AI-off | Kit 4.8 (short) |
| Practical assessment in a provided lab | 2–8 hours or a take-home | Finding and documenting issues in an intentionally vulnerable application within scope | Read the rules; some allow tools including AI, all require your own write-up | A legal practice lab |
| Report review | 30–45 min | Clarity, accuracy, severity, remediation advice | AI-off live discussion | Kit 4.8 with a reporting QUESTION |
| Ethics and legal scenario | 20–30 min | Scope, data handling, disclosure | AI-off | Kit 4.11 |
| Secure code review or threat modelling (AppSec roles) | 45–60 min | Spotting and fixing weaknesses in code and designs | AI-off or AI-on review | Kit 4.2 review variant |
| Behavioural and client communication | 45 min | Consulting skills | AI-off | Kit 4.11, 4.12 |

**Certifications** (for example OSCP, PNPT, CEH, cloud security certifications) are used as filters, particularly by Indian consultancies; public write-ups of legal practice show skill (see the role page).

## 2. How to use this bank

Answer aloud with a timer, then open the guide. Keep every answer at the level of concepts, root causes, defences and process, which is what strong candidates do in these interviews too.

## 3. Questions

### Methodology, scope and ethics

**Q1 · NG · What must be in place before an authorised test begins?**

<details><summary>Answer guide</summary>

- **Testing:** professional and legal foundations.
- **Strong answer:** written authorisation from someone with authority over the systems; a defined scope (hosts, applications, environments, accounts) and explicit exclusions; rules of engagement (testing windows, prohibited actions such as denial-of-service or social engineering unless agreed, rate limits); emergency contacts and a stop procedure; data-handling rules (what you may view or store, encryption, retention, deletion after the engagement); third-party permissions (for example cloud or hosting provider policies); and how findings are reported, including critical issues mid-test.
- **Common mistakes:** treating a verbal OK or a bug bounty listing as permission for anything.
- **Follow-ups:** the client's application calls a third-party API; is it in scope?
</details>

**Q2 · NG · During a test you come across customer personal data in a location outside your scope. What do you do?**

<details><summary>Answer guide</summary>

- **Testing:** ethics under pressure.
- **Strong answer:** stop interacting with that system; do not copy, download or browse further; record only the minimum needed to describe where the exposure is; notify the client's emergency contact immediately as the rules of engagement specify; document what you saw and when; follow instructions on data handling. The exposure itself may be a critical finding for the client.
- **Common mistakes:** "gathering a bit more evidence" first; keeping screenshots of the data.
- **Follow-ups:** the client asks you to keep testing that system; what do you need first?
</details>

**Q3 · Mid · Describe your methodology for testing a web application.**

<details><summary>Answer guide</summary>

- **Testing:** structured approach.
- **Strong answer:** align with a public methodology such as the OWASP Web Security Testing Guide: understand the application (business logic, roles, data flows, technologies); map the attack surface (endpoints, parameters, file uploads, integrations); test categories systematically (configuration, identity and authentication, authorisation, session management, input handling, error handling, cryptography, business logic, client-side); combine automated scanning with manual testing; track coverage; validate findings; report with remediation. Emphasise business-logic and authorisation testing, which tools miss.
- **Common mistakes:** "I run a scanner and verify the results."
- **Follow-ups:** how do you test multi-role authorisation efficiently (a matrix of roles × functions × objects)?
</details>

**Q4 · Mid · The client asks you to test in production. How do you keep it safe?**

<details><summary>Answer guide</summary>

- **Testing:** risk management in testing.
- **Strong answer:** dedicated test accounts and data; avoid state-changing actions on real customer records; throttle request rates; exclude destructive tests or agree on them explicitly with windows and monitoring; coordinate with operations so alerts are expected but still investigated; clear stop conditions; backups confirmed; log everything you do with timestamps for correlation.
- **Common mistakes:** running a full-speed scanner against production without telling anyone.
- **Follow-ups:** your test triggers an outage; what do you do in the next ten minutes?
</details>

**Q5 · Mid · What do automated scanners find well, and what do they miss?**

<details><summary>Answer guide</summary>

- **Testing:** tool judgement.
- **Strong answer:** scanners are good at known-signature issues, missing security headers, outdated components, some input-handling flaws and configuration errors. They miss most authorisation flaws (they do not know who should see what), business-logic flaws, multi-step workflows, chained low-severity issues and context. They also produce false positives that must be validated manually before reporting.
- **Common mistakes:** reporting scanner output unvalidated.
- **Follow-ups:** how do you configure authenticated scanning for an app with several roles?
</details>

### Weakness classes: root causes and fixes

**Q6 · NG · What is the root cause of injection weaknesses, and what is the correct fix?**

<details><summary>Answer guide</summary>

- **Testing:** conceptual depth.
- **Strong answer:** untrusted data is mixed into something an interpreter parses as code or commands (SQL, operating-system commands, templates, LDAP queries), so data can change the structure of the statement. The fix is to keep data and code separate: parameterised queries or prepared statements, safe APIs that do not invoke a shell, auto-escaping template engines; plus input validation by allow-list as a secondary control and least-privilege database accounts to limit impact.
- **Common mistakes:** "escape special characters" or blocklists as the main fix.
- **Follow-ups:** parameters cannot be used for a dynamic column name in ORDER BY; what do you do (map user choices to an allow-list)?
</details>

**Q7 · NG · Broken object-level authorisation: explain the root cause and how a team prevents it systemically.**

<details><summary>Answer guide</summary>

- **Testing:** the most common serious API flaw class.
- **Strong answer:** the server returns or modifies an object identified by a client-supplied ID without checking that the caller is allowed to access that object. Prevention: deny by default; a central authorisation layer or policy engine used by every handler; derive ownership from the authenticated session, not from request parameters; scope database queries by tenant and owner; automated tests that run each endpoint as a different user and expect denial. Unpredictable IDs reduce discoverability but are not a fix.
- **Common mistakes:** "use UUIDs" as the remedy.
- **Follow-ups:** how would you verify a fix across 200 endpoints?
</details>

**Q8 · Mid · Server-side request forgery (SSRF): what is it conceptually, and how do you defend against it?**

<details><summary>Answer guide</summary>

- **Testing:** cloud-era weakness understanding.
- **Strong answer:** a feature that fetches a URL supplied by the user (webhooks, image import, link previews) can be made to send requests from the server's network position to internal services, including cloud metadata services. Defences: avoid fetching user-supplied URLs where possible; allow-list destinations; resolve and validate the destination address after DNS resolution and on every redirect; block private and link-local ranges; route outbound fetches through an egress proxy; use the hardened metadata service version that requires session tokens (for example IMDSv2 on AWS); least-privilege instance roles.
- **Common mistakes:** validating the hostname string only, before DNS resolution.
- **Follow-ups:** how do you test that the egress controls actually block internal ranges?
</details>

**Q9 · Mid · What do you check when reviewing session management?**

<details><summary>Answer guide</summary>

- **Testing:** completeness.
- **Strong answer:** session identifiers with enough randomness; regenerated at login and privilege change; cookie attributes (`Secure`, `HttpOnly`, `SameSite`, scoped path and domain); idle and absolute timeouts; logout invalidates server-side; session listing and revocation for users; password change revokes other sessions; tokens not in URLs or logs; CSRF protection for state-changing requests where cookies are used.
- **Common mistakes:** checking only cookie flags.
- **Follow-ups:** how do these change for stateless tokens (JWT)?
</details>

**Q10 · Mid · Why is deserialising untrusted data dangerous, and what do you recommend?**

<details><summary>Answer guide</summary>

- **Testing:** understanding of a high-impact class.
- **Strong answer:** native object deserialisation in many languages can instantiate arbitrary types and invoke code during reconstruction, so attacker-controlled input can lead to code execution or logic abuse. Recommend data-only formats (JSON with schema validation) instead of native serialisation for untrusted input; if unavoidable, strict type allow-lists, integrity protection (signatures) on serialised data, and keeping libraries updated.
- **Common mistakes:** "validate the input string" as the fix.
- **Follow-ups:** a legacy system must accept serialised objects from partners; options.
</details>

### Secure code review

**Q11 · Mid · Review this handler.**

```python
@app.get("/download")
def download():
    name = request.args["file"]
    return send_file(os.path.join("/srv/reports", name))
```

<details><summary>Answer guide</summary>

- **Testing:** spotting path handling flaws and fixing them properly.
- **Strong answer:** the file name is user-controlled and joined to a base directory, so a name containing parent-directory segments or an absolute path (which makes `os.path.join` discard the base) can reach files outside `/srv/reports`. There is also no authorisation: any user can download any report. Fix: do not accept paths; accept a report ID, look it up in the database with an ownership check, and serve the stored file; if names must be used, use a safe-join helper (for example `send_from_directory`) and verify the resolved real path stays under the base directory. Add tests for both the traversal case and cross-user access.
- **Common mistakes:** stripping `../` with string replacement.
- **Follow-ups:** how would a static analysis rule detect this pattern?
</details>

**Q12 · Mid · Review this token check.**

```js
app.get("/api/me", (req, res) => {
  const token = req.headers.authorization?.split(" ")[1];
  const claims = jwt.decode(token);
  if (!claims) return res.sendStatus(401);
  res.json(getUser(claims.sub));
});
```

<details><summary>Answer guide</summary>

- **Testing:** authentication implementation review.
- **Strong answer:** `decode` reads the claims without verifying the signature, so the server trusts whatever a client puts in the token. Fix: `jwt.verify` with the correct key, an explicit allow-list of algorithms, and checks of expiry, issuer and audience; handle verification errors as 401; keep keys in a secret manager with rotation. Add a test with a token signed by the wrong key.
- **Common mistakes:** noticing only the missing expiry check.
- **Follow-ups:** how do you revoke a JWT before it expires?
</details>

**Q13 · NG · Review this password storage.**

```python
def store_password(user, password):
    user.pw_hash = hashlib.sha256(password.encode()).hexdigest()
```

<details><summary>Answer guide</summary>

- **Testing:** cryptographic hygiene.
- **Strong answer:** a fast, unsalted hash lets anyone with the database test billions of guesses per second and reuse precomputed tables. Use a slow, salted password-hashing function: Argon2id (the OWASP Password Storage Cheat Sheet recommends at minimum 19 MiB memory, 2 iterations, 1 degree of parallelism), or scrypt or bcrypt with an appropriate work factor. Upgrade existing hashes by rehashing at next login. Compare in constant time via the library.
- **Common mistakes:** adding a single global salt to SHA-256.
- **Follow-ups:** you must migrate 10 million existing SHA-256 hashes now; options (wrap the old hash in Argon2id, then rehash on login).
</details>

**Q14 · Sr · How do you run secure code review across 80 repositories with a team of three?**

<details><summary>Answer guide</summary>

- **Testing:** scaling AppSec.
- **Strong answer:** risk-rank repositories (internet exposure, data sensitivity, payment or authentication logic); automate the baseline (SAST, dependency and secret scanning in CI with tuned rules and low false positives); manual review focused on high-risk changes (authentication, authorisation, cryptography, file handling, deserialisation) flagged by code-owner rules; secure-by-default libraries and frameworks; security champions in product teams; review checklists; track findings to root causes.
- **Common mistakes:** trying to review every pull request manually.
- **Follow-ups:** developers ignore SAST findings; how do you fix trust in the tool?
</details>

### Threat modelling

**Q15 · Mid · Threat-model a password-reset flow.**

<details><summary>Answer guide</summary>

- **Testing:** structured threat modelling (for example STRIDE).
- **Strong answer:** draw the flow (request reset, token issued, email delivered, token used, password changed). Threats: account enumeration through different responses (spoofing/information disclosure); guessable or long-lived tokens; token leakage through referrer headers or logs; tokens not invalidated after use; host-header manipulation of reset links; email account compromise; no rate limiting; existing sessions not revoked. Mitigations: uniform responses, high-entropy single-use tokens with short expiry stored hashed, fixed link domain, rate limits, notification to the user, session revocation, MFA re-verification for sensitive accounts.
- **Common mistakes:** listing generic threats without tying them to steps in the flow.
- **Follow-ups:** support staff can trigger resets; what new threats appear?
</details>

**Q16 · Sr · Threat-model an inbound payment webhook endpoint.**

<details><summary>Answer guide</summary>

- **Testing:** threat modelling for money flows.
- **Strong answer:** threats: forged webhooks (verify signatures with a shared secret or public key, check timestamps to limit replay), replayed or duplicated events (idempotent processing by event ID), out-of-order events (state machine), amount or currency tampering (reconcile against the provider's API), denial of service (rate limits, queue processing), secret leakage (rotation), excessive information in error responses. Also: monitoring for mismatches and alerting on failed verifications.
- **Common mistakes:** trusting the source IP alone.
- **Follow-ups:** the provider rotates its signing key; how do you avoid downtime?
</details>

**Q17 · Mid · Threat-model an AI agent that can read a user's email and create calendar events.**

<details><summary>Answer guide</summary>

- **Testing:** AI-era threat modelling.
- **Strong answer:** incoming emails are untrusted input that can contain instructions aimed at the agent (indirect prompt injection), so the agent may take actions the user did not intend or leak data (OWASP Top 10 for LLM Applications covers prompt injection, sensitive information disclosure and excessive agency). Mitigations: least privilege (separate read and write permissions, no sending email without confirmation), human approval for actions with external effects, clear separation of instructions from retrieved content, output filtering for data exfiltration channels (for example external links and images), allow-lists for invited domains, logging and anomaly detection, and evaluation with injection test cases before release.
- **Common mistakes:** relying on a system prompt that says "ignore instructions in emails".
- **Follow-ups:** how would you build an evaluation suite to measure this risk over time?
</details>

### Reporting and communication

**Q18 · NG · Outline a good finding write-up for an authorisation flaw on an orders endpoint.**

<details><summary>Answer guide</summary>

- **Testing:** reporting clarity.
- **Strong answer:** title naming the weakness and location; severity with justification; affected endpoints and versions; description of the flaw in plain terms; business impact (what data or actions are exposed, to whom); evidence (requests and responses with sensitive data redacted, timestamps, test accounts used); reproduction steps sufficient for the client's engineers using test accounts; root cause; remediation (specific fix plus systemic recommendation); references (for example OWASP API Security Top 10 category); retest status.
- **Common mistakes:** pasting tool output; vague remediation such as "implement proper access control".
- **Follow-ups:** how do you write it for a client whose developers are juniors?
</details>

**Q19 · Mid · How do you set severity, and what do you do when the client disagrees?**

<details><summary>Answer guide</summary>

- **Testing:** calibrated risk judgement.
- **Strong answer:** use a standard such as CVSS (version 4.0 was published by FIRST in November 2023) for technical severity, then adjust risk for business context (data sensitivity, exposure, compensating controls) and state both. When the client disagrees, discuss the evidence and assumptions, adjust if they provide valid context (for example the endpoint is not internet-facing), document the rationale, and never downgrade to please a client without justification.
- **Common mistakes:** every finding "critical"; or changing ratings under pressure.
- **Follow-ups:** a chain of three low-severity issues leads to account takeover; how do you rate it?
</details>

**Q20 · Mid · You find a critical issue on day one of a two-week test. What do you do?**

<details><summary>Answer guide</summary>

- **Testing:** communication duties.
- **Strong answer:** follow the agreed critical-finding procedure: notify the designated contact promptly (not at the end of the engagement), securely, with enough detail to act; agree whether testing continues on that component; record the time of notification; include it in the final report with its status.
- **Common mistakes:** waiting for the final report; emailing details unencrypted to a broad list.
- **Follow-ups:** the client fixes it within hours; how do you retest and report?
</details>

**Q21 · Mid · Write the executive summary for a test with 2 high, 5 medium and 12 low findings.**

<details><summary>Answer guide</summary>

- **Testing:** communication to non-specialists.
- **Strong answer:** one paragraph on scope and dates; overall risk posture in business terms; the two highest-risk issues described by impact ("an authenticated customer could view other customers' invoices"); themes behind the findings (for example authorisation checks implemented inconsistently); prioritised recommendations with effort; what went well. No jargon, no tool names.
- **Common mistakes:** a list of vulnerability names.
- **Follow-ups:** the board asks "are we secure now?"; how do you answer honestly?
</details>

### Remediation and programmes

**Q22 · Mid · The developer says the issue is fixed. How do you verify?**

<details><summary>Answer guide</summary>

- **Testing:** verification discipline.
- **Strong answer:** retest the original case and its variants (other parameters, other HTTP methods, other roles, other endpoints sharing the same code path); review the fix in code if available (root cause vs symptom); check that a regression test was added; confirm deployment to the tested environment and version; report retest status precisely.
- **Common mistakes:** retesting the exact request only.
- **Follow-ups:** the fix blocks your test but the root cause remains; how do you report it?
</details>

**Q23 · Sr · The same weakness keeps appearing in every test. What do you recommend?**

<details><summary>Answer guide</summary>

- **Testing:** systemic thinking.
- **Strong answer:** move from findings to causes: secure-by-default framework components (a central authorisation helper, auto-escaping templates), lint or static analysis rules that block the pattern, developer training tied to their own code, threat modelling at design time, security acceptance criteria in tickets, and metrics on recurrence by team.
- **Common mistakes:** more testing as the only answer.
- **Follow-ups:** how do you prove the systemic fix worked?
</details>

**Q24 · Mid · Vulnerability disclosure programme or bug bounty: what is the difference, and what must either have?**

<details><summary>Answer guide</summary>

- **Testing:** programme knowledge.
- **Strong answer:** a vulnerability disclosure programme (VDP) gives anyone a safe, published way to report issues, usually without payment; a bug bounty adds rewards and often a narrower, managed scope. Both need: a clear scope and rules, a safe-harbour statement for good-faith research, a reporting channel (including a `security.txt` file as specified in RFC 9116), triage capacity and response time targets, coordination with reporters on disclosure timelines, and a process to fix and credit. Start with a VDP before a bounty.
- **Common mistakes:** launching a bounty without triage capacity.
- **Follow-ups:** a researcher reports an issue in a system outside your scope; what do you do?
</details>

### AI-era judgement

**Q25 · Mid · How do you use AI tools responsibly in an authorised test?**

<details><summary>Answer guide</summary>

- **Testing:** professional judgement with AI.
- **Strong answer:** check the engagement contract and client policy first: client data, source code and findings may not be sent to third-party AI services without permission; prefer approved or local tools; use AI for note organisation, report drafting from your own verified findings, explaining unfamiliar code, and test-case ideas; never let a tool take autonomous actions against targets or step outside scope; verify every AI-suggested finding manually before reporting; disclose AI use if the client requires it.
- **Common mistakes:** pasting client code into a public chatbot.
- **Follow-ups:** an AI tool claims a critical finding you cannot reproduce; do you report it?
</details>

**Q26 · Mid · An automated tool reports 40 "critical" findings overnight. What do you do before telling the client?**

<details><summary>Answer guide</summary>

- **Testing:** validation and noise reduction.
- **Strong answer:** deduplicate by root cause and location; validate each safely by hand within scope; discard false positives with notes on why; re-rate severity with context; group related issues; report only validated findings, with evidence; tune the tool to reduce repeat noise.
- **Common mistakes:** forwarding tool output; or dismissing all of it.
- **Follow-ups:** how do you track false-positive rates per tool?
</details>

### Behavioural

**Q27 · Mid · Tell me about a client or team that pushed back on your findings.**

<details><summary>Answer guide</summary>

- **Testing:** consulting maturity.
- **Strong answer:** the finding and their objection; how you listened for valid context; how you demonstrated impact safely and clearly; what changed (rating, wording, or nothing, with rationale); the relationship afterwards; what you now do earlier (agree on severity criteria at kickoff).
- **Common mistakes:** "they did not understand security".
- **Follow-ups:** what if they asked you to remove a finding from the report?
</details>

## Sources

Checked October 2026.

- OWASP, *Web Security Testing Guide*: https://owasp.org/www-project-web-security-testing-guide/ ; *API Security Top 10*: https://owasp.org/API-Security/ ; *Password Storage Cheat Sheet*: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html ; *Top 10 for LLM Applications*: https://genai.owasp.org/
- FIRST, *CVSS v4.0* (published November 2023): https://www.first.org/cvss/v4-0/
- IETF, *RFC 9116: A File Format to Aid in Security Vulnerability Disclosure* (April 2022): https://www.rfc-editor.org/rfc/rfc9116
- Legal practice environments: PortSwigger Web Security Academy https://portswigger.net/web-security ; OWASP Juice Shop https://owasp.org/www-project-juice-shop/
- Loop structure: [OFF role page](../../01_market_map/roles/OFF_ethical_hacking_offensive_security.md).

_Last reviewed: 2026-10_
