"""Time the in operator on a list and on a set of 1,000,000 integers."""

from timeit import repeat

N = 1_000_000
as_list = list(range(N))
as_set = set(as_list)
target = N - 1  # The last item: the worst case for a list

# repeat() times 5 rounds of n checks; keep the fastest round
n = 20
rounds = repeat("target in as_list", globals=globals(), number=n)
t_list = min(rounds) / n
n = 1_000_000  # A set check is fast: many more checks per round
rounds = repeat("target in as_set", globals=globals(), number=n)
t_set = min(rounds) / n
print(f"list: {t_list * 1e6:10.3f} microseconds per check")
print(f"set:  {t_set * 1e6:10.3f} microseconds per check")
print(f"The set is {t_list / t_set:,.0f} times faster")
