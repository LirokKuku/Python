p = {1,2,4,8}
q = {1,2,3,4,5,6}
a = []
for x in range(0, 1000):
    f = (x not in a) <= (not((x in p) or (x in q)))
    if f == 0:
        a.append(x)
print(a)