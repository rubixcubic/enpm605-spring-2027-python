"""A Protocol: any class with these names fits, with no inheritance."""

from typing import Protocol, runtime_checkable

from robotics_competition.robot import Robot
from robotics_competition.scout import Scout
from robotics_competition.sensor import Sensor


@runtime_checkable
class Performer(Protocol):
    """What a team needs from a robot: a name and perform_task()."""

    @property
    def name(self) -> str: ...

    def perform_task(self, task: str, minutes: int) -> bool: ...


class SimRobot:
    """A robot in a simulator: not a Robot, but the same names."""

    def __init__(self, name: str):
        self.name = name

    def perform_task(self, task: str, minutes: int) -> bool:
        return True


def run_all(performers: list[Performer], task: str) -> None:
    for performer in performers:
        print(performer.name, performer.perform_task(task, 5))


run_all([Robot("Basic"), Scout("Scout"), SimRobot("Sim-1")], "patrol")
print(isinstance(SimRobot("Sim-2"), Performer))
print(isinstance(Sensor("lidar", 12.0), Performer))
