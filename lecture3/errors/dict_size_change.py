battery = {"robot1": 87, "robot2": 15, "robot3": 42}
for name in battery:
    if battery[name] < 20:
        del battery[name]
