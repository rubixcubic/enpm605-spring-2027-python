from abc import ABC, abstractmethod


class RangeReader(ABC):
    @abstractmethod
    def read_m(self) -> float:
        """Return one range, in meters."""


class Camera(RangeReader):
    def read_range(self) -> float:  # Not read_m: a different name
        return 3.0


print("Camera is defined")
cam = Camera()
