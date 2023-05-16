for i in range(1, 1000):
    k = 0
    c = 0
    s = bin(i)[2::]
    if i % 2 == 0:
        s = '1' + s + '0'
    else:
        s = '11' + s + '10'
    c = s.count('1')
    s = int(s, 2)
    s = str(s)
    for i in range(len(s)):
        k += int(s[i])
    if k > 17:
        print(c)
        break