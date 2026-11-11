"""In rclpy, LaserScan.ranges is an array.array of float32.

Needs ROS 2 Jazzy: source /opt/ros/jazzy/setup.bash first (Lecture 8).
"""

import numpy as np
from sensor_msgs.msg import LaserScan

msg = LaserScan()
msg.ranges = [2.5, 0.9, float("inf")]
print(type(msg.ranges).__name__, msg.ranges.typecode)
ranges = np.asarray(msg.ranges)
print(ranges, ranges.dtype)
