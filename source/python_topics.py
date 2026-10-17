from helper import lesson, mod

PY = [
    mod("py-start", "Start from the files you already have", [
        lesson(
            "py-diagnostic",
            "Diagnostic: do not restart Python from print()",
            "beginner", "essential", 45,
            "Prove what you already have, then skip ahead. This is the first lesson on 18 October 2026.",
            prereq="A Python 3 interpreter. Your files on this Mac: abstraction.py, abstractex.py, script.py, knapsackzeroonebyset.py.",
            what="A short closed-book check. It is not a day of new theory. Accenture Days 1–14 were a PHP sprint; this diagnostic is the first Python lesson in Upgrade 2026.",
            why="Restarting at installation wastes the only 90 days that matter for a ₹20 LPA screen. The files on disk already show a class, an edit-distance table, and a knapsack stub. They also show that ABC and a working knapsack are unfinished.",
            how="Sit without notes. Type four small programs. Mark this topic done only if all four are fluent. If one stalls, mark this topic revision and open #py-classes.",
            code='''class Loan:
    def __init__(self, principal: int) -> None:
        self.principal = principal

    def describe(self) -> str:
        return f"principal={self.principal}"

    @staticmethod
    def currency() -> str:
        return "INR"

print(Loan(50000).describe())
print(Loan.currency())
print([1, 2] is [1, 2])
print((1, 2) == (1, 2))

def min_edit_distance(w1: str, w2: str) -> int:
    m, n = len(w1), len(w2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if w1[i - 1] == w2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

print(min_edit_distance("cat", "cats"))''',
            out='principal=50000 then INR then False then True then 1. The last number matches the run of your existing script.py.',
            mistakes=[
                "Ticking this done because the public v4 roadmap listed Python in week 1.",
                "Calling the 2018 training four years of Python. It was Core PHP training.",
                "Skipping ABC forever because abstractex.py is commented out. That topic stays open until you write a working ABC.",
            ],
            exercise="Without this page, write the four programs in a new file. Time yourself. Over 20 minutes on any one item means #py-classes first.",
            task="Create a folder document-assistant/ and a tests/ folder. Do not start a second repo.",
            interview=["How would you explain four years of Laravel and still be honest that Python is growing?"],
            refs=["[Python tutorial](https://docs.python.org/3/tutorial/)"],
            checklist=["Four programs typed without copy-paste", "Fluent path: continue to #py-functions", "Stuck path: #py-classes then retake this"],
            nxt="#py-env if the interpreter is missing. Otherwise #py-functions if fluent, #py-classes if not.",
        ),
        lesson(
            "py-env",
            "Interpreter, versions, venv, pip, project layout",
            "beginner", "essential", 50,
            "The same hygiene Composer already taught you, in Python.",
            prereq="#py-diagnostic or a working python3.",
            what="Python 3.12+ interpreter, REPL, scripts, virtual environments, pip, and a src-or-package layout.",
            why="Global pip install is how two projects fight. Laravel already isolated PHP with Composer; venv is that isolation.",
            how="python3 -m venv .venv, then source .venv/bin/activate, then python -m pip install. Pin versions. Never commit .venv.",
            code='''# pyproject.toml (excerpt)
[project]
name = "document-assistant"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []

[project.optional-dependencies]
dev = ["pytest>=8"]''',
            mistakes=["python vs python3 on macOS", "pip install as a user package outside venv", "Checking venv into git"],
            compare="composer.json is pyproject.toml. vendor/ is .venv. composer.lock is a lock file you will add later with uv or pip-tools.",
            task="Create .venv, add .gitignore for it, write README with python -m pytest.",
            refs=["[venv](https://docs.python.org/3/library/venv.html)", "[Installing packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)"],
            nxt="#py-syntax",
        ),
    ]),
    mod("py-core", "Language you must speak without notes", [
        lesson(
            "py-syntax",
            "Syntax, names, types, mutability, truthiness",
            "beginner", "essential", 55,
            "Indentation is the block. Identity is not equality. Empty collections are false.",
            what="Comments, names, built-in types, mutability, is vs ==, conversion, operators, truthiness.",
            why="A Laravel if ($user) check and a Python if user: check fail on different empty values. Interviews start here because bugs start here.",
            code='''a = [1]
b = a
b.append(2)
print(a)          # [1, 2] — same list
print(a == [1, 2])
print(a is [1, 2])  # False — different objects
print(bool(""), bool([]), bool(0), bool("0"))''',
            out="[1, 2] then True then False then False False False True.",
            mistakes=["Using is for string or number equality", "Mutating a default list argument", "Treating '0' as empty"],
            task="Write five assert lines that fail if you mix is and ==.",
            refs=["[Data model](https://docs.python.org/3/reference/datamodel.html)"],
            nxt="#py-strings",
        ),
        lesson(
            "py-strings",
            "Strings, slicing, f-strings, Unicode, regex",
            "beginner", "essential", 50,
            "Text is Unicode. Slicing copies. Regex is a tool, not the first parser.",
            code='''import re
name = "Kanhaiya"
print(name[0:3])
print(f"{name} pays {1500.5:.2f}")
print(re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", "ABCDE1234F") is not None)''',
            out="Kan then Kanhaiya pays 1500.50 then True.",
            realistic="PAN-shaped validation belongs in a function with tests, the same way you already validate on Ugro. Do not paste client PAN numbers into a public repo.",
            mistakes=["Calling str.replace and ignoring that strings are immutable", "Bytes treated as text"],
            refs=["[re](https://docs.python.org/3/library/re.html)"],
            nxt="#py-collections",
        ),
        lesson(
            "py-collections",
            "List, tuple, set, dict, comprehensions, copying",
            "beginner", "essential", 55,
            "Lists grow. Tuples are records. Sets and dicts hash. deepcopy is rare.",
            code='''from copy import copy, deepcopy
roles = {"admin", "ops"}
loan = {"id": "L-1", "tags": ["overdue"]}
shallow = copy(loan)
deep = deepcopy(loan)
loan["tags"].append("legal")
print(shallow["tags"], deep["tags"])
print({r.upper() for r in roles})''',
            out="['overdue', 'legal'] ['overdue'] then {'ADMIN', 'OPS'}.",
            perf="Average dict/set lookup is O(1). Membership in a list is O(n). That is why a role check should not scan a long list in a hot path.",
            refs=["[collections](https://docs.python.org/3/library/collections.html)"],
            nxt="#py-control",
        ),
        lesson(
            "py-control",
            "Conditionals, loops, iterables, enumerate, zip",
            "beginner", "essential", 40,
            "for x in items is the default. range is for indexes you actually need.",
            code='''status = "PAID"
match status:
    case "PAID" | "SETTLED":
        print("closed")
    case _:
        print("open")
for i, name in enumerate(["Religare", "Ugro"], start=1):
    print(i, name)''',
            out="closed then 1 Religare then 2 Ugro.",
            compare="PHP foreach is this for. match is PHP 8 match.",
            nxt="#py-functions",
        ),
        lesson(
            "py-functions",
            "Functions, scope, closures, *args, lambdas",
            "intermediate", "essential", 60,
            "If the diagnostic was fluent, this is the same-day continuation. Default arguments are bound once.",
            why="Laravel controllers already inject services. Python functions that close over config are the same idea, and the default-list bug is the first interview trap.",
            code='''def add_tag(tag: str, bucket: list[str] | None = None) -> list[str]:
    if bucket is None:
        bucket = []
    bucket.append(tag)
    return bucket

print(add_tag("a"))
print(add_tag("b"))

def make_multiplier(n: int):
    def inner(x: int) -> int:
        return x * n
    return inner

double = make_multiplier(2)
print(double(21))''',
            out="['a'] then ['b'] then 42. If bucket=[] were the default, the second call would print ['a', 'b'].",
            mistakes=["Mutable default arguments", "Using a lambda for a multi-line function", "Returning None by accident after a print"],
            task="Write a retry helper that takes a callable and a max_tries integer. Test that it stops after three failures.",
            interview=["What is a closure?", "Why is def f(x=[]): a bug?"],
            refs=["[Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)"],
            nxt="#py-decorators",
        ),
        lesson(
            "py-decorators",
            "Decorators, generators, context managers",
            "intermediate", "essential", 70,
            "A decorator is a callable that wraps a callable. yield pauses. with closes the file even on error.",
            compare="Laravel middleware wraps a request. @app.get in FastAPI is a decorator. Eloquent scopes are not generators; Python generators are pull-based streams.",
            code='''from functools import wraps
from contextlib import contextmanager

def logged(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("call", fn.__name__)
        return fn(*args, **kwargs)
    return wrapper

@logged
def ping() -> str:
    return "ok"

def numbers():
    yield 1
    yield 2

@contextmanager
def fake_tx():
    print("begin")
    try:
        yield
        print("commit")
    except Exception:
        print("rollback")
        raise

print(ping())
print(list(numbers()))
with fake_tx():
    pass''',
            out="call ping then ok then [1, 2] then begin then commit.",
            task="Write a timer decorator that prints milliseconds. Wrap a dummy PDF parse function.",
            refs=["[functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps)", "[contextlib](https://docs.python.org/3/library/contextlib.html)"],
            nxt="#py-classes",
        ),
    ]),
    mod("py-oop-quality", "Objects, types, tests, packaging", [
        lesson(
            "py-classes",
            "Classes, methods, inheritance, composition, ABC",
            "intermediate", "essential", 70,
            "Your Car class in abstraction.py is a start. abstractex.py is commented out, so ABC is not done.",
            what="instance vs class vs static methods, inheritance, composition, MRO, properties, dataclasses, protocols, dunder methods, ABC.",
            why="PaymentGateway as an interface is the same story as Day 4 of the Accenture PHP plan. Python uses ABC or Protocol.",
            code='''from abc import ABC, abstractmethod
from dataclasses import dataclass

class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, paise: int) -> str: ...

class FakeRazorpay(PaymentGateway):
    def charge(self, paise: int) -> str:
        return f"ok:{paise}"

@dataclass
class Charge:
    paise: int
    currency: str = "INR"

print(FakeRazorpay().charge(100))
print(Charge(100))''',
            out="ok:100 then Charge(paise=100, currency='INR').",
            task="Uncomment and finish abstractex.py as a real ABC with two shapes, plus a pytest file. Leave the original file on disk; copy the idea into the new repo.",
            interview=["ABC versus Protocol", "When composition beats inheritance"],
            refs=["[abc](https://docs.python.org/3/library/abc.html)", "[dataclasses](https://docs.python.org/3/library/dataclasses.html)"],
            nxt="#py-exceptions",
        ),
        lesson(
            "py-exceptions",
            "Exceptions, chaining, logging, cleanup",
            "intermediate", "essential", 45,
            "Raise exceptions for contract failures. Log with structure. Never swallow and return None silently on money paths.",
            code='''import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("assistant")

class TenantMismatch(Exception):
    pass

def load_doc(doc_org: str, user_org: str) -> None:
    if doc_org != user_org:
        raise TenantMismatch("cross-tenant read")

try:
    load_doc("A", "B")
except TenantMismatch:
    log.exception("blocked")
    raise''',
            compare="Laravel's renderable exceptions and report() are this plus HTTP mapping, which FastAPI does in handlers.",
            refs=["[logging](https://docs.python.org/3/library/logging.html)"],
            nxt="#py-typing",
        ),
        lesson(
            "py-typing",
            "Type hints, unions, TypedDict, Protocols, checking",
            "intermediate", "essential", 50,
            "Hints are for humans and checkers. Runtime stays dynamic unless you use Pydantic.",
            code='''from typing import TypedDict, Literal

class Chunk(TypedDict):
    text: str
    tenant_id: str
    source: Literal["pdf", "html"]

def words(chunk: Chunk) -> int:
    return len(chunk["text"].split())''',
            refs=["[typing](https://docs.python.org/3/library/typing.html)"],
            nxt="#py-stdlib",
        ),
        lesson(
            "py-stdlib",
            "Files, paths, JSON, env, dates, decimal, csv",
            "beginner", "essential", 50,
            "Money is Decimal or integer paise. Time is timezone-aware. Secrets are environment, not source.",
            code='''from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, timezone
amount = Decimal("10.2").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
now = datetime.now(timezone.utc)
print(amount, now.tzinfo)''',
            out="10.20 and datetime.timezone.utc. Never float for balances. That rule already lived on Accenture Day 13.",
            refs=["[decimal](https://docs.python.org/3/library/decimal.html)", "[datetime](https://docs.python.org/3/library/datetime.html)"],
            nxt="#py-pytest",
        ),
        lesson(
            "py-pytest",
            "pytest, fixtures, parametrize, mocks, coverage",
            "intermediate", "essential", 60,
            "PHPUnit is pytest. A test is a function named test_*. Assertions are assert.",
            code='''import pytest

@pytest.mark.parametrize("a,b,expected", [("cat", "cats", 1), ("", "a", 1)])
def test_distance(a, b, expected):
    assert len(b) - len(a) == expected or a != b

def test_tenant_guard():
    with pytest.raises(PermissionError):
        raise PermissionError("org B")''',
            task="Add pytest.ini and two tests for the retry helper from #py-functions.",
            refs=["[pytest](https://docs.pytest.org/)"],
            nxt="#py-packaging",
        ),
        lesson(
            "py-packaging",
            "Modules, packages, pyproject, lock files",
            "intermediate", "essential", 40,
            "__name__ == '__main__' is a script. A package has __init__.py or is a src layout with pyproject.toml.",
            refs=["[Packaging](https://packaging.python.org/)"],
            nxt="#py-quality",
        ),
        lesson(
            "py-quality",
            "SOLID, patterns, DI, clean boundaries",
            "intermediate", "essential", 45,
            "You already practiced SOLID on Accenture Day 4 in PHP. Repeat it in Python: controller thin, domain in services, I/O at the edge.",
            interview=["Give a Laravel example of DIP and the Python equivalent."],
            nxt="#py-async",
        ),
        lesson(
            "py-async",
            "Threads, processes, GIL, asyncio",
            "advanced", "essential", 70,
            "The GIL lets one bytecode thread run at a time. asyncio is for waiting on sockets, not for crunching numbers.",
            code='''import asyncio

async def fetch_fake(n: int) -> int:
    await asyncio.sleep(0.01)
    return n

async def main() -> None:
    print(await asyncio.gather(fetch_fake(1), fetch_fake(2)))

asyncio.run(main())''',
            out="[1, 2] after both sleeps overlap.",
            when="Use asyncio for outbound HTTP. Use a process pool for CPU-heavy PDF parsing. Use a queue worker for work that should survive a request.",
            refs=["[asyncio](https://docs.python.org/3/library/asyncio.html)"],
            nxt="#py-perf",
        ),
        lesson(
            "py-perf",
            "Memory, profiling, common slow spots",
            "advanced", "advanced", 40,
            "Profile before rewriting. list.append in a loop is fine; concatenating huge strings in a loop is not.",
            refs=["[profile](https://docs.python.org/3/library/profile.html)"],
            nxt="#dsa-big-o",
        ),
    ]),
]
