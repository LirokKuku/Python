p = {2,4,6,8,10,12,14,16,18,20}
q = {5,10,15,20,25,30,35,40,45,50}
a = []
for x in range(0, 1000):
    a.append(x)
    f = ((x in a) <= (x in p)) and ((x in q) <= (not(x in a)))
    if f == 0:
        a.pop(-1)
print(len(a))