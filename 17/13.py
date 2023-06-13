f = open('Files/17_13.txt')
s = [int(x) for x in f.readlines()]

maxx = -10**10
for i in range(len(s)):
    if len(str(s[i])) == 2:
        maxx = max(s[i], maxx)


a = []
b = []
for i in range(len(s) - 1):
    a = []
    if (len(str(s[i])) == 2 and len(str(s[i + 1])) != 2) or (len(str(s[i])) != 2 and len(str(s[i + 1])) == 2):
        if (s[i] + s[i + 1]) % maxx == 0:
            a.append(s[i])
            a.append(s[i + 1])
            b.append(a)
print(len(b), sum(max(b)), maxx)