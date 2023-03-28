F = [0]*(2025+1)
for n in range(2025+1):
    if n < 3:
        F[n] = n
    if n > 2:
        F[n] = n + 2 * F[n - 1] - F[n - 2]
print(F[2025] - F[2018])