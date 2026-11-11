"""A bug that a type checker finds before the program runs."""


def first_obstacle(scan: list[float], safe_m: float) -> int | None:
    """Return the index of the first reading below safe_m, or None."""
    for i, r in enumerate(scan):
        if r < safe_m:
            return i
    return None


scan = [2.5, 0.9, 3.1]
i = first_obstacle(scan, 0.5)
print(f"Obstacle {scan[i]} m away")  # i can be None
