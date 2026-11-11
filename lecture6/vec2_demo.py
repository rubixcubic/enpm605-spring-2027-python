"""+, *, and abs() for a 2D vector class."""

import math


class Vec2:
    """A 2D vector, in meters."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vec2({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vec2):
            return NotImplemented
        return Vec2(self.x + other.x, self.y + other.y)

    def __mul__(self, k):
        if not isinstance(k, (int, float)):
            return NotImplemented
        return Vec2(self.x * k, self.y * k)

    def __rmul__(self, k):
        return self.__mul__(k)

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)


# Positions and steps in meters, chosen for this example
start = Vec2(1.0, 2.0)
step = Vec2(0.5, 0.0)
print(start + step, step * 4, 4 * step)
print(start + 4 * step, abs(Vec2(3.0, 4.0)))
print(start + 3)  # No rule for Vec2 + int: TypeError
