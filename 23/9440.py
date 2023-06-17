def f(x, y):
    if x > y or x == 35:
        return 0
    if x == y:
        return 1
    if str(x)[0] == '9':
        return f(x + 5, y)
    else:
        return f(x + 5, y) + f(int(str(int(str(x)[0]) + 1) + str(x)[1::]), y)
print(f(30, 60))