def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n > 3:
        return f(n-3) + f(n-2) + f(n-1)
print(f(11))