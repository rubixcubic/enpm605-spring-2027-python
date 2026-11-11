"""raise stops __init__ when it gets a battery level out of range."""


class Robot:
    """A robot in the competition."""

    def __init__(self, name: str, battery: int = 100):
        if not 0 <= battery <= 100:
            raise ValueError(f"battery must be 0 to 100, got {battery}")
        self.name = name
        self.battery = battery


scout = Robot("Scout", 80)
print(scout.name, scout.battery)
hauler = Robot("Hauler", 150)
print("This line does not run")
