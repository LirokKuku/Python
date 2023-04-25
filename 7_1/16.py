f = [0] * 31
for n in range(31):
    if n <= 1:
        f[n] = 0
    if n > 1 and n % 2 != 0:
        f[n] = 2 * f[n - 1] + 2
    if n > 1 and n % 2 == 0:
        f[n] = n / 2 + f[n-1]
print(f[30])