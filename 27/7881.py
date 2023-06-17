f = open('File/27A_7881.txt')
n = int(f.readline())
k = int(f.readline())
s = [int(x) for x in f.readlines()]
print(n,k,len(s))
count = 0
for i in range(0, n - 1):
    if i + k < n:
        for j in range(1, k + 1):
            if abs(s[i] - s[i + j]) % 100 == 0:
                if (s[i] % 37 == 0 and s[i + j] % 37 != 0) or (s[i] % 37 != 0 and s[i + j] % 37 == 0):
                    count += 1
    else:
        for j in range(i + 1, n):
            if abs(s[i] - s[j]) % 100 == 0:
                if (s[i] % 37 == 0 and s[j] % 37 != 0) or (s[i] % 37 != 0 and s[j] % 37 == 0):
                    count += 1
print(count)