"""A ROS 2 message is a Python object with one attribute per field.

Needs ROS 2 Jazzy sourced. Makes one message; no node, nothing sent.
"""

from sensor_msgs.msg import BatteryState

msg = BatteryState()  # Every field starts at its default
print(msg.percentage, msg.present, msg.location == "")
msg.percentage = 0.16  # The message uses 0 to 1: 16% is 0.16
msg.present = True
print(msg.percentage, msg.present)
msg.percentage = "full"  # Not a float, and no error yet
print(msg.percentage)
try:
    msg.charge_level = 3  # Not a field of BatteryState
except AttributeError as err:
    print(type(err).__name__, err)
