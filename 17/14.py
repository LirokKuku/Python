f = open('Files/17_14.txt')
s = [int(x) for x in f.readlines()]

maxx = 0
for i in range(len(s)):
    if abs(s[i]) % 570 == 0:
        maxx = max(maxx, abs(s[i]))


a = []
b = []
for i in range(len(s) - 3):
    a = []
    if (s[i] + s[i + 1] + s[i + 2] + s[i + 3])/4 > maxx:
        a.append(s[i])
        a.append(s[i + 1])
        a.append(s[i + 2])
        a.append(s[i + 3])
        b.append(a)

c = []
for i in range(len(s) - 2):
    a = []
    if (s[i] > 0 and s[i + 1] > 0) or (s[i + 1] > 0 and s[i + 2] > 0) or (s[i] > 0 and s[i + 2] > 0):
        if (s[i] + s[i + 1] + s[i + 2]) % 34 == 0:
            a.append(s[i])
            a.append(s[i + 1])
            a.append(s[i + 2])
            c.append(a)
print(len(b), len(c))