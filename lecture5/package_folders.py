"""Print the folders Python searches for installed packages, in order."""

import sys
from pathlib import Path

for folder in sys.path:
    if folder.endswith("packages"):
        folder = folder.replace(str(Path.cwd()), ".")  # Shorter paths
        print(folder.replace(str(Path.home()), "~"))
