# LinkedIn and a credible professional presence

| Goal | Time | Level | Back to |
|---|---|---|---|
| A profile recruiters can find and trust, a posting habit that shows real work, and outreach people answer | ~3 hours to set up, 1–2 hours a week after | L2 → L4 | [Portfolio hub](README.md) |

"Personal brand" here means one thing: **when someone in your field searches for you or meets you, they quickly find accurate evidence of what you do well.** It does not mean becoming an influencer. The aim is credibility, not reach.

## 1. The profile

Recruiters search LinkedIn by title, skills, location and employer, so the profile must be accurate and consistent with your resume. Interviewers open it to check that the person matches the resume.

| Field | What to write | Example (illustrative) |
|---|---|---|
| Photo | A clear, recent photo of your face with plain background | — |
| Headline | Target role · strongest proof · domain. Not "Student at X" alone | "Backend engineer (Go, PostgreSQL) · built a crash-safe ledger, 1,500 tx/s · OpenTelemetry contributor" |
| Location | Real city; add "open to remote" in About if true | "Bengaluru, Karnataka, India" |
| Custom URL | linkedin.com/in/firstname-lastname | — |
| About | 4–6 short lines (template below) | — |
| Featured | 2–4 items: flagship repository, best case study, a talk or post | — |
| Experience | Same roles and dates as the resume; 2–3 bullets each | — |
| Projects | Flagship and one other, with links | — |
| Skills | 10–15 you can be tested on; put the most relevant first | — |
| Recommendations | One or two from a manager, maintainer or teacher who saw your work | — |

**About template.**

```text
I build backend systems and measure them. Recently: a double-entry ledger that stays correct
under 50 forced crashes (1,500 tx/s, write-up linked below), and 6 merged pull requests to
OpenTelemetry Go contrib.

Interested in: payments infrastructure, reliability, observability.
Looking for: backend / platform engineering roles from July 2028, India or remote.

Code: github.com/yourname · Writing: yoursite.dev · Email: you@example.com
```

**"Open to Work".** LinkedIn lets you signal you are looking either to recruiters only or to all members (the green photo frame). Recruiters-only is the safer default while employed. The public frame is reasonable when you are a student or between jobs; it is a personal choice, and neither setting replaces direct outreach.

**Verification.** LinkedIn offers verification of identity and workplace for many members. A verified workplace on a recruiter's profile is one of several signals that a message is genuine (see section 5).

## 2. Posting: what credible looks like

Post when you have something real to show. Good posts for students and early-career engineers:

| Post | Shape | Why it works |
|---|---|---|
| Project result | Problem, one diagram or chart, the measured result, link to code | It is evidence, not opinion |
| Debugging lesson | Symptom, cause, fix, one lesson; link the longer write-up | Shows how you think |
| Paper or talk notes | The claim, what you tried yourself, what surprised you | Shows learning beyond the syllabus |
| Open-source milestone | What the pull request fixed and what you learned from review | Shows collaboration |
| Internship or co-op wrap-up | Two things you built, one thing you learned about working in a team (within confidentiality) | Useful to the next student |

**Cadence.** One good post every two to four weeks beats daily filler. Comment thoughtfully on posts by engineers in your field; a specific, correct comment often gets more useful attention than a post.

**What reads as spam.**

- Engagement bait ("Agree?", "Comment YES for the PDF"), polls with no purpose.
- Generic AI-written posts and carousels with no personal evidence.
- Certificates of every short online course. Post only the ones tied to a project you built with that knowledge.
- Tagging people who were not involved to borrow their reach.
- Reposting someone's work or diagram without credit.
- Inflated titles ("Founder & CEO" of a solo side project with no users, "AI expert" after one course).

## 3. Messaging and connecting

**Connection requests.** Add a short note that says why. Keep it brief (under about 200 characters fits the current limits on free accounts; limits vary by account type and change over time).

```text
Hi Meera, I read your post on moving order events to Kafka and tried the outbox pattern in
my own ledger project. Would like to follow your work.
```

**Asking for advice (not a job).**

```text
Hi Meera, I'm a final-year CS student building backend projects (ledger with exactly-once
posting: <link>). I'm deciding between payments and observability teams. Could I ask you
two questions over a 15-minute call, any day next week? If not, no problem at all.
```

**Asking for a referral** is covered with templates in [search strategy](../07_job_search_offers_negotiation/search_strategy.md#2-referrals).

**Rules.**

1. One message and one polite follow-up after a week. Then stop.
2. Make the ask small and specific; offer an easy "no".
3. Never send the same paste to fifty people; personalise the first line with something real.
4. Thank people and tell them what happened later. It is rare and remembered.

## 4. Beyond LinkedIn

| Place | Use it for |
|---|---|
| GitHub | Code, contributions, profile README ([guide](github_profile.md)) |
| A personal site on your own domain | Case studies and posts you own permanently ([guide](case_studies_and_writing.md)) |
| Competitive programming profiles (Codeforces, CodeChef, LeetCode) | Rating as a signal for DSA-heavy loops, if strong |
| Kaggle | Data science competition results and notebooks |
| Stack Overflow, project forums, Discord or Slack communities of open-source projects | Answering questions in your area |
| X, Bluesky, Mastodon | Following researchers and maintainers; optional for posting |

Use the same name, photo and one-line description everywhere so people can connect the profiles.

## 5. Safety: fake jobs and recruiter scams

Fake job offers are common, and job seekers are a target. Warning signs:

- You are asked to **pay** for anything: registration, training, a "security deposit", equipment, a background check.
- An "offer" arrives without any real interview, or after a chat-only interview.
- The recruiter uses a personal email or messaging app instead of a company domain, or the company domain is a near-copy of the real one.
- "Task-based" jobs that pay small amounts for likes or reviews, then ask you to "invest" to unlock larger payments.
- Pressure to decide in hours, or requests for bank details, Aadhaar, PAN or passport copies before any formal offer.

Check by finding the job on the company's official careers page and contacting the company through its official site. In India, report cyber fraud at [cybercrime.gov.in](https://cybercrime.gov.in/) or the national cybercrime helpline **1930**. Elsewhere, report to the platform and to your national fraud authority.

## 6. Checklist

- [ ] Headline names your target role and one proof.
- [ ] About section: what you build, recent evidence, what you are looking for, links.
- [ ] Featured: flagship repository and best write-up.
- [ ] Experience and dates match your resume exactly.
- [ ] One or two recommendations from people who saw your work.
- [ ] Same name and photo on GitHub and your site.

## 7. Practice

1. Rewrite your headline three ways; ask two engineers in your target role which one tells them most.
2. Draft a post about your best project in under 150 words with one image and one link. Cut any sentence that is not evidence.
3. Write five personalised advice requests to people in your target role, send them over a week, and log replies in your [pipeline tracker](../07_job_search_offers_negotiation/applications_pipeline.md).

## Sources

All checked October 2026.

1. National Cyber Crime Reporting Portal (Government of India). https://cybercrime.gov.in/
2. LinkedIn Help Center (profile, Open to Work and verification features). https://www.linkedin.com/help/linkedin

_Last reviewed: 2026-10_
