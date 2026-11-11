"""The same calls on a Robot, a Scout, and a Hauler."""

from robotics_competition.hauler import Hauler
from robotics_competition.robot import Robot
from robotics_competition.scout import Scout

fleet = [Robot("Basic"), Scout("Scout"), Hauler("Hauler")]
for robot in fleet:
    robot.perform_task("patrol", 10)  # 10 min: chosen for this example
    print(robot)
