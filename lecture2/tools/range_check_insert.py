"""Find the sensors package by editing sys.path inside the program."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sensors.lidar import MAX_RANGE_M

print(f"Lidar range: {MAX_RANGE_M} m")
