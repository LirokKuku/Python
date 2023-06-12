for i in range(1, 1000):
    a = bin(i)[2::]
    if i % 3 == 0:
        a = a + '010'
    else:
        a = a + bin((i % 3) * 5)[2::]
    r = int(a, 2)
    if r > 300:
        print(i)
        break