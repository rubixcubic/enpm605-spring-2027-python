"""The Robot class of the robotics competition."""


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
        Robot.total_robots += 1

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
        if self._battery < Robot.LOW_BATTERY_PCT:
            return "needs_recharge"
        return "active"

    def perform_task(self, task: str, minutes: int) -> bool:
        """Do the task if active and the battery covers it; True if done."""
        drain = minutes * Robot.DRAIN_PCT_PER_MIN
        if self.status != "active" or drain > self._battery:
            return False
        self.battery = self._battery - drain
        return True

    def recharge(self) -> None:
        """Fill the battery to 100%."""
        self.battery = 100

    def __repr__(self) -> str:
        return f"Robot({self._name!r}, battery={self._battery})"

    def __str__(self) -> str:
        return f"{self._name} [{self._battery}%, {self.status}]"
