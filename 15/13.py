def f(x):
    return (x & 87 == 0) <= ((x & 31 != 0) <= (x & a != 0))

k = 0
for a in range(1, 1000+1):
    if all(f(x) for x in range(1, 1001)):
        k += 1
print(k)

for a in range(1, 1001):
    t = True
    for x in range(1, 1001):
        f = (x & 87 == 0) <= ((x & 31 != 0) <= (x & a != 0))
        if f == 0:
            t = False
            break
    if t:
        print(a)