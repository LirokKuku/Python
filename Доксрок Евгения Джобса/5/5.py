for i in range(1, 10000):
    s = bin(i)[2::]
    if i % 3 == 0:
        s = s + s[-1:-4:-1]
    if