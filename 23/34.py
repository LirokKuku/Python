k = 0
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if k != 5:
        return f(x + 1, y)
