"""The Robot class of the robotics competition (Lecture 7 version).

Lecture 6's robot.py with four changes: from_dict() and battery_bar()
(a class method and a static method); add_sensor(), which makes the
robot's sensors (composition); the rule constants read through self, so
a subclass can change them; and a repr that names the object's class.
"""

from robotics_competition.sensor import Sensor


class Robot:
    """A competition robot with a name, a battery level, and a status.

    The battery level is a whole percent from 0 to 100. Below
    LOW_BATTERY_PCT, the robot needs a recharge and does no tasks.
    """

    LOW_BATTERY_PCT = 10  # Rule 3, chosen for this example
    DRAIN_PCT_PER_MIN = 2  # Rule 4, chosen for this example
    total_robots = 0

    def __init__(self, name: str, battery: int = 100):
        self._name = name
        self.battery = battery  # Runs the battery setter
        self._sensors: list[Sensor] = []
        Robot.total_robots += 1

    @classmethod
    def from_dict(cls, config: dict) -> "Robot":
        """Make a robot from a dictionary, such as one read from a file."""
        return cls(config["name"], config.get("battery", 100))

    @staticmethod
    def battery_bar(level: int) -> str:
        """Draw a battery level as ten characters: [######----]."""
        bars = level // 10
        return "[" + "#" * bars + "-" * (10 - bars) + "]"

    @property
    def name(self) -> str:
        """The robot's name. It cannot change (rule 5)."""
        return self._name

    @property
    def battery(self) -> int:
        """The battery level, in percent."""
        return self._battery

    @battery.setter
    def battery(self, value: int) -> None:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"battery must be an int, got {value!r}")
        if not 0 <= value <= 100:
            raise ValueError(f"battery must be 0 to 100, got {value}")
        self._battery = value

    @property
    def status(self) -> str:
        """'needs_recharge' below LOW_BATTERY_PCT, else 'active'."""
        if self._battery < self.LOW_BATTERY_PCT:
            return "needs_recharge"
        return "active"

    @property
    def sensors(self) -> tuple[Sensor, ...]:
        """The robot's sensors, as a tuple: a caller cannot add one."""
        return tuple(self._sensors)

    def add_sensor(self, kind: str, range_m: float) -> None:
        """Make a sensor and mount it on this robot (composition)."""
        self._sensors.append(Sensor(kind, range_m))

    def perform_task(self, task: str, minutes: int) -> bool:
        """Do the task if active and the battery covers it; True if done."""
        drain = minutes * self.DRAIN_PCT_PER_MIN
        if self.status != "active" or drain > self._battery:
            return False
        self.battery = self._battery - drain
        return True

    def recharge(self) -> None:
        """Fill the battery to 100%."""
        self.battery = 100

    def __repr__(self) -> str:
        cls = type(self).__name__
        return f"{cls}({self._name!r}, battery={self._battery})"

    def __str__(self) -> str:
        return f"{self._name} [{self._battery}%, {self.status}]"
