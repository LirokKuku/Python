for A in range(0, 1000):
    t = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (8 - 2 * y - y ** 2 <= 0) <= ((x**2-11*x + 24 > 0) or (y**2 + x**2 > A))
            if not f:
                t = False
                break
        f = (8 - 2 * y - y ** 2 <= 0) <= ((x**2-11*x + 24 > 0) or (y**2 + x**2 > A))
        if not f:
            t = False
            break
    if t:
        print(A)