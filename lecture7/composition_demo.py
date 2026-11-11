"""Composition: a robot makes its own sensors and keeps them."""

from robotics_competition.robot import Robot

scout = Robot("Scout")
scout.add_sensor("lidar", 12.0)  # Ranges in meters, chosen
scout.add_sensor("sonar", 4.0)
print(scout.sensors)
print(max(sensor.range_m for sensor in scout.sensors))
try:
    scout.add_sensor("camera", -1.0)
except ValueError as err:
    print("ValueError", err)
print(len(scout.sensors))
