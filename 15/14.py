for a in range(1, 1001):
    t = True
    for x in range(1, 1001):
        f = (x & a != 0) <= ((x & 14 == 0) <= (x & 75 != 0))
        if f == 0:
            t = False
            break
    if t:
        print(a)