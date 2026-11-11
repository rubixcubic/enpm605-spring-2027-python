"""The @ line applies a decorator when def runs."""


def log_calls(func):
    print(f"Decorating {func.__name__}")

    def wrapper(distance_m, speed_mps):
        print(f"Calling {func.__name__}{(distance_m, speed_mps)}")
        result = func(distance_m, speed_mps)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


@log_calls  # The same as drive_time = log_calls(drive_time)
def drive_time(distance_m, speed_mps):
    """Seconds to drive distance_m at speed_mps (Lecture 4)."""
    return distance_m / speed_mps


print("Before the first call")
print(drive_time(9.0, 1.5))  # Values chosen for this example
print(drive_time.__name__, drive_time.__doc__)
