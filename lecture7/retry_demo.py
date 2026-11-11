"""A decorator with an argument: retry(times) makes the decorator."""

import functools


def retry(times):
    """Make a decorator that tries the function up to times times."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except TimeoutError as err:
                    print(f"Attempt {attempt} failed: {err}")
            raise TimeoutError(f"{func.__name__} failed {times} times")

        return wrapper

    return decorator


replies = iter([None, None, 2.5])  # Two timeouts, then 2.5 m (chosen)


@retry(times=3)
def read_lidar() -> float:
    """Read one range from the lidar, in meters."""
    reply = next(replies)
    if reply is None:
        raise TimeoutError("no reply from the lidar")
    return reply


print(read_lidar())
