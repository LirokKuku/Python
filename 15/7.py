p = [int(i) for i in range(12,27)]
q = [int(i) for i in range(30,36)]
a = []
for x in range(0, 1000):
    a.append(x)
    f = (x in a) and ((x not in p) and (x not in q))
    if f != 0:
        a.pop(-1)
print(a)