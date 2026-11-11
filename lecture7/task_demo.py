"""The competition's Task: checked by __post_init__, and frozen."""

from robotics_competition.task import Task

pick = Task("pick widget", "high", 5)  # Values chosen for this example
print(pick, pick.points)
for args in [("dance", "urgent", 1), ("lift", "low", 2.5)]:
    try:
        Task(*args)
    except (ValueError, TypeError) as err:
        print(type(err).__name__, err)
try:
    pick.minutes = 7
except AttributeError as err:
    print(type(err).__name__, err)
done = {pick, Task("pick widget", "high", 5)}  # A set needs __hash__
print(len(done), hash(pick) == hash(Task("pick widget", "high", 5)))
