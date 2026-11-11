"""A wrapper with *args and **kwargs, and functools.wraps."""

import functools


def log_calls(func):
    @functools.wraps(func)  # Copies __name__, __doc__, ... from func
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@log_calls
def drive_time(distance_m, speed_mps):
    """Seconds to drive distance_m at speed_mps (Lecture 4)."""
    return distance_m / speed_mps


@log_calls
def recharge_time(battery, pct_per_min=5):
    """Minutes to fill the battery; 5% per minute is an example rate."""
    return (100 - battery) / pct_per_min


print(drive_time(12.0, speed_mps=1.5))
print(recharge_time(40))
print(drive_time.__name__, "|", drive_time.__doc__)
