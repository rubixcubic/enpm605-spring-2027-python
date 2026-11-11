"""NumPy arrays versus Python lists."""

import numpy as np

# The same computation with a list and with an array
ranges_list = [2.5, 0.9, 3.1, 1.2]  # Meters, chosen for this example
print([r * 100 for r in ranges_list])  # To centimeters
ranges = np.array(ranges_list)
print(ranges * 100)

# + and * mean different things for a list and for an array
print(ranges_list + ranges_list)
print(ranges + ranges)
print(ranges_list * 2)
print(ranges * 2)

# Ways to make an array
print(np.zeros(3), np.ones(2))
print(np.full(3, np.inf))
print(np.arange(0.0, 1.0, 0.25))
print(np.linspace(0.0, 1.0, 5))

# One data type for every item
print(np.array([1, 2, 3]).dtype)
print(np.array([1, 2.5, 3]).dtype)
print(repr(np.array([1, 2.5, "lidar"])))

# An array holds the numbers themselves, 8 bytes each
a = np.arange(1_000_000, dtype=np.float64)
print(a.nbytes, a.itemsize)
print(type(a).__name__, type(a[0]).__name__)
