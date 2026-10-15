# The AI-native study protocol

| Read time | Applies to | Taught in depth in |
|---|---|---|
| ~25 minutes | Every course, every year | [FND105 AI-Native Learning and Building](../01_year_1_foundations/semester_1/FND105_ai_native_learning_and_building/README.md) |

AI assistants can explain, generate, debug and review faster than any person. That is exactly why they can stop you from learning: if the assistant does the thinking, the assistant gets the practice. This page explains what the research says, then gives a routine that uses AI where it helps and keeps it away where it harms: a daily method, AI-off drills, tutor prompts you can copy, a checklist for verifying AI explanations, and rules for integrity and privacy.

## 1. What the research says

### How skills form (decades of evidence)

| Finding | What was shown | Source |
|---|---|---|
| **Generation effect** | People remember information they produce themselves (for example, completing a word from a cue) better than information they only read | Slamecka and Graf, 1978, [doi:10.1037/0278-7393.4.6.592](https://doi.org/10.1037/0278-7393.4.6.592) |
| **Retrieval practice (testing effect)** | Practising recall from memory produces better long-term retention than re-studying the same material, even though re-studying feels more productive at the time | Roediger and Karpicke, 2006, [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x); review: Roediger and Butler, 2011, [doi:10.1016/j.tics.2010.09.003](https://doi.org/10.1016/j.tics.2010.09.003) |
| **Retrieval beats elaborate studying** | Students who practised retrieval learned more than students who built detailed concept maps with the material in front of them | Karpicke and Blunt, 2011, [doi:10.1126/science.1199327](https://doi.org/10.1126/science.1199327) |
| **Which techniques work** | A review of ten common techniques rated practice testing and distributed (spaced) practice as high utility; highlighting and rereading as low utility | Dunlosky et al., 2013, [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266) |
| **Spacing** | Spreading practice over days beats massing it into one session, for the same total time | Cepeda et al., 2006, [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354) |
| **Interleaving** | Mixing different problem types in one practice set improved later test performance in mathematics compared with blocks of one type | Rohrer and Taylor, 2007, [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8) |
| **Productive failure** | Students who struggled with complex problems before instruction did better on later transfer problems than students taught first | Kapur, 2008, [doi:10.1080/07370000802212669](https://doi.org/10.1080/07370000802212669) |
| **Cognitive load and worked examples** | Complete beginners can be overloaded by unguided problem solving; studying worked examples helps them at the start | Sweller, 1988, [doi:10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4); Alfieri et al., 2011, [doi:10.1037/a0021017](https://doi.org/10.1037/a0021017) |

The last two rows pull in different directions, and both are true. **When a topic is completely new, study one or two worked examples first. Once you have the basic idea, attempt problems yourself before asking for help.** Struggle helps when you have enough to struggle with.

### What happens when learners use AI

| Study | Who and what | Result |
|---|---|---|
| Bastani et al., *PNAS*, 2025, [doi:10.1073/pnas.2422633122](https://doi.org/10.1073/pnas.2422633122) | Field experiment with nearly a thousand high-school mathematics students; one group had a standard GPT-4 chat ("GPT Base"), another a tutor prompted to give hints instead of answers ("GPT Tutor") | With access, practice grades rose 48% (GPT Base) and 127% (GPT Tutor). When access was removed, the GPT Base group did **17% worse** on their own than students who never had access. The tutor's safeguards largely removed that harm |
| Shen and Tamkin (Anthropic), January 2026, [arXiv:2601.20245](https://arxiv.org/abs/2601.20245); [summary](https://www.anthropic.com/research/AI-assistance-coding-skills) | Randomised experiment: 52 software engineers learning a new asynchronous programming library, with or without AI | The AI group scored 50% on the follow-up quiz against 67% for the hand-coding group, and was not significantly faster. AI delegation, progressive reliance and iterative AI debugging scored lowest; generation-then-comprehension, hybrid code-explanation and conceptual inquiry preserved learning |
| Kestin et al., *Scientific Reports*, 2025, [doi:10.1038/s41598-025-97652-6](https://doi.org/10.1038/s41598-025-97652-6) | Randomised controlled trial with college students: a custom AI tutor built on the same research-based teaching practices as an active-learning class, against the class itself | Students learned significantly more in less time with the AI tutor, and reported more engagement |

**What this means.** The same tool can help or harm. It harms when it **replaces** the work your brain must do (generating, retrieving, debugging). It helps when it is set up to make you do that work: giving hints instead of answers, asking you questions, explaining after you have tried. The protocol below is built on that difference.

## 2. The protocol: five steps for every topic

```text
 1. ATTEMPT (AI-off)  ->  2. TUTOR (Socratic AI)  ->  3. BUILD (AI allowed, logged)
                                                            |
 5. RETRIEVE (AI-off, spaced)  <-  4. VERIFY (evidence, not trust)
```

| Step | What you do | Time | AI |
|---|---|---|---|
| **1. Attempt** | Read the lesson or a worked example, then close it and try the exercise yourself. Write down what you tried and exactly where you got stuck | 20–40 min | Off |
| **2. Tutor** | Ask an AI for a **hint**, a question, or an explanation of the concept you are stuck on, never the solution. Use the prompts in section 4 | 10–20 min | On, in tutor mode |
| **3. Build** | Do the lab or project. AI may generate, review and debug, but you log every use in `AI_LOG.md` and you can explain every line you submit | Most of the lab time | On, logged |
| **4. Verify** | Check anything the AI told you against tests, official documentation, a second method, or a counterexample (section 5) | 10–20 min | Off for the check itself |
| **5. Retrieve** | Next day, and again a week later: answer three questions about the topic from memory, redo one exercise from scratch, or explain it aloud for two minutes | 15 min per session | Off |

### Your weekly rhythm

- **Daily (20 minutes, AI-off):** spaced-repetition review. Put definitions, commands, complexity facts and "why" questions into a flashcard tool such as [Anki](https://apps.ankiweb.net/), written in your own words.
- **Per course, per week:** at least one AI-off drill (section 3), timed, with the score logged.
- **Weekly (30 minutes):** read your `AI_LOG.md`. Where did AI save time? Where did it mislead you? Which tasks did you hand over that you could not yet do yourself? Move one of those back to AI-off for next week.
- **Every four weeks:** retake your AI-off baseline (the [placement questions](05_placement_check.md) for your current courses, or the course's sample gate). Your unaided score should rise or hold. If it falls, you are delegating too much: return to step 1 for that course.

### The AI-dependency check

Ask yourself these five questions every Friday. Two or more "no" answers mean you should cut AI back.

1. Could I rebuild this week's main piece of work without AI, perhaps more slowly?
2. When the AI was wrong this week, did I notice before running the code?
3. Can I explain the key idea of this week to a friend without notes?
4. Did I attempt each exercise before asking for help?
5. Is my AI-off drill score the same or better than four weeks ago?

## 3. AI-off drills

A drill is a short, timed exercise done without AI, and normally without search, to keep a core skill sharp. Each course lists its own. These are the common ones across the curriculum:

| Area | Drill | Time | Courses |
|---|---|---|---|
| Programming | Write a function from a one-paragraph spec with five tests, from a blank file | 20 min | FND101, FND111 |
| Reading code | Trace a 30-line program by hand with a state table and predict its output | 15 min | FND101, CS205 |
| Debugging | Fix a program with one planted bug, given only the failing test and traceback | 20 min | FND101, CS202 |
| Data structures and algorithms | One medium problem: clarify, brute force, optimise, code, test, state complexity aloud | 35–45 min | FND112, CS201 |
| Mathematics | One proof, or one derivation (a gradient, a probability), checked afterwards by code | 20 min | FND103, FND113, FND116, CS206 |
| Systems | Convert numbers between binary, hex and two's complement; explain one `strace` line by line | 15 min | FND102, CS202, CS203 |
| Shell and Git | Answer a question about a log file with one pipeline; recover a "lost" commit with `reflog` | 15 min | FND104 |
| SQL | Three queries on a known schema, including one window function and one anti-join | 20 min | FND115, CS211 |
| Networks | Read a packet capture and explain where the time went | 20 min | CS204 |
| Design | Sketch a design for a stated problem on paper: components, data, one failure mode | 30 min | CS205, CS212 |
| Writing | Write a bug report or a one-page design note from a scenario | 20 min | FND106 |
| Security | Threat-model a small system with STRIDE on paper | 20 min | CS213 |

Record each drill in `drills/` in your progress repository: date, drill, time taken, score, and the one mistake you made first.

## 4. Using AI as a Socratic tutor

A Socratic tutor answers questions with questions and gives the smallest useful hint. Most assistants will do this if you ask clearly. Paste one of these at the start of a conversation and adapt the bracketed parts.

**General tutor setup**

```text
You are my tutor for [topic, e.g. "binary search trees in a first DSA course"].
Rules: do not give me the solution or write code for my exercise. When I ask
for help, first ask me what I have tried. Then give the smallest hint that
lets me take the next step. If I am wrong, ask a question that exposes the
mistake instead of correcting it directly. After I solve it, ask me one
question that checks whether I understood why it works.
```

**Unstuck on an exercise**

```text
Here is the exercise and my attempt so far: [paste]. I am stuck at [exact
point]. Do not fix it. Tell me which part of my reasoning to re-examine,
and ask me one question about it.
```

**Explain a concept at the right level**

```text
Explain [concept] to someone who knows [what you already know] but not
[what you do not know]. Use one concrete example with small numbers. Then
give me two questions to check my understanding, and wait for my answers.
```

**Check my explanation (the Feynman test)**

```text
I will explain [concept] in my own words. Point out anything that is wrong,
vague or missing, but do not rewrite my explanation. Rate it: would a
classmate understand it from this alone?
```

**Quiz me from memory**

```text
Quiz me on [topic] with 8 questions, one at a time, mixing recall ("what
is...") and reasoning ("why would... fail if..."). Wait for each answer,
tell me if it is right, and keep score. At the end, list the two weakest
areas.
```

**Review my code like a senior engineer (after I finish)**

```text
Review this code I wrote for [purpose]. List problems by severity:
correctness, edge cases, readability, performance. For each, explain why it
matters and where, but do not rewrite the code. I will fix it myself.
```

**Generate practice, not answers**

```text
Give me 5 new practice problems on [topic], ordered from easy to hard,
similar to [an example problem]. Do not include solutions. I will ask for a
hint on each one only if I need it.
```

Tutoring works only if you keep to its rules too. If you catch yourself typing "just give me the answer", stop, take a short break, and return to step 1.

## 5. Verifying AI explanations

AI assistants produce fluent, confident text whether or not it is correct. Language models are trained and evaluated in ways that can reward guessing over admitting uncertainty ([Kalai et al., 2025](https://arxiv.org/abs/2509.04664)). Treat every AI explanation as a claim to check.

| Kind of claim | How to verify it |
|---|---|
| "This code works" | Run it. Write tests for the edge cases first: empty input, one element, duplicates, very large values, invalid input |
| "This function or package exists" | Look it up in the official documentation or the package registry. Assistants sometimes invent package names, and attackers register such names ([Spracklen et al., USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)) |
| "This algorithm runs in O(n log n)" | Derive it yourself, then run a doubling experiment: time it at n, 2n, 4n and check the growth |
| A mathematical derivation | Check it numerically: finite differences for gradients, a brute-force count for combinatorics, a simulation for probability |
| A fact with a date, number or name | Find the primary source (standard, RFC, official docs, the paper). If the AI gives a citation, open it and confirm it says what was claimed |
| "This is the best practice" | Ask for the trade-offs and the case where it is wrong. A practice with no downside is usually an overstatement |
| A security claim | Check against the relevant standard (OWASP, NIST) and test only on systems you own or legal practice platforms |
| An explanation of an error | Reproduce the error, apply the suggested cause, and confirm the error disappears for the stated reason, not by accident |

Red flags that should make you check twice: very specific numbers with no source, APIs that look plausible but that you have never seen, a "fix" that removes or weakens a test, and an answer that changes when you ask the same question again.

## 6. Academic integrity

There is no registrar here, so integrity is about whether your evidence is true. These rules apply to all coursework and gates in this curriculum:

1. **Gates and exams are AI-off unless the course says otherwise.** An AI-assisted gate is not a pass; it is practice.
2. **Log AI use in every project.** Keep an `AI_LOG.md` with the prompt (or its gist), what the AI produced, what you accepted or rejected, and how you verified it.
3. **Disclose it.** Each project README states which parts were AI-assisted. Employers increasingly ask, and some interviews test it: Canva, for example, expects some engineering candidates to use AI tools in interviews and evaluates whether they can "identify and fix issues in AI-generated code" ([Canva, 2025](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)), while Anthropic's guidance says live interviews are done without AI unless stated ([Anthropic](https://www.anthropic.com/candidate-ai-guidance)). Know the rules of each setting you are in.
4. **Explain every line.** If you cannot explain a line you submit, it is not yet yours. Rewrite it or remove it.
5. **Group work stays honest.** Discuss ideas freely; write your own solution. In study circles, never share gate answers with someone who has not attempted the gate.
6. **Follow your institution's rules when they are stricter.** If you are also enrolled at a college or on a course with its own AI policy (for example, [CS50's academic honesty policy](https://cs50.harvard.edu/x/honesty/)), that policy governs work you submit there.
7. **Do not trust AI-text detectors to judge you or others.** Detectors have been shown to misclassify writing by non-native English speakers as AI-generated ([Liang et al., 2023](https://arxiv.org/abs/2304.02819)). Use process evidence instead: drafts, commit history, logs.

## 7. Privacy and safety

What you paste into a hosted AI tool leaves your machine. Depending on the provider and your settings, it may be stored, reviewed or used for training. Before you paste anything:

| Never paste | Why | Do instead |
|---|---|---|
| Passwords, API keys, tokens, private keys, `.env` files | They can leak and be abused | Use placeholders; keep secrets in environment variables or a secret manager |
| Personal data about other people (names, phone numbers, Aadhaar numbers, health or financial details) | India's [Digital Personal Data Protection Act, 2023](https://www.meity.gov.in/data-protection-framework) and similar laws elsewhere govern processing of personal data | Use synthetic or anonymised data |
| Your employer's or client's code, documents or data | It may breach your contract and confidentiality; companies have restricted AI tools after staff pasted internal material into them ([TechCrunch, May 2023](https://techcrunch.com/2023/05/02/samsung-bans-use-of-generative-ai-tools-like-chatgpt-after-april-internal-data-leak/)) | Follow the employer's AI policy; use only approved tools |
| Unreleased exam or gate tasks | It breaks the integrity of the gate for everyone | Attempt the task yourself |

Practical settings and habits:

- **Read the data settings** of each AI tool you use: whether chats are used for training, how long they are kept, and how to delete them. Turn off training on your data where the option exists.
- **Use a local model for sensitive material.** A small model running on your laptop through [Ollama](https://ollama.com/) keeps the text on your machine (setup in [set up your lab](04_set_up_your_lab.md#6-a-local-llm-ollama)).
- **Run coding agents in a sandbox.** Give an agent its own branch, container or VM, review its changes hunk by hunk, and never give it production credentials. [FND104](../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) teaches this.
- **Treat AI-read content as untrusted.** Text an AI reads from web pages, documents or emails can contain hidden instructions ("prompt injection"). Do not let an AI act on your accounts based on content you have not reviewed.

## 8. One page to keep

Print or pin this:

1. **Attempt first, AI second.** Twenty honest minutes before any hint.
2. **Hints, not answers.** Use the tutor prompts.
3. **Log it.** Every AI use in a project goes in `AI_LOG.md`.
4. **Verify it.** Tests, docs, a second method, a counterexample.
5. **Retrieve it.** Tomorrow and next week, from memory.
6. **Drill weekly, AI-off.** Score it, log it.
7. **Gates are AI-off.** No exceptions unless the course says so.
8. **Protect secrets and people's data.** Placeholders, synthetic data, local models.

## Sources

All links checked October 2026.

1. Slamecka, N. J., and Graf, P. (1978). The generation effect: Delineation of a phenomenon. *Journal of Experimental Psychology: Human Learning and Memory*, 4(6). https://doi.org/10.1037/0278-7393.4.6.592
2. Roediger, H. L., and Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science*, 17(3). https://doi.org/10.1111/j.1467-9280.2006.01693.x
3. Roediger, H. L., and Butler, A. C. (2011). The critical role of retrieval practice in long-term retention. *Trends in Cognitive Sciences*, 15(1). https://doi.org/10.1016/j.tics.2010.09.003
4. Karpicke, J. D., and Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science*, 331(6018). https://doi.org/10.1126/science.1199327
5. Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., and Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest*, 14(1). https://doi.org/10.1177/1529100612453266
6. Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., and Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3). https://doi.org/10.1037/0033-2909.132.3.354
7. Rohrer, D., and Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science*, 35. https://doi.org/10.1007/s11251-007-9015-8
8. Kapur, M. (2008). Productive failure. *Cognition and Instruction*, 26(3). https://doi.org/10.1080/07370000802212669
9. Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2). https://doi.org/10.1207/s15516709cog1202_4
10. Alfieri, L., Brooks, P. J., Aldrich, N. J., and Tenenbaum, H. R. (2011). Does discovery-based instruction enhance learning? *Journal of Educational Psychology*, 103(1). https://doi.org/10.1037/a0021017
11. Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., and Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*, 122(26). https://doi.org/10.1073/pnas.2422633122
12. Shen, J. H., and Tamkin, A. (2026). How AI Impacts Skill Formation. arXiv:2601.20245. https://arxiv.org/abs/2601.20245 ; Anthropic summary (29 Jan 2026): https://www.anthropic.com/research/AI-assistance-coding-skills
13. Kestin, G., Miller, K., Klales, A., Milbourne, T., and Ponti, G. (2025). AI tutoring outperforms in-class active learning: an RCT introducing a novel research-based design in an authentic educational setting. *Scientific Reports*, 15. https://doi.org/10.1038/s41598-025-97652-6
14. Kalai, A. T., Nachum, O., Vempala, S. S., and Zhang, E. (2025). Why Language Models Hallucinate. arXiv:2509.04664. https://arxiv.org/abs/2509.04664
15. Spracklen, J., et al. (2025). We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs. USENIX Security 2025. https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen
16. Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., and Zou, J. (2023). GPT detectors are biased against non-native English writers. arXiv:2304.02819. https://arxiv.org/abs/2304.02819
17. Canva Engineering (11 Jun 2025). Yes, you can use AI in our interviews. https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/ ; Anthropic, Guidance on candidates' AI usage. https://www.anthropic.com/candidate-ai-guidance
18. Ministry of Electronics and IT, India. Data protection framework (DPDP Act 2023 and Rules). https://www.meity.gov.in/data-protection-framework
19. TechCrunch (2 May 2023). Samsung bans use of generative AI tools like ChatGPT after April internal data leak. https://techcrunch.com/2023/05/02/samsung-bans-use-of-generative-ai-tools-like-chatgpt-after-april-internal-data-leak/

_Last reviewed: 2026-10_
