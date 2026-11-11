"""The Team class of the robotics competition."""

from robotics_competition.robot import Robot
from robotics_competition.task import Task


class Team:
    """A team of robots made elsewhere, and the tasks they did."""

    MAX_ROBOTS = 3  # Rule 7, chosen for this example

    def __init__(self, name: str):
        self._name = name
        self._robots: list[Robot] = []  # Aggregation: robots are added
        self._done: list[Task] = []  # Association: tasks done

    @property
    def name(self) -> str:
        return self._name

    @property
    def score(self) -> int:
        """The points of the tasks done (rule 8), added at each read."""
        return sum(task.points for task in self._done)

    def add_robot(self, robot: Robot) -> None:
        """Add a robot made elsewhere, once; at most MAX_ROBOTS."""
        if robot in self._robots:
            raise ValueError(f"{robot.name} is already in {self._name}")
        if len(self._robots) == Team.MAX_ROBOTS:  # Rule 7
            raise ValueError(f"{self._name} is full")
        self._robots.append(robot)

    def assign(self, task: Task) -> bool:
        """Give the task to the first robot that does it; True if done."""
        for robot in self._robots:
            if robot.perform_task(task.name, task.minutes):
                self._done.append(task)
                return True
        return False

    def __len__(self) -> int:
        return len(self._robots)

    def __iter__(self):
        return iter(self._robots)

    def __repr__(self) -> str:
        names = [robot.name for robot in self._robots]
        return f"Team({self._name!r}, {names}, score={self.score})"
