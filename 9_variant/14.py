for p in range(7, 100):
    for x in range(p):
        for y in range(p):
            a = 1 * p ** 2 + 6 * p + 1
            b = 5 * p + 6
            if a * b == 5 * p ** 3 + x * p ** 2 + y * p + 6:
                print(p, y * p + x)
                exit()