# Interview rubrics

| Used by | Levels | Read with |
|---|---|---|
| Every question bank, the [mock kit](how_to_run_a_mock_with_any_llm.md) and the [simulation days](simulation_days.md) | Intern/new grad (L2), mid-level (L3), senior (L4) | [Section overview](README.md) · [Curriculum levels](../../docs/CONTENT_STANDARD.md#3-levels-and-mastery-gates) |

A rubric turns "that felt good" into evidence. Real companies write their own rubrics, and they differ; the structure below follows the common pattern of scoring several independent dimensions with written evidence, then deciding per round and per loop. Use it to grade yourself, a friend, or an LLM interviewer's transcript.

---

## 1. How to score

**The scale (per dimension).**

| Score | Label | Meaning |
|---|---|---|
| 4 | Strong hire | Clearly above the bar for this level; you would argue for this candidate |
| 3 | Hire | Meets the bar for this level with minor gaps |
| 2 | Lean no hire | Below the bar; real gaps that would show up on the job |
| 1 | Strong no hire | Far below the bar, or a red flag (section 12) |

There is no middle score on purpose: every score must take a side.

**Evidence rule.** Every score needs at least one piece of evidence: a quote, a timestamp in the recording, or a line of code. "Seemed smart" is not evidence. "At 12:40 asked whether the input could contain duplicates before coding" is.

**Level calibration.** Each dimension below describes what a **3 (meets the bar)** looks like at three levels. The same performance can be a 3 for a new graduate and a 2 for a senior engineer. Score against the level you are targeting.

**Round outcome (a simple, transparent rule).**

- **Hire:** every must-have dimension for that round scores 3 or 4, and no dimension scores 1.
- **Lean hire:** exactly one must-have dimension scores 2, the others 3 or above, and no 1.
- **No hire:** anything else.

**Loop outcome.** Hire if most rounds are Hire, none is a Strong no hire on a must-have, and there is no integrity red flag. One bad round in five is often survivable; a pattern is not. (Analysis: this mirrors how many debriefs work, but each company sets its own rule.)

---

## 2. Problem solving

Understanding the problem, choosing an approach, and reasoning about its cost.

| Score | What it looks like |
|---|---|
| 4 | Clarifies inputs, outputs, constraints and edge cases before coding; states a brute-force approach and its complexity, then improves it with a named insight; compares two viable approaches with trade-offs; adapts quickly when a constraint changes |
| 3 | Asks the important clarifying questions; reaches a correct, reasonably efficient approach with small nudges; states time and space complexity correctly |
| 2 | Starts coding before understanding; needs several hints to find an approach; complexity analysis wrong or missing |
| 1 | Cannot reach a working approach even with hints; or memorised a solution and cannot explain why it works |

| Level | Meets the bar (3) |
|---|---|
| Intern / new grad | Standard patterns (two pointers, hashing, BFS/DFS, heaps, binary search, simple DP) applied correctly; one or two hints are acceptable |
| Mid-level | No hints on standard problems; handles a twist (streaming input, memory limit, concurrency) with reasoning |
| Senior | Frames the problem in context ("in production I'd also need..."), spots ambiguity others miss, chooses the simplest approach that meets the real constraint |

---

## 3. Code quality

Correctness, readability and structure of the code you write (or accept from an AI).

| Score | What it looks like |
|---|---|
| 4 | Correct on first full run or after one self-found fix; small functions, clear names, no duplication; idiomatic for the language; handles empty, single, large and invalid inputs deliberately |
| 3 | Correct after a couple of fixes; readable; minor naming or structure issues; most edge cases handled |
| 2 | Works only for the main case; tangled control flow; magic numbers; off-by-one or null errors left unfound |
| 1 | Does not run, or is unreadable; or pasted code the candidate cannot explain |

| Level | Meets the bar (3) |
|---|---|
| Intern / new grad | Working, readable code in one language; standard library used sensibly |
| Mid-level | Code you would approve in review: error handling, clear interfaces, sensible module boundaries |
| Senior | Code designed for change: extension points where they matter, none where they do not; explains what they would refactor with more time |

---

## 4. Testing and verification

How you establish that code, a query, a design or an AI output is actually correct.

| Score | What it looks like |
|---|---|
| 4 | Writes or walks through tests before being asked: normal, boundary, adversarial and large inputs; uses invariants and assertions; checks AI output against a spec or test rather than by eye; finds their own bugs |
| 3 | Tests the main case and the obvious edge cases when prompted or near the end; catches most of their own mistakes |
| 2 | Declares "done" without testing; tests only the example given |
| 1 | Cannot describe how they would know the code is right; accepts AI output with no check |

| Level | Meets the bar (3) |
|---|---|
| Intern / new grad | Dry-runs code on two or three inputs including one edge case |
| Mid-level | Proposes a small test suite with boundaries and failure cases; uses a property or invariant where it fits |
| Senior | Chooses the test strategy for the risk (unit vs integration vs property-based vs load); explains what cannot be tested and how to monitor it instead |

---

## 5. Communication

Thinking aloud, structure, listening and writing.

| Score | What it looks like |
|---|---|
| 4 | Narrates the plan before acting; signposts ("three parts: ..."); checks in at the right moments; takes hints gracefully and uses them; explains trade-offs in plain language; concise |
| 3 | Mostly clear; occasional silent stretches; answers questions directly |
| 2 | Long silences or rambling; the interviewer has to pull information out; defensive about hints |
| 1 | Cannot explain their own approach; dismissive or disrespectful |

| Level | Meets the bar (3) |
|---|---|
| Intern / new grad | Explains what they are doing and why, in order |
| Mid-level | Drives the conversation; summarises decisions; states assumptions explicitly |
| Senior | Adjusts depth to the audience; makes the interviewer's job easy; writes a clear decision record when asked |

---

## 6. Debugging and incident handling

Moving from symptom to cause with evidence, and acting safely under pressure.

| Score | What it looks like |
|---|---|
| 4 | Forms hypotheses, ranks them by likelihood and cost to test, asks for the specific evidence (logs, metrics, traces, recent changes) that splits them; mitigates first in production (rollback, failover, feature flag), then finds root cause; communicates status on a cadence |
| 3 | Systematic, finds the cause with some prompting; mitigation considered |
| 2 | Random changes; ignores recent deploys; goes straight to root cause while users are still affected |
| 1 | Guesses without evidence; proposes risky actions (deleting data, restarting everything) without considering impact |

| Level | Meets the bar (3) |
|---|---|
| Intern / new grad | Reads an error and a stack trace correctly; isolates the failing input; uses a debugger or prints deliberately |
| Mid-level | Uses observability data; knows the common failure modes of their stack; writes a blameless postmortem |
| Senior | Leads an incident: roles, communication, decision to roll back under uncertainty; turns findings into systemic fixes |

---

## 7. System design

Score each sub-dimension separately, then take the round score as the lower of "core" (7.1–7.5) and "depth" (7.6–7.9) averages, rounded down. Must-haves for most design rounds: 7.1, 7.3, 7.4, 7.6, 7.9.

| Sub-dimension | A 4 looks like | A 2 looks like |
|---|---|---|
| 7.1 Requirements and scope | Separates functional and non-functional requirements; asks about scale, latency, consistency, read/write mix, regions; states what is out of scope | Starts drawing boxes immediately |
| 7.2 Estimation | Back-of-envelope numbers (requests per second, storage per year, bandwidth) that drive decisions | No numbers, or numbers that are never used |
| 7.3 API and data model | Clear endpoints or events with idempotency where needed; schema and keys chosen for the access patterns | Vague "store it in a database" |
| 7.4 Architecture and data flow | Components with clear responsibilities; walks a request end to end; justifies sync vs async | Box soup; cannot trace one request |
| 7.5 Scale and performance | Identifies the bottleneck; caching, partitioning, replication and indexing chosen for a reason | Adds "a cache" and "sharding" with no reasoning |
| 7.6 Reliability and failure modes | Names what fails (node, zone, dependency, network partition) and the behaviour in each; retries with backoff and idempotency; degraded modes | Assumes nothing fails |
| 7.7 Security and privacy | Authentication, authorisation, encryption, least privilege, PII handling, abuse cases | Mentions "HTTPS" only |
| 7.8 Cost and operability | Rough cost drivers; observability (metrics, logs, traces, SLOs); deployment and migration path | Ignores how it is run |
| 7.9 Trade-offs and evolution | States what was traded and why; what changes at 10× scale; what to build first | One "right answer" with no alternatives |

| Level | Meets the bar (3) |
|---|---|
| Intern / new grad | Rarely given a full design round. When given one: a working single-region design with a sensible data model and one scaling step |
| Mid-level | A complete design for a well-known problem with correct trade-offs and failure handling; can go deep on one component |
| Senior | Drives the whole session; finds the hard part early; makes and defends decisions under ambiguity; covers operability, migration and cost unprompted |

**ML and LLM system design add-ons.** Add these sub-dimensions for ML, data-science-product and LLM/agent design rounds:

| Sub-dimension | A 4 looks like |
|---|---|
| 7.10 Problem framing and metrics | Converts a business goal into an ML or LLM task, an offline metric and an online metric, and says how they could disagree |
| 7.11 Data and labels | Sources, label quality, leakage, freshness, privacy, feedback loops |
| 7.12 Model or prompt choice | Starts with the simplest baseline (rules, logistic regression, retrieval only, a small model); justifies complexity with expected gain |
| 7.13 Evaluation | Offline evaluation set with slices; for LLMs, task-specific evals (golden sets, rubric grading, human review sample), regression tests on prompt or model changes; online A/B or shadow tests |
| 7.14 Serving, latency and cost | Batch vs online; caching; token or GPU cost per request; fallbacks when the model is slow or down |
| 7.15 Safety and abuse | For LLM systems: prompt injection treated as untrusted input, tool permissions scoped, human approval for irreversible actions, output filtering, logging for audit |
| 7.16 Monitoring and iteration | Drift, quality metrics in production, alerting, retraining or prompt-update process |

---

## 8. AI-collaboration skill

How well you work with an AI assistant when it is allowed. This dimension is must-have in every AI-on round. Its criteria follow what employers say they look for: when and how to use AI, breaking down ambiguous requirements, and identifying and fixing issues in AI-generated code ([Canva, Jun 2025](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)); prompt engineering, output validation and debugging ([Google pilot, reported May 2026](https://finance.yahoo.com/sectors/technology/articles/asking-kid-math-test-without-151500986.html)).

| Sub-skill | A 4 looks like | A 2 looks like |
|---|---|---|
| 8.1 Framing and context | Gives the assistant the relevant files, constraints, interfaces and acceptance criteria; asks for a plan before code on larger tasks | Pastes the whole problem and accepts the first answer |
| 8.2 Decomposition and delegation | Delegates well-defined subtasks (boilerplate, a parser, test scaffolding); keeps the design decisions and tricky logic for themself | Delegates the entire task, including decisions they cannot evaluate |
| 8.3 Verification | Reads every line before accepting; runs tests; checks edge cases, complexity, security and API correctness; asks the AI to critique its own output only as a supplement | Accepts output because it "looks right" |
| 8.4 Error detection and recovery | Spots hallucinated APIs, off-by-one errors, missing error handling, wrong concurrency assumptions; fixes them or re-prompts with a precise correction | Loops on vague re-prompts ("still wrong, fix it") |
| 8.5 Judgement on when not to use AI | Writes small or subtle code directly when that is faster or safer; does not paste secrets or confidential data | Uses AI for everything, including two-line changes |
| 8.6 Transparency | Says aloud what the AI produced and what they changed; can explain every accepted line | Presents AI output as their own reasoning |
| 8.7 Efficiency | Finishes more, at higher quality, than they would alone | Spends the interview prompting and debugging the assistant |

| Level | Meets the bar (3) |
|---|---|
| Intern / new grad | Uses the assistant for clear subtasks; reads and tests what it produces; catches obvious errors |
| Mid-level | Plans before prompting; catches subtle errors (concurrency, boundary, security); output is production-quality |
| Senior | Uses AI to explore alternatives quickly, then decides; sets guardrails (tests first, small diffs); explains how they would review AI-generated changes from a team |

**Observable evidence to note during an AI-on round:** number of suggestions rejected and why; time from AI output to first test run; any bug found in AI output by the candidate (strong positive); any bug the interviewer had to point out (negative); whether the candidate could explain a randomly chosen accepted line.

---

## 9. Data reasoning

For SQL, analytics, data science and experiment rounds.

| Score | What it looks like |
|---|---|
| 4 | Defines the question and the metric precisely (numerator, denominator, time window, unit); checks data quality first (duplicates, nulls, late data, timezone); chooses a valid method (correct test, sufficient power, correct unit of randomisation); states uncertainty and confounders; recommends an action |
| 3 | Correct SQL or analysis with minor gaps in validity checks; sensible recommendation |
| 2 | Correct-looking numbers on an ill-defined metric; ignores duplicates or bias; overclaims causation |
| 1 | Wrong joins or aggregations that change the answer; no awareness of uncertainty |

| Level | Meets the bar (3) |
|---|---|
| Intern / new grad | Joins, group-bys and window functions correct; knows what a p-value and a confidence interval mean |
| Mid-level | Designs an experiment end to end; catches Simpson's paradox, novelty effects and sample ratio mismatch |
| Senior | Chooses which question is worth answering; designs metric systems (guardrails, north star); communicates limits to executives |

---

## 10. Security judgement

For security, cloud, architecture and any round with a security component. Defensive and authorised work only.

| Score | What it looks like |
|---|---|
| 4 | Prioritises by risk (likelihood × impact), uses a framework (STRIDE, the OWASP Top 10, MITRE ATT&CK for detection mapping, NIST CSF), proposes layered controls, preserves evidence, respects scope and law, and explains residual risk to non-specialists |
| 3 | Finds the main risks and proposes sensible controls; minor gaps |
| 2 | Lists tools instead of reasoning; ignores business impact; one control as the whole answer |
| 1 | Suggests actions outside authorisation, destroys evidence, or dismisses a serious risk |

| Level | Meets the bar (3) |
|---|---|
| Intern / new grad | Knows authentication vs authorisation, common weakness classes and their fixes, least privilege, why logs matter |
| Mid-level | Runs a threat model or triage alone; writes a clear finding with remediation |
| Senior | Sets security direction; makes risk trade-offs with the business; designs controls that teams adopt |

---

## 11. Behavioural and hiring-manager rounds

| Dimension | A 4 looks like | A 2 looks like |
|---|---|---|
| 11.1 Ownership | Took responsibility beyond their task; followed through after launch | Describes what "the team" did; no personal actions |
| 11.2 Impact and scope | Measurable results matching the target level | Activity without outcome |
| 11.3 Collaboration and conflict | Disagreed with data, listened, reached a decision, kept the relationship | Blames others; avoids conflict |
| 11.4 Learning and self-awareness | Names a real mistake, its cost, and the changed behaviour | "My weakness is working too hard" |
| 11.5 Judgement with AI and data | Clear rules for what they delegate to AI, how they verify, what they never paste into a tool | No view, or uncritical use |
| 11.6 Integrity | Consistent story under follow-up; credits others | Story changes under probing |

| Level | Expected scope of stories |
|---|---|
| Intern / new grad | Course projects, internships, clubs, open source: own work, own learning |
| Mid-level | Features end to end, on-call, cross-team coordination |
| Senior | Multi-team or multi-quarter outcomes, mentoring, setting direction, decisions under ambiguity |

---

## 12. Red flags

Any one of these is a 1 on the affected dimension and is usually decisive:

- Integrity: using unpermitted help, a story that changes under probing, claiming others' work.
- Unsafe actions: proposing destructive production changes without considering impact; security actions outside authorisation.
- Unexplainable code: cannot explain lines they submitted, including AI-generated ones.
- Disrespect towards the interviewer, former colleagues or users.
- Refusing to engage with a hint or a changed constraint.

---

## 13. Which dimensions each round uses

**M** = must-have, **S** = scored but not decisive, blank = not scored.

| Round type | Problem solving | Code quality | Testing and verification | Communication | Debugging | System design | AI collaboration | Data reasoning | Security | Behavioural |
|---|---|---|---|---|---|---|---|---|---|---|
| Coding (AI-off) | M | M | S | M | S | | | | | |
| AI-assisted coding | M | M | M | S | S | | M | | | |
| AI code review | S | M | M | S | S | | M | | S | |
| Low-level design / machine coding | M | M | S | S | | S | | | | |
| System design | S | | | M | | M | | | S | |
| ML system design | S | | | M | | M (with 7.10–7.16) | | S | | |
| LLM / agent system design | S | | S | M | | M (with 7.10–7.16) | S | | M | |
| Data case | M | | | M | | | | M | | |
| SQL | M | S | S | S | | | | M | | |
| Security scenario (defensive) | S | | | M | S | | | | M | |
| Cloud / SRE incident | S | | | M | M | S | | | S | |
| Frontend machine coding | M | M | S | S | | S | | | | |
| Behavioural | | | | M | | | | | | M |
| Hiring manager | S | | | M | | S | S | | | M |

---

## 14. Score sheet template

Copy this into your notes (or ask the LLM grader to fill it in).

```markdown
## Score sheet
Round: <type>   Level targeted: <new grad | mid | senior>   Date: <yyyy-mm-dd>   Duration: <min>

| Dimension | Score (1–4) | Evidence (quote / timestamp / line) |
|---|---|---|
| Problem solving | | |
| Code quality | | |
| Testing and verification | | |
| Communication | | |
| <round-specific dimension> | | |

Must-have dimensions for this round: <list>
Round outcome: Hire / Lean hire / No hire  (rule: rubrics.md section 1)
Red flags: none / <describe>
Top 3 things to fix, each with a drill:
1.
2.
3.
```

---

## 15. Calibrating an LLM or a friend as grader

1. **Give them this file.** Paste the relevant sections, not just "score me 1–10".
2. **Demand evidence.** Reject any score without a quote or timestamp.
3. **Grade twice.** Run the grading prompt in two fresh chats; if scores differ by more than one point on any dimension, re-read the transcript yourself for that dimension.
4. **Anchor with examples.** Grade one deliberately weak answer and one strong answer first; if the grader gives both a 3, it is not discriminating and its scores are noise.
5. **Watch for verbosity bias.** Graders, human and LLM, tend to reward longer answers. Ask: "Would this score change if the answer were half as long with the same content?"

_Last reviewed: 2026-10_
