"""Plot the scan of scan_data.py: a top view, and range against angle."""

import matplotlib.pyplot as plt
import numpy as np
from plots import BLUE, ORANGE, save, tag
from scan_data import make_scan

scan = make_scan()
ranges = np.asarray(scan.ranges)
angles = scan.angle_min + np.arange(ranges.size) * scan.angle_increment
valid = (ranges >= scan.range_min) & (ranges <= scan.range_max)
i = np.where(valid, ranges, np.inf).argmin()  # The nearest reading
x = ranges * np.cos(angles)  # Robot frame; NaN and inf stay NaN, inf
y = ranges * np.sin(angles)

plt.rcParams["font.size"] = 9

# 1. Top view, in the robot's frame: x straight ahead
fig, ax = plt.subplots(figsize=(3.6, 2.9), layout="constrained")
ax.plot(x[valid], y[valid], ".", color=BLUE, markersize=3)
ax.plot(x[i], y[i], "o", color=ORANGE, markersize=6)
ax.plot(0, 0, ">", color="black", markersize=7)  # The robot, facing +x
ax.set_xlabel("x, robot frame (m)")
ax.set_ylabel("y, robot frame (m)")
ax.set_aspect("equal")
ax.grid(alpha=0.3)
tag(ax, x[i] - 0.6, y[i] - 0.6, 1)
tag(ax, x[171] + 0.1, y[171] - 0.6, 2)
tag(ax, 5.8, 3.2, 3)
tag(ax, 0.0, 0.7, 4)
save(fig, "scan_top")

# 2. Range against angle: a graph, not a map
fig, ax = plt.subplots(figsize=(3.6, 2.4), layout="constrained")
deg = np.degrees(angles)
ax.plot(deg, ranges, color=BLUE, linewidth=1.5)
ax.plot(deg[i], ranges[i], "o", color=ORANGE, markersize=6)
ax.set_xlabel("angle (deg)")
ax.set_ylabel("range (m)")
ax.set_xticks(np.arange(-180, 181, 60))
ax.grid(alpha=0.3)
tag(ax, deg[i], ranges[i] + 0.7, 1)
tag(ax, -9.0, 1.6, 2)
tag(ax, 36.0, 7.0, 3)
save(fig, "scan_graph")
