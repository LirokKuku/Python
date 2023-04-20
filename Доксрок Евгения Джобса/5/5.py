for N in range(1, 10000):
    R = bin(N)[2::]
    if N % 3 == 0:
        R = R + R[-1:-4:-1]
    else:
        N = N * 3
        N = N % 3
        R = R + bin(N)[2::]
    if int(R, 2) < 100:
        print(N)