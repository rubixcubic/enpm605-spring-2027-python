class Robot:
    def __init__(self, name: str):
        self.name = name

    def perform_task(self, task: str) -> None:
        self.last_task = task  # Made only when this method runs

    def report(self) -> None:
        print(self.name, self.last_task)


scout = Robot("Scout")
scout.report()
