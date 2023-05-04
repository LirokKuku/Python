for A in range(0, 300):
    fl = True
    for x in range(0, 300):
        for y in range(0, 300):
            f = ((7 * y + 5 * x) < 1000) or (x < y) or (A < x)
            if f == 0:  # if not f:                fl = False                break        if fl == 1:
                print(A)
                break