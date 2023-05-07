F = [0] * 72
for n in range(72):
    if n < 3:
        F[n] = 1
    if n > 2 and n % 2 == 0:
        F[n] = F[n - 2] - F[n - 1]
    if n > 2 and n % 2 != 0:
        F[n] = 3 * F[n - 1] - F[n - 2]
b = F[71]
b = str(b)
s = 0
for i in range(len(b)):
    s += int(b[i])
print(s)