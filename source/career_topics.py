from helper import lesson, mod

CAREER = [
    mod("career-iv", "Interviews, resume, search", [
        lesson(
            "career-python-iv",
            "Python and coding rounds",
            "intermediate", "essential", 40,
            "Patterns from #dsa-ladder. Speak brute force, then the structure, then tests. PHP is allowed if they let you pick and the role is Laravel. For Python roles, write Python.",
            nxt="#career-backend-iv",
        ),
        lesson(
            "career-backend-iv",
            "API, SQL, Laravel-bridge rounds",
            "intermediate", "essential", 50,
            "Map Eloquent to SQLAlchemy, middleware to Depends, jobs to workers. Do not claim FastAPI production until project 2 is done.",
            nxt="#career-sys-iv",
        ),
        lesson(
            "career-sys-iv",
            "System design and AI-application rounds",
            "advanced", "essential", 45,
            "Draw the document assistant you built. If RAG is not built yet, draw the FastAPI service you did build and the RAG you are adding. Do not draw Kafka if it is not in the repo.",
            nxt="#career-story",
        ),
        lesson(
            "career-story",
            "How to tell 4.5 years without inflating Python",
            "beginner", "essential", 40,
            "Lead with Gomilestone from June 2022: portals, Razorpay, queues, Oracle on Religare, AWS EC2 deploys. Then: I am building the same class of system in Python, and here is the repo. Count 2018 training separately. Write your own sentence for August 2018–May 2022.",
            mistakes=["Saying 4.5+ years of Python", "Listing JWT as production", "Listing RDS on a project that only had it in a summary"],
            nxt="#career-resume",
        ),
        lesson(
            "career-resume",
            "Resume, GitHub, README, demo tape",
            "beginner", "essential", 40,
            "Laravel proof first. Python as the new system. Impact you can defend. GitHub only with a real URL; the old PDF had github.com/ truncated. README: architecture, how to run, trade-offs, eval numbers only if measured.",
            nxt="#career-mocks",
        ),
        lesson(
            "career-mocks",
            "Mock interviews and written answers",
            "intermediate", "essential", 30,
            "Use the Interview questions tab. Record one 45-minute technical and one 30-minute behavioral from week 4 onward.",
            nxt="#career-search",
        ),
        lesson(
            "career-search",
            "Search, weekly applications, negotiation, milestones",
            "beginner", "essential", 40,
            "From week 3: 8–12 tailored applications. Track company, role, stack, date, follow-up. Ask band ₹15–20 LPA with current CTC ₹7 LPA. ₹30 LPA is a later milestone after the RAG system is real.",
            task="A private applications.md that never goes in a public repo if it has names you should not share.",
            nxt="#py-diagnostic",
        ),
    ]),
]
