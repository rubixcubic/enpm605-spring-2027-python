class Robot:
    def __init__(self, name: str, battery: int = 100):
        self.name = name
        self.battery = battery


scout = Robot("Scout")
print(scout.batery)
