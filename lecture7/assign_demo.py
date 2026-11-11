"""Association: a team uses each Task it is given, and scores it."""

from robotics_competition.robot import Robot
from robotics_competition.task import Task
from robotics_competition.team import Team

alpha = Team("Alpha")
alpha.add_robot(Robot("Scout", 30))  # 30%: chosen for this example
alpha.add_robot(Robot("Hauler"))
deliver = Task("deliver part", "critical", 12)  # Chosen tasks
scan = Task("scan shelf", "medium", 3)
for task in [deliver, scan]:
    print(task.name, alpha.assign(task), alpha.score)
for robot in alpha:
    print(robot)
