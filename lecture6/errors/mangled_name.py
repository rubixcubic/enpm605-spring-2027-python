class Robot:
    def __init__(self, battery: int = 100):
        self.__battery = battery  # Two underscores: the name is mangled


scout = Robot()
print(vars(scout))
print(scout.__battery)
