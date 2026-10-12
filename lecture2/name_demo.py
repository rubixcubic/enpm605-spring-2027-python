"""Print __name__ in the file that runs and in a module it imports."""

import sensors.lidar

print(f"In name_demo.py, __name__ is {__name__!r}")
print(f"In lidar.py, __name__ is {sensors.lidar.__name__!r}")
