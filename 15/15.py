for a in range(0, 1001):
    t = True
    for x in range(0, 1001):
        for y in range(0, 1001):
            f = (3 * x + 2 * y != 90) or ((a > x) and (a > y))
            if f == 0:
                t = False
                break
        if f == 0:
            t = False
            break
    if t:
        print(a)