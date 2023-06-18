f = open('File/24_9471.txt')
s = f.readline()

a = s[0]
b = []
for i in range(1, len(s) - 1):
    if s[i] != s[i + 1]:
        a += s[i]
    else:
        b.append(a)
        a = s[i]

maxx = 0
for i in b:
    maxx = max(maxx, len(i))
print(maxx)