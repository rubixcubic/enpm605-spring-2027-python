"""Four ways to import names from the sensors package."""

import sensors.lidar
from sensors import lidar
from sensors.lidar import MAX_RANGE_M
from sensors.sonar import MAX_RANGE_M as SONAR_MAX_RANGE_M

print(sensors.lidar.MAX_RANGE_M)  # Full path to the name
print(lidar.MAX_RANGE_M)  # The module, by its own name
print(MAX_RANGE_M)  # The name itself
print(SONAR_MAX_RANGE_M)  # The name itself, renamed
