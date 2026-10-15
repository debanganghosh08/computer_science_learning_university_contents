# The applications pipeline

| Goal | Time | Level | Back to |
|---|---|---|---|
| Run the search as a measured pipeline: one tracker, weekly numbers, timely follow-ups and a routine you can keep for months | 2 hours to set up; 8–12 hours a week while searching | L2 → L4 | [Job search hub](README.md) |

## 1. The tracker

Use a spreadsheet (or a plain CSV in a private repository). One row per opportunity, not per company.

```csv
id,company,role,job_link,tier,channel,contact,date_found,date_applied,resume_version,stage,next_action,next_action_date,last_contact,outcome,notes
1,Example Payments,Backend Engineer I,https://...,target,referral,Karan (alum),2026-10-01,2026-10-03,v2026-10-ledger,OA scheduled,Practice graphs + SQL,2026-10-09,2026-10-05,,Referral submitted 3 Oct
2,Example Cloud GCC,SDE-1,https://...,reach,careers page,,2026-10-02,2026-10-02,v2026-10-general,applied,Find engineer on team for advice,2026-10-08,,,
3,Example Startup,Founding engineer,https://...,likely,cold email,Ananya (founder),2026-10-04,,,outreach sent,Follow up,2026-10-11,2026-10-04,,Sent export bug note
```

**Stages** (use exactly these so counts work): `researching`, `outreach sent`, `applied`, `OA scheduled` (online assessment), `OA done`, `phone screen`, `onsite/loop`, `final`, `offer`, `accepted`, `rejected`, `withdrawn`, `ghosted` (no reply 21+ days after last follow-up).

**Channels:** `referral`, `cold email`, `careers page`, `job board`, `campus`, `recruiter inbound`, `hiring challenge`, `OSS programme`.

## 2. Weekly numbers

Add a summary sheet. With the tracker in a sheet named `T` (columns as above: F = channel, K = stage, I = date applied), these formulas work in Google Sheets and Excel:

| Metric | Formula |
|---|---|
| Applications this week | `=COUNTIFS(T!I:I,">="&TODAY()-7)` |
| Applications by channel | `=COUNTIFS(T!F:F,"referral",T!I:I,"<>")` (repeat per channel) |
| Response rate by channel | Rows in that channel that reached `OA scheduled` or later ÷ applications in that channel |
| Interview conversion | Rows at `onsite/loop` or later ÷ rows at `phone screen` or later |
| Offer rate | Rows at `offer` or later ÷ rows at `final` or later |

To make "reached a stage or later" easy, add a numeric `stage_rank` column (researching = 0, outreach sent = 1, applied = 2, OA scheduled = 3, … offer = 8, accepted = 9) and count `stage_rank >= n`. Keep the highest rank reached even after a rejection.

Review these numbers every week. The point is diagnosis (section 6), not judging yourself.

## 3. Follow-ups

| Situation | When | Template |
|---|---|---|
| Applied with no response | 7–10 working days | "Hi <name>, I applied for <role> (ID) on <date>. Since then I <one new piece of evidence, e.g. published the load-test report>. Is there anything else useful I can share?" |
| After any interview | Same day | "Thank you for the conversation about <specific topic>. I enjoyed the <problem> discussion; I thought more about <one point> and would <brief improvement>." (Keep it to 3–4 lines.) |
| Promised timeline passed | 2 working days after | "Hi <recruiter>, checking in on next steps for <role>. I'm still very interested. I also have a timeline elsewhere, so any update would help me plan." (Only mention other timelines if true.) |
| Rejected | Within a week | "Thank you for letting me know. If you have one or two points I could improve for future roles, I'd be grateful. I'd like to apply again in the future." |
| You withdraw | As soon as you decide | "Thank you for your time. I've accepted another offer and am withdrawing from the process. I hope we cross paths again." |

Not every company will give feedback after a rejection; many have policies against it. Ask once, politely, and move on.

## 4. The weekly routine

A routine stops the search from swallowing your whole week or stalling for a month. For about 10 hours a week alongside study or work:

| Day | Time | Task |
|---|---|---|
| Monday | 60 min | Add 5–10 targets; find the right person for each; draft messages |
| Tuesday | 90 min | Coding practice without AI ([02](../02_dsa_for_hiring/)) |
| Wednesday | 60 min | Send referral requests and outreach; 3–5 tailored applications |
| Thursday | 90 min | System design or role-specific practice ([03](../03_system_design/), [04](../04_ai_driven_interviews/)) |
| Friday | 60 min | Follow-ups due this week; update tracker stages |
| Saturday | 2 hours | Project or open-source work that produces new evidence; one mock interview |
| Sunday | 30 min | Weekly review: numbers, what worked, plan for next week |

During active interview weeks, replace project time with interview-specific preparation, but keep the Sunday review.

**Sunday review template.**

```markdown
## Week of 2026-10-12
- Sent: 6 outreach, 3 referral asks, 5 applications
- Responses: 2 replies, 1 OA invite, 1 rejection
- Interviews: 1 phone screen (Example Payments) – debrief below
- What worked: messages mentioning the ledger write-up got 2 of 3 replies
- What didn't: 4 portal-only applications, 0 responses
- Next week: shift 3 portal applications to referral attempts; practise graph problems
```

## 5. Interview logistics

**Before each round:** read the job description again, the company's engineering blog, and your own resume. Ask the recruiter for the format (coding, design, behavioural; AI allowed or not; language; tools; duration) and who the interviewers are.

**Story bank.** Prepare eight stories, each in 2 minutes, mapped to questions you will be asked:

| Story | Shows | Used for |
|---|---|---|
| The duplicate-posting bug | Debugging, persistence | "Hardest bug", "a time you were wrong" |
| Moving cron jobs to a queue (co-op) | Ownership, impact | "Proudest project", "impact" |
| Disagreeing with a reviewer on the API design | Collaboration | "Conflict", "feedback" |
| … | | |

**Debrief after every interview (within an hour):**

```markdown
## Example Payments · phone screen · 2026-10-10
- Questions: (1) design an idempotent refund API (2) graph: detect cycle in dependencies
- What went well: idempotency key discussion; clarified requirements first
- What went badly: took 12 min to see topological sort; forgot to test the empty graph
- Follow-up practice: 5 topological-sort problems; always list edge cases before coding
```

Debriefs turn every interview, including the failed ones, into targeted practice.

## 6. When to change strategy

| Symptom (after 4+ weeks and 30+ applications) | Likely cause | Change |
|---|---|---|
| Almost no responses | Resume does not show fit, or channel is mostly cold portals | Get resume reviewed by someone in the role; shift to referrals and direct outreach |
| Responses but online assessments fail | DSA speed or accuracy | Timed practice without AI, pattern-based ([02](../02_dsa_for_hiring/)) |
| Pass screens, fail onsites | Design depth, communication or behavioural answers | Mock loops with an experienced engineer; story bank |
| Reach finals, no offers | Team-fit questions, references, or comparison with stronger candidates | Ask for feedback; strengthen the flagship project and its write-up |
| Offers below expectations | Target tier or negotiation | Re-check your [market data](../01_market_map/README.md) and [negotiation](offers_and_negotiation.md) |

## 7. Records and privacy

- Keep the tracker private. It contains other people's names and contact details; do not share or publish it.
- Save every job description you apply to (as a PDF or text) in a folder named by the row ID. Postings disappear, and you will need them before interviews.
- Tag the exact resume version sent with each application.

## 8. Practice

1. Set up the tracker and summary sheet; add 20 rows from your target list.
2. Run the weekly routine for three weeks and write three Sunday reviews.
3. Write your eight-story bank and rehearse each story aloud in under two minutes.

_Last reviewed: 2026-10_
