f = open('File/17.txt')
r = [int(x) for x in f.readlines()]

b = []
for i in range(len(r) - 1):
    a = []
    if abs(r[i]) + abs(r[i + 1]) > 17043 and (abs(r[i]) + abs(r[i + 1])) % 3 == 0:
        a.append(r[i])
        a.append(r[i + 1])
        b.append(a)
print(len(b), sum(min(b)))