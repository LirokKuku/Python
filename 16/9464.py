f = [3002, 3001]
a, b = 0, 0
c = 3001
for i in range(2, 3003):
    c -= 1
    f.append(f[i - 2] + 2)
    if c == 43:
        a = f[i]
    if c == 40:
        b = f[i]
print(b - a)