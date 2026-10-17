from topics_lib import topic as t

BACKEND_MODULES = [
    {
        "id": "be-http",
        "title": "HTTP, APIs, FastAPI",
        "topics": [
            t(
                "http-basics",
                "HTTP, TLS, DNS, request lifecycle",
                level="beginner",
                priority="essential",
                minutes=70,
                summary="Browser or client → DNS → TCP → TLS → HTTP. You already run Nginx + PHP-FPM. FastAPI sits where Laravel sits.",
                prereq=["Production story: one portal you can draw"],
                blocks=[
                    {
                        "h": "How it works",
                        "p": [
                            "GET should not change state. POST creates. PUT is idempotent replace. PATCH is partial. DELETE is idempotent in the 'already gone is 404 or 204' sense you must pick and document.",
                            "Status families: 2xx success, 4xx the client can fix, 5xx you log.",
                        ],
                    },
                    {
                        "h": "Laravel map",
                        "p": ["Kernel middleware ≈ FastAPI middleware and dependencies. Blade web tier vs JSON API tier is Accenture day 5 — keep that split in Python too."],
                    },
                    {"h": "References", "p": ["[MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)"]},
                    {"h": "Next", "p": ["#rest-design"]},
                ],
            ),
            t(
                "rest-design",
                "REST, pagination, versioning, errors, OpenAPI",
                level="intermediate",
                priority="essential",
                minutes=80,
                summary="Resources, not RPC soup. Pagination, filters, sort. Version in URL or header. Error body is a contract. FastAPI emits OpenAPI; claiming you authored OpenAPI at Gomilestone is unverified.",
                prereq=["#http-basics"],
                blocks=[
                    {
                        "h": "Error shape",
                        "code": '{"error": {"code": "validation_error", "message": "title is required", "request_id": "…"}}\n',
                    },
                    {
                        "h": "Idempotency",
                        "p": ["Payment-shaped POST needs `Idempotency-Key`. You used this idea on Razorpay callbacks. In FastAPI store the key per tenant."],
                    },
                    {
                        "h": "Task",
                        "p": ["Write the error format in README. Do not put OpenAPI on the resume until a spec file exists in this repo."],
                    },
                    {"h": "References", "p": ["[MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP) · FastAPI generates [OpenAPI](https://fastapi.tiangolo.com/tutorial/metadata/)"]},
                    {"h": "Next", "p": ["#fastapi-core"]},
                ],
            ),
            t(
                "fastapi-core",
                "FastAPI routes, params, Pydantic, Depends",
                level="intermediate",
                priority="essential",
                minutes=110,
                summary="This is the Laravel routes + FormRequest + container for the new stack. Production-ready means validation, typed models, and tests, not a hello world.",
                prereq=["#py-typing", "#http-basics"],
                blocks=[
                    {
                        "h": "What it is",
                        "p": ["Starlette + Pydantic. A path operation is a function. Return models become JSON. Invalid bodies become 422 unless you override."],
                    },
                    {
                        "h": "Example",
                        "code": "from fastapi import FastAPI, Depends, HTTPException\nfrom pydantic import BaseModel, Field\n\napp = FastAPI()\n\nclass DocumentIn(BaseModel):\n    title: str = Field(min_length=1, max_length=200)\n\nclass Store:\n    def __init__(self):\n        self.items: dict[str, str] = {}\n\ndef get_store() -> Store:\n    return app.state.store\n\n@app.on_event('startup')\ndef boot():\n    app.state.store = Store()\n\n@app.post('/v1/documents', status_code=201)\ndef create(body: DocumentIn, store: Store = Depends(get_store)):\n    store.items[body.title] = body.title\n    return {'title': body.title}\n",
                    },
                    {
                        "h": "Note",
                        "p": ["`on_event` is legacy; prefer lifespan in current FastAPI. Use lifespan in the real repo: see official lifespan docs."],
                    },
                    {
                        "h": "Mistakes",
                        "ul": [
                            "Doing database work in the path function without a session scope.",
                            "Returning ORM objects that leak extra columns.",
                            "Forgetting tenant on every query.",
                        ],
                    },
                    {
                        "h": "Task",
                        "p": ["Implement GET list + POST create for documents in-memory with pytest via `TestClient`. Then replace memory in #sqlalchemy-core."],
                    },
                    {"h": "References", "p": ["[FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) · [Pydantic](https://docs.pydantic.dev/)"]},
                    {"h": "Next", "p": ["#fastapi-prod"]},
                ],
            ),
            t(
                "fastapi-prod",
                "Middleware, exceptions, config, background, lifespan",
                level="intermediate",
                priority="essential",
                minutes=80,
                summary="Request id middleware, domain exception handlers, settings from env, lifespan for pool startup, background only for tiny after-response work — real jobs go to a worker.",
                prereq=["#fastapi-core"],
                blocks=[
                    {
                        "h": "Laravel map",
                        "p": ["Middleware ≈ middleware. `.env` ≈ pydantic-settings. `ShouldQueue` ≠ FastAPI `BackgroundTasks`. BackgroundTasks die if the process dies; use Redis/SQS for SMS."],
                    },
                    {
                        "h": "Task",
                        "p": ["Add `X-Request-Id` middleware. Attach it to logs. Return it on errors."],
                    },
                    {"h": "References", "p": ["[FastAPI advanced](https://fastapi.tiangolo.com/advanced/)"]},
                    {"h": "Next", "p": ["#authz"]},
                ],
            ),
            t(
                "authz",
                "Authn, authz, passwords, JWT, OAuth concepts, RBAC",
                level="intermediate",
                priority="essential",
                minutes=100,
                summary="Practice JWT in this repo. Resume still describes Ugro as roles on one account unless you later ship JWT. OAuth2 is a protocol with an authorization server you have not run in production.",
                prereq=["#fastapi-core", "Accenture days 10–11 notes if you did them"],
                blocks=[
                    {
                        "h": "How it works",
                        "ul": [
                            "Password hashing: Argon2 or bcrypt. Never SHA1.",
                            "Session cookies: HttpOnly, Secure, SameSite. Fits browser apps.",
                            "JWT: three segments, signature, short `exp`. Logout is hard without a denylist or short TTL.",
                            "OAuth2 authorization code: user, your app, identity provider. Client credentials: service to service, no user.",
                            "RBAC: role on membership to org. Check org on every query, not only in the token.",
                        ],
                    },
                    {
                        "h": "Security",
                        "p": ["Do not store JWT in localStorage for a browser app if you can use cookies. Do not put secrets in the payload. Filter documents by `org_id` in SQL."],
                    },
                    {
                        "h": "Task",
                        "p": ["Issue and verify an HMAC JWT in tests. Reject expired and tampered. A user in org A must 404 on org B's document id (same 404 as missing)."],
                    },
                    {"h": "References", "p": ["[FastAPI security](https://fastapi.tiangolo.com/tutorial/security/)"]},
                    {"h": "Next", "p": ["#pg-sql"]},
                ],
            ),
        ],
    },
    {
        "id": "be-data",
        "title": "PostgreSQL, SQLAlchemy, Redis, jobs",
        "topics": [
            t(
                "pg-sql",
                "PostgreSQL: schema, SQL, transactions, indexes",
                level="intermediate",
                priority="essential",
                minutes=110,
                summary="You already write SQL. This lesson is Postgres dialect: types, CTEs, window functions, isolation, EXPLAIN. Do not invent Religare latency numbers.",
                prereq=["#rest-design"],
                blocks=[
                    {
                        "h": "Schema sketch",
                        "code": "CREATE TABLE orgs (id uuid PRIMARY KEY, name text NOT NULL);\nCREATE TABLE users (\n  id uuid PRIMARY KEY,\n  org_id uuid NOT NULL REFERENCES orgs(id),\n  email citext UNIQUE NOT NULL\n);\nCREATE TABLE documents (\n  id uuid PRIMARY KEY,\n  org_id uuid NOT NULL REFERENCES orgs(id),\n  title text NOT NULL,\n  created_at timestamptz NOT NULL DEFAULT now()\n);\nCREATE INDEX documents_org_created_idx ON documents (org_id, created_at DESC);\n",
                    },
                    {
                        "h": "Isolation",
                        "p": ["Read committed is the default. Repeatable read / serializable matter when two payments debit one balance. You explained this on Accenture day 7 without fake metrics."],
                    },
                    {
                        "h": "Task",
                        "p": ["Write five queries: list by org with limit; count per day (window or group); documents without chunks; EXPLAIN ANALYZE a filter; a transaction that inserts audit + document."],
                    },
                    {"h": "References", "p": ["[PostgreSQL docs](https://www.postgresql.org/docs/)"]},
                    {"h": "Next", "p": ["#sqlalchemy-core"]},
                ],
            ),
            t(
                "sqlalchemy-core",
                "SQLAlchemy, sessions, Alembic, pooling",
                level="intermediate",
                priority="essential",
                minutes=100,
                summary="ORM is Eloquent's cousin, not a twin. Unit of work is the Session. Migrations are Alembic, not `artisan migrate`.",
                prereq=["#pg-sql", "#fastapi-core"],
                blocks=[
                    {
                        "h": "Boundaries",
                        "p": ["Route → service → repository/session. Do not query inside Pydantic validators. Expire objects after commit so you do not see stale state."],
                    },
                    {
                        "h": "Task",
                        "p": ["Alembic revision for orgs, users, documents. FastAPI dependency yields a session and closes it."],
                    },
                    {"h": "References", "p": ["[SQLAlchemy](https://docs.sqlalchemy.org/)"]},
                    {"h": "Next", "p": ["#redis-cache"]},
                ],
            ),
            t(
                "redis-cache",
                "Redis: cache, TTL, invalidation, locks, rate limits",
                level="intermediate",
                priority="essential",
                minutes=80,
                summary="Cache-aside for reads. Never cache a payment write. TTL plus explicit delete on update. Distributed lock is easy to get wrong — prefer idempotency keys.",
                prereq=["#sqlalchemy-core"],
                blocks=[
                    {
                        "h": "Failure modes",
                        "ul": [
                            "Stampede: many clients miss together. Soft TTL or single-flight.",
                            "Poison cache: cached 404 of a document that was just uploaded.",
                            "Key without tenant: org B reads org A's list.",
                        ],
                    },
                    {
                        "h": "Task",
                        "p": ["Cache document GET for 30s keyed by org+id. Delete on update. Rate-limit POST /messages per user."],
                    },
                    {"h": "References", "p": ["[Redis docs](https://redis.io/docs/)"]},
                    {"h": "Next", "p": ["#queues"]},
                ],
            ),
            t(
                "queues",
                "Queues, retries, backoff, DLQ, idempotency, scheduling",
                level="intermediate",
                priority="essential",
                minutes=90,
                summary="You ship Laravel jobs. In Python: Redis queue or SQS, worker process, retry with jitter, dead letter after N, exactly-once is a lie — aim for at-least-once plus idempotent handlers.",
                prereq=["#redis-cache", "#py-exceptions"],
                blocks=[
                    {
                        "h": "Eventual consistency",
                        "p": ["The API returns 202 with a job id. The document is searchable after the worker finishes. The UI polls or you use a later websocket. Do not block the request on PDF parse."],
                    },
                    {
                        "h": "Task",
                        "p": ["A worker that 'sends' a notification twice with the same event id must insert one row. Failed jobs after 3 tries land in a failed table."],
                    },
                    {"h": "Next", "p": ["#integrations"]},
                ],
            ),
            t(
                "integrations",
                "Webhooks, HTTP clients, timeouts, circuit breakers, files",
                level="intermediate",
                priority="essential",
                minutes=70,
                summary="Outbound: timeouts, retries only on idempotent methods, cap backoff. Inbound webhooks: verify signature, store event id. Files: S3 + signed URLs, not the app disk, for anything private.",
                prereq=["#queues"],
                blocks=[
                    {
                        "h": "Laravel map",
                        "p": ["Razorpay callback pattern is the webhook lesson. HTTP client timeouts are the Spring-client week of the Accenture plan, now in `httpx`."],
                    },
                    {
                        "h": "Task",
                        "p": ["httpx client with 2s timeout and retry on 503. A webhook handler that rejects a bad signature."],
                    },
                    {"h": "Next", "p": ["#be-testing"]},
                ],
            ),
        ],
    },
    {
        "id": "be-quality",
        "title": "Testing, architecture, observability, security",
        "topics": [
            t(
                "be-testing",
                "Unit, API, database, and contract tests",
                level="intermediate",
                priority="essential",
                minutes=70,
                summary="TestClient for HTTP. A real test database, not sqlite-if-you-use-pg-features. Factories like Laravel factories.",
                prereq=["#fastapi-core", "#py-pytest"],
                blocks=[
                    {
                        "h": "Task",
                        "p": ["Tests for 201 create, 422 validation, 401 missing token, tenant isolation. One SQL-level test that the index exists is optional."],
                    },
                    {"h": "Next", "p": ["#be-arch"]},
                ],
            ),
            t(
                "be-arch",
                "Layered design, modular monolith, microservice trade-offs",
                level="intermediate",
                priority="essential",
                minutes=60,
                summary="This product is a modular monolith until a second deployable is forced. Microservices need a network, a contract, and a reason.",
                prereq=["#py-solid"],
                blocks=[
                    {
                        "h": "When not microservices",
                        "p": ["One developer, one product, one database. Split workers as processes, not as a new company."],
                    },
                    {"h": "Next", "p": ["#observability"]},
                ],
            ),
            t(
                "observability",
                "Logs, metrics, traces, health, shutdown",
                level="intermediate",
                priority="essential",
                minutes=70,
                summary="Structured logs with request id, tenant, route. Metrics: latency, errors, queue depth. Health for k8s/compose. SIGTERM: stop taking work, finish in-flight, close pools.",
                prereq=["#fastapi-prod"],
                blocks=[
                    {"h": "References", "p": ["[OpenTelemetry](https://opentelemetry.io/docs/)"]},
                    {"h": "Task", "p": ["`/healthz` checks DB ping. Document what CloudWatch or stdout will show for one failed request."]},
                    {"h": "Next", "p": ["#owasp-api"]},
                ],
            ),
            t(
                "owasp-api",
                "OWASP, injection, XSS, CSRF, SSRF, CORS, secrets",
                level="intermediate",
                priority="essential",
                minutes=80,
                summary="Parameterised SQL. Never send untrusted document text to a tool that can exfiltrate. CORS is not auth. Secrets in a manager, not git.",
                prereq=["#authz"],
                blocks=[
                    {
                        "h": "SSRF",
                        "p": ["If the API fetches a user-supplied URL for 'import', that is SSRF. Allowlist hosts. Block link-local."],
                    },
                    {"h": "References", "p": ["[OWASP](https://owasp.org/)"]},
                    {"h": "Next", "p": ["#linux-fs"]},
                ],
            ),
        ],
    },
]
