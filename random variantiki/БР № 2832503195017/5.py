for i in range(1, 1000):
    s = bin(i)[2::]
    s = s[::-1]
    while s[0] == '0':
        s = s[1::]
    s = int(s, 2)
    if i < 100 and s == 13:
        print(i)