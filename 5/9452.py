c = ''
for n in range(1, 1001):
    s = bin(n)[2::]
    if n % 2 == 0:
        for i in range(len(s)):
            c += s[i] * 2
    else:
        s = s.replace('1', '*')
        s = s.replace('0', '1')
        s = s.replace('*', '0')
        for i in range(len(s)):
            c += s[i] * 2
    r = int(c, 2)
    c = ''
    if r > 60:
        print(n)