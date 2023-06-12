g = [0] * 3001
f = [0] * 19
for n in range(16):
    if n >= 3210:
        f[n] = 1

for n in range(3001):
    if n < 10:
        g[n] = n
    if n >= 10:
        g[n] = g[n - 3] + 5

print(f[15] - g[3000])