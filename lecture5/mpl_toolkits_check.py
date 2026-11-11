"""Print the folder Python loads mpl_toolkits from (Matplotlib's add-ons)."""

from pathlib import Path

import matplotlib.pyplot  # noqa: F401
import mpl_toolkits

for folder in mpl_toolkits.__path__:
    folder = folder.replace(str(Path.cwd()), ".")  # Shorter paths
    print(folder.replace(str(Path.home()), "~"))
