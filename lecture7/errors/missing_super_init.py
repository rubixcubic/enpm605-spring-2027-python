class Robot:
    def __init__(self, name: str):
        self.name = name


class Scout(Robot):
    def __init__(self, name: str, max_speed_mps: float = 2.0):
        self.max_speed_mps = max_speed_mps  # No super().__init__


scout = Scout("Scout")
print(scout.max_speed_mps)
print(scout.name)
