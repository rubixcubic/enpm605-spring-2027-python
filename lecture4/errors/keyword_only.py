def move(distance_m, *, speed_mps=0.2):
    return f"move {distance_m} m at {speed_mps} m/s"


print(move(1.5, 0.1))
