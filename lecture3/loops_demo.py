"""Loops: for, range(), enumerate(), while, break, continue, and else."""

import sys

# for over a list
ranges_m = [2.5, 0.9, 3.1]  # Chosen for this example
for r in ranges_m:
    print(f"Range: {r} m")
print(f"After the loop, r is {r}")

# range
print(list(range(5)))
print(list(range(2, 7)))
print(list(range(0, 10, 2)))
print(list(range(5, 0, -1)))
print(range(5))
for _ in range(2):
    print("Beep")

# range stores start, stop, and step
numbers = range(1_000_000)
print(len(numbers), numbers[10], 999_999 in numbers)
print(sys.getsizeof(numbers), sys.getsizeof(list(numbers)))

# enumerate
sensors = ["lidar", "camera", "imu"]
for i in range(len(sensors)):
    print(i, sensors[i])
for i, name in enumerate(sensors):
    print(i, name)
for i, name in enumerate(sensors, start=1):
    print(f"{i}. {name}")

# while
battery_pct = 100  # Chosen for this example
tasks = 0
while battery_pct >= 20:
    battery_pct -= 30  # Each task: 30%, chosen for this example
    tasks += 1
print(f"{tasks} tasks, battery at {battery_pct}%")

# break
ranges_m = [2.5, 0.9, 0.3, 3.1]  # Chosen for this example
SAFE_M = 0.5  # Chosen for this example
for i, r in enumerate(ranges_m):
    if r < SAFE_M:
        print(f"Obstacle at index {i}: {r} m")
        break
    print(f"Index {i}: clear")

# continue
RANGE_MIN_M, RANGE_MAX_M = 0.12, 12.0  # The lidar of Lecture 2
scan = [2.5, 0.0, 3.1, float("inf"), 1.2]
total = 0.0
count = 0
for r in scan:
    if not (RANGE_MIN_M <= r <= RANGE_MAX_M):
        continue
    total += r
    count += 1
print(f"{count} valid readings, mean {total / count:.2f} m")

# else on a loop: no reading below SAFE_M
for r in [2.5, 0.9, 3.1]:
    if r < SAFE_M:
        print(f"Stop: {r} m")
        break
else:
    print("Path clear")

# else on a loop: one reading below SAFE_M
for r in [2.5, 0.3, 3.1]:
    if r < SAFE_M:
        print(f"Stop: {r} m")
        break
else:
    print("Path clear")
