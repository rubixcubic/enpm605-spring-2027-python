"""Two leading underscores: a base class and a subclass keep apart."""


class Robot:
    def __init__(self):
        self.__serial = "R-100"  # Stored as _Robot__serial
        self._code = "R"


class Scout(Robot):
    def __init__(self):
        super().__init__()
        self.__serial = "S-200"  # Stored as _Scout__serial: no clash
        self._code = "S"  # One underscore: replaces Robot's _code


print(vars(Scout()))
