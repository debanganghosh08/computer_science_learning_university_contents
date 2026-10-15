# The first 90 days

| Goal | Time | Level | Back to |
|---|---|---|---|
| Start a job (or the [IND401](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/) co-op) so that by day 90 you have shipped real work, earned trust, and know what "good" means on your team | 2 hours to plan; then daily habits | L3 | [Job search hub](README.md) |

The first three months decide how people see you for much longer. Nobody expects a new engineer to know the codebase. People do notice whether you learn fast, ask good questions, finish what you start and make the people around you more effective.

## 1. Before day one

- Finish paperwork and background verification early; keep copies of everything.
- Read what is public: the product, the engineering blog, open-source repositories, talks by your future teammates.
- Ask your manager: "Is there anything you'd like me to read or set up before I start?"
- Write three personal goals for the first 90 days (section 6).

## 2. Days 1–30: learn how work flows

| Week | Do | Output |
|---|---|---|
| 1 | Set up your machine and get the main service running locally. **Write down every step that was missing or wrong** in the setup docs | A pull request that fixes the onboarding docs; it is often the best first contribution |
| 1–2 | Learn the path of a change: ticket → branch → pull request → review → CI → deploy → monitoring | A one-page diagram of how code reaches production |
| 2 | Ship a small, real change (a bug fix, a test, a log line) through the whole path | First merged pull request |
| 2–3 | Read the last few incident reports or postmortems and the on-call runbooks | A list of the systems that break most and why |
| 3–4 | Meet each teammate and the people your team depends on (15–30 minutes each): what they work on, what is hard, what they wish new people knew | Notes; a "who to ask about what" list |
| 4 | Agree with your manager what success at 30, 60 and 90 days looks like | Written expectations (section 6) |

**Keep a glossary.** Every team has words that mean something specific (a "settlement", a "tenant", a "shard", a "partner"). Write them down with definitions and the code where they live.

## 3. Days 31–60: own something small end to end

- Take one feature or bug from ticket to production on your own, asking for help when blocked.
- Write a short design note (one page) before any non-trivial change, and get it reviewed. It catches misunderstandings while they are cheap.
- Shadow on-call if your team has it, then take shifts with a buddy. Learn the runbooks before you need them.
- Start reviewing teammates' pull requests: read carefully, ask questions, point out missing tests. Reviewing is how you learn a codebase fastest.

## 4. Days 61–90: deliver and improve

- Deliver one piece of work that matters to the team's goals, with a measured result (latency, error rate, time saved, customer issue resolved).
- Propose one improvement backed by data you collected: a flaky test you fixed and how much CI time it saves, an alert that fires too often, a missing dashboard.
- Ask for explicit feedback: "What should I do more of, and what should I change?"
- If you are on probation, ask what confirmation depends on and whether you are on track.

## 5. Habits that build trust

**Ask for help well.** Try on your own for a set time (for example, 30–60 minutes for a setup problem, longer for a design question), then ask with context:

```text
I'm trying to run the payments service locally to test the refund fix.
I ran `make dev`; it fails at the migration step with "relation ledger_entries does not exist".
I checked that Postgres is running and the DB URL in .env points to it.
I expected migrations to create the table. Is there a seed step I'm missing?
```

This shows what you tried, makes the answer fast, and the answer often goes into the docs.

**Say what you will do, then do it.** Small promises kept ("I'll have the draft by Thursday") build more trust than large ones. If you will miss a date, say so early.

**Write things down.** Decisions in the ticket or design doc, not only in chat. Meeting notes with action items.

**Keep a brag document.** A running list of what you shipped, what you learned, problems you solved and help you gave, with links. It makes 1:1s, performance reviews and your resume much easier ([Julia Evans, "Get your work recognized: write a brag document"](https://jvns.ca/blog/brag-documents/)).

**Receive review well.** Thank reviewers, ask when you do not understand, and do not take it personally. Fix the same comment once; do not make reviewers repeat it.

**Use AI tools within the rules.** Follow your employer's policy on which tools are approved and what code or data may be shared with them. Review AI-generated code at least as carefully as a colleague's. Note where the tools fail in your codebase (internal libraries, unusual conventions) and share that with the team.

## 6. The 30-60-90 plan

Write it in week one, agree it with your manager, and review it at each checkpoint.

```markdown
# 30-60-90 plan · Rahul Menon · Ledger team · start 2028-07-01

## Day 30: learning
- Main service and reconciliation job running locally; onboarding doc fixes merged
- 3 small changes merged through the full pipeline
- Read last 6 months of incident reports; can explain the top 3 failure modes
- Met everyone on the team and the 2 partner teams

## Day 60: contributing
- Owned and shipped: idempotent retry for failed settlement callbacks (ticket LED-412)
- Completed 2 shadow on-call shifts; joined rotation with a buddy
- Reviewing 3+ pull requests a week

## Day 90: owning
- Delivered: reconciliation mismatch report automated (target: manual work from 4 h/week to <30 min)
- Proposed one improvement with data (e.g. flaky integration tests)
- Feedback conversation with manager; probation confirmation criteria met

## How I'll know I'm on track
Weekly 1:1 notes; brag document; manager feedback at day 30 and 60
```

**1:1 agenda template.**

```markdown
- What I shipped since last time (links)
- Where I'm blocked or slow
- One question about the system, the team or the business
- Feedback: anything I should do differently?
- Next week's priorities (agree them)
```

## 7. Special situations

**Remote or hybrid teams.** Over-communicate progress in writing (short end-of-day notes in the team channel or ticket), turn on your camera for 1:1s, and ask for a regular pairing session in the first month, because you cannot learn by overhearing.

**Large services firms with initial training.** Many large Indian services firms run structured training for freshers before project allocation, and some people then wait "on the bench" between projects (common practice; length varies). Use that time deliberately: finish the training well, build one portfolio project with the stack you were trained on, and ask the allocation team regularly and specifically for the projects you want.

**A team that is struggling.** If there is no onboarding, unclear priorities or constant firefighting, stay calm: write down what you learn, fix one painful thing, and raise the patterns with your manager with suggestions, not only complaints. Teams where people feel safe to raise problems and admit mistakes tend to be more effective; Google's research on its own teams named this "psychological safety" as the most important factor it found ([Google re:Work](https://rework.withgoogle.com/)).

**Warning signs.** Being asked to do something unsafe or unethical (bypassing security reviews, misusing customer data), no feedback at all by day 60, or repeated changes to what you are told success means. Ask for clarity in writing; if nothing changes, start planning (see [layoffs and setbacks](layoffs_and_setbacks.md#4-performance-improvement-plans)).

## 8. Practice

1. Write a 30-60-90 plan for your IND401 co-op in week one and review it with your co-op supervisor.
2. During any onboarding (co-op, internship, open-source project), produce a pull request that fixes the setup docs.
3. Keep a brag document for one semester and use it to write your next resume version.

## Sources

All checked October 2026.

1. Julia Evans. *Get your work recognized: write a brag document* (2019). https://jvns.ca/blog/brag-documents/
2. Google re:Work. *Understand team effectiveness* (Project Aristotle findings on psychological safety). https://rework.withgoogle.com/

_Last reviewed: 2026-10_
