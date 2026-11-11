"""Scopes: local, enclosing, global, and built-in names (LEGB)."""

speed_mps = 0.2  # A global name (chosen for this example)


def drive_time(distance_m):
    time_s = distance_m / speed_mps  # time_s is local
    print(locals())
    return time_s


print(drive_time(3.0))
print("time_s" in globals(), "speed_mps" in globals())

# LEGB: each name below is found in a different scope
robot = "waffle_01"  # G: assigned at the top of the file


def outer():
    sensor = "lidar"  # E, for inner: assigned in outer

    def inner():
        reading = 2.5  # L: assigned in inner
        print(reading, sensor, robot, max(reading, 1.0))  # max: B

    inner()


outer()

# The same name in three scopes: three different names
label = "global"


def outer2():
    label = "enclosing"

    def inner2():
        label = "local"
        print("inner2:", label)

    inner2()
    print("outer2:", label)


outer2()
print("module:", label)

# global: assign to the module's name
scans_seen = 0


def on_scan(scan):
    global scans_seen
    scans_seen += 1
    print(f"Scan {scans_seen}: nearest {min(scan)} m")


on_scan([2.5, 0.9])
on_scan([0.4])
print(scans_seen)

# Changing a global list needs no global statement
history = []


def log_reading(r):
    history.append(r)


log_reading(2.5)
log_reading(0.9)
print(history)


# nonlocal: assign to a name of the enclosing function
def process(scans):
    count = 0

    def on_scan(scan):
        nonlocal count
        count += 1
        print(f"Scan {count}: nearest {min(scan)} m")

    for scan in scans:
        on_scan(scan)
    return count


print(process([[2.5, 0.9], [0.4], [1.0, 1.1, 1.2]]))
