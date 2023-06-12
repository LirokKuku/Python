for p in range(1, 1000):
    for x in range(p):
        for y in range(p):
            a = 8 * p ** 3 + 9 * p ** 2 + x * p + 0
            b = x * p ** 3 + 6 * p ** 2 + x * p + 4
            c = 1 * p ** 4 + y * p ** 3 + y * p ** 2 + 1 * p + 4
            if (a + b) == c:
                print(y * p ** 3 + x * p ** 2 + y * p + x)