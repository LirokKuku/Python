k = 0
for n in range(1000, 10000):
    a = []
    i = str(n)
    a.append(int(i[0]) * int(i[1]))
    a.append(int(i[1]) * int(i[2]))
    a.append(int(i[2]) * int(i[3]))
    a.sort(reverse=True)
    i = str(a[0]) + str(a[1]) + str(a[2])
    if i == '12106':
        k += 1
print(k)