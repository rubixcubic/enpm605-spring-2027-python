"""Two threads that wait, and two threads that compute, timed.

Each task is run once alone, then twice at the same time in two threads.
Every time is the best of 5 repeats, in seconds.
"""

import threading
import time

N = 8_000_000  # Chosen so that one count takes about 0.2 s on the instructor PC


def wait():
    time.sleep(0.2)  # Waiting: the thread runs no Python code


def count():
    total = 0
    for i in range(N):  # Computing: the thread runs Python code
        total += i


def best_time(task, threads):
    best = float("inf")
    for _ in range(5):
        workers = [threading.Thread(target=task) for _ in range(threads)]
        start = time.perf_counter()
        for w in workers:
            w.start()
        for w in workers:
            w.join()
        best = min(best, time.perf_counter() - start)
    return best


for task in (wait, count):
    one = best_time(task, 1)
    two = best_time(task, 2)
    print(f"{task.__name__}: 1 thread {one:.2f} s, 2 threads {two:.2f} s")
