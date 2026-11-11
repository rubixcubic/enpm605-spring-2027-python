"""__str__ sets the text print() shows; a list still shows the default."""


class Robot:
    """A robot in the competition."""

    def __init__(self, name: str, battery: int = 100):
        self.name = name
        self.battery = battery

    def __str__(self) -> str:
        return f"{self.name} ({self.battery}%)"


scout = Robot("Scout", 80)
print(scout)
print(str(scout), f"Robot: {scout}")
print([scout])
