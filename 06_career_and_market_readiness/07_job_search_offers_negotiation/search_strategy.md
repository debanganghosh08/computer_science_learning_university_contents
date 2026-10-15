# Search strategy: where jobs actually come from

| Goal | Time | Level | Back to |
|---|---|---|---|
| A target list, a referral and outreach habit, the right job boards for India and global roles, and a calendar that matches hiring seasons | Set-up ~8 hours; then part of the [weekly routine](applications_pipeline.md#4-the-weekly-routine) | L2 → L4 | [Job search hub](README.md) |

## 1. Build a target list

Applying to whatever appears in a feed is the least effective search. Decide where you want to work, then find a way in.

**Kinds of employer** (pay and learning differ a lot; see [offers](offers_and_negotiation.md#6-comparing-employers)):

| Type | Examples of where to find them |
|---|---|
| Product companies (Indian and global) | Engineering blogs, app stores, the tools you use |
| Global capability centres (GCCs): in-house technology centres of foreign firms in India | Company careers pages filtered to Indian cities; news coverage of new centres |
| Startups | [YC company directory](https://www.ycombinator.com/companies) (filter by location and "hiring"), [Wellfound](https://wellfound.com/), funding news |
| IT services and consulting firms | Careers pages, national hiring tests (section 6) |
| Open-source companies | Organisations behind projects you contribute to |
| Research labs and universities | Lab pages, paper author affiliations |
| Government and public sector | [National Career Service portal](https://www.ncs.gov.in/), official recruitment notifications |

**The list.** Aim for 60–100 organisations in three tiers: about 20% "reach", 50% "target", 30% "likely". For each, record:

| Company | Type | Tier | Team or product you want | Why you (one line of evidence) | Contacts | Channel | Status |
|---|---|---|---|---|---|---|---|
| Example Payments | Product | Target | Ledger / reconciliation | Built ledger-lite (exactly-once posting) | 2 alumni, 1 OSS reviewer | Referral | Asked 12 Oct |

The "why you" column forces you to match evidence to employers. If you cannot fill it, either the company is a poor fit or you need a project that fits.

## 2. Referrals

**Why.** In data from nine large firms in three industries (call centres, trucking and high-tech), referred applicants were more likely to be hired and, once hired, less likely to quit than non-referred applicants ([Burks, Cowgill, Hoffman and Housman, *Quarterly Journal of Economics*, 2015](https://doi.org/10.1093/qje/qjv010)). Employers trust referrals because someone they know vouches for you. For you, a referral usually means a human reads your application.

**Whom to ask, in order of strength:**

1. People who have worked with you: internship managers and teammates, open-source maintainers who reviewed your code, teaching staff who supervised your project.
2. Alumni of your college at the company (LinkedIn's alumni tool on your school's page lets you filter by company and role).
3. People you have had a real conversation with: meetups, conferences, hackathons, communities.
4. Strangers: do not ask for a referral directly. Ask for advice first (template in [LinkedIn guide](../06_portfolio_resume_github/linkedin_and_personal_brand.md#3-messaging-and-connecting)); a referral may follow if the conversation goes well.

**How to ask.** Make it easy: give the job link or ID, your resume, and a short paragraph they can paste into the internal referral form.

```text
Subject: Referral for Backend Engineer (Job ID 12345)?

Hi Karan,

Hope the payments migration went well. I'm applying for Backend Engineer I on the ledger
team (job ID 12345, link). Would you be comfortable referring me?

Why I think I fit: I built ledger-lite, a double-entry ledger with exactly-once posting that
held 1,500 tx/s with zero duplicates across 50 forced crashes (write-up: <link>), and I have
6 merged pull requests in OpenTelemetry Go contrib.

Resume attached. A blurb you can paste:
"Rahul built a crash-safe ledger service with measured throughput and contributes to
OpenTelemetry. I worked with him during his internship at Example Fintech."

If you'd rather not, no problem at all, and thanks either way.
Rahul
```

Rules: only ask people who can honestly say something about you; never misstate how you know them; tell them the outcome; return the favour later.

## 3. Direct outreach to hiring managers and engineers

When you have no referral, write to the person who owns the problem: the hiring manager, the team lead, or at a startup, the founder or CTO.

**Email to a hiring manager.**

```text
Subject: Ledger engineer: built exactly-once posting, 1,500 tx/s

Hi Ms Iyer,

I saw the Backend Engineer opening on your reconciliation team. I've spent the last three
months building a double-entry ledger with an outbox and idempotent consumers; it held
1,500 postings/s and lost or duplicated nothing across 50 forced crashes. Design doc and
load-test report: <link>.

I've applied through the careers page (ID 12345). If you're open to it, I'd value 15 minutes
to hear what the team's hardest reconciliation problem is right now.

Thanks,
Rahul Menon · github.com/rmenon · +91 90000 00000
```

**Message to a startup founder.** Startups move fast and value proof of initiative. Show you used the product.

```text
Hi Ananya, I used <product> to <task> and noticed exports time out above ~5,000 rows. I
reproduced it and wrote a two-page note on a streaming export approach: <link>. I'm a final-
year CS student looking for a backend role from June; if you're hiring, I'd love to talk.
```

**Rules.**

- One message plus one follow-up after 5–7 working days. Then stop.
- Lead with evidence relevant to *their* product, not with your life story.
- Keep it under 150 words. Put links, not attachments, in a first cold email.
- Find addresses through public sources only (company sites, talks, papers, public profiles). Do not buy contact lists or guess dozens of addresses.
- Expect a low reply rate and do not take silence personally. Track it ([pipeline](applications_pipeline.md)).

## 4. Job boards and portals

Job boards are useful for **discovery**. Applying cold through them has the lowest response rate of any channel (**analysis**, consistent with the referral evidence above), so use them to find openings, then look for a referral or a direct contact for each one you care about.

**India.**

| Portal | Best for | Notes |
|---|---|---|
| [Naukri](https://www.naukri.com/) | Broad market, services firms, GCCs, experienced hires | Recruiters also search the profile database, so complete the structured fields (skills, notice period, CTC) accurately |
| [foundit](https://www.foundit.in/) (formerly Monster India) | Broad market | Same profile-search model |
| [LinkedIn Jobs](https://www.linkedin.com/jobs/) | Product companies, GCCs, startups, global roles | Use filters for experience level and "posted in the past week" |
| [Instahyre](https://www.instahyre.com/) | Product companies and startups | Recruiter-initiated matching |
| [Cutshort](https://cutshort.io/) | Startups, tech roles | — |
| [Wellfound](https://wellfound.com/) (formerly AngelList Talent) | Startups in India and abroad | Salary and equity often shown on the listing |
| [Hirist](https://www.hirist.tech/) | Tech roles | — |
| [Internshala](https://internshala.com/) | Internships and fresher jobs | Check stipend and company credibility carefully |
| [Unstop](https://unstop.com/) | Hiring challenges, hackathons, competitions run by employers | Good for off-campus visibility |
| [National Career Service](https://www.ncs.gov.in/) | Government-run job portal | Includes public-sector and private listings |

**Global.**

| Source | Best for |
|---|---|
| [LinkedIn Jobs](https://www.linkedin.com/jobs/), [Indeed](https://www.indeed.com/) | Broad coverage |
| [Hacker News "Ask HN: Who is hiring?"](https://news.ycombinator.com/submitted?id=whoishiring) | Monthly thread, posted on the first weekday of each month; many startups, many remote roles, often written by engineers |
| [Work at a Startup](https://www.workatastartup.com/) | Y Combinator companies |
| [Wellfound](https://wellfound.com/) | Startups worldwide |
| [RemoteOK](https://remoteok.com/), [We Work Remotely](https://weworkremotely.com/), [Remotive](https://remotive.com/) | Remote roles (check each listing's location restrictions) |
| Company careers pages | The source of truth. Many are hosted on Greenhouse (`boards.greenhouse.io`), Lever (`jobs.lever.co`) or Workday; a web search such as `site:jobs.lever.co "backend" "India"` finds openings that never reach aggregators |

**Avoid** paying anyone to "guarantee" a job, and avoid automated mass-apply bots: they produce low-quality applications, and platforms such as LinkedIn prohibit bots and automated access in their terms ([LinkedIn User Agreement](https://www.linkedin.com/legal/user-agreement)). See [job-scam warning signs](../06_portfolio_resume_github/linkedin_and_personal_brand.md#5-safety-fake-jobs-and-recruiter-scams).

## 5. Remote and global roles

**Four ways to work for a foreign employer:**

| Model | How it works | What to check |
|---|---|---|
| Employee of the company's Indian entity (including GCCs) | Normal Indian employment contract, payroll, PF | Same as any Indian offer ([offers](offers_and_negotiation.md)) |
| Employer of record (EOR) | A third party (for example, Deel or Remote) employs you in India on the foreign company's behalf | Who is your legal employer, benefits, notice, equipment |
| Independent contractor | You invoice the foreign company; no PF, gratuity or paid leave unless negotiated | Tax, GST on export of services, receiving payments: see [India company basics](../08_solo_founder_and_freelance/india_company_basics.md) and [freelancing](../08_solo_founder_and_freelance/freelancing_and_consulting.md) |
| Relocation with a work visa | The employer sponsors a visa | Visa rules, timeline, cost, what happens if the job ends |

**Remote-role checklist.** Required time-zone overlap (for example, "4 hours with US Eastern" means evenings in India); where they can legally employ people ("remote, US only" means the US); currency and payment method; who provides equipment; contractor or employee; how performance is judged without office visibility.

**US work visas: recent changes (check current USCIS guidance before relying on these).**

- In September 2025, Presidential Proclamation 10973 introduced a $100,000 payment for certain new H-1B petitions filed on or after 21 September 2025, applying mainly to beneficiaries outside the US; change-of-status cases inside the US (for example, many F-1 students) were generally reported as not covered ([law-firm summary, hlc.com](https://hlc.com/en/publications/trump-administration-imposes-100000-fee-for-new-h1b-petitions-and-proposes-giving-priority); status as of October 2026 unconfirmed).
- A Department of Homeland Security final rule, reported effective 27 February 2026, weights the H-1B cap lottery by the wage level offered, from one entry at Level I up to four at Level IV ([Adams and Reese summary](https://www.adamsandreese.com/visa-viewpoint/the-new-h-1b-cap-weighted-lottery-final-rule-higher-wages-equal-better-odds)). Entry-level offers therefore have lower selection odds than before.
- If an H-1B job ends, US rules allow a grace period of up to 60 consecutive days, or until the end of the authorised validity period if sooner, to change status or find a new sponsor ([8 CFR 214.1(l)(2)](https://www.law.cornell.edu/cfr/text/8/214.1)). See [layoffs and setbacks](layoffs_and_setbacks.md).

Other countries (UK Skilled Worker, Germany's EU Blue Card, Canada's Express Entry, Australia's skilled visas) have their own salary thresholds and points rules that change often. Read the official government page for the exact year before planning around them.

## 6. Campus and off-campus hiring in India

**Campus placement.** The usual sequence is a pre-placement talk, an online assessment (aptitude, coding, sometimes AI-proctored), technical interviews and an HR round. Many colleges have rules such as "one offer per student" or tiers that stop you from applying after a first offer; read your placement cell's policy before the season, because it changes your strategy. An internship that converts into a **pre-placement offer (PPO)** is often the strongest campus outcome.

**Off-campus routes for freshers.**

| Route | What it is | Check |
|---|---|---|
| National hiring tests of large services firms | For example TCS National Qualifier Test (NQT), Infosys's HackWithInfy competition, Wipro's Elite National Talent Hunt, Cognizant's GenC programmes | Names, eligibility (often minimum marks in Class 10, 12 and degree) and formats change yearly; use only the official careers pages |
| Hiring challenges and hackathons | Employer-run contests on Unstop, HackerEarth and similar platforms; some product companies run annual challenges | Whether the contest actually leads to interviews; read the rules |
| Startup outreach | Direct messages to founders (section 3) | Pay, contract type, runway |
| Government schemes | [PM Internship Scheme](https://pminternship.mca.gov.in/) (internships with large companies; eligibility rules apply), graduate apprenticeships under [NATS](https://nats.education.gov.in/) | Eligibility on the official portal |
| Open-source programmes | GSoC, Outreachy, LFX ([open source](../06_portfolio_resume_github/open_source.md#5-funded-programmes-checked-october-2026)) | Dates |

**Service agreements.** Some employers ask freshers to sign a service agreement or training bond. Read [offers and negotiation](offers_and_negotiation.md#5-contract-clauses-to-read-before-signing) before signing.

## 7. Hiring seasons

These are commonly observed patterns, not measured data (**unconfirmed**; they vary by country, company and year):

| Market | Pattern |
|---|---|
| Indian campuses | Summer internships for pre-final-year students are often decided in the preceding autumn; final placements often start early in the final year |
| Indian off-campus and experienced hiring | Year-round; movement often rises after appraisal cycles, which many firms run around the April start of the financial year |
| US new-graduate and internship roles | Many large employers open applications in late summer and autumn for roles starting the next summer |
| Everywhere | Slower around year-end holidays; new budgets in the first quarter of a company's fiscal year |

Check postings trends rather than guessing: Indeed publishes daily postings indices by country and category ([Indeed Hiring Lab data](https://github.com/hiring-lab/job_postings_tracker); the [market map](../01_market_map/README.md) uses it).

## 8. AI on both sides of the search

- **Employers** use applicant tracking systems with search, knockout questions and, increasingly, AI ranking ([resume: ATS realities](../06_portfolio_resume_github/resume.md#5-applicant-tracking-systems-realities-and-myths)). Some interviews require AI and some forbid it ([market map, section 7](../01_market_map/README.md#7-what-hiring-managers-now-screen-for)).
- **Candidates** can now produce tailored applications in seconds, which raises application volume. **Analysis:** when everyone can generate a polished application, the signals that cannot be generated (a referral from someone who worked with you, a merged pull request, a working demo, a specific message about the employer's product) carry more weight. Spend your time there.
- **Good uses of AI in the search:** researching a company's stack from its engineering blog, preparing questions for a hiring manager, mock interviews, checking your messages for clarity.
- **Bad uses:** mass auto-applying, generating messages you did not read, inventing experience to match a job description.

## 9. Practice

1. Build a 60-company target list with the "why you" column filled for at least 30.
2. Send five advice requests and two referral requests this week using the templates; log each in the tracker.
3. Find ten openings on company careers pages that do not appear on LinkedIn or Naukri, using `site:` searches.

## Sources

All checked October 2026.

1. Burks, Cowgill, Hoffman, Housman. "The Value of Hiring through Employee Referrals". *Quarterly Journal of Economics* 130(2), 2015. https://doi.org/10.1093/qje/qjv010
2. hlc.com (law-firm publication). *Trump Administration Imposes $100,000 Fee for New H-1B Petitions* (Sept 2025). https://hlc.com/en/publications/trump-administration-imposes-100000-fee-for-new-h1b-petitions-and-proposes-giving-priority
3. Adams and Reese. *The New H-1B Cap Weighted Lottery Final Rule*. https://www.adamsandreese.com/visa-viewpoint/the-new-h-1b-cap-weighted-lottery-final-rule-higher-wages-equal-better-odds
4. 8 CFR 214.1(l)(2) (Cornell LII). https://www.law.cornell.edu/cfr/text/8/214.1
5. LinkedIn. *User Agreement*. https://www.linkedin.com/legal/user-agreement
6. Indeed Hiring Lab. *Job postings tracker*. https://github.com/hiring-lab/job_postings_tracker
7. Government portals: National Career Service https://www.ncs.gov.in/ ; PM Internship Scheme https://pminternship.mca.gov.in/ ; NATS https://nats.education.gov.in/
8. Y Combinator company directory https://www.ycombinator.com/companies ; Hacker News "Who is hiring" https://news.ycombinator.com/submitted?id=whoishiring

_Last reviewed: 2026-10_
