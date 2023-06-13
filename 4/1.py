q = [int(x) for x in range(20, 51)]
k = 0
a = list()
for n in range(1, 1001):
    s = bin(n)[2::]
    s = s + str(s.count('1') % 2)
    s = s + str(s.count('1') % 2)
    r = int(s, 2)
    if r in q:
        k += 1
        a.append(r)
print(k, a)