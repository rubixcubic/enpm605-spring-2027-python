"""__slots__ lists the only attribute names an object can have."""


class Pose:
    __slots__ = ("theta", "x", "y")

    def __init__(self, x: float, y: float, theta: float = 0.0):
        self.x = x  # Meters
        self.y = y
        self.theta = theta  # Radians


p = Pose(1.0, 2.0)  # Values chosen for this example
p.x = 1.5  # A listed name: allowed
try:
    p.thetta = 0.5  # Misspelled
except AttributeError as err:
    print("AttributeError", err)
print(p.x, p.theta, hasattr(p, "__dict__"))
