"""Shape, data type, indexing, slicing, and reshape."""

import numpy as np

# Poses of a robot: one row per pose; columns x (m), y (m), theta (rad).
# Chosen for this example.
# fmt: off
poses = np.array([
    [0.0, 0.0, 0.00],
    [1.0, 0.0, 0.00],
    [2.0, 0.5, 0.46],
    [2.5, 1.5, 1.11],
])
# fmt: on
print(poses.ndim, poses.shape, poses.size)
print(poses.dtype, poses.itemsize, poses.nbytes)

# Indexing: [row, column]
print(poses[2, 0])  # Row 2, column 0
print(poses[-1])  # The last row
print(poses[:, 0])  # Column 0: every x
print(poses[1:3, :2])

# Slicing a 1D array works as for a list
ranges = np.array([2.5, 0.9, 3.1, 1.2, 0.4, 2.2])
print(ranges[1:4], ranges[::2])
print(ranges[::-1])

# A slice of a list is a copy; a slice of an array is a view
ranges_list = [2.5, 0.9, 3.1]
part = ranges_list[0:2]
part[0] = 99.0
print(ranges_list)
part = ranges[0:2]
part[0] = 99.0
print(ranges)
print(part.base is ranges)
safe = ranges[2:4].copy()
safe[0] = -1.0
print(ranges[2], safe.base is None)

# reshape gives the same numbers a new shape
xy = np.array([0.0, 0.0, 1.0, 0.0, 2.0, 0.5])
pairs = xy.reshape(3, 2)
print(pairs)
print(xy.reshape(-1, 2).shape, pairs.base is xy)
