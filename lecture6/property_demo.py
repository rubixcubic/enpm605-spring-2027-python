"""The battery and name properties of the competition's Robot."""

from robotics_competition.robot import Robot

scout = Robot("Scout")
scout.battery = 80  # Runs the setter
print(scout.battery, scout.name)  # Run the getters
print(vars(scout))

for value in [150, "full"]:
    try:
        scout.battery = value
    except (ValueError, TypeError) as err:
        print(type(err).__name__, err)

try:
    scout.name = "Bob"
except AttributeError as err:
    print("AttributeError", err)
print(scout)
