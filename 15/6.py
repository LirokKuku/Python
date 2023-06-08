P = [int(i) for i in range(20, 51)]
Q = [int(i) for i in range(10, 61)]
A = []
for x in range(0, 1000):
    A.append(x)
    f = ((x in P) <= (x in A)) and ((x in A) <= (x in Q))
    if f == 0:
        A.pop(-1)
print(len(A))