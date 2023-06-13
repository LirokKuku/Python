k = 0
for n in range(1, 1001):
    s = '3' + '0' * 40 + '1' * n + '2' * 40
    while '31' in s or '32' in s or '30' in s:
        if '31' in s:
            s = s.replace('31', '223')
        if '32' in s:
            s = s.replace('32', '23')
        if '30' in s:
            s = s.replace('30', '13')
    s = s.replace('3', '0')
    k = 0
    for i in range(len(s)):
        k += int(s[i])
    b = str(k)
    if len(b) == 3 and b[0] == b[1] == b[2]:
        print(n)
        break