def log_calls(func):
    def wrapper(distance_m, speed_mps):  # Fits drive_time() only
        print(f"Calling {func.__name__}")
        return func(distance_m, speed_mps)

    return wrapper


@log_calls
def recharge_time(battery):
    """Minutes to fill the battery at 5% per minute."""
    return (100 - battery) / 5


print(recharge_time(40))
