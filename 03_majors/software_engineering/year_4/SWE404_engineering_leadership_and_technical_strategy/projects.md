# SWE404 · Labs and projects

Leadership is practised on real people. Students work in teams of 5–6 on a running software project (your IND401 co-op team, a capstone team, or an open-source project), and each student rotates as tech lead for at least three weeks. Mentoring pairs each student with a first- or second-year student for the semester. Role-plays use written scenarios; nobody discusses real colleagues' private matters. Peer and mentee feedback is collected anonymously.

## Labs (workshops)

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Ladders and archetypes | Map three public career frameworks; classify two staff engineers' work into archetypes | Comparison table and a one-page note on your own target path | 3 h |
| 2 · Definition of done | Write your team's definition of done, including rules for agent-generated PRs | The document, adopted by the team (meeting notes) | 2 h |
| 3 · RFC and decision meeting | Write an RFC on a contested change; run a 45-minute decision meeting | RFC, decision record with owner, dissent and follow-ups; observer ratings | 5 h |
| 4 · Monte Carlo forecasting | Forecast your team's next milestone from 8+ weeks of throughput data | 50% and 85% dates, method, and the actual outcome later in the term | 3 h |
| 5 · Strategy kernel | Diagnose a provided organisation's technical problems; write guiding policies and actions | 2-page strategy; critique from two peers | 4 h |
| 6 · Structured interview design and calibration | Design a structured SDE-2 loop (one AI-assisted round, one AI-free round); score 4 recorded mock interviews independently, then calibrate | Rubrics, independent scores, inter-rater agreement before and after calibration | 5 h |
| 7 · AI-team assessment | Score a real team (or an open-source project's maintainers) on DORA's seven AI capabilities with evidence | Scorecard and two improvement proposals | 3 h |
| 8 · 1:1, feedback and conflict role-plays | Four scripted scenarios: career 1:1, underperformance, interpersonal conflict, burnout | Your plans, observer feedback, and a reflection | 4 h |
| 9 · Organisation design | Redesign a 40-person organisation (provided) around team types and cognitive load | Team map, interaction modes, 90-day transition plan | 4 h |
| 10 · Executive memo | One-page memo asking for a migration investment; 5-minute presentation to a panel | Memo, slides, panel questions and your answers | 3 h |

## Projects

### P1 · RFC that reaches a decision (L1, ~6 hours)

**Real-world inspiration:** open RFC processes such as Rust RFCs, Python PEPs and Kubernetes KEPs, and internal design-doc reviews at product companies.

**What to build:** an RFC for a real change: either in your team's project or as a contribution proposal to an open-source project that accepts design proposals. Gather feedback, revise, and drive it to a decision.

**Acceptance criteria:**
- The RFC states the problem, constraints, at least two alternatives with costs, a recommendation, risks, and a rollout plan.
- At least 3 reviewers' comments are addressed in writing, each marked accepted, rejected (with reason) or deferred.
- A recorded decision exists (accepted, rejected or postponed) with a named owner; if open source, a link to the discussion.
- One page maximum for the summary; full RFC under 6 pages.

**Stretch goals:** the change is implemented and the RFC is updated with what actually happened.

**What it proves to an employer:** you can move a group to a decision through writing, the core skill of senior and staff engineers.

### P2 · Tech-lead rotation with an AI-augmented team (L2, ~15 hours of leadership time, alongside team delivery)

**Real-world inspiration:** first-time tech leads at product companies and GCCs (global capability centres) in India, who lead 4–8 engineers while still writing code, now with agents in the workflow.

**What to build:** lead your team for at least three weeks. Produce a plan with forecasts, split work between people and agents with reasons, run stand-ups, a design review and a retrospective, and protect the quality bar. Hand over cleanly to the next lead.

**Acceptance criteria:**
- Plan with Monte Carlo forecast; actual delivery within the 85% range, or a written re-forecast issued at least one week before the miss.
- Work-split log: every task with owner (person or agent), reason, outcome, and review time.
- Quality held: no increase in change failure rate or escaped defects during your rotation compared with the previous rotation (team metrics).
- Retrospective actions: at least 2 of 3 completed before the next retrospective.
- Peer feedback (anonymous) from at least 4 teammates, and your written response to it.
- Handover document that the next lead rates as sufficient to start without a meeting.

**Stretch goals:** introduce one AI-workflow improvement (from SWE304) and measure its effect over your rotation.

**What it proves to an employer:** you can lead a small team to delivery and keep quality up, with evidence rather than self-description.

### P3 · Technical strategy and leadership portfolio (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** staff engineers and engineering managers write strategies for problems such as "our monolith slows every team", "our AI tooling is unmanaged", or "we cannot hire fast enough". Organisations in this project are **illustrative** unless you have permission to use a real one.

**What to build:** choose a real or realistic organisation of 30–150 engineers (your co-op employer with permission, an open-source foundation, or a provided case such as an Indian fintech scaling after a funding round). Deliver:
1. A technical strategy (5–8 pages): diagnosis with evidence, guiding policies, coherent actions over 12 months, risks, and how success is measured.
2. An AI engineering policy appendix (tools, data rules, review, measurement, junior development), consistent with the strategy.
3. A hiring plan for the next 6 months with one structured interview loop and rubrics.
4. A leadership portfolio: your P1 RFC, P2 rotation evidence, mentoring report (with mentee feedback) and a reflection.

**Acceptance criteria:**
- The diagnosis cites at least 5 pieces of evidence (metrics, incidents, surveys, design docs); every guiding policy follows from the diagnosis.
- Actions are sequenced, owned and costed; at least one action is something the organisation will stop doing.
- A 30-minute panel (product, engineering and finance roles) questions the strategy; you answer, then revise once with a change log.
- The AI policy addresses every one of DORA's seven AI capabilities explicitly.
- The interview loop's rubrics reach acceptable agreement between two independent scorers on two mock candidates (method and numbers reported).
- Mentoring report shows progress on at least two agreed goals, with the mentee's written view.

**Stretch goals:** present the strategy to real engineers at your co-op employer or an open-source community and record their feedback.

**What it proves to an employer:** you can think and write at staff or manager level, set direction, hire and grow people, and lead teams where agents do much of the implementation.

## Feeds into

- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): the strategy and hiring plan become a founder's or first engineering manager's playbook.
- [THS502 Thesis or Capstone II](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): leading the capstone team.
- [CAR401 Career Lab II](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): behavioural and leadership interview stories come from P2 and P3 evidence.
