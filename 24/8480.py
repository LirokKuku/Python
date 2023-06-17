f = open('File/24_8480.txt')
s = f.readline()

kmax = 0
k = 1
for i in range(0, len(s) - 1):
    if s[i] not in 'ABC' or s[i + 1] not in 'ABC':
        k += 1
    else:
        kmax = max(kmax, k)
        k = 1
print(kmax)