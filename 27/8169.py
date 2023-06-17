f = open('File/27_A_8169.txt')
k = int(f.readline())
n = int(f.readline())
s = [int(x) for x in f.readlines()]

maxx = 0
for i in range(0, n - k):
    for j in range(i + k + 1, n):
        if abs(s[i] - s[j]) % 2 != 0:
            if s[i] % 26 == 0 or s[j] % 26 == 0:
                maxx = max(maxx, s[i] + s[j])
print(maxx)