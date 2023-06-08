alf = '012'
def f(x, k):
    s = ''
    while x > 0:
        s = alf[x%k] + s
        x //= k
    return s
for n in range(1, 1000):
    b = f(n, 3)
    c = b
    b = b + b[-1]
    b = b + str((c.count('1') + c.count('2') * 2) % 3)
    b = b + str((b.count('1') + b.count('2') * 2) % 3)
    r = int(b, 3)
    if r > 136:
        print(n)
        break