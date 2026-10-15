# Frequently asked questions

| Questions | Facts checked | Related pages |
|---|---|---|
| 20 | October 2026 | [How it works](01_how_this_university_works.md) · [Choose your major](02_choose_your_major.md) · [Market map](../06_career_and_market_readiness/01_market_map/README.md) |

Honest answers to the questions people ask before committing years of their life. Where a fact matters, it links to its source. Where something cannot be verified, it says so. Answers marked **Analysis** are interpretation.

## Contents

**Degree, time and money:** [1](#1-is-this-a-degree) · [2](#2-should-i-skip-or-leave-college-and-do-this-instead) · [3](#3-how-long-will-it-take-me) · [4](#4-what-does-it-cost) · [5](#5-i-have-only-a-phone-or-an-old-laptop-can-i-still-do-this)
**Jobs and AI:** [6](#6-will-ai-take-the-jobs-this-prepares-me-for) · [7](#7-why-learn-to-code-when-ai-writes-code) · [8](#8-which-major-pays-best) · [9](#9-do-i-need-a-masters-or-phd) · [10](#10-can-i-get-a-job-abroad-with-this)
**India-specific:** [11](#11-what-about-gate) · [12](#12-how-do-i-get-hired-without-campus-placement-off-campus) · [13](#13-can-i-combine-this-with-nptel-swayam-or-an-online-degree)
**Studying:** [14](#14-i-am-not-good-at-maths-is-this-for-me) · [15](#15-i-come-from-a-non-cs-background-can-i-start) · [16](#16-can-i-use-chatgpt-claude-or-copilot-for-the-work) · [17](#17-are-certifications-worth-it) · [18](#18-how-do-i-prove-what-i-learned-without-grades) · [19](#19-is-it-legal-to-learn-hacking-here) · [20](#20-what-if-i-fall-behind-or-get-stuck)

---

## Degree, time and money

### 1. Is this a degree?

No. It is a curriculum, not an accredited institution. Nobody here grants degrees, credits recognised by universities, or certificates. What you build is a **portfolio of evidence**: projects, gate notes, code reviews, write-ups. Employers, clients and graduate schools can inspect it, and interviewers can ask you to repeat any of it live.

Some employers are dropping degree requirements: in the World Economic Forum's 2025 survey, 30% of employers in India said they plan to remove degree requirements, against 19% globally ([WEF Future of Jobs 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)). That still leaves most employers keeping them. See question 2.

### 2. Should I skip or leave college and do this instead?

**If you can get or finish a degree, do it, and use this curriculum alongside it.** A degree still unlocks things a portfolio cannot:

- **Eligibility rules.** Many large employers' fresher hiring drives in India list specific degrees and academic cut-offs; GATE requires you to be in at least the third year of an undergraduate degree or to have completed one (see question 11).
- **Visas.** For example, the US H-1B "specialty occupation" route requires "a bachelor's or higher degree in a directly related specific specialty (or its equivalent)" ([USCIS](https://www.uscis.gov/working-in-the-united-states/h-1b-specialty-occupations)).
- **Graduate school and public-sector jobs**, which almost always require a degree.

If a full-time degree is out of reach (money, location, family duties), consider a low-cost or online degree while you study here; see question 13. **Analysis:** the strongest position is a degree *plus* the evidence this curriculum produces. The weakest is a degree with nothing to show beyond marks.

### 3. How long will it take me?

At full-time pace (about 40–48 hours a week) the whole path is 5 years, as at a university. At about 20 hours a week, Years 1–2 take roughly 3–4 calendar years, and job-readiness in one major (Years 1–2, your major's Year 3 and the career labs, about 3,700 hours) takes roughly 4–5 years. If you already know some of the material, the [placement check](05_placement_check.md) lets you skip it. The arithmetic is in [how this university works](01_how_this_university_works.md#4-pacing-full-time-and-part-time).

Be suspicious of anyone promising job-readiness in a few weeks. The hours in each course come from what its mastery gate requires.

### 4. What does it cost?

The content is free. Real costs:

| Item | Cost | Can you avoid it? |
|---|---|---|
| A computer | The largest cost | Partly: browser-based options in [set up your lab](04_set_up_your_lab.md#8-low-budget-and-phone-only-options) |
| Internet | Monthly data | Download big files once, on Wi-Fi |
| Software | Free: every tool in the lab setup has a free option | Yes |
| Cloud | Free tiers and credits, with a budget alarm | Mostly; delete resources after each lab |
| Textbooks | Most recommended texts are free online (see the [free resource index](../07_library/free_resource_index.md)) | Mostly |
| Certifications | From about US$100 to several thousand per exam | Yes: none are required ([certifications map](../07_library/certifications_map.md)) |
| Electronics kit (Embedded major only) | A microcontroller board and basic instruments | Simulators cover early labs |

### 5. I have only a phone or an old laptop. Can I still do this?

Much of Years 1–2, yes. GitHub Codespaces gives a full Linux environment in a browser (120 compute hours a month on a free personal account, used faster on larger machines), Google Colab runs Python notebooks for free, and Termux gives a terminal on Android. Heavy work (Docker, local LLMs, large builds) needs a real computer or a cloud machine. Details and limits: [set up your lab, section 8](04_set_up_your_lab.md#8-low-budget-and-phone-only-options).

## Jobs and AI

### 6. Will AI take the jobs this prepares me for?

Some tasks, yes; whole fields, the evidence says not now. From the [market map](../06_career_and_market_readiness/01_market_map/README.md):

- **Entry level is under real pressure.** US software developers aged 22–25 were close to 20% below their late-2022 employment peak by September 2025, while older developers kept growing, and the declines concentrate where AI automates tasks rather than augments them ([Brynjolfsson, Chandar and Chen, Nov 2025](https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf)).
- **The wider labour market is not broadly disrupted (yet).** The Yale Budget Lab found no "discernible disruption" in the US occupational mix since ChatGPT ([Yale Budget Lab, Oct 2025](https://budgetlab.yale.edu/research/evaluating-impact-ai-labor-market-current-state-affairs)).
- **Big fields still grow.** The US BLS projects software developers +10%, information security analysts +21% and data scientists +35% for 2025–35, with computer programmers −7% ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/home.htm)).
- **Reliability lags capability.** On METR's software tasks, a February 2026 model succeeded half the time on tasks taking an expert about 12 hours, but its 80%-reliability horizon was about 70 minutes ([METR](https://metr.org/time-horizons/)). Someone must judge which outputs are right.

**Analysis.** The tasks that used to train juniors (boilerplate, simple UI, first-draft SQL) are the most automated. This curriculum responds by building judgement early: verification, debugging, system design, production work and real projects. See the [AI impact matrix](../06_career_and_market_readiness/01_market_map/ai_impact_matrix.md) for your field.

### 7. Why learn to code when AI writes code?

Because someone has to tell whether the code is right, and that takes the skill you would be skipping.

- Only 6.6% of developers trust AI output for important decisions, and 48.0% trust it only when they can easily verify it ([Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data)).
- In a 2026 randomised experiment, engineers who learned a new library with AI help scored 50% on a follow-up quiz against 67% for those who coded by hand, and were not significantly faster ([Anthropic](https://www.anthropic.com/research/AI-assistance-coding-skills)).
- Some employers now test exactly this: Canva's AI-assisted interviews ask whether candidates "can identify and fix issues in AI-generated code" ([Canva](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)). Others ban AI in interviews ([Anthropic](https://www.anthropic.com/candidate-ai-guidance)), so you need both modes.

The [AI-native study protocol](03_ai_native_study_protocol.md) shows how to use AI without losing the skill.

### 8. Which major pays best?

There is no reliable single answer, and salary sources disagree sharply. For "software engineer" in India, Levels.fyi shows a median total compensation of ₹30.6 lakh (self-reported, mostly product companies and multinationals), while Payscale shows an average base salary of ₹8.1 lakh across the whole market ([market map, section 6](../06_career_and_market_readiness/01_market_map/README.md#6-india)). The difference is about who is counted and what pay includes.

**Analysis.** Within any major, pay depends far more on the employer type (product company, global capability centre, services firm, startup), your depth, and your evidence than on the major's name. Choose by the work you want to do every day ([choose your major](02_choose_your_major.md)); the role pages show pay sources for each field.

### 9. Do I need a master's or PhD?

For most engineering roles, no. For research roles, often yes: the US BLS lists a master's degree as the typical entry education for computer and information research scientists ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm)), and industry deep-learning research is concentrated and highly competitive ([DLR market page](../06_career_and_market_readiness/01_market_map/roles/DLR_deep_learning.md)). Year 5 of this curriculum (research methods, reproducing papers, a thesis) is designed to prepare you for that application, not to replace it.

### 10. Can I get a job abroad with this?

Your skills travel; your paperwork may not. Work visas in many countries ask for a degree or a formally assessed equivalent, as in the US H-1B example in question 2. Rules differ by country and change often; check the official immigration site of the country you are targeting. Remote work for foreign employers avoids visas but brings its own tax and contract questions. **Analysis:** a public portfolio and open-source record help most here, because they are visible to employers anywhere.

## India-specific

### 11. What about GATE?

The **Graduate Aptitude Test in Engineering** is used for admission to master's and doctoral programmes (often with financial assistance at Ministry of Education-supported institutions) and by several public-sector undertakings for recruitment. Facts for **GATE 2027** (organised by IIT Madras; checked October 2026):

- **Exam dates:** 6, 7, 13, 14, 20 and 21 February 2027; the score is valid for three years from the result ([IIT Madras press release, 20 Jul 2026](https://www.iitm.ac.in/happenings/press-releases-and-coverages/iit-madras-announces-dates-syllabus-revision-new-paper)).
- **Relevant papers:** CS (Computer Science and Information Technology) and DA (Data Science and Artificial Intelligence) ([papers and syllabus](https://gate2027.iitm.ac.in/exam_papers_and_syllabus)).
- **Eligibility:** you must be in the third or a higher year of an undergraduate degree, or have completed a government-approved degree. B.Sc., B.A., B.Com. and BCA students qualify from the third year; no age limit is stated ([eligibility](https://gate2027.iitm.ac.in/eligibility_criteria)). Self-study alone, without a degree in progress or completed, does not make you eligible.

**How this curriculum helps.** Years 1–2 cover most of the core areas a CS-style exam tests: discrete mathematics, data structures and algorithms, computer architecture, operating systems, networks, databases, compilers, probability and linear algebra. Compare the official syllabus with the course list before relying on it, and add timed practice with past papers: GATE rewards speed and accuracy on short problems, which is a different skill from building projects.

### 12. How do I get hired without campus placement (off-campus)?

Off-campus routes that work, roughly in order of reliability:

1. **Referrals** from people who have seen your work: open-source maintainers, former colleagues, members of your study circle who got hired first.
2. **Direct applications with evidence.** Link a project that matches the job, with a README, tests and measured results, at the top of your résumé.
3. **Company hiring drives and tests** run by large employers for freshers. Eligibility usually lists specific degrees, graduation years and academic cut-offs; read each drive's official notice on the company's own careers site before you prepare.
4. **Internships and apprenticeships**, including unpaid open-source programmes, which give the production experience junior candidates now need.
5. **Startups and global capability centres (GCCs)**, which the market map identifies as places where depth pays most ([market map, section 6](../06_career_and_market_readiness/01_market_map/README.md#6-india)).

NASSCOM expects Indian tech hiring to "shift from volume to skill mix" in FY27 ([NASSCOM 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026)). **Analysis:** mass hiring of generalist freshers is a weaker route than it was; specific, demonstrable skills are a stronger one.

**Protect yourself.** Apply only through official company sites or verified job boards, never pay a "registration", "training" or "security deposit" fee to get a job, and verify any offer letter with the company directly.

### 13. Can I combine this with NPTEL, SWAYAM or an online degree?

Yes, and it is often a good idea.

- **SWAYAM** hosts free courses from Indian institutions (including NPTEL courses), with optional proctored exams for a certificate. UGC regulations advise universities to identify SWAYAM courses whose credits can be transferred to students' academic records ([SWAYAM](https://swayam.gov.in/about)); check with your own university before counting on it.
- **Online degrees** from Indian institutions exist at low cost compared with residential programmes, for example IIT Madras's online programmes in [Data Science and Applications](https://study.iitm.ac.in/ds/) and [Electronic Systems](https://study.iitm.ac.in/es/). Check the current eligibility, fees and recognition on the official pages.
- Map each formal course onto the matching course here, and use this curriculum's labs, projects and gates to go deeper than the exam requires.

## Studying

### 14. I am not good at maths. Is this for me?

Year 1 assumes only school arithmetic and algebra, and teaches the rest from the start: discrete mathematics ([FND103](../01_year_1_foundations/semester_1/FND103_discrete_mathematics_for_computing/README.md)), linear algebra and calculus ([FND113](../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md)) and probability and statistics ([FND116](../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md)), each checked with code. How much more maths you need depends on the major: a lot for Deep Learning, Data Science, ML Engineering and Theory; less for Frontend, QA, Cloud or Networking, though probability and logic stay useful everywhere. Many people who "were bad at maths" at school were taught it without a reason to care; computing gives the reason.

### 15. I come from a non-CS background. Can I start?

Yes. Year 1 assumes no programming. Commerce, arts, science and other engineering backgrounds all bring something useful: domain knowledge (finance, healthcare, manufacturing) is exactly what the market map calls hard to automate ([market map, section 8](../06_career_and_market_readiness/01_market_map/README.md#8-skills-that-compound-and-skills-being-commoditised)). Be realistic about hiring filters that ask for specific degrees (question 2), and look at roles where your background is an advantage, such as data analysis in your industry or forward deployed engineering.

### 16. Can I use ChatGPT, Claude or Copilot for the work?

Yes, in the right way. The default rules: in the first six weeks of Year 1, AI only as a tutor that gives hints; after that, AI allowed for building with every use logged in `AI_LOG.md`; at least one AI-off drill per course every week; mastery gates and exams AI-off unless the course says otherwise. The reasons and a daily routine are in the [AI-native study protocol](03_ai_native_study_protocol.md).

### 17. Are certifications worth it?

Sometimes, as a filter; rarely as proof of skill. Hands-on, performance-based exams (for example CKA for Kubernetes) carry more weight than multiple-choice ones, and some fields (networking, security, cloud partners and services firms) use certifications as screens more than others. None is required by this curriculum. The [certifications map](../07_library/certifications_map.md) rates the main ones per major and says what to do instead when one is not worth it.

### 18. How do I prove what I learned without grades?

Keep a public progress repository with one row per course, linked to evidence (projects, gate notes, recordings, reviewed pull requests) and to who reviewed each gate. The template and rules are in [how this university works](01_how_this_university_works.md#5-self-certifying-your-progress). In interviews, offer to repeat a gate task live; few candidates can.

### 19. Is it legal to learn hacking here?

Security is taught for defence and for authorised testing only. Testing systems you do not own, without written permission, is a crime in India and most other countries, whatever your intent. Practise on systems you own or on platforms built for it, such as [PortSwigger Web Security Academy](https://portswigger.net/web-security), [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/), [TryHackMe](https://tryhackme.com/), [Hack The Box](https://www.hackthebox.com/), [OverTheWire](https://overthewire.org/wargames/) and [picoCTF](https://picoctf.org/). [CS213](../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) covers what Indian and international law permit. The Ethical Hacking and Offensive Security major is coming later; until then, the [Cybersecurity Defense](../03_majors/cybersecurity_defense/README.md) and [Security Architecture](../03_majors/security_architecture/README.md) majors are the security paths.

### 20. What if I fall behind or get stuck?

It happens to almost everyone, and it is fixable.

- **Stuck on a concept for more than two sessions:** go back to its prerequisite course's gate and check you can still pass it; most "stuck" moments are a missing foundation.
- **Falling behind on hours:** drop to the part-time pairing for the semester ([Year 1](../01_year_1_foundations/README.md#suggested-weekly-timetable), [Year 2](../02_year_2_core_computer_science/README.md#part-time-path-1525-hours-a-week)) rather than skipping labs.
- **Failed a gate:** record what failed, practise that part, and retake with a new task after a few days. Retakes are normal.
- **Losing motivation:** join or start a study circle ([how it works, section 6](01_how_this_university_works.md#6-studying-in-a-group-or-with-a-mentor)), and finish one small project you can show someone this week.
- **Found an error in the curriculum:** open an issue in the repository. Corrections are welcome.

## Sources

All checked October 2026.

- World Economic Forum. *Future of Jobs Report 2025*. https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- USCIS. *H-1B Specialty Occupations*. https://www.uscis.gov/working-in-the-united-states/h-1b-specialty-occupations
- Brynjolfsson, Chandar, Chen. *Canaries in the Coal Mine?* (13 Nov 2025). https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf
- Yale Budget Lab. *Evaluating the Impact of AI on the Labor Market* (1 Oct 2025). https://budgetlab.yale.edu/research/evaluating-impact-ai-labor-market-current-state-affairs
- US Bureau of Labor Statistics. *Occupational Outlook Handbook* (2025–35 projections). https://www.bls.gov/ooh/computer-and-information-technology/home.htm
- METR. *Time horizons*. https://metr.org/time-horizons/
- Stack Overflow. *2026 Developer Survey: AI*. https://survey.stackoverflow.co/2026/ai/data
- Anthropic. *How AI assistance impacts the formation of coding skills* (29 Jan 2026). https://www.anthropic.com/research/AI-assistance-coding-skills ; *Guidance on candidates' AI usage*. https://www.anthropic.com/candidate-ai-guidance
- Canva Engineering. *Yes, you can use AI in our interviews* (11 Jun 2025). https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/
- IIT Madras. *GATE 2027 dates, syllabus revision and new paper* (20 Jul 2026). https://www.iitm.ac.in/happenings/press-releases-and-coverages/iit-madras-announces-dates-syllabus-revision-new-paper ; GATE 2027 eligibility and papers. https://gate2027.iitm.ac.in/eligibility_criteria ; https://gate2027.iitm.ac.in/exam_papers_and_syllabus
- NASSCOM. *Technology Sector in India: Strategic Review 2026*. https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026
- SWAYAM. *About*. https://swayam.gov.in/about
- IIT Madras online degree programmes. https://study.iitm.ac.in/ds/ ; https://study.iitm.ac.in/es/
- Salary figures: Levels.fyi and Payscale as cited in the [market map](../06_career_and_market_readiness/01_market_map/README.md#6-india).

_Last reviewed: 2026-10_
