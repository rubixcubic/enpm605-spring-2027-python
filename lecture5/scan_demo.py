"""A laser scan as an array: invalid readings, nearest obstacle."""

import numpy as np
from geometry import rot
from scan_data import POSE, make_scan

scan = make_scan()  # Synthetic, with the fields of a LaserScan message
ranges = np.asarray(scan.ranges)
print(type(scan.ranges).__name__, ranges.dtype, ranges.shape)

# The angle of each reading, in the robot's frame
angles = scan.angle_min + np.arange(ranges.size) * scan.angle_increment
print(np.degrees(angles[[0, 1, 180, 359]]))

# min() of an array with a NaN is NaN
print(ranges.min(), ranges.argmin())

# The invalid readings, by kind
print(np.isnan(ranges).sum(), np.isposinf(ranges).sum())
valid = (ranges >= scan.range_min) & (ranges <= scan.range_max)
print(valid.sum(), "valid of", ranges.size)

# The nearest valid reading: invalid ones become inf, then argmin
i = np.where(valid, ranges, np.inf).argmin()
deg = np.degrees(angles[i])
print(f"nearest: index {i}, {ranges[i]:.3f} m at {deg:.0f} deg")

# Only the front: within 30 degrees of straight ahead
front = valid & (np.abs(angles) <= np.radians(30))
j = np.where(front, ranges, np.inf).argmin()
deg = np.degrees(angles[j])
print(f"front: index {j}, {ranges[j]:.3f} m at {deg:.0f} deg")

# Each valid reading as a point (x, y) in the robot's frame
x = ranges[valid] * np.cos(angles[valid])
y = ranges[valid] * np.sin(angles[valid])
points = np.column_stack([x, y])
print(points.shape, points.dtype)

# The nearest point, in the world frame: on the wall y = 0?
x0, y0, theta = POSE
p = ranges[i] * np.array([np.cos(angles[i]), np.sin(angles[i])])
print(np.round(rot(theta) @ p + [x0, y0], 3))
