"""A synthetic laser scan, with the fields of a ROS 2 LaserScan message.

The field names and their meaning come from sensor_msgs/msg/LaserScan.msg
in ROS 2 Jazzy: angles are measured counterclockwise from the robot's x
axis (straight ahead), and "values < range_min or > range_max should be
discarded". As in rclpy, ranges is an array.array of float32 ('f').

The scan is made up for Lecture 5 (synthetic, seeded): every value below
is chosen for the lecture. The robot stands in a rectangular room and
measures the distance to the walls and to a round pillar. Rays that leave
through a doorway get no return, +inf (ROS REP 117: "out of range
detections will be represented by +Inf"). A few readings, picked at
random, are erroneous: NaN (REP 117: "Erroneous detections shall be
represented by quiet (non-signaling) NaNs").
"""

import array
from types import SimpleNamespace

import numpy as np
from geometry import rot

ROOM_W_M, ROOM_H_M = 8.0, 6.0  # Walls at x = 0, x = 8, y = 0, y = 6
DOOR_X_M = (5.0, 6.0)  # A doorway in the wall y = 6
PILLAR_XY_M = np.array([4.5, 2.0])  # A round pillar: center ...
PILLAR_R_M = 0.3  # ... and radius
POSE = (2.0, 1.0, np.radians(30.0))  # Robot x (m), y (m), heading (rad)
NOISE_M = 0.01  # Standard deviation of the noise on each range
N_ERRORS = 3  # Number of NaN readings
N_RAYS = 360


def wall_distance(origin, directions):
    """Distance along each unit direction to the first wall of the room."""
    x0, y0 = origin
    dx, dy = directions[:, 0], directions[:, 1]
    with np.errstate(divide="ignore", invalid="ignore"):
        tx = np.where(dx > 0, (ROOM_W_M - x0) / dx, -x0 / dx)
        ty = np.where(dy > 0, (ROOM_H_M - y0) / dy, -y0 / dy)
    tx = np.where(dx == 0, np.inf, tx)
    ty = np.where(dy == 0, np.inf, ty)
    t = np.minimum(tx, ty)
    # A ray that reaches the wall y = 6 inside the doorway has no return
    hit_x = x0 + ty * dx
    through_door = (ty < tx) & (dy > 0)
    through_door &= (hit_x > DOOR_X_M[0]) & (hit_x < DOOR_X_M[1])
    return np.where(through_door, np.inf, t)


def pillar_distance(origin, directions):
    """Distance along each unit direction to the pillar, or inf."""
    f = np.asarray(origin) - PILLAR_XY_M
    b = directions @ f
    c = f @ f - PILLAR_R_M**2
    disc = b**2 - c
    t = -b - np.sqrt(np.maximum(disc, 0.0))
    return np.where((disc >= 0) & (t > 0), t, np.inf)


def make_scan(seed=605):
    """Return a scan with the fields of a LaserScan message."""
    rng = np.random.default_rng(seed)
    angle_min = -np.pi
    angle_increment = 2 * np.pi / N_RAYS
    angles = angle_min + np.arange(N_RAYS) * angle_increment
    x0, y0, theta = POSE
    # The direction of each ray in the room: robot frame, rotated
    directions = np.column_stack([np.cos(angles), np.sin(angles)])
    directions = directions @ rot(theta).T
    r = np.minimum(
        wall_distance((x0, y0), directions),
        pillar_distance((x0, y0), directions),
    )
    r = r + rng.normal(0.0, NOISE_M, N_RAYS)  # inf + noise stays inf
    r[rng.choice(N_RAYS, N_ERRORS, replace=False)] = np.nan
    return SimpleNamespace(
        angle_min=float(angle_min),
        angle_max=float(angles[-1]),
        angle_increment=float(angle_increment),
        range_min=0.12,  # The lidar of Lecture 2
        range_max=12.0,
        ranges=array.array("f", r),
    )
