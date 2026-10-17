from helper import lesson, mod

SD = [
    mod("sd-ideas", "Language of a design interview", [
        lesson(
            "sd-reqs",
            "Requirements, SLOs, capacity, trade-offs",
            "intermediate", "essential", 40,
            "Functional vs non-functional. QPS, storage, p99 latency, availability. Write the numbers before the boxes.",
            nxt="#sd-scale",
        ),
        lesson(
            "sd-scale",
            "Load balancing, cache, CDN, replica, shard, indexes",
            "intermediate", "essential", 45,
            "Vertical then horizontal. Cache-aside. Read replica for reads that can lag. Shard only with a key you can live with.",
            nxt="#sd-style",
        ),
        lesson(
            "sd-style",
            "Monolith, modular monolith, microservices",
            "intermediate", "essential", 30,
            "This product stays a modular monolith through project 10 unless a real constraint appears.",
            nxt="#sd-async",
        ),
        lesson(
            "sd-async",
            "Sync vs async, queues, delivery, ordering, retries",
            "intermediate", "essential", 40,
            "At-least-once plus idempotency is the default. Exactly-once is a marketing phrase for a transaction plus a dedupe table.",
            nxt="#sd-cap",
        ),
        lesson(
            "sd-cap",
            "Consistency, availability, partitions, failure",
            "advanced", "essential", 40,
            "A tenant read-after-write on documents should hit the primary. Search indexes can lag. Say that out loud.",
            nxt="#sd-resilience",
        ),
        lesson(
            "sd-resilience",
            "Rate limits, gateways, circuit breakers, bulkheads, timeouts",
            "intermediate", "essential", 35,
            "Timeouts are first. Retries need jitter. Bulkheads isolate the LLM client from the database pool.",
            nxt="#sd-slo",
        ),
        lesson(
            "sd-slo",
            "SLI, SLO, SLA, alerts, incidents, postmortems",
            "intermediate", "essential", 30,
            "SLA is a contract. You have not claimed SLA ownership at work. SLO is an internal target. Alerts on symptoms, not every 5xx spike of one bot.",
            nxt="#sd-url",
        ),
    ]),
    mod("sd-drills", "Six designs on paper and then in the repo", [
        lesson(
            "sd-url",
            "Design: URL shortener",
            "intermediate", "essential", 40,
            "Requirements: create, redirect, optional expiry. API POST /links. Table links(code pk, url, owner, expires_at). Hash collision retry. Cache hot codes. Abuse: rate limit and malware scan later.",
            nxt="#sd-notify",
        ),
        lesson(
            "sd-notify",
            "Design: notification service",
            "intermediate", "essential", 40,
            "API accepts notify commands. Worker talks to SMS/email. Idempotency on (tenant, event_id). This maps to Ugro queued SMS without copying client code.",
            nxt="#sd-upload",
        ),
        lesson(
            "sd-upload",
            "Design: file upload",
            "intermediate", "essential", 35,
            "Client uploads to signed S3 PUT. API stores metadata. Virus scan worker. Size limits. This becomes document ingestion.",
            nxt="#sd-ecom",
        ),
        lesson(
            "sd-ecom",
            "Design: ecommerce backend",
            "advanced", "advanced", 45,
            "Catalog, cart, order, payment states. Inventory reservation. Fit Paradox is the honest story: catalog, subscription, Razorpay, Shiprocket — as you actually built them.",
            nxt="#sd-pay",
        ),
        lesson(
            "sd-pay",
            "Design: payment workflow",
            "advanced", "essential", 45,
            "States: created, authorized, captured, failed, refunded. Never mark paid on browser return. Webhook + event id. Ledger row in the same transaction as the status change.",
            nxt="#sd-ai-search",
        ),
        lesson(
            "sd-ai-search",
            "Design: AI document search platform",
            "advanced", "essential", 50,
            "Ingest → parse → chunk → embed → pgvector. Query → tenant filter → retrieve → generate → cite. Eval set in CI. Cost per request. This is the capstone of the repo.",
            nxt="#ai-literacy",
        ),
    ]),
]
