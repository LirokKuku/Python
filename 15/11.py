for a in range(1, 1000):
    t = True
    for x in range(1, 1000):
        f = (a % 9 == 0) and ((280 % x == 0) <= ((not(a % x == 0)) <= (not(730 % x == 0))))
        if f == 0:
            t = False
            break
    if t:
        print(a)