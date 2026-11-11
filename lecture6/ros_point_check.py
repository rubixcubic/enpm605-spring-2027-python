"""A ROS 2 message is an object: repr, ==, and its x property.

Needs ROS 2 Jazzy sourced (Lecture 8). Makes a message object only:
no node, nothing sent.
"""

from geometry_msgs.msg import Point

p = Point(x=1.0, y=2.0)
print(repr(p))
print(p == Point(x=1.0, y=2.0, z=0.0))
print(type(vars(Point)["x"]).__name__, Point.__slots__[:3])
p.x = "far"  # Checked only when ROS_PYTHON_CHECK_FIELDS=1
print(repr(p))
