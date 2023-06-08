s = '0' + '1' * 20 + '2' * 18 + '3' * 15
while '01' in s or '02' in s or '03' in s:
    if '01' in s:
        s = s.replace('01', '2203')
        print(s)

    if '02' in s:
        s = s.replace('02', '20')
        print(s)

    if '03' in s:
        s = s.replace('03', '1102')
        print(s)

print(s.count('1') + (s.count('2') * 2) + (s.count('3') * 3))