for i in range(1, 1000):
    s = bin(i)[2::]
    if i % 2 == 0:
        s = s + '01'
    else:
        s = s+ '10'
    s = int(s, 2)
    if s > 281:
        print(i)
        break