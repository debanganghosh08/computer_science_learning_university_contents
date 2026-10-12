# FND106 · Technical Communication and Professional Skills

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 1 · 1 | 4 (≈ 120 hours) | L0 → L2 | none | no formal dependents; used in every later course, especially [CS205](../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CAR301](../../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md), [RES501](../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) and the [FDE major](../../../03_majors/forward_deployed_engineering/README.md) |

## Why this course matters now

Engineering work is mostly written and spoken: issues, pull-request descriptions, code reviews, design docs, incident reports, status updates and demos. Amazon runs meetings on narratively structured memos read in silence instead of slide decks; Google teams write design docs before building; the IETF and open-source projects such as Rust and Python make decisions through written RFCs and PEPs. AI assistants (Claude, ChatGPT, Gemini, Copilot's pull-request summaries) now produce fluent text instantly, so fluency is no longer the differentiator. Precision, structure, verified facts, and judgment about what the reader needs are what reviewers, managers and clients reward, and they are what this course trains, in plain international English.

## Learning outcomes

By the end you can:

1. Write a README that lets a stranger install, run and test your project in 10 minutes or less, verified by an observed user test.
2. Organise documentation by reader need using Diátaxis (tutorial, how-to, reference, explanation).
3. Write a bug report with a minimal reproducible example that another person reproduces on the first try.
4. Write a 2–4 page design doc with goals, non-goals, alternatives and trade-offs, using RFC 2119 requirement words correctly.
5. Write a blameless postmortem with timeline, impact, root cause, contributing factors and owned action items.
6. Give code-review comments that are specific, labelled by severity and kind, and receive review without defensiveness.
7. Deliver a 5-minute technical talk with a live demo and a fallback, and handle questions.
8. Write clear asynchronous messages and emails for global teams across time zones.
9. Build a professional presence: GitHub profile, project write-ups, LinkedIn, and respectful networking.
10. Use AI to edit and critique your writing while keeping your voice, checking every fact, and disclosing use.

## Chapters and lessons

### Chapter 1 · Clear writing for engineers (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Audience and purpose | Who reads this, what they already know, what they must do afterwards. | For one topic, write three openings: for a teammate, a manager, a new user. |
| 1.2 Sentences | Short sentences, one idea each, active voice, strong verbs, defining terms on first use (Google Technical Writing One). | Rewrite three dense paragraphs; halve the word count without losing facts. |
| 1.3 Words | Plain language, consistent terminology, numbers with units, no undefined acronyms. | Build a 20-term glossary for your FND101 project. |
| 1.4 Editing | Read aloud, cut, reorder; a readability checker as a hint, not a rule. | Edit a peer's paragraph with tracked changes and a one-line reason per change. |

**Check your understanding:** (1) Why does passive voice hide responsibility in incident reports? (2) When is a longer, more precise sentence better than a short vague one? (3) Why must one concept keep one name throughout a document?

### Chapter 2 · Structure and visuals (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Lead with the point | Bottom line up front, inverted pyramid, the summary a busy reader needs. | Rewrite a rambling update so the first two lines carry the decision. |
| 2.2 Scannable pages | Headings, lists, tables, code blocks; how people scan web pages (Nielsen Norman Group research). | Turn a wall of text into a structured Markdown page. |
| 2.3 Markdown | GitHub-flavoured Markdown: tables, task lists, links, relative paths, fenced code with languages. | Write a page that renders correctly on GitHub with all of these. |
| 2.4 Diagrams | When a diagram beats words; Mermaid sequence and flow diagrams, Excalidraw sketches, the C4 model levels. | Draw the data flow of your FND101 P3 as a Mermaid diagram and a C4 context diagram. |

**Check your understanding:** (1) What does a reader lose when the conclusion is in the last paragraph? (2) When is a table better than a list? (3) What must every diagram have so it can be read without you?

### Chapter 3 · READMEs and documentation (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 README anatomy | What and why, quickstart, usage, configuration, tests, contributing, licence, status. | Write the README for FND101 P1. |
| 3.2 Diátaxis | Tutorials (learning), how-to guides (tasks), reference (facts), explanation (understanding); why mixing them confuses readers. | Classify 10 pages from a real project's docs; propose one fix. |
| 3.3 Docs as code | Docs in the repo, reviewed in PRs, linted (markdownlint, Vale with a style guide), commands tested in CI. | Add markdownlint and Vale to a repo's CI. |
| 3.4 Change communication | `CHANGELOG.md` (Keep a Changelog), Semantic Versioning, release notes for users vs developers. | Write release notes for a version of your FND104 P2 tool. |
| 3.5 The stranger test | Watching someone follow your docs silently; noting every hesitation. | Run the test with two people; fix every point where they stalled. |

**Check your understanding:** (1) Why does a tutorial fail when it stops to explain every option? (2) What breaks first in a README that nobody tests? (3) What belongs in release notes but not in a commit log?

### Chapter 4 · Bug reports, questions and issues (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Bug reports | Steps to reproduce, expected vs actual, environment, versions, logs; Simon Tatham's "How to Report Bugs Effectively". | Rewrite three vague bug reports from a public issue tracker into reproducible ones. |
| 4.2 Minimal reproducible examples | Remove everything not needed to show the bug (Stack Overflow's MRE guide). | Reduce a 200-line failing script to under 20 lines. |
| 4.3 Asking good questions | What you tried, what you expected, what happened; Julia Evans on good questions; "no hello" in chat. | Post one well-formed question in a public forum or class channel. |
| 4.4 Issues as a system | Templates, labels, triage, linking issues to PRs, closing with a reason. | Design issue templates for your team's P3 repository in FND104. |

**Check your understanding:** (1) Why is "it doesn't work" unanswerable? (2) What do you learn by minimising a bug before reporting it? (3) Why should the expected behaviour be written down even when it seems obvious?

### Chapter 5 · Commits, pull requests and code review (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Commit messages | Summary line, body explaining why, Conventional Commits; the history as documentation. | Rewrite the messages of your last 10 commits. |
| 5.2 Pull-request descriptions | Context, what changed, how it was tested, risk and rollback, screenshots; small PRs. | Write descriptions for three of your PRs; a peer rates them for reviewability. |
| 5.3 Reviewing | Google's review guidance: design, functionality, complexity, tests, naming, comments; approve once the change clearly improves code health, even if not perfect. | Review three peer PRs with the checklist. |
| 5.4 Comment craft | Conventional Comments labels (praise, nitpick, suggestion, issue, question); asking instead of commanding; explaining why. | Rewrite 10 harsh or vague review comments. |
| 5.5 Receiving review | Separating self from code, asking for clarification, disagreeing with evidence, closing the loop. | Respond to every comment on one of your PRs and get it approved. |
| 5.6 Reviewing AI-written changes | AI summaries describe intent, not necessarily the diff; checking scope creep, new dependencies and tests. | Compare an AI-generated PR summary with the actual diff; list every mismatch. |

**Check your understanding:** (1) Why does a reviewer need the "why" of a change, not only the "what"? (2) When is blocking a PR on a style nit wrong? (3) What is the risk of approving an AI-summarised PR without reading the diff?

### Chapter 6 · Design docs and RFCs (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Why write before building | Design docs at Google: context, goals and non-goals, design, alternatives considered, cross-cutting concerns; Amazon's narrative memos. | Read one public RFC (Rust or Python PEP) and outline its structure. |
| 6.2 Requirements language | RFC 2119 keywords: MUST, SHOULD, MAY and their exact meanings. | Rewrite 10 loose requirements with RFC 2119 words; argue each choice. |
| 6.3 Alternatives and trade-offs | At least two real alternatives, criteria, a trade-off table, risks, what you would measure. | Write the alternatives section for a feature in your FND101 P2. |
| 6.4 Decision records | Architecture Decision Records (Michael Nygard's format): context, decision, consequences. | Record three decisions from your projects as ADRs. |
| 6.5 Running a review | Asynchronous comments, a review meeting, resolving or deferring every comment, publishing the outcome. | Hold a design review of a classmate's doc with written comments. |

**Check your understanding:** (1) Why do non-goals prevent arguments later? (2) What is the difference between "the system SHOULD retry" and "MUST retry"? (3) Why record rejected alternatives?

### Chapter 7 · Incident and status communication (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Blameless postmortems | Focus on systems, not people (Google SRE book); summary, impact, timeline, root cause, contributing factors, action items with owners. | Write a postmortem for a real failure in one of your labs. |
| 7.2 Reading real postmortems | Cloudflare's 18 November 2025 outage report; GitLab's 2017 database incident. | Critique Cloudflare's report: what makes it clear, what you would add. |
| 7.3 Updates during incidents | Short, timestamped, factual updates; what is known, unknown and next; audience-specific channels. | Write 4 status updates for an illustrative scenario of a payment-page outage. |
| 7.4 Routine status | Weekly updates that lead with outcomes, risks and asks; escalating early. | Send a weekly status note for your FND104 P3 team for 4 weeks. |

**Check your understanding:** (1) Why does blame make future incidents worse? (2) What makes an action item real rather than a wish? (3) During an outage, why is "no new information; next update at 14:30 IST" still worth posting?

### Chapter 8 · Speaking and presenting (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Structure a talk | Problem, insight, evidence or demo, ask; one idea per slide; Patrick Winston's "How to Speak" (MIT). | Outline a 5-minute talk on one of your projects. |
| 8.2 Demos | Scripted live demos, fallback recordings, preparing data, rehearsing failure. | Record a 2-minute demo; rehearse it with the network disconnected. |
| 8.3 Delivery and Q&A | Pace, pauses, eye contact on video calls; repeating the question; "I don't know, I'll find out". | Give the 5-minute talk to a group; answer 3 questions. |
| 8.4 Meetings | Agendas, notes, decisions and action items, ending on time. | Run a 20-minute team meeting and publish the notes within an hour. |

**Check your understanding:** (1) Why open with the problem rather than with your name and outline? (2) What is your plan if the live demo fails? (3) What should a meeting note contain so that someone absent can act on it?

### Chapter 9 · English for global tech teams (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Precise technical English | Words engineers misuse (latency vs throughput, error vs failure, deprecated vs removed); hedging vs commitment. | Fix 15 sentences with imprecise technical words. |
| 9.2 Clear for every reader | Avoiding idioms and region-specific phrases that confuse global readers (for example "do the needful", "prepone", "revert back"); dates in ISO 8601; time zones stated (IST and UTC). | Rewrite 10 messages for a reader in another country. |
| 9.3 Asynchronous writing | One complete message instead of "hi" followed by silence; context, ask, deadline; threads. | Write async standups for 2 weeks in your team channel. |
| 9.4 Email | Subject lines that say the ask, short bodies, clear next step, polite follow-ups. | Write three emails: requesting access, escalating a blocker, declining a request. |
| 9.5 Reading specifications | Reading RFCs, API docs and contracts carefully; summarising for a teammate. | Summarise one section of an RFC in 150 words; a peer checks accuracy. |

**Check your understanding:** (1) Why can "please revert" be misunderstood across regions? (2) What does "by EOD" mean to a team spread over IST and PST, and what should you write instead? (3) Why is a complete async message faster for everyone, even if it takes longer to write?

### Chapter 10 · Professional presence and networking (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 GitHub profile | Profile README, pinned repositories with strong READMEs, contribution history as evidence, not decoration. | Publish your profile README and pin three projects. |
| 10.2 Writing about your work | Project case studies and technical blog posts: problem, approach, evidence, what you'd change; learn from company engineering blogs (Zerodha, PhonePe and others). | Draft a 1,000-word case study of one Year 1 project. |
| 10.3 LinkedIn and résumé basics | Headline, about, featured work, one-page résumé with achievement bullets you can prove. | Write five achievement bullets with numbers you measured. |
| 10.4 Networking | Meetups and communities (FOSS United, PyCon India), short specific cold messages, informational interviews, referral etiquette. | Send three informational-interview requests using a template you wrote. |

**Check your understanding:** (1) Why is a well-documented small project more persuasive than many unfinished ones? (2) What makes a cold message easy to say yes to? (3) Why must every number on your résumé be one you can explain in detail?

### Chapter 11 · Working in teams (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Team agreements | Roles, working hours, response times, definition of done, decision rules. | Write a one-page team charter for your FND104 P3 team. |
| 11.2 Feedback | Situation–behaviour–impact feedback; specific praise; asking for feedback. | Give and receive two pieces of written feedback in your team. |
| 11.3 Disagreement | Disagreeing with data, escalating respectfully, then committing (Amazon's "Have Backbone; Disagree and Commit"). | Role-play a design disagreement; write the decision record afterwards. |
| 11.4 Estimating and saying no | Breaking work down, ranges instead of single numbers, protecting scope. | Estimate 5 tasks, then compare with actual time at the end of the month. |

**Check your understanding:** (1) Why does vague praise not help anyone? (2) When should you stop arguing and commit? (3) Why give an estimate as a range?

### Chapter 12 · Writing with AI, honestly (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 AI as editor and critic | Asking for clarity edits, structural suggestions, a skeptical reviewer's critique; keeping your voice. | Edit a draft with AI; accept or reject each suggestion with a reason. |
| 12.2 Facts and fabrication | AI adds plausible but invented versions, commands and citations; every fact traced to a source. | Fact-check an AI-expanded paragraph; mark each claim verified or removed. |
| 12.3 Confidentiality and disclosure | Never paste confidential or personal data; when and how to disclose AI help; AI detectors are unreliable and biased against non-native English writers. | Write your disclosure note for the portfolio. |
| 12.4 Portfolio review | Assemble README, bug report, design doc, postmortem, reviews and talk recording. | Submit the portfolio for the final review. |

**Check your understanding:** (1) What does an AI edit typically remove that your reader needed? (2) Why is a fluent paragraph with one invented version number worse than a clumsy correct one? (3) What would you do if a teacher's detector flagged your own writing?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Rewrite clinic | Edited paragraphs |
| 2 | 2 | Markdown and Mermaid | Structured page with diagram |
| 3 | 3 | README and stranger test | Stranger-test notes |
| 4 | 4 | Real bug report | Issue link; **P1 due** |
| 5 | 5 | Commit and PR descriptions | Rewritten history |
| 6 | 5 | Review exchange | Labelled review comments |
| 7 | 6 | Design doc draft | Draft |
| 8 | 6 | Design review | **P2 due** |
| 9 | 7 | Postmortem | Postmortem and incident updates |
| 10 | 8 | Talk and demo | Recorded 5-minute talk |
| 11 | 9 | Global English | Rewritten messages; async standups |
| 12 | 10 | Profile and case study | Profile README, case study draft |
| 13 | 11 | Team charter and feedback | Charter, feedback log |
| 14 | 12 | AI editing and portfolio | **P3 due** |
| 15 | Review and exam | Timed writing practice | Final exam (AI-off) |

## Working with AI in this course

- **Use AI for:** clarity and grammar edits on a finished draft; alternative structures; a simulated skeptical reviewer ("critique this design doc as a staff engineer would"); rehearsing Q&A for a talk; explaining unfamiliar English usage. Tools: Claude, ChatGPT, Gemini, and Copilot's PR summaries (to be checked against the diff).
- **Do without AI (drills):** timed writing (a bug report in 15 minutes, a design-doc section in 30, a status update in 5); live talks and Q&A; review comments; the final exam.
- **Verify AI output by:** tracing every factual claim to a source; comparing every AI summary with the underlying diff, log or document; reading aloud; the stranger test for READMEs; asking a peer to restate your main point.
- **Where AI still fails here:** generic filler and inflated adjectives; invented details (version numbers, flags, metrics) inserted to sound complete; PR summaries describing what a change was meant to do rather than what it does; terminology drifting between sections; flattening a distinctive voice into a uniform one. Chapter 12's practice has you document each of these in your own drafts.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Writing portfolio (README, bug report, design doc, postmortem, review comments, case study) | 35% |
| Talks and demos | 15% |
| Projects: P1 5%, P2 10%, P3 15% | 30% |
| Final exam (timed, AI-off writing tasks) | 20% |

**Gate:** you pass when (1) two strangers install and run your project from your README alone in 10 minutes or less; (2) a reviewer can restate your design doc's goal, non-goals, chosen option and main trade-off after one reading; (3) someone else reproduces your bug report on the first try; and (4) you deliver a 5-minute talk with a working demo and answer three questions clearly.

## Industry reality

Written communication is how decisions are made and remembered: Amazon's memos, Google's design docs and code review guidance, IETF RFCs, Python PEPs, Rust RFCs, Oxide's public RFDs, and the Linux kernel's patch-submission rules are all public examples. Postmortems such as Cloudflare's (18 November 2025) and GitLab's (2017) are read by thousands of engineers because they are clear. Client-facing roles such as forward-deployed engineering and consulting depend on this skill daily.

**Interview questions from this course**

1. *"Tell me about a time you disagreed with a teammate's technical decision."* Situation, the evidence you brought, how you raised it, the outcome, committing to the final decision, what you learned.
2. *"Explain your project to a non-technical person, then to an engineer."* Switching vocabulary and depth, leading with the problem, one concrete example, checking understanding.
3. *"How would you review a PR you think is badly designed?"* Talk early, ask questions, separate blocking issues from nits, propose alternatives, approve on improved code health.
4. *"Walk me through a bug you fixed."* Symptom, reproduction, hypotheses, root cause, fix, regression test, and who you told and how.
5. *"Write a short design proposal for this feature."* Goals and non-goals, at least two alternatives, trade-offs, risks, rollout and how success will be measured.

## Resources (free first)

- **Writing:** [Google Technical Writing One and Two](https://developers.google.com/tech-writing); [Google developer documentation style guide](https://developers.google.com/style); [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/); [Plain language guide](https://digital.gov/guides/plain-language); [Diátaxis](https://diataxis.fr/); [Write the Docs guide](https://www.writethedocs.org/guide/); [Make a README](https://www.makeareadme.com/); [About READMEs on GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes); [GitHub Markdown syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax); [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); [Semantic Versioning](https://semver.org/).
- **Bugs, questions and review:** Simon Tatham, [How to Report Bugs Effectively](https://www.chiark.greenend.org.uk/~sgtatham/bugs.html); [Stack Overflow MRE guide](https://stackoverflow.com/help/minimal-reproducible-example); Julia Evans, [Asking good questions](https://jvns.ca/blog/good-questions/); [nohello.net](https://nohello.net/); [Google code review guide](https://google.github.io/eng-practices/review/); [Conventional Comments](https://conventionalcomments.org/); [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/); [Linux kernel: submitting patches](https://docs.kernel.org/process/submitting-patches.html).
- **Design and decisions:** Malte Ubl, [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/); [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119); [Rust RFCs](https://github.com/rust-lang/rfcs); [PEP 1](https://peps.python.org/pep-0001/); [Oxide RFD 1](https://rfd.shared.oxide.computer/rfd/0001); Michael Nygard, [Documenting Architecture Decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions); [adr.github.io](https://adr.github.io/); [C4 model](https://c4model.com/); [Mermaid](https://mermaid.js.org/).
- **Incidents:** [Google SRE book: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/); [Cloudflare, 18 November 2025 outage](https://blog.cloudflare.com/18-november-2025-outage/); [GitLab 2017 postmortem](https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/).
- **Speaking and English:** Patrick Winston, [How to Speak (MIT OCW)](https://ocw.mit.edu/courses/res-tll-005-how-to-speak-january-iap-2018/); NPTEL [Technical English for Engineers](https://nptel.ac.in/courses/109106094) (Prof. Aysha Viswamohan, IIT Madras); [BBC Learning English](https://www.bbc.co.uk/learningenglish).
- **Presence and community:** [GitHub profile README](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme); [Open Source Guides](https://opensource.guide/how-to-contribute/); [FOSS United events](https://fossunited.org/events); [PyCon India](https://in.pycon.org/); [Zerodha tech blog](https://zerodha.tech/blog/); [PhonePe tech blog](https://tech.phonepe.com/).
- **Tools:** [Vale](https://vale.sh/); [markdownlint](https://github.com/DavidAnson/markdownlint); [Excalidraw](https://excalidraw.com/).

## Sources

- Amazon's narrative memos instead of slide presentations; "a great memo probably should take a week or more": [2017 Letter to Shareholders](https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders) (checked Oct 2026).
- "Have Backbone; Disagree and Commit": [Amazon Leadership Principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles) (checked Oct 2026).
- Approving once a change improves overall code health: [Google eng-practices, The Standard of Code Review](https://google.github.io/eng-practices/review/reviewer/standard.html) (checked Oct 2026).
- Cloudflare outage of 18 Nov 2025 (database permissions change, oversized feature file, not an attack): [Cloudflare blog](https://blog.cloudflare.com/18-november-2025-outage/) (checked Oct 2026).
- GitLab outage of 31 Jan 2017: [GitLab postmortem](https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/) (checked Oct 2026).
- AI-text detectors misclassify non-native English writing: [Liang et al., 2023](https://arxiv.org/abs/2304.02819) (checked Oct 2026).
- How people read web pages: [Nielsen Norman Group, F-shaped pattern](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/) (checked Oct 2026).

_Last reviewed: 2026-10_
