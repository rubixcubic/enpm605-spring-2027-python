"""Defining and calling functions: def, return, None, and function objects."""


# Lecture 3, Exercise 1, task 5, as a function
def first_obstacle(scan):
    """Index of the first valid reading under 0.5 m."""
    for i, r in enumerate(scan):
        if not (0.12 <= r <= 12.0):
            continue
        if r < 0.5:
            return i
    return None


print(first_obstacle([2.5, 0.0, 1.1, 0.4, 13.5, 0.8]))
print(first_obstacle([2.5, 0.0, 13.5, 0.8]))


# The parts of a function
def drive_time(distance_m, speed_mps):
    """Return the time in seconds to drive distance_m at speed_mps."""
    time_s = distance_m / speed_mps
    return time_s


t = drive_time(3.0, 0.25)  # Values chosen for this example
print(t)


# A function without return returns None
def report(scan):
    print(f"{len(scan)} readings")


result = report([2.5, 0.9])
print(result)


# return gives back one object; several values travel as a tuple
def nearest_and_farthest(scan):
    """Return the smallest and the largest reading of scan."""
    return min(scan), max(scan)


pair = nearest_and_farthest([2.5, 0.9, 3.1])
print(pair, type(pair).__name__)
nearest, farthest = nearest_and_farthest([2.5, 0.9, 3.1])
print(f"nearest {nearest} m, farthest {farthest} m")


# A function is an object, and def binds a name to it
print(type(drive_time).__name__, drive_time.__name__)
go = drive_time
print(go is drive_time, go(1.0, 0.5))
print(drive_time.__doc__)
