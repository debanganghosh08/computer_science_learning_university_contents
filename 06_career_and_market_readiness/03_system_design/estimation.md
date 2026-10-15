# Back-of-the-envelope estimation

An estimate is not about getting the exact number. It is about finding which resource runs out first (CPU, memory, disk, network, GPU memory, a single hot key) and by how much, using numbers you can defend. Interviewers check three things: that you state assumptions, that the arithmetic is right within an order of magnitude, and that you *use* the result to make a design decision.

The theory and more drills are in [SWE401 chapter 2](../../03_majors/software_engineering/year_4/SWE401_large_scale_system_design/README.md) and [BE402 chapter 11](../../03_majors/backend_engineering/year_4/BE402_scalability_and_performance_caching_sharding/README.md). Latency and throughput reference numbers are in [building_blocks.md](building_blocks.md#0-latency-numbers-every-engineer-should-know).

## The method in seven steps

1. **Start from a published or stated volume** (users, transactions per month, concurrent viewers). Say where it comes from, or label it "assumed".
2. **Convert to an average rate.** Divide by seconds in the period.
3. **Apply a peak factor with a reason.** "Peak = 2× average" is a habit, not evidence. Ticket openings, match finishes, salary days and festival sales produce 10–100× spikes concentrated in seconds.
4. **Split reads and writes.** They scale differently and often go to different stores.
5. **Multiply by size** for storage and bandwidth. Include replication, indexes and metadata.
6. **Find the bottleneck.** Compare each number with what one machine or one partition can do ([building_blocks.md throughput table](building_blocks.md#throughput-ballparks)).
7. **Decide something.** "So one Postgres primary is enough for writes, but reads need a cache", or "so the hot key needs splitting".

## Handy numbers

| Quantity | Value | Shortcut |
|---|---|---|
| Seconds per day | 86,400 | ≈ 10⁵ (gives answers 15% low; fine for orders of magnitude) |
| Seconds per 30-day month | 2,592,000 | ≈ 2.6 × 10⁶ |
| Seconds per year | 31,536,000 | ≈ 3 × 10⁷ |
| 1 million requests per day | ≈ 11.6 per second | "1M/day ≈ 12/s" |
| 1 billion requests per month | ≈ 386 per second | "1B/month ≈ 400/s" |
| KB → MB → GB → TB → PB | × 1,000 each (or 1,024) | Say which you use; the difference is 2.4% per step |
| 1 Gbps | 125 MB/s | Divide bits by 8 |
| ASCII character in UTF-8 | 1 byte | |
| Devanagari, Bengali, Tamil and most Indic characters in UTF-8 | 3 bytes | Indian-language text is ~3× the bytes of the same length in English |
| UUID | 16 bytes binary (36 as text) | Store binary |
| Timestamp, 64-bit integer, double | 8 bytes | |
| float32 embedding of 768 dimensions | 3,072 bytes | dims × 4 |
| Availability 99.9% / 99.99% per 30 days | 43.2 min / 4.3 min of downtime | |

**Little's law** (for any stable system): **items in the system = arrival rate × time each spends in it** (L = λW). It turns request rates into concurrent connections, threads, database connections or GPU sequences.

---

## Example 1 · QPS: a UPI-scale payment switch

**Prompt.** Size the request rate for a central switch that routes all UPI-style payments.

**Published volume.** UPI processed about 24.07 billion transactions in September 2026 (NPCI data as reported; see [SWE401](../../03_majors/software_engineering/year_4/SWE401_large_scale_system_design/README.md)).

**Average.**
24.07 × 10⁹ ÷ 2,592,000 s ≈ **9,290 transactions/s** (≈ 802 million a day).

**Peak.** NPCI's 2025 API guidelines define peak hours as 10:00–13:00 and 17:00–21:30, 7.5 hours a day (as reported by MediaNama). *Assume* 60% of daily volume falls in those hours:
0.6 × 802 × 10⁶ ÷ (7.5 × 3,600 s) ≈ **17,800 transactions/s** across peak hours.
*Assume* the busiest minute of a festival or salary day is 2× the peak-hour average: design for **≈ 40,000 transactions/s** with headroom.

**Messages, not just transactions.** Each payment is several API calls through the switch: request to the payer's bank to debit, request to the payee's bank to credit, responses, and notifications to both apps. *Assume* 6 switch messages per transaction: ≈ **240,000 messages/s** at design peak. Status-check calls add more, which is why NPCI limited them after the 2025 outages ([case study 08](case_studies/08_upi_style_payment_switch.md)).

**Decision.** At 240,000 messages/s with a 10–15 s end-to-end budget, the switch must be horizontally partitioned (for example by transaction ID hash) with no shared lock on the hot path, and each transaction's state must live in one partition so that its messages are processed in order.

## Example 2 · Storage: a chat service

**Prompt.** How much storage does 1:1 and group chat need for five years?

**Assumptions (illustrative).** 500 million daily active users; 40 messages sent per user per day; average text message 100 bytes of content plus 100 bytes of metadata (IDs, timestamps, status); 5% of messages carry media averaging 200 KB.

**Text.**
- Messages per day: 500 × 10⁶ × 40 = **2 × 10¹⁰** (20 billion), ≈ 231,000 writes/s average.
- Bytes per day: 2 × 10¹⁰ × 200 B = **4 TB/day**.

**Two product choices give very different answers.**

| Retention model | Storage | Example |
|---|---|---|
| Store until delivered, then delete | Only undelivered messages: if 10% wait a day, ≈ 0.4 TB live, × 3 replicas ≈ 1.2 TB | WhatsApp says "Messages are not stored on the server after they are delivered" |
| Keep full history on the server | 4 TB × 365 × 5 ≈ **7.3 PB** raw; × 3 replicas ≈ 22 PB; compression (2–3×) brings it to ~7–11 PB | Discord stores trillions of messages |

**Media dominates.** 2 × 10¹⁰ × 5% × 200 KB = **200 TB/day** of media, 50× the text. Media goes to object storage behind a CDN, with lifecycle rules; text goes to a wide-column store partitioned by conversation.

**Decision.** The retention requirement is the single biggest storage decision. Ask it in the first five minutes.

## Example 3 · Bandwidth: live cricket streaming

**Prompt.** What egress does a national live-streaming platform need for a record match?

**Published volume.** JioHotstar reported 65.2 million peak concurrent viewers during the India–England T20 World Cup semi-final on 5 March 2026 (ICC media release; see [BE402](../../03_majors/backend_engineering/year_4/BE402_scalability_and_performance_caching_sharding/README.md)).

**Naive estimate.** *Assume* an average delivered bitrate of 1.5 Mbps:
65.2 × 10⁶ × 1.5 × 10⁶ bit/s ≈ **98 Tbps**.

**Anchor on a published ratio instead.** Hotstar reported 10+ Tbps of peak bandwidth at 25.3 million concurrent viewers in 2019 (AWS re:Invent talk, as reported). That is ≈ 10 × 10¹² ÷ 25.3 × 10⁶ ≈ **0.4 Mbps per viewer**, because most viewers watched on phones at modest resolutions. Applying the same ratio:
65.2 × 10⁶ × 0.4 Mbps ≈ **26 Tbps**.

The two estimates differ by almost 4×. That spread is the lesson: say which assumption drives the answer (the bitrate mix), give a range (26–98 Tbps), and note that bitrates have risen since 2019, so the truth is likely between them.

**Requests, not just bits.** With 6-second segments, every viewer fetches one segment per 6 s plus a playlist refresh: 65.2 × 10⁶ × 2 ÷ 6 ≈ **22 million HTTP requests/s** at the edge.

**Decision.** No single CDN or origin serves this. You need multiple CDNs, an origin shield so the origin sees only cache misses (at a 99% hit ratio, ≈ 0.3–1 Tbps), and pre-provisioned capacity because traffic can grow by over 1 million viewers per minute ([case study 10](case_studies/10_live_video_streaming.md)).

## Example 4 · Cache size for a URL shortener

**Prompt.** How much cache memory does a shortener need?

**Assumptions (illustrative).** 100 million new links a month; links kept 5 years; 100 redirects per link created (read:write = 100:1); 1% of all stored links are clicked on a given day.

- Links stored after 5 years: 100 × 10⁶ × 60 = **6 × 10⁹**.
- Redirects: 100 × 10⁸ = 10¹⁰ a month ≈ **3,860/s average**; *assume* 5× at peak ≈ **19,300/s**.
- Cache entry: 7-byte code + ~100-byte long URL + ~100 bytes of per-key overhead in an in-memory store (**rough**) ≈ **~200–250 bytes**.

**Working set.** 1% of 6 × 10⁹ = 6 × 10⁷ links clicked per day × 250 B ≈ **15 GB**.

**Decision.** 15 GB fits in one cache node; use a primary-replica pair (or three shards for headroom) with LRU eviction. Caching *every* link would need 6 × 10⁹ × 250 B = 1.5 TB, which is wasteful because most links are never clicked after their first week. The database sees only misses: at a 95% hit rate, ≈ 1,000 reads/s at peak, which a single key-value store handles easily. See [case study 01](case_studies/01_url_shortener.md).

## Example 5 · GPU and token cost: an enterprise AI assistant

**Prompt.** A company of 20,000 employees wants an internal assistant that answers questions from its documents (RAG). Estimate tokens, cost through an API, and the GPUs needed to self-host.

**Assumptions (illustrative).** 30% daily active (6,000 users); 15 questions per user per day; 22 working days a month; each request sends 4,000 input tokens (1,000 of instructions and question + 3,000 of retrieved passages) and receives 400 output tokens.

**Tokens.**
- Requests: 6,000 × 15 = **90,000 per day**; ≈ 1.98 million a month.
- Input: 90,000 × 4,000 = 360 million/day → **7.9 billion/month**.
- Output: 90,000 × 400 = 36 million/day → **0.79 billion/month**.

**API cost.** Prices change often and differ by model; use the provider's current pricing page. With *illustrative* prices of $3 per million input tokens and $15 per million output tokens:
7,920 × $3 + 792 × $15 = $23,760 + $11,880 ≈ **$35,600 per month**, about **$6 per active user per month**. Prompt caching of the fixed 1,000-token instruction block, and fewer but better retrieved passages, are the two biggest levers.

**Self-hosting: how many GPUs?**
- Peak rate: *assume* traffic falls in 8 working hours with a 3× peak: 90,000 ÷ 28,800 s × 3 ≈ **9.4 requests/s**.
- Concurrency (Little's law): *assume* 30 output tokens/s per sequence, so each answer takes 400 ÷ 30 ≈ 13 s of decoding: 9.4 × 13 ≈ **~120 sequences in flight**.
- KV cache for a Llama-3-70B-class model: 320 KiB per token ([building_blocks.md](building_blocks.md#17-llm-serving)) × 4,400 tokens ≈ 1.34 GiB per sequence × 120 ≈ **~160 GiB**.
- Weights at 16-bit: **~140 GB**. Total ≈ 300 GB, so at least 4 × 80 GB H100s with no slack; in practice one 8-GPU server (or FP8 weights on 4 GPUs), and a second server for redundancy.
- Cost: at an *illustrative* $3 per GPU-hour, 16 GPUs × 730 h ≈ **$35,000 per month** running 24×7.

**Decision.** At this volume, the API and self-hosting cost about the same, and self-hosting adds an on-call burden. Self-hosting wins when utilisation is high (traffic spread across time zones, batch jobs at night), when data must stay on premises, or when a smaller fine-tuned model is good enough (an 8B model needs a fraction of the memory: 128 KiB of KV per token and ~16 GB of weights). Always state that model quality differs between the options. See [case study 14](case_studies/14_rag_enterprise_assistant.md) and [case study 16](case_studies/16_llm_inference_serving.md).

## Example 6 · Concurrency and fleet size: a Tatkal-style ticket opening

**Prompt.** Size the front tier for a ticket window that opens at 10:00 sharp.

**Published anchor.** IRCTC's public record is **30,155 tickets booked in a single minute** (12 March 2025, at 10:01), and it states the system can handle more than 30,000 bookings per minute. That is ≈ **503 tickets/s** of *successful* bookings.

**Demand is much larger than successful bookings (illustrative).** *Assume* 1 million users are waiting at 10:00 for AC-class Tatkal, 30% of them act in the first 10 seconds, and each makes 3 requests in that time (availability, passenger form, booking attempt):
0.3 × 10⁶ × 3 ÷ 10 s = **90,000 requests/s** for the first 10 seconds.

**Concurrency.** *Assume* 200 ms average server time per request: L = 90,000 × 0.2 = **18,000 requests in flight**. If one application instance handles 200 concurrent requests comfortably (**rough**, measure yours), you need 90 instances, ~135 with 50% headroom, *already running* at 09:59 (autoscaling takes minutes; the spike takes seconds).

**The real bottleneck is not the web tier.** All those requests compete for a small number of rows: the seat inventory of one train, class and date. If 50,000 users try to book the same popular train's AC 3-tier Tatkal quota, a single database row receives tens of thousands of conflicting updates per second. That is why the design admits users through a virtual waiting room at a rate the inventory service can process, and allocates seats from a per-train counter in memory with a durable log ([case study 09](case_studies/09_tatkal_flash_booking.md)).

**Decision.** Pre-scale the stateless tier, but design the admission control and inventory partitioning first. More web servers would only push more contention onto the same row.

---

## Common estimation mistakes

1. Using "peak = 2× average" for events that spike 10–100× in seconds.
2. Forgetting replication (×3), indexes (+30–100%) and metadata.
3. Mixing bits and bytes (a factor of 8) or KB and KiB without noticing.
4. Estimating total storage but not the **hot set**, which decides cache size.
5. Estimating QPS for the whole system but not for the **hottest key**.
6. Computing a number and never using it to make a decision.
7. Quoting a precise figure for a real company that you cannot source. Say "assumed" instead.

## Sources

All checked 12 Oct 2026.

- UPI September 2026 volume, reported from NPCI data — https://www.outlookmoney.com/banking/upi-processes-2407-billion-transactions-worth-rs-2937-lakh-crore-in-september
- MediaNama, NPCI guidelines on UPI API usage and peak hours (May 2025) — https://www.medianama.com/2025/05/223-npci-banks-balance-upi-transaction-guidelines/
- WhatsApp, "How WhatsApp enables multi-device capability" (14 Jul 2021) — https://engineering.fb.com/2021/07/14/security/whatsapp-multi-device/
- Discord, "How Discord Stores Trillions of Messages" (2023) — https://discord.com/blog/how-discord-stores-trillions-of-messages
- ICC media release on the JioHotstar concurrency record (Mar 2026) — https://www.icc-cricket.com/media-releases/icc-men-s-t20-world-cup-2026-sets-new-global-streaming-record-on-jiohotstar-during-india-england-semi-final
- Hotstar at AWS re:Invent 2019 (CMY302), report by Classmethod — https://dev.classmethod.jp/articles/reinvent-2019-cmy302/
- IRCTC, Internet Ticketing (booking records) — https://www.irctc.com/internet-ticketing.php
- Llama 3 configurations — https://arxiv.org/abs/2407.21783 ; NVIDIA H100 — https://www.nvidia.com/en-us/data-center/h100/

_Last reviewed: 2026-10_
