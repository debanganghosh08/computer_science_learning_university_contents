# MOB403 · Labs and projects

Every project has two halves: a written design (scored with the course's design rubric) and a working client that proves its riskiest parts with measurements. Clients may be native or cross-platform. The course provides a network shaper (3G-like, lossy and flapping profiles), a mock backend kit and a load generator. Labs 1 and 5 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Requirements and estimates (no AI) | Ten timed drills: clarifying questions, users, payloads, bytes per session, on-device storage | Drill sheets with your numbers and assumptions | 4 h |
| 2 · API contracts and pagination | Offset vs cursor pagination under concurrent inserts; error and idempotency contracts | A test that shows offset pagination duplicating items and cursor pagination not | 5 h |
| 3 · Normalised cache | One copy per entity; a like in the feed updates the detail screen and the profile | Tests across three screens; memory footprint | 5 h |
| 4 · Image pipeline budgets | Memory and disk cache sizes for a 2 GB phone; downsampling; resized CDN URLs | Peak memory and bytes per 100 images before and after | 5 h |
| 5 · Reconnect and gap filling (no AI) | WebSocket client with heartbeats, backoff with jitter and sequence-gap detection | Chaos test log: disconnects, gaps detected and filled | 6 h |
| 6 · Chat client core | Message states, outbox, per-conversation ordering, receipts | State diagram; tests for every transition | 6 h |
| 7 · Location cadence and battery | Update intervals by trip state; smoothing; energy measurement | 30-minute energy report per cadence; chosen policy | 5 h |
| 8 · Offline search | Full-text search over 50,000 notes with SQLite FTS on the low-end device | Query latency p50/p95; index size | 4 h |
| 9 · Flash-sale client behaviour | Jittered start, retry with backoff, queue screen, kill switches | Load-generator chart of request arrival with and without jitter | 4 h |
| 10 · Observability and flags | Traces for one user journey; flags with safe cold-start defaults | Trace screenshots; a test with config unavailable | 4 h |

## Projects

### P1 · Image feed client with a design note (L1, ~6 hours)

**Real-world inspiration:** photo feeds such as Instagram's must scroll smoothly on cheap phones while new posts arrive. This feed and its backend are an illustrative scenario.

**What to build:** a two-page design note (requirements, estimates, API with cursor pagination, client data layer, image pipeline) and a client that pages from a local database backed by the mock feed API, with downsampled images and prefetching.

**Acceptance criteria:**
- **Correct paging:** across 100 randomised runs in which new items are inserted while the user scrolls, no item is shown twice and none is skipped.
- **Memory:** peak memory under 250 MB while scrolling 2,000 images on the low-end device (release build).
- **Data:** bytes per 100 images reported, and at least 40% lower than full-resolution downloads.
- **Offline:** the first page loads from cache in airplane mode, with a freshness label.
- **Design note:** scores at least "meets bar" on the rubric's requirements, estimates and data-layer rows.

**Stretch goals:** video items with autoplay that respects Data Saver; impression logging that never blocks scrolling.

**What it proves to an employer:** you can turn a design into a measured client and explain pagination and image budgets, the two topics every feed question probes.

### P2 · Chat that never loses a message (L2, ~15 hours)

**Real-world inspiration:** chat apps such as WhatsApp must deliver every message exactly once, in order, across flaky networks and app kills. Your client and server are an illustrative scenario; encryption is designed on paper, not implemented.

**What to build:** a design document for one-to-one and small-group chat, and a client plus a minimal WebSocket server: client-generated IDs, outbox, message states, per-conversation sequence numbers, receipts, history pagination, and push as a wake-up signal when backgrounded (FCM/APNs or a simulated push).

**Acceptance criteria:**
- **Delivery:** a 1,000-message chaos test with random disconnects, server restarts and duplicate deliveries ends with zero lost and zero duplicated messages, and order preserved in every conversation.
- **Recovery:** after the network returns, the client reconnects within 5 seconds at p95, using backoff with jitter (log evidence).
- **Background behaviour:** no socket is held in the background; a push wakes a sync that fetches missed messages.
- **Battery:** one hour with the app backgrounded and messages arriving costs at most 2% battery on the reference phone (method documented).
- **Design:** the document covers multi-device, group fan-out and what end-to-end encryption would change, and scores "hire" from one reviewer.

**Stretch goals:** media messages with resumable upload; on-device search of history; typing indicators that cost no battery when the screen is off.

**What it proves to an employer:** you can design and prove a real-time mobile system, which is the most common senior mobile design question.

### P3 · Hyperlocal delivery tracking: design and client (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** quick-commerce and food-delivery apps in India (for example Swiggy, Blinkit and Zepto) show live rider location, ETAs and order status, and run big sale events. Your system, its rider simulator and its backend are an illustrative scenario.

**What to build:**
- **Design document (up to 10 pages):** requirements and estimates; API contract; client architecture; order and rider state machines; real-time strategy (socket in foreground, push in background, polling fallback); location cadence; payment-pending handling; flash-sale behaviour; observability; security and accessibility notes; failure-mode table.
- **Client:** order list and detail, live map tracking with ETA, status notifications, idempotent order creation, a payment-pending state, jittered behaviour at a scheduled sale start, kill switches and traces for the order journey.
- **Backend:** mock services with a rider simulator moving along real roads, plus the course load generator.

**Acceptance criteria:**
- **Design quality:** two reviewers score the document and a 45-minute defence at "hire" or above.
- **Data:** a 30-minute tracked order uses at most 2 MB of mobile data (proxy capture).
- **Battery:** 30 minutes on the tracking screen costs at most 4% battery on the reference phone (method documented).
- **Latency:** status changes reach the screen at p95 within 3 seconds on Wi-Fi and 10 seconds on the 3G-like profile, measured over 200 events.
- **Correctness:** 20 forced timeouts during order creation produce zero duplicate orders.
- **Load behaviour:** with 10,000 simulated clients, jitter spreads sale-start requests over at least 30 seconds instead of a spike; the chart is included.
- **Operability:** a trace for one order journey from tap to delivered is visible end to end; turning off live tracking with a flag degrades to polling without a release.

**Stretch goals:** a rider app with a 10-hour battery budget; a home-screen widget or Live Activity for the order; multi-order tracking.

**What it proves to an employer:** you can design a real mobile system end to end, defend it under questioning and back it with measurements, which is the bar for senior mobile roles in commerce, mobility and delivery.

## Feeds into

- [CAR401 Career Lab II](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): your P2 and P3 designs become interview stories and mock rounds.
- [MOB501 Frontier Seminar](../../year_5/MOB501_frontier_seminar_wearables_ar_and_ambient/README.md): designing for watches, glasses and ambient surfaces.
- The [Mobile Engineering flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/MOB_mobile_engineering.md) and [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) founder work.
