for N in range(4, 100):
    R = bin(N)[2::]
    if N % 3 == 0:
        R = R + R[-3::]
    else:
        R = R + bin(3*(N%3))[2::]
    R = int(R, 2)
    if R < 100:
        print(N)