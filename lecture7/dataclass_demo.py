"""@dataclass writes __init__, __repr__, and __eq__ from the fields."""

import inspect
from dataclasses import dataclass


@dataclass
class Task:
    """A competition task; rule 2 is not checked yet."""

    name: str
    priority: str
    minutes: int


pick = Task("pick widget", "high", 5)  # Values chosen for this example
print(pick)
print(pick == Task("pick widget", "high", 5), pick.minutes)
print(inspect.signature(Task))
pick.minutes = 7  # Fields are plain attributes
print(pick, Task.__hash__)
