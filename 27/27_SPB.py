f = open('File/27A_6638.txt')
n = 100
s = []
for i in f:
    s.append(list(map(int, i.split())))
for i in range(n):
    if s[i][1] % 100 != 0:
        s[i][1] = s[i][1] // 100 + 1
    else:
        s[i][1] = s[i][1] // 100
minn = 10**10
count = 0
for j in range(n):
    summ = 0
    for i in range(1, n):
        summ += abs(s[i][0] - s[0][0]) * s[i][1]
    if summ < minn:
        minn = summ
        count = s[0][0]
    s.append(s[0])
    s.pop(0)
print(minn, count)