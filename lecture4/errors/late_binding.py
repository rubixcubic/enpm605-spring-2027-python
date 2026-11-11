checks = []
for limit in [0.5, 1.0, 2.0]:
    checks.append(lambda r: r < limit)
print(limit, [check(0.8) for check in checks])
