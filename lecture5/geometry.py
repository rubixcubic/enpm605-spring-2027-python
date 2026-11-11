"""2D rotation matrices and homogeneous transforms."""

import numpy as np


def rot(theta):
    """Return the 2x2 matrix that rotates a vector by theta (rad)."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])


def transform(x, y, theta):
    """Return the transform of a frame at (x, y), turned by theta."""
    T = np.eye(3)
    T[:2, :2] = rot(theta)
    T[:2, 2] = [x, y]
    return T
