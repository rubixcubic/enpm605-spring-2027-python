"""== and < for Sensor objects: __eq__ and __lt__."""


class Sensor:
    """A range sensor: its kind and its range in meters."""

    def __init__(self, kind: str, range_m: float):
        self.kind = kind
        self.range_m = range_m

    def __repr__(self) -> str:
        return f"Sensor({self.kind!r}, {self.range_m})"

    def __eq__(self, other):
        if not isinstance(other, Sensor):
            return NotImplemented
        return self.kind == other.kind and self.range_m == other.range_m

    def __lt__(self, other):
        if not isinstance(other, Sensor):
            return NotImplemented
        return self.range_m < other.range_m


# Ranges in meters, chosen for this example
lidar = Sensor("lidar", 12.0)
print(lidar == Sensor("lidar", 12.0), lidar is Sensor("lidar", 12.0))
print(lidar == "lidar", lidar != Sensor("sonar", 4.0))

sensors = [lidar, Sensor("sonar", 4.0), Sensor("camera", 10.0)]
print(sorted(sensors))
print(min(sensors), lidar > Sensor("camera", 10.0))
