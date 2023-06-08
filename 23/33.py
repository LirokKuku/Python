def f(x, y):
    if x > y or x == 32:
        return 0
    if x == y:
        return 1
    return f(x + 3, y) + f(x + 5, y) + f(x * 2, y)
print(f(4, 16) * f(16, 64))

def f(x, y):
    if x > y or x == 16:
        return 0
    if x == y:
        return 1
    return f(x + 3, y) + f(x + 5, y) + f(x * 2, y)
print(f(4, 32) * f(32, 64))