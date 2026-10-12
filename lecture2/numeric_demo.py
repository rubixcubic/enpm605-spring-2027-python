"""int, float, and complex: conversions, rounding, and precision."""

import math

count = 42
ratio = 3.14
impedance = 2 + 1j
print(type(count), type(ratio), type(impedance))
print(2**100)  # An int has no fixed size

# Conversions
print(int(3.7), int(-3.7))
print(int("42"), int("101011", 2))
print(float("3.5"), float(3), float("inf"))
print(round(2.5), round(3.5), round(2.567, 2))

# Floats are approximate
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)

# Compare floats with a tolerance
goal_x_m = 0.3
x_m = 0.1 + 0.2  # Two moves: 0.1 m, then 0.2 m
print(x_m == goal_x_m)
print(math.isclose(x_m, goal_x_m))
print(abs(x_m - goal_x_m) < 0.01)  # 0.01 m, chosen for this example
print(math.isclose(1e-12, 0.0))
print(math.isclose(1e-12, 0.0, abs_tol=1e-9))

# Small integers are shared objects in CPython
a = 256
b = int("256")
print(a is b)
c = 257
d = int("257")
print(c is d, c == d)
