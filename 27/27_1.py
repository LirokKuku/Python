f = open('File/27_T.txt')
n = f.readline()
s = []
for i in f:
    s.append(list(map(int, i.split())))
summ = 0
minn = 10**10
for i in range(len(s)):
    summ += max(s[i])
    if abs(s[i][0] - s[i][1]) % 17 != 0:
        minn = min(minn, abs(s[i][0] - s[i][1]))
print(summ, summ % 17, minn)