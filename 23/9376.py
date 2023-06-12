def f(x, y):
    if x > y or x == 21:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)
print(f(6, 15) * f(15, 25))
def f(x, y):
    if x > y or x == 15:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)
print(f(6, 21) * f(21, 25))
print(1320 + 1380)