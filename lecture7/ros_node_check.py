"""A ROS 2 node is an object of a class that inherits from Node.

Needs ROS 2 Jazzy sourced (Lecture 8). Makes one node and shuts it
down: nothing is published.
"""

import rclpy
from rclpy.node import Node


class ScoutNode(Node):
    def __init__(self):
        super().__init__("scout")  # Node.__init__ takes the node's name
        self.max_speed_mps = 2.0  # Chosen for this example


rclpy.init()
node = ScoutNode()
print(node.get_name(), node.max_speed_mps, isinstance(node, Node))
print([cls.__name__ for cls in ScoutNode.__mro__])
node.destroy_node()
rclpy.shutdown()
