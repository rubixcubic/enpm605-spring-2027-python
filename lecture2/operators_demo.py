"""Arithmetic, comparison, logical, and membership operators."""

# Arithmetic
print(7 + 3, 7 - 3, 7 * 3)
print(7 / 3)
print(7 // 3, 7 % 3, 2**10)

# Floor division and modulo round toward negative infinity
print(7 // 2, -7 // 2)
print(7 % 3, -7 % 3)
heading_deg = -30
print(heading_deg % 360)
print(370 % 360)

# Precedence
print(2 + 3 * 4)
print(-(2**2))
print((-2) ** 2)

# Augmented assignment
distance_m = 0.0
distance_m += 0.5
distance_m += 0.5
distance_m *= 2
print(distance_m)

# Comparison
range_m = 3.2
print(range_m == 3.2, range_m != 3.2)
print(range_m > 1.0, range_m <= 1.0)
print(0.12 <= range_m <= 12.0)  # Within the lidar's range

# Logical
battery_ok = True
obstacle_ahead = False
print(battery_ok and not obstacle_ahead)
print(battery_ok or obstacle_ahead)
print(not battery_ok)

# and and or return one of their operands
label = "lidar"
count = 0
missing = ""
print(label and count)
print(label and "sonar")
print(missing or "default")
print(count or None)

# A default with or replaces 0.0 too
requested_speed = 0.0  # The operator asks the robot to stop
speed = requested_speed or 0.5  # 0.5 m/s when no speed is given
print(speed)
speed = 0.5 if requested_speed is None else requested_speed
print(speed)

# Short-circuit evaluation
readings = []
print(len(readings) > 0 and readings[0] > 1.0)

# Membership
topic = "/robot1/cmd_vel"
print("cmd_vel" in topic)
print("scan" not in topic)
print(3 in [1, 2, 3])
