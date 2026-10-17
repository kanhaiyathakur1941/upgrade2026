from topics_lib import topic as t

PYTHON_MODULES = [
    {
        "id": "py-start",
        "title": "Start here — Python for a Laravel developer",
        "topics": [
            t(
                "py-diagnostic",
                "Python diagnostic (next lesson)",
                level="beginner",
                priority="essential",
                minutes=45,
                summary="Unverified checkpoint. Your files show a Car class and a working edit-distance function. They do not show decorators, typing, pytest, or FastAPI. Pass this before claiming Week 1 of the old roadmap is done.",
                prereq=["A Python 3 interpreter on this machine.", "Willingness to write from memory, not from this page."],
                blocks=[
                    {
                        "h": "What it is",
                        "p": [
                            "A 45-minute closed-book check so the rest of this curriculum does not restart at print statements or skip gaps.",
                            "Laravel maps: this is not PHPUnit. It is 'can you drive the language you will interview in?'",
                        ],
                    },
                    {
                        "h": "Why it exists",
                        "p": ["Public roadmap v4 compressed Python into weeks 1–2. There is no local evidence those weeks happened. Marking them done would be a lie."],
                    },
                    {
                        "h": "Closed-book task",
                        "ol": [
                            "Create a class with `__init__` that stores a name. Add an instance method that returns a greeting.",
                            "Add a `@staticmethod` that does not use `self`. Say one sentence on why you would use it versus an instance method.",
                            "Write two lines that show a list is mutable and a tuple is not.",
                            "Without opening `script.py`, state what `min_edit_distance('cat', 'cats')` returns and why.",
                        ],
                    },
                    {
                        "h": "A fair example (look after you attempt)",
                        "code": "class User:\n    def __init__(self, name: str) -> None:\n        self.name = name\n\n    def greet(self) -> str:\n        return f'hello {self.name}'\n\n    @staticmethod\n    def roles() -> tuple[str, ...]:\n        return ('reader', 'admin')\n\nnames = ['a']\nnames.append('b')  # list mutates\n# ('a',).append('b')  # AttributeError\n",
                        "out": "Fix the staticmethod indent if you copied this. `roles` is a function on the class that needs no instance. Edit distance of cat→cats is 1 (one insert).",
                    },
                    {
                        "h": "How to score it",
                        "ul": [
                            "Fluent: you wrote all four without searching. Same day continue to #py-functions.",
                            "Stalled on classes: open #py-oop then retake this page.",
                            "Forgot edit distance: that is fine. Open #dsa-dp after the Python functions lesson, not before pytest.",
                            "Abstract base classes: `abstractex.py` is commented out. Do not tick ABC complete.",
                        ],
                    },
                    {
                        "h": "Practice exercise",
                        "p": ["Run your class file. Then run `python3 -c \"print(1)\"` only if the interpreter is missing — install 3.11+ and a venv first (#py-env)."],
                    },
                    {
                        "h": "Interview questions",
                        "ul": [
                            "What is the difference between a list and a tuple?",
                            "When is a static method the wrong tool?",
                            "How would you describe your Python level honestly given Laravel is your production language?",
                        ],
                    },
                    {
                        "h": "Official documentation",
                        "p": ["[Python tutorial](https://docs.python.org/3/tutorial/)"],
                    },
                    {
                        "h": "Completion checklist",
                        "ul": [
                            "Four tasks written from memory.",
                            "Branch chosen: functions next, or classes then retry.",
                            "This topic marked done only after the four tasks, not because you read the page.",
                        ],
                    },
                    {"h": "Next", "p": ["If pass: #py-functions. If fail: #py-oop. Environment gaps: #py-env."]},
                ],
            ),
            t(
                "py-env",
                "Install, versions, venv, pip, project layout",
                level="beginner",
                priority="essential",
                minutes=75,
                summary="The equivalent of a PHP runtime plus Composer, except the unit of isolation is a virtual environment per project.",
                prereq=["macOS or Linux shell. You already use Ubuntu in production."],
                blocks=[
                    {
                        "h": "What it is",
                        "p": [
                            "CPython is the interpreter. `python3 --version` must be 3.11 or 3.12 for this plan. A venv is a folder of that interpreter plus packages so Gomilestone PHP and this repo do not share site-packages.",
                            "Laravel map: `vendor/` is Composer. `.venv/` is pip. `pyproject.toml` is closer to `composer.json` than `requirements.txt` is, but you will still pin a lock file.",
                        ],
                    },
                    {
                        "h": "Why it exists",
                        "p": ["Global `pip install` on a laptop is how two projects disagree about FastAPI versions. Production already taught you that undeclared PHP extensions fail deploys. Same rule."],
                    },
                    {
                        "h": "How it works",
                        "code": "python3 -m venv .venv\nsource .venv/bin/activate\npython -m pip install --upgrade pip\npython -m pip install fastapi uvicorn pytest\npython -m pip freeze > requirements.lock\n",
                        "out": "Prompt shows `(.venv)`. `which python` points inside `.venv`.",
                    },
                    {
                        "h": "Suggested layout for the one repo",
                        "code": "docassist/\n  pyproject.toml\n  README.md\n  app/\n    __init__.py\n    api/\n    domain/\n    workers/\n  tests/\n  alembic/\n",
                    },
                    {
                        "h": "Common mistakes",
                        "ul": [
                            "Installing packages with a system Python then running a different interpreter.",
                            "Committing `.venv`.",
                            "Using `python` on macOS and silently getting 2.7 or no file.",
                        ],
                    },
                    {
                        "h": "Task",
                        "p": ["Create `docassist` with a venv. Add an empty `app/__init__.py` and `tests/test_health.py` that asserts `True`. Commit without the venv."],
                    },
                    {
                        "h": "References",
                        "p": ["[venv](https://docs.python.org/3/library/venv.html) · [pip](https://pip.pypa.io/en/stable/)"],
                    },
                    {"h": "Next", "p": ["#py-syntax"]},
                ],
            ),
            t(
                "py-syntax",
                "Syntax, names, types, mutability, truthiness",
                level="beginner",
                priority="essential",
                minutes=80,
                summary="Indentation is the block. Identity is `is`. Equality is `==`. Empty containers are false.",
                prereq=["#py-env or a working 3.11+ REPL"],
                blocks=[
                    {
                        "h": "What it is",
                        "p": [
                            "Names bind to objects. `a = []` then `b = a` means two names, one list. `b.append(1)` mutates what `a` sees.",
                            "PHP map: PHP arrays copy on assign in some cases and objects do not. Python never copies on assign.",
                        ],
                    },
                    {
                        "h": "How it works",
                        "code": "x = 10\ny = 10\nprint(x == y, x is y)  # True True for small ints may intern\n\na = [1]\nb = a\nc = list(a)\nb.append(2)\nprint(a, c)  # [1, 2] [1]\n\nprint(bool(''), bool('0'), bool([]), bool([0]))\n",
                        "out": "`a` is `[1, 2]`, `c` is `[1]`. Empty string and empty list are false. `'0'` is true.",
                    },
                    {
                        "h": "When not to use `is`",
                        "p": ["Use `is` for `None`, `True`, `False`, and sentinels. Use `==` for values. `is` on strings or ints that look equal is an intern detail, not a contract."],
                    },
                    {
                        "h": "Exercise",
                        "p": ["Write a function `truthy_keys(d)` that returns keys whose values are truthy. Test `{'a': 0, 'b': 'x', 'c': []}` → `['b']`."],
                    },
                    {"h": "References", "p": ["[Built-in types](https://docs.python.org/3/library/stdtypes.html)"]},
                    {"h": "Next", "p": ["#py-strings"]},
                ],
            ),
            t(
                "py-strings",
                "Strings, slicing, f-strings, Unicode, regex",
                level="beginner",
                priority="essential",
                minutes=70,
                summary="Python strings are immutable Unicode. Slicing copies. Regex lives in `re`.",
                prereq=["#py-syntax"],
                blocks=[
                    {
                        "h": "How it works",
                        "code": "s = 'invoice-1042.pdf'\nprint(s[-4:], s.split('-')[0])\nprint(f'{s=}')\nimport re\nprint(re.findall(r'\\d+', s))\n",
                        "out": "`pdf` and `invoice`. `s='invoice-1042.pdf'`. `['1042']`.",
                    },
                    {
                        "h": "Backend example",
                        "p": ["Tenant slugs, filenames, and prompt snippets all need sanitising. Do not build SQL with f-strings. Use bound parameters later in SQLAlchemy."],
                    },
                    {
                        "h": "Mistakes",
                        "ul": [
                            "`s[0] = 'x'` raises TypeError.",
                            "Calling `.replace` and throwing away the return value.",
                            "Using regex when `str.endswith` is enough.",
                        ],
                    },
                    {
                        "h": "Task",
                        "p": ["In the repo, write `app/text.py` with `safe_filename(name)` that keeps letters, digits, dash, underscore, and a single extension. Test `../a.PDF` does not escape a directory."],
                    },
                    {"h": "References", "p": ["[re](https://docs.python.org/3/library/re.html) · [f-strings](https://docs.python.org/3/tutorial/inputoutput.html)"]},
                    {"h": "Next", "p": ["#py-collections"]},
                ],
            ),
            t(
                "py-collections",
                "Lists, tuples, sets, dicts, comprehensions, copying",
                level="beginner",
                priority="essential",
                minutes=90,
                summary="These four types are the working memory of Python backends. Know average complexity: dict/set get is O(1) average; list insert at 0 is O(n).",
                prereq=["#py-syntax"],
                blocks=[
                    {
                        "h": "How it works",
                        "code": "from copy import deepcopy\nids = {1, 2, 2}\nby_org = {'acme': ['a.pdf']}\nclone = deepcopy(by_org)\nclone['acme'].append('b.pdf')\nprint(ids, by_org)\nprint([n.upper() for n in by_org['acme']])\n",
                        "out": "`{1, 2}` and `{'acme': ['a.pdf']}` if deepcopy worked. Comprehension prints `['A.PDF']` on the original names.",
                    },
                    {
                        "h": "When to use which",
                        "ul": [
                            "list — ordered documents, job batches.",
                            "tuple — fixed pairs, dict keys if frozen.",
                            "set — membership, unique tenant ids.",
                            "dict — JSON-shaped records, indexes in memory.",
                        ],
                    },
                    {
                        "h": "Laravel map",
                        "p": ["PHP associative arrays do all of this. In Python, mixing list and dict operations on the same object is a type error. That is a feature."],
                    },
                    {
                        "h": "Exercise",
                        "p": ["Deduplicate a list of emails case-insensitively while keeping first-seen order. Test with `['A@x', 'a@x', 'b@x']`."],
                    },
                    {"h": "References", "p": ["[Data structures tutorial](https://docs.python.org/3/tutorial/datastructures.html)"]},
                    {"h": "Next", "p": ["#py-control"]},
                ],
            ),
            t(
                "py-control",
                "if, loops, iterables, enumerate, zip",
                level="beginner",
                priority="essential",
                minutes=50,
                summary="`for` iterates any iterable. `range` is not a list in Python 3. `else` on a loop runs if there was no `break`.",
                prereq=["#py-collections"],
                blocks=[
                    {
                        "h": "Example",
                        "code": "files = ['a.pdf', 'b.txt']\nfor i, name in enumerate(files, start=1):\n    print(i, name)\nfor left, right in zip(files, ['pdf', 'txt']):\n    assert name_ok := left.endswith(right)\n",
                        "out": "Prints `1 a.pdf` then `2 b.txt`. The walrus in the assert is optional; skip it if it feels cute rather than clear.",
                    },
                    {
                        "h": "Task",
                        "p": ["Write `first_pdf(names)` that returns the first name ending with `.pdf` or `None`. Do not index blindly."],
                    },
                    {"h": "Next", "p": ["#py-functions"]},
                ],
            ),
        ],
    },
    {
        "id": "py-core",
        "title": "Functions, OOP, errors, typing",
        "topics": [
            t(
                "py-functions",
                "Functions, scope, closures, *args, decorators",
                level="intermediate",
                priority="essential",
                minutes=100,
                summary="Functions are objects. Decorators are functions that return functions. This is the first topic after a passed diagnostic.",
                prereq=["#py-diagnostic passed or #py-oop if you stalled"],
                blocks=[
                    {
                        "h": "What it is",
                        "p": [
                            "Parameters can be positional, keyword-only, `*args`, `**kwargs`. Default values are bound once. Never use a mutable default list.",
                            "A decorator `@f` means `g = f(g)`. FastAPI uses this for routes. Laravel uses attributes and middleware instead.",
                        ],
                    },
                    {
                        "h": "How it works",
                        "code": "from functools import wraps\nimport time\n\ndef timed(fn):\n    @wraps(fn)\n    def wrapper(*args, **kwargs):\n        t0 = time.perf_counter()\n        try:\n            return fn(*args, **kwargs)\n        finally:\n            print(fn.__name__, round(time.perf_counter() - t0, 4))\n    return wrapper\n\n@timed\ndef add(a: int, b: int = 0) -> int:\n    return a + b\n\nprint(add(2, b=3))\n",
                        "out": "Prints `5` then a line `add 0.0…`.",
                    },
                    {
                        "h": "Closure",
                        "code": "def make_limiter(max_n: int):\n    n = 0\n    def allow() -> bool:\n        nonlocal n\n        n += 1\n        return n <= max_n\n    return allow\n\nallow = make_limiter(2)\nprint(allow(), allow(), allow())\n",
                        "out": "`True True False`",
                    },
                    {
                        "h": "Mistakes",
                        "ul": [
                            "`def f(items=[])` shares one list across calls.",
                            "Forgetting `@wraps` so tests and traces show `wrapper`.",
                            "Using a decorator when a plain function call is clearer.",
                        ],
                    },
                    {
                        "h": "Task",
                        "p": ["Add `app/timing.py` with `timed`. Wrap a function that sleeps 0.01s. Assert the test still sees the original `__name__`."],
                    },
                    {
                        "h": "Generators",
                        "p": ["`yield` turns a function into an iterator. Use it to stream chunk text without loading a whole PDF as one string. A generator expression `(x for x in xs)` is a lazy comprehension."],
                        "code": "def chunks(text: str, n: int):\n    for i in range(0, len(text), n):\n        yield text[i:i + n]\n\nprint(list(chunks('abcdef', 2)))\n",
                        "out": "`['ab', 'cd', 'ef']`",
                    },
                    {"h": "Interview", "p": ["Explain a decorator without saying 'it is a decorator'. Tie it to logging or auth. When is yield better than returning a list?"]},
                    {"h": "References", "p": ["[Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)"]},
                    {"h": "Next", "p": ["#py-oop"]},
                ],
            ),
            t(
                "py-oop",
                "Classes, methods, inheritance, dataclasses, protocols",
                level="intermediate",
                priority="essential",
                minutes=110,
                summary="Your `Car` file proves instance methods. ABC is still commented out in `abstractex.py`. Composition beats deep trees in backends.",
                prereq=["#py-functions"],
                blocks=[
                    {
                        "h": "What it is",
                        "p": [
                            "`__init__` is not a constructor in the C++ sense; it initialises an already created instance. `@classmethod` receives the class. `@staticmethod` receives neither.",
                            "Dataclasses generate `__init__` and `__repr__`. Protocols describe a shape without inheritance (duck typing made explicit).",
                        ],
                    },
                    {
                        "h": "Example",
                        "code": "from abc import ABC, abstractmethod\nfrom dataclasses import dataclass\nfrom typing import Protocol\n\nclass Embedder(Protocol):\n    def embed(self, text: str) -> list[float]: ...\n\nclass Storage(ABC):\n    @abstractmethod\n    def put(self, key: str, data: bytes) -> None: ...\n\n@dataclass\nclass Document:\n    id: str\n    org_id: str\n    title: str\n",
                    },
                    {
                        "h": "Laravel map",
                        "p": ["Eloquent models are Active Record. Dataclasses plus a repository are closer to a service + DTO split. Interfaces in PHP are Protocols here if you do not need runtime enforcement, ABCs if you do."],
                    },
                    {
                        "h": "Task",
                        "p": ["Uncomment and fix `abstractex.py` locally, or better: implement `Storage` with an in-memory dict in the docassist repo. Do not copy the commented file into GitHub as if it were production."],
                    },
                    {"h": "References", "p": ["[Classes](https://docs.python.org/3/tutorial/classes.html) · [dataclasses](https://docs.python.org/3/library/dataclasses.html)"]},
                    {"h": "Next", "p": ["#py-exceptions"]},
                ],
            ),
            t(
                "py-exceptions",
                "Exceptions, cleanup, logging",
                level="intermediate",
                priority="essential",
                minutes=70,
                summary="Raise specific errors. Log with a request id. Never return None to hide a failure on a payment-shaped path.",
                prereq=["#py-oop"],
                blocks=[
                    {
                        "h": "Example",
                        "code": "import logging\nlog = logging.getLogger('docassist')\n\nclass NotFound(Exception):\n    pass\n\ndef get_doc(store: dict, doc_id: str) -> dict:\n    try:\n        return store[doc_id]\n    except KeyError as exc:\n        raise NotFound(doc_id) from exc\n",
                    },
                    {
                        "h": "Laravel map",
                        "p": ["This is a Domain Exception plus `report()`. `from exc` is exception chaining, like previous throwable."],
                    },
                    {
                        "h": "Task",
                        "p": ["Configure logging to stderr as JSON-ish key=value including `request_id`. Raise `NotFound` from a lookup and assert `__cause__` is KeyError."],
                    },
                    {"h": "References", "p": ["[logging](https://docs.python.org/3/library/logging.html) · [exceptions](https://docs.python.org/3/tutorial/errors.html)"]},
                    {"h": "Next", "p": ["#py-typing"]},
                ],
            ),
            t(
                "py-typing",
                "Type hints, generics, TypedDict, checking",
                level="intermediate",
                priority="essential",
                minutes=80,
                summary="Hints are not runtime enforcement unless you use Pydantic. They are for readers, editors, and `mypy` or `ty`.",
                prereq=["#py-functions"],
                blocks=[
                    {
                        "h": "Example",
                        "code": "from typing import TypedDict, Literal\n\nclass Page(TypedDict):\n    items: list[str]\n    next: str | None\n\nRole = Literal['reader', 'admin']\n\ndef can_read(role: Role, org_id: str, doc_org: str) -> bool:\n    return role == 'admin' or org_id == doc_org\n",
                    },
                    {
                        "h": "When not to",
                        "p": ["Do not annotate every local `i: int = 0`. Annotate public functions and dicts that cross API boundaries."],
                    },
                    {
                        "h": "Task",
                        "p": ["Add hints to `safe_filename` and run a type checker if installed. A failing hint is a lesson, not a resume line."],
                    },
                    {"h": "References", "p": ["[typing](https://docs.python.org/3/library/typing.html)"]},
                    {"h": "Next", "p": ["#py-modules"]},
                ],
            ),
        ],
    },
    {
        "id": "py-prod",
        "title": "Modules, tests, async, quality",
        "topics": [
            t(
                "py-modules",
                "Modules, packages, pyproject.toml",
                level="intermediate",
                priority="essential",
                minutes=60,
                summary="`__name__ == '__main__'` is the PHP equivalent of a file that is both includable and runnable. Packages need `__init__.py` or implicit namespace discipline.",
                prereq=["#py-env"],
                blocks=[
                    {
                        "h": "Example",
                        "code": "# pyproject.toml\n[project]\nname = 'docassist'\nversion = '0.1.0'\nrequires-python = '>=3.11'\ndependencies = ['fastapi', 'sqlalchemy', 'pydantic-settings']\n",
                    },
                    {
                        "h": "Task",
                        "p": ["Put a real `pyproject.toml` in the repo. Install with `pip install -e .` inside the venv."],
                    },
                    {"h": "References", "p": ["[Modules](https://docs.python.org/3/tutorial/modules.html)"]},
                    {"h": "Next", "p": ["#py-stdlib"]},
                ],
            ),
            t(
                "py-stdlib",
                "Paths, JSON, env, dates, decimal",
                level="beginner",
                priority="essential",
                minutes=70,
                summary="Use `pathlib`, `json`, `os.environ` / pydantic-settings, `datetime` timezone-aware, `Decimal` for money. Never float for currency — same rule as the Accenture day 13 notes.",
                prereq=["#py-syntax"],
                blocks=[
                    {
                        "h": "Example",
                        "code": "from datetime import datetime, timezone\nfrom decimal import Decimal\nfrom pathlib import Path\nimport json\n\ncreated = datetime.now(timezone.utc).isoformat()\namount = Decimal('1500.50')\nPath('/tmp/docassist-sample.json').write_text(json.dumps({'created': created, 'amount': str(amount)}))\n",
                    },
                    {
                        "h": "Task",
                        "p": ["Write `app/money.py` with `paise(rupees: str) -> int` using Decimal. Reject more than two decimal places."],
                    },
                    {"h": "Next", "p": ["#py-pytest"]},
                ],
            ),
            t(
                "py-pytest",
                "pytest, fixtures, parametrize, mocks, coverage",
                level="intermediate",
                priority="essential",
                minutes=90,
                summary="pytest is PHPUnit with less boilerplate. Fixtures replace `setUp`. Parametrize replaces data providers.",
                prereq=["#py-functions", "#py-env"],
                blocks=[
                    {
                        "h": "Example",
                        "code": "import pytest\nfrom app.money import paise\n\n@pytest.mark.parametrize('raw,expected', [('0.00', 0), ('1.50', 150)])\ndef test_paise(raw, expected):\n    assert paise(raw) == expected\n\ndef test_rejects_three_places():\n    with pytest.raises(ValueError):\n        paise('1.234')\n",
                    },
                    {
                        "h": "Task",
                        "p": ["Run `pytest -q` in CI-shaped command. Add one mock of time only if you must; prefer pure functions."],
                    },
                    {"h": "References", "p": ["[pytest](https://docs.pytest.org/)"]},
                    {"h": "Next", "p": ["#py-solid"]},
                ],
            ),
            t(
                "py-solid",
                "SOLID, DI, clean boundaries",
                level="intermediate",
                priority="essential",
                minutes=60,
                summary="You already practised SOLID on Accenture day 4 in PHP. Repeat it in Python: FastAPI Depends is the container.",
                prereq=["#py-oop"],
                blocks=[
                    {
                        "h": "How it maps",
                        "ul": [
                            "S — a worker module does not parse HTTP.",
                            "O — new Embedder without editing the retriever.",
                            "L — fakes in tests must honour timeouts.",
                            "I — do not force Storage to implement search.",
                            "D — pass a protocol, not a concrete S3 client, into domain code.",
                        ],
                    },
                    {
                        "h": "Task",
                        "p": ["Draw the first repo layers: api / domain / adapters. One page in README."],
                    },
                    {"h": "Next", "p": ["#py-async"]},
                ],
            ),
            t(
                "py-async",
                "Threads, GIL, asyncio, context managers",
                level="advanced",
                priority="essential",
                minutes=100,
                summary="The GIL means CPU-bound Python threads do not speed numeric loops. I/O-bound FastAPI work uses async. Workers can be processes.",
                prereq=["#py-functions"],
                blocks=[
                    {
                        "h": "What it is",
                        "p": [
                            "`async def` is a coroutine. `await` yields the event loop. Blocking `time.sleep` or `requests.get` inside async endpoints stalls everyone else on that worker.",
                            "Laravel: HTTP is usually sync PHP-FPM. You already moved SMS to queues. Same instinct: do not hold the request for PDF parse or LLM calls that exceed a second without streaming or a job.",
                        ],
                    },
                    {
                        "h": "Example",
                        "code": "import asyncio\nfrom contextlib import asynccontextmanager\n\n@asynccontextmanager\nasync def lifespan():\n    print('start')\n    yield\n    print('stop')\n\nasync def fetch():\n    await asyncio.sleep(0.01)\n    return 'ok'\n\nasync def main():\n    print(await asyncio.gather(fetch(), fetch()))\n\nasyncio.run(main())\n",
                        "out": "`['ok', 'ok']` after about 0.01s, not 0.02s.",
                    },
                    {
                        "h": "When not to",
                        "p": ["Do not make a function async if it never awaits. Do not run CPU-heavy chunking on the event loop; use a process pool or a worker."],
                    },
                    {
                        "h": "Task",
                        "p": ["Write a test that `asyncio.gather` of two 50ms sleeps finishes under 80ms."],
                    },
                    {"h": "References", "p": ["[asyncio](https://docs.python.org/3/library/asyncio.html)"]},
                    {"h": "Next", "p": ["#py-memory"]},
                ],
            ),
            t(
                "py-memory",
                "Memory, profiling, performance",
                level="advanced",
                priority="advanced",
                minutes=50,
                summary="Objects are heap-allocated. Large PDF bytes in RAM will hurt before CPU does. Profile before rewriting algorithms.",
                prereq=["#py-async"],
                blocks=[
                    {
                        "h": "How to look",
                        "p": ["`python -m cProfile` for CPU. Watch RSS when ingesting files. Streaming parse beats `read()` of a 200MB PDF."],
                    },
                    {
                        "h": "Task",
                        "p": ["Note in README: max upload size you will accept in the API and why."],
                    },
                    {"h": "Next", "p": ["#dsa-big-o"]},
                ],
            ),
        ],
    },
]
