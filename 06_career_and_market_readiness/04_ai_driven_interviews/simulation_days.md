# Simulation days: six full mock interview loops

| Days | Each day takes | You need | Score with |
|---|---|---|---|
| New-grad SWE · Backend SDE-2 · ML engineer · Data analyst · Cloud/SRE · AI engineer or FDE | 4–6 hours including breaks and debrief | The [mock kit](how_to_run_a_mock_with_any_llm.md), a timer, a recorder, your editor | [Rubrics](rubrics.md) |

A single mock tests one skill. A full day tests the thing real loops test: whether you stay sharp in round four after a bad round two. Run one simulation day in week 5 of the [six-week plan](README.md#12-how-to-prepare-a-six-week-plan) and another in week 6.

**How every round works.**

1. Open a **new chat** for each round.
2. Paste the **operating rules** ([kit section 3](how_to_run_a_mock_with_any_llm.md#3-step-1-the-operating-rules-paste-first-every-time)).
3. Paste the **brief** named in the round (from the kit, or the full text given here), with placeholders filled, plus the `QUESTION:` line given.
4. Record, time with a real timer, type `END INTERVIEW` at the end.
5. Grade in a fresh chat with the [grading prompt](how_to_run_a_mock_with_any_llm.md#5-step-3-the-grading-prompt-fresh-chat) and the rubric dimensions listed. Save each score sheet.
6. At the end of the day, run the **hiring-committee debrief** (section 7).

Do not read a round's question before the round starts. Take the breaks; they are part of the simulation.

---

## 1. Day 1: new-grad software engineer at a product company (India)

**Target:** SDE-1 / Software Engineer I, intern or new grad (L2). **Pattern:** online assessment, two coding rounds (one AI-assisted), machine coding, hiring manager.

| Time | Round | Minutes | Brief | Must-have dimensions |
|---|---|---|---|---|
| 09:30 | Online assessment (self-run) | 90 | Text below | Problem solving, code quality |
| 11:15 | Coding (AI-off) | 45 | Kit 4.1 | Problem solving, code quality, communication |
| 12:00 | Lunch | 60 | | |
| 13:00 | AI-assisted coding | 60 | Kit 4.2 | AI collaboration, problem solving, code quality, testing |
| 14:15 | Break | 15 | | |
| 14:30 | Machine coding (backend variant) | 90 | Kit 4.10, backend variant | Problem solving, code quality |
| 16:15 | Hiring manager | 45 | Kit 4.12 | Behavioural 11.1, 11.3, 11.4, 11.6; communication |
| 17:15 | Debrief | 30 | Section 7 | |

**09:30 Online assessment.** In a fresh chat, paste only this (no operating rules needed):

```text
Generate a 90-minute online coding assessment for a new-graduate software engineer at an Indian
product company. Three problems: (1) easy, hashing or two pointers; (2) medium, graph BFS/DFS or
heap; (3) medium-hard, dynamic programming or binary search on the answer. For each give: a
realistic story, precise input/output format, constraints (n up to 10^5 where sensible), two
sample tests with outputs, and a list of 8 hidden test DESCRIPTIONS (not answers) covering edge
cases. Do not give solutions or hints. After I paste my code later, you will grade it against the
hidden test descriptions by reasoning, and tell me which ones you believe fail and why.
```

Solve in your own editor with AI autocomplete off. Run the samples and write at least five tests of your own. At 11:00 stop, paste your code and ask for grading.

**11:15 Coding (AI-off).** Kit 4.1 with `{LEVEL}` = new grad, `{ROLE}` = software engineer, `{COMPANY_TYPE}` = Indian product company, and:

```text
QUESTION: A food-delivery platform records each rider's shifts for a day as [start, end) pairs in
minutes from midnight. Given all shifts for one city, return the maximum number of riders on duty
at the same time, and one time interval when that maximum occurs. Follow-up after a working
solution: shifts now arrive as a live stream and you must answer "riders on duty now" and
"maximum so far" after each new shift.
```

**13:00 AI-assisted coding.** Kit 4.2 with `{LANGUAGE}` = your main language, and add: `Use the leaderboard-with-ties-and-cursor-pagination scenario.` Open your assistant in a second chat ([kit section 6](how_to_run_a_mock_with_any_llm.md#6-practising-ai-on-rounds-with-two-chats)).

**14:30 Machine coding.** Kit 4.10 with the backend variant and:

```text
QUESTION: Build an expense-sharing service (in memory) supporting: add user; add expense paid by
one user and split EQUAL, EXACT amounts, or PERCENT among users; show balances for one user;
show all balances; simplify debts to minimise the number of transactions. Amounts in paise
(integers). Provide a runnable demo. Extension at T+80: add a new split type SHARES (for example
2:1:1) without modifying the existing split classes.
```

**16:15 Hiring manager.** Kit 4.12; paste your anonymised résumé.

**Pass line for the day:** Hire or Lean hire in at least four of five rounds, no Strong no hire in a must-have, and the OA solving at least problems 1 and 2 fully.

---

## 2. Day 2: backend engineer, SDE-2 (mid-level)

**Target:** L3, 2–5 years of experience. **Pattern:** coding, low-level design, system design, database and debugging deep dive, AI code review, hiring manager.

| Time | Round | Minutes | Brief | Must-have dimensions |
|---|---|---|---|---|
| 09:30 | Coding (AI-off) | 45 | Kit 4.1 | Problem solving, code quality, communication |
| 10:30 | Low-level design / machine coding | 75 | Kit 4.10 backend variant | Problem solving, code quality |
| 12:00 | Lunch | 60 | | |
| 13:00 | System design | 60 | Kit 4.3 | 7.1, 7.3, 7.4, 7.6, 7.9; communication |
| 14:15 | Database and debugging deep dive | 45 | Text below | Debugging, problem solving, communication |
| 15:15 | AI code review | 25 | Kit 4.2 variant | Code quality, testing, AI collaboration |
| 15:45 | Break | 15 | | |
| 16:00 | Hiring manager | 45 | Kit 4.12 | Behavioural 11.1–11.6; communication |
| 17:00 | Debrief | 30 | Section 7 | |

**09:30 Coding.** Kit 4.1, `{LEVEL}` = mid-level, and:

```text
QUESTION: Implement allow(user_id, timestamp_ms) -> bool for an API that permits at most N
requests per user in any sliding window of W milliseconds. Calls arrive in non-decreasing
timestamp order. Then: (a) make memory per user O(1) with an approximation and state its error;
(b) explain what changes if 8 application servers share the limit.
```

**10:30 Low-level design.** Kit 4.10 backend variant, 75 minutes, and:

```text
QUESTION: Build an in-memory key-value store with: set(key, value, ttl_seconds optional),
get(key), delete(key), and transactions begin/commit/rollback that can be nested. Expired keys
must never be returned. Provide a demo and unit tests for nested rollback and expiry. Extension:
add a "watch(key)" so that commit fails if a watched key changed since begin.
```

**13:00 System design.** Kit 4.3, `{LEVEL}` = mid-level, and:

```text
QUESTION: Design a notification service for a consumer app: product teams send push, SMS and
email notifications to users; users set channel preferences and quiet hours; some notifications
are transactional (OTP, payment receipts) and must arrive within seconds; marketing campaigns
can target 50 million users. Include retries, deduplication and provider failover.
```

**14:15 Database and debugging deep dive.** Paste the operating rules, then:

```text
ROUND BRIEF: DATABASE AND DEBUGGING DEEP DIVE
Candidate level: mid-level. Role: backend engineer. Duration: 45 minutes.
Scenario: an orders service on PostgreSQL. The endpoint GET /users/{id}/orders?status=&page= got
slow after a release: p95 went from 80 ms to 2.5 s. You hold the hidden truth: the release added a
filter on status and an ORDER BY created_at DESC with OFFSET pagination; the only index is on
(user_id); a few large merchants' accounts have over 2 million orders; autovacuum has fallen
behind on the orders table. Reveal evidence only when asked: the SQL text, EXPLAIN (ANALYZE,
BUFFERS) output (invent a realistic plan), table sizes, pg_stat_statements rows, deploy diff,
dead tuple counts.
Phases: 0-25 diagnose; 25-35 fix (index design, keyset pagination, vacuum settings) and how to
roll out safely (CREATE INDEX CONCURRENTLY, migration order); 35-45 questions on isolation
levels: ask me to explain a lost update and write skew with this schema, and how I would
prevent each.
Score: debugging (must-have), problem solving (must-have), communication (must-have),
system design 7.5 and 7.6.
Start with the alert text.
```

**15:15 AI code review.** Kit 4.2 variant with `{TASK}` = "a payment-capture endpoint that must be idempotent and must not double-charge when the client retries".

**16:00 Hiring manager.** Kit 4.12.

**Pass line:** Hire in system design and the deep dive (these decide SDE-2 level), no Strong no hire anywhere.

---

## 3. Day 3: machine learning engineer (mid-level)

| Time | Round | Minutes | Brief | Must-have dimensions |
|---|---|---|---|---|
| 09:30 | Coding (Python, AI-off) | 45 | Kit 4.1 | Problem solving, code quality, communication |
| 10:30 | ML fundamentals | 45 | Text below | Problem solving, communication, data reasoning |
| 11:30 | Break | 15 | | |
| 11:45 | ML debugging | 60 | Text below | Debugging, testing, code quality |
| 12:45 | Lunch | 60 | | |
| 13:45 | ML system design | 60 | Kit 4.4 | 7.10, 7.11, 7.13; communication |
| 15:00 | Behavioural | 45 | Kit 4.11 | 11.1, 11.3, 11.4, 11.6; communication |
| 16:00 | Debrief | 30 | Section 7 | |

**09:30 Coding.** Kit 4.1, `{LANGUAGE}` = Python, and:

```text
QUESTION: Given, for each query, a ranked list of returned item IDs and a dict of graded relevance
labels (0-3) for that query, implement precision@k, recall@k and nDCG@k, then the mean over
queries. Handle queries with no relevant items and lists shorter than k. Follow-up: vectorise it
with NumPy for 1 million queries, and explain how ties in model scores affect the metric.
```

**10:30 ML fundamentals.** Operating rules, then:

```text
ROUND BRIEF: ML FUNDAMENTALS
Candidate level: mid-level. Role: ML engineer. Duration: 45 minutes.
Ask these one at a time, with 1-2 follow-ups each, moving on after about 5 minutes:
1. Why does L2 regularisation reduce variance? What does it do to the weights geometrically?
2. Your classifier has 99% accuracy on a dataset with 1% positives. What do you report instead,
   and how do you choose the decision threshold?
3. Explain data leakage with two realistic examples and how you would detect each.
4. When would gradient-boosted trees beat a neural network on tabular data, and why?
5. What is calibration? How do you measure it and fix it?
6. Training loss falls but validation loss rises after epoch 5. List causes and actions.
7. How would you detect and respond to feature drift in production?
8. Explain the bias-variance trade-off using k in k-nearest neighbours.
Score: problem solving (must-have), communication (must-have), data reasoning (must-have).
```

**11:45 ML debugging.** Operating rules, then:

```text
ROUND BRIEF: ML DEBUGGING
Candidate level: mid-level. Duration: 60 minutes.
Write a PyTorch training and evaluation script (about 80 lines) for binary classification on
tabular data. Plant exactly four bugs: (1) feature standardisation statistics computed on the full
dataset before the train/validation split; (2) model.eval() and torch.no_grad() missing during
validation while the model uses dropout; (3) a sigmoid applied to outputs that are then passed to
BCEWithLogitsLoss; (4) the validation metric averaged per batch instead of over all examples, with
uneven final batch size. Present the script and these symptoms: "validation AUC is 0.97 offline
but 0.71 in the first week of production; validation numbers fluctuate between runs."
I must find the bugs, explain how each affects the symptoms, and propose tests that would have
caught them. Do not reveal the bugs. Score: debugging (must-have), testing and verification
(must-have), code quality (must-have), communication. In feedback list all four bugs and
which ones I found.
```

**13:45 ML system design.** Kit 4.4 with:

```text
QUESTION: Design delivery-time (ETA) prediction for a food-delivery app, shown to users before
they order and updated during delivery. Under-promising loses orders; over-promising causes
complaints and refunds.
```

**15:00 Behavioural.** Kit 4.11, adding: "Include one question about a model I shipped and one about a model I decided not to ship."

**Pass line:** Hire in ML system design and ML debugging; at most one Lean hire elsewhere.

---

## 4. Day 4: data analyst (new grad or mid-level)

| Time | Round | Minutes | Brief | Must-have dimensions |
|---|---|---|---|---|
| 09:00 | Take-home released (self-run) | 180 | Text below | |
| 12:00 | Lunch | 45 | | |
| 12:45 | Live SQL | 45 | Kit 4.7 | Data reasoning, problem solving |
| 13:45 | Statistics and experiments | 45 | Text below | Data reasoning, communication |
| 14:45 | Break | 15 | | |
| 15:00 | Business case | 45 | Kit 4.6 | Data reasoning, problem solving, communication |
| 16:00 | Take-home presentation | 30 | Text below | Communication, data reasoning |
| 16:45 | Behavioural | 30 | Kit 4.11 (shortened) | 11.1, 11.4, 11.6 |
| 17:30 | Debrief | 30 | Section 7 | |

**09:00 Take-home.** In a fresh chat:

```text
Write a Python script (standard library plus pandas and NumPy only) that generates a synthetic
CSV of 20,000 orders for a quick-commerce grocery app over 8 weeks, with columns: order_id,
user_id, order_ts, city, platform, is_new_user, basket_value_inr, discount_inr, delivery_minutes,
cancelled. Plant three patterns I must discover without being told: a city where delivery time
worsened in week 6; a platform where cancellations rose after an app release date; and discount
spending that rises without a matching rise in orders from new users. Add realistic noise,
duplicates (0.5% of rows) and some missing delivery times. Print nothing about the patterns.
```

Run the script, analyse with SQL or Python (AI assistance allowed for this take-home, but write down what you used it for), and prepare five slides or a one-page memo: question, data checks, three findings with charts, recommendation, limitations.

**12:45 Live SQL.** Kit 4.7 with `{DIALECT}` = PostgreSQL. AI-off.

**13:45 Statistics and experiments.** Operating rules, then:

```text
ROUND BRIEF: STATISTICS AND EXPERIMENTS
Candidate level: {LEVEL}. Role: data analyst. Duration: 45 minutes.
Present this result: "New checkout page A/B test, 14 days. Control: 50,210 users, 4,519 orders.
Treatment: 49,120 users, 4,665 orders. Product wants to ship." Then ask, one at a time:
1. Is the difference significant? Walk through the test and the confidence interval.
2. The split was planned 50/50. Is the observed split a concern? How would you check?
3. The PM looked at results daily and wanted to stop on day 4 when p < 0.05. What is the problem?
4. Conversion is up but average order value is down 3%. How do you decide?
5. What sample size would you have needed to detect a 0.3 percentage-point lift with 80% power?
   (Reasoning and formula, approximate numbers are fine.)
6. Name two reasons this result might not hold after launch.
Score: data reasoning (must-have), communication (must-have), problem solving.
```

**15:00 Business case.** Kit 4.6 with `QUESTION: Daily orders fell 8% yesterday in a quick-commerce app.`

**16:00 Take-home presentation.** Operating rules, then: "ROUND BRIEF: You are a VP of operations with little statistics background. I will present a take-home analysis in 10 minutes, then you ask 20 minutes of questions: challenge one finding, ask what I would do with one more week, ask how confident I am, and ask what decision you should make on Monday. Score communication (must-have) and data reasoning (must-have)." Paste your memo or slide text when asked.

**Pass line:** Hire in SQL and case; the take-home finds at least two of the three planted patterns and reports data-quality issues.

---

## 5. Day 5: cloud engineer / site reliability engineer (mid-level)

| Time | Round | Minutes | Brief | Must-have dimensions |
|---|---|---|---|---|
| 09:30 | Linux and networking troubleshooting | 45 | Text below | Debugging, communication |
| 10:30 | Scripting (AI-off) | 45 | Kit 4.1 | Problem solving, code quality |
| 11:30 | Break | 15 | | |
| 11:45 | Incident simulation | 60 | Kit 4.9 | Debugging, communication |
| 12:45 | Lunch | 60 | | |
| 13:45 | Reliability system design | 60 | Kit 4.3 | 7.1, 7.4, 7.6, 7.8, 7.9; communication |
| 15:00 | Behavioural (on-call focus) | 45 | Kit 4.11 | 11.1, 11.3, 11.4, 11.6 |
| 16:00 | Debrief | 30 | Section 7 | |

**09:30 Troubleshooting.** Operating rules, then:

```text
ROUND BRIEF: LINUX AND NETWORKING TROUBLESHOOTING
Candidate level: mid-level. Role: SRE. Duration: 45 minutes.
Scenario 1 (25 min): "Users say the internal wiki is slow since this morning." Hidden truth: the
VM's disk is 100% full because log rotation failed, so the app blocks on writes; there is also
high iowait. Respond to my commands (uptime, top, vmstat, iostat, df -h, du, journalctl, ss,
curl -w timings, dig) with realistic synthetic output.
Scenario 2 (20 min): "Pods in one namespace intermittently fail to resolve external hostnames."
Hidden truth: that namespace's workloads make many external calls; with the default ndots:5 in
the pods' resolv.conf, each external lookup first tries several cluster search domains, multiplying
query volume; the cluster DNS pods hit their low CPU limit and are throttled at peak, so some
queries time out. Reveal resolv.conf, DNS pod metrics, throttling counters and query logs on request.
Score: debugging (must-have), communication (must-have), problem solving.
```

**10:30 Scripting.** Kit 4.1 with `{LANGUAGE}` = Python, Go or Bash, and:

```text
QUESTION: Read an Nginx-style access log from stdin (format given by you, include malformed
lines). Output, per endpoint path (with numeric IDs normalised to {id}), per minute: request
count, error rate (5xx), and p95 latency. Then print an alert line when any endpoint's error rate
exceeds 5% for 3 consecutive minutes. Follow-up: the file is 50 GB; what changes?
```

**11:45 Incident simulation.** Kit 4.9 with `QUESTION: HTTP 502s on checkout after a deploy, 18:05 on a Friday during a sale.`

**13:45 Reliability system design.** Kit 4.3 with:

```text
QUESTION: The checkout service of an e-commerce company must meet a 99.95% monthly availability
SLO. Design its deployment across two regions, the monitoring and alerting (SLIs, SLOs, burn-rate
alerts), the release process (canary, automatic rollback), and the failover procedure. Estimate
the error budget in minutes per month and explain how it changes release decisions.
```

**15:00 Behavioural.** Kit 4.11, adding: "Focus two questions on on-call: an outage I caused or fixed, and how I improved alert quality or on-call load."

**Pass line:** Hire in the incident and troubleshooting rounds; the postmortem names contributing factors without blaming a person.

---

## 6. Day 6: AI engineer or forward-deployed engineer (mid-level)

| Time | Round | Minutes | Brief | Must-have dimensions |
|---|---|---|---|---|
| 09:30 | AI-assisted coding | 60 | Kit 4.2 | AI collaboration, problem solving, code quality, testing |
| 10:45 | LLM / agent system design | 60 | Kit 4.5 | 7.10, 7.13, 7.15; security; communication |
| 11:45 | Lunch | 60 | | |
| 12:45 | Evals and trace debugging | 45 | Text below | Debugging, testing, AI collaboration |
| 13:45 | Customer scenario | 45 | Text below | Communication, problem solving |
| 14:30 | Written design note (self-run) | 30 | Text below | Communication |
| 15:15 | Hiring manager | 45 | Kit 4.12 | 11.1–11.6; communication |
| 16:15 | Debrief | 30 | Section 7 | |

**09:30 AI-assisted coding.** Kit 4.2 with:

```text
QUESTION: Starter project: a small FAQ answering service in {LANGUAGE} with a document loader,
a chunker, an in-memory vector index (stub embeddings are fine), and an answer function that calls
a model client interface (mocked). Planted defects: the chunker drops the last partial chunk;
retrieved chunks are not deduplicated so the same passage appears three times in the prompt.
Feature request: answers must include citations (document ID and section) and must reply
"I don't know" when the best retrieval score is below a threshold. Acceptance criteria: unit tests
with a mocked model for a cited answer, an "I don't know" answer, and a duplicate-passage case.
```

**10:45 LLM / agent system design.** Kit 4.5 with `QUESTION: an agent that files expense reports from emailed receipts into the company's expense system, with manager approval rules and a monthly budget per team.`

**12:45 Evals and trace debugging.** Operating rules, then:

```text
ROUND BRIEF: EVALS AND TRACE DEBUGGING
Candidate level: mid-level. Role: AI engineer. Duration: 45 minutes.
Part 1 (25 min): show five synthetic traces (as JSON-like logs: user message, retrieved chunk IDs
and scores, model calls with prompts truncated, tool calls with arguments and results, final
answer) from a customer-support agent. Two traces are failures with different causes: one where
the retrieved policy document is outdated (index not refreshed after a policy change), one where
the agent called the refund tool with an amount parsed from the wrong field. Ask me to find the
failures, their causes, and the fix for each.
Part 2 (20 min): ask me to design the evaluation suite that would have caught both before
release: datasets, slices, graders (exact match, rubric-based model grading with human
calibration), thresholds, and how evals run on every prompt, model or index change.
Score: debugging (must-have), testing and verification (must-have), AI collaboration,
system design 7.13 and 7.15.
```

**13:45 Customer scenario.** Operating rules, then:

```text
ROUND BRIEF: CUSTOMER SCENARIO (FORWARD-DEPLOYED)
Candidate level: mid-level. Duration: 45 minutes.
You are the head of operations at a mid-sized logistics company (illustrative). Your opening
line: "We want to use AI to cut the time our team spends on delivery exception emails." Hidden
facts, reveal only when asked: about 3,000 emails a day in English and Hindi; exceptions include
address problems, damaged goods and delays; data sits in a ticketing tool and a legacy
warehouse system with a nightly CSV export; legal requires that no customer data leaves India;
the team of 40 is worried about job cuts; budget approval needs a measurable pilot in 6 weeks.
Behave like a real customer: sometimes vague, sometimes impatient, one unrealistic demand
("fully automatic replies from day one").
Phases: 0-20 discovery questions | 20-35 proposed pilot: scope, success metric, data access,
human review, risks | 35-45 handling the unrealistic demand and agreeing next steps.
Score: communication (must-have), problem solving (must-have), system design 7.1, 7.7 and 7.9,
security.
```

**14:30 Written design note.** Write, in 30 minutes, a one-page note to that customer: problem, proposed pilot, what the system will and will not do, data handling, success metric and how it is measured, risks, timeline, decisions needed from them. Then grade it in a fresh chat: "Grade this one-page customer design note for clarity, correctness, honesty about limits, and actionability, as a senior forward-deployed engineer would. Score communication 1–4 with quotes, and list every claim a customer could misread."

**15:15 Hiring manager.** Kit 4.12, adding: "Probe how I handle travel, ambiguity, and a customer who wants something unsafe."

**Pass line:** Hire in AI-assisted coding and the customer scenario (both decide FDE hires); the eval design covers both trace failures.

---

## 7. The hiring-committee debrief (end of every day)

In a fresh chat, paste all your score sheets from the day, then:

```text
You are a hiring committee. Below are score sheets from every round of one candidate's interview
loop for {ROLE} at {LEVEL}. Using these rules:
- Round outcomes are as recorded.
- Hire if most rounds are Hire, no round is Strong no hire on a must-have dimension, and there is
  no integrity red flag.
- Consider whether the evidence supports a lower or higher level than targeted.
Produce: (1) a decision (Hire / No hire) and level; (2) the two rounds that most influenced the
decision and why; (3) whether any score looks inconsistent with its evidence; (4) a two-week
practice plan targeting the weakest two dimensions across rounds, with a daily drill.
Be strict. Do not average away a must-have failure.

SCORE SHEETS:
<paste>
```

Then compare with your own judgement, add the plan to your mistake log, and schedule the next simulation day for two weeks later. Improvement shows as fewer Lean hires on the same dimensions.

_Last reviewed: 2026-10_
