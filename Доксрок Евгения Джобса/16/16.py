f = [0] * 2030
for n in range(2029, 0, -1):
    if n >= 2025:
        f[n] = n
    else:
        f[n] = n + 3 + f[n + 3]
print(f[23]-f[21])