ff = open('27-99a.txt')
N = int(ff.readline())
s = list(map(int, ff.readlines()))

r = 25
cnt = 0
for i in range(N-r):
    for j in range(i+r, N):
        if (s[i] * s[j]) % 9009 == 0 and (s[i] + s[j]) % 4 == 0:
            cnt += 1
print(cnt)