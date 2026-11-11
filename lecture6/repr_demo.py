"""__repr__ sets the text for developers; str() falls back to it."""


class Robot:
    """A robot in the competition."""

    def __init__(self, name: str, battery: int = 100):
        self.name = name
        self.battery = battery

    def __repr__(self) -> str:
        return f"Robot({self.name!r}, battery={self.battery})"

    def __str__(self) -> str:
        return f"{self.name} ({self.battery}%)"


class Sensor:
    """A range sensor, with __repr__ only."""

    def __init__(self, kind: str, range_m: float):
        self.kind = kind
        self.range_m = range_m

    def __repr__(self) -> str:
        return f"Sensor({self.kind!r}, {self.range_m})"


scout = Robot("Scout", 80)
print(repr(scout))
print([scout, Robot("Hauler")])
print(f"{scout} and {scout!r}")
lidar = Sensor("lidar", 12.0)  # 12.0 m: the lidar of Lecture 2
print(lidar, str(lidar))
