minn = 10**10
c = 0
b = 0
d = 0
for n in range(1, 65):
    b = 0
    c = minn
    s = '1' * 33 + '2' * 33 + '3' * n
    while '11' in s or '22' in s or '13' in s or '23' in s:
        s = s.replace('11', '2', 1)
        s = s.replace('22', '1', 1)
        s = s.replace('13', '2', 1)
        s = s.replace('23', '1', 1)
    d += 1
    for i in range(len(s)):
        b += int(s[i])
    print(d, b, n)