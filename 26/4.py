f = open('File/26_4.txt')
K = int(f.readline())
N = int(f.readline())
KH = [-1] * (K + 1)
pas = []
for x in f:
    a, b = map(int, x.split())
    pas.append((a, b))
pas.sort()
k = 0
for p in pas:
    for i in range(1, K + 1):
        if KH[i] < p[0]:
            k += 1
            KH[i] = p[1]
            yach = i
            break
print(k, yach)