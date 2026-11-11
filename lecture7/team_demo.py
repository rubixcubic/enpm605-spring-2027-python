"""Aggregation: a team holds robots that were made outside it."""

from robotics_competition.robot import Robot
from robotics_competition.team import Team

scout = Robot("Scout")
hauler = Robot("Hauler", 60)  # 60%: chosen for this example
alpha = Team("Alpha")
alpha.add_robot(scout)
alpha.add_robot(hauler)
print(alpha, len(alpha))
for robot in [scout, Robot("Carrier"), Robot("Lifter")]:
    try:
        alpha.add_robot(robot)
    except ValueError as err:
        print("ValueError", err)
del alpha  # The team is gone; the robots are not
print(scout, hauler)
