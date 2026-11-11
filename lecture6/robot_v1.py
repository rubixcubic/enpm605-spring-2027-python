"""A Robot class with __init__ and two methods."""


class Robot:
    """A robot in the competition."""

    def __init__(self, name: str, battery: int = 100):
        self.name = name
        self.battery = battery  # Percent, 0 to 100

    def perform_task(self, task: str, minutes: int) -> None:
        self.battery -= 2 * minutes  # 2% per minute: an example value
        print(f"{self.name} did {task}: battery {self.battery}%")

    def recharge(self) -> None:
        self.battery = 100


scout = Robot("Scout")
hauler = Robot("Hauler", battery=60)
print(scout.name, scout.battery, hauler.name, hauler.battery)

scout.perform_task("pick widget", 5)
print(scout.battery, hauler.battery)

Robot.perform_task(hauler, "carry crate", 10)  # The same kind of call
hauler.recharge()
print(hauler.battery)
