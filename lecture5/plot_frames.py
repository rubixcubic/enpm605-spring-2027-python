"""Plot the world frame, the robot's frame, and one point in both."""

import matplotlib.pyplot as plt
import numpy as np
from geometry import rot
from plots import BLUE, BLUE_TEXT, GRAY, ORANGE, save, tag

pose = (2.0, 1.0, np.radians(30))  # As in transforms_demo.py
t = np.array(pose[:2])
R = rot(pose[2])
p_world = R @ [1.5, 0.0] + t  # 1.5 m straight ahead of the robot


def arrow(ax, start, vec, color, style="-"):
    ax.annotate(
        "",
        start + vec,
        start,
        arrowprops={"arrowstyle": "-|>", "color": color, "lw": 1.5, "ls": style},
    )


plt.rcParams["font.size"] = 9
fig, ax = plt.subplots(figsize=(3.6, 2.5), layout="constrained")
o = np.zeros(2)
arrow(ax, o, np.array([1.0, 0.0]), "black")  # World x
arrow(ax, o, np.array([0.0, 1.0]), "black")  # World y
arrow(ax, o, t, GRAY, "--")  # t: from the world origin to the robot
arrow(ax, t, R @ [1.0, 0.0], BLUE)  # Robot x: straight ahead
arrow(ax, t, R @ [0.0, 1.0], BLUE)  # Robot y: to its left
ax.plot(*p_world, "o", color=ORANGE, markersize=6)
for pos, s in [((1.08, -0.1), "x"), ((-0.15, 1.05), "y")]:
    ax.text(*pos, s)
for vec, s in [(R @ [1.12, 0.0], "x"), (R @ [0.0, 1.15], "y")]:
    ax.text(*(t + vec), s, color=BLUE_TEXT, ha="center", va="center")
tag(ax, -0.25, -0.25, 1)
tag(ax, 0.9, 0.7, 2)
tag(ax, t[0] + 0.15, t[1] - 0.3, 3)
tag(ax, p_world[0] + 0.3, p_world[1] - 0.15, 4)
ax.set_xlim(-0.5, 4.0)
ax.set_ylim(-0.5, 2.5)
ax.set_xlabel("x, world frame (m)")
ax.set_ylabel("y, world frame (m)")
ax.set_aspect("equal")
ax.grid(alpha=0.3)
print(np.round(p_world, 3))
save(fig, "frames")
