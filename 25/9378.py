for i in range(4013, 10**12 + 1, 4013):
    a = str(i)
    if a[0:3] == '123' and a[4] == '4' and a[-4::] == '5679':
        print(i, i // 4013)