"""Publishing a message whose field has the wrong type.

Needs ROS 2 Jazzy sourced, with ROS_DOMAIN_ID set (not 0 in class).
"""

import rclpy
from sensor_msgs.msg import BatteryState

rclpy.init()
node = rclpy.create_node("bad_publisher")
publisher = node.create_publisher(BatteryState, "battery_test", 10)
msg = BatteryState()
msg.percentage = "full"  # Accepted: fields are not checked here
print("publishing", flush=True)
publisher.publish(msg)  # The conversion to C checks the type
print("published")  # Never printed
