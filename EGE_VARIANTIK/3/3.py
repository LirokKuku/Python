for i in range(1, 10000):
    S = bin(i)[2::]
    if S.count('1') % 2 == 0:
        S = S + '00'
    else:
        S = S + '11'
    R = int(S, 2)
    if R > 114:
        print(i)
        break