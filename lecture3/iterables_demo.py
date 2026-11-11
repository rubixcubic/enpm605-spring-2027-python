"""Iterables and iterators: list(), iter(), next(), and zip()."""

# Iterables
print(list("imu"))
print(list(range(3)))
print(list({"x": 1.0, "y": 2.0}))

# iter() and next()
ranges_m = [2.5, 0.9, 3.1]  # Chosen for this example
it = iter(ranges_m)
print(type(it))
print(next(it))
print(next(it))
print(next(it))

# One pass uses up an iterator
it = iter(ranges_m)
print(list(it))
print(list(it))
print(list(ranges_m), list(ranges_m))

# zip
angles_deg = [-30, 0, 30]  # Chosen for this example
for angle, r in zip(angles_deg, ranges_m):
    print(f"{angle:>4} deg: {r} m")
print(list(zip(angles_deg, ranges_m)))

# zip stops at the shortest input
print(list(zip([-30, 0, 30], [2.5, 0.9])))
