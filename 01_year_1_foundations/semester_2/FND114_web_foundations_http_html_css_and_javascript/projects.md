# FND114 · Labs and projects

Labs use plain HTML, CSS and JavaScript, plus Node.js 24 for servers; frameworks are not allowed until Lab 10. Every page you submit must pass the W3C validator and axe-core with zero violations unless a lab says otherwise. Test in at least two browser engines (for example Chromium and Firefox).

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Network tracing | `traceroute`, `dig +trace`, `curl -v` against three sites; label every DNS step and every round trip | An annotated report with raw output | 3 h |
| 2 · Raw HTTP | A Python socket client, then a tiny file server with correct `Content-Type`, `Content-Length`, 404 and ETag/304 | Code and request/response transcripts | 4 h |
| 3 · TLS, CORS and cookies | `openssl s_client` on two sites; reproduce and correctly fix a CORS error; set and inspect cookie flags; the introductory XSS and CSRF labs in PortSwigger Web Security Academy | A report with screenshots of solved labs | 4 h |
| 4 · Semantic page | A train timetable page with a real data table and a booking form | The page and its validator output | 3 h |
| 5 · Accessibility audit | Audit a page with axe, keyboard only and NVDA; fix at least 10 issues | An audit report (issue, WCAG criterion, fix) and the diff | 4 h |
| 6 · Layout challenges | Five layouts: card grid with `auto-fit`, dashboard with named areas, sticky footer, responsive navigation, media object | Live pages and screenshots at 320, 768 and 1440 px | 5 h |
| 7 · Event loop and closures | 15 ordering predictions; `once`, `memoize`, `debounce` with tests | Answers with explanations, code, tests | 3 h |
| 8 · DOM to-do app | Keyboard-operable to-do list with one delegated listener and `localStorage` | The app and a screen-reader test log | 5 h |
| 9 · `fetch` with failures | Forecast page with an 8-second timeout, one retry with backoff, and loading, empty and error states | The app and screenshots of each state, produced with DevTools throttling | 4 h |
| 10 · Tiny backend | The same API twice: `node:http`, then Hono or Express 5 with Zod validation and SQLite | Repository with 20 passing `node:test` tests in CI | 6 h |

## Projects

### P1 · Accessible personal portfolio (L1, ~6 hours)

**Real-world inspiration.** The [GOV.UK Design System](https://design-system.service.gov.uk/) publishes accessibility-tested patterns for public services, and India's [GIGW 3.0](https://guidelines.india.gov.in/) sets WCAG-based rules for government sites. Both show that plain, well-structured HTML works for everyone.

**What to build.** A hand-written site with no framework and no required JavaScript: home, projects, résumé and contact pages, with dark mode and a print stylesheet for the résumé.

**Acceptance criteria**
- Zero W3C validator errors and zero axe violations on every page.
- A recorded keyboard-only walkthrough in which every control is reachable and focus is always visible.
- Lighthouse scores of at least 95 for Accessibility, Best Practices and SEO, and at least 90 for Performance on the mobile profile.
- Text contrast of at least 4.5:1 in both light and dark modes, checked with a contrast tool.
- No horizontal scroll at 320, 768 or 1440 px, and `prefers-reduced-motion` respected.
- Deployed on GitHub Pages over HTTPS with a custom 404 page.

**Common pitfalls.**
- Choosing headings for their visual size, which breaks the outline that screen-reader users navigate by.
- Removing focus outlines with `outline: none` and adding nothing in their place.
- Dark-mode colours that pass contrast for body text but fail for links or focus rings.
- Images without `width` and `height` attributes, which cause layout shift.

**Stretch goals.** A Hindi version with `lang="hi"` and correct font fallbacks; a custom domain.

**What it proves to an employer.** You write semantic, accessible front-end code from first principles, which many framework-only developers cannot.

### P2 · Weather and air-quality dashboard for Indian cities (L2, ~15 hours)

**Real-world inspiration.** Public air-quality dashboards are among the most-checked pages in Indian cities in winter. [Open-Meteo](https://open-meteo.com/en/docs) offers free [geocoding](https://open-meteo.com/en/docs/geocoding-api), forecast and [air-quality](https://open-meteo.com/en/docs/air-quality-api) APIs that need no key.

**What to build.** A vanilla JavaScript app built from ES modules. A user searches for a city and sees current PM2.5 and PM10 readings and a 7-day forecast, and can compare up to three cities. Label which AQI scale, if any, you display, because India's national AQI uses its own breakpoints. Charts need a data-table alternative. Cache responses in memory with a TTL, and keep the app state in the URL (`?city=Pune`).

**Data notes.** The air-quality API returns hourly `pm2_5` and `pm10` concentrations, and also `european_aqi` and `us_aqi` indices, which are not India's national AQI. Set the forecast API's `timezone` parameter so hours display in IST, and show the data timestamp so users can tell fresh data from cached data.

**Acceptance criteria**
- Every request has an 8-second timeout through `AbortController` and one retry with backoff, for network errors only. Loading, empty and error states each look different, shown with DevTools offline mode and throttling.
- No API data is ever passed to `innerHTML`, enforced by a CI check.
- Every control works by keyboard; axe reports zero violations; every chart has a table alternative.
- CLS below 0.1 and INP below 200 ms in your measurements; at most 50 KB of uncompressed JavaScript, with no framework.
- Back and forward buttons restore earlier states through the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API).
- Data-transformation functions have unit tests run by `node:test` or Vitest.

**Common pitfalls.**
- Treating 4xx and 5xx responses as success, because `fetch` rejects only on network failure.
- Race conditions: a slow response for an old search overwrites a newer one. Fix it with one `AbortController` per search.
- Charts that carry meaning only through colour.
- Caching an error response as if it were data.

**Stretch goals.** A [service worker](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) that shows the last viewed data offline; Hindi labels; an installable web app manifest.

**What it proves to an employer.** You can build a fast, resilient, accessible client against real APIs without leaning on a framework.

### P3 · Full-stack link shortener with click analytics (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Link shorteners power campaigns, SMS messages and QR codes everywhere. [Dub](https://github.com/dubinc/dub) is an open-source link-management platform whose code you can read for reference.

**What to build.** A Hono or Express 5 backend with SQLite and a lightweight front end. Users sign up and log in with session cookies, with passwords hashed using argon2id or bcrypt as the [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) recommends. They create short links with optional custom aliases. The redirect uses 301 or 302, and the README explains the choice. Clicks are counted by day and referrer domain. Deploy it on a custom domain over HTTPS.

**Acceptance criteria**
- **API.** Documented endpoints return the right status codes (201, 301/302, 400, 401, 404, 409, 429), and at least 40 automated tests pass in CI.
- **Security.**
  - Cookies are `Secure`, `HttpOnly` and `SameSite=Lax`, and every state-changing form has a CSRF token.
  - The CSP has no `'unsafe-inline'` scripts, and HSTS is enabled.
  - Every query is parameterised, with a CI check that rejects SQL built from strings.
  - Only `http` and `https` targets are accepted.
  - Mozilla Observatory gives a grade of A− or better.
- **Performance.** Server-side redirect p95 is under 50 ms over 1,000 requests, measured with [autocannon](https://github.com/mcollina/autocannon) on your deployment, with the method documented.
- **Accessibility.** Zero axe violations, and the whole journey (sign up, create a link, view stats) works by keyboard alone.
- **Operations.** A health endpoint, structured logs and a documented backup of the SQLite file. The README has an architecture diagram and a short threat model: five threats, each with its mitigation.
- **AI review.** If you used AI-generated code, the log shows the review checklist and at least three issues you found and fixed.

**Suggested milestones.**
- Week 12: the API with its tests.
- Week 13: accounts, security headers and the first deployment.
- Week 14: analytics, the performance run and the threat model.
- Week 15: polish and demo.

Each milestone ends with a tagged release and a short changelog entry.

**Common pitfalls.**
- An open redirect: you validate the short link's target but follow an unchecked `next=` parameter after login.
- Recording clicks synchronously inside the redirect, which makes every redirect slow.
- Session identifiers stored in `localStorage` instead of `HttpOnly` cookies.
- Stack traces returned to users in production error responses.
- Forgetting that SQLite allows one writer at a time. Analytics writes then block redirects under load; use WAL mode and batch the inserts.

**Stretch goals.** QR codes; link expiry; caching redirects at the edge with `Cache-Control`; a blocklist check for known-malicious target domains.

**What it proves to an employer.** You can ship a secure, tested, deployed full-stack product on your own and explain every request it handles.

## Feeds into

- The frontend major: [FE301](../../../03_majors/frontend_engineering/year_3/FE301_modern_javascript_and_typescript_in_depth/README.md) (JavaScript and TypeScript in depth), [FE302](../../../03_majors/frontend_engineering/year_3/FE302_react_and_component_architecture/README.md) (React), [FE303](../../../03_majors/frontend_engineering/year_3/FE303_css_design_systems_and_accessibility/README.md) (design systems and accessibility), [FE304](../../../03_majors/frontend_engineering/year_3/FE304_browser_internals_and_web_performance/README.md) (browser internals and performance) and [FE305](../../../03_majors/frontend_engineering/year_3/FE305_frontend_testing_and_tooling/README.md) (testing).
- [CS204 Computer Networks](../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md) goes deeper into TCP/IP, DNS and QUIC from Chapters 1–3.
- [CS213 Security Foundations](../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) builds on the defensive web-security material from Chapter 3 and P3.
- [BE301 API Design](../../../03_majors/backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md) extends the API work from Chapters 9–10.
- [FND115 Databases I](../FND115_databases_i_data_modeling_and_sql/README.md) supplies the SQL behind P3.
