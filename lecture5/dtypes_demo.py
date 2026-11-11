"""Data types: float64, float32, and uint8."""

import numpy as np

# A LaserScan's ranges are float32: 4 bytes, less precise
r32 = np.array([0.1, 2.5], dtype=np.float32)
print(r32.dtype, r32.itemsize)
print(r32[0], float(r32[0]))
r64 = r32.astype(np.float64)  # A converted copy
print(r64.dtype, r64[0])

# 8-bit pixel values: uint8 holds 0 to 255, and a sum wraps around
pixels = np.array([200, 250], dtype=np.uint8)
print(pixels + 100)
print(pixels.astype(np.int64) + 100)
