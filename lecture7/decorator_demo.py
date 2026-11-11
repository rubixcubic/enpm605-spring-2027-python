"""A decorator: a function that takes a function and returns one."""


def log_calls(func):
    print(f"Decorating {func.__name__}")  # Runs once, when applied

    def wrapper(distance_m, speed_mps):
        print(f"Calling {func.__name__}{(distance_m, speed_mps)}")
        result = func(distance_m, speed_mps)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


def drive_time(distance_m, speed_mps):
    """Seconds to drive distance_m at speed_mps (Lecture 4)."""
    return distance_m / speed_mps


drive_time = log_calls(drive_time)  # The name now refers to wrapper
print(drive_time(12.0, 1.5))  # Values chosen for this example
