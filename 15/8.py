p = [int(i) for i in range(13, 22)]
q = [int(i) for i in range(17, 31)]
r = [int(i) for i in range(24, 39)]
a = []
for x in range(0,1000):
    f = (not((x in q) <= ((x in p) or (x in r)))) <= ((x not in a) <= (x not in q))
    if f == 0:
        a.append(x)
print(a)