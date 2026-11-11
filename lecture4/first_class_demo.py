"""Functions as values: assign, pass, store, and return functions."""

import math


def to_cm(m: float) -> float:
    return m * 100


# Without parentheses: the function; with them: a call
convert = to_cm
print(convert(2.5), convert is to_cm)
print(type(to_cm).__name__, type(to_cm(2.5)).__name__)

# callable(): can this object be called?
print(callable(to_cm), callable(print), callable(int))
print(callable(2.5), callable("lidar"), callable(None))


# A function that takes a function: a higher-order function
def apply_to_scan(scan: list[float], func) -> list:
    return [func(r) for r in scan]


print(apply_to_scan([2.5, 0.9], to_cm))
print(apply_to_scan([2.5, 0.9], round))

# key=: sorted(), min(), and max() call a function on each item
waypoints = [(3.0, 0.5), (0.5, 0.0), (1.0, 2.0)]  # (x, y), chosen


def distance(p: tuple[float, float]) -> float:
    return math.hypot(p[0], p[1])  # From (0, 0)


print(sorted(waypoints, key=distance))
print(max(waypoints, key=distance))
maxima = {"robot_1": 2.1, "robot_2": 1.5, "robot_3": 1.0}
print(max(maxima, key=maxima.get))  # Lecture 3, Exercise 4


# map() and filter() take a function and an iterable
def is_valid(r: float) -> bool:
    return 0.12 <= r <= 12.0  # The lidar of Lecture 2


scan = [2.5, 0.0, 3.1, 14.0, 1.2]
print(list(filter(is_valid, scan)))
print(list(map(to_cm, filter(is_valid, scan))))
print([to_cm(r) for r in scan if is_valid(r)])


# A dictionary of functions: a dispatch table
def forward(value: float) -> str:
    return f"drive at {value} m/s"


def turn(value: float) -> str:
    return f"turn by {value} deg"


handlers = {"forward": forward, "turn": turn}
for word, value in [("forward", 0.2), ("turn", 90), ("turn", -45)]:
    print(handlers[word](value))


# A function that returns a function
def make_range_check(min_m: float, max_m: float):
    def check(r: float) -> bool:
        return min_m <= r <= max_m

    return check


lidar_ok = make_range_check(0.12, 12.0)  # The lidar of Lecture 2
sonar_ok = make_range_check(0.02, 4.0)  # 4.0: the sonar of Lecture 2
print(lidar_ok(5.0), sonar_ok(5.0))
print(lidar_ok.__name__, lidar_ok is sonar_ok)
