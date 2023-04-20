for n in range(4, 100):
    b = 0
    s = '3' + '5' * n
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '3', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '23', 1)
    for i in s:
        b += int(i)
    if b == 27:
        print(n)
        exit()
