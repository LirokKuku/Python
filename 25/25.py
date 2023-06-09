b = []
c = []
for i in range(1017, 10**10, 1017):
    b = []
    a = str(i)
    if '9' in a and a[0] == '2' and a[2:6] == '5432' and a[-1] == '1':
        b.append(a)
        b.append(int(a)//1017)
        c.append(b)
print(c)