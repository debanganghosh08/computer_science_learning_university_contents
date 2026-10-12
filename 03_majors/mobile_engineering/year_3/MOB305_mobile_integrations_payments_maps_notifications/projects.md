# MOB305 · Labs and projects

All payment work uses provider test modes (Razorpay, Stripe, Google Play and StoreKit sandboxes) or the course's payment simulator, which can delay, drop and duplicate callbacks and webhooks on a seed. No real money, real cards or real bank credentials are ever used. Identity labs use a test identity provider and test accounts only. Labs 3 and 7 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · SDK audit and wrapping | Score three SDKs on size, startup cost, permissions and data collected; wrap one behind an interface with a kill switch | Scorecard; a commit that removes the SDK in one change | 4 h |
| 2 · UPI intent flow | Launch UPI apps via intent on Android and iOS; server-side status check; kill-after-pay test | Sequence diagram; video of a killed app whose order still completes once | 6 h |
| 3 · Gateway with signature verification (no AI) | Server-created order, client checkout, server HMAC verification, idempotent webhook handler | Tests: tampered signature rejected; 10 duplicate webhooks produce one fulfilment | 5 h |
| 4 · Location and geofencing | Compare location priorities; build arrival geofences | 30-minute accuracy and battery log per setting; trigger-delay measurements | 5 h |
| 5 · FCM and APNs from your server | Send data, notification and alert pushes using FCM HTTP v1 and APNs token auth | Delivery report for 500 test pushes; token-refresh handling | 6 h |
| 6 · Verified deep links | App Links and Universal Links with routing for 15 link types | `pm get-app-links` output; AASA validation; routing test results | 4 h |
| 7 · OAuth with PKCE and token refresh (no AI) | Authorization code + PKCE in a system browser; fix a refresh race | 10 parallel requests during expiry trigger exactly one refresh | 6 h |
| 8 · OTP and passkeys | One-tap OTP with SMS Retriever and iOS autofill; passkey registration and sign-in | Videos of both flows; rate-limit test against a scripted abuser | 5 h |
| 9 · Failure injection | 50 interrupted-payment scenarios; expired tokens; revoked permissions | Scenario table with expected and observed end states | 5 h |
| 10 · Privacy disclosures | Data safety form and Apple privacy label for an app with five SDKs | Forms with evidence from a proxy capture | 3 h |

## Projects

### P1 · Event tickets with links and push (L1, ~6 hours)

**Real-world inspiration:** ticketing apps send a link by SMS or WhatsApp that opens the exact ticket in the app, and a push before the doors open. This app is an illustrative scenario.

**What to build:** an event list and ticket screen with QR, verified deep links (`/event/{id}`, `/ticket/{id}`, invite links), push reminders from a small server you write, and correct routing when the user is logged out.

**Acceptance criteria:**
- **Verification:** links verify on Android (`adb shell pm get-app-links` shows "verified") and iOS (Universal Links open the app from Notes and Messages).
- **Routing:** 15 link variants (cold start, warm start, logged out, expired event, malformed ID) route correctly in automated tests.
- **Push:** 20 test pushes each open the right screen; tokens refresh after reinstall and the server stops sending to stale tokens.
- **Safety:** no link parameter can skip login or open an arbitrary URL (tests).

**Stretch goals:** deferred deep link through the Play Install Referrer API; a lock-screen Live Activity or progress notification for "doors open in 10 minutes".

**What it proves to an employer:** you can wire the two integrations every consumer app needs and handle their edge cases.

### P2 · Food-order checkout that never double-charges (L2, ~15 hours)

**Real-world inspiration:** food-delivery apps such as Swiggy and Zomato take UPI, cards and wallets at checkout, and users often switch apps, lose signal or kill the app mid-payment. This checkout and its backend are an illustrative scenario.

**What to build:** a cart and checkout with UPI intent and a Razorpay test-mode checkout (cards and UPI), with an optional Stripe test-mode path for international cards. A backend you write creates orders with idempotency keys, verifies signatures, handles webhooks and runs a status-check job. The app shows pending, success, failed and refunded states and survives being killed at any point.

**Acceptance criteria:**
- **No double fulfilment:** across the course's 50 interrupted-payment scenarios (kill after pay, network loss, duplicate and late webhooks, webhook before redirect), zero orders are fulfilled twice and zero paid orders are left unfulfilled.
- **Resolution:** every order reaches a final state (paid, failed or refunded) within 15 simulated minutes.
- **Secrets:** the gateway secret key never appears in the app; a search of the release APK or IPA for it finds nothing (scripted check).
- **Correct rules:** a written classification of what the app sells and which store payment rules apply, with the guideline or policy reference.
- **Observability:** funnel metrics (checkout started, app chosen, returned, server-confirmed) by payment method, from test runs.
- **Privacy:** Data safety form and privacy label complete and consistent with a proxy capture.

**Stretch goals:** saved cards through gateway tokenisation; partial refunds; switching payment provider with a remote flag during a simulated outage.

**What it proves to an employer:** you understand that the server decides payment truth and can prove your checkout handles failure, which Indian fintech and commerce teams test in every interview.

### P3 · Parcel or ride tracking app (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** ride and parcel apps such as Rapido, Porter and Uber combine sign-in, live location, maps, push status updates, shareable tracking links and payment at the end of the trip. Your app, its driver simulator and its backend are an illustrative scenario.

**What to build:**
- **Sign-in:** phone OTP with one-tap autofill and server-side abuse controls, plus passkeys; tokens in Keystore/Keychain; account deletion.
- **Trip:** booking, a simulated driver moving along a real road route, live map with ETA, and the customer's own location shared only during the trip, with foreground-only permission by default.
- **Notifications:** status pushes via FCM and APNs, plus an iOS Live Activity or Android progress notification during the trip.
- **Sharing:** a verified deep link that lets a friend follow the trip.
- **Payment:** UPI intent or gateway at the end of the trip, using your P2 backend.
- **Operations:** kill switches for maps, payments and push providers.

**Acceptance criteria:**
- **Real users:** a Play closed test (at least 12 testers for 14 days) or TestFlight build; crash-free users at least 99.5%.
- **Battery:** a 60-minute simulated trip with tracking on uses at most 6% battery on the reference phone; the measurement method (Battery Historian or Xcode energy report) is documented and repeatable.
- **Latency:** over 200 status pushes, push-to-screen p95 is under 5 seconds on Wi-Fi and under 15 seconds on a throttled mobile profile; the app catches up correctly when a push is lost.
- **Abuse controls:** a scripted client attempting 100 OTP sends per minute is throttled after the configured limit, and the cost per blocked attempt is reported.
- **Privacy:** location sharing stops when the trip ends (verified in a proxy capture and in the server logs); disclosures match observed traffic.
- **Payment correctness:** the P2 failure suite still passes from inside this app.
- **Write-up:** integration architecture, failure-mode table for every provider, and the measured numbers above.

**Stretch goals:** offline maps for a city with MapLibre; trip-share links that expire; a watch complication with the ETA.

**What it proves to an employer:** you can integrate payments, location, push and identity into one product, respect battery and privacy, and prove each integration handles failure. That covers most of the mobile work at mobility, delivery and commerce companies.

## Feeds into

- [MOB403 Mobile System Design](../../year_4/MOB403_mobile_system_design/README.md): the ride-hailing and payments design cases build on P2 and P3.
- [MOB404 Mobile Analytics, Experimentation and Growth Engineering](../../year_4/MOB404_mobile_analytics_experimentation_and_growth/README.md): push strategy, deep-link attribution and checkout funnels.
- [OV10 FinTech Systems Engineering](../../../../04_overlaps/OV10_fintech_systems_engineering/README.md) for students specialising in payments.
- The [Mobile Engineering flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/MOB_mobile_engineering.md).
