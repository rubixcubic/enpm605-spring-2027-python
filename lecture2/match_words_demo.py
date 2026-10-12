"""Match the words of a command against sequence patterns.

Run it with a command in quotes:  uv run lecture2/match_words_demo.py "move 2.5"
"""

import sys

words = sys.argv[1].split()

match words:
    case ["move", distance] if float(distance) > 0:
        print(f"Moving {distance} m")
    case ["turn", direction]:
        print(f"Turning {direction}")
    case ["stop"]:
        print("Stopping")
    case _:
        print(f"Cannot run: {words}")
