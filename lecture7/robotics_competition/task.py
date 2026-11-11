"""The Task class of the robotics competition, as a data class."""

from dataclasses import dataclass

POINTS = {"low": 1, "medium": 2, "high": 3, "critical": 5}  # Rules 2, 8


@dataclass(frozen=True)
class Task:
    """A task: a name, a priority (rule 2), and a length in minutes."""

    name: str
    priority: str
    minutes: int

    def __post_init__(self) -> None:
        if self.priority not in POINTS:
            raise ValueError(f"priority must be one of {list(POINTS)}")
        m = self.minutes
        if not isinstance(m, int) or isinstance(m, bool):
            raise TypeError(f"minutes must be an int, got {m!r}")
        if m <= 0:
            raise ValueError(f"minutes must be positive, got {m}")

    @property
    def points(self) -> int:
        """The points a team scores when one of its robots does it."""
        return POINTS[self.priority]
