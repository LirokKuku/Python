for n in range(0, 10000):
    s = bin(n)[2::]
    if n % 3 == 0:
        s = '10' + s[2::] + '1'
    else:
        s = bin((n % 3) * 2)[2::] + s
    r = int(s, 2)
    if r > 8000:
        print(r)
        break