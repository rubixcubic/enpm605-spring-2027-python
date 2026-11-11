"""What @property does, written without the @ line."""


class Robot:
    def __init__(self, name: str):
        self._name = name

    def name(self) -> str:
        """The robot's name. It cannot change."""
        return self._name

    name = property(name)  # What @property above def name would do


scout = Robot("Scout")
print(scout.name, type(vars(Robot)["name"]).__name__)
print(Robot.name.__doc__)
