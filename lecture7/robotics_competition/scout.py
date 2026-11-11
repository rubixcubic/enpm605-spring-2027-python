"""The Scout class: a light robot, a kind of Robot."""

from robotics_competition.robot import Robot


class Scout(Robot):
    """A light, fast robot: 1% of the battery per minute."""

    DRAIN_PCT_PER_MIN = 1  # Replaces Robot's 2; chosen for this example

    def __init__(
        self, name: str, battery: int = 100, max_speed_mps: float = 2.0
    ) -> None:
        super().__init__(name, battery)  # Robot sets name and battery
        self.max_speed_mps = max_speed_mps

    def drive_time(self, distance_m: float) -> float:
        """Seconds to drive distance_m at the scout's top speed."""
        return distance_m / self.max_speed_mps
