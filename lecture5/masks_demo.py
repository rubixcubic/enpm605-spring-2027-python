"""Boolean masks: select the readings that pass a test."""

import numpy as np

ranges = np.array([2.5, 0.9, 3.1, 0.4, 14.0, 0.7])  # Chosen
close = ranges < 1.0
print(close)
print(ranges[close])
print(close.sum(), np.flatnonzero(close))

# Combine tests with & (and), | (or), and ~ (not), in parentheses
valid = (ranges >= 0.12) & (ranges <= 12.0)
print(valid)
print(ranges[valid & ~close])
print(ranges[(ranges < 0.5) | (ranges > 12.0)])

# Assign through a mask, in a copy
capped = ranges.copy()
capped[~valid] = 12.0
print(capped)
print(np.where(valid, ranges, np.nan))

# An array of positions also selects items: here, the 3 nearest
order = np.argsort(ranges)
print(order)
print(ranges[order[:3]])
