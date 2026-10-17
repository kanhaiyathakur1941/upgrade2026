from helper import lesson, mod

AI = [
    mod("ai-found", "LLM literacy for application engineers", [
        lesson(
            "ai-literacy",
            "AI, ML, DL, generative models, tokens, cost",
            "beginner", "essential", 45,
            "Enough to choose a model and a budget. Not an ML Engineer syllabus. Training vs inference. Context window. Tokens drive latency and money.",
            when="Use a hosted API first. Do not train. Fine-tuning is a later comparison, not the default.",
            refs=["[Hugging Face conceptual guides](https://huggingface.co/docs)"],
            nxt="#ai-api",
        ),
        lesson(
            "ai-api",
            "Calling LLM APIs from Python",
            "intermediate", "essential", 55,
            "Keys in env. Timeouts. Retries on 429/503. Streaming for UX. Structured output with a schema. Log tokens, not prompts that contain secrets.",
            code='''import os, json, urllib.request

def complete(prompt: str) -> dict:
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps({
            "model": "gpt-4.1-mini",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 200,
        }).encode(),
        headers={
            "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())''',
            out="A JSON object with choices[0].message.content when the key is set. Do not commit the key. Swap in the official SDK when you add the dependency.",
            refs=["[OpenAI API](https://platform.openai.com/docs/)"],
            nxt="#ai-prompt",
        ),
        lesson(
            "ai-prompt",
            "Prompts, tools, structured output, versioning",
            "intermediate", "essential", 45,
            "System message sets policy. Few-shot shows shape. Tool/function calling is a JSON contract. Version prompts in git like code.",
            nxt="#ai-embed",
        ),
        lesson(
            "ai-embed",
            "Embeddings, similarity, chunking, filters",
            "intermediate", "essential", 50,
            "An embedding is a vector. Cosine similarity finds neighbours. Chunk by heading, not a random 500 characters. Metadata filter tenant_id before similarity.",
            nxt="#ai-rag",
        ),
        lesson(
            "ai-rag",
            "RAG end to end",
            "advanced", "essential", 70,
            "Ingest, parse, clean, chunk, embed, index, retrieve, rerank, prompt, generate, cite, evaluate. Refuse when retrieval is empty.",
            how="Never put another tenant's chunks in the prompt. Citations are document ids returned by SQL, not invented by the model.",
            refs=["[roadmap.sh AI engineer](https://roadmap.sh/ai-engineer)"],
            nxt="#ai-pgvector",
        ),
        lesson(
            "ai-pgvector",
            "pgvector first; dedicated vector DBs later",
            "advanced", "essential", 40,
            "Keep vectors next to tenant rows. A separate vector database is for scale or hybrid features you can measure. Not a week-one dependency.",
            refs=["[pgvector](https://github.com/pgvector/pgvector)"],
            nxt="#ai-ingest",
        ),
        lesson(
            "ai-ingest",
            "PDFs and files: workers, duplicates, deletes, ACL",
            "advanced", "essential", 45,
            "Store the original in object storage. Parsing is a job. Dedup by hash. Deletes remove chunks. ACL is a SQL filter, not a prompt instruction.",
            nxt="#ai-tools",
        ),
        lesson(
            "ai-tools",
            "Tools, workflows, agents, human approval",
            "advanced", "advanced", 50,
            "After a working RAG path. A raw loop first: observe, decide, call, observe. Bound tools. Timeouts. Human approval for writes.",
            nxt="#ai-mcp",
        ),
        lesson(
            "ai-mcp",
            "Model Context Protocol, one real server",
            "advanced", "optional", 40,
            "MCP is a tool transport. One server that exposes tenant-scoped search is enough. After the raw loop.",
            refs=["[MCP](https://modelcontextprotocol.io/)"],
            nxt="#ai-sec",
        ),
        lesson(
            "ai-sec",
            "Prompt injection, leakage, tenant isolation, unsafe tools",
            "advanced", "essential", 45,
            "Documents are untrusted. A PDF must not become a system prompt. Tools cannot run shell. Isolation is in the query.",
            nxt="#ai-eval",
        ),
        lesson(
            "ai-eval",
            "Eval sets, groundedness, regression, humans",
            "advanced", "essential", 40,
            "Week of the first LLM endpoint: 20 questions in CI. Later 100, with retrieval scores. LLM-as-judge is a helper, not the only check.",
            nxt="#ai-obs",
        ),
        lesson(
            "ai-obs",
            "Traces, cost, cache, fallback, rate limits",
            "advanced", "essential", 35,
            "Log model, tokens, latency, tenant, prompt version, chunk ids. Fallback to a cheaper model on timeout. Cache identical prompts per tenant.",
            nxt="#ai-ft",
        ),
        lesson(
            "ai-ft",
            "Prompt vs RAG vs fine-tune — a decision, not a career",
            "advanced", "optional", 30,
            "Prompt for format. RAG for changing private documents. Fine-tune only for a stable style or schema, after you measured RAG. One small LoRA note is enough.",
            nxt="#ai-responsible",
        ),
        lesson(
            "ai-responsible",
            "Privacy, retention, consent, sensitive data",
            "intermediate", "essential", 25,
            "Do not paste loan PII into a public model. Retention policy on prompts. User consent for training if a vendor asks. Default is no training.",
            nxt="#ai-product",
        ),
        lesson(
            "ai-product",
            "AI features that sit on real APIs and SQL",
            "advanced", "essential", 30,
            "The assistant is a FastAPI route with auth, a usage table, and a worker. A notebook chatbot is a demo, not the portfolio.",
            nxt="#career-python-iv",
        ),
    ]),
]
