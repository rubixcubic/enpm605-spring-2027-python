"""The Sensor class of the robotics competition, as a data class."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Sensor:
    """A range sensor: its kind and its range in meters (rule 6)."""

    kind: str
    range_m: float

    def __post_init__(self) -> None:
        r = self.range_m
        if not isinstance(r, (int, float)) or isinstance(r, bool):
            raise TypeError(f"range_m must be a number, got {r!r}")
        if r <= 0:
            raise ValueError(f"range_m must be positive, got {r}")
