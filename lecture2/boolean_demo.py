"""The bool type and truth value testing."""

# bool is a kind of int
print(True + True)
print(isinstance(True, int))
print(int(False))

# Falsy values
print(bool(0), bool(0.0), bool(""), bool([]), bool({}), bool(None))

# Truthy values
print(bool(1), bool(-2), bool("hi"), bool([0]), bool(" "), bool(0.001))
print(bool("False"))  # A non-empty string

# A position of 0.0 m is a value, not a missing one
goal_x_m = 0.0  # The goal is at the origin
if not goal_x_m:
    print("not goal_x_m: no goal set (wrong)")
if goal_x_m is None:
    print("No goal set")
else:
    print(f"Goal: x = {goal_x_m} m")
