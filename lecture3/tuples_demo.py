"""Tuples: creating, indexing, unpacking, and hashing."""

# A pose: x (m), y (m), heading (deg), chosen for this example
pose = (1.5, -0.3, 90)
print(pose[0], pose[-1], pose[:2], len(pose))
print(type(pose))

# The comma makes the tuple
point = 3.0, 4.0
single = (42,)
not_a_tuple = (42)  # fmt: skip
empty = ()
print(type(point), type(single))
print(type(not_a_tuple), type(empty))
print(tuple(range(3)), tuple("xy"))

# Unpacking
x, y, heading = pose
print(x, y, heading)
waypoints = [(0.0, 0.0), (1.0, 0.5), (2.0, 1.5)]
for x, y in waypoints:
    print(f"Go to ({x}, {y})")
first, *rest = waypoints
print(first, rest)
x, y, _ = pose
print(x, y)

# A tuple can hold a mutable object
record = ("lidar", [2.5, 0.9])
record[1].append(3.1)
print(record)
