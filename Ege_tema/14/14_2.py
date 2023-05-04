P = {1, 2, 3, 4}
Q = {1, 2, 3, 4, 5, 6}
A = set()
for x in range(1, 1000):
    f = (x not in A) <= ((x not in P) or (x not in Q))
    if f == 0:
        A.add(x)
print((len(A)))
