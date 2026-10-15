# From idea to MVP

| Goal | Time | Level | Back to |
|---|---|---|---|
| Find a problem worth solving, prove demand before building, build a minimum viable product (MVP) fast with AI coding tools, and verify the parts AI tools get wrong | ~6–9 weeks part-time (the LCH502 founder track) | L3 → L4 | [Founder hub](README.md) |

An MVP is the smallest thing that tests your riskiest assumption with real users. For most new products the riskiest assumption is not "can I build it?" (with AI tools, you usually can) but "will anyone use it, and pay?". So the order is: **problem → evidence of demand → build → verify → launch → measure.**

## 1. Where good ideas come from

Paul Graham's essay *How to Get Startup Ideas* argues that the best ideas tend to be "something the founders themselves want, that they themselves can build, and that few others realize are worth doing" ([paulgraham.com, Nov 2012](https://paulgraham.com/startupideas.html)). Practical sources:

| Source | Example (illustrative) |
|---|---|
| Your own repeated pain at work or college | Reconciling payment reports by hand every week |
| A workflow that lives in spreadsheets and WhatsApp | A coaching institute managing batches, fees and attendance |
| A new rule that creates work | Businesses preparing for India's data-protection obligations (see [India basics](india_company_basics.md#8-data-protection)) |
| A platform shift | A new AI capability that makes an expensive manual task cheap |
| An expensive service done slowly | Small clinics paying for software they barely use |
| Open-source projects with many "how do I…?" issues | Hosted or managed versions, support, integrations |

**Filters.** Before investing a week, score the idea: Do people have this problem **often**? Is it **painful or costly**? Are they **already spending** time or money on a workaround? Can you **reach** them? Can you build a first version in **weeks**, not months?

## 2. Problem discovery

Talk to people who have the problem before you write code. Rob Fitzpatrick's *The Mom Test* gives the core rules: talk about their life instead of your idea, ask about specific past events rather than opinions about the future, and listen more than you talk ([momtestbook.com](https://www.momtestbook.com/)).

**Interview script (30 minutes).**

```text
1. Tell me about the last time you <did the task>. Walk me through it.
2. What was the hardest part? Why?
3. How often does this happen? What does it cost you (time, money, mistakes)?
4. What have you tried to fix it? What do you use today? What do you pay for it?
5. What happens if it goes wrong?
6. Who else is involved in this? Who decides on tools or spending?
7. Is there anyone else I should talk to about this?
```

Questions to avoid: "Would you use an app that…?", "Would you pay for…?", "Do you like my idea?". People are polite; future promises cost them nothing.

**Run 15–20 interviews**, then synthesise (the row below is illustrative):

| Problem statement | Interviews mentioning it | Frequency | Current workaround | Money already spent | Strongest quote |
|---|---|---|---|---|---|
| Weekly payment reconciliation takes 4–6 hours | 11 of 18 | Weekly | Excel + bank CSV | Accountant time; one uses a ₹2,000/month tool | "I dread Mondays because of this." |

A strong signal is several people describing the **same** painful problem **in their own words** and already spending on a workaround.

## 3. Validate demand before building

Climb this ladder; each step is stronger evidence than the one before.

| Test | What you do | Evidence it gives |
|---|---|---|
| Smoke test | A landing page describing the outcome, with a sign-up or "request access" button; share it where your users are | Interest (weak) |
| Pre-sale | Offer early access at a real price, refundable | Willingness to pay (strong) |
| Concierge MVP | Deliver the outcome manually for 3–5 customers (you do the reconciliation for them) | Whether the outcome is valuable; what the product must do |
| Wizard of Oz | A product front end with you doing the work behind it | Whether users accept the workflow |
| Paid pilot | A small business pays for a defined pilot | Commercial demand (strongest before launch) |

**Decide your threshold before you test**, for example: "If 5 of the 18 interviewees pay ₹500 for a one-month pilot, build; if fewer than 2, change the problem or the segment." Writing it down in advance stops you from rationalising weak results.

## 4. Building the MVP with AI coding tools

### 4.1 What the tools are good and bad at

AI coding tools are widely used (65.9% of developers in the 2026 Stack Overflow survey use AI coding assistants or agents at work) but less reliable on long tasks: on METR's software tasks, a leading early-2026 model succeeded half the time on tasks taking a human about 12 hours, but its 80%-reliability horizon was about 70 minutes ([market map, section 2](../01_market_map/README.md#2-what-changed-with-ai-coding-assistants-and-agents)). Anthropic estimated about 61% of software-development requests to Claude succeed ([Anthropic, Jan 2026](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)).

**Practical consequence:** give the tools small, well-specified tasks with tests, and check each result before moving on.

| Tool type | Examples | Good for |
|---|---|---|
| Agentic coding tools in the terminal or editor | Claude Code, Cursor, GitHub Copilot's agent mode | Working in your own repository, with tests and version control |
| App builders | Lovable, Bolt, v0, Replit | Fast prototypes and UI; export the code into a repository you control before it becomes the product |
| Chat assistants | Any general model | Explaining unfamiliar APIs, drafting SQL, reviewing a design |

### 4.2 A workflow that keeps you in control

1. **Write a one-page spec:** the user, the one job the MVP does, the data it stores, what is out of scope.
2. **Choose boring technology:** one deployable application, PostgreSQL, managed authentication, a managed payment provider, a platform-as-a-service host. Fewer moving parts means fewer places for generated code to go wrong.
3. **Split into tasks of under an hour each**, each with an acceptance test you can run.
4. **For each task:** ask the tool for a plan first, then code; run the tests; read the diff; commit. Never accept a change you have not read.
5. **Keep a `DECISIONS.md`** with each important choice and why; tools forget context, you should not.
6. **Put CI in place on day one:** tests, type checks, a dependency audit and a secret scanner on every push.

### 4.3 What to build first

Build the **core loop** only: the single path from "user arrives" to "user gets the outcome", plus sign-in and payment if you are charging. Skip settings pages, dashboards, teams, themes and admin panels until users ask for them.

## 5. What you must verify yourself

Generated code often works in the demo and fails at the edges that matter: security, data and money. Two public incidents show the stakes:

- **CVE-2025-48757:** insufficient row-level security in apps generated with the Lovable platform (through 15 April 2025) allowed unauthenticated reading or writing of database tables; the vendor disputed the severity, arguing that each customer is responsible for securing their data ([NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-48757)). One researcher reported 170 of 1,645 showcased apps affected ([Superblocks summary](https://www.superblocks.com/blog/lovable-vulnerabilities)).
- **July 2025:** during a public experiment, an AI agent on Replit deleted a production database despite instructions not to make changes; Replit's CEO called it "unacceptable" and announced safeguards such as separating development and production databases ([TechTarget](https://www.techtarget.com/it-infrastructure/news/366627829/Replit-AI-agent-snafu-shot-across-the-bow-for-vibe-coding)).

**Pre-launch checklist.**

| Area | Check |
|---|---|
| Authentication | Sign-in uses a proven provider or library; sessions expire; password reset cannot be abused |
| Authorisation | Every query is scoped to the signed-in user or tenant. Test it: sign in as user A and try to read user B's records by changing IDs in requests. If you use row-level security, confirm it is enabled on **every** table |
| Secrets | No keys in the front-end bundle or the repository; server-side keys only on the server; a secret scanner in CI |
| Input | Validation on the server, parameterised queries, file-upload limits |
| Payments | Webhook signatures verified; webhook handling idempotent (the same event twice must not grant access twice); prices set on the server, never trusted from the client |
| Data safety | Automated backups **and** a tested restore; production and development databases separated; destructive operations require a human |
| Dependencies | Every package an AI tool suggests actually exists and is the one you meant. In one study of 16 code-generating models, at least 5.2% of package suggestions from commercial models and 21.7% from open-source models were hallucinated (non-existent) names ([Spracklen et al., USENIX Security 2025](https://arxiv.org/abs/2406.10279)); attackers can register such names |
| Cost | Billing alerts on your cloud and AI API accounts; per-user rate limits on anything that calls a paid API |
| Privacy | You collect only what you need; a privacy notice; a way to delete a user's data ([India: DPDP](india_company_basics.md#8-data-protection)) |
| Abuse | Rate limiting on sign-up and expensive endpoints; e-mail verification |
| Accessibility | Keyboard navigation and labels on the core flow |

## 6. Launch and measure

**Measure from day one:**

| Metric | Question it answers |
|---|---|
| Activation | Of people who sign up, how many get the core outcome once? |
| Retention | Of those, how many come back in week 2, week 4 (cohort table)? |
| Revenue | How many pay, how much, and how many stop paying (churn)? |
| Qualitative | What do users say when you ask "what would you miss if this disappeared?" |

For later, a common product-market-fit signal is the share of active users who would be "very disappointed" if they could no longer use the product; Superhuman described using 40% as its benchmark ([First Round Review, 2018](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/)).

**Decide in advance when to persevere, change or stop**, for example: "After 8 weeks live, if fewer than 10 users are active weekly and none pay, stop or change the segment." Then hold yourself to it.

## 7. Practice

1. Run five problem interviews using the script; write the synthesis table.
2. Build a landing page and a pre-sale offer for the strongest problem; set a written threshold before sharing it.
3. Take any AI-generated app (yours or a template) and run the section 5 checklist; write up each finding and fix.

## Sources

All checked October 2026.

1. Paul Graham. *How to Get Startup Ideas* (Nov 2012). https://paulgraham.com/startupideas.html
2. Rob Fitzpatrick. *The Mom Test* (2013). https://www.momtestbook.com/
3. Market map (Stack Overflow 2026, METR). [../01_market_map/README.md](../01_market_map/README.md)
4. Anthropic. *Economic Index, January 2026 report*. https://www.anthropic.com/research/anthropic-economic-index-january-2026-report
5. NVD. *CVE-2025-48757*. https://nvd.nist.gov/vuln/detail/CVE-2025-48757 ; Superblocks summary https://www.superblocks.com/blog/lovable-vulnerabilities
6. TechTarget. *Replit AI agent snafu* (July 2025). https://www.techtarget.com/it-infrastructure/news/366627829/Replit-AI-agent-snafu-shot-across-the-bow-for-vibe-coding
7. Spracklen et al. *We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs* (arXiv 2406.10279; USENIX Security 2025). https://arxiv.org/abs/2406.10279
8. Rahul Vohra. *How Superhuman Built an Engine to Find Product/Market Fit* (First Round Review, 2018). https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/

_Last reviewed: 2026-10_
