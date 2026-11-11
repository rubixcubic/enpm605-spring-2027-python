"""Docstrings: help() prints a function's signature and docstring."""


def drive_time(distance_m, speed_mps):
    """Return the time to drive a distance at a constant speed.

    Args:
        distance_m: The distance to drive, in meters.
        speed_mps: The speed, in meters per second. Must not be 0.

    Returns:
        The time, in seconds.
    """
    return distance_m / speed_mps


help(drive_time)
