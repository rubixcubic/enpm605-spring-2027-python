class Sensor:
    def __init__(self, kind: str, range_m: float):
        self.kind = kind
        self.range_m = range_m


lidar = Sensor("lidar", 12.0)
same = lidar  # A second name for the same object
print(lidar == Sensor("lidar", 12.0), lidar == same)
print(sorted([lidar, Sensor("sonar", 4.0)]))
