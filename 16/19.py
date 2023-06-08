f = [0] * 2024
for n in range(2024):
    if n <= 2:
        f[n] = n
    if n > 2:
        f[n] = n + f[n-2]
print(f[2023] + f[2020])