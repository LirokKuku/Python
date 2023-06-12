for n in range(0, 100):
    a = 0
    s ='3' * n + '1' * 40 + '2' * 40
    while '23' in s or '12' in s or '32' in s:
        if '12' in s:
            s = s.replace('12', '21', 1)
        if '32' in s:
            s = s.replace('32', '1', 1)
        if '23' in s:
            s = s.replace('23', '2', 1)
    b = str(s)
    for i in range(len(b)):
        a += int(b[i])
    if a == 100:
        print(n)
        break