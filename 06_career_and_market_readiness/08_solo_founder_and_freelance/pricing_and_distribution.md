# Pricing and distribution

| Goal | Time | Level | Back to |
|---|---|---|---|
| Set a price you can defend, collect payments in India and abroad, compute unit economics (including AI costs), and find a repeatable channel to the first 100 customers | ~2 weeks of the LCH502 founder track | L3 → L4 | [Founder hub](README.md) |

Most technical founders underprice and over-build, then wait for users to arrive. Users do not arrive by themselves. Pricing and distribution are design problems with experiments, like any other.

## 1. Pricing principles

1. **Price from value, bounded by cost.** Three numbers matter: your **cost to serve** one customer (the floor), what the problem **costs the customer** today (the ceiling), and what **alternatives** charge (the reference).
2. **Charge early.** Payment is the strongest evidence of demand. Free users tell you less than paying ones.
3. **Business customers pay for outcomes.** Time saved, revenue gained, risk avoided. A tool that saves an accountant four hours a week is worth a meaningful share of four hours of their pay. Patrick McKenzie's essay *Don't Call Yourself A Programmer* makes the case for describing work in terms of business value rather than code ([kalzumeus.com, 2011](https://www.kalzumeus.com/2011/10/28/dont-call-yourself-a-programmer/)).
4. **Simple beats clever.** Two or three plans with one clear difference between them.
5. **You can raise prices later** for new customers. Keep early customers on their old price for a while ("grandfathering") to reward trust.

## 2. Pricing models

| Model | Works for | Watch out for |
|---|---|---|
| One-time purchase | Templates, desktop tools, courses, UI kits | Revenue stops unless you keep selling; updates are unpaid |
| Lifetime deal | A cash boost early | You carry the cost of serving forever. The case of Tailwind Labs, which sold lifetime licences, shows the risk when new sales fall ([case studies](case_studies.md)) |
| Subscription (monthly, annual) | Software used continuously | Churn; annual plans with a discount (commonly around two months free) improve cash flow |
| Per seat | Team tools | Customers share logins; growth depends on team size |
| Usage-based | APIs, infrastructure, AI features with variable cost | Unpredictable bills worry customers; add caps and alerts |
| Tiered (good, better, best) | Products with clear feature or usage levels | Too many tiers confuse buyers |
| Freemium | Products with low marginal cost and viral or team spread | Most users never pay; free usage still costs you |
| Free trial (7–30 days) | Products where value shows quickly | Ask for payment details or not: fewer trials, more paying, or the reverse; test it |
| Services plus software | Early B2B products | Hard to scale if the service part dominates |

## 3. Unit economics, including AI costs

If your product calls a paid AI model, each user action has a real marginal cost. Work it out before setting a price.

**Illustrative calculation** (made-up prices; use your provider's current price list):

| Item | Value |
|---|---|
| Average AI calls per active user per month | 300 |
| Average tokens per call (input + output) | 4,000 |
| Blended model price | $3 per million tokens |
| AI cost per user per month | 300 × 4,000 × $3 / 1,000,000 = **$3.60** |
| Hosting, database, email, monitoring per user | $0.80 |
| Payment fees (assume ~3% of a $15 price) | $0.45 |
| **Cost to serve** | **$4.85** |
| Price | $15/month |
| **Gross margin** | (15 − 4.85) / 15 = **68%** |

Ways to protect margin: cache repeated results, use smaller models for easy steps and route only hard cases to large ones, cap usage per plan, and charge heavy users more. Watch the top 5% of users by cost every week.

**SaaS formulas.**

| Metric | Formula |
|---|---|
| MRR (monthly recurring revenue) | Sum of monthly subscription revenue (annual plans ÷ 12) |
| Churn rate (monthly) | Customers lost in the month ÷ customers at the start of the month |
| Customer lifetime (months) | ≈ 1 ÷ monthly churn |
| LTV (lifetime value) | Average revenue per customer per month × gross margin × lifetime |
| CAC (customer acquisition cost) | Sales and marketing spend ÷ new customers in the period |
| CAC payback (months) | CAC ÷ (monthly revenue per customer × gross margin) |

Example (illustrative): $15/month, 68% margin, 5% monthly churn → lifetime ≈ 20 months → LTV ≈ 15 × 0.68 × 20 = $204. If CAC is $60, payback is 60 ÷ (15 × 0.68) ≈ 6 months.

## 4. India and global pricing

- **Purchasing power differs.** Many products charge Indian customers less than US customers, either with separate rupee plans or regional pricing. Expect lower prices but often a larger number of potential customers.
- **State whether prices include GST.** Indian consumers generally expect the price they see to be the price they pay; business quotes usually show GST separately. Once registered for GST, your invoices must show it correctly ([India basics](india_company_basics.md#5-gst)).
- **Selling to customers abroad** from India is usually an export of services; see [receiving foreign payments](india_company_basics.md#7-receiving-foreign-payments) for GST and banking rules.
- **Currency.** Price global plans in US dollars or euros; price Indian plans in rupees.

## 5. Pricing experiments

1. **Ask for money in the first conversation** about the product ("It's ₹1,500 a month; would you like to start a pilot?"). Note who says yes, who negotiates, who disappears.
2. **Test price on new cohorts**, not on existing customers: show a different price to new visitors for two to four weeks and compare conversion and **revenue per visitor**, not conversion alone.
3. **Interview people who did not buy.** "What would have made this an easy yes?" The answer is often not price.
4. **Raise prices when** most prospects accept without hesitation, or when you are too busy to serve everyone well.

## 6. Collecting payments

**India.**

| Option | Notes |
|---|---|
| Payment aggregators authorised by the Reserve Bank of India (for example Razorpay, Cashfree, PayU) | Cards, UPI, net banking, wallets; subscriptions via card mandates or UPI AutoPay. Check onboarding requirements (business proof, bank account in the business's name, GST if applicable) and fees on each provider's site |
| UPI AutoPay and card e-mandates for subscriptions | Recurring payments under the RBI e-mandate framework; above certain amounts, each charge needs additional authentication by the customer (limits set by the RBI; check current values) |
| Bank transfer with invoice | Common for business customers |

**Selling abroad.**

| Option | Notes |
|---|---|
| Stripe | Stripe's support pages describe new Indian accounts as **invite-only**, with existing accounts still supported ([Stripe support](https://support.stripe.com/questions/stripe-accounts-are-invite-only-in-india); checked October 2026) |
| Merchant of record (for example Paddle, Lemon Squeezy) | The provider is the legal seller to your customer, collects and remits sales tax or VAT in other countries, and pays you out. Higher fees, much less tax work. Check whether they accept India-based sellers and how payouts reach you |
| PayPal, Payoneer, Wise and similar | Mostly for invoices to business clients; compare exchange-rate markups and whether you receive the inward-remittance documents your bank and tax filings need ([India basics](india_company_basics.md#7-receiving-foreign-payments)) |

**App stores.** Apple's App Store Small Business Program charges a 15% commission for eligible developers earning up to $1 million a year ([Apple](https://developer.apple.com/app-store/small-business-program/)); Google Play charges 15% on the first $1 million of a developer's annual earnings ([Google Play Console Help](https://support.google.com/googleplay/android-developer/answer/112622)). Check the current terms and regional exceptions.

## 7. Distribution

Weinberg and Mares's book *Traction* (2014) describes 19 channels and a "bullseye" method: brainstorm all channels, test the three most promising cheaply, then focus on the one that works ([book site](https://www.tractionbook.com/)). Common channels for small software businesses:

| Channel | Works when | First test |
|---|---|---|
| Communities where users already gather (forums, Slack and Discord groups, Reddit, professional associations, WhatsApp groups) | You are a genuine member and follow the rules | Answer questions helpfully for two weeks; share the product only where allowed |
| Content and search (SEO) | People search for the problem by name | Five pages answering the exact questions from your interviews |
| Launch sites (Product Hunt, Hacker News "Show HN") | The product is usable without a sales call | One launch, following each site's rules ([Show HN guidelines](https://news.ycombinator.com/showhn.html)) |
| Marketplaces and integrations (Shopify App Store, Chrome Web Store, Slack, Atlassian, Zoho) | Your product extends a platform your users already use | Publish a minimal integration |
| Direct outreach (sales) | Business customers with clear pain and budget | 30 personalised messages to the people from your interviews and their referrals |
| Open source | Developers are the users; a free core builds trust | Publish the core; a hosted or paid tier for teams ([OSS models](open_source_business_models.md)) |
| Partnerships | Someone already serves your customer (accountants, agencies, consultants) | Offer a referral share to three partners |
| Paid ads | You know your conversion rate and LTV | Only after a channel works organically; small budget with a clear CAC target |

**Do things that don't scale at first.** Recruit users one by one, onboard them personally, and fix their problems by hand; Paul Graham's essay argues that this is how most successful startups began ([*Do Things that Don't Scale*, 2013](https://paulgraham.com/ds.html)).

**Rules for outreach.** Respect anti-spam rules: in the US, commercial email must follow CAN-SPAM; in the EU, consent rules for marketing apply; in India, commercial SMS and calls are regulated by TRAI's Telecom Commercial Communications Customer Preference Regulations, 2018, and personal data handling falls under the DPDP Act ([India basics](india_company_basics.md#8-data-protection)). Never buy contact lists.

## 8. The first ten customers: a playbook

1. Go back to everyone you interviewed; offer the MVP to the ones with the strongest pain.
2. Onboard each one on a call; watch them use it; fix what blocks them that week.
3. Ask each satisfied customer for one introduction.
4. Write one case study with their permission ("reconciliation from 5 hours to 30 minutes").
5. Post it where your users gather; follow up personally with everyone who responds.
6. Keep a sheet with every conversation, objection and outcome (the [pipeline tracker](../07_job_search_offers_negotiation/applications_pipeline.md) works with "customer" in place of "company").

## 9. Practice

1. Fill in the unit-economics table for your MVP with real provider prices; find the price at which margin reaches 70%.
2. Choose three channels with the bullseye method and run a one-week test of each with a written success threshold.
3. Write a pricing page with two plans and ask five target customers which they would choose and why.

## Sources

All checked October 2026.

1. Patrick McKenzie. *Don't Call Yourself A Programmer, And Other Career Advice* (2011). https://www.kalzumeus.com/2011/10/28/dont-call-yourself-a-programmer/
2. Paul Graham. *Do Things that Don't Scale* (2013). https://paulgraham.com/ds.html
3. Gabriel Weinberg and Justin Mares. *Traction* (2014). https://www.tractionbook.com/
4. Stripe Support. *Stripe accounts are invite-only in India*. https://support.stripe.com/questions/stripe-accounts-are-invite-only-in-india
5. Apple. *App Store Small Business Program*. https://developer.apple.com/app-store/small-business-program/
6. Google Play Console Help. *Service fees*. https://support.google.com/googleplay/android-developer/answer/112622
7. Hacker News. *Show HN guidelines*. https://news.ycombinator.com/showhn.html

_Last reviewed: 2026-10_
