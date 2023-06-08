for a in range(0, 1001):
    t = True
    for x in range(0, 1001):
        for y in range(0, 1001):
            f = (x ** 2 - 11 * x + 28 > 0) or (y ** 2 - 9 * y + 14 > 0) or (x ** 2 + y ** 2 > a)
            if f == 0:
                t = False
                break
        if f == 0:
            t = False
            break
    if t:
        print(a)