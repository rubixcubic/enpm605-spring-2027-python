class Robot:
    def __init__(self, name: str):
        self.name = name


scout = Robot("Scout")
print(scout.name)
print(Robot.name)
