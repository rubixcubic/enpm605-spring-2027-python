"""Every value in Python is an object, and its type is a class."""

import numpy as np

ranges = [2.5, 0.9]  # Meters, chosen for this example
ranges.append(3.1)  # A method of the list object
print(type(ranges), ranges)
kind = "lidar"
print(type(kind), kind.upper())
scan = np.array(ranges)
print(type(scan), scan.shape, scan.max())
print(isinstance(scan, np.ndarray), isinstance(ranges, list))
