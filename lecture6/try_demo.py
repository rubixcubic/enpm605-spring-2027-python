"""try and except: the program handles the error and goes on."""


class Robot:
    """A robot in the competition."""

    def __init__(self, name: str, battery: int = 100):
        if not 0 <= battery <= 100:
            raise ValueError(f"battery must be 0 to 100, got {battery}")
        self.name = name
        self.battery = battery


for level in [80, 150, 5]:  # Battery levels, chosen for this example
    try:
        robot = Robot("Hauler", level)
        print("Made", robot.name, "with", robot.battery)
    except ValueError as err:
        print("Not made:", err)
print("Done")
