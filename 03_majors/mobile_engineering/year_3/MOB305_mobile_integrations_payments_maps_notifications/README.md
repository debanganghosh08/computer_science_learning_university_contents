# MOB305 · Mobile Integrations: Payments, Maps, Notifications and Identity

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [FND111](../../../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [MOB403](../../year_4/MOB403_mobile_system_design/README.md), [MOB404](../../year_4/MOB404_mobile_analytics_experimentation_and_growth/README.md), [OV10](../../../../04_overlaps/OV10_fintech_systems_engineering/README.md) |

Part of the [Mobile Engineering major](../../README.md). Labs use Android or iOS (both for P3). All payments run in provider test modes or a course simulator; no real money or real credentials are ever used. [CS213 Security Foundations](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) supplies the OAuth and crypto background.

## Why this course matters now

Most mobile apps make money, move people or deliver things, so most of the hard bugs live where the app meets a payment network, a map, a push service or an identity provider. In India, UPI processed 24.07 billion transactions in September 2026, and apps reach it by launching a UPI app through an intent. NPCI stopped peer-to-peer "collect requests" from 1 October 2025 to curb fraud, so flows built on them had to change. Identity changed too: Android's Credential Manager replaces the legacy Google Sign-In, One Tap and Smart Lock APIs and makes passkeys first-class. Apple's guideline 4.8 requires an equivalent privacy-preserving login option when you offer a third-party one. Firebase Dynamic Links shut down on 25 August 2025, breaking deferred deep links in many apps. AI assistants paste SDK quick-starts well. They also confidently treat a payment SDK's success callback as proof of payment, store tokens in plain preferences and use deprecated sign-in APIs. This course teaches the end-to-end contract of each integration: what the client may trust, what only the server may decide, and how to test the failures.

## Learning outcomes

By the end you can:

1. **Evaluate** a third-party SDK for size, startup cost, permissions and data collection, and **wrap** it behind an interface you can replace.
2. **Implement** UPI intent payments and gateway checkouts (Razorpay, Stripe) where the server, not the client, confirms payment.
3. **Implement** store billing (Google Play Billing, StoreKit 2) for digital goods with server-side verification, and **apply** store payment rules correctly.
4. **Build** location and map features that meet accuracy needs within battery and permission limits.
5. **Deliver** push notifications through FCM and APNs, and **measure** delivery instead of assuming it.
6. **Configure** verified deep links (Android App Links, iOS Universal Links) and route them safely.
7. **Implement** sign-in with OAuth 2.0 and PKCE, Sign in with Google and Apple, OTP and passkeys, with tokens stored in Keystore or Keychain.
8. **Test** integrations with sandboxes, mock servers and fault injection, and **document** their privacy and compliance impact.

## Chapters and lessons

### Chapter 1 · Integration engineering (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Choosing an SDK | Download size, initialisation cost, transitive dependencies, permissions, data collected, maintenance | Audit three SDKs; score them in a table |
| 1.2 Wrapping and isolation | Interfaces around SDKs, lazy initialisation, kill switches | Wrap an analytics SDK so it can be removed in one commit |
| 1.3 Trust boundaries | The client is untrusted: secrets never ship in the app; the server decides | Find three secrets in a sample app's resources and move them server-side |
| 1.4 Sandboxes and test modes | Provider test modes, simulators, test cards and test VPAs | Set up test accounts for every integration in this course |

**Check your understanding:** Why is an API key inside an app binary public? What does a kill switch protect you from? Why initialise an SDK lazily?

### Chapter 2 · Payments I: UPI (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 How UPI works | Payer and payee PSPs, NPCI switch, banks, VPAs; P2P vs P2M; why the app never sees bank credentials | Draw a UPI payment sequence diagram |
| 2.2 Intent flow | `upi://pay` deep links, app choosers, Android package visibility (`<queries>`), iOS `LSApplicationQueriesSchemes` | Launch test UPI apps from Android and iOS |
| 2.3 QR and collect | Static and dynamic QR; P2P collect ended from 1 Oct 2025; merchant collect continues | Rewrite a P2P collect flow as an intent or QR flow |
| 2.4 The result is not the truth | The UPI app's response can be missing or wrong; server-side status check and webhooks; pending states | Kill the app after paying and still fulfil the order exactly once |
| 2.5 Recurring and small payments | UPI AutoPay mandates and UPI Lite (concepts, user experience, failure handling) | Design the mandate-revoked flow |

**Check your understanding:** Why must fulfilment wait for the server's confirmation? What should the user see if the UPI app returns nothing? Why did NPCI remove P2P collect, and what replaced it in your app?

### Chapter 3 · Payments II: gateways and stores (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Gateway checkout | Server creates the order; client opens Razorpay or Stripe checkout; server verifies the signature (Razorpay HMAC) or PaymentIntent status; webhooks | Complete a test payment end to end with signature verification |
| 3.2 Idempotency and retries | Idempotency keys on order creation; double taps; webhook duplicates | Survive 10 duplicate webhooks with one fulfilment |
| 3.3 Cards and compliance | Tokenised card-on-file in India (RBI, from Oct 2022), PCI DSS scope: never touch raw card numbers | Show that no card data reaches your logs or server |
| 3.4 Store billing | Google Play Billing (acknowledge within 3 days or the purchase is refunded), StoreKit 2 transactions, server verification, subscriptions | Sell a test subscription on one platform with server verification |
| 3.5 Which rule applies | Apple 3.1.1 (in-app purchase for digital unlocks) vs 3.1.3(e) (other methods for physical goods and services); Google Play's payments policy | Classify 12 products by required payment method |

**Check your understanding:** Why is a client-side "success" callback insufficient for a gateway payment? What happens if you forget to acknowledge a Play purchase? A tutoring app sells live classes held online: which rule applies, and why?

### Chapter 4 · Maps and location (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Location APIs | Fused Location Provider priorities; Core Location and `CLLocationUpdate`; accuracy vs battery | Log accuracy and battery for three priority settings over 30 minutes |
| 4.2 Permissions and policy | Approximate vs precise; foreground vs background; Play's background-location declaration; iOS "Always" | Make a delivery-tracking feature work with only foreground, approximate access |
| 4.3 Geofencing | Limits (up to 100 geofences per app on Android, 20 regions on iOS), dwell vs enter, reliability | Build store-arrival reminders; measure trigger delay |
| 4.4 Map SDKs | Google Maps SDK, MapKit, MapLibre with OpenStreetMap, Indian providers such as Mappls; cost, offline tiles, licensing | Render the same route in two SDKs; compare size and startup cost |
| 4.5 Indian addresses | Landmark-heavy addresses, pin codes, DIGIPIN (India Post's geocoded address grid); confirming a drop pin | Design an address-entry screen that reduces failed deliveries |

**Check your understanding:** Why does requesting high accuracy drain battery even when the user is still? What must you show Play before using background location? Why do delivery apps ask users to confirm a pin on the map?

### Chapter 5 · Push notifications (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 FCM | Registration tokens and refresh, the HTTP v1 API with short-lived OAuth 2.0 tokens, notification vs data messages, 4,096-byte payloads, priority and deprioritisation | Send data and notification messages from a server you write |
| 5.2 APNs | Token-based authentication (.p8 keys), push types, priority, collapse IDs, payload limits; the 2025 server certificate change | Send pushes to a test iPhone from your server |
| 5.3 Permission and channels | Android 13 runtime permission; channels and importance; iOS provisional authorisation; asking at the right moment | Raise opt-in rate in a usability test with a better prompt moment |
| 5.4 Rich and live notifications | Images, actions, grouping; iOS Live Activities and Android 16 Live Updates | A delivery-status Live Activity or progress notification |
| 5.5 Delivery is best-effort | Measuring sent vs delivered vs opened; fallbacks (in-app sync, SMS for critical alerts) | A delivery report for 500 test pushes |

**Check your understanding:** Why should critical state never live only in a push payload? When is a data message better than a notification message? What happens to tokens when a user reinstalls?

### Chapter 6 · Deep links (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Verified links | Android App Links (`assetlinks.json`, `autoVerify`) and iOS Universal Links (`apple-app-site-association`); custom schemes and their risks | Make links verify on both platforms; debug a failing one |
| 6.2 Routing | Mapping URLs to screens and back stacks; logged-out and stale links | Route 15 link types, including expired ones |
| 6.3 Deferred deep links | Restoring context after install; Play Install Referrer API; life after Firebase Dynamic Links | Rebuild an invite flow without Dynamic Links |
| 6.4 Link security | Validating parameters, never trusting links for authorisation, open-redirect and intent-redirection risks | Review a deep-link handler and fix three flaws |

**Check your understanding:** Why did links that worked on Android 11 open in the browser on Android 12? What should happen when a logged-out user opens a link to an order? Why is a custom URL scheme not proof that the link came from your website?

### Chapter 7 · Identity I: sign-in and tokens (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 OAuth for native apps | RFC 8252, PKCE (RFC 7636), system browser vs WebView, Custom Tabs and `ASWebAuthenticationSession` | Implement authorization code + PKCE against a test identity provider |
| 7.2 Sign in with Google | Credential Manager on Android (replacing legacy Google Sign-In, One Tap and Smart Lock); Google sign-in on iOS | Migrate a legacy sign-in sample to Credential Manager |
| 7.3 Sign in with Apple | Guideline 4.8; private relay emails (new relay domain from Aug 2026); revocation | Add Sign in with Apple and handle a hidden email |
| 7.4 Tokens and sessions | Access and refresh tokens, Keystore/Keychain storage, refresh races, logout and server-side revocation, account deletion | Fix a refresh-token race with 10 parallel requests |

**Check your understanding:** Why are WebViews unsuitable for OAuth sign-in? What goes wrong when two requests refresh a token at the same time? What must account deletion remove, and what may you keep?

### Chapter 8 · Identity II: OTP and passkeys (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Phone OTP | SMS Retriever and SMS User Consent APIs (no SMS read permission); iOS one-time-code autofill; Play's SMS permission policy | One-tap OTP fill on both platforms |
| 8.2 OTP abuse (defensive) | SMS pumping and cost attacks, rate limits, device and IP throttling, resend timers | Add server rate limits; show an abuse script being blocked |
| 8.3 Passkeys | WebAuthn/FIDO2 basics, Credential Manager and AuthenticationServices, associated domains, account recovery | Add passkey sign-in alongside OTP |
| 8.4 Regulated identity | eKYC and DigiLocker integrations happen through regulated partners; consent and minimal data (concepts only) | Write the data-minimisation note for a KYC step |

**Check your understanding:** Why is SMS OTP weaker than a passkey? What does the SMS Retriever app hash prevent? How should account recovery work when a passkey device is lost?

### Chapter 9 · Testing and observing integrations (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Mock servers | MockWebServer, WireMock, recorded fixtures; contract tests against provider schemas | A payment test suite that runs offline in CI |
| 9.2 Failure injection | Timeouts, duplicate callbacks, out-of-order webhooks, revoked permissions, expired tokens | Run 50 interrupted-payment scenarios |
| 9.3 Funnels per integration | Payment success rate by UPI app, push opt-in and delivery, sign-in conversion by method | Dashboard of integration health from test data |
| 9.4 Kill switches and fallbacks | Remote flags to disable a failing provider; graceful degradation | Switch payment providers without a release |

**Check your understanding:** Why are provider sandboxes not enough for testing failures? Which metric tells you a UPI app is having an outage? What should the app do if the map SDK fails to load?

### Chapter 10 · Privacy and compliance (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Store disclosures | Play Data safety and Apple privacy labels for each SDK; Apple 5.1.2 consent | Complete both disclosures for P3 with evidence |
| 10.2 India's DPDP Rules | Notice, consent and breach duties; phased timeline to 2027 | Write a consent notice for location and contacts |
| 10.3 Payments compliance | PCI DSS scope, RBI tokenisation, what an app team owns vs the gateway | Produce a data-flow diagram showing card data never touches you |
| 10.4 Integration review | Threat model of P3's integrations | Peer review with a checklist |

**Check your understanding:** Who is responsible when an SDK collects data you did not declare? What must a valid consent notice contain? Which parts of PCI DSS does a tokenised checkout remove from your scope?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · SDK audit and wrapping | SDK scorecard |
| 2 | 2 | Lab 2 · UPI intent flow | — |
| 3 | 2 | Lab 2 (cont.) · Kill-after-pay | **P1 due** |
| 4 | 3 | Lab 3 · Gateway with signature verification | — |
| 5 | 4 | Lab 4 · Location and geofencing | Battery log |
| 6 | 5 | Lab 5 · FCM and APNs from your server | — |
| 7 | 5 | Lab 5 (cont.) | Mid-term (AI off) |
| 8 | 6 | Lab 6 · Verified deep links | — |
| 9 | 7 | Lab 7 · OAuth with PKCE | — |
| 10 | 7 | Lab 7 (cont.) · Token refresh race | **P2 due** |
| 11 | 8 | Lab 8 · OTP and passkeys | — |
| 12 | 9 | Lab 9 · Failure injection | — |
| 13 | 10 | Lab 10 · Privacy disclosures | — |
| 14 | 10 | Integration review | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** reading long SDK documentation and summarising required steps; drafting server endpoints for order creation and webhooks; generating test fixtures for webhook payloads; drafting privacy disclosures (then checking every line against the SDK's own documentation).
- **Do without AI (drills):** the UPI and gateway sequence diagrams; signature verification code; the token refresh race fix; the mid-term and final.
- **Verify AI output by:** (1) tracing every money or identity decision to the server; (2) running the failure-injection suite (kill after pay, duplicate webhooks, expired tokens); (3) checking each API against current docs, because sign-in and push APIs changed in 2023–2025 (legacy Google Sign-In, legacy FCM APIs, Dynamic Links); (4) inspecting network traffic with a proxy for leaked tokens or personal data.
- **Where AI still fails here (collect your own evidence):** record each generated snippet that trusted a client callback for payment, verified a signature on the client with the secret key, stored tokens in plain `SharedPreferences` or `UserDefaults`, used a deprecated sign-in or push API, or requested `READ_SMS` for OTP. Bring the log to the integration review.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 25% |
| Integration review | 5% |

**Mastery gate.** You pass when you can, with AI tools off: (1) draw and explain the complete UPI intent and gateway payment flows, including every failure path and who decides the final state; (2) implement server-side signature verification and an idempotent webhook handler in 45 minutes; (3) show your P3 completing 50 interrupted payments with zero double fulfilments and every payment resolved.

## Industry reality

UPI volumes make payment reliability a daily engineering concern for Indian apps (24.07 billion transactions in September 2026, NPCI data as reported). Razorpay's documentation describes the intent flow as showing intent-capable UPI apps and returning the result to your activity, and requires iOS apps to declare the UPI app URL schemes they query. Apple's guideline 4.8 and Google's move to Credential Manager mean sign-in code written before 2024 often needs rework. Firebase Dynamic Links' shutdown in August 2025 forced many apps to rebuild invite and referral flows.

**Interview questions from this course**

1. *Design the UPI payment flow for a food order. The user pays, then the app is killed.* Strong answer: server creates the order with an idempotency key; intent launch; client result treated as a hint; server status check and webhooks decide; pending state with a timeout; fulfilment idempotent; refund path; metrics by UPI app.
2. *How do you make sure a ride status update reaches the user?* Strong answer: high-priority data message or APNs alert; foreground connection when the app is open; sync on resume as a fallback; never rely on push alone for state; measures delivery and latency.
3. *Implement sign-in with Google and Apple. Where do tokens live, and what happens at logout and account deletion?* Strong answer: Credential Manager and AuthenticationServices; server-side token exchange; Keystore/Keychain; single-flight refresh; server revocation; guideline 4.8 and 5.1.1(v).
4. *App Links work on some devices but not others. Debug it.* Strong answer: checks `assetlinks.json` content-type, redirects and fingerprints; `autoVerify`; Android 12+ verification behaviour; `pm get-app-links`; CDN caching; tests for both release and debug signing keys.
5. *Design phone OTP login that is secure and converts well.* Strong answer: SMS Retriever/one-time-code autofill; rate limits and abuse controls; resend timers; fallback channels; passkeys as the next step; no SMS read permission.

## Resources (free first)

- **Payments:** NPCI (UPI product pages, circulars and monthly statistics) — https://www.npci.org.in/ ; Razorpay docs (UPI intent, Android and iOS SDKs, webhooks) — https://razorpay.com/docs/ ; Stripe mobile docs — https://docs.stripe.com/payments/accept-a-payment ; Google Play Billing — https://developer.android.com/google/play/billing ; StoreKit — https://developer.apple.com/storekit/
- **Location and maps:** Android location — https://developer.android.com/develop/sensors-and-location/location ; Core Location — https://developer.apple.com/documentation/corelocation ; MapLibre — https://maplibre.org/ ; Google Maps SDK for Android — https://developers.google.com/maps/documentation/android-sdk
- **Push:** Firebase Cloud Messaging — https://firebase.google.com/docs/cloud-messaging ; Apple User Notifications — https://developer.apple.com/documentation/usernotifications
- **Deep links:** Android App Links — https://developer.android.com/training/app-links ; Universal Links — https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app
- **Identity:** Credential Manager — https://developer.android.com/identity/sign-in/credential-manager ; Sign in with Apple — https://developer.apple.com/sign-in-with-apple/ ; passkeys — https://developer.apple.com/passkeys/ ; SMS Retriever — https://developers.google.com/identity/sms-retriever/overview ; RFC 8252 — https://www.rfc-editor.org/rfc/rfc8252 ; RFC 7636 — https://www.rfc-editor.org/rfc/rfc7636 ; OWASP MASVS-AUTH — https://mas.owasp.org/MASVS/

## Sources

- StartupTalky, UPI transactions September 2026 (NPCI data) — https://startuptalky.com/upi-transactions-september-2026/ (checked 2026-10)
- Business Today, NPCI ends P2P collect from 1 Oct 2025 (13 Aug 2025) — https://www.businesstoday.in/personal-finance/banking/story/npci-to-tighten-upi-rules-peer-to-peer-collect-feature-to-end-in-october-489244-2025-08-13 (checked 2026-10)
- Razorpay, UPI Intent documentation — https://razorpay.com/docs/payments/payment-methods/upi/upi-intent/ (checked 2026-10)
- Android Developers, Credential Manager — https://developer.android.com/identity/sign-in/credential-manager (checked 2026-10)
- Apple, App Review Guidelines (4.8, 3.1.1, 3.1.3(e), 5.1.1(v), 5.1.2) — https://developer.apple.com/app-store/review/guidelines/ ; Apple Developer News, new Sign in with Apple relay domain (24 Aug 2026) — https://developer.apple.com/news/ ; APNs certificate update (2025) — https://developer.apple.com/news/upcoming-requirements/ (checked 2026-10)
- Firebase Cloud Messaging overview (4,096-byte payload) — https://firebase.google.com/docs/cloud-messaging ; Firebase Dynamic Links FAQ (shutdown 25 Aug 2025) — https://firebase.google.com/support/dynamic-links-faq (checked 2026-10)
- Press Information Bureau, DPDP Rules 2025 (Nov 2025) — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf (checked 2026-10)

_Last reviewed: 2026-10_
