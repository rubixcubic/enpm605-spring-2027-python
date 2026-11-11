"""len(), in, for, and bool() for a TaskLog object."""


class TaskLog:
    """The tasks a robot has done, in order."""

    def __init__(self):
        self.tasks = []

    def add(self, task: str) -> None:
        self.tasks.append(task)

    def __len__(self) -> int:
        return len(self.tasks)

    def __contains__(self, task: str) -> bool:
        return task in self.tasks

    def __iter__(self):
        return iter(self.tasks)


log = TaskLog()
print(len(log), bool(log))
log.add("pick widget")
log.add("carry crate")
print(len(log), bool(log), "carry crate" in log)
for task in log:
    print("-", task)
