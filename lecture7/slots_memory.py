"""Memory used by 100,000 poses, with and without __slots__."""

import tracemalloc
from dataclasses import dataclass


class Pose:
    def __init__(self, x: float, y: float, theta: float):
        self.x, self.y, self.theta = x, y, theta


class SlotPose:
    __slots__ = ("theta", "x", "y")

    def __init__(self, x: float, y: float, theta: float):
        self.x, self.y, self.theta = x, y, theta


@dataclass(slots=True)
class DataPose:
    x: float
    y: float
    theta: float


def bytes_per_pose(cls, ask_dict=False, n=100_000):
    """Bytes allocated per object (list included) to make n of them."""
    tracemalloc.start()
    poses = [cls(1.0, 2.0, 0.5) for _ in range(n)]
    if ask_dict:
        for pose in poses:
            vars(pose)  # Asks each object for its __dict__
    used, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    del poses
    return used / n


runs = [(Pose, False), (Pose, True), (SlotPose, False)]
runs.append((DataPose, False))
for cls, ask_dict in runs:
    # The smallest of 5 runs
    best = min(bytes_per_pose(cls, ask_dict) for _ in range(5))
    label = cls.__name__ + (" + vars()" if ask_dict else "")
    print(f"{label:16} {best:6.1f} bytes per pose")
print(DataPose.__slots__)
