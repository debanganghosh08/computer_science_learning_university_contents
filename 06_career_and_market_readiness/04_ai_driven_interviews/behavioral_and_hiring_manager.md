# Behavioural and hiring-manager interviews

| Covers | Levels | Practise with | Score with |
|---|---|---|---|
| STAR and CARL, a story bank, 30 questions with strong-answer outlines, the hiring-manager round, questions to ask, rejection and feedback | Intern/new grad to senior | [Behavioural brief 4.11](how_to_run_a_mock_with_any_llm.md#411-behavioural-45-minutes) and [hiring-manager brief 4.12](how_to_run_a_mock_with_any_llm.md#412-hiring-manager-45-minutes) | [Rubric section 11](rubrics.md#11-behavioural-and-hiring-manager-rounds) |

Behavioural rounds decide more offers than candidates expect. A strong technical loop with a weak behavioural round often ends in "no hire" or a lower level, because interviewers are predicting how you will behave on a bad day: when a deploy breaks, a colleague disagrees, or a deadline slips. Some companies publish the competencies they hire for; Amazon's [Leadership Principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles) are a well-known example. Read the published values of every company you interview with, then map your stories to them.

---

## 1. What these rounds measure

| Dimension | The question behind it |
|---|---|
| Ownership | Do you take responsibility for outcomes, not just tasks? |
| Impact and scope | Is the size of what you did right for the level? |
| Collaboration and conflict | Can you disagree well and still deliver together? |
| Learning and self-awareness | Do you see your mistakes and change? |
| Judgement with AI and data | Do you know when to trust a tool, a number or yourself? |
| Integrity | Is your story true, consistent and fair to others? |

Interviewers test these with **follow-up questions**, not with your first answer. A rehearsed two-minute story is the entry ticket; what you say in the next five minutes decides the score.

---

## 2. Two answer structures

**STAR**: Situation, Task, Action, Result. The default in most interviews.

**CARL**: Context, Action, Result, Learning. Better for failure and growth questions, because it ends with what changed in you.

| Part | Share of a 2–3 minute answer | What goes in it |
|---|---|---|
| Situation / Context | ~15% | Where, when, who, why it mattered. One or two sentences |
| Task | ~10% | Your responsibility specifically |
| Action | ~50% | What **you** did, in order, with the reasoning behind each choice |
| Result | ~15% | What happened, with a number where possible, including what did not go well |
| Learning (CARL) | ~10% | What you now do differently, with evidence that you did it again |

**The same story in both forms.**

> *STAR.* **Situation:** In my final-year project, our team of four built a canteen pre-ordering app used by about 300 students in a pilot. **Task:** I owned the backend and the deployment. **Action:** Two days before the pilot, load testing with 200 simulated users showed checkout timing out. I profiled the endpoint and found each order made 14 separate database queries for menu items. I replaced them with one query using an `IN` list, added an index on `menu_item(canteen_id, available)`, and wrote a regression test that fails if checkout issues more than three queries. **Result:** p95 checkout time fell from 4.1 seconds to 280 ms; the pilot ran a week with no timeouts.
>
> *CARL.* **Context:** same. **Action:** same. **Result:** same. **Learning:** I had only tested with five users. I now add a load test with realistic concurrency before any demo, and I did that in my internship, where it caught a connection-pool limit before release.

Note what makes it strong: one person's actions, a cause found with evidence, a number before and after, and a habit that changed.

---

## 3. Build a story bank

Write **8 to 10 stories** once, then reuse them. Each story should be able to answer several questions.

**Where stories come from.** Internships, course and capstone projects, open-source contributions, hackathons, college clubs and fests, part-time jobs, family businesses, teaching or tutoring, on-call or support work. For new graduates, interviewers expect student-scale stories; what they look for is the same behaviour at a smaller scope.

**Format for each story (bullets, not a script):**

```text
Title:            Checkout timeouts before the canteen pilot
When / where:     Final year, team of 4, 300-student pilot
My role:          Backend owner
Problem:          Checkout p95 > 4 s under 200 simulated users
What I did:       1) profiled  2) removed N+1 queries  3) index  4) regression test on query count
Result:           p95 280 ms; one-week pilot with no timeouts
What went wrong:  I tested with only 5 users at first
Learning:         Load test before every demo (did it again in internship: found pool limit)
Fits questions:   hardest bug, ownership, deadline pressure, quality vs speed, learning
```

**Coverage matrix.** Make sure every column has at least two stories:

| Story | Ownership | Conflict | Failure | Ambiguity | Influence | Customer | AI judgement |
|---|---|---|---|---|---|---|---|
| Checkout timeouts | ✓ | | ✓ | | | ✓ | |
| (your story 2) | | | | | | | |

**Two versions of each story.** A 30-second version (for recruiter screens and AI video interviews) and a 3-minute version with details ready for follow-ups.

---

## 4. Handling follow-ups

| Follow-up | What it tests | How to answer |
|---|---|---|
| "What did *you* do?" | Whether "we" hides a passenger | Name your actions; credit others specifically |
| "Why did you choose that?" | Reasoning, alternatives | Name the option you rejected and why |
| "What would the other person say?" | Fairness, self-awareness | Give their view honestly, including where they were right |
| "What would you do differently?" | Learning | A concrete change, not "communicate more" |
| "How did you measure that?" | Truthfulness of the result | Say how the number was obtained, or say it was an estimate |
| "What happened next?" | Follow-through | What happened after launch or after the conflict |

**Never embellish.** Interviewers compare stories across rounds, and inconsistency is a red flag that outweighs a modest result. "It was a small project, but here is what I learned" is a strong answer.

---

## 5. Thirty behavioural questions with strong-answer outlines

Level notes: **NG** = intern/new grad, **Mid**, **Sr**. The same question is asked at all levels; the expected scope grows.

### Ownership and delivery

**1. Tell me about a project you owned end to end.**
- *Tests:* ownership beyond coding; scope for level.
- *Strong outline:* why the project existed; your decisions from design to launch to after-launch; one hard trade-off; a measured outcome; what you would change. Sr: include stakeholders, sequencing and how you de-risked delivery.
- *Red flags:* only describes tasks assigned to you; no outcome; no "after launch".

**2. Tell me about a time you missed, or nearly missed, a deadline.**
- *Tests:* early communication, scope negotiation.
- *Strong outline:* when you saw the risk (early, with evidence); who you told and what options you gave (cut scope, add help, move date); what you shipped; how you plan differently now.
- *Red flags:* surprise at the last minute; blaming others; heroics (all-nighters) as the only tool.

**3. Tell me about a time you fixed something that was not your job.**
- *Tests:* ownership, judgement about stepping in.
- *Strong outline:* the problem and its cost to users or the team; why you acted rather than escalated (or how you did both); how you coordinated with the actual owner; lasting fix.
- *Red flags:* overriding owners without telling them; changes in production without review.

**4. What is the hardest technical problem you have solved?**
- *Tests:* depth, debugging method, honesty about difficulty.
- *Strong outline:* why it was hard (non-obvious cause, intermittent, cross-system); the hypotheses you ruled out with evidence; the cause; the fix and how you verified it; what you added to prevent recurrence. Expect deep technical follow-ups.
- *Red flags:* a problem solved by an AI tool that you cannot explain; no verification.

**5. Tell me about delivering with incomplete information or a very tight timeline.**
- *Tests:* bias to action with risk control.
- *Strong outline:* the minimum you needed to know and how you got it fast; reversible vs irreversible decisions; what you deliberately did not build; how you signalled uncertainty; outcome and follow-up work.
- *Red flags:* waiting for perfect information; or shipping without any safety net.

### Conflict and collaboration

**6. Tell me about a time you disagreed with a teammate or manager on a technical decision.**
- *Tests:* disagree-and-commit, use of evidence.
- *Strong outline:* both positions stated fairly; how you gathered evidence (benchmark, prototype, data); how the decision was made; whether you were right; how you supported the final decision either way.
- *Red flags:* "I was right and they were wrong"; escalating first; never disagreeing.

**7. Tell me about working with a difficult person or stakeholder.**
- *Tests:* empathy, professionalism.
- *Strong outline:* what made it difficult (incentives, pressure, communication style), not their character; what you did to understand their goals; the change in approach; the outcome for the work and the relationship.
- *Red flags:* character attacks; no attempt to understand the other side.

**8. Tell me about critical feedback you received.**
- *Tests:* coachability.
- *Strong outline:* the exact feedback; your first reaction (honestly); what you changed; evidence the change stuck (later feedback, a result).
- *Red flags:* trivial feedback; feedback you dismissed.

**9. Tell me about giving difficult feedback to a peer.**
- *Tests:* candour with care.
- *Strong outline:* the behaviour and its impact (specific); how you prepared; private, timely delivery; their response; what changed.
- *Red flags:* went to the manager first without talking to the person; vague feedback.

**10. Tell me about helping a teammate succeed.**
- *Tests:* team orientation, multiplier behaviour.
- *Strong outline:* what they were stuck on; how you helped them learn (pairing, a document, a review) rather than doing it for them; their result. Sr: show a repeatable mechanism (onboarding guide, review checklist).
- *Red flags:* "I did it for them" as the whole story.

### Failure and learning

**11. What is the biggest mistake you have made at work or in a project?**
- *Tests:* honesty, accountability, learning.
- *Strong outline:* a real mistake with real cost; your part in it, stated plainly; how you contained it; what you changed in your process; evidence the change worked.
- *Red flags:* a disguised strength; blaming tools or people; a mistake with no consequence.

**12. Tell me about a project that failed.**
- *Tests:* judgement about when to stop; learning.
- *Strong outline:* what success meant; the early signals of failure; whether you stopped or pivoted, and when; what you salvaged; what you now check at the start of projects.
- *Red flags:* no signals noticed; sunk-cost reasoning presented as persistence.

**13. Tell me about learning something quickly to get a job done.**
- *Tests:* learning method, including use of AI.
- *Strong outline:* what you had to learn and the deadline; your method (official documentation, a small prototype, an expert, AI explanations checked against sources); how you verified your understanding; result.
- *Red flags:* "I asked an AI and it worked" with no verification.

**14. Tell me about a decision you would make differently now.**
- *Tests:* reflective judgement.
- *Strong outline:* the decision and the information you had; why it was reasonable then; what you know now; the principle you extracted.
- *Red flags:* hindsight blame; nothing learned.

### Ambiguity and judgement

**15. Tell me about a time requirements were unclear.**
- *Tests:* turning ambiguity into a plan.
- *Strong outline:* the questions you asked and of whom; how you wrote down assumptions and got them confirmed; a prototype or small first release to learn; how requirements evolved.
- *Red flags:* built the wrong thing and blamed the requester.

**16. How did you prioritise between competing tasks?**
- *Tests:* prioritisation framework, communication.
- *Strong outline:* the competing items and their impact and urgency; who decided and on what basis; what you dropped and how you told people; outcome.
- *Red flags:* "I worked harder to do everything".

**17. Tell me about a trade-off between speed and quality.**
- *Tests:* risk-based judgement.
- *Strong outline:* what was at stake on each side; the guardrails you kept (tests on the risky path, feature flag, monitoring, rollback plan); the debt you recorded and when you paid it.
- *Red flags:* quality is always sacrificed; or speed is never acceptable.

**18. Tell me about a time you said no to a request.**
- *Tests:* backbone with respect.
- *Strong outline:* the request and why it was a problem (risk, cost, ethics, priorities); how you said no with an alternative; the outcome and relationship afterwards.
- *Red flags:* refusing without alternatives; never having said no.

### Influence and leadership

**19. Tell me about convincing others to adopt an idea without authority.**
- *Tests:* influence through evidence.
- *Strong outline:* the idea and the resistance; a small proof (prototype, data, pilot); addressing the concerns of each group; adoption measured. Sr: cross-team adoption.
- *Red flags:* "I told them it was best practice".

**20. Tell me about mentoring someone.**
- *Tests:* growing others.
- *Strong outline:* who, what they needed, your approach (goals, regular check-ins, stretch tasks), their progress with evidence, what you learned about mentoring.
- *Red flags:* mentoring as answering questions only.

**21. Tell me about leading a team or initiative.** (NG: a club, hackathon or project team.)
- *Tests:* setting direction, delegation, accountability.
- *Strong outline:* goal and constraints; how you split work by strengths; how you tracked progress and handled a slipping member; outcome; what you would do differently as a leader.
- *Red flags:* doing everything yourself; no handling of problems.

**22. Tell me about improving a process for your team.**
- *Tests:* systems thinking, initiative.
- *Strong outline:* the pain, measured (time lost, failure rate); the change (automation, checklist, template, CI step); adoption; before and after numbers.
- *Red flags:* a process change nobody adopted, presented as success.

### Customers and quality

**23. Tell me about going out of your way for a user or customer.**
- *Tests:* user focus.
- *Strong outline:* how you learned about the user's problem; what you did that was not required; the result for the user; whether it changed the product.
- *Red flags:* customer focus that ignored cost or other users.

**24. Tell me about a problem you found in production.**
- *Tests:* incident behaviour.
- *Strong outline:* detection; impact assessment; mitigation first (rollback, flag); communication; root cause; the follow-up actions and whether they were done; blameless framing.
- *Red flags:* hiding it; fixing silently in production; blaming a person.

**25. Tell me about being asked to do something you thought was wrong.** (Shipping with a known serious issue, misusing data, misleading a customer.)
- *Tests:* integrity under pressure.
- *Strong outline:* the request and why it was wrong (risk, law, ethics); how you raised it, with facts and an alternative; escalation path if needed; outcome.
- *Red flags:* went along silently; or a self-righteous story with no attempt to solve the underlying need.

### AI-era judgement

**26. How do you use AI tools in your work? Walk me through a recent example.**
- *Tests:* mature, specific use.
- *Strong outline:* a concrete task; what you delegated and what you kept; the context you gave; how you verified (tests, docs, review); a time you rejected output; your rules about confidential data and company policy.
- *Red flags:* "I use it for everything"; or "I never use it" said as a virtue without reason.

**27. Tell me about a time AI output misled you.**
- *Tests:* verification habits.
- *Strong outline:* the task; the plausible-but-wrong output (a non-existent API, a subtle logic error, an outdated configuration, an invented citation); how you caught it, or the cost if you caught it late; the habit you now follow (tests first, check official docs, smaller diffs).
- *Red flags:* has never noticed an AI error, which suggests no checking.

**28. What do you not delegate to AI, and why?**
- *Tests:* principled judgement.
- *Strong outline:* categories, with reasons: security-sensitive code and secrets; final decisions on design trade-offs; anything you cannot verify; confidential or personal data; communication where accountability matters (incident updates, performance feedback). Mention when you write small code yourself because it is faster.
- *Red flags:* no boundaries.

**29. A teammate keeps merging AI-generated code that causes incidents. What do you do?**
- *Tests:* collaboration, process thinking.
- *Strong outline:* talk to them first, privately, with specific examples; understand pressure they are under; propose team-level guardrails (review checklist for AI-generated changes, tests required on risky paths, smaller pull requests); raise with the lead if the pattern continues; focus on the system, not blame.
- *Red flags:* public blame; or ignoring it.

**30. How do you keep your fundamentals strong when AI can do the task?**
- *Tests:* long-term learning discipline.
- *Strong outline:* deliberate AI-off practice (solving or debugging by hand), reading code and docs deeply, explaining concepts to others, a specific recent example of something you learned to the level of being able to teach it.
- *Red flags:* no plan; or dismisses fundamentals.

---

## 6. The hiring-manager round

The hiring manager (HM) is the person you would report to. The round blends behavioural questions, a project deep dive, motivation and team fit, and often decides your level.

**What HMs are deciding.**

1. Can this person do the work on my team in the next six months?
2. At what level: how much scope can I give them?
3. Will they make the team better: communication, ownership, learning?
4. Do they actually want this job, or any job?

**Prepare a one-page brief for your best project.** The HM will go deep on one project. Have these ready:

```text
Project:           what it does, for whom, why it mattered
Architecture:      components, data stores, external services (draw in under 2 minutes)
My decisions:      3 decisions I made, the alternatives, and why
Hardest problem:   symptoms, cause, fix, verification
Numbers:           users, latency, cost, error rate, time saved (with how measured)
What broke:        an incident or bug and what I changed after
If I rebuilt it:   2 changes and why
AI use:            what tools did, what I verified, what I wrote myself
```

**"Why this company?"** Specific beats flattering: a product you used and what you would improve, an engineering blog post you read and a question it raised, a problem in their domain you have worked on.

**Scenario questions HMs like.** "Your product manager wants a feature in two weeks you estimate at six." (Strong: break it down, offer a smaller first version with a date, state risks, agree on what is cut.) "You join and find no tests on the payment path." (Strong: add characterisation tests around the riskiest flows before changing anything, then improve incrementally.) "A teammate's AI-generated changes keep failing review." (See question 29.)

**Level conversations.** If asked what level you are targeting, describe the scope you have handled with evidence, and ask how the team defines the levels. Do not inflate; down-levelling after a mismatch is common and painful.

**Compensation.** Usually handled by the recruiter. Know your number from public data (see the [market map](../01_market_map/README.md#6-india)), ask for the structure in writing (in India: fixed pay, variable pay, joining bonus, stock or ESOPs, notice-period buy-out where offered), and avoid naming a number before you know the level.

---

## 7. Questions to ask your interviewers

Ask two or three per round. Good questions show judgement and get you information you need.

**To engineers (peers):**
- What did you ship last month, and how did it get from idea to production?
- What does code review look like here? How are AI-generated changes reviewed?
- What is on-call like: how many pages a week, and what happens after an incident?
- What slows the team down most?
- What is a decision the team reversed recently, and why?

**To the hiring manager:**
- What would success look like in my first 3, 6 and 12 months?
- What is the team's biggest challenge this year?
- How do you give feedback, and how often?
- Why is this role open?
- How are levels and promotions decided?
- How is the team's work changing because of AI tools, and what is the team's policy on them?

**To the recruiter:**
- What are the rounds, how long is each, and what is the AI and tools policy for each?
- What is the expected timeline to a decision?
- What level is this role, and how is it determined?
- What is the compensation structure, and what is negotiable?

**To senior leaders (skip-level or director rounds):**
- What would make this team's work matter more next year than this year?
- What is the biggest risk to the product or the business?
- How do you decide what to build versus buy, including AI capabilities?

**Avoid:** questions answered on the first page of the company website; questions only about leave and perks in technical rounds (ask the recruiter instead); questions that criticise the interviewer.

---

## 8. Rejection and feedback

**Expect little detailed feedback.** Many employers give only a decision, and often a cool-down period before you can reapply (commonly six to twelve months; it varies by company and role, so ask the recruiter). That is a common policy, not a judgement on you.

**Ask once, politely, within two days.**

> Thank you for the interviews and for letting me know. If you are able to share any feedback on the areas I should strengthen, I would value it. I would like to reapply in future; could you tell me when I would be eligible?

**Run your own post-mortem the same day.** Memory fades quickly.

```text
Company / role / level:
Rounds (type, minutes, AI policy):
Per round: what was asked | what I did well | where I struggled | rubric self-score
The single round that most likely decided it:
Root cause (knowledge gap / practice gap / nerves / communication / misread level):
Drills for the next 2 weeks:
Reapply date:
```

**Track your funnel, not single outcomes.** Applications → OAs → technical rounds → final rounds → offers. If you fail mostly at the OA, practise timed problems; if mostly in final rounds, practise system design and behavioural; if at résumé screening, fix the résumé and target better-matched roles.

**Keep relationships.** Thank your interviewers or recruiter briefly. Recruiters move between companies and remember candidates who were gracious.

**Offers and integrity.** Accepting an offer and then backing out (reneging) can harm the company and your reputation; campus placement programmes in India often have rules about this. Know the rules before you accept.

**Look after yourself.** Rejection rates in tech hiring are high even for strong candidates. Plan rest days, keep a list of what you have improved, and talk to peers going through the same loops.

---

## Sources

Checked October 2026.

1. Amazon. *Leadership Principles*. https://www.amazon.jobs/content/en/our-workplace/leadership-principles
2. This section's [README](README.md) for company AI policies and their sources.
3. This repository's [market map](../01_market_map/README.md) for pay data.

_Last reviewed: 2026-10_
