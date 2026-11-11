from typing import Protocol


class Performer(Protocol):
    @property
    def name(self) -> str: ...

    def perform_task(self, task: str, minutes: int) -> bool: ...


class Sensor:
    def __init__(self, kind: str):
        self.kind = kind


def run_all(performers: list[Performer]) -> None:
    for performer in performers:
        print(performer.name, performer.perform_task("patrol", 5))


run_all([Sensor("lidar")])  # No name, no perform_task
