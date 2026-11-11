"""Instance attributes, a class attribute, and where Python finds each."""


class Robot:
    """A robot in the competition."""

    total_robots = 0  # A class attribute: one value, shared

    def __init__(self, name: str, battery: int = 100):
        self.name = name  # Instance attributes: one per object
        self.battery = battery
        Robot.total_robots += 1


scout = Robot("Scout")
hauler = Robot("Hauler", 60)
print(vars(scout))
print(vars(hauler))
print(Robot.total_robots, scout.total_robots)
print("total_robots" in vars(scout), "total_robots" in vars(Robot))

# Assigning through an object makes an instance attribute
scout.total_robots = 99
print(scout.total_robots, hauler.total_robots, Robot.total_robots)
print(vars(scout))

# A misspelled name in an assignment makes one more attribute
hauler.batery = 50
print(hauler.battery, vars(hauler))
