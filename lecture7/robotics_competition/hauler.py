"""The Hauler class: a robot that carries loads, a kind of Robot."""

from robotics_competition.robot import Robot


class Hauler(Robot):
    """A robot that carries loads: 3% of the battery per minute."""

    DRAIN_PCT_PER_MIN = 3  # Replaces Robot's 2; chosen for this example

    def __init__(
        self, name: str, battery: int = 100, payload_kg: float = 120.0
    ) -> None:
        super().__init__(name, battery)
        self.payload_kg = payload_kg

    def __str__(self) -> str:
        return f"{super().__str__()} carrying {self.payload_kg} kg"
