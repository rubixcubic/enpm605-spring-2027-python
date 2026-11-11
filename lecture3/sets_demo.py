"""Sets: unique items, set operations, adding and removing."""

# A set holds each item once (values chosen for this example)
readings = [1.5, 2.3, 1.5, 3.7, 2.3]
unique = set(readings)
print(unique)
print(len(readings), len(unique))
print(type(set()), type({}))

# Set operations (detections chosen for this example)
lidar_sees = {"wall", "person", "cone", "pallet"}
camera_sees = {"person", "cone", "door"}
print(sorted(lidar_sees | camera_sees))
print(sorted(lidar_sees & camera_sees))
print(sorted(lidar_sees - camera_sees))
print(sorted(lidar_sees ^ camera_sees))

# Adding and removing items
seen = set()
for label in ["person", "cone", "person"]:
    seen.add(label)
print(sorted(seen))
seen.discard("door")  # Not there: no error
seen.remove("cone")
print(sorted(seen))

# A set comprehension
topics = ["/scan", "/odom", "/robot1/scan", "/robot2/scan"]
names = {t.split("/")[-1] for t in topics}
print(sorted(names))
