"""Where a running Python program keeps things (Reading Material: Memory).

Run from the root of the course repository:

    uv run reading/memory/memory_demo.py

Each section prints a header. id() values change from run to run.
"""

import code
import copy
import gc
import sys
import tracemalloc
import weakref

import numpy as np

print("== Names and namespaces ==")
speed_mps = 0.5  # A global name, in the module's namespace


def drive(distance_m):
    time_s = distance_m / speed_mps  # A local name, in this call's namespace
    print(locals())
    return time_s


print(globals()["speed_mps"])
print(drive(10.0))
print("time_s" in globals())

print("== Two names, one object ==")
battery_pct = 87
level = battery_pct
print(type(battery_pct), id(battery_pct) == id(level), battery_pct is level)

print("== Object sizes ==")
print(sys.getsizeof(87), sys.getsizeof(0.5), sys.getsizeof(""), sys.getsizeof("rover"))
print(sys.getsizeof([]), sys.getsizeof([1, 2, 3]))
print(sys.getsizeof(["a" * 1000, "b" * 1000, "c" * 1000]))

print("== Reference counts ==")
waypoints = [1, 2]
print(sys.getrefcount(waypoints))
route = waypoints
print(sys.getrefcount(waypoints))
del route
print(sys.getrefcount(waypoints))

print("== Immortal objects ==")
print(sys.getrefcount(None), sys.getrefcount(True), sys.getrefcount(1))

print("== Call frames ==")


def g():
    frame = sys._getframe()
    return [
        frame.f_code.co_name,
        frame.f_back.f_code.co_name,
        frame.f_back.f_back.f_code.co_name,
    ]


def f():
    return g()


print(f())
print(sys.getrecursionlimit())


def down(n):
    return down(n + 1)


try:
    down(0)
except RecursionError as error:
    print(error)

print("== Containers hold references ==")
scan = [0.5, 0.7]
history = [scan, scan]
scan.append(0.9)
print(history)

grid = [[0, 0], [0, 0]]
shallow = copy.copy(grid)
deep = copy.deepcopy(grid)
grid[0][0] = 1
print(shallow, deep)
print(shallow is grid, shallow[0] is grid[0], deep[0] is grid[0])

print("== When objects are freed ==")


class Robot:
    pass


rover = Robot()
weakref.finalize(rover, print, "rover freed")
backup = rover
del rover
print("after del rover")
del backup
print("after del backup")

gc.collect()
a = Robot()
b = Robot()
a.partner = b
b.partner = a
weakref.finalize(a, print, "a freed")
del a, b
print("after del a, b")
gc.collect()
print("after gc.collect()")

print("== Small integers and interned strings ==")
x = 256
y = int("256")
print(x is y)
x = 257
y = int("257")
print(x is y, x == y)
name = "rover"
parts = ["ro", "ver"]
built = "".join(parts)  # Built while the program runs
print(name is built, name == built, name is sys.intern(built))

print("== Script versus REPL ==")
first = 257
second = 257
print(first is second)  # One code object: the two 257s are one constant
repl = code.InteractiveInterpreter()
for typed in ["first = 257", "second = 257", "print(first is second)"]:
    repl.runsource(typed)  # Each line compiled on its own, as in the REPL

print("== Measuring memory ==")
tracemalloc.start()
readings = [float(i) for i in range(1_000_000)]
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(sys.getsizeof(readings), current)
array = np.arange(1_000_000, dtype=np.float64)
print(array.nbytes, array.itemsize)
