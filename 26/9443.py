f = open('File/26_9443.txt')
k, n = list(map(int, f.readline().split()))

a = []
b = []
for i in f:
    i = list(map(int, i.split()))
    b.append(i)

b.sort()
a = []
for i in range(len(b)):
    a.append(b[i][1]/b[i][0])
c = a.copy()
c.sort()
d = []
for i in range(n):
    d.append(a.index(c[i]))


e = []
maxx = 0
for i in d:
    e.append(b[i])
    maxx += b[i][0]
print(maxx, max(e))