"""Pass-by-assignment: a parameter is a new name for the caller's object."""


def show_id(scan):
    print("inside: ", id(scan))


ranges_m = [2.5, 14.0, 3.1]
print("outside:", id(ranges_m))
show_id(ranges_m)


# Changing the object: the caller sees it
def clip_in_place(scan, max_m):
    for i, r in enumerate(scan):
        if r > max_m:
            scan[i] = max_m


# Assigning the parameter: the caller does not see it
def clip_rebind(scan, max_m):
    scan = [min(r, max_m) for r in scan]


ranges_m = [2.5, 14.0, 3.1]
clip_rebind(ranges_m, 12.0)
print(ranges_m)
clip_in_place(ranges_m, 12.0)
print(ranges_m)


# Return a new object instead
def clipped(scan, max_m):
    return [min(r, max_m) for r in scan]


raw = [2.5, 14.0, 3.1]
clean = clipped(raw, 12.0)
print(raw, clean)


# An immutable argument: += makes a new object
def add_charge(pct):
    pct += 10
    return pct


battery_pct = 80  # Chosen for this example
print(add_charge(battery_pct), battery_pct)
