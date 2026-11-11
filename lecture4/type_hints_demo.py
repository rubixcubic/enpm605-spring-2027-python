"""Type hints: annotations for parameters and return values."""


def drive_time(distance_m: float, speed_mps: float) -> float:
    return distance_m / speed_mps


print(drive_time(3.0, 0.25))
for name, hint in drive_time.__annotations__.items():
    print(name, hint)


# Python does not check the hints when it runs the code
def repeat_label(label: str, count: int) -> str:
    return label * count


print(repeat_label("ab", 3))
print(repeat_label(2.5, 2))  # Not a str, and it runs


# Hints for collections, and for a value that can be None
def nearest(scan: list[float]) -> float:
    return min(scan)


def pose() -> tuple[float, float, float]:
    return 1.5, -0.3, 90.0


def limits() -> dict[str, float]:
    return {"min_m": 0.12, "max_m": 12.0}


def find_sensor(names: list[str], wanted: str) -> int | None:
    for i, name in enumerate(names):
        if name == wanted:
            return i
    return None


print(nearest([2.5, 0.9]), pose(), limits())
print(find_sensor(["lidar", "imu"], "imu"))
print(find_sensor(["lidar", "imu"], "gps"))
