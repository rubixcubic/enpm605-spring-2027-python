"""Arguments: positional, keyword, default, *args, **kwargs, and unpacking."""


def drive_time(distance_m, speed_mps):
    return distance_m / speed_mps


# Positional arguments are matched by order
print(drive_time(3.0, 0.25))
print(drive_time(0.25, 3.0))  # Swapped: no error, wrong answer

# Keyword arguments are matched by name
print(drive_time(speed_mps=0.25, distance_m=3.0))
print(drive_time(3.0, speed_mps=0.25))


# A default value makes an argument optional
def drive_time_at(distance_m, speed_mps=0.2):  # 0.2: chosen
    return distance_m / speed_mps


print(drive_time_at(3.0))
print(drive_time_at(3.0, 0.25))


# None as the default: a new list at each call
def log_reading(r, history=None):
    if history is None:
        history = []
    history.append(r)
    return history


a = log_reading(2.5)
b = log_reading(0.9)
print(a, b, a is b)


# *args collects extra positional arguments in a tuple
def mean_of(*readings):
    print(type(readings).__name__, readings)
    return sum(readings) / len(readings)


print(f"{mean_of(2.5, 0.9, 3.1):.2f}")
print(mean_of(1.2))


# **kwargs collects extra keyword arguments in a dictionary
def make_robot(name, **settings):
    print(type(settings).__name__, settings)
    settings["name"] = name
    return settings


print(make_robot("waffle_01", max_speed_mps=0.26, lidar=True))


# Parameters after * are keyword-only
def move(distance_m, *, speed_mps=0.2):
    return f"move {distance_m} m at {speed_mps} m/s"


print(move(1.5, speed_mps=0.1))


# Every kind of parameter, in the order Python requires
def show(a, b, *args, option=True, **kwargs):
    print(f"{a=}, {b=}, {args=}, {option=}, {kwargs=}")


show(1, 2, 3, 4, option=False, x=10)

# * and ** unpack a sequence and a dictionary into arguments
leg = (3.0, 0.25)
print(drive_time(*leg))
config = {"distance_m": 3.0, "speed_mps": 0.25}
print(drive_time(**config))
