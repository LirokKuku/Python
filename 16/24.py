from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 4 == 0:
        return n +f(n/2 - 1)
    if n > 5 and n % 4 != 0:
        return n + f(n + 2)
k = 0
for i in range(0, 10**10):
    k += 1
    print(f(i), k, i)