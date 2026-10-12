"""if, elif, else, conditional expressions, and nested conditions."""

battery_pct = 15  # Chosen for this example

# if
if battery_pct < 20:
    print("Battery low")
print("Checked the battery")

# if and else
if battery_pct >= 20:
    print("Continue the mission")
else:
    print("Return to the dock")

# if, elif, and else
if battery_pct >= 80:
    level = "full"
elif battery_pct >= 50:
    level = "moderate"
elif battery_pct >= 20:
    level = "low"
else:
    level = "critical"
print(f"Battery level: {level}")

# Conditional expression
mode = "charge" if battery_pct < 20 else "explore"
print(mode)

# Nested conditions
obstacle_ahead = True
if battery_pct >= 20:
    if obstacle_ahead:
        print("Plan a path around the obstacle")
    else:
        print("Drive forward")
else:
    print("Stay at the dock")
