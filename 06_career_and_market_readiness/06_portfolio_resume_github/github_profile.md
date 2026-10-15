# GitHub profile and project repositories

| Goal | Time | Level | Back to |
|---|---|---|---|
| A GitHub profile where a reviewer finds your best three projects in ten seconds, can run each one in five minutes, and can see how you think | ~5 hours for the profile, ~2 hours per project README | L1 → L3 | [Portfolio hub](README.md) |

## 1. What a technical reviewer actually opens

Hiring managers and interviewers who look at GitHub usually do it in this order (**analysis**, based on common review practice; no reliable survey measures it):

1. Your **pinned repositories** and their one-line descriptions.
2. The **README** of the most relevant one: what it is, how to run it, what the results were.
3. The **code**: structure, tests, error handling, a few files in depth.
4. The **commit history and pull requests**: are commits meaningful, were there reviews, did you fix your own bugs?
5. Your **contributions to other people's projects**, which show you can work in code you did not write.

Everything below makes these five steps fast and convincing.

## 2. Profile README

GitHub shows a profile README when you have created a repository whose name matches your username, the repository is public, and it contains a non-empty `README.md` in its root ([GitHub Docs](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme)).

Keep it short. A reviewer wants orientation, not decoration.

```markdown
### Asha Rao · backend and distributed systems

Final-year CS student in Pune. I build and measure small storage and networking systems.

**Start here**
- [ledger-lite](https://github.com/asharao/ledger-lite): double-entry ledger with an outbox and
  exactly-once posting; load and chaos test reports in the repo.
- [rate-limiter-go](https://github.com/asharao/rate-limiter-go): token-bucket middleware,
  2,000 requests/s at p99 +1.8 ms.
- [Writing](https://asharao.dev/posts): how I found a race in token refill.

**Open source:** contributor to OpenTelemetry Go contrib (6 merged pull requests).

**Now:** learning Raft by implementing it from the paper (MIT 6.5840 labs).

Contact: asha.rao@example.com
```

Avoid walls of badges, auto-generated statistics cards and visitor counters. They do not show skill, they slow the page, and some third-party widgets stop working when their hosting changes.

## 3. Pinned repositories

You can pin up to six items. Pin **three to six**, ordered by relevance to the role you are applying for, and give each a one-line description that states what it is and one result:

| Weak description | Strong description |
|---|---|
| My project | Token-bucket rate limiter in Go; 2,000 req/s at p99 +1.8 ms (k6) |
| ML stuff | Churn model with time-split evaluation; AUC 0.81 vs 0.72 rule baseline |
| Website | Accessible recipe app; Lighthouse accessibility 100, WCAG 2.2 AA checklist in repo |

Archive or make private repositories you would not want to discuss: half-finished tutorials, copied assignments, forks you never changed.

## 4. The contribution graph: myths and facts

**Facts** ([GitHub Docs](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/why-are-my-contributions-not-showing-up-on-my-profile)):

- A commit counts only if it uses an email address connected to your GitHub account (or your GitHub `noreply` address).
- It must be on the repository's default branch or the `gh-pages` branch. Work on other branches counts once merged.
- Commits made in a fork do not count until they are merged into the parent repository through a pull request.
- New contributions can take up to 24 hours to appear.
- Issues, pull requests and reviews also count, and you can choose to show anonymised counts of private contributions on your profile.

**Myths.**

| Myth | Reality |
|---|---|
| "A full green graph proves skill" | It proves activity. A reviewer opening one repository learns more than from a year of squares |
| "You must commit every day" | Consistency matters for learning, but daily trivial commits look like gaming. Steady, meaningful work beats streaks |
| "Recruiters will not see private or work code" | True, so write case studies about work you cannot show ([guide](case_studies_and_writing.md)), and show private-contribution counts if you want the graph to reflect it |
| "Scripts that make backdated commits help" | They are easy to spot (identical messages, no content) and destroy trust if noticed |
| "Stars are what matter" | Stars measure attention, not quality. A project with 5 stars and excellent tests is better evidence than a starred awesome-list |

## 5. The project README

Use this structure for every pinned repository. A reviewer should be able to run the project in five minutes and understand the hardest decision in one.

```markdown
# ledger-lite

Double-entry ledger service with exactly-once posting semantics, built to learn how payment
systems avoid losing or duplicating money.

![architecture](docs/architecture.png)

## Why
Payment ledgers must never post a transaction twice or lose one, even when consumers crash.
This project tests one way to get there: a transactional outbox plus idempotent consumers.

## Quickstart
    git clone https://github.com/asharao/ledger-lite && cd ledger-lite
    docker compose up --build     # starts Postgres, Kafka, the service
    make test                     # unit + integration tests (needs Docker)

## Results
| Test | Setup | Result |
|---|---|---|
| Throughput | 3 nodes, laptop, k6 script in /bench | 1,500 postings/s, p95 38 ms |
| Crash safety | consumer killed mid-batch 50 times (/chaos) | 0 lost, 0 duplicated |

## Design decisions
- Outbox table instead of dual writes: avoids the write-to-DB-then-crash-before-publish gap.
  Rejected: distributed transactions (operational cost, few brokers support them well).
- Idempotency key = (account, client_txn_id); unique index enforces it.

## Limitations
- Single region. No multi-currency. Rebalancing storms not tested above 6 consumers.

## How AI tools were used
- Generated the first draft of the k6 script and the Docker Compose file; both reviewed and
  edited. Core posting logic and tests written by hand.

## License
MIT
```

Two sections make the biggest difference and are the most often missing: **Results** (measured, with the method) and **Design decisions** (with the alternative you rejected and why). The "How AI tools were used" section is optional but useful: it answers a question interviewers now ask, and it shows you know which parts you own.

## 6. Repository hygiene

| Practice | Minimum standard |
|---|---|
| One-command setup | `docker compose up`, `make dev` or a documented equivalent, tested from a fresh clone |
| Tests in CI | A GitHub Actions (or similar) workflow that runs on every push and pull request, with the badge only if it is green |
| Meaningful commits | Messages that say why ("Fix refund double-post when retry races commit"), not "update" or "final final" |
| Issues as a roadmap | Open issues for known limitations; it shows you know them |
| Releases | Tag versions that you mention in a resume or post |
| Dependencies | Lock files committed; automated update pull requests (for example, Dependabot) on long-lived projects |
| `.gitignore` | Build output, virtual environments, `.env` files excluded |

**Secrets.** Never commit API keys, passwords or tokens. GitHub offers secret scanning, including push protection that blocks some known secret formats before they are pushed ([GitHub Docs: secret scanning](https://docs.github.com/en/code-security/secret-scanning)). If a secret reaches a public repository, **revoke and rotate it first**; deleting the commit or rewriting history does not help once the value has been exposed, because copies may already exist.

## 7. Licences

If your repository has no licence, the default copyright rules apply: you keep all rights, and others may not legally reproduce, distribute or create derivative works from your code ([GitHub Docs: licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)). For portfolio projects you want people to reuse, add one.

| Licence | Others may | Main condition | Typical use |
|---|---|---|---|
| MIT | Use, modify, sell | Keep the copyright and licence notice | Small libraries, portfolio projects |
| Apache-2.0 | Same as MIT | Notice, state changes; includes an explicit patent grant | Libraries companies will adopt; many foundation projects |
| MPL-2.0 | Combine with closed code | Changes to MPL-licensed files stay open | Libraries that want file-level copyleft |
| GPL-3.0 | Use, modify, distribute | Distributed derivatives must be GPL with source | Applications that should stay free software |
| AGPL-3.0 | Same as GPL | Also applies when users interact with it over a network | Server software whose authors want hosted forks to share changes |

[choosealicense.com](https://choosealicense.com/) explains each in plain language. Two cautions:

- **Course assignments.** Your college's academic-integrity rules may forbid publishing solutions. Publish your own projects, not graded assignments, unless allowed.
- **Employer code.** Code written for an employer usually belongs to the employer under your contract. Never publish it; write a case study instead.

**AI-generated code and copyright.** The US Copyright Office's January 2025 report concluded that material generated by AI without sufficient human control over its expressive elements is not protected by copyright, while human-authored contributions and creative selection or arrangement can be ([US Copyright Office, *Copyright and Artificial Intelligence, Part 2: Copyrightability*](https://www.copyright.gov/ai/)). The law differs by country and is still developing. Practically: know which parts of your repository you wrote, and do not paste in AI output that reproduces someone else's licensed code.

## 8. Checklist

- [ ] Profile README with "start here" links to 3 projects.
- [ ] 3–6 pinned repositories, each with a one-line description containing a result.
- [ ] Each pinned README has Quickstart, Results, Design decisions, Limitations, License.
- [ ] Each pinned project builds from a fresh clone and CI is green.
- [ ] No secrets in history (run a scanner such as gitleaks or trufflehog on old repositories).
- [ ] Commit email linked to your account so contributions appear.
- [ ] Weak repositories archived or private.

## 9. Practice

1. **Fresh-clone test.** Ask a classmate to clone one of your projects on their machine and get it running using only the README. Time it and fix every step where they got stuck.
2. **Ten-second test.** Show your profile to someone for ten seconds, then close it. Ask what you build. If they cannot say, rewrite the profile README and pinned descriptions.
3. **Secret audit.** Run a secret scanner over all your public repositories. Rotate anything it finds, even if it looks expired.

## Sources

All checked October 2026.

1. GitHub Docs. *Managing your profile README*. https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme
2. GitHub Docs. *Why are my contributions not showing up on my profile?* https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/why-are-my-contributions-not-showing-up-on-my-profile
3. GitHub Docs. *Secret scanning*. https://docs.github.com/en/code-security/secret-scanning
4. GitHub Docs. *Licensing a repository*. https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
5. choosealicense.com. https://choosealicense.com/
6. US Copyright Office. *Copyright and Artificial Intelligence, Part 2: Copyrightability* (January 2025). https://www.copyright.gov/ai/

_Last reviewed: 2026-10_
