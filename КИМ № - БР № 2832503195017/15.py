for A in range(1, 1000):
    t = True
    for x in range(1, 1000):
        f = (A % 25 == 0) and (((x % 75 == 0) and (x % 24 == 0)) <= (x % A == 0))
        if not f:
            t = False
            break
        if t:
            print(A)