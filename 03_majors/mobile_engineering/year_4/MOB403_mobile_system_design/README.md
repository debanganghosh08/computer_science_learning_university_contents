# MOB403 · Mobile System Design

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [MOB303](../../year_3/MOB303_cross_platform_apps_flutter_and_react_native/README.md) | [MOB501](../../year_5/MOB501_frontier_seminar_wearables_ar_and_ambient/README.md), [CAR401](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) |

Part of the [Mobile Engineering major](../../README.md). The catalog lists MOB303; the course also builds directly on [MOB304](../../year_3/MOB304_mobile_architecture_offline_first_and_sync/README.md) (sync, caching) and [MOB305](../../year_3/MOB305_mobile_integrations_payments_maps_notifications/README.md) (push, payments, location). [BE301 API Design](../../../backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md) is a useful elective beforehand. Taken in the same semester as CAR401, which runs the general system design interviews.

## Why this course matters now

Mid-level and senior mobile loops include a mobile system design round: design an offline-first chat app, an image feed, a ride-hailing client or a payments screen. Strong answers, as the [MOB market page](../../../../06_career_and_market_readiness/01_market_map/roles/MOB_mobile_engineering.md) notes, cover caching, sync, pagination, background work, battery and failure states. This is not backend system design with a phone drawn on top. The client holds state, runs on an unreliable network, is killed by the OS, cannot be updated instantly and pays for every byte and every radio wake-up. AI assistants can produce a plausible architecture diagram in seconds, and design rounds are one of the places where interviewers now probe hardest, because a confident diagram is easy to generate and hard to defend. This course trains the reasoning behind the diagram: estimates, contracts, data flow, failure handling and trade-offs, practised on the systems people use every day, and then proved by building a working client.

## Learning outcomes

By the end you can:

1. **Run** a 45–60 minute mobile system design discussion: clarify requirements, estimate, sketch, deep-dive and state trade-offs.
2. **Design** mobile-friendly APIs: REST, GraphQL or gRPC choices, backend-for-frontend, cursor pagination, versioning for old clients and idempotent writes.
3. **Design** the client data layer: normalised caches, the database as source of truth, prefetching and invalidation.
4. **Design** image and video pipelines with memory and data budgets.
5. **Choose** real-time mechanisms (WebSocket, server-sent events, MQTT, long polling, push) by battery, latency and reliability.
6. **Design** complete clients for chat, feed, ride-hailing, offline-first notes and high-traffic checkout, and **defend** each against failure scenarios.
7. **Integrate** cross-cutting concerns: observability, feature flags, security, accessibility, localisation and modularisation.
8. **Prove** a design by building a client that meets measured targets.

## Chapters and lessons

### Chapter 1 · The method (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Requirements | Functional scope; non-functional: offline, latency, battery, data, security, accessibility; what to ask first | Turn "design WhatsApp" into 10 clarifying questions |
| 1.2 Estimates | Daily active users, sessions, payload sizes, bytes per session, data cost per user, storage on device | Estimate monthly data use of a feed for a user on a 1.5 GB/day plan (illustrative) |
| 1.3 The client diagram | UI, state, repositories, local store, sync engine, network layer, background workers, push | Draw the client for a weather app in 10 minutes |
| 1.4 Trade-off language | Stating options, choosing, and naming what you give up | Rewrite three weak answers into trade-off statements |

**Check your understanding:** Why should a mobile design start with offline and failure requirements? Which estimates change the design, and which are decoration? How long should you spend on the diagram before deep-diving?

### Chapter 2 · API design for mobile (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Protocol choice | REST, GraphQL and gRPC on mobile: payload size, caching, tooling, schema evolution | Choose for three apps and justify |
| 2.2 Backend for frontend | Screen-shaped endpoints, aggregation, reducing round trips on high-latency links | Collapse five calls on a home screen into one |
| 2.3 Pagination | Offset vs cursor; Relay-style connections; stable ordering under inserts; deduplication | Show offset pagination duplicating items during inserts |
| 2.4 Old clients | Additive changes, versioning, minimum supported version, feature negotiation | Plan a breaking change with 15% of users on old versions |
| 2.5 Writes and errors | Idempotency keys, error contracts, retries the client may make | Specify the error contract for checkout |

**Check your understanding:** Why does cursor pagination stay correct when items are inserted? When does GraphQL's flexibility hurt mobile caching? What must an API promise to a client that never updates?

### Chapter 3 · The client data layer (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Normalised caches | One copy of each entity; updating everywhere it appears (Apollo, Relay, hand-rolled) | Like a post in a feed and see it update in the detail screen |
| 3.2 Database as source of truth | Paging from the database with remote mediators (Android Paging 3), observation on iOS | Feed pages from Room or SwiftData backed by network |
| 3.3 Invalidation and freshness | TTLs, server push invalidation, stale-while-revalidate, "pull to refresh" semantics | Write freshness rules for five screens |
| 3.4 Prefetching | Viewport-aware prefetch, next-page prefetch, Wi-Fi and charging conditions | Prefetch without exceeding a data budget |

**Check your understanding:** What bug appears when the same entity is cached in two places? Why page from the database rather than straight from the network? When is prefetching wasteful?

### Chapter 4 · Images and media (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Image pipeline | Request → memory cache → disk cache → network; decode and downsample to view size; pooling | Design the cache sizes for a 2 GB phone |
| 4.2 Formats and CDNs | WebP, AVIF, HEIC; server-side resizing parameters; placeholders such as BlurHash | Halve image bytes per session with resized URLs |
| 4.3 Video | HLS and DASH adaptive bitrate, preloading, autoplay budgets, Media3/ExoPlayer and AVPlayer | Design autoplay that respects Data Saver |
| 4.4 Uploads | Compression on device, resumable and chunked uploads, background transfer | Resumable upload that survives app kill |

**Check your understanding:** Why does decoding a 12-megapixel photo into a 200-pixel cell crash low-end phones? What does adaptive bitrate trade? Why must uploads be resumable on mobile?

### Chapter 5 · Real-time and background communication (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Options | WebSocket, server-sent events, MQTT, long polling, push notifications; their battery and reliability profiles | Compare four mechanisms for a live score feature |
| 5.2 Connection management | Heartbeats, reconnect with exponential backoff and jitter, connection state in the UI | Reconnect logic tested with random disconnects |
| 5.3 Push as a wake-up | Push to trigger sync, not to carry state; collapsing; quotas and throttling | Design push for a 10-message burst |
| 5.4 Ordering and delivery | Sequence numbers, acknowledgements, at-least-once with deduplication | Detect and fill a gap in a message stream |

**Check your understanding:** Why should a closed app not hold a WebSocket? What happens to a mobile connection when the phone switches from Wi-Fi to mobile data? Why is push "best effort"?

### Chapter 6 · Case: chat (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Requirements and estimates | One-to-one and group chat, media, receipts, offline send, multi-device | Full requirements and estimates in 10 minutes |
| 6.2 Message lifecycle | Client IDs, states (sending, sent, delivered, read), outbox, ordering per conversation | State diagram for a message |
| 6.3 Sync and history | Delta sync after offline periods, pagination of history, local search (SQLite FTS) | Design catch-up after 3 days offline |
| 6.4 End-to-end encryption (overview) | The Signal Protocol as used by WhatsApp (published whitepaper): keys per device, what servers can and cannot see, multi-device impact | Explain what changes in the design when the server cannot read messages |
| 6.5 Groups and media | Fan-out, large groups, media upload once and share keys | Design a 1,000-member group send |

**Check your understanding:** How do you keep message order when two devices send at once? What does end-to-end encryption remove from the server's abilities, such as search? Why do read receipts in large groups need special handling?

### Chapter 7 · Case: feed (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Feed model | Server-ranked feed, cursor pages, deduplication across sessions, inserting new items | Design the feed API and client cache |
| 7.2 Scroll performance | Item recycling, image prefetch, layout cost, video autoplay limits | Scroll budget for a 2 GB phone |
| 7.3 Impressions and logging | Viewability rules, batched logging, offline queue | Design impression logging that never blocks scrolling |
| 7.4 Offline and cold start | Cached first page, freshness indicator, background refresh | First meaningful paint from cache under 1 second (design) |

**Check your understanding:** Why does a feed client need deduplication if the server already ranks? When should a video start downloading? What makes impression counts wrong on mobile?

### Chapter 8 · Case: ride-hailing and hyperlocal delivery (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 State machines | Rider, driver and trip states; cancellations; payment at the end | Trip state machine with every cancel path |
| 8.2 Location at scale | Update cadence vs battery, map-matching, smoothing, server-side geo-indexing (Uber's H3 as a public example) | Choose update intervals for waiting, en route and arrived |
| 8.3 Live updates | Socket while foreground, push when background, polling fallback, ETA updates | Design delivery of a driver-assigned event within 5 s |
| 8.4 Bad networks | Lost requests during booking, duplicate bookings, offline recovery | Make "Book" idempotent end to end |
| 8.5 Driver app specifics | Long sessions, background location policies, battery and heat in a car mount | Battery budget for a 10-hour driver shift |

**Check your understanding:** What must never happen if the booking request times out? How often should a driver's location be sent, and what decides it? Why do driver apps fight the OS more than rider apps?

### Chapter 9 · Case: offline-first notes (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Data model | Notes, attachments, folders, sharing; client IDs | Schema and sync scope |
| 9.2 Conflicts | Server-authoritative merges vs CRDTs for text; user-visible conflicts | Choose and defend for plain-text and rich-text notes |
| 9.3 Search and attachments | On-device full-text search, lazy attachment download, storage budgets | Search 50,000 notes offline |
| 9.4 Privacy | Local encryption, end-to-end encryption trade-offs for sharing and search | Design encrypted sharing |

**Check your understanding:** Why might a notes app choose CRDTs for body text but not for folder structure? What does end-to-end encryption cost in features? How do you keep storage from growing forever?

### Chapter 10 · Case: checkout during a flash sale (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Load from the client's side | Thundering herds at sale start, client-side jitter, queue screens, cached catalogue | Design the "sale starts at noon" behaviour |
| 10.2 Payments | UPI intent and gateway flows from MOB305; pending states; idempotent order creation | Payments sequence for a sale with retries |
| 10.3 Degradation | Kill switches, disabling non-essential calls, static fallbacks | Plan what the app turns off at 10× load |
| 10.4 Inventory honesty | Reservations and timeouts; what the client may show as "in stock" | Design the cart-hold experience |

**Check your understanding:** How can a million clients retrying at once take down the backend, and how does jitter help? What should the app show while payment is pending? Which features would you switch off first?

### Chapter 11 · Cross-cutting concerns and scale (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Observability | Client logs, traces (OpenTelemetry mobile SDKs), sampling, privacy of telemetry | Add tracing for one user journey |
| 11.2 Flags, experiments and kill switches | Where they live in the design; defaults at cold start | Add flags to your chat design |
| 11.3 Security and accessibility | Token handling, pinning decisions, MASVS references; screen readers, text scaling, Indian scripts | Review a design for both |
| 11.4 Many teams, one app | Modularisation, design systems, release trains, mini-app platforms (for example WeChat Mini Programs) | Propose an architecture for 100 engineers |

**Check your understanding:** What telemetry is too expensive or too private to collect? Why do flags need safe defaults when config cannot load? What changes when a design must support 20 feature teams?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Requirements and estimates drills | — |
| 2 | 2 | Lab 2 · API contracts and pagination | Pagination bug demo |
| 3 | 3 | Lab 3 · Normalised cache | **P1 due** |
| 4 | 4 | Lab 4 · Image pipeline budgets | — |
| 5 | 5 | Lab 5 · Reconnect and gap filling | — |
| 6 | 6 | Mock interview 1 (chat) | — |
| 7 | 6 | Lab 6 · Chat client core | Mid-term (AI off, design on paper) |
| 8 | 7 | Mock interview 2 (feed) | — |
| 9 | 8 | Lab 7 · Location cadence and battery | — |
| 10 | 8 | Mock interview 3 (ride-hailing) | **P2 due** |
| 11 | 9 | Lab 8 · Offline search | — |
| 12 | 10 | Lab 9 · Flash-sale client behaviour | — |
| 13 | 11 | Lab 10 · Observability and flags | — |
| 14 | 11 | Mock interview 4 (candidate's choice) | **P3 due** |
| 15 | Review | Oral defence of P3 | Final: two live design rounds (AI off) |

## Working with AI in this course

- **Use AI for:** generating a first list of requirements or failure scenarios to compare with yours; acting as a mock interviewer that asks follow-up questions; critiquing your design document; drafting API schemas and sequence diagrams.
- **Do without AI (drills):** every mock interview; estimates; the first draft of every design; the mid-term and final. In design rounds you must reason live.
- **Verify AI output by:** (1) checking each claim about platform behaviour (background limits, push delivery, caching) against official docs; (2) running the numbers yourself; (3) asking "what happens when this fails?" for every arrow in the diagram; (4) building the riskiest part (P2, P3) and measuring it.
- **Where AI still fails here (collect your own evidence):** generated mobile designs often keep sockets open in the background, treat push as reliable, use offset pagination for live feeds, ignore old clients, and skip battery and data estimates. Keep a list of such errors from your critique sessions; it becomes your interview checklist.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| Projects P1–P3 | 35% |
| Mock interviews (4, scored with a rubric) | 10% |
| Mid-term (AI off, design on paper) | 10% |
| Final: two live design rounds (AI off) + oral defence of P3 | 25% |

**Mastery gate.** You pass when you can, with AI tools off, in 60 minutes and with an examiner probing: design a mobile client for a system you have not practised (for example, a live-streaming app or a hospital appointment app), covering requirements, estimates, API contract, data layer, sync, real-time updates, failure handling, battery and data use, and security, and score at least "hire" on the rubric for two different examiners.

## Industry reality

The typical mobile loop described on the [market page](../../../../06_career_and_market_readiness/01_market_map/roles/MOB_mobile_engineering.md) includes a design round on offline-first chat, an image feed or a payments screen. Public sources show real decisions behind these cases: WhatsApp's security whitepaper describes Signal Protocol encryption on every device; Uber open-sourced H3, the hexagonal geo-index used for location-based systems; the Relay connections specification is a widely used cursor-pagination contract. Treat any company detail not in a public source as unknown, and label invented scenarios as illustrative.

**Interview questions from this course**

1. *Design a WhatsApp-like chat client.* Strong answer: message lifecycle with client IDs and an outbox; ordering and acknowledgements; socket in foreground and push as wake-up; delta sync after long offline periods; media upload; encryption's effect on server features; battery and data estimates.
2. *Design an Instagram-like feed for low-end phones on slow networks.* Strong answer: cursor pagination with deduplication; database-backed paging; image downsampling and resized CDN URLs; video autoplay limits and Data Saver; impression logging off the main thread; cached first page.
3. *Design a ride-hailing rider app.* Strong answer: trip state machine; idempotent booking; location cadence by state; socket plus push plus polling fallback; ETA updates; payment at trip end; behaviour on network loss.
4. *Design an offline-first notes app with sharing.* Strong answer: local store as source of truth; conflict strategy by data type; on-device search; attachment budgets; encryption trade-offs.
5. *Your app must survive a flash sale with 20× normal traffic.* Strong answer: client jitter and backoff; cached catalogue; queue screens; idempotent order creation; pending payment states; kill switches; what is turned off first.

## Resources (free first)

- **Mobile design practice:** Mobile System Design (open-source guide by Alex Lementuev) — https://github.com/weeeBox/mobile-system-design
- **Specifications:** Relay cursor connections — https://relay.dev/graphql/connections.htm ; RFC 9111 HTTP caching — https://www.rfc-editor.org/rfc/rfc9111 ; RFC 6455 WebSocket — https://www.rfc-editor.org/rfc/rfc6455 ; RFC 8216 HTTP Live Streaming — https://www.rfc-editor.org/rfc/rfc8216 ; MQTT — https://mqtt.org/
- **Platform:** Android Paging 3 — https://developer.android.com/topic/libraries/architecture/paging/v3-overview ; Media3 — https://developer.android.com/media/media3 ; Apple AVFoundation — https://developer.apple.com/av-foundation/
- **Case material:** WhatsApp Encryption Overview (security whitepaper) — https://www.whatsapp.com/security/WhatsApp-Security-Whitepaper.pdf ; Signal protocol documentation — https://signal.org/docs/ ; Uber H3 — https://h3geo.org/ ; BlurHash — https://blurha.sh/ ; OpenTelemetry — https://opentelemetry.io/
- **Paid, optional:** Tjeerd in 't Veen, *Mobile System Design* (self-published). The open-source guide above and the course cases cover the interview material.

## Sources

- MOB market page (hiring loop and design-round topics) — [roles/MOB_mobile_engineering.md](../../../../06_career_and_market_readiness/01_market_map/roles/MOB_mobile_engineering.md) (checked 2026-10)
- WhatsApp security whitepaper; Signal documentation; Uber H3; Relay connections specification — as listed under Resources (checked 2026-10)
- Android Developers, Reduce your app size (emerging-market networks) — https://developer.android.com/topic/performance/reduce-apk-size (checked 2026-10)

_Last reviewed: 2026-10_
