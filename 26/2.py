f = open('File/26_2.txt')
S, N = map(int, f.readline().split())
a = list(map(int, f.readlines()))
a.sort()
summ = 0
k = 0
b = []
for x in a:
    if summ + x <= S:
        k += 1
        summ += x
        file = x
    else:
        b.append(x)
ost = S - summ + file
for x in b:
    if x <= ost:
        big = x
print(k, big)