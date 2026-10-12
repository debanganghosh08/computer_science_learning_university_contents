# FE401 · Full-Stack Frameworks: Rendering, Data Fetching and State

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [FE301](../../year_3/FE301_modern_javascript_and_typescript_in_depth/README.md) (and in practice [FE302](../../year_3/FE302_react_and_component_architecture/README.md), [FE304](../../year_3/FE304_browser_internals_and_web_performance/README.md)) | [FE501](../../year_5/FE501_frontier_seminar_multimodal_spatial_and_on/README.md), [FE404](../FE404_frontend_system_design_at_scale/README.md), [OV08](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/README.md) |

Part of the [Frontend Engineering major](../../README.md). This is where a frontend engineer becomes a product engineer: you own the server that renders your UI, the caches in front of it and the authentication behind it. Backend depth comes from [BE301](../../../backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md) (elective) and [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md).

## Why this course matters now

Full-stack frameworks now decide most of a web product's architecture. The current releases:
- **Next.js 16** (October 2025) made Turbopack the default and introduced Cache Components (Partial Prerendering plus `use cache`). Version 16.2 stabilised a build Adapter API for non-Vercel hosts, and 16.4 (October 2026) turned Cache Components on by default for new apps.
- **React Router v8** (June 2026) is the React meta-framework that absorbed Remix v2, which is now end of life. Remix 3 left React behind as a requirement and ships its own UI runtime on web primitives.
- **SvelteKit 3** (October 2026), **Nuxt 4** and **Astro 7** (June 2026, with a new Rust compiler) complete the field.

These frameworks blur client and server, and that has a security cost. The December 2025 React Server Components flaw (CVE-2025-55182, CVSS 10.0) allowed unauthenticated remote code execution through Next.js, React Router and other RSC frameworks, and on 8 October 2026 Next.js pre-announced another out-of-band security release. App generators such as v0, Lovable and Bolt produce a working full-stack app in minutes. What they do not reliably get right is which data may be cached for whom, where authorisation is checked, what happens during a deploy when old clients talk to new servers, and what each rendering choice costs users on a slow phone.

## Learning outcomes

By the end you can:

1. **Choose** a rendering strategy per route (CSR, SSR, SSG, ISR, streaming, partial prerendering, islands) and **prove** the choice with TTFB, LCP and INP measurements.
2. **Design** data loading without waterfalls, using loaders, Server Components, parallel fetching, prefetching and Suspense boundaries.
3. **Implement** mutations with progressive enhancement, optimistic UI and precise revalidation (tags, paths, `updateTag`, `refresh`).
4. **Reason about** every cache layer (browser, CDN, framework data cache, `use cache`) and **guarantee** that personalised data is never served to the wrong user.
5. **Deploy** to Node servers, serverless functions and edge runtimes, and **explain** the latency, cold-start and data-locality trade-offs for Indian users.
6. **Build** authentication (sessions, OAuth 2.1/OIDC with PKCE, passkeys) and **enforce** authorisation on the server for every data access and mutation.
7. **Secure** server-rendered apps against framework-specific risks: exposed Server Functions, deserialisation flaws, secrets in client bundles, SSRF in image optimisers, CSP with streaming.
8. **Compare** Next.js, React Router, Nuxt, SvelteKit, Astro, TanStack Start and Remix 3 by building the same feature, and **operate** an app with tracing, skew protection and safe rollbacks.

## Chapters and lessons

### Chapter 1 · The rendering spectrum (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Where HTML is made | CSR, SSR, SSG, ISR, streaming SSR; the timing of TTFB, FCP, LCP and hydration for each | Build one product page five ways; record all vitals on the FE304 baseline profile |
| 1.2 Partial prerendering | A static shell with dynamic holes; Cache Components and `use cache` in Next.js 16 | Convert a fully dynamic page to a prerendered shell with two dynamic holes |
| 1.3 Islands and resumability | Astro islands, Qwik-style resumability, zero-JS content routes | Rebuild a docs site in Astro 7; compare shipped JavaScript |
| 1.4 Choosing per route | A decision table: freshness, personalisation, SEO, interactivity, cost | Write a rendering plan for 8 routes of an e-commerce app |

**Check your understanding:** Why can SSR improve LCP but worsen INP? What makes a route a poor candidate for static generation? Why is "the whole app uses SSR" usually the wrong unit of decision?

### Chapter 2 · Routing and data loading (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Nested routes and layouts | File-based routing, layouts that persist, parallel and intercepting routes | Build a dashboard whose sidebar state survives navigation |
| 2.2 Loaders and Server Components | Route loaders (React Router), data fetching in Server Components, request deduplication | Fetch the same data in loader style and RSC style; compare round trips |
| 2.3 Waterfalls | Sequential awaits, component-level fetching, parallel `Promise.all`, preloading patterns | Remove a 4-level waterfall; show the timing change |
| 2.4 Suspense placement | Where to stream, loading UI that does not shift layout, error boundaries per segment | Stream a slow recommendations panel with zero CLS |
| 2.5 Navigation | Prefetching on viewport or intent, instant navigations and client-cached shells (Next.js 16.3) | Measure navigation time with and without prefetching on a throttled network |

**Check your understanding:** Why do Server Components make waterfalls easier to create? When does prefetching waste a user's data? Where should a Suspense boundary go on a product page, and why?

### Chapter 3 · Mutations and progressive enhancement (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Forms that work without JavaScript | Native forms posting to actions; enhancing with JavaScript | A checkout form that completes with JavaScript disabled |
| 3.2 Server Functions and actions | React Router actions, Next.js Server Functions, SvelteKit remote functions and form actions; every one is a public endpoint | Implement the same mutation in two frameworks; add validation and authorisation |
| 3.3 Revalidation | Tag-based and path-based revalidation, `revalidateTag`, `updateTag`, `refresh` (Next.js 16) | Update a cart and revalidate exactly the affected UI |
| 3.4 Optimistic UI and idempotency | `useOptimistic`, idempotency keys for retried submissions, double-submit protection | Prove a double-clicked "Place order" creates one order |

**Check your understanding:** What does a user on a slow 3G connection experience before JavaScript loads, and how do forms help? Why must every Server Function check authorisation even if the button is hidden? What makes a retried mutation dangerous?

### Chapter 4 · Caching layers and correctness (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The stack of caches | Browser, service worker, CDN, framework data cache, database cache; which keys each uses | Draw every cache between a user and the database for one request |
| 4.2 HTTP caching for HTML | `Cache-Control` for documents, `private` vs `public`, `Vary`, `stale-while-revalidate`, CDN rules | Configure caching so anonymous pages are CDN-cached and logged-in pages never are |
| 4.3 Framework caches | `use cache` and cache keys, tags, lifetimes; React `cache()` for request deduplication | Cache an expensive query with correct tags and lifetime |
| 4.4 Cache correctness bugs | Personalised data cached publicly, missing `Vary: Cookie`, cache poisoning via unkeyed headers | Find and fix 3 planted cache leaks; write a test that would have caught each |
| 4.5 Invalidation design | Event-driven invalidation, TTL vs tags, thundering herds | Design invalidation for prices that change every 5 minutes on a flash sale |

**Check your understanding:** What is the worst caching bug a full-stack app can have, and how do you test for it? Why is `stale-while-revalidate` safe for a product page but not for an account page? What happens to your origin when a popular tag is invalidated during a sale?

### Chapter 5 · Runtimes: Node, serverless and edge (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Runtime models | Long-lived Node servers, serverless functions, V8-isolate edge runtimes (Cloudflare Workers); API differences and limits | Deploy the same route to all three; compare cold and warm latency |
| 5.2 Data locality | Rendering at the edge but querying a database in one region; serving Indian users from Mumbai or Hyderabad regions | Measure TTFB from Delhi- and Chennai-like test locations against a single-region database |
| 5.3 Middleware | Request interception for redirects, A/B tests and authentication checks; what must not run there | Move a slow middleware check into the route |
| 5.4 Portability | Build adapters (stable in Next.js 16.2), OpenNext, Nitro (Nuxt), SvelteKit adapters | Deploy one Next.js app to a non-Vercel host via an adapter |

**Check your understanding:** Why can edge rendering make TTFB worse? What belongs in middleware and what does not? How do you avoid locking a product to one host?

### Chapter 6 · Authentication and authorisation (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Sessions vs tokens | Cookie sessions (`HttpOnly`, `Secure`, `SameSite`), JWT trade-offs, revocation, rotation | Implement sessions with rotation and server-side revocation |
| 6.2 OAuth 2.1 and OIDC | Authorisation code with PKCE, ID tokens vs access tokens, the backend-for-frontend pattern | Add "Sign in with Google" using a backend-for-frontend; no tokens in JavaScript-readable storage |
| 6.3 Passkeys | WebAuthn registration and authentication, account recovery, Playwright passkey testing | Add passkey login with a tested fallback |
| 6.4 Authorisation | Role- and attribute-based checks, multi-tenancy, checking at the data layer, IDOR prevention | Write tests proving tenant A can never read tenant B's data through any route or function |

**Check your understanding:** Why is a JWT in `localStorage` a risk, and what does a backend-for-frontend fix? Where must authorisation be enforced in an app with Server Components, Server Functions and API routes? What makes account recovery the weakest point of passkey adoption?

### Chapter 7 · Security of server-rendered apps (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The RSC incident | CVE-2025-55182: unsafe deserialisation of Server Function payloads in RSC packages, affected frameworks, fixed versions; why apps without Server Functions were exposed | Write a patch runbook: detection, upgrade, verification, communication |
| 7.2 Secrets and bundles | Environment variable prefixes that expose values to the client; taint APIs; scanning bundles | Find a planted secret in client output; add a CI check |
| 7.3 Content Security Policy | Nonce-based CSP with streaming SSR, `strict-dynamic`, Trusted Types (Baseline February 2026; supported by React 19.3) | Ship a strict CSP and Trusted Types with zero violations in a full test run |
| 7.4 Server-side request risks | SSRF through image optimisers and URL-fetching features; allow-lists | Restrict an image optimiser to known hosts; test the restriction |
| 7.5 Patch cadence | Watching framework security advisories (for example Next.js's announced 14 October 2026 release), automated updates, staged rollout | Set up advisory alerts and a weekly dependency update with tests |

**Check your understanding:** Why does blurring client and server enlarge the attack surface? What does a nonce-based CSP require from a streaming renderer? How fast should a team be able to ship a critical framework patch, and what makes that possible?

### Chapter 8 · Beyond Next.js (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 React Router v8 | Framework mode, loaders and actions, middleware on by default, ESM-only, RSC support still unstable | Build the "orders" feature in React Router v8 |
| 8.2 Nuxt 4 and SvelteKit 3 | Nitro server engine; SvelteKit remote functions, form actions and built-in OpenTelemetry | Build the same feature in one of them |
| 8.3 Astro 7 and content sites | Islands, content collections, server rendering where needed | Build a content-heavy route with zero JavaScript by default |
| 8.4 TanStack Start and Remix 3 | Type-safe routing and server functions (TanStack); Remix 3's web-primitives approach with an optional React layer | Spike one route in each; write a one-page assessment |
| 8.5 Comparing fairly | Same feature, same data, same budget: JavaScript shipped, TTFB, INP, lines of code, developer experience | A comparison report with numbers and a recommendation |

**Check your understanding:** What does each framework decide for you that you would otherwise decide yourself? Why might a content site choose Astro over Next.js? What would make you recommend a non-React framework to a React team?

### Chapter 9 · Real-time and state across the boundary (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Server state vs client state | URL state, server cache, form state and local UI state in a server-rendered app | Classify all state in a sample app; remove one client store |
| 9.2 Real-time updates | Server-Sent Events and WebSockets in server-rendered apps; hosting limits on long connections | Add live order status updates with reconnection |
| 9.3 Optimistic and offline-tolerant UX | Queued mutations, retry with idempotency, conflict messages | Survive a 30-second network drop without losing a form submission |
| 9.4 Background work | Queues and scheduled jobs from frameworks; when to hand off to a backend service | Move email sending out of the request path |

**Check your understanding:** Why do serverless platforms struggle with WebSockets, and what are the options? How does an optimistic update interact with server revalidation? When should frontend engineers stop and ask for a dedicated backend?

### Chapter 10 · Observability, deployment and version skew (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Tracing across client and server | OpenTelemetry in frameworks, trace context from browser to server to database | One trace from a click to a SQL query |
| 10.2 Errors | Server and client error boundaries, digest-only errors in production, source maps | Debug a production error from a digest to code |
| 10.3 Version skew | Old clients calling new servers during deploys; skew protection, deployment IDs, backward-compatible actions | Reproduce a skew failure; fix it with versioning |
| 10.4 Safe deploys | Preview environments, canaries, feature flags, instant rollback, database migrations that come before code | Roll out and roll back a breaking change with zero failed requests |

**Check your understanding:** Why are deploys riskier for server-rendered apps than for static SPAs? What is the order of operations for a database change used by a server-rendered page? What does a trace show that logs alone do not?

### Chapter 11 · Migrations and framework choice (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Incremental migration | Pages Router to App Router, Remix v2 to React Router, SPA to framework; strangler pattern by route | Migrate 3 routes of a legacy SPA while the rest keeps working |
| 11.2 Codemods and AI-assisted migration | Official codemods, agents for repetitive edits, tests as the safety net | Use an agent to migrate 20 files; measure how many needed human fixes |
| 11.3 Writing the decision | Decision records, cost of change, team skills, hosting, lock-in | A 3-page framework decision for a provided scenario |

**Check your understanding:** Why is a big-bang framework migration rarely the right plan? What should an agent be trusted to do in a migration, and what must a human check? Which costs of a framework only appear after a year?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Five renderings | Vitals table |
| 2 | 2 | Lab 2 · Waterfalls and streaming | Timing report; **P1 starts** |
| 3 | 3 | Lab 3 · Progressive mutations | No-JS checkout |
| 4 | 4 | Lab 4 · Cache map | Cache diagram; **P1 due** |
| 5 | 4 | Lab 4 (cont.) · Cache leaks | Leak tests |
| 6 | 5 | Lab 5 · Three runtimes | Latency report |
| 7 | 6 | Lab 6 · Auth (no AI for the authorisation tests) | Tenant isolation suite; mid-term (AI off) |
| 8 | 7 | Lab 7 · Hardening | CSP, Trusted Types, patch runbook; **P2 due** |
| 9 | 8 | Lab 8 · Same feature, other frameworks | Two implementations |
| 10 | 8 | Lab 8 (cont.) | Comparison report |
| 11 | 9 | Lab 9 · Real-time | Live order status |
| 12 | 10 | Lab 10 · Tracing and skew | Trace and skew fix; **P3 starts** |
| 13 | 11 | Migration sprint | Migrated routes |
| 14 | 11 | Decision record | **P3 due** |
| 15 | Review | P3 defence with a live incident drill | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** scaffolding routes and forms; generating framework comparisons that you then verify by building; codemod-style migrations with agents; drafting CSP and caching configuration from your specification; explaining framework error messages.
- **Do without AI (drills):** the cache map; the tenant-isolation authorisation tests; the patch runbook; the mid-term (choose rendering and caching for a scenario on paper) and the final incident drill.
- **Verify AI output by:** cache-leak tests run as two different users; authorisation tests for every route and function; bundle scans for secrets; checking every framework API against current documentation, because Next.js 16, React Router v8, SvelteKit 3 and Astro 7 all changed APIs within the last year; reproducing performance claims on the baseline profile.
- **Where AI still fails here (collect your own evidence):** generated full-stack code often checks authorisation in the UI but not in the Server Function, and exposes secrets through client-prefixed environment variables. It also caches personalised responses, mixes Pages Router and App Router APIs, or uses APIs removed in the current major version. Log each case with the test that exposed it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 20% |
| Mid-term (AI off) | 10% |
| Final (AI off, 3 h) including a live incident drill | 20% |

**Mastery gate.** You pass when you can, with AI off, take a provided multi-tenant app in a framework of your choice and, within 3 hours:
1. find and fix a planted cache leak, a missing authorisation check in a Server Function, and a secret in the client bundle, each with a regression test;
2. move one route to the rendering strategy that meets LCP ≤ 2.5 s on the baseline profile;
3. explain, in a 10-minute oral, how you would patch a critical framework vulnerability across three environments within 24 hours.

## Industry reality

Full-stack and product engineer roles expect frontend engineers to own server rendering and data access (see the [FE market page](../../../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md)). The React team's advisory for CVE-2025-55182 listed affected frameworks and bundlers, including Next.js, React Router, Waku, Parcel's RSC support and Vite's RSC plugin. One flaw reached across the ecosystem, and teams that could patch in hours were safe. Next.js 16.2's stable Adapter API and OpenNext respond to teams' demand for host portability. Frontend system design interviews (FE404) routinely ask for rendering and caching choices per page.

**Interview questions from this course**

1. *Which rendering strategy would you use for the home page, product page, cart and order history of an e-commerce site?* A strong answer gives a static or partially prerendered home page, a product page with a cached shell and dynamic price and stock, a dynamic and private cart, and server-rendered order history that is never shared-cached. It justifies each with freshness, personalisation, SEO and vitals.
2. *A user reports seeing another user's name in the header. What happened and how do you prevent it?* A strong answer suspects a shared cache storing a personalised response: CDN rules, a missing `private` directive or `Vary`, or a framework cache keyed without the user. It describes immediate mitigation (purge, disable caching), a regression test with two users, and a review of all cache layers.
3. *Where do you check authorisation in an app using Server Components and Server Functions?* A strong answer checks on the server at every data access and every mutation, ideally in a data-access layer. It never relies on hidden UI, treats Server Functions as public endpoints with validation, and tests tenant isolation.
4. *Our app renders at the edge but feels slow in India. Why?* A strong answer points to edge rendering that still calls a database in a distant region, so each request crosses continents. It proposes regional rendering near the data (for example an Indian cloud region), caching, read replicas, or moving data-independent parts to the edge. It shows the TTFB math.
5. *After a deploy, some users get errors for 10 minutes. What is going on?* A strong answer identifies version skew: old client bundles calling renamed actions or changed APIs. It proposes skew protection, keeping old deployments briefly, backward-compatible changes, deployment IDs, and monitoring by client version.

## Resources (free first)

- **Frameworks:** [Next.js docs](https://nextjs.org/docs); [React Router](https://reactrouter.com/); [Nuxt docs](https://nuxt.com/docs); [SvelteKit docs](https://svelte.dev/docs/kit); [Astro docs](https://docs.astro.build/); [TanStack Start](https://tanstack.com/start/latest); [OpenNext](https://opennext.js.org/); [Cloudflare Workers](https://developers.cloudflare.com/workers/).
- **Concepts:** [Rendering on the web](https://web.dev/articles/rendering-on-the-web); [patterns.dev](https://www.patterns.dev/); [React Server Components reference](https://react.dev/reference/rsc/server-components); [Cache-Control for civilians](https://csswizardry.com/2019/03/cache-control-for-civilians/).
- **Auth and security:** [OAuth 2.1](https://oauth.net/2.1/); [WebAuthn Level 3](https://www.w3.org/TR/webauthn-3/); [Better Auth](https://www.better-auth.com/); [OWASP cheat sheets](https://cheatsheetseries.owasp.org/); [PortSwigger Web Security Academy](https://portswigger.net/web-security) (legal practice labs).
- **Operations:** [OpenTelemetry JavaScript](https://opentelemetry.io/docs/languages/js/); [Sentry JavaScript](https://docs.sentry.io/platforms/javascript/).

## Sources

All checked 12 Oct 2026.

- Next.js blog: Next.js 16 (21 Oct 2025), 16.2 (18 Mar 2026), adapters post (25 Mar 2026), 16.3 (3 Aug 2026), 16.4 (6 Oct 2026), security pre-announcement (8 Oct 2026) — https://nextjs.org/blog · https://nextjs.org/blog/next-16 · https://nextjs.org/blog/next-16-4
- Remix team: React Router v8 (17 Jun 2026) — https://remix.run/blog/react-router-v8 · Remix 3 Release Candidate (31 Aug 2026) — https://remix.run/blog/remix-3-release-candidate · npm `remix` latest 3.0.0 on 12 Oct 2026 — https://registry.npmjs.org/remix
- React blog: Critical Security Vulnerability in React Server Components (3 Dec 2025) — https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components · React 19.3 (Trusted Types support) — https://react.dev/blog/2026/09/09/react-19-3
- Svelte blog (SvelteKit 3, 1 Oct 2026; remote functions; OpenTelemetry) — https://svelte.dev/blog
- Astro blog (Astro 7.0, 22 Jun 2026) — https://astro.build/blog/astro-7/ · Nuxt blog (Nuxt 4, 15 Jul 2025; 4.6, 5 Oct 2026) — https://nuxt.com/blog
- web-features 3.42.0 (Trusted Types Baseline Feb 2026) — https://web-platform-dx.github.io/web-features/

_Last reviewed: 2026-10_
