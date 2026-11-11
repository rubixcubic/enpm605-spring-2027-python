"""Lists: creating, changing, searching, sorting, comprehensions, and copies."""

import copy

# Creating lists
ranges_m = [2.5, 0.9, 3.1]  # Chosen for this example
mixed = ["lidar", 12.0, True, None]
empty = []
print(len(ranges_m), len(mixed), len(empty))
print(list("imu"), list(range(4)))
print([0.0] * 4, [1, 2] + [3])

# Indexing, slicing, and changing items
ranges_m = [2.5, 0.9, 3.1, 0.3, 4.2]
print(ranges_m[0], ranges_m[-1])
print(ranges_m[1:3], ranges_m[::2])
ranges_m[0] = 2.6
print(ranges_m)
ranges_m[1:3] = [1.0]
print(ranges_m)

# Adding items
scan = [2.5]
scan.append(0.9)
scan.extend([3.1, 0.3])
scan.insert(0, 1.7)
print(scan)
scan.append([4.2, 5.0])
print(scan, len(scan))

# Removing items
waypoints = ["dock", "A", "B", "A", "C"]
last = waypoints.pop()
first = waypoints.pop(0)
print(last, first, waypoints)
waypoints.remove("A")
print(waypoints)
del waypoints[0]
print(waypoints)
waypoints.clear()
print(waypoints)

# Searching
waypoints = ["dock", "A", "B", "A"]
print("B" in waypoints, "Z" in waypoints)
print(waypoints.index("A"), waypoints.count("A"))

# In-place methods return None
ranges_m = [2.5, 0.9, 3.1]
result = ranges_m.sort()
print(result, ranges_m)
ranges_m = [2.5, 0.9, 3.1]
print(sorted(ranges_m), ranges_m)
print(sorted(ranges_m, reverse=True))

# Removing items while looping skips items
RANGE_MIN_M = 0.12  # The lidar of Lecture 2
scan = [0.0, 0.0, 2.5, 0.0, 3.1]
for r in scan:
    if r < RANGE_MIN_M:
        scan.remove(r)
print(scan)

# List comprehensions
squares = [n**2 for n in range(5)]
print(squares)
squares = []
for n in range(5):
    squares.append(n**2)
print(squares)

# A comprehension with if, and with a conditional expression
scan = [2.5, 0.0, 3.1, 13.5, 0.8]
valid = [r for r in scan if 0.12 <= r <= 12.0]
labels = ["near" if r < 1.0 else "far" for r in valid]
print(valid)
print(labels)

# Functions that take an iterable
print(len(valid), min(valid), max(valid), sum(valid))
print(f"Mean: {sum(valid) / len(valid):.2f} m")
print(any(r < 1.0 for r in valid), all(r < 1.0 for r in valid))

# A 3 x 3 occupancy grid: 1 means occupied
grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(grid[1][1], len(grid), len(grid[0]))
for row in grid:
    for cell in row:
        print("#" if cell else ".", end="")
    print()

# Repetition copies references, not inner lists
bad = [[0] * 3] * 3
bad[0][0] = 1
print(bad)
good = [[0] * 3 for _ in range(3)]
good[0][0] = 1
print(good)
print(bad[0] is bad[1], good[0] is good[1])

# Copies of a list of lists: waypoints as [x, y] lists
path = [[0.0, 0.0], [1.0, 0.0]]
alias = path
shallow = path.copy()
deep = copy.deepcopy(path)
path[0][0] = 9.9
path.append([2.0, 0.0])
print(alias)
print(shallow)
print(deep)
