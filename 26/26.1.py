
f = open('File/266.txt')
r = [int(x) for x in f.readlines()]
r = sorted(r)

z = 8358
a = 0
b = []
for i in range(len(r)):
    if a + r[i] > z:
        break
    a += r[i]
print(r[i])
zapas = z - a
for j in range(len(r)):
    if r[j] - r[i - 1] <= zapas:
        itog = [j]
print(itog)