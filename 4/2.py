minn = 10**10
for n in range(1, 10000):
    s = bin(n)[2::]
    s = s.replace('1', '*')
    s = s.replace('0', '1')
    s = s.replace('*', '0')
    k = int(s, 2)
    r = n - k
    if n % 2 != 0 and r > 37:
        minn = min(minn, n)
print(minn)