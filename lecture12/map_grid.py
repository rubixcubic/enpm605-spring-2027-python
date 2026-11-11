"""A saved map (yaml and pgm) read with NumPy: cells, values, places."""

import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent


def read_yaml(path):
    """Return a map's yaml settings, one key per line, as text."""
    info = {}
    for line in path.read_text().splitlines():
        key, _, value = line.partition(":")
        info[key.strip()] = value.strip()
    return info


def read_pgm(path):
    """Return a binary PGM image (P5) as rows of uint8, top first."""
    magic, size, maxval, pixels = path.read_bytes().split(b"\n", 3)
    assert magic == b"P5" and maxval == b"255"
    width, height = map(int, size.split())
    return np.frombuffer(pixels, dtype=np.uint8).reshape(height, width)


def load_map(yaml_path):
    """Return the settings and the grid, the bottom row as row 0."""
    info = read_yaml(yaml_path)
    image = read_pgm(yaml_path.parent / info["image"])
    p = (255 - image) / 255.0  # negate: 0, so black (0) is p = 1.0
    grid = np.full(image.shape, -1, dtype=np.int8)  # Unknown, unless...
    grid[p > float(info["occupied_thresh"])] = 100
    grid[p < float(info["free_thresh"])] = 0
    return info, grid[::-1]  # Row 0 at the bottom, as in OccupancyGrid


DEFAULT = HERE / "maps" / "sandbox.yaml"
yaml_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
info, grid = load_map(yaml_path)
res = float(info["resolution"])
ox, oy, _ = (float(v) for v in info["origin"].strip("[]").split(","))
print("shape (rows, columns):", grid.shape, "cell:", res, "m")
print("origin:", (ox, oy))

values, counts = np.unique(grid, return_counts=True)
print("cells by value:", dict(zip(values.tolist(), counts.tolist())))
print(f"area known: {(grid >= 0).sum() * res * res:.1f} m^2")

# The area the grid covers, in the map frame
rows, cols = grid.shape
print(f"x from {ox} to {ox + cols * res:.3f}")
print(f"y from {oy} to {oy + rows * res:.3f}")

# The cell that holds a point: where AMCL said the robot stopped (run 1)
x, y = 3.39, 0.97
c, r = int((x - ox) // res), int((y - oy) // res)
print(f"point ({x}, {y}): row {r}, column {c}, value {grid[r, c]}")

# The center of that cell
cx, cy = ox + (c + 0.5) * res, oy + (r + 0.5) * res
print(f"center of row {r}, column {c}: ({cx:.3f}, {cy:.3f})")
