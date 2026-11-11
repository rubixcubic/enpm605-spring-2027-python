"""Closures: a function that keeps the names of its enclosing call."""


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


scans = make_counter()
print(scans(), scans(), scans())
images = make_counter()
print(images(), scans())
print(scans.__code__.co_freevars)
print(scans.__closure__[0].cell_contents)


# A closure that remembers its arguments
def make_range_check(min_m, max_m):
    def check(r):
        return min_m <= r <= max_m

    return check


lidar_ok = make_range_check(0.12, 12.0)
print(lidar_ok.__code__.co_freevars)
print([c.cell_contents for c in lidar_ok.__closure__])

# A default value is evaluated when the lambda is made
checks = []
for limit in [0.5, 1.0, 2.0]:
    checks.append(lambda r, limit=limit: r < limit)
print([check(0.8) for check in checks])
