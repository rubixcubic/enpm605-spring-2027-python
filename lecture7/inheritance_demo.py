"""Scout and Hauler inherit from Robot."""

from robotics_competition.hauler import Hauler
from robotics_competition.robot import Robot
from robotics_competition.scout import Scout

scout = Scout("Scout", max_speed_mps=2.5)  # Values chosen
hauler = Hauler("Hauler", 80)
print(repr(scout), scout.max_speed_mps, scout.drive_time(10.0))
print(hauler.name, hauler.battery, hauler.payload_kg)
print(hauler)

print(isinstance(scout, Robot), isinstance(scout, Hauler))
print(issubclass(Scout, Robot), issubclass(Robot, Scout))
print([cls.__name__ for cls in Scout.__mro__])

print(Scout.DRAIN_PCT_PER_MIN, Robot.DRAIN_PCT_PER_MIN)
print("perform_task" in vars(Scout), "perform_task" in vars(Robot))
print(Robot.total_robots, Scout.total_robots)
print(repr(Scout.from_dict({"name": "S2", "battery": 70})))
