class Sensor:
    def __init__(self, kind: str, range_m: float):
        self.kind = kind
        self.range_m = range_m

    def __eq__(self, other):
        if not isinstance(other, Sensor):
            return NotImplemented
        return self.kind == other.kind and self.range_m == other.range_m


print(Sensor.__hash__)
mounted = {Sensor("lidar", 12.0)}
