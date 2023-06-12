p = [int(x) for x in range(5, 55)]
q = [int(x) for x in range(50, 94)]
for a in range(0, 1000):
    t = True
    for x in range(0, 1000):
        f = (x not in p) and (x in q) <= (x > a)
        if f == 0:
            t = False
            break
    if t:
        print(a)