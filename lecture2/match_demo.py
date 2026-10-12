"""Match a command against literal patterns.

Run it with a command:  uv run lecture2/match_demo.py stop
"""

import sys

command = sys.argv[1]  # The first word after the file name

match command:
    case "stop":
        print("Stopping")
    case "forward" | "back":
        print(f"Driving {command}")
    case _:
        print(f"Unknown command: {command}")
