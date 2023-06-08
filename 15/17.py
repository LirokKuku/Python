for a in range(0, 1001):
    t = True
    for x in range(0, 1001):
        f = ((x % 2 == 0) <= (not(x % 3 == 0))) or (x + a >= 80)
        if f == 0:
            t = False
            break
    if t:
        print(a)