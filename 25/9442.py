def prost(x):
    if x == 1: return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def E(x):
    a = []
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0 and prost(i):
            a.append(i)
        if x % i == 0 and prost(x // i):
            a.append(x//i)
    if len(a) == 0:
        return 0
    return max(a) - min(a)

k = 0
for x in range(22800, 22800 * 10):
    if E(x) % 47 == 17:
        print(x, E(x))
        k += 1
    if k == 5:
        break