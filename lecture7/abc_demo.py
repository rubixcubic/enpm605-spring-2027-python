"""An abstract base class: every range reader must define read_m()."""

from abc import ABC, abstractmethod


class RangeReader(ABC):
    """Reads ranges from a sensor. Subclasses say how."""

    def __init__(self, max_range_m: float):
        self.max_range_m = max_range_m

    @abstractmethod
    def read_m(self) -> float:
        """Return one range, in meters."""

    def obstacle_within(self, limit_m: float) -> bool:
        """True if the reading is closer than limit_m."""
        return self.read_m() < limit_m


class Lidar(RangeReader):
    def __init__(self, reading_m: float):
        super().__init__(12.0)  # A 12 m lidar, as in Lecture 2
        self._reading_m = reading_m  # A recorded reading, chosen

    def read_m(self) -> float:
        return min(self._reading_m, self.max_range_m)


class Sonar(RangeReader):
    def __init__(self, echo_s: float):
        super().__init__(4.0)  # A 4 m sonar, chosen for this example
        self._echo_s = echo_s  # Time for the sound to go and come back

    def read_m(self) -> float:
        return round(343.0 * self._echo_s / 2, 2)  # Sound: 343 m/s


for reader in [Lidar(2.5), Sonar(0.004)]:
    near = reader.obstacle_within(1.0)  # 1 m: chosen for this example
    print(type(reader).__name__, reader.read_m(), near)
