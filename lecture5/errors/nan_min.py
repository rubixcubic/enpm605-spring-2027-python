import numpy as np

ranges = np.array([2.5, np.nan, 0.9, 3.1])
print(ranges.min(), ranges.argmin())
print(min([2.5, np.nan, 0.9]), min([np.nan, 2.5, 0.9]))
