f = open('27-B_3231.txt')
N = int(f.readline())
s = list(map(int, f.readlines()))

ps = [0] * N
ps[0] = sum(s[: N//2])
for i in range(1, N):
    ps[i] = ps[i-1] - s[i-1] + s[(i - 1 + N//2) % N]
left = 0
right = 0
for i in range(0, N//2):
    right += i * s[i]
for i in range(1, N//2 + 1):
    left += i * s[N - i]
minsum = left + right
minind = 0
for i in range(1, N):
    right -= ps[i]
    left += ps[(N//2 + i) % N]
    if left + right < minsum:
        minsum = left + right
        minind = i + 1
print(minind)