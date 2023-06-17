f = open('File/27a_8483.txt')
n = int(f.readline())
k = int(f.readline())
s = [int(x) for x in f.readlines()]

maxx = 0
for i in range(0, n - 2 * k):
    for j in range(i + k + 1, n - k):
        for l in range(j + k + 1, n):
                maxx = max(maxx, s[i] + s[j] + s[l])
print(maxx)