l = 1000000
for i in range(1, 1000):
    k = 0
    f = i
    s = ''
    while f > 0:
        s = s + str(f % 3)
        f //= 3
    if i % 2 == 0:
        s = s + s[-2::]
    else:
        for j in range(len(s)):
            k += int(s[j])
        h = ''
        while k > 0:
            h = h + str(k % 3)
            k //= 3
        s = s + h
    if i > 9:
        if int(s,3) == 4:
            print(i)