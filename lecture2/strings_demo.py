"""Strings: literals, escapes, f-strings, methods, indexing, slicing."""

# Literals
frame_id = "base_link"
quote = 'He said "stop"'  # Single quotes can hold double quotes
note = """A string
on two lines"""
print(frame_id, len(frame_id))
print(quote)
print(note)
print(str(42) + "%", type(str(42)))

# Escape sequences
print("x:\t1.5\ny:\t2.0")
print("Backslash: \\")
print(r"C:\new\table")  # Raw string: no escapes

# f-strings
robot = "rover"
battery_pct = 87
speed_mps = 0.4567
print(f"{robot}: {battery_pct}% battery")
print(f"Next: {battery_pct - 1}%")
print(f"Speed: {speed_mps:.2f} m/s")
print(f"[{robot:>8}] [{robot:<8}]")
print(f"{battery_pct=}")

# Older formatting you will read in other code
print("%s: %d%% battery" % (robot, battery_pct))  # noqa: UP031
print("{}: {}% battery".format(robot, battery_pct))  # noqa: UP032

# Methods return new strings
topic = "  /robot1/cmd_vel  "
clean = topic.strip()
print(repr(clean))
print(clean.upper())
print(clean.replace("robot1", "robot2"))
print(clean.split("/"))
print(clean.startswith("/"), clean.endswith("vel"))
print(clean.find("cmd"), clean.count("o"))
print(repr(topic))  # Unchanged

# Concatenation, repetition, join
namespace = "robot1"
print("/" + namespace + "/scan")
print("-" * 20)
parts = ["", "robot1", "odom"]
print("/".join(parts))

# Indexing
sensor = "lidar"
print(sensor[0], sensor[4])
print(sensor[-1], sensor[-5])

# Slicing
print(sensor[1:4], sensor[:3], sensor[2:])
print(sensor[:])
print(sensor[-4:-1], sensor[-3:])
print(sensor[::2], sensor[::-1], sensor[4:1:-1])
print(sensor[1:100])
