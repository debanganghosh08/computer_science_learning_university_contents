# Case studies and technical writing

| Goal | Time | Level | Back to |
|---|---|---|---|
| Write project case studies and technical posts that show how you think, which interviewers read and which you can talk through for 30 minutes | 4–6 hours per piece | L2 → L4 | [Portfolio hub](README.md) |

## 1. Why write

- **Interviews are built on stories.** "Tell me about a project you are proud of" and "tell me about a hard bug" appear in almost every loop. A written case study is that answer, rehearsed and checked.
- **Writing shows judgement.** Code shows what you did; writing shows why, what you rejected, and what you learned. Judgement is the part AI tools substitute least (see the [market map, section 3](../01_market_map/README.md#3-entry-level-hiring-what-the-data-shows)).
- **It covers work you cannot show.** Internship and employer code is private. A case study written within your confidentiality obligations is the only public evidence of it.
- **Engineering is written.** Design documents, pull-request descriptions, incident reviews and runbooks are daily work. Practising now is practising the job.

## 2. The project case study

### 2.1 Template (600–1,200 words)

```markdown
# <Project>: <the result in one line>

**Role:** what you did (solo / one of three / owned the X part) · **Time:** 6 weeks ·
**Stack:** Go, PostgreSQL, Kafka · **Code:** link · **Demo:** link

## Context
Who needed this and why. One paragraph. Real users, a course, an internship, or your own need.

## Problem and constraints
What made it hard. State constraints as numbers where possible:
"must not double-post under consumer crashes", "p95 < 100 ms", "runs on a 2 GB VM", "budget ₹0".

## Approach
The design, with one diagram. Explain the key mechanism in enough detail that a peer could
rebuild it.

## Alternatives considered
2–3 options you rejected and why. This section is what separates strong case studies.

## Results
Measured outcomes with the method: tool, setup, number of runs. Compare with a baseline.

## What went wrong
One failure or surprise, how you found it, how you fixed it. Be specific.

## What I would do differently
Concrete changes, not "write more tests".

## How AI tools were used
Which parts were AI-assisted, how you verified them, where the tools were wrong.
```

### 2.2 A worked excerpt (illustrative)

> **What went wrong.** The first load test showed 0.3% duplicate postings, which should have been impossible. Tracing one duplicate showed the consumer committing its Kafka offset *before* the database transaction committed; a crash between the two re-delivered the message, and the idempotency check missed it because it ran in a separate transaction. Moving the idempotency insert into the same transaction as the posting, and committing the offset only after it, brought duplicates to zero across 50 forced crashes. The fix took ten lines; finding it took two days and taught me to trace a single message end to end before guessing.

This paragraph gives an interviewer five things to ask about (offsets, transactions, idempotency, tracing, the chaos test), and you can answer all of them.

### 2.3 Writing about confidential work

For internships and jobs:

1. **Read your agreement first.** Confidentiality and IP clauses decide what you can publish. When unsure, ask your manager in writing.
2. **Abstract the domain.** "A logistics company's nightly batch jobs" instead of the client's name.
3. **Use relative numbers** ("failed runs fell from 6 a month to 0") unless absolute numbers are public or approved.
4. **No code, no screenshots of internal tools, no architecture details that reveal security controls.**
5. **Keep a private version** with full detail for your own interview preparation.

## 3. Technical blog posts

### 3.1 Types that work for early-career engineers

| Type | Structure | Example title (illustrative) |
|---|---|---|
| Debugging story | Symptom → hypotheses → evidence → root cause → fix → lesson | "A 0.3% duplicate rate and the offset I committed too early" |
| Implementing a paper | Paper's claim → your implementation → what matched → what did not → why | "Implementing Raft leader election from the paper: what the figure leaves out" |
| Benchmark with method | Question → setup (hardware, versions, data) → results with variance → limits | "PostgreSQL GIN vs trigram index for 12,000 notes: numbers and EXPLAIN plans" |
| Explainer | One concept, one diagram, one runnable example | "Idempotency keys in 15 lines of SQL" |
| Project postmortem | Timeline → impact → contributing factors → what changed (blameless) | "My side project was down for 9 hours: what happened" |
| Today I learned (TIL) | 100–300 words, one fact with a link to the source | "`go test -race` found what my eyes did not" |

### 3.2 Postmortems

The blameless postmortem format used in site reliability engineering focuses on contributing causes and fixes rather than on who made a mistake ([Google SRE book, "Postmortem Culture"](https://sre.google/sre-book/postmortem-culture/)). Writing one for your own project (even a two-hour outage of a hobby site) is good practice for on-call work and a strong interview story.

Minimum sections: summary, impact (who, how long, how measured), timeline with timestamps, root cause and contributing factors, what went well, what went badly, action items with owners.

### 3.3 Read good engineering writing

Read one strong post a week and note how it is structured:

- Discord, [*How Discord Stores Trillions of Messages*](https://discord.com/blog/how-discord-stores-trillions-of-messages) (2023): a migration explained with the problem, the options and the results.
- [Cloudflare blog](https://blog.cloudflare.com/): detailed public incident reports and protocol explainers.
- [Zerodha tech blog](https://zerodha.tech/blog/): an Indian broker's engineering, including running a large trading platform with a small team.
- [Julia Evans](https://jvns.ca/) and [Dan Luu](https://danluu.com/): clear explanations and careful use of evidence.
- [Google SRE books](https://sre.google/books/): the standard reference for incident writing.

## 4. Process

1. **Outline in bullets** before writing prose: the question, the answer, the evidence.
2. **Draft fast**, then cut by a third. Remove throat-clearing introductions.
3. **Make every code sample run.** Put them in the repository and link the exact commit.
4. **Add one diagram.** Mermaid diagrams render in GitHub Markdown; Excalidraw is good for hand-drawn style.
5. **Get one review** from someone who will tell you what is unclear.
6. **Publish** on a site you control (for example, GitHub Pages with Hugo, Jekyll or Astro). If you cross-post to dev.to, Hashnode or Medium, set the canonical URL to your own site so search engines credit the original.
7. **Link it** from the project README and your profile README.

Length guide: case study 600–1,200 words; debugging story 800–1,500; explainer 500–1,000; TIL under 300.

## 5. Writing with AI tools

- **Use AI for:** finding unclear sentences, suggesting a tighter structure, checking that a definition is correct, generating alternative titles, spotting missing steps in a tutorial.
- **Do yourself:** the outline, the claims, the numbers, the story of what went wrong, the conclusions.
- **Verify:** run every code sample; open every link and citation an AI tool suggests, because tools can produce plausible references that do not exist; check every technical claim against documentation.
- **Disclose** significant AI assistance in a short note if your readers would want to know. It costs nothing and builds trust.

A generic, AI-sounding post can hurt more than no post: it suggests you either did not do the work or cannot explain it.

## 6. A sustainable cadence

| Stage | Cadence |
|---|---|
| Year 3 (CAR301) | One case study per finished project; one TIL a month |
| Year 4 | One substantial post a month (flagship project, co-op lessons, a debugging story) |
| Working | One post a quarter; design documents and incident reviews at work count as practice |

Track what matters: which posts interviewers or peers mentioned, and which questions they raised. Views and likes are not the goal.

## 7. Practice

1. Write the "What went wrong" section for your best project in 150 words. Have a friend ask five follow-up questions; add what was missing.
2. Write a blameless postmortem of any failure in a project of yours (a bad deploy, lost data, a missed deadline).
3. Pick one post from section 3.3 and outline it in ten bullets. Then outline your next post in the same shape.

## Sources

All checked October 2026.

1. Google. *Site Reliability Engineering*, chapter "Postmortem Culture: Learning from Failure". https://sre.google/sre-book/postmortem-culture/
2. Discord. *How Discord Stores Trillions of Messages* (2023). https://discord.com/blog/how-discord-stores-trillions-of-messages
3. Zerodha tech blog. https://zerodha.tech/blog/
4. Cloudflare blog. https://blog.cloudflare.com/

_Last reviewed: 2026-10_
