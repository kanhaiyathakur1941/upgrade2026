from topics_lib import topic as t

SD_MODULES = [
    {
        "id": "sd-core",
        "title": "System design",
        "topics": [
            t(
                "sd-fundamentals",
                "Requirements, capacity, scaling, trade-offs",
                level="intermediate",
                priority="essential",
                minutes=70,
                summary="Functional vs non-functional. Estimate QPS, storage, bandwidth. Latency vs throughput. Availability as nines. Horizontal scale vs vertical. Write the trade-off.",
                prereq=["#http-basics", "#pg-sql"],
                blocks=[
                    {
                        "h": "How to run a 45-minute design",
                        "ol": [
                            "Clarify users and scale.",
                            "API sketch.",
                            "Data model.",
                            "Happy path architecture.",
                            "Bottlenecks, cache, queue.",
                            "Failure and security.",
                            "What you would measure.",
                        ],
                    },
                    {"h": "References", "p": ["[roadmap.sh system design](https://roadmap.sh/system-design)"]},
                    {"h": "Next", "p": ["#sd-url"]},
                ],
            ),
            t(
                "sd-url",
                "Design: URL shortener",
                level="intermediate",
                priority="essential",
                minutes=50,
                summary="Write vs read heavy. Hash vs counter ids. 301/302. Analytics as async. Hot keys.",
                prereq=["#sd-fundamentals"],
                blocks=[
                    {
                        "h": "Sketch",
                        "ul": [
                            "POST /v1/links {url} → {code}",
                            "GET /{code} → redirect",
                            "Table: code PK, url, org_id, expires_at",
                            "Cache code→url. Unique index on code.",
                            "Failure: collision retry. Abuse: rate limit and malware URLs.",
                        ],
                    },
                    {"h": "Interview", "p": ["How do you guarantee uniqueness without a global lock?"]},
                    {"h": "Next", "p": ["#sd-notify"]},
                ],
            ),
            t(
                "sd-notify",
                "Design: notification service",
                level="intermediate",
                priority="essential",
                minutes=50,
                summary="You already queue SMS. This is the generalisation: templates, channels, retries, preferences, idempotent providers.",
                prereq=["#queues", "#sd-fundamentals"],
                blocks=[
                    {
                        "h": "Sketch",
                        "ul": [
                            "POST /v1/notifications with event id.",
                            "Tables: outbox, delivery_attempts.",
                            "Worker per channel. DLQ. At-least-once to Sinch/SNS.",
                            "Do not send twice for the same event id + channel.",
                        ],
                    },
                    {"h": "Next", "p": ["#sd-upload"]},
                ],
            ),
            t(
                "sd-upload",
                "Design: file upload service",
                level="intermediate",
                priority="essential",
                minutes=45,
                summary="Direct-to-S3 with presigned PUT. Virus scan async. Metadata in Postgres. Size limits. Content-type allowlist.",
                prereq=["#aws-core"],
                blocks=[
                    {
                        "h": "Security",
                        "p": ["Never serve user files from the API process with user-controlled content-type that can become XSS. Signed GET, correct Content-Disposition."],
                    },
                    {"h": "Next", "p": ["#sd-ecom"]},
                ],
            ),
            t(
                "sd-ecom",
                "Design: ecommerce backend",
                level="intermediate",
                priority="essential",
                minutes=55,
                summary="Catalog, cart, inventory, order. Fit Paradox-shaped. Inventory races need transactions or reservations.",
                prereq=["#sd-fundamentals"],
                blocks=[
                    {
                        "h": "Bottleneck",
                        "p": ["Hot SKU. Reservation row with TTL. Payment is a different service (#sd-pay)."],
                    },
                    {"h": "Next", "p": ["#sd-pay"]},
                ],
            ),
            t(
                "sd-pay",
                "Design: payment workflow",
                level="intermediate",
                priority="essential",
                minutes=55,
                summary="State machine: created → authorized → captured / failed / refunded. Trust provider webhooks, not browser redirects. You have Razorpay stories — keep them factual.",
                prereq=["#integrations"],
                blocks=[
                    {
                        "h": "Idempotency",
                        "p": ["event_id unique. Replay does not double-capture. Ledger line per transition."],
                    },
                    {"h": "Next", "p": ["#sd-ai-search"]},
                ],
            ),
            t(
                "sd-ai-search",
                "Design: AI document search platform",
                level="advanced",
                priority="essential",
                minutes=70,
                summary="This is the product you will build. Ingestion pipeline, chunk/embed, pgvector, permission filter before similarity, generation with citations, evals, cost.",
                prereq=["#sd-fundamentals", "#rag-e2e"],
                blocks=[
                    {
                        "h": "Non-negotiables",
                        "ul": [
                            "Tenant in the query, not only the prompt.",
                            "Original stored; chunks derived.",
                            "Refuse when retrieval is empty.",
                            "Trace tokens and chunk ids.",
                        ],
                    },
                    {"h": "Next", "p": ["#ai-literacy"]},
                ],
            ),
            t(
                "sd-distributed",
                "Consistency, queues vs RPC, gateways, resilience",
                level="advanced",
                priority="advanced",
                minutes=60,
                summary="CAP as a discussion tool, not a slogan. At-least-once vs at-most-once. API gateway, rate limits, circuit breaker, bulkhead, graceful degradation.",
                prereq=["#sd-fundamentals"],
                blocks=[
                    {
                        "h": "Kafka",
                        "p": ["Optional after SQS. Log of events, consumer groups, ordering per partition. Not required to apply. Docs: [Kafka](https://kafka.apache.org/documentation/)."],
                    },
                    {"h": "Next", "p": ["#ai-literacy"]},
                ],
            ),
        ],
    }
]
