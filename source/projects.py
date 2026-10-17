PROJECTS = [
    {
        "id": "p1",
        "title": "1 · CLI inspector, packaged and tested",
        "problem": "You will ingest files later. Today you need a tested command that reads a path, prints encoding and byte size, and fails closed on a missing file.",
        "blocks": [
            {"h": "Scope", "ul": ["Python package", "pytest", "no network", "maps to the text inspector in roadmap v4 week 2"]},
            {"h": "Folder", "code": "src/assistant_cli/\ntests/\npyproject.toml"},
            {"h": "Done when", "ul": ["`python -m pytest` is green", "README has install steps", "You can explain pathlib vs open()"]},
            {"h": "Stretch", "ul": ["Detect a likely PDF by magic bytes without parsing it"]},
            {"h": "Interview", "ul": ["Why packaging before FastAPI?", "How do you test a CLI without OS noise?"]},
        ],
    },
    {
        "id": "p2",
        "title": "2 · FastAPI CRUD with PostgreSQL",
        "problem": "A tenant stores document metadata. List, get, create. This is the Laravel API you already know, in Python.",
        "blocks": [
            {"h": "API", "ul": ["POST /v1/documents", "GET /v1/documents", "GET /v1/documents/{id}", "consistent 422 body"]},
            {"h": "Schema", "ul": ["tenants", "users", "documents(id, tenant_id, title, created_at)"]},
            {"h": "Security", "ul": ["No cross-tenant get", "SQL parameters only"]},
            {"h": "Done when", "ul": ["Alembic migrations", "TestClient coverage", "OpenAPI matches the routes"]},
            {"h": "Interview", "ul": ["Eloquent vs SQLAlchemy session", "Where does pagination live?"]},
        ],
    },
    {
        "id": "p3",
        "title": "3 · Auth and authorization API",
        "problem": "Org membership must be enforced on every query. Practice JWT or a signed session. Label it practice on the resume until it has been in production.",
        "blocks": [
            {"h": "Requirements", "ul": ["Register/login", "password hash", "RBAC: owner vs member", "tenant check in SQL"]},
            {"h": "Done when", "ul": ["Failing test for org B reading org A", "Secrets only in env"]},
            {"h": "Interview", "ul": ["How is this different from Ugro roles on one account?"]},
        ],
    },
    {
        "id": "p4",
        "title": "4 · Notification worker",
        "problem": "Document events fan out to a fake SMS/email provider. Duplicates must not double-send.",
        "blocks": [
            {"h": "Flow", "ul": ["API writes outbox row", "worker claims row", "provider call with timeout", "processed_id unique"]},
            {"h": "Done when", "ul": ["Retry twice then DLQ", "Idempotent consumer test"]},
            {"h": "Compare", "p": ["Laravel ShouldQueue and failed_jobs. SNS on the resume is not this worker unless you actually used it this way."]},
        ],
    },
    {
        "id": "p5",
        "title": "5 · Docker and CI",
        "problem": "A reviewer clones the repo and runs Compose. GitHub Actions runs pytest.",
        "blocks": [
            {"h": "Done when", "ul": ["Non-root image", "compose healthchecks", "PR fails on red tests"]},
        ],
    },
    {
        "id": "p6",
        "title": "6 · Deployed API with logs",
        "problem": "The same repo on AWS or an honest local-prod. Architecture README. Cost note.",
        "blocks": [
            {"h": "Allowed claims", "ul": ["Only services you operated. EC2+Nginx is valid. ECS only after you use it."]},
            {"h": "Done when", "ul": ["HTTPS", "request_id in logs", "rollback sentence written"]},
        ],
    },
    {
        "id": "p7",
        "title": "7 · Ingestion and semantic search",
        "problem": "PDFs become chunks with embeddings. Search is tenant-scoped.",
        "blocks": [
            {"h": "Done when", "ul": ["Bad PDF recorded as failed", "Original in object storage", "Search SQL includes tenant_id"]},
        ],
    },
    {
        "id": "p8",
        "title": "8 · RAG with citations, evals, cost",
        "problem": "Answer only from retrieved chunks. Cite ids. 100-question suite later; 20 at first LLM week.",
        "blocks": [
            {"h": "Done when", "ul": ["Empty retrieval refuses", "Cost per request logged", "Eval in CI"]},
        ],
    },
    {
        "id": "p9",
        "title": "9 · Bounded tool-calling workflow",
        "problem": "The assistant may search or create a ticket-shaped record. Writes need approval. No shell tool.",
        "blocks": [
            {"h": "Done when", "ul": ["Raw loop you can draw", "Allowlist", "Audit row"]},
        ],
    },
    {
        "id": "p10",
        "title": "10 · Capstone: the same product, hardened",
        "problem": "Auth, Postgres, Redis, worker, Docker, deploy, RAG, evals. One README story.",
        "blocks": [
            {"h": "Done when", "ul": ["Threat model page", "5-minute spoken demo", "Resume lists only what is in the repo plus Laravel work"]},
            {"h": "Stretch", "ul": ["MCP server", "one LoRA comparison note", "never required for the first ₹20 LPA screen"]},
        ],
    },
]
