from helper import lesson, mod

BE = [
    mod("http-api", "HTTP, REST, FastAPI, Pydantic", [
        lesson(
            "http-basics",
            "HTTP, TLS, DNS, TCP, the request cycle",
            "beginner", "essential", 50,
            "You already run Nginx in front of PHP-FPM. Name the same hops in Python.",
            what="DNS finds an IP. TCP connects. TLS wraps. HTTP carries method, path, headers, body. The status code is part of the contract.",
            how="Browser or curl → Nginx → uvicorn → FastAPI route → service → PostgreSQL. Cookies are headers. Sessions are server state keyed by a cookie.",
            compare="Laravel's public/index.php is uvicorn plus the FastAPI app object.",
            refs=["[MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)"],
            nxt="#http-rest",
        ),
        lesson(
            "http-rest",
            "REST, idempotency, pagination, versioning",
            "intermediate", "essential", 50,
            "GET and PUT retry safely. POST payment does not, unless an Idempotency-Key is stored.",
            realistic="Razorpay callbacks on Ugro Customer Portal are the story: verify signature, store event id, do not credit twice. That is idempotency. Do not invent a second incident.",
            refs=["[MDN HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)"],
            nxt="#http-json",
        ),
        lesson(
            "http-json",
            "JSON, validation, OpenAPI, error bodies",
            "intermediate", "essential", 45,
            "Practice OpenAPI. Do not put OpenAPI on the resume until a file in the repo is the source of truth.",
            how="Pydantic models become the OpenAPI schema FastAPI publishes at /docs. Error body: code, message, request_id.",
            refs=["[OpenAPI](https://spec.openapis.org/oas/latest.html)"],
            nxt="#fastapi-core",
        ),
        lesson(
            "fastapi-core",
            "FastAPI routing, params, body, Pydantic",
            "intermediate", "essential", 70,
            "This is the Laravel routes file plus Form Request, in one decorator.",
            code='''from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class DocumentIn(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    tenant_id: str

@app.post("/v1/documents", status_code=201)
def create_document(body: DocumentIn) -> dict[str, str]:
    if body.tenant_id == "blocked":
        raise HTTPException(status_code=403, detail="tenant blocked")
    return {"id": "doc_1", "title": body.title}''',
            out="POST with a title returns 201 JSON. Empty title returns 422 from Pydantic.",
            compare="Route::post is @app.post. Form Request is the Pydantic model. abort(403) is HTTPException.",
            task="Versioned documents API with list, get, create. Tests with httpx AsyncClient or TestClient.",
            refs=["[FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)", "[Pydantic](https://docs.pydantic.dev/)"],
            nxt="#fastapi-prod",
        ),
        lesson(
            "fastapi-prod",
            "Dependencies, middleware, lifespan, background, config",
            "intermediate", "essential", 60,
            "Depends is the service container for one request. lifespan starts the pool. Background tasks are for tiny work, not SMS at scale.",
            how="A get_current_user dependency reads the Authorization header. Middleware logs request_id. Settings use pydantic-settings from env.",
            mistakes=["Putting the database session in a global without a request scope", "Using BackgroundTasks for work that must retry after a crash — that belongs on a queue"],
            refs=["[Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)"],
            nxt="#auth-core",
        ),
    ]),
    mod("auth-data", "Auth, SQL, ORM, Redis, jobs", [
        lesson(
            "auth-core",
            "Passwords, sessions, JWT, OAuth2, RBAC",
            "intermediate", "essential", 70,
            "Practice JWT here. The Accenture gap note is still right: Ugro is roles on one account, not a named OAuth2 deployment.",
            what="password hashing (bcrypt/argon2), session cookies, JWT access/refresh, OAuth2 authorization code vs client credentials, RBAC vs permission flags.",
            why="A document assistant with tenants is useless if org A can read org B.",
            how="Hash passwords with a slow function. JWT is three Base64url parts. Verify exp, signature, aud. Store refresh tokens hashed if you need revoke.",
            code='''import hashlib, hmac, json, base64, time

def b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()

def sign(payload: dict, secret: str) -> str:
    header = b64(json.dumps({"alg": "HS256"}).encode())
    body = b64(json.dumps(payload).encode())
    sig = b64(hmac.new(secret.encode(), f"{header}.{body}".encode(), hashlib.sha256).digest())
    return f"{header}.{body}.{sig}"

print(sign({"sub": "u1", "exp": int(time.time()) + 60}, "dev-only")[:12])''',
            out="A JWT prefix, not a production secret. Rotate secrets. Never log the token.",
            interview=["JWT versus the session model you shipped", "Why logout is hard with only a stateless access token"],
            refs=["[OWASP Auth](https://owasp.org/www-project-web-security-testing-guide/)"],
            nxt="#sql-schema",
        ),
        lesson(
            "sql-schema",
            "PostgreSQL schema, types, constraints, transactions",
            "intermediate", "essential", 60,
            "You already write SQL. Add PostgreSQL names: jsonb, timestamptz, uuid, exclusion where needed.",
            how="PK, FK, unique, check. Transactions wrap payment + ledger. Isolation: read committed is the default; serializable is rare and costly.",
            refs=["[PostgreSQL](https://www.postgresql.org/docs/)"],
            nxt="#sql-query",
        ),
        lesson(
            "sql-query",
            "Joins, CTE, windows, indexes, EXPLAIN, locks",
            "intermediate", "essential", 70,
            "Same story as Accenture Day 7, on PostgreSQL: EXPLAIN ANALYZE, leftmost prefix, covering indexes, tenant_id in the index.",
            code='''-- documents for one tenant, recent first
-- CREATE INDEX documents_tenant_created_idx ON documents (tenant_id, created_at DESC);
SELECT id, title, created_at
FROM documents
WHERE tenant_id = 'org_a'
ORDER BY created_at DESC
LIMIT 20;''',
            task="Five EXPLAIN ANALYZE captures in a notes/sql.md file. No fake timings.",
            nxt="#orm-alchemy",
        ),
        lesson(
            "orm-alchemy",
            "SQLAlchemy, Alembic, sessions, pooling",
            "intermediate", "essential", 60,
            "Eloquent is SQLAlchemy 2.x. Migrations are Alembic, like Laravel migrations.",
            how="Session per request. expire_on_commit awareness. relationship() is with(). A repository hides query details from the HTTP layer.",
            refs=["[SQLAlchemy](https://docs.sqlalchemy.org/)"],
            nxt="#cache-redis",
        ),
        lesson(
            "cache-redis",
            "Redis: cache, TTL, invalidation, rate limits, locks",
            "intermediate", "essential", 55,
            "Cache a repayment-shaped read. Do not cache a payment write. Religare already taught this in Laravel.",
            mistakes=["Cache without tenant in the key", "No TTL", "Lock without a timeout"],
            refs=["[Redis](https://redis.io/docs/)"],
            nxt="#jobs-queues",
        ),
        lesson(
            "jobs-queues",
            "Queues, retries, backoff, DLQ, idempotency, schedules",
            "intermediate", "essential", 60,
            "Laravel jobs map to Redis/SQS workers. Duplicate delivery is normal. Idempotency keys on the write.",
            how="At-least-once: the worker may run twice. Store processed_message_id. Dead-letter after N tries. Exponential backoff with jitter.",
            compare="SNS on the resume is pub/sub. SQS is a queue. Do not say you administered SQS unless you did.",
            nxt="#jobs-webhooks",
        ),
        lesson(
            "jobs-webhooks",
            "Webhooks, HTTP clients, timeouts, circuit breakers",
            "intermediate", "essential", 45,
            "Outbound calls get a timeout, a retry policy for 502/503, and no retry on 400. Circuit breakers stop calling a dead peer.",
            nxt="#files-email",
        ),
        lesson(
            "files-email",
            "Files, object storage, signed URLs, email/SMS",
            "intermediate", "essential", 40,
            "S3 private buckets, short-lived signed GET. SMS stays on a worker. Do not list RDS on a project unless that project used it.",
            nxt="#test-api",
        ),
        lesson(
            "test-api",
            "Unit, API, database, and contract tests",
            "intermediate", "essential", 50,
            "HTTP tests hit TestClient. Database tests use a transaction rollback or a disposable schema. One test is the tenant isolation proof.",
            nxt="#arch-clean",
        ),
        lesson(
            "arch-clean",
            "Layered architecture, modular monolith, microservices",
            "intermediate", "essential", 40,
            "Default is a modular monolith. Microservices after a team and a failure domain need them. v4 already rejected seven toy apps.",
            nxt="#obs-prod",
        ),
        lesson(
            "obs-prod",
            "Logs, metrics, traces, health, shutdown",
            "intermediate", "essential", 45,
            "JSON logs with request_id. Metrics: rate, errors, duration, queue depth. Health: liveness vs readiness. SIGTERM finishes in-flight work.",
            refs=["[OpenTelemetry](https://opentelemetry.io/docs/)"],
            nxt="#sec-owasp",
        ),
        lesson(
            "sec-owasp",
            "OWASP, injection, XSS, CSRF, SSRF, CORS, secrets",
            "intermediate", "essential", 50,
            "Parameterized SQL. Escape HTML. CSRF on cookie sessions. Block SSRF by allowlisting outbound URLs. CORS is not auth.",
            refs=["[OWASP](https://owasp.org/)"],
            nxt="#linux-fs",
        ),
    ]),
]
