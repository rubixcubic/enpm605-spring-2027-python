class Robot:
    def __init__(self, name: str, battery: int = 100):
        self.name = name
        self.battery = battery

    def perform_task(self, task: str, minutes: int) -> None:
        self.battery -= 2 * minutes


scout = Robot("Scout")
scout.battery = "full"  # Any code can assign any value
scout.perform_task("pick widget", 5)
