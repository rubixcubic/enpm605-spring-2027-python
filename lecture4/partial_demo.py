"""functools.partial: a new callable with some arguments filled in."""

from functools import partial


def in_range(r: float, min_m: float, max_m: float) -> bool:
    return min_m <= r <= max_m


lidar_ok = partial(in_range, min_m=0.12, max_m=12.0)
print(lidar_ok(5.0), lidar_ok(14.0))
print(type(lidar_ok).__name__)
print(lidar_ok.func.__name__, lidar_ok.args, lidar_ok.keywords)


def drive_time(distance_m: float, speed_mps: float) -> float:
    return distance_m / speed_mps


one_meter = partial(drive_time, 1.0)  # Fills distance_m, the first
print(one_meter(0.25), one_meter.args)


# A closure that fills in speed_mps
def make_driver(speed_mps):
    def drive(distance_m):
        return drive_time(distance_m, speed_mps)

    return drive


# Three ways to fill in an argument
fillers = [
    partial(drive_time, speed_mps=0.25),
    lambda d: drive_time(d, 0.25),
    make_driver(0.25),
]
print([f(3.0) for f in fillers])
