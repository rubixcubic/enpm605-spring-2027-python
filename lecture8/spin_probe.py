"""What rclpy.spin() raises when the process gets a signal.

Needs ROS 2 Jazzy sourced. Stop it with Ctrl+C (SIGINT), or with kill
(SIGTERM). Prints the exception, whether ROS 2 is still running, and
what a second rclpy.shutdown() does.
"""

import rclpy
from rclpy.executors import ExternalShutdownException

rclpy.init()
node = rclpy.create_node("spin_probe")
try:
    rclpy.spin(node)
except (KeyboardInterrupt, ExternalShutdownException) as err:
    print("spin raised", type(err).__name__, "| rclpy.ok():", rclpy.ok())
node.destroy_node()
try:
    rclpy.shutdown()
except RuntimeError as err:
    print("rclpy.shutdown() again:", type(err).__name__)
rclpy.try_shutdown()
print("rclpy.try_shutdown(): no error")
