"""A getter and a setter method that checks every change."""


class Robot:
    """A robot in the competition."""

    def __init__(self, name: str, battery: int = 100):
        self._name = name
        self.set_battery(battery)

    def get_battery(self) -> int:
        return self._battery

    def set_battery(self, value: int) -> None:
        if not 0 <= value <= 100:
            raise ValueError(f"battery must be 0 to 100, got {value}")
        self._battery = value


scout = Robot("Scout")
scout.set_battery(scout.get_battery() - 30)
print(scout.get_battery())
