"""The smallest class, and two objects made from it."""


class Robot:
    """A robot in the competition."""


scout = Robot()
hauler = Robot()
print(type(Robot), type(scout))
print(scout is hauler, isinstance(scout, Robot))
print(scout)
