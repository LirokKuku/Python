from functools import lru_cache

lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n/2) + 3
    if n > 0 and n % 2 != 0:
        return 2*f(n - 1) + 1

k = 0
for i in range(0, 10000):
    if 1<=f(i)<=1000:
        k += 1
print(k)