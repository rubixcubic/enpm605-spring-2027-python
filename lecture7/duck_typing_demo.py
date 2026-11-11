"""Duck typing: Team works with any object that has the methods."""

from robotics_competition.task import Task
from robotics_competition.team import Team


class SimRobot:
    """A robot in a simulator: not a Robot, but the same names."""

    def __init__(self, name: str):
        self.name = name

    def perform_task(self, task: str, minutes: int) -> bool:
        print(f"[sim] {self.name} does {task} ({minutes} min)")
        return True


beta = Team("Beta")
beta.add_robot(SimRobot("Sim-1"))  # Not a Robot
print(beta.assign(Task("scan shelf", "medium", 3)), beta.score)
