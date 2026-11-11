import numpy as np

ranges = np.array([2.5, 0.9, 14.0])
valid = ranges >= 0.12 & ranges <= 12.0
print(valid)
