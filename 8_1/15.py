for A in range(52, 53):
    flag = 1
    for x in range(1, 10000000):
        f = (x % A == 0) or ((50 <= x <= 60) <= (x % 13 != 0))
        if not f:
            flag = 0
    if flag:
        print(A)
