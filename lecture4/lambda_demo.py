"""Lambda functions: one expression, no name."""

waypoints = [(3.0, 0.5), (0.5, 0.0), (1.0, 2.0)]  # (x, y), chosen


def by_y(p):
    return p[1]


print(sorted(waypoints, key=by_y))
print(sorted(waypoints, key=lambda p: p[1]))

robots = [
    {"name": "waffle_01", "battery_pct": 87},
    {"name": "burger_02", "battery_pct": 15},
    {"name": "waffle_03", "battery_pct": 52},
]
low_first = sorted(robots, key=lambda r: r["battery_pct"])
print([r["name"] for r in low_first])
print(min(robots, key=lambda r: r["battery_pct"])["name"])
scan = [2.5, 0.0, 3.1, 14.0, 1.2]
print(list(filter(lambda r: 0.12 <= r <= 12.0, scan)))

# A lambda is a function object; its name is <lambda>
rules = [lambda r: r < 0.5, lambda r: "low" if r < 0.5 else "ok"]
print(type(rules[0]).__name__, rules[0].__name__)
print([rule(0.3) for rule in rules])
