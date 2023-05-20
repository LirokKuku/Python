f = open('Files/17_8427.txt')
s = [int(x) for x in f.readlines()]

minn = 10**10
for i in range(len(s)):
    if s[i] % 10 == 3 and len(str(s[i])) == 3:
        minn = min(minn, s[i])

b = []
for i in range(len(s) - 1):
    a = []
    if (len(str(s[i])) == 4 and len(str(s[i + 1])) != 4) or (len(str(s[i])) != 4 and len(str(s[i + 1])) == 4):
        if (s[i]**2 + s[i + 1]**2) % minn == 0:
            a.append(s[i]**2)
            a.append(s[i + 1]**2)
            b.append(a)
print(len(b), sum(max(b)), b)