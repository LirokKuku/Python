P = [int (i) for i in range(2, 21)]
Q = [int (i) for i in range(15, 26)]
A = []
for x in range(0, 1000):
    f = ((x not in A) <= (x not in P)) or (x in Q)
    if f ==0:
        A.append(x)
print(len(A))