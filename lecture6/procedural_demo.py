"""A robot as a dictionary, and functions that change it (Lecture 4)."""


def make_robot(name, battery=100):
    return {"name": name, "battery": battery}


def drain(robot, percent):
    robot["battery"] -= percent


scout = make_robot("Scout")
drain(scout, 30)  # 30%: chosen for this example
print(scout)

# Nothing checks a change made outside the functions
scout["battery"] = 150
scout["batery"] = 50  # A typo adds a new key
print(scout)
