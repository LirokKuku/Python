p = [int(x) for x in range(40, 46)]
q = [int(x) for x in range(10, 34)]
a = []
for x in range(1, 1001):
    f = (not((x in q) <= (x in a))) <= (x in p)
    if f == 0:
        a.append(x)
print(len(a))