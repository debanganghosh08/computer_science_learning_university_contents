# FND114 · Web Foundations: HTTP, HTML, CSS and JavaScript

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 1 · 2 | 4 (≈ 120 hours) | L0 → L2 | [FND101](../../semester_1/FND101_programming_i_computational_thinking_with_python/README.md), [FND104](../../semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) | [FE301](../../../03_majors/frontend_engineering/year_3/FE301_modern_javascript_and_typescript_in_depth/README.md), [FE302](../../../03_majors/frontend_engineering/year_3/FE302_react_and_component_architecture/README.md), [FE303](../../../03_majors/frontend_engineering/year_3/FE303_css_design_systems_and_accessibility/README.md), [FE304](../../../03_majors/frontend_engineering/year_3/FE304_browser_internals_and_web_performance/README.md), [FE305](../../../03_majors/frontend_engineering/year_3/FE305_frontend_testing_and_tooling/README.md) |

## Why this course matters now

Almost every product, from a UPI app's help pages to a SaaS dashboard, is delivered over HTTP and rendered by a browser. AI app builders such as v0, Bolt and Lovable, and coding assistants, now generate whole sites in minutes. The evidence says the output still needs a skilled reviewer. Veracode's 2025 study found that 45% of AI-generated code samples introduced OWASP Top 10 flaws, and that cross-site scripting was left undefended in 86% of the relevant samples. WebAIM's 2026 scan found detectable WCAG failures on 95.9% of the top million home pages, and that is the web these models learned from. In India, the Supreme Court held in April 2025 that digital access is part of the right to life under Article 21. A person who understands the wire, the markup, the security model and the browser is the one who can ship, debug and fix what a generator produced.

## Learning outcomes

By the end you can:

1. Explain what happens from typing a URL to a rendered page (DNS, TCP or QUIC, TLS 1.3, HTTP, rendering), using evidence from `dig`, `curl -v` and DevTools.
2. Use HTTP semantics correctly: safe and idempotent methods, status codes, caching headers, cookies and CORS.
3. Write valid, semantic HTML that works by keyboard and screen reader and meets WCAG 2.2 AA on the pages you build.
4. Lay out responsive pages with the cascade, Flexbox and Grid from 320 px to 1440 px without a CSS framework.
5. Write modern JavaScript with closures, modules, promises and `async`/`await`, and predict event-loop ordering.
6. Change the DOM safely, handle events with delegation, and build pages that still work without JavaScript.
7. Call APIs with `fetch`, handling loading, errors, timeouts and aborts, and diagnose CORS failures.
8. Build, test and deploy a small Node.js backend with validation, SQLite persistence and security headers, on a custom domain over HTTPS.
9. Audit any page, including AI-generated ones, for accessibility, security headers and Core Web Vitals, and fix what you find.

## Chapters and lessons

### Chapter 1 · How the internet and DNS work (week 1)

| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Packets and routes | IPv4 and IPv6 addresses, routers, hops, NAT, latency vs bandwidth | `traceroute` to three sites hosted on different continents; explain the hop count and the latency jumps |
| 1.2 TCP, UDP and ports | Sockets, the three-way handshake, ports, why round trips dominate page load | Count the round trips before the first byte of a page using DevTools timing |
| 1.3 URLs | Scheme, host, port, path, query, fragment, percent-encoding; the `URL` API | Parse 10 tricky URLs with `new URL()` and Python's `urllib.parse`; explain any differences |
| 1.4 DNS resolution | Stub and recursive resolvers, root, TLD and authoritative servers (RFC 1034/1035); A, AAAA, CNAME, MX, TXT, NS; TTL | `dig +trace` your college's domain and draw the chain; change records on messwithdns.net and watch TTLs |
| 1.5 Seeing the traffic | `curl -v`, the DevTools Network panel, Wireshark on your own machine | Capture your own request to a local server and label every layer |

**Check your understanding:** (1) Why can a DNS change appear to "work for some people but not others" for hours? (2) Why does a site hosted far away feel slow even on fast broadband? (3) What do a CNAME and an A record each tell a resolver?

### Chapter 2 · HTTP (weeks 2–3)

| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Messages | Request line, status line, headers, body; HTTP/1.1 framing (RFC 9112) | Send a raw HTTP/1.1 request from a Python socket and parse the response by hand |
| 2.2 Semantics | GET, POST, PUT, PATCH, DELETE; safe and idempotent methods; status code classes (RFC 9110) | Choose the method and status code for 15 API scenarios and defend each choice |
| 2.3 Caching | `Cache-Control`, `ETag`, conditional requests, `304 Not Modified` (RFC 9111) | Make a server send ETags and show a 304 in DevTools |
| 2.4 Cookies and sessions | `Set-Cookie` with `Secure`, `HttpOnly`, `SameSite` (RFC 6265; its revision 6265bis is still a draft) | Build a toy login and inspect each cookie flag |
| 2.5 HTTP/2 and HTTP/3 | Multiplexing, head-of-line blocking, QUIC over UDP (RFC 9000, RFC 9114) | Compare the Protocol column for five sites and explain one difference you see |

**Check your understanding:** (1) Why must a retried POST not be assumed safe, and what makes PUT different? (2) A user sees stale data after a deploy. Which headers do you check first? (3) What problem does HTTP/3 solve that HTTP/2 could not?

### Chapter 3 · TLS and web security basics (week 4)

| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Why HTTPS | Confidentiality, integrity and authentication; the TLS 1.3 handshake at a high level (RFC 9846, which replaced RFC 8446 in July 2026) | `openssl s_client` to a site; record the protocol version, cipher suite and certificate chain |
| 3.2 Certificates and trust | Certificate authorities, chains, ACME and Let's Encrypt, expiry | Read a chain in the browser and explain why the root is not sent |
| 3.3 Same-origin policy and CORS | Origins, preflight requests, `Access-Control-Allow-*`; CORS protects users, not servers | Trigger a CORS error between two local ports, then fix it correctly |
| 3.4 XSS and CSRF from the defender's side | Output encoding, Content Security Policy, `SameSite` cookies, CSRF tokens; OWASP Top 10:2025 (Injection is A05) | Complete the introductory XSS and CSRF labs in PortSwigger Web Security Academy, a legal practice environment |

**Check your understanding:** (1) What exactly does the padlock prove, and what does it not prove? (2) Why does `Access-Control-Allow-Origin: *` not let a site read another site's logged-in data? (3) Why does `HttpOnly` reduce, but not remove, the damage of an XSS bug?

### Chapter 4 · HTML and semantics (week 5)

| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Document structure | Doctype, `<head>`, charset, viewport, `lang` (including `hi` and `en` on the same page) | A page that passes the W3C validator with zero errors |
| 4.2 Semantic elements | `header`, `nav`, `main`, `article`, `section`, `footer`; heading outline; lists; data tables with `caption` and `th scope` | Mark up a train timetable as a real data table |
| 4.3 Forms | Input types, `label`, `fieldset`/`legend`, built-in validation, `autocomplete` tokens | A booking form whose errors are announced to screen readers |
| 4.4 Images and links | `alt` text, `srcset`/`sizes`, meaningful link text | Write alt text for 10 images and fix 10 "click here" links |
| 4.5 Parsing into the DOM | How the HTML parser recovers from errors | Inspect the DOM of a malformed page and explain what the parser did |

**Check your understanding:** (1) Why is `<button>` better than `<div onclick>` even when they look the same? (2) When should an image have an empty `alt=""`? (3) What does a screen-reader user lose when headings are chosen for their size?

### Chapter 5 · Accessibility (week 6)

| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Standards and law | WCAG 2.2 principles (perceivable, operable, understandable, robust), levels A and AA; India's GIGW 3.0 (WCAG 2.1 AA), the RPwD Act 2016, *Rajive Raturi v. Union of India* (Nov 2024), *Pragya Prasun v. Union of India* (Apr 2025) | Summarise 10 WCAG criteria in one sentence each |
| 5.2 Keyboard and focus | Tab order, visible focus, skip links; new in 2.2: Focus Not Obscured and a 24×24 px minimum target size | Use three sites by keyboard only and log every failure |
| 5.3 Screen readers | NVDA (free, Windows), VoiceOver, TalkBack; accessible names; the first rule of ARIA (use native elements) | Complete a task on your own page with NVDA and the screen turned off |
| 5.4 Contrast and motion | 4.5:1 text contrast, `prefers-reduced-motion`, not using colour alone | Fix every contrast failure on a page |
| 5.5 Auditing | axe-core and Lighthouse catch only part of the problems, so manual testing is required | Audit a page: an automated report plus a manual report, then fix 10 issues |

**Check your understanding:** (1) Why can a page score 100 in Lighthouse accessibility and still be unusable by keyboard? (2) When does adding ARIA make a page worse? (3) Which 2.2 criterion would a sticky cookie banner most likely fail?

### Chapter 6 · CSS: cascade and layout (weeks 7–8)

| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The cascade | Origin, specificity, order, inheritance, `@layer` | Predict the winner in 12 rule conflicts, then check |
| 6.2 Box model and flow | `box-sizing`, display types, margin collapse, positioning, stacking context | Rebuild a card component to match a screenshot |
| 6.3 Flexbox | Main and cross axes, `flex-grow`/`shrink`/`basis`, alignment, wrapping | A wrapping navigation bar and a media object |
| 6.4 Grid | Tracks, `fr`, `minmax()`, `auto-fit`, named areas, subgrid | A dashboard layout with named grid areas |
| 6.5 Responsive design | Mobile first, media and container queries, `clamp()`, `rem`, `prefers-color-scheme`; MDN Baseline ("widely available" means 30 months of support) | Make the timetable page work from 320 px to 1440 px with no horizontal scroll |

**Check your understanding:** (1) Why did your `margin-top` escape its parent? (2) When do you choose Grid over Flexbox? (3) Why does a container query fit a reusable component better than a media query?

### Chapter 7 · JavaScript, the language (weeks 8–9)

| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Values and types | Primitives, objects, `===`, truthiness, coercion surprises | A 15-item predict-the-output quiz |
| 7.2 Functions and closures | Scope, closures, `this`, arrow functions | Implement `once`, `memoize` and `debounce` |
| 7.3 Data and modules | Destructuring, spread, array methods, ES modules, JSON | Split a 300-line script into three modules |
| 7.4 The event loop | Call stack, task queue, microtasks, rendering; promises and `async`/`await`; errors in async code | Predict the order of mixed `setTimeout`/`Promise`/`await` logs; explain why a long loop freezes the page |

**Check your understanding:** (1) Why does a resolved promise's callback run before a `setTimeout(…, 0)` callback? (2) What does a closure capture: the value or the variable? (3) Why is `await` inside a `for` loop sometimes a performance bug?

### Chapter 8 · The DOM and events (weeks 9–10)

| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Changing the DOM safely | `querySelector`, `createElement`, `textContent` vs `innerHTML`, `classList` | Render user comments safely; explain from the OWASP XSS cheat sheet why `innerHTML` is unsafe |
| 8.2 Events | Listeners, bubbling and capturing, delegation, `preventDefault`, keyboard events | An accessible to-do list using one delegated listener |
| 8.3 Progressive enhancement | Forms that work without JavaScript; the Constraint Validation API | The booking form still submits with JavaScript disabled |
| 8.4 Rendering and Core Web Vitals | Parse, style, layout, paint, composite; layout thrashing; LCP, INP, CLS | Find and fix one layout shift and one slow interaction with the Performance panel |

**Check your understanding:** (1) Why does event delegation keep working for items added later? (2) What causes layout thrashing? (3) Which Core Web Vital does a late-loading banner hurt?

### Chapter 9 · `fetch` and APIs (week 11)

| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 `fetch` and JSON | `Request`/`Response`, headers, `response.ok`, parsing | Show a 7-day forecast for your city from Open-Meteo (no API key needed) |
| 9.2 Failure handling | Network vs HTTP errors, timeouts with `AbortController`, retries with backoff, loading, empty and error states | Simulate offline and 500 errors with DevTools; the UI handles each one |
| 9.3 API styles | REST resources, pagination, versioning, idempotency keys; asynchronous callback APIs such as the Beckn protocol behind ONDC (`search` → `on_search`) | Draw the sequence diagram of a Beckn search |
| 9.4 Browser storage | `localStorage`, `sessionStorage`, IndexedDB, cookies; what never to store in JavaScript-readable storage | Persist the to-do list and justify the storage choice |

**Check your understanding:** (1) Why does `fetch` not reject on a 404? (2) When is a retry dangerous? (3) Why is an access token in `localStorage` a risk?

### Chapter 10 · A tiny backend (week 12)

| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 A server from scratch | `node:http`, manual routing, reading request bodies, status codes | A JSON API with three routes and no framework |
| 10.2 A minimal framework | Hono or Express 5, middleware, schema validation with Zod | Port the API and reject invalid input with a 400 and a clear message |
| 10.3 Persistence and configuration | SQLite through a driver or Node's built-in `node:sqlite` (still a release candidate); parameterised queries; environment variables; secrets kept out of Git | A link-shortener API backed by SQLite |
| 10.4 Testing and headers | `node:test` for endpoints; CSP, HSTS, `X-Content-Type-Options`; simple rate limiting | 20 endpoint tests that run in CI |

**Check your understanding:** (1) What does middleware buy you over a hand-written router? (2) Why are parameterised queries enough to stop SQL injection, while escaping strings is not? (3) Which security header would have stopped an XSS bug from loading a remote script?

### Chapter 11 · Deploy, measure and harden (weeks 13–14)

| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Static hosting | GitHub Pages, Cloudflare Pages and Workers; build output; custom 404 pages | Deploy P1 |
| 11.2 Domains and HTTPS | A and CNAME records for your host, certificate issuance, checking with `dig` and SSL Labs | Point a domain or subdomain at your site and verify it |
| 11.3 Running a backend | Platform hosting vs a small VM; configuration, logs, health checks | Deploy the link-shortener API |
| 11.4 Measure and harden | Lighthouse vs PageSpeed Insights field data, Mozilla Observatory, caching and compression | Reach Lighthouse ≥ 90 in every category and Observatory grade B+ or better; document before and after |
| 11.5 Auditing AI-built sites | Review a generated page for semantics, accessibility, headers, bundle size and unsafe DOM use | Generate a page with an AI app builder and publish an audit with fixes |

**Check your understanding:** (1) Why can Lighthouse scores differ from what real users experience? (2) Your custom domain shows a certificate error. What do you check, in order? (3) What is the first thing you audit on an AI-generated form?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Network tracing | Annotated `traceroute`/`dig +trace` report |
| 2–3 | 2 | Lab 2 · Raw HTTP | Socket client and tiny server |
| 4 | 3 | Lab 3 · TLS, CORS and cookies | Certificate and CORS report; P1 starts |
| 5 | 4 | Lab 4 · Semantic page | Validated timetable page |
| 6 | 5 | Lab 5 · Accessibility audit | Audit plus fixes; P1 due |
| 7–8 | 6 | Lab 6 · Layout challenges | Responsive layouts |
| 8–9 | 7 | Lab 7 · Event-loop puzzles | Quiz plus `debounce` |
| 9–10 | 8 | Lab 8 · DOM to-do app | Accessible app; P2 starts |
| 11 | 9 | Lab 9 · `fetch` with failures | Resilient forecast page; P2 due |
| 12 | 10 | Lab 10 · Tiny backend | API with tests; P3 starts |
| 13–14 | 11 | Deploy and audit | Live URLs with reports |
| 15 | Review and exam | Practical exam (AI off) and P3 demo | P3 due |

## Working with AI in this course

- **Use AI for:** explaining an unfamiliar header or status code after you have read MDN; generating layout variations to compare; listing test cases for your API; a second opinion on your markup's accessibility; boilerplate server code that you then test.
- **Do without AI (drills):** hand-write the HTML and CSS of P1 with completion off; explain "what happens when you type a URL" on a whiteboard; event-loop ordering puzzles; read raw HTTP responses; fix a CORS error using DevTools alone.
- **Verify AI output by:** the W3C validator; axe-core plus a manual keyboard and NVDA pass; Lighthouse; `curl -v` to see the real headers; the OWASP cheat sheets for any code that touches user input; Mozilla Observatory; MDN Baseline status for every feature; endpoint tests with `node:test`.
- **Where AI still fails here:** the Veracode and WebAIM figures above are the measurable failures. In your own audits, check generated code for `div`s used as buttons, inputs without labels, ARIA that contradicts native semantics, `innerHTML` with user data, permissive CORS, secrets in client bundles, and missing error states in `fetch` code. Log each one you find in your P3 audit.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 20% |
| Practical exam, AI off (3 hours) | 30% |

**Mastery gate.** You pass when you can, with AI off, in 3 hours, build and deploy a page that fetches data from an API you wrote, where:
- the page passes axe with zero violations and a keyboard-only walkthrough;
- the layout works from 320 px to 1440 px;
- the API returns correct status codes and caching headers.

You must then explain the full request path using your own `dig` and `curl -v` output.

## Industry reality

Browsers are converging: the Interop project's 2025 cross-browser score rose from 25 to 95, so standard HTML, CSS and JavaScript now go much further without workarounds. Node.js 24 is the current LTS line, and Express 5 was announced as stable in October 2024. TLS 1.3 was re-specified as RFC 9846 in July 2026. In India, GIGW 3.0 requires government sites to conform to WCAG 2.1 AA. ONDC builds open commerce on the Beckn protocol: plain HTTPS calls with asynchronous callbacks. Frontend, backend and full-stack interviews still open with the fundamentals below.

**Interview questions from this course**

1. *"What happens when you type a URL and press Enter?"* URL parsing and HSTS; DNS caches and recursive resolution; TCP or QUIC handshake; TLS 1.3; the HTTP request and response; caching; HTML parsing, subresources, layout and paint, with a rough count of round trips.
2. *"Explain CORS. Why did my request fail in the browser but work in curl?"* The same-origin policy is enforced by the browser; preflight `OPTIONS`; allow-origin and credentials rules; CORS is not server-side access control; common misconfigurations.
3. *"Predict the output order of this code mixing `setTimeout`, promises and `await`."* Microtasks drain before the next task; `await` splits a function; rendering happens between tasks; long tasks hurt INP.
4. *"How do you prevent XSS?"* Contextual output encoding; `textContent` and auto-escaping templates; sanitising HTML with a vetted library such as DOMPurify; CSP; `HttpOnly` cookies; never `innerHTML` with untrusted data.
5. *"Make this custom dropdown accessible."* Prefer a native `<select>`; otherwise follow the WAI-ARIA APG combobox or listbox pattern, with keyboard support, `aria-expanded`, focus management and an accessible name, then test with a screen reader.

## Resources (free first)

- **Courses and books:** [MDN Learn web development](https://developer.mozilla.org/en-US/docs/Learn_web_development); web.dev [Learn HTML](https://web.dev/learn/html), [Learn CSS](https://web.dev/learn/css), [Learn Accessibility](https://web.dev/learn/accessibility); [Full Stack Open](https://fullstackopen.com/en/) (Helsinki); [The Odin Project](https://www.theodinproject.com/paths); [CS50 Web](https://cs50.harvard.edu/web/); [Stanford CS142 lectures](https://web.stanford.edu/class/cs142/lectures.html); [High Performance Browser Networking](https://hpbn.co/).
- **Networking explained:** [Cloudflare Learning Center: What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/); Julia Evans, [How updating DNS works](https://jvns.ca/blog/how-updating-dns-works/) and the [Mess With DNS](https://messwithdns.net/) playground; [Let's Encrypt: How it works](https://letsencrypt.org/how-it-works/).
- **Standards:** [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110), [9111](https://www.rfc-editor.org/rfc/rfc9111), [9112](https://www.rfc-editor.org/rfc/rfc9112), [9114](https://www.rfc-editor.org/rfc/rfc9114), [9000](https://www.rfc-editor.org/rfc/rfc9000), [9846](https://www.rfc-editor.org/rfc/rfc9846), [1034](https://www.rfc-editor.org/rfc/rfc1034), [6265](https://www.rfc-editor.org/rfc/rfc6265); [HTML Living Standard](https://html.spec.whatwg.org/multipage/); [Fetch Standard](https://fetch.spec.whatwg.org/); [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and its [quick reference](https://www.w3.org/WAI/WCAG22/quickref/); [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/).
- **Tools:** [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview); [axe-core](https://github.com/dequelabs/axe-core); [NVDA](https://www.nvaccess.org/download/); [W3C validator](https://validator.w3.org/); [Mozilla Observatory](https://developer.mozilla.org/en-US/observatory); [SSL Labs](https://www.ssllabs.com/ssltest/); [Wireshark](https://www.wireshark.org/); [Node.js `node:test`](https://nodejs.org/api/test.html); [Hono](https://hono.dev/docs/); [Express](https://expressjs.com/); [Open-Meteo](https://open-meteo.com/en/docs); [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages); [Cloudflare Pages](https://developers.cloudflare.com/pages/).
- **Security practice (legal environments):** [PortSwigger Web Security Academy](https://portswigger.net/web-security); [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/); OWASP [XSS](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) and [CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) prevention cheat sheets.

## Sources

All checked 12 Oct 2026.

- Veracode, 2025 GenAI Code Security Report (30 Jul 2025) — https://www.veracode.com/blog/genai-code-security-report/
- WebAIM Million 2026 (Feb 2026 data) — https://webaim.org/projects/million/
- OWASP Top 10:2025 — https://top10.owasp.org/2025
- RFC 9846, TLS 1.3 (Jul 2026, obsoletes RFC 8446) — https://www.rfc-editor.org/rfc/rfc9846 · RFC 6265bis draft status — https://datatracker.ietf.org/doc/draft-ietf-httpbis-rfc6265bis/
- Mozilla Hacks, "Launching Interop 2026" (12 Feb 2026, includes final Interop 2025 scores) — https://hacks.mozilla.org/2026/02/launching-interop-2026/
- MDN, Baseline compatibility definition — https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility
- Node.js releases — https://nodejs.org/en/about/previous-releases · `node:sqlite` stability — https://nodejs.org/api/sqlite.html · Express 5 release (15 Oct 2024) — https://expressjs.com/en/blog/2024-10-15-v5-release
- WCAG 2.2 (Recommendation since 5 Oct 2023) — https://www.w3.org/TR/WCAG22/ · WCAG 3.0 Working Draft (10 Sep 2026) — https://www.w3.org/TR/wcag-3.0/
- GIGW 3.0, Guidelines for Indian Government Websites and Apps — https://guidelines.india.gov.in/
- *Rajive Raturi v. Union of India*, Supreme Court of India (8 Nov 2024) — https://api.sci.gov.in/supremecourt/2005/9321/9321_2005_1_1503_56986_Judgement_08-Nov-2024.pdf · summary: https://www.scconline.com/blog/post/2024/11/12/union-mandate-rules-under-rpwd-act-ensure-accessibility-of-public-places-supreme-court/
- *Pragya Prasun v. Union of India*, 2025 INSC 599 (30 Apr 2025) — https://api.sci.gov.in/supremecourt/2024/17879/17879_2024_13_1501_61229_Order_30-Apr-2025.pdf · summary: https://www.verdictum.in/court-updates/supreme-court/digital-kyc-accessible-for-acid-attack-survivors-2025-insc-599-pragya-prasun-v-union-of-india-1575850
- Beckn protocol specifications (used by ONDC) — https://github.com/beckn/protocol-specifications
- axe-core (states it finds on average 57% of WCAG issues automatically) — https://github.com/dequelabs/axe-core

_Last reviewed: 2026-10_
