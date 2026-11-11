"""type_check.py with the None checked before the index."""


def first_obstacle(scan: list[float], safe_m: float) -> int | None:
    """Return the index of the first reading below safe_m, or None."""
    for i, r in enumerate(scan):
        if r < safe_m:
            return i
    return None


scan = [2.5, 0.9, 3.1]
i = first_obstacle(scan, 0.5)
if i is not None:
    print(f"Obstacle {scan[i]} m away")
else:
    print("No obstacle below 0.5 m")
