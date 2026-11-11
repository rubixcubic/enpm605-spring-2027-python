class Robot:
    log = []  # A class attribute: one list for every robot

    def __init__(self, name: str):
        self.name = name

    def perform_task(self, task: str) -> None:
        self.log.append(task)


scout = Robot("Scout")
hauler = Robot("Hauler")
scout.perform_task("pick widget")
print(hauler.log, scout.log is hauler.log)
