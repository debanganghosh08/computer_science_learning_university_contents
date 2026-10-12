# FND106 · Labs and projects

This course writes about real work from your other Year 1 courses: your FND101 programs, FND102 measurements, FND104 repositories and FND105 tools. Every written deliverable lives in a Git repository as Markdown, is reviewed through a pull request, and ends with a short note of any AI help used.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Rewrite clinic | Clear sentences and words | Three paragraphs rewritten to half their length with all facts kept, plus a 20-term project glossary | 3 h |
| 2 · Structure and diagrams | Scannable pages | A wall-of-text document restructured in GitHub Markdown, with a Mermaid diagram and a C4 context diagram | 3 h |
| 3 · README stranger test | Docs that work for newcomers | README for FND101 P1; notes from two silent stranger tests with every hesitation and the fix you made | 4 h |
| 4 · A real bug report | Reproducible reports | One issue filed on a public open-source project (or the class tracker) with a minimal reproducible example; evidence that someone reproduced it | 3 h |
| 5 · Review exchange | Giving and receiving review | 10+ labelled review comments on peers' PRs; your replies to all comments on your own PR, through to approval; one AI PR summary compared against its diff | 4 h |
| 6 · Design review | Running a written review | Written comments on a classmate's design doc using Conventional Comments; meeting notes with decisions and owners | 3 h |
| 7 · Postmortem and incident updates | Blameless incident writing | Postmortem for a real failure in one of your labs; 4 timestamped status updates for an illustrative outage | 4 h |
| 8 · Talk and demo | Speaking with evidence | Recorded 5-minute talk with a live demo and fallback recording; peer feedback forms; your improvement plan | 4 h |
| 9 · Global async communication | Writing for a distributed team | Two weeks of async standups; 10 messages rewritten for international readers; three emails (access request, escalation, polite refusal) | 3 h |
| 10 · Professional presence | Public evidence of skill | GitHub profile README, three pinned repositories with strong READMEs, five achievement bullets with numbers you measured | 3 h |

## Projects

### P1 · Documentation makeover (L1, ~6 hours)

**Real-world inspiration.** Well-run open-source projects such as pytest and uv separate tutorials, how-to guides and reference material, and treat docs as code reviewed in pull requests. A newcomer's first ten minutes decide whether they adopt a tool.

**What to build.** Take one of your FND101 or FND104 projects and give it complete documentation: README (with a quickstart of at most five commands), `CONTRIBUTING.md`, `CHANGELOG.md`, and a `docs/` folder with one tutorial, one how-to guide, one reference page and one explanation page (Diátaxis).

**Acceptance criteria**
- Two people who have never seen the project each complete the quickstart in 10 minutes or less, observed silently and timed; their notes are in the repo.
- Every command in the README runs in CI (for example, a script that executes the quickstart in a clean container) and passes.
- Zero markdownlint errors; Vale with a published style guide reports no errors and at most 5 warnings, each justified.
- Each docs page states its Diátaxis type, and a peer reviewer agrees with the classification.

**Stretch goals.** Publish the docs as a static site (for example, GitHub Pages); add a "Troubleshooting" page built from real questions your testers asked.

**What it proves to an employer.** You make your work usable by others without hand-holding, which is the difference between code and a product.

### P2 · Design doc and review cycle (L2, ~15 hours)

**Real-world inspiration.** Google's design-doc practice, Rust's RFC process, Python's PEPs and Amazon's narrative memos all use the same loop: write the proposal, gather written critique, decide, and record why.

**What to build.** A 3–5 page design doc (at most 2,000 words) for a meaningful extension of one of your projects, for example adding multi-currency support and import from bank statement CSVs to your FND101 expense settler (an illustrative scenario). It must contain context, goals, non-goals, requirements using RFC 2119 keywords, the proposed design with one diagram, at least two alternatives, a trade-off table, risks, a test and rollout plan, and open questions. Then run a formal review with at least three reviewers, publish a revised version, and record the final decision as an ADR.

**Acceptance criteria**
- At least three reviewers leave labelled comments; every comment is resolved or explicitly deferred with a reason, visible in the PR.
- After one reading, at least two of three reviewers correctly restate the goal, the chosen option and its main trade-off in a short survey.
- RFC 2119 keywords are used only in the requirements section and each is defensible in review.
- The revision history shows what changed in response to review.
- An ADR in Nygard's format records the decision and its consequences.

**Stretch goals.** Present the doc in a 10-minute review meeting run Amazon-style (silent reading first, then discussion); implement the smallest slice and record in a follow-up ADR what the design got wrong.

**What it proves to an employer.** You can think through a change before building it, invite criticism, and leave a decision record others can trust: core skills for any engineer who will grow beyond writing tickets.

### P3 · Public engineering portfolio (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Engineers in India and elsewhere are often found through their public work: project write-ups, open-source pull requests, conference and meetup talks (FOSS United, PyCon India), and company engineering blogs such as Zerodha's and PhonePe's.

**What to build.** A public portfolio with six parts:
1. GitHub profile README and three pinned repositories, each passing the P1 stranger test.
2. Two technical articles of 1,200 words or more: one explaining a concept from FND102 or FND103 with your own diagrams, one case study of a Year 1 project with measured results. Each includes a sources list.
3. One upstream open-source pull request with an excellent description (merged, or under active review).
4. A recorded 8–10 minute talk with a live demo, given to a real audience (college club, meetup or online community), with slides.
5. A blameless postmortem of a real failure in your own work.
6. An updated LinkedIn profile featuring the articles, talk and projects.

**Acceptance criteria**
- Every factual claim in both articles is sourced or backed by your own measurement; a peer fact-check finds zero unsupported claims after revision.
- The talk stays within 10 minutes, includes a working demo, and answers at least three audience questions (recording or audience feedback as evidence).
- Feedback is gathered from at least three people outside your class, summarised, and at least two changes are made in response.
- The upstream PR description states context, change, testing and risk.
- An AI-use note lists what AI helped with and how you checked it.

**Stretch goals.** Get an article accepted on a community or company engineering blog; submit a talk proposal to a regional meetup or conference.

**What it proves to an employer.** You can explain your work clearly to engineers and non-engineers, in writing and in person, with evidence: the trait that separates candidates with similar technical skills.

## Feeds into

- [CS205 Software Engineering I](../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md): design docs, reviews and team process on larger projects.
- [CAR301 Career Lab I](../../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) and [CAR401 Career Lab II](../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): portfolio, interviews and system-design communication.
- [RES501 Research Methods and Scientific Writing](../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) and the thesis or capstone.
- [FDE305 Technical Communication in the Field](../../../03_majors/forward_deployed_engineering/year_3/FDE305_technical_communication_in_the_field_demos/README.md) and [LCH502 Career Launch and Founder Studio](../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md).
