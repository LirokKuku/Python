f = [0] * 48
for n in range(48):
    if n == 0:
        f[n] = 0
    if 1 <= n < 3:
        f[n] = 1
    if n >= 3:
        f[n] = f[n - 1] + f[n - 2]
print(f[47])