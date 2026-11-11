def mean_range(scan):
    total = sum(scan)
    total / len(scan)  # The return is missing


mean = mean_range([2.5, 0.9, 3.1])
print(f"Mean: {mean:.2f} m")
