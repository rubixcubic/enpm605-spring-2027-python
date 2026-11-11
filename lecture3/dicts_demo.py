"""Dictionaries: keys and values, lookups, views, loops, and comprehensions."""

from collections import Counter
from pprint import pp

# Keys and values (chosen for this example)
robot = {
    "name": "waffle_01",
    "max_speed_mps": 0.26,
    "sensors": ["lidar"],
}
print(robot["name"], robot["max_speed_mps"])
print(len(robot))
print(robot)

# Ways to create a dictionary
a = {"x": 1.0, "y": 2.0}
pairs = [("x", 1.0), ("y", 2.0)]
b = dict(pairs)
keys = ["x", "y"]
values = [1.0, 2.0]
c = dict(zip(keys, values))
print(a == b == c, a)
print({}, type({}))

# A missing key: get() and in
robot = {"name": "waffle_01", "max_speed_mps": 0.26}
print(robot.get("battery_pct"))
print(robot.get("battery_pct", 100))
print("battery_pct" in robot, "name" in robot)

# Adding, changing, and removing entries
robot["battery_pct"] = 87  # A new key: added at the end
robot["max_speed_mps"] = 0.2  # An existing key: value replaced
print(robot)
robot.update({"mode": "map", "battery_pct": 80})
print(robot["mode"], robot["battery_pct"])
speed = robot.pop("max_speed_mps")
del robot["mode"]
print(speed, robot)

# Keys must be hashable: a grid cell (row, col) as the key
costs = {(0, 0): 1.0, (0, 1): 5.0}
print(costs[(0, 1)], costs[0, 1])

# Views
robot = {"name": "waffle_01", "battery_pct": 87}
keys = robot.keys()
print(keys)
robot["mode"] = "explore"
print(keys)
print(list(robot.values()))
print(list(robot.items()))

# Looping over a dictionary
for key in robot:
    print(key)
for key, value in robot.items():
    print(f"{key:>11}: {value}")

# Removing entries while looping: loop over a copy of the keys
battery = {"robot1": 87, "robot2": 15, "robot3": 42}
for name in list(battery):
    if battery[name] < 20:
        del battery[name]
print(battery)

# Dictionary comprehensions
sensors = ["lidar", "camera", "imu"]
sensor_ids = {name: i for i, name in enumerate(sensors)}
battery = {"robot1": 87, "robot2": 15, "robot3": 42}
ok = {name: pct for name, pct in battery.items() if pct >= 20}
by_id = {i: name for name, i in sensor_ids.items()}
print(sensor_ids)
print(ok)
print(by_id)

# Counting with a dictionary (the log of Lecture 2, Exercise 4)
status_log = "IDLE:MOVING:CHARGING:MOVING:IDLE"
counts = {}
for state in status_log.split(":"):
    counts[state] = counts.get(state, 0) + 1
print(counts)
print(Counter(status_log.split(":")))

# Nested dictionaries
robot = {
    "name": "waffle_01",
    "lidar": {"range_max_m": 12.0, "rate_hz": 5},
    "camera": {"fps": 30, "width_px": 640},
}
print(robot["lidar"]["range_max_m"])
pp(robot, width=40)
