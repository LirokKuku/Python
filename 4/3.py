minn = 10**10
for n in range(1, 1001):
    s = bin(n)[2::]
    if n % 2 == 0:
        s = '1' +  s + '00'
    else:
        s = s + bin(s.count('1'))[2::]
    r = int(s, 2)
    if n > 8 and r > 88:
        minn = min(minn, r)
        print(n, minn)