"""What rclpy.init() reads from the command line.

Needs ROS 2 Jazzy sourced. Run it with arguments of its own and ROS
arguments, for example:

    python3 lecture9/ros_args_demo.py --laps 3 --ros-args -r __node:=scout_1
"""

import sys

import rclpy
from rclpy.utilities import remove_ros_args

print("sys.argv[1:]:", sys.argv[1:])
rclpy.init(args=None)  # None: rclpy reads sys.argv itself
node = rclpy.create_node("scout")  # The name written in the code
print("node name:", node.get_fully_qualified_name())
print("program's own arguments:", remove_ros_args(sys.argv)[1:])
node.destroy_node()
rclpy.shutdown()
