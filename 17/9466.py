f = open('Files/17_9466.txt')
s = [int(x) for x in f.readlines()]

maxx = 0
for i in range(len(s)):
    if len(str(s[i])) == 2:
        maxx = max(maxx, s[i])
print(maxx)

a = []
b = []
for i in range(len(s) - 1):
    if len(str(abs(s[i]))) == 2  or len(str(abs(s[i + 1]))) == 2:
        if s[i] + s[i + 1] <= maxx:
            a.append(s[i])
            a.append(s[i + 1])
            b.append(a)
            a = []
print(len(b))
maxx = 0
for i in range(len(b)):
    maxx = max(maxx, b[i][0] + b[i][1])
print(maxx)