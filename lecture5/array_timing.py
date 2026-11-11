"""Time one operation on 1,000,000 ranges: a list against an array."""

from timeit import repeat

import numpy as np

N = 1_000_000
rng = np.random.default_rng(605)  # Seeded: the same ranges every run
ranges = rng.uniform(0.12, 12.0, N)  # Meters
ranges_list = ranges.tolist()  # The same numbers, as a list of floats

# Convert every range to centimeters; repeat() times 5 rounds of n
# conversions, and the fastest round, divided by n, is one conversion
n = 10
to_cm = "[r * 100 for r in ranges_list]"
rounds = repeat(to_cm, globals=globals(), number=n)
t_list = min(rounds) / n
rounds = repeat("ranges * 100", globals=globals(), number=n)
t_array = min(rounds) / n
print(f"list:  {t_list * 1e3:7.3f} ms per conversion")
print(f"array: {t_array * 1e3:7.3f} ms per conversion")
print(f"The array is {t_list / t_array:.0f} times faster")
