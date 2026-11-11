"""Vectorized operations: arithmetic, ufuncs, and reductions."""

import numpy as np

# Element by element, with no loop (offsets chosen for this example)
dx = np.array([3.0, 0.5, 1.0])  # m
dy = np.array([4.0, 0.0, 2.0])  # m
print(np.sqrt(dx**2 + dy**2))
print(np.hypot(dx, dy))
print(np.degrees(np.arctan2(dy, dx)))

# Reductions: one number from many
ranges = np.array([2.5, 0.9, 3.1, 1.2])
print(ranges.sum(), ranges.mean(), ranges.min(), ranges.argmin())

# axis: the direction a reduction runs in
# fmt: off
poses = np.array([  # x (m), y (m), theta (rad), as in indexing_demo.py
    [0.0, 0.0, 0.00],
    [1.0, 0.0, 0.00],
    [2.0, 0.5, 0.46],
    [2.5, 1.5, 1.11],
])
# fmt: on
print(poses.mean(axis=0))
print(poses.max(axis=1))

# cumsum: running totals, here of the distances a wheel reports
steps = np.array([0.1, 0.1, 0.2, 0.2])  # m per step, chosen
print(np.cumsum(steps))
print(np.diff(np.cumsum(steps)))
