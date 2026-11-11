scans_seen = 0


def on_scan(scan):
    scans_seen += 1  # An assignment: scans_seen is local here
    print(f"Scan {scans_seen}: nearest {min(scan)} m")


on_scan([2.5, 0.9])
