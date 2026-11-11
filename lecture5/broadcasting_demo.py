"""Broadcasting: operations between arrays of different shapes."""

import numpy as np

# An array and a number: the number is used for every item
ranges = np.array([2.5, 0.9, 3.1])
print(ranges - 0.1)

# A (3, 2) array minus a (2,) array: the row is used for every row
points = np.array([[1.0, 2.0], [3.0, 1.0], [4.0, 4.0]])  # x, y (m)
robot = np.array([1.0, 1.0])  # Chosen for this example
rel = points - robot
print(rel.shape)
print(rel)
print(np.linalg.norm(rel, axis=1))

# A (3, 1) column against a (4,) row gives a (3, 4) table
robots_x = np.array([[0.0], [2.5], [5.5]])  # 3 robots on a line (m)
goals_x = np.array([1.0, 3.0, 4.0, 6.0])  # 4 goals on that line (m)
dist = np.abs(robots_x - goals_x)
print(dist.shape)
print(dist)
print(dist.argmin(axis=1))
