"""A class method makes a robot; a static method draws a battery."""

from robotics_competition.robot import Robot

config = {"name": "Scout", "battery": 80}  # As read from a file
scout = Robot.from_dict(config)  # cls is Robot
print(repr(scout), Robot.total_robots)
print(Robot.battery_bar(scout.battery), scout.battery_bar(35))
