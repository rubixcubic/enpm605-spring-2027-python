"""Plot a robot's path and its GPS fixes, seen from above."""

import matplotlib.pyplot as plt
import numpy as np
from plots import BLUE, ORANGE, save, tag

# The path: add up small steps of constant speed (values chosen)
dt = 0.1  # s
t = np.arange(0.0, 15.0, dt)  # 150 times
v = 0.5  # m/s
omega = np.where((t >= 5.0) & (t < 9.0), 0.4, 0.0)  # rad/s
theta = np.cumsum(omega * dt)  # Heading after each step
x = np.cumsum(v * np.cos(theta) * dt)
y = np.cumsum(v * np.sin(theta) * dt)
print(f"end: x = {x[-1]:.2f} m, y = {y[-1]:.2f} m")

# A GPS fix once a second, with noise (synthetic, seeded)
rng = np.random.default_rng(605)
gps = np.column_stack([x[::10], y[::10]])
gps = gps + rng.normal(0.0, 0.15, gps.shape)
print(gps.shape)

plt.rcParams["font.size"] = 9  # Points, at the size the slide shows
fig, ax = plt.subplots(figsize=(3.6, 2.6), layout="constrained")
ax.plot(x, y, color=BLUE, linewidth=2)
ax.plot(gps[:, 0], gps[:, 1], "o", color=ORANGE, markersize=4)
ax.plot(x[0], y[0], "s", color="black", markersize=5)
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_aspect("equal")
ax.grid(alpha=0.3)
tag(ax, x[30], y[30] + 0.45, 1)
tag(ax, gps[13, 0] - 0.5, gps[13, 1], 2)
tag(ax, x[0], y[0] + 0.45, 3)
save(fig, "trajectory")
