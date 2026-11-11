"""Two processes do not share memory: a change in one stays in it."""

import multiprocessing
import os

readings = [3.2]  # Range readings in meters, chosen for this example


def child():
    readings.append(2.8)  # Changes the child's copy of the list
    print(f"child sees  {readings}")


if __name__ == "__main__":
    process = multiprocessing.Process(target=child)
    process.start()  # A new process, with its own copy of memory
    process.join()  # Wait for it to finish
    print(f"parent sees {readings}")
    print("different process IDs:", process.pid != os.getpid())
