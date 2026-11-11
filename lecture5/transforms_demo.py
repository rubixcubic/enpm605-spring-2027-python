"""Vectors, rotation matrices, and 2D transforms."""

import numpy as np
from geometry import rot, transform

# The vector from a robot to a goal (positions chosen, in m)
robot = np.array([2.0, 1.0])
goal = np.array([5.0, 5.0])
d = goal - robot
print(d, np.linalg.norm(d))
print(np.degrees(np.arctan2(d[1], d[0])))

# Turn (1, 0) by 90 degrees: (0, 1)
R = rot(np.radians(90))
p = np.array([1.0, 0.0])
print(R @ p)
print(np.round(R @ p, 12))
print(R * p)  # * multiplies item by item: not a rotation

# What makes R a rotation
R30 = rot(np.radians(30))
print(np.round(R30, 3))
print(np.allclose(R30.T @ R30, np.eye(2)))
print(np.allclose(rot(0.2) @ rot(0.3), rot(0.5)))

# From the robot's frame to the world frame
pose = (2.0, 1.0, np.radians(30))  # x (m), y (m), theta: chosen
t = np.array(pose[:2])
p_robot = np.array([1.5, 0.0])  # 1.5 m straight ahead of the robot
p_world = rot(pose[2]) @ p_robot + t
print(np.round(p_world, 3))
print(np.round(rot(pose[2]).T @ (p_world - t), 3))  # And back

# Many points at once: one row per point
pts = np.array([[1.5, 0.0], [0.0, 1.0], [1.0, -1.0]])
print(np.round(pts @ rot(pose[2]).T + t, 3))

# A homogeneous transform: rotation and translation in one matrix
T_world_robot = transform(*pose)
print(np.round(T_world_robot, 3))
print(np.round(T_world_robot @ [1.5, 0.0, 1.0], 3))

# Composing: if the lidar were 0.2 m ahead of the robot's center
T_robot_lidar = transform(0.2, 0.0, 0.0)
T_world_lidar = T_world_robot @ T_robot_lidar
print(np.round(T_world_lidar @ [1.3, 0.0, 1.0], 3))
print(np.round(np.linalg.inv(T_world_robot) @ [3.299, 1.75, 1.0], 3))
