"""Print the version of NumPy and Matplotlib, and the folder of each."""

from pathlib import Path

import matplotlib
import numpy

for module in (numpy, matplotlib):
    folder = str(Path(module.__file__).parent)
    folder = folder.replace(str(Path.cwd()), ".")  # Shorter paths
    folder = folder.replace(str(Path.home()), "~")
    print(module.__name__, module.__version__, folder)
