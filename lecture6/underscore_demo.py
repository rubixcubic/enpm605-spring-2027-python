"""A leading underscore marks an attribute as non-public."""


class Robot:
    """A robot in the competition."""

    def __init__(self, name: str, battery: int = 100):
        self._name = name  # Non-public: use the methods
        self._battery = battery

    def report(self) -> str:
        return f"{self._name}: {self._battery}%"


scout = Robot("Scout")
print(scout.report())
scout._battery = 5  # Python allows it; Ruff's SLF001 reports it
print(scout.report())
