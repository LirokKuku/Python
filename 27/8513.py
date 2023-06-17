f = open('File/27_A_8513.txt')
k = int(f.readline())
n = int(f.readline())
s = [int(x) for x in f.readlines()]

maxx = 0
for i in range(0, n):
    for j in range(0, n):
        if abs(i - j) > 20:
            maxx = max(maxx, s[i] + s[j])
print(maxx)