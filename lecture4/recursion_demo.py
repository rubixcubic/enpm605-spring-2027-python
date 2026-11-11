"""Recursive functions: a base case and a recursive case."""


def factorial(n: int) -> int:
    if n == 0:  # Base case: no further call
        return 1
    return n * factorial(n - 1)  # Recursive case: a smaller n


print(factorial(5))


# The same function, printing each call and each return
def factorial_traced(n: int, depth: int = 0) -> int:
    pad = "    " * depth
    print(f"{pad}factorial({n})")
    if n == 0:
        result = 1
    else:
        result = n * factorial_traced(n - 1, depth + 1)
    print(f"{pad}returns {result}")
    return result


factorial_traced(3)

# Coordinate frames: each value is a dict of child frames
frames = {"odom": {"base_link": {"lidar_link": {}, "camera_link": {}}}}


def print_tree(tree: dict, depth: int = 0) -> None:
    for name, children in tree.items():
        print("  " * depth + name)
        print_tree(children, depth + 1)  # {} has no items: no call


print_tree(frames)
