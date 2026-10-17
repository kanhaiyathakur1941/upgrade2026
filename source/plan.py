from datetime import date, timedelta

START = date(2026, 10, 18)


def d(n: int) -> str:
    return (START + timedelta(days=n - 1)).isoformat()


PLAN = [
    {"day": 1, "date": d(1), "focus": "Closed-book #py-diagnostic. If stuck, #py-classes. If fluent, #py-functions the same afternoon.", "build": "Repo skeleton, venv, README. Do not start Accenture day 15."},
    {"day": 2, "date": d(2), "focus": "#py-decorators and finish ABC from abstractex.py as tests in the new repo.", "build": "Logged decorator plus PaymentGateway ABC."},
    {"day": 3, "date": d(3), "focus": "#py-exceptions #py-typing #py-stdlib money and UTC.", "build": "TenantMismatch and Decimal helpers with pytest."},
    {"day": 4, "date": d(4), "focus": "#py-pytest #py-packaging. Two sum from #dsa-hash as a warm-up.", "build": "pytest.ini and CI-ready local command."},
    {"day": 5, "date": d(5), "focus": "#http-basics #http-rest. Compare to Ugro portal verbs you actually shipped.", "build": "Written error body and status code table in README."},
    {"day": 6, "date": d(6), "focus": "#fastapi-core list/create documents.", "build": "Project 2 started: FastAPI + TestClient."},
    {"day": 7, "date": d(7), "focus": "Revision day. Redo diagnostic. Four DSA beginner problems spoken aloud.", "build": "No new library."},
    {"day": 8, "date": d(8), "focus": "#sql-schema #sql-query on a local PostgreSQL.", "build": "orgs, users, documents tables. Five EXPLAIN notes."},
    {"day": 9, "date": d(9), "focus": "#orm-alchemy Alembic.", "build": "Migrations in the repo."},
    {"day": 10, "date": d(10), "focus": "#fastapi-prod Depends for a fake current user.", "build": "Tenant id on every query."},
    {"day": 11, "date": d(11), "focus": "#dsa-two-pointers and longest substring without repeat.", "build": "One problem file with tests."},
    {"day": 12, "date": d(12), "focus": "#http-json OpenAPI as a file in the repo. Practice only.", "build": "openapi.yaml matching the documents API."},
    {"day": 13, "date": d(13), "focus": "#py-async timeouts on a fake outbound call.", "build": "Async client tests for timeout."},
    {"day": 14, "date": d(14), "focus": "Checkpoint. Speak FastAPI request path. #career-story first draft.", "build": "90-second intro recorded. Python is growing; Laravel is shipped."},
    {"day": 15, "date": d(15), "focus": "#auth-core hashing. Session vs JWT drawing.", "build": "Password hash on user create. JWT remains labelled practice."},
    {"day": 16, "date": d(16), "focus": "RBAC on documents.", "build": "Org A cannot read org B, with a failing test first."},
    {"day": 17, "date": d(17), "focus": "#cache-redis cache-aside on GET document.", "build": "Tenant in the cache key."},
    {"day": 18, "date": d(18), "focus": "#docker-core Compose: api, postgres, redis.", "build": "One command to boot."},
    {"day": 19, "date": d(19), "focus": "#dsa-dp finish knapsack tests.", "build": "knapsack module, not the Desktop stub."},
    {"day": 20, "date": d(20), "focus": "Revision + first tailored applications (week 3).", "build": "8 applications. Log privately."},
    {"day": 21, "date": d(21), "focus": "#sec-owasp CORS vs auth, SQL injection proof with parameters.", "build": "Security notes in README."},
    {"day": 22, "date": d(22), "focus": "#test-api isolation tests.", "build": "Definition of done for project 2."},
    {"day": 23, "date": d(23), "focus": "#career-resume rewrite. Laravel proof, Python building.", "build": "One-page resume draft. No new keywords."},
    {"day": 24, "date": d(24), "focus": "#sd-url on paper then as a module if time.", "build": "Design one-pager."},
    {"day": 25, "date": d(25), "focus": "Project 3 auth polish.", "build": "Refresh token hashed or a documented session design."},
    {"day": 26, "date": d(26), "focus": "#jobs-queues worker skeleton.", "build": "Project 4 started: notify job idempotent."},
    {"day": 27, "date": d(27), "focus": "#linux-fs #linux-net on your own machine.", "build": "Journal of commands you actually ran."},
    {"day": 28, "date": d(28), "focus": "Weekly mock from Interview tab, Python + SQL.", "build": "Three weak answers written."},
    {"day": 29, "date": d(29), "focus": "#git-flow PR hygiene.", "build": "Protected main, if the repo is yours."},
    {"day": 30, "date": d(30), "focus": "Month close: Compose demo, tenant test, resume, 20+ applications cumulative.", "build": "Tag v0.1.0."},
    {"day": 35, "date": d(35), "focus": "Project 4 DLQ and retry with jitter.", "build": "Failed job visible."},
    {"day": 40, "date": d(40), "focus": "#cicd-gha pytest on PR.", "build": "Project 5 green check."},
    {"day": 45, "date": d(45), "focus": "#obs-prod JSON logs and request_id.", "build": "One broken request traced."},
    {"day": 50, "date": d(50), "focus": "#aws-core study plus the smallest real deploy you can pay for or a documented local-prod.", "build": "Project 6 architecture note. Do not claim ECS if you used EC2."},
    {"day": 55, "date": d(55), "focus": "#sd-pay and #sd-notify on paper.", "build": "Two diagrams in /designs."},
    {"day": 60, "date": d(60), "focus": "#ai-literacy #ai-api streaming endpoint with usage log.", "build": "20-question eval file. Keys in env."},
    {"day": 70, "date": d(70), "focus": "#ai-prompt structured output. Cost note.", "build": "Prompt version in git."},
    {"day": 80, "date": d(80), "focus": "Mocks twice a week. DSA maintenance. Keep applying.", "build": "Application tracker review."},
    {"day": 90, "date": d(90), "focus": "₹20 LPA gate: FastAPI service, tests, Docker, one LLM endpoint, honest Laravel stories.", "build": "Capstone not required. RAG is next, not a blocker for the first ₹20 LPA conversations."},
]

LATER = [
    "Days 90–120: #ai-ingest #ai-embed #ai-pgvector #ai-rag with citations and tenant filters. Project 7–8.",
    "Then #ai-eval to 100 questions, #ai-sec, #ai-obs. That is the v4 week-24 spirit, compressed only if the API is already real.",
    "₹30 LPA conversations after you can defend retrieval quality, cost, and a failure. Not on day 90 by default.",
    "Projects 9–10, #ai-tools #ai-mcp after RAG. #iac-tf #k8s-fund #Kafka only if a target role names them.",
    "Kafka reference stays [Apache Kafka docs](https://kafka.apache.org/documentation/) until you have a reason to run it.",
]
