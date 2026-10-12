# FE401 · Labs and projects

Every lab runs against a real database and measures the FE304 baseline mobile profile (4× CPU, 9 Mbps, 100 ms RTT). Security labs use only your own applications and legal practice environments. The authorisation test suite in Lab 6 is written without AI, because generated authorisation code is where the course's failure log grows fastest.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Five renderings | One product page as CSR, SSR, SSG, ISR and a partially prerendered shell | Table of TTFB, LCP, INP and JavaScript bytes (median of 5); a one-paragraph recommendation | 5 h |
| 2 · Waterfalls and streaming | Remove a 4-level waterfall; stream a slow panel with zero CLS | Before/after waterfalls; CLS 0 on the streamed boundary | 4 h |
| 3 · Progressive mutations | Checkout that works without JavaScript, enhanced with optimistic UI and idempotency keys | Test: double-submit creates one order; JavaScript-disabled run passes | 5 h |
| 4 · Cache map and leaks | Diagram every cache layer; find and fix 3 planted leaks | Diagram; two-user tests that fail before and pass after each fix | 6 h |
| 5 · Three runtimes | Deploy one route to Node, serverless and edge; database in an Indian region | Cold/warm latency and TTFB from two locations; data-locality analysis | 4 h |
| 6 · Auth (authorisation tests without AI) | Sessions with rotation, OIDC with PKCE through a backend-for-frontend, passkeys, multi-tenant authorisation | Tenant-isolation suite covering every route, loader and Server Function; Playwright passkey test | 7 h |
| 7 · Hardening | Nonce CSP with streaming, Trusted Types, SSRF allow-list, secret scanning, RSC patch runbook | Zero CSP violations in a full E2E run; CI blocks a planted secret; runbook | 5 h |
| 8 · Same feature, other frameworks | Orders feature in React Router v8 plus one of Nuxt 4, SvelteKit 3 or Astro 7 | Two implementations; comparison of JavaScript, TTFB, INP and lines of code | 8 h |
| 9 · Real-time | Live order status over SSE or WebSocket with reconnection and resume | Disconnect test: no missed updates after a 30-second outage | 4 h |
| 10 · Tracing and skew | OpenTelemetry trace from click to SQL; reproduce and fix version skew | Trace screenshot; skew test that fails before and passes after | 4 h |

## Projects

### P1 · Content site with zero-JavaScript defaults (L1, ~6 hours)

**Real-world inspiration:** documentation, news and marketing sites gain the most from static and island rendering. Astro's docs and the Next.js docs both show this pattern publicly. The site, a course catalogue for this university, is built from `catalog.json`.

**What to build:** a statically generated site listing every course, filterable by year and major, with course pages, search (an island) and a "related courses" panel streamed from a server endpoint. Use Astro 7 or Next.js 16.

**Acceptance criteria:**
- **Speed:** Lighthouse performance at least 95 on the baseline mobile profile for the home page and a course page; LCP at most 1.8 s.
- **JavaScript:** zero JavaScript on course pages except the search island, which loads on interaction and weighs at most 20 KB gzipped.
- **Accessibility:** axe zero; filters usable by keyboard and announced to screen readers.
- **Build:** every course in the catalogue has a page; a CI check fails if a catalogue entry has no page.
- **Caching:** hashed assets are `immutable`; HTML revalidates; headers verified with `curl -I`.

**Stretch goals:** incremental builds that regenerate only changed course pages; an Open Graph image per course generated at build time.

**What it proves to an employer:** you choose the simplest rendering that meets the need and can show the payoff in numbers.

### P2 · Storefront with correct caching and authentication (L2, ~15 hours)

**Real-world inspiration:** Indian e-commerce runs large sale events where prices and stock change quickly and traffic spikes. The store is an **illustrative scenario**.

**What to build:** a storefront with:
- home, category, product, cart, checkout (mock payment) and order history;
- authentication with sessions and passkeys, and an admin role that edits prices;
- partially prerendered product pages with dynamic price and stock, tag-based revalidation when the admin changes a price, and a flash-sale mode;
- a database in an Indian cloud region, a CDN in front, and Hindi and English.

**Acceptance criteria:**
- **Cache correctness:** a two-user test suite (anonymous, user A, user B, admin) across all routes proves no personalised data is ever served to another user, by CDN, framework cache or browser. A planted leak is caught by the suite.
- **Freshness:** after an admin price change, the new price appears on product and category pages within 5 seconds, verified by an automated test.
- **Performance:** product page LCP at most 2.5 s and INP at most 200 ms on the baseline profile; cart and checkout INP at most 200 ms.
- **Load:** during a simulated sale (500 requests/s for 5 minutes to product pages), origin requests stay below 10% of total because of caching, and p95 TTFB stays under 800 ms.
- **Authorisation:** non-admins cannot change prices through any route or Server Function (tested); every Server Function validates input with a shared schema.
- **Idempotency:** a retried or double-clicked order submission creates exactly one order.

**Stretch goals:** a stock counter streamed over SSE; skew protection demonstrated during a deploy in the middle of the load test.

**What it proves to an employer:** you can build the parts of a commerce site where mistakes leak data or lose money, and prove they are right.

### P3 · Multi-tenant SaaS dashboard, production-grade (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** B2B SaaS products from Indian companies serve customers worldwide. They need tenant isolation, single sign-on, audit logs, fast dashboards and safe deploys. The product, an inventory dashboard for small retailers, is an **illustrative scenario**.

**What to build:**
- tenants with organisations and roles (owner, manager, viewer);
- OIDC sign-in plus passkeys, and invitations;
- a dashboard with server-rendered tables, streamed charts and live stock alerts over SSE;
- CSV import as a background job, and an audit log of every mutation;
- strict CSP with Trusted Types and OpenTelemetry tracing;
- deployment to two environments with previews, canary and rollback, and skew protection;
- one feature (the alerts page) also built in a second framework, embedded or deployed separately, with a written comparison.

**Acceptance criteria:**
- **Isolation:** an automated suite of at least 60 tests attempts cross-tenant reads and writes through every route, loader, Server Function, API endpoint and export; all are denied. A planted bug in one data-access function is caught.
- **Security:** zero CSP and Trusted Types violations across the E2E suite. No secrets in client bundles (CI scan). Dependencies at or above patched framework versions, with automated advisory alerts and a tested patch runbook.
- **Performance:** dashboard LCP at most 2.5 s and INP at most 200 ms on the baseline profile with 10,000 rows (server pagination and virtualisation).
- **Reliability:** a deploy during a 15-minute synthetic session test produces zero failed user actions (skew protection evidence). A planted bad release is detected by the canary and rolled back within 10 minutes.
- **Observability:** a single trace links a user's click to the database query and the background job it triggered.
- **Comparison:** a 3-page report compares the two framework implementations of the alerts page with measurements and a recommendation.

**Stretch goals:** SAML single sign-on for an enterprise tenant; per-tenant rate limits; an MCP server exposing read-only dashboard data to an AI assistant, with tenant-scoped authorisation (preview of FE403).

**What it proves to an employer:** you can own a full-stack product end to end, including the security and operational work that separates a demo from software people pay for.

## Feeds into

- [FE403 AI-Native Interfaces](../FE403_ai_native_interfaces_streaming_generative_ui/README.md): streaming routes, Server Functions and authorisation for AI features.
- [FE404 Frontend System Design at Scale](../FE404_frontend_system_design_at_scale/README.md): rendering, caching and deployment choices in design reviews.
- [FE501 Frontier Seminar](../../year_5/FE501_frontier_seminar_multimodal_spatial_and_on/README.md): local-first and on-device alternatives to server rendering.
- [OV08 Full-Stack AI Product Engineering](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/README.md) and [OV02 Cloud-Native Backend](../../../../04_overlaps/OV02_cloud_native_backend/README.md).
