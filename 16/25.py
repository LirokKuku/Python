from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 5 == 0:
        return n + f(n/5 + 1)
    if n > 5 and n % 5 != 0:
        return n + f(n + 6)

for i in range(1000, 10**10):
    print(f(i), i)