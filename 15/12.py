def f(x):
    return (a % 12 == 0) and ((530%x == 0) <= ((a%x != 0) < (170%x != 0)))

k = 0
for a in range(1, 1000+1):
    if all(f(x) for x in range(1, 1001)):
        k += 1
print(k)